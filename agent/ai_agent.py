from core.prompts import build_prompt
from core.config import OPENAI_API_KEY
from utils.logger import log_query
from agent.tools import analyze_salary
import openai

openai.api_key = OPENAI_API_KEY


class AIAgent:

    def __init__(self):
        pass

    def call_llm(self, prompt):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"

    def decide_tool(self, query):
        if "salary" in query.lower():
            return "salary_tool"
        return "llm_only"

    def process_query(self, query):
        tool = self.decide_tool(query)

        if tool == "salary_tool":
            context = analyze_salary()
        else:
            context = ""

        prompt = build_prompt(query, context)
        response = self.call_llm(prompt)

        log_query(query, response)
        return response
