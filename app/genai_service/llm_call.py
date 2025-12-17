# genai_service/llm_call.py

from app.configs.config import settings
from google import genai

from app.prompts.text_prompt import build_single_prompt
from app.data_ingestion.preprocess_data import encoded_tax_data


class LLMService:
    """
    LLM service using Gemini 2.5 Flash with a single unified prompt string.
    """

    def __init__(self):
        self.client = genai.Client(api_key=settings.GOOGLE_API_KEY)

    def get_response(self, user_question: str) -> str:
        user_question = (user_question or "").strip()
        if not user_question:
            return "Please provide a valid question."

        # Build one monolithic prompt: instructions + data + question
        prompt = build_single_prompt(user_question, encoded_tax_data)

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config={
                "temperature": 0.2,
                "max_output_tokens": 1024,
            },
        )

        text = getattr(response, "text", None)
        if not text:
            return "I could not generate an answer from the model."

        return text.strip()


llm_service = LLMService()


if __name__ == "__main__":
    answer = llm_service.get_response("How many properties have pending tax?")
    print(answer)
