"""
LangChain Experiments - Day 1
Try different prompts, temperatures, and chain types
"""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate, FewShotPromptTemplate, PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

# def temperature_experiments():
#     """Compare responses at different temperatures"""
#     print("=== Temperature Experiments (Gemini) ===\n")

#     prompt = ChatPromptTemplate.from_template(
#         "Write a creative product name for: {product_description}"
#     )

#     temperature = [0.0, 0.5, 1.0]

#     for temp in temperature:
        
#         llm = ChatGoogleGenerativeAI(
#             model= "gemini-2.5-flash",temperature=temp
#         )
#         chain = prompt|llm|StrOutputParser()

#         response = chain.invoke({
#             "product_description": "a smart water bottle that tracks hydration"}
#             )
#         print(f"Temperature {temp}:{response}\n")

# def few_shot_learning():
#     """Demonstrate few-shot prompting"""
#     print("=== Few-Shot Learning (Gemini) ===\n")

#     examples = [
#         {"input": "happy", "output": "😊"},
#         {"input": "sad", "output": "😢"},
#         {"input": "excited", "output": "🎉"}
#     ]

#     example_prompt = PromptTemplate(
#         input_variables=["input","output"],
#         template="Emotion: {input}\nEmoji: {output}"
#     )

#     few_shot_prompt = FewShotPromptTemplate(
#         examples=examples,
#         example_prompt = example_prompt,
#         prefix="convert emotions to emojis:",
#         suffix= "Emotion: {emotion}\nEmoji:",
#         input_variables=["emotion"]
#     )

#     llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature= 0)
#     chain = few_shot_prompt|llm| StrOutputParser()

#     test_emotions = ["surprised", "angry", "confused"]

#     for emotion in test_emotions:
#         response = chain.invoke({"emotion":emotion})
#         print(f"{emotion} → {response}")


def chain_composition():
    print("\n=== Chain Composition (Gemini) ===\n")

    idea_prompt = ChatPromptTemplate.from_template(
        "Generate a one-sentence product idea for: {category}"
    )

    tagline_prompt = ChatPromptTemplate.from_template(
        "Create a catchy marketing tagline for this product:\n{product_idea}"
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.8)
    
    # Fixed: Added () to the parsers
    idea_chain = idea_prompt | llm | StrOutputParser()
    tagline_chain = tagline_prompt | llm | StrOutputParser()

    category = "fitness for seniors"

    product_idea = idea_chain.invoke({"category": category})
    tagline = tagline_chain.invoke({"product_idea": product_idea})

    print(f"Category: {category}")
    print(f"Product Idea: {product_idea}")
    print(f"Tagline: {tagline}\n")

if __name__ == "__main__":
    # temperature_experiments()
    # few_shot_learning()
    chain_composition()

    print("✅ Gemini Experiments completed!")