# 🦜 LangChain Basics - Day 1

Part of my **90-day Gen AI mastery journey**. Learning LangChain fundamentals and building my first LLM chains.

## 🎯 Learning Goals

-✅ Set up LangChain environment
-✅ Understand LLM wrappers (OpenAI, Gemini)
-✅ Create basic chains with prompt templates
-✅ Experiment with temperature and few-shot learning
-✅ Build conversational chains with memory

## 🚀 What I Built

### 1. Basic LLM Chain (`basic_llm_chain.py`)
Simple chains connecting prompts → LLMs → outputs
-Tested both OpenAI GPT-4o and Google Gemini
-Created prompt templates
-Implemented conversational memory

### 2. Experiments (`experiments.py`)
Hands-on exploration of:
-**Temperature effects** (0.0 vs 1.0)
-**Few-shot prompting** (teaching by example)
-**Chain composition** (sequential chains)

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/01-langchain-basics.git
cd 01-langchain-basics

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Add your API keys to .env
## 🔑 Environment Setup

Create `.env` file:

```
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

## ▶️ Usage

Run basic examples:

```bash
python basic_llm_chain.py
```

Run experiments:

```bash
python experiments.py
```

## 📸 Demo

### Temperature Comparison

```
Temperature 0.0: "HydroTrack Smart Bottle"
Temperature 0.5: "AquaSync Intelligent Hydration"
Temperature 1.0: "SipSense - The Mindful Water Companion"
```

### Chain Composition

```
Category: fitness for seniors
Product: "GentleMove - A low-impact exercise platform..."
Tagline: "Stay Active, Stay Vibrant - Movement Designed for You"
```

## 📚 What I Learned

1. **LangChain simplifies LLM interactions** - No need to manage raw API calls
2. **Prompt templates are reusable** - Define once, use many times
3. **Temperature matters** - Low for factual, high for creative tasks
4. **Chains enable complex workflows** - Sequential processing made easy
5. **Memory enables conversations** - Context preservation across turns

## 🔜 Next Steps (Day 2)

- Document loaders for PDFs and text files
- Text splitters for long documents
- Building a PDF summarizer
- Chain types (Sequential, Transform, Router)

## 🛠️ Tech Stack

- **LangChain** - LLM orchestration framework
- **OpenAI GPT-4o** - Primary LLM
- **Google Gemini** - Alternative LLM
- **Python 3.10+** - Programming language

## 📝 Notes

- Keep API calls minimal during experimentation (costs)
- Always use environment variables for keys
- Test with both models to understand differences
- Document learnings immediately (memory fades!)

## 📬 Connect

Building in public! Follow my journey:
- **LinkedIn**: https://www.linkedin.com/in/dhayanidhi-p-3372b0291/
- **GitHub**: https://github.com/Dhayanidhi-96
- **Twitter/X**: https://x.com/p_dhayanid42210

---
