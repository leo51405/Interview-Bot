import google.generativeai as genai
from typing import List

# Set up Gemini API key
GOOGLE_API_KEY = "AIzaSyD8d8foqTNUDIn4COLFnFre-cDkWdWbWdI"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash')

# 題庫作為風格示範資料庫
QUESTION_BANK = {
    "資料科學家": {
        "繁體中文": [
            "請解釋 bias-variance tradeoff 是什麼?它為何重要?",
            "假設你在處理一個高度不平衡的分類問題，你會採用哪些策略?",
            "什麼情況下你會選擇使用隨機森林而不是邏輯回歸?",
            "請描述你過去如何使用資料來驅動業務決策的案例。",
            "你如何評估一個預測模型是否適合實際部署?",
            "如果你的模型準確率為 95%，你怎麼說服老闆它還不夠好?",
            "請解釋 A/B test 與多變量測試的差異。",
            "如何處理有許多缺失值與異常值的資料集?請舉例。",
            "你遇過資料偏誤(data bias)嗎?是怎麼發現並修正的?",
            "當你的模型在 training 表現良好但在 production 出現問題時，你會怎麼處理?"
        ],
        "英文": [
            "Please explain what the bias-variance tradeoff is and why it matters.",
            "Suppose you're dealing with a highly imbalanced classification problem. What strategies would you use?",
            "In what situations would you choose random forest over logistic regression?",
            "Describe a case where you used data to drive a business decision.",
            "How do you evaluate whether a predictive model is ready for deployment?",
            "If your model has 95% accuracy, how would you convince your boss that it’s not good enough?",
            "Explain the difference between A/B testing and multivariate testing.",
            "How do you handle datasets with many missing or anomalous values? Give an example.",
            "Have you ever encountered data bias? How did you detect and correct it?",
            "If your model performs well in training but poorly in production, what steps would you take?"
        ]
    },
    "數據分析師": {
        "繁體中文": [
            "請描述你過去如何運用 SQL 從大型資料庫中擷取重要資訊。",
            "什麼是 cohort analysis?在什麼場景下會使用它?",
            "你會如何處理一個充滿類別型變數的資料集?",
            "你曾經做過哪些儀表板?你如何決定 KPI 呈現方式?",
            "假設某產品銷售下滑，你會怎麼用資料來找出原因?",
            "在處理時間序列資料時，會注意哪些陷阱?",
            "你怎麼解釋 p-value?它在 A/B test 中的角色是什麼?",
            "當老闆要求明天交出數據報告，但你資料還不完整時怎麼辦?",
            "怎麼從原始資料轉化出有洞見的商業分析?請舉例。",
            "你遇過最難處理的髒資料是什麼?你是如何清理的?"
        ],
        "英文": [
            "Describe how you've used SQL to extract insights from a large database.",
            "What is cohort analysis, and in what scenario would you use it?",
            "How would you handle a dataset with many categorical variables?",
            "What dashboards have you built, and how did you decide which KPIs to show?",
            "Suppose product sales are declining—how would you use data to find out why?",
            "What are the common pitfalls in working with time series data?",
            "How do you explain the concept of a p-value, and what role does it play in A/B testing?",
            "What would you do if your boss asked for a report tomorrow but the data is incomplete?",
            "How do you convert raw data into business insights? Please give an example.",
            "Describe the most difficult dirty data you've encountered and how you cleaned it."
        ]
    },
    "機器學習工程師": {
        "繁體中文": [
            "請說明你對 model deployment 的經驗與流程。",
            "在選擇神經網絡架構時，你通常考量哪些因素?",
            "請解釋 batch size 的選擇會如何影響訓練過程。",
            "你是如何處理模型過擬合問題的?",
            "如何評估模型 drift?你有哪些監控策略?",
            "當需要處理數百萬筆資料進行模型訓練，你會怎麼做?",
            "請解釋什麼是 transfer learning?什麼情況適合使用?",
            "請說明在實務上使用過的 CI/CD 工具來部署模型的經驗。",
            "你有實作過推薦系統嗎?請說明架構與演算法選擇。",
            "在處理語音/影像/時間序列資料時，模型設計有何不同?"
        ],
        "英文": [
            "Describe your experience with model deployment and the steps involved.",
            "What factors do you usually consider when choosing a neural network architecture?",
            "How does the choice of batch size affect the training process?",
            "How do you handle model overfitting?",
            "How do you detect and respond to model drift? What monitoring strategies do you use?",
            "How would you handle training a model with millions of records?",
            "What is transfer learning, and when is it appropriate to use?",
            "Explain your experience using CI/CD tools to deploy models in production.",
            "Have you implemented a recommendation system? Describe its architecture and algorithm choices.",
            "How does model design differ when working with audio, image, or time series data?"
        ]
    },
    "通用": {
        "繁體中文": [
            "你為什麼想加入我們公司?",
            "你覺得你最大的優點與缺點是什麼?",
            "當你和同事意見不合時你會怎麼做?",
            "描述你面對困難任務時的處理方式。",
            "你如何安排工作優先順序?",
            "你最挫折的一次經驗是什麼?",
            "在上一份工作中，你主要負責什麼工作?／最有成就感的事是什麼?",
            "你離開上一份工作的原因是什麼?",
            "碰到完全沒接觸過的領域時，你會怎麼做?",
            "比起別人，你的優勢是什麼?"
        ],
        "英文": [
            "Why do you want to join our company?",
            "What are your greatest strengths and weaknesses?",
            "How do you handle disagreements with colleagues?",
            "Describe how you handle a difficult or challenging task.",
            "How do you prioritize your tasks at work?",
            "What was your most frustrating experience?",
            "What were your main responsibilities in your last job, and what are you most proud of?",
            "Why did you leave your last job?",
            "What would you do when facing a domain you've never worked in before?",
            "Compared to others, what is your biggest advantage?"
        ]
    }
}

