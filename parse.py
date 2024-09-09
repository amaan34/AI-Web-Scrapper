# Download Ollama
# Ollama allows you to run Open Source LLM's Locally on your own computer
# You can download different models of Ollama by first Downloading Ollama and then going to their GitHub and choosing what model best suits your computer
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = {
    "You are tasked with extracting specific information from the folllowing text content: {dom_content}"
    "Please follow these intructions carefully: \n\n"
    "1. **Extract Information:** Only extract information that directly matches the provided description: {parse_description}"
    "2. **No Extra Content:** Do not include any additional text, comments, or explanation in your response. "
    "3. **Empty Response:** If no information matches the description, return an empty string('')."
    "4. **Direct Data Only:** Your output should contain only the data that is explicitly requested, with no other text"
}

model = OllamaLLM(model="moondream")

def parse_with_ollama(dom_chunks, parse_description):
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model 

    parsed_results = []

    for i, chunk in enumerate(dom_chunks, start=1):
        response = chain.invoke(
            {"dom_content": chunk, "parse_description": parse_description}
        )
        print(f"Parsed Batch {i} of {len(dom_chunks)}")
        parsed_results.append (response)
    return "\n".join(parsed_results)