import os
from core.prompt_runner import run_all

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    leads_path = os.path.join(base_dir, "data", "leads.json")
    prompt_path = os.path.join(base_dir, "data", "prompt.json")
    output_dir = os.path.join(base_dir, "outputs")

    run_all(
        leads_path=leads_path,
        prompt_path=prompt_path,
        output_dir=output_dir
    )