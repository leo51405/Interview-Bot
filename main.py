import google.generativeai as genai
from typing import List

# Set up Gemini API key
GOOGLE_API_KEY = "AIzaSyD8d8foqTNUDIn4COLFnFre-cDkWdWbWdI"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')


def build_prompt(job_title: str, language: str) -> str:
    return (
        f"你是一位資深面試官，正在面試一位應徵 {job_title} 的候選人。\n"
        f"請提供 3 個技術問題、1 個行為問題、1 個情境題。\n"
        f"每個問題請用數字開頭（例如 1. 2. 3.），一個問題最多兩行。\n"
        f"問題請以 {language} 呈現，問題應具挑戰性且貼近實務，"
        f"避免給出範例答案或解釋，只需列出問題本身。\n"
    )

def generate_questions(job_title: str, language: str = "繁體中文") -> List[str]:
    prompt = build_prompt(job_title, language)
    response = model.generate_content(prompt)
    raw = response.text.strip()

    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    return "\n".join(lines)

print(generate_questions("資料科學家","中文"))