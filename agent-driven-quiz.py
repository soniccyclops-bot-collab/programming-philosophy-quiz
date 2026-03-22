#!/usr/bin/env python3
"""
SonicCyclops Agent-Driven Programming Philosophy Quiz
Dynamic assessment where SonicCyclops generates code examples and scenarios in real-time
based on Nathan's responses, allowing for deep exploration of programming preferences.
"""

import json
import datetime
import requests
import os
import sys
from typing import Dict, List, Any, Optional
from pathlib import Path

class AgentDrivenQuiz:
    def __init__(self):
        self.responses = {}
        self.start_time = datetime.datetime.now()
        self.agent_base_url = self.get_agent_endpoint()
        self.conversation_history = []
        
    def get_agent_endpoint(self) -> str:
        """Get the SonicCyclops agent endpoint."""
        # Try common endpoints, or use environment variable
        endpoint = os.getenv('SONICCYCLOPS_ENDPOINT')
        if endpoint:
            return endpoint
            
        # Try local Ollama first, then OpenClaw gateway
        possible_endpoints = [
            'http://localhost:11434/api/generate',  # Local Ollama
            'http://localhost:18789/v1/chat/completions',  # OpenClaw gateway
        ]
        
        for endpoint in possible_endpoints:
            try:
                # Test connectivity
                response = requests.get(endpoint.replace('/api/generate', '/api/tags').replace('/v1/chat/completions', '/health'), timeout=2)
                if response.status_code == 200:
                    return endpoint
            except:
                continue
                
        print("❌ Could not connect to SonicCyclops agent!")
        print("Options:")
        print("1. Start local Ollama: `ollama serve`")
        print("2. Set endpoint: `export SONICCYCLOPS_ENDPOINT=http://your-endpoint`")
        print("3. Use OpenClaw gateway if available")
        sys.exit(1)

    def call_agent(self, prompt: str, context: str = "") -> str:
        """Call SonicCyclops agent to generate examples and questions."""
        full_prompt = f"""You are SonicCyclops conducting a dynamic programming philosophy quiz for Nathan.

Context from previous responses:
{context}

Current conversation:
{chr(10).join(self.conversation_history[-3:])}

Your task: {prompt}

Instructions:
- Generate concrete, realistic code examples
- Present specific architectural scenarios
- Ask for detailed critiques and preferences
- Follow up on interesting responses
- Keep examples relevant to real-world development
- Make Nathan think about tradeoffs, not just pick answers

Response format: Return just your question/example, no meta-commentary."""

        try:
            if 'ollama' in self.agent_base_url:
                # Ollama API format
                response = requests.post(self.agent_base_url, json={
                    'model': 'nemotron-cascade-2',  # or whatever model Nathan has
                    'prompt': full_prompt,
                    'stream': False
                })
                return response.json()['response']
            else:
                # OpenAI-compatible format (OpenClaw)
                response = requests.post(self.agent_base_url, json={
                    'model': 'claude-sonnet-4',
                    'messages': [{'role': 'user', 'content': full_prompt}],
                    'max_tokens': 1000
                })
                return response.json()['choices'][0]['message']['content']
                
        except Exception as e:
            print(f"❌ Agent call failed: {e}")
            return f"[Agent Error] Please manually provide: {prompt}"

    def dynamic_question(self, category: str, base_topic: str) -> str:
        """Generate a dynamic question using the agent."""
        context = self.get_context_summary()
        
        prompt = f"""Generate a programming philosophy question about {base_topic} for category '{category}'.

Requirements:
- Present 2-3 concrete code examples showing different approaches
- Ask Nathan to critique each approach and explain his preference
- Include specific implementation details he can nitpick
- Focus on real-world scenarios he might encounter
- Generate examples that reveal philosophical differences

Topic: {base_topic}"""

        return self.call_agent(prompt, context)

    def get_context_summary(self) -> str:
        """Summarize previous responses for context."""
        if not self.responses:
            return "No previous responses yet."
            
        summary = []
        for category, responses in self.responses.items():
            if responses:
                latest = responses[-1]
                summary.append(f"{category}: {latest['response']} (Reason: {latest['reasoning']})")
                
        return "\n".join(summary)

    def ask_dynamic_question(self, category: str, topic: str) -> str:
        """Ask a dynamically generated question and record the response."""
        print(f"\n{'='*80}")
        print(f"CATEGORY: {category.upper()}")
        print(f"{'='*80}")
        
        # Get agent-generated question with examples
        question_content = self.dynamic_question(category, topic)
        print(f"\n{question_content}")
        
        # Record the conversation
        self.conversation_history.append(f"Agent: {question_content}")
        
        # Get Nathan's response
        response = input("\nYour detailed response: ").strip()
        self.conversation_history.append(f"Nathan: {response}")
        
        # Ask follow-up if response is interesting
        if len(response) > 100:  # If Nathan gave a detailed response
            follow_up = self.call_agent(
                f"Nathan gave this detailed response: '{response}'. Ask one specific follow-up question to dig deeper into his reasoning or explore edge cases.",
                self.get_context_summary()
            )
            print(f"\n🤖 Follow-up: {follow_up}")
            follow_up_response = input("Follow-up response: ").strip()
            self.conversation_history.append(f"Follow-up: {follow_up}")
            self.conversation_history.append(f"Nathan: {follow_up_response}")
            response += f" | Follow-up: {follow_up_response}"

        # Store the response
        if category not in self.responses:
            self.responses[category] = []
            
        self.responses[category].append({
            "topic": topic,
            "question_content": question_content,
            "response": response,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return response

    def run_agent_quiz(self):
        """Run the agent-driven programming philosophy quiz."""
        print("🤖 SonicCyclops Agent-Driven Programming Philosophy Quiz")
        print("=" * 60)
        print("I'll dynamically generate code examples and scenarios based on your")
        print("responses. Critique everything, be specific, and tell me exactly")
        print("what you like and don't like about each approach!")
        print()
        print("Connected to agent:", self.agent_base_url)
        
        input("\nPress Enter to begin the dynamic assessment...")
        
        # Core categories with specific topics for agent generation
        quiz_topics = [
            ("Language Philosophy", "choosing between Python, Go, and Rust for a CLI tool"),
            ("Architecture Patterns", "microservices vs monolith for an e-commerce platform"),
            ("Error Handling", "exception handling vs result types in payment processing"),
            ("API Design", "REST vs GraphQL for a social media backend"),
            ("Database Design", "SQL vs NoSQL for user analytics"),
            ("Testing Strategy", "unit testing vs integration testing for business logic"),
            ("Code Organization", "organizing a large web application codebase"),
            ("Performance Optimization", "caching strategies for high-traffic endpoints"),
            ("Security Practices", "authentication and authorization implementation"),
            ("Development Workflow", "git branching strategies for team development"),
            ("Code Quality", "code review practices and standards"),
            ("Team Collaboration", "technical decision-making in team settings")
        ]
        
        for category, topic in quiz_topics:
            try:
                self.ask_dynamic_question(category, topic)
                print("\n" + "→" * 60)
            except KeyboardInterrupt:
                print("\n\n⏸️  Quiz interrupted by user.")
                break
            except Exception as e:
                print(f"\n❌ Error in {category}: {e}")
                continue
        
        print(f"\n{'='*80}")
        print("🎉 Agent-Driven Quiz Complete!")
        print("SonicCyclops now has deep insights into your programming philosophy.")
        print(f"{'='*80}")

    def save_results(self, filename: str = None):
        """Save quiz results with full conversation history."""
        if filename is None:
            timestamp = self.start_time.strftime("%Y%m%d_%H%M%S")
            filename = f"nathan_programming_philosophy_agent_{timestamp}.json"
            
        results = {
            "quiz_metadata": {
                "start_time": self.start_time.isoformat(),
                "end_time": datetime.datetime.now().isoformat(),
                "agent_endpoint": self.agent_base_url,
                "total_categories": len(self.responses),
                "quiz_type": "agent_driven_dynamic"
            },
            "conversation_history": self.conversation_history,
            "responses": self.responses,
            "context_evolution": self.get_context_summary()
        }
        
        Path(filename).write_text(json.dumps(results, indent=2))
        print(f"\n📄 Complete results with conversation history saved to: {filename}")
        return filename

if __name__ == "__main__":
    print("🔍 Detecting SonicCyclops agent...")
    
    quiz = AgentDrivenQuiz()
    quiz.run_agent_quiz()
    filename = quiz.save_results()
    
    print(f"\n🧠 SonicCyclops will now analyze your responses and upgrade SOUL.md")
    print(f"with your authentic programming philosophy and decision patterns!")