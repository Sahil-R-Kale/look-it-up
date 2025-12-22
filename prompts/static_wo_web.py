# Prompt used for the static split without web search

PROMPT_STATIC_WO_WEB = '''You are an expert at answering questions based on provided context.

Given the following question, provide concise and very to-the-point answer in JSON format. Also provide a confidence score between 0 and 1 for your answer, representing how confident you are in your factual knowledge that led to the answer.

No explanation is needed, just the precise answer and confidence with minimal information to answer the question. Make sure that each answer provides only concise factual answers with no extra details at all. The answer should be based on your knowledge, not fabricated.'''