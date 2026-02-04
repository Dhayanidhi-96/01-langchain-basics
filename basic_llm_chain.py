"""
Basic LLM Chain - Day 1
Purpose: Understand how LangChain wraps LLM calls (Google Gemini)
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from dotenv import load_dotenv
import os

load_dotenv()

# -------------------------------
# Test 1: Basic Gemini LLM call
# -------------------------------
def test_gemini():
    """Test basic Google Gemini chat"""
    print("Testing Google Gemini...")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )

    response = llm.invoke("Explain LangChain in one sentence")
    print(f"Response: {response.content}\n")

    return response.content


# ---------------------------------------
# Test 2: Prompt template + chain
# ---------------------------------------
def basic_chain_example():
    """Create a simple chain with prompt template"""
    print("Creating basic chain with Gemini...")

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant that explains technical concepts simply."),
        ("user", "{topic}")
    ])

    llm = ChatGoogleGenerativeAI(
        model= "gemini-2.5-flash",
        temperature=0.7,
        convert_system_message_to_human= True
    )

    chain = prompt | llm | StrOutputParser()

    response = chain.invoke({"topic": "What is a vector database?"})
    print(f"Chain Response: {response}\n")

    return response


# ---------------------------------------
# Test 3: Multi-turn conversation (memory)
# ---------------------------------------
def multi_turn_conversation():
    """Demonstrate conversational memory with Gemini"""
    print("Multi-turn conversation example with Gemini...")

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7,
        convert_system_message_to_human= True
    )

    conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )

    response1 = conversation.predict(
        input="Hi, I am learning LangChain"
    )
    print(f"Turn 1: {response1}\n")

    response2 = conversation.predict(
        input="What did I just say I was learning?"
    )
    print(f"Turn 2: {response2}\n")

    return conversation


# ---------------------------------------
# Main execution
# ---------------------------------------
if __name__ == "__main__":
    print("=== LangChain Basics - Day 1 (Google Gemini) ===\n")

    test_gemini()
    basic_chain_example()
    multi_turn_conversation()

    print("✅ All tests completed!")
