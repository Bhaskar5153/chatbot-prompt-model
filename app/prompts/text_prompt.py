# app/prompts/text_prompt.py

from textwrap import dedent


def build_single_prompt(user_question: str, encoded_base64_data: str) -> str:
    """
    Build a single unified prompt string that:
    - Explains the task
    - Embeds the dataset (base64-encoded CSV)
    - Uses a chain-of-thought style instruction (internally)
    - Asks the model to answer without revealing its reasoning steps
    """

    prompt = dedent(f"""
    You are an assistant that answers questions strictly based on a tax dataset
    from Khazipur (DCB). The dataset is provided below as a base64-encoded CSV.

    DATASET (BASE64-ENCODED CSV):
    --- BEGIN DATA ---
    {encoded_base64_data}
    --- END DATA ---

    The dataset may contain columns such as (examples, actual columns may differ):
    - Ward, Village, Property ID
    - Owner Name
    - Tax Amount, Paid Amount, Pending Amount
    - Scheme, Year, Category, etc.

    Your job is to:
    - Decode and conceptually parse this base64 CSV as a table.
    - Use ONLY this dataset to answer questions.
    - Never invent or guess values that are not supported by the data.
    - If the dataset does not clearly support an answer, say:
      "The dataset does not contain enough information to answer this."

    CHAIN-OF-THOUGHT STYLE INSTRUCTIONS (INTERNAL, DO NOT EXPOSE STEPS VERBATIM):
    1. Carefully read the user question.
    2. Infer which columns and rows of the dataset are relevant.
    3. Silently perform any necessary operations:
       - filtering (e.g., by ward, village, scheme)
       - counting rows (e.g., number of properties with pending tax)
       - summing amounts (e.g., total pending tax for a ward or village)
       - grouping or aggregating as needed.
    4. Formulate a clear, concise final answer.
    5. Do NOT output the intermediate reasoning steps; only output the final answer
       and a brief explanation grounded in the data (e.g., referencing column names).

    USER QUESTION:
    {user_question}

    INSTRUCTIONS FOR THE FINAL ANSWER:
    - Answer in a concise, structured way (bullets or short paragraphs).
    - Base everything explicitly on the dataset above.
    - If the answer cannot be determined from the dataset, state that clearly.
    - Do not mention that you are using base64 or internal reasoning instructions;
      just answer as a data-aware assistant.
    """).strip()

    return prompt
