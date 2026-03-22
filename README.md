# SonicCyclops Agent-Driven Programming Philosophy Quiz

A dynamic assessment where **SonicCyclops generates code examples and scenarios in real-time** based on Nathan's responses, allowing for deep exploration of programming preferences and decision-making patterns.

## 🔥 What Makes This Different

Instead of static multiple choice questions, this quiz features:

- **Live code generation** - SonicCyclops creates specific examples tailored to your responses
- **Dynamic follow-ups** - Agent digs deeper when you give interesting answers  
- **Real scenarios** - Concrete architectural decisions, not abstract preferences
- **Critique-driven** - You nitpick actual code, revealing true preferences
- **Context-aware** - Each question builds on your previous responses

## 🚀 Quick Start

### 1. Ensure SonicCyclops Agent is Running

**Option A: Local Ollama**
```bash
ollama serve
# Should have nemotron-cascade-2 or similar model loaded
```

**Option B: OpenClaw Gateway**
```bash
# OpenClaw gateway should be running on localhost:18789
```

**Option C: Custom Endpoint**
```bash
export SONICCYCLOPS_ENDPOINT=http://your-agent-endpoint
```

### 2. Run the Agent-Driven Quiz

```bash
git clone https://github.com/soniccyclops-bot-collab/programming-philosophy-quiz.git
cd programming-philosophy-quiz
python3 agent-driven-quiz.py
```

### 3. Upgrade SonicCyclops' SOUL.md

```bash
python3 upgrade-soul.py nathan_programming_philosophy_agent_YYYYMMDD_HHMMSS.json
```

## 🤖 How It Works

1. **Detection** - Script finds your SonicCyclops agent endpoint
2. **Dynamic Generation** - Agent creates specific code examples for each topic
3. **Interactive Critique** - You analyze and criticize the generated examples
4. **Context Building** - Each question informed by your previous responses  
5. **Follow-up Exploration** - Agent asks deeper questions based on your detailed answers
6. **Philosophy Extraction** - Patterns analyzed and integrated into SOUL.md

## 📊 What Gets Assessed

### Core Categories
- **Language Philosophy** - Real CLI tool implementation choices
- **Architecture Patterns** - Concrete microservices vs monolith scenarios
- **Error Handling** - Payment processing failure strategies
- **API Design** - Social media backend implementation approaches
- **Database Design** - User analytics storage decisions
- **Testing Strategy** - Business logic verification approaches
- **Code Organization** - Large application structure examples
- **Performance** - High-traffic caching implementations
- **Security** - Authentication system comparisons
- **Workflow** - Team git branching scenarios
- **Code Quality** - Real code review situations
- **Team Dynamics** - Technical decision-making examples

### What Makes This Valuable

**Authentic Responses** - You critique real code, not hypotheticals
**Pattern Recognition** - Agent learns your actual decision-making process
**Context Evolution** - Questions become more targeted as quiz progresses
**Deep Philosophy** - Goes beyond surface preferences to core values

## 🔧 Technical Details

**Agent Communication** - REST API calls to your SonicCyclops instance
**Context Persistence** - Conversation history maintained throughout quiz
**Response Analysis** - Structured JSON output ready for SOUL.md integration
**Error Handling** - Graceful fallback if agent calls fail

## 📄 Output Format

Quiz generates:
- **Complete conversation history** - Every question and response
- **Structured responses** - Categorized by topic with metadata
- **Context evolution** - How understanding builds over time
- **Philosophy patterns** - Extracted decision-making preferences

## 🎯 Example Agent Interaction

```
Agent: Here are three approaches to handling user authentication in a Go CLI tool:

[Code Example A: JWT tokens with local storage]
[Code Example B: OAuth2 with browser flow]  
[Code Example C: API keys with config file]

Analyze each approach - what do you like and dislike about the implementation details?

Nathan: [Detailed critique of each approach]

Agent: You mentioned security concerns about local storage. Here's a more specific scenario:
Your CLI needs offline capability but users are worried about token theft...
[Follow-up scenario with implementation details]
```

## ⚡ Requirements

- Python 3.7+
- SonicCyclops agent running (local or remote)
- Network connectivity to agent endpoint

Ready to let SonicCyclops learn your authentic programming philosophy through dynamic code analysis? 🚀