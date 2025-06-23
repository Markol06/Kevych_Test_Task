AI Specialist Test Task – Prompt Engineering Evaluation

This project explores prompt engineering with GPT-4o to extract structured lead data from unstructured input and define a human-like chatbot tone for the healthcare domain.

Task 1: Lead Extraction (Structured Output)

Design a single universal prompt that extracts both factual and inferred fields about a company from a block of text. The model must return valid JSON, always with the same structure.

Task 2: Chatbot Tone Definition
Define a system prompt that gives the chatbot a friendly, natural, and ethical tone suitable for general healthcare conversations. The assistant:

- [x] Never provides diagnosis

- [x] Sounds like a helpful human

- [x] Uses verbal fillers and empathy

- [x] Is safe and non-prescriptive

📁 Project Structure
```text
Kevych Test Task/
├── lead_extraction_task/
│   ├── core/
│   │   ├── config.py               # Loads env and model settings
│   │   └── prompt_runner.py        # Main logic to run prompt and save outputs
│   ├── data/
│   │   ├── leads.json              # 3 lead examples
│   │   └── prompt.json             # Lead extraction prompt
│   ├── outputs/
│   │   └── lead1.json ...          # Saved results
│   └── main.py                     # Entry point for Task 1
├── chatbot_tone_task/
│   └── chatbot_tone.json           # Human-like tone definition for LLM
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/Markol06/Kevych_Test_Task.git
cd Kevych_Test_Task
```
### 2. Set up environment variables
Create your .env file:
```bash
cp .env.example .env
```
Then add your OpenAI API key:
```bash
OPENAI_API_KEY=your_openai_key_here
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run Task 1 (lead extraction)
(You can check the results in outputs/lead...json)
```bash
python lead_extraction_task/main.py  
```
