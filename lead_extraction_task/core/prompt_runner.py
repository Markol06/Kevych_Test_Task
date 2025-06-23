import json
import os

from openai import OpenAI

from core import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_TEMPERATURE

def load_prompt(path: str) -> str:
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['base_prompt']

def load_leads(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def call_openai(prompt: str) -> dict:
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=OPENAI_TEMPERATURE
    )
    content = response.choices[0].message.content.strip()

    if content.startswith("```json"):
        content = content.removeprefix("```json").strip()
    if content.endswith("```"):
        content = content.removesuffix("```").strip()

    try:
        return json.loads(content)
    except Exception:
        return {"error": "Invalid JSON response", "raw": content}

def save_output(output: dict, path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

def run_all(leads_path: str, prompt_path: str, output_dir: str) -> None:
    leads = load_leads(leads_path)
    base_prompt = load_prompt(prompt_path)
    os.makedirs(output_dir, exist_ok=True)
    for key, text in leads.items():
        full_prompt = f"{base_prompt}{text}"
        result = call_openai(full_prompt)
        save_output(result, os.path.join(output_dir, f"{key}.json"))