def build_prompt(job_title: str, language: str) -> str:
    examples = QUESTION_BANK.get(job_title, QUESTION_BANK["通用"])
    example_block = "\n".join(examples)
    return (
        f"你是一位資深面試官，正在面試一位應徵 {job_title} 的候選人。\n"
        f"以下是你出題風格的範例題:\n{example_block}\n\n"
        f"請依照相同風格再出 3 題，"
        f"每個問題最多兩行，請用 {language} 呈現，"
        f"不要給出答案或解釋。"
    )

def generate_questions(job_title: str, language: str) -> str:
    prompt = build_prompt(job_title, language)
    response = model.generate_content(prompt)
    raw = response.text.strip()

    lines = [line.strip() for line in raw.splitlines() if line.strip()]
    # return "\n".join(lines)
    return lines


def build_feedback_prompt(question: str, answer: str, language: str = "繁體中文") -> str:
    return (
        f"你是一位資深面試官，正在進行模擬面試。\n"
        f"以下是應徵者的作答內容，請針對這個問題進行回饋:\n\n"
        f"問題:{question}\n"
        f"回答:{answer}\n\n"
        f"請從三個面向進行評分(每項 1~5 分):\n"
        f"1. 技術深度\n"
        f"2. 表達清晰度\n"
        f"3. 問題理解能力\n\n"        
        f"請用 {language} 回覆，並且總結建議限制100字內，格式如下:\n"
        f"技術深度:X分\n"
        f"表達清晰度:X分\n"
        f"問題理解能力:X分\n"
        f"總結建議:......"
        f"請嚴格遵從上面的格式。"
    )

def evaluate_answer(question: str, user_answer: str, language: str = "繁體中文") -> str:
    prompt = build_feedback_prompt(question, user_answer, language)
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ GPT 回應失敗：{e}"


# 測試輸出
def interview_round(question: str, language: str = "繁體中文") -> dict:
    print(f"問題:{question}")
    user_answer = input("請輸入你的回答:\n")
    feedback = evaluate_answer(question, user_answer, language)
    return {
        "question": question,
        "answer": user_answer,
        "feedback": feedback
    }

# 測試輸出
def interview_session(job_title: str, language: str = "繁體中文", num_questions: int = 3):
    questions = generate_questions(job_title, language)
    print(f"🎯 模擬面試開始：{job_title}（共 {num_questions} 題）\n")
    results = []
    for i in range(min(num_questions, len(questions))):
        print(f"\n--- 第 {i+1} 題 ---")
        result = interview_round(questions[i], language)
        print("\n📝 GPT 回饋：")
        print(result["feedback"])
        results.append(result)
    print("\n✅ 模擬面試結束！\n")
    return results

# 主程式啟動點
if __name__ == "__main__":
    job = input("請輸入職缺名稱（例如：資料科學家）：")
    lang = input("請選擇語言（例如：繁體中文 或 英文）：")
    interview_session(job, language=lang, num_questions=2)
