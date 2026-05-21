from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI 
load_dotenv()

def main():
    print("Hello from langchain-course!")
    print("Your OpenAI API key is:", os.environ.get("OPENAI_API_KEY"))

    llm = ChatOpenAI(temperature=0.9, model="gpt-3.5-turbo")
    response = llm.invoke("What is the capital of France?")
    print(response.content)


if __name__ == "__main__":
    main()
