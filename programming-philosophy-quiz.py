#!/usr/bin/env python3
"""
SonicCyclops Programming Philosophy Quiz
A comprehensive assessment of Nathan's coding preferences and architectural decision-making patterns.
"""

import json
import datetime
from typing import Dict, List, Any
from pathlib import Path

class ProgrammingPhilosophyQuiz:
    def __init__(self):
        self.responses = {}
        self.start_time = datetime.datetime.now()
        
    def ask_question(self, category: str, question: str, options: List[str] = None, question_type: str = "choice") -> Any:
        """Ask a question and record the response."""
        print(f"\n{'='*60}")
        print(f"CATEGORY: {category.upper()}")
        print(f"{'='*60}")
        print(f"\n{question}")
        
        if question_type == "choice" and options:
            print("\nOptions:")
            for i, option in enumerate(options, 1):
                print(f"  {i}. {option}")
            
            while True:
                try:
                    choice = input(f"\nEnter choice (1-{len(options)}): ").strip()
                    choice_idx = int(choice) - 1
                    if 0 <= choice_idx < len(options):
                        response = options[choice_idx]
                        break
                    else:
                        print("Invalid choice. Try again.")
                except ValueError:
                    print("Please enter a number.")
                    
        elif question_type == "scale":
            print("Rate from 1-10 (1 = strongly disagree, 10 = strongly agree)")
            while True:
                try:
                    response = int(input("Rating: ").strip())
                    if 1 <= response <= 10:
                        break
                    else:
                        print("Please enter a number between 1 and 10.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif question_type == "open":
            response = input("Your answer: ").strip()
            
        # Follow up with reasoning
        reasoning = input("Why? (brief explanation): ").strip()
        
        # Store the response
        if category not in self.responses:
            self.responses[category] = []
            
        self.responses[category].append({
            "question": question,
            "response": response,
            "reasoning": reasoning,
            "timestamp": datetime.datetime.now().isoformat()
        })
        
        return response

    def run_quiz(self):
        """Run the complete programming philosophy quiz."""
        print("🤖 SonicCyclops Programming Philosophy Assessment")
        print("=" * 50)
        print("This quiz will help me understand your coding preferences,")
        print("architectural decisions, and development philosophy.")
        print("Take your time - there are no wrong answers!")
        
        input("\nPress Enter to begin...")
        
        # Language Philosophy
        self.ask_question(
            "Language Philosophy",
            "When choosing a programming language for a new project, what's your primary consideration?",
            [
                "Performance and efficiency above all",
                "Developer productivity and expressiveness", 
                "Ecosystem and library availability",
                "Team familiarity and maintainability",
                "Problem domain fit (right tool for the job)"
            ]
        )
        
        self.ask_question(
            "Language Philosophy", 
            "How do you feel about dynamic vs static typing?",
            [
                "Static typing always - catch errors early",
                "Dynamic for rapid prototyping, static for production",
                "Dynamic typing for flexibility and speed",
                "It depends entirely on the problem domain",
                "Gradual typing (TypeScript style) is the sweet spot"
            ]
        )
        
        # Architecture Patterns
        self.ask_question(
            "Architecture",
            "For a medium-scale web application, what's your preferred architecture?",
            [
                "Monolith with clear internal boundaries",
                "Microservices from the start",
                "Modular monolith that can split later", 
                "Service-oriented architecture with larger services",
                "Serverless/function-based architecture"
            ]
        )
        
        self.ask_question(
            "Architecture",
            "How do you approach database design?",
            [
                "Start with relational, add NoSQL as needed",
                "Choose database per use case (polyglot persistence)",
                "Event sourcing and CQRS for complex domains",
                "Simple SQL database until it doesn't scale",
                "Graph databases for connected data"
            ]
        )
        
        self.ask_question(
            "Architecture",
            "Rate your preference for Domain-Driven Design principles",
            question_type="scale"
        )
        
        # Code Organization
        self.ask_question(
            "Code Organization",
            "How do you prefer to organize code in a project?",
            [
                "By technical layer (controllers, services, models)",
                "By business domain/feature (user, order, payment)",
                "Hybrid approach - domains with technical separation",
                "Flat structure until complexity demands organization",
                "Package-by-component with vertical slices"
            ]
        )
        
        self.ask_question(
            "Code Organization",
            "What's your stance on code comments?",
            [
                "Code should be self-documenting, minimal comments",
                "Comment the 'why', not the 'what'",
                "Comprehensive comments for all non-trivial code",
                "Comments are code smells - refactor instead",
                "API documentation via comments, internal code self-documents"
            ]
        )
        
        # Testing Philosophy
        self.ask_question(
            "Testing",
            "What's your testing strategy for a typical application?",
            [
                "Unit tests for everything, minimal integration tests",
                "Testing pyramid: many unit, some integration, few e2e",
                "Testing trophy: focus on integration tests",
                "Test what matters, don't chase coverage metrics",
                "Property-based testing and fuzzing over examples"
            ]
        )
        
        self.ask_question(
            "Testing",
            "Rate the importance of Test-Driven Development (TDD)",
            question_type="scale"
        )
        
        # Performance vs Readability
        self.ask_question(
            "Performance vs Readability",
            "When you encounter a performance bottleneck, what's your approach?",
            [
                "Profile first, then optimize the actual bottleneck",
                "Optimize for readability, then performance as needed", 
                "Design for performance from the beginning",
                "Use the simplest solution that meets requirements",
                "Benchmark multiple approaches and choose the best"
            ]
        )
        
        self.ask_question(
            "Performance vs Readability",
            "How do you feel about premature optimization?",
            [
                "It's the root of all evil - avoid at all costs",
                "Some upfront performance thinking is wise",
                "Optimize early if you know it's a bottleneck",
                "Design for performance, implement for clarity",
                "It depends on the performance requirements"
            ]
        )
        
        # Error Handling
        self.ask_question(
            "Error Handling", 
            "What's your preferred error handling strategy?",
            [
                "Exceptions for exceptional cases, results for expected failures",
                "Return codes/result types, avoid exceptions",
                "Fail fast with meaningful error messages",
                "Railway-oriented programming with monads",
                "Let it crash and restart (Erlang style)"
            ]
        )
        
        self.ask_question(
            "Error Handling",
            "How verbose should error messages be?",
            [
                "Minimal - just enough to identify the problem",
                "Detailed for developers, simple for users",
                "Comprehensive logging, structured error responses",
                "Context-rich errors with suggested fixes",
                "Machine-readable error codes with human descriptions"
            ]
        )
        
        # Development Workflow
        self.ask_question(
            "Development Workflow",
            "What's your preferred git workflow?",
            [
                "GitHub Flow (feature branches to main)",
                "GitFlow with develop and release branches", 
                "Trunk-based development with feature flags",
                "Rebase-heavy workflow for clean history",
                "Simple: work on main, commit often"
            ]
        )
        
        self.ask_question(
            "Development Workflow",
            "How do you approach code reviews?",
            [
                "Focus on functionality and correctness",
                "Architectural decisions and design patterns",
                "Code style and consistency enforcement",
                "Knowledge sharing and learning opportunities",
                "Security and performance considerations"
            ]
        )
        
        # API Design
        self.ask_question(
            "API Design",
            "For designing REST APIs, what's your priority?",
            [
                "Strict RESTful principles and resource modeling",
                "Pragmatic API that serves client needs well",
                "GraphQL for flexible data fetching",
                "RPC-style APIs with clear method names",
                "Event-driven APIs with webhooks/streaming"
            ]
        )
        
        self.ask_question(
            "API Design",
            "How do you handle API versioning?",
            [
                "URL versioning (/v1/, /v2/)",
                "Header-based versioning",
                "Query parameter versioning", 
                "Avoid breaking changes, extend instead",
                "Semantic versioning with deprecation periods"
            ]
        )
        
        # Security Mindset
        self.ask_question(
            "Security",
            "Rate the importance of security-by-design in your development process",
            question_type="scale"
        )
        
        self.ask_question(
            "Security",
            "What's your approach to authentication/authorization?",
            [
                "Use proven libraries, don't roll your own",
                "OAuth2/OIDC for everything",
                "JWT tokens with proper validation",
                "Session-based auth with secure cookies",
                "Zero-trust architecture with service mesh"
            ]
        )
        
        # Technology Adoption
        self.ask_question(
            "Technology Adoption",
            "How do you approach adopting new technologies?",
            [
                "Early adopter - try new things immediately",
                "Wait for community adoption and proven patterns",
                "Evaluate based on specific project needs",
                "Stick with proven, stable technologies",
                "Prototype new tech in side projects first"
            ]
        )
        
        self.ask_question(
            "Technology Adoption",
            "What's your philosophy on technical debt?",
            [
                "Refactor continuously, never accumulate debt",
                "Strategic debt is acceptable for delivery speed",
                "Track debt explicitly and pay it down regularly",
                "Focus on business value, clean up when needed",
                "Architecture decisions matter more than code quality"
            ]
        )
        
        # Documentation
        self.ask_question(
            "Documentation",
            "What's your approach to project documentation?",
            [
                "Comprehensive docs for everything",
                "Just enough documentation to onboard new people",
                "Code-generated docs with minimal manual writing",
                "README and inline comments are sufficient", 
                "Living documentation that evolves with code"
            ]
        )
        
        # Team Collaboration
        self.ask_question(
            "Team Collaboration",
            "In a team setting, how do you prefer to make architectural decisions?",
            [
                "Architecture committee with formal approval",
                "Team consensus through discussion",
                "Tech lead makes final decisions",
                "Democratic voting on alternatives",
                "Experiment with prototypes, then decide"
            ]
        )
        
        self.ask_question(
            "Team Collaboration",
            "Rate your preference for pair programming",
            question_type="scale"
        )
        
        # Personal Philosophy
        self.ask_question(
            "Personal Philosophy",
            "What's your core belief about good software?",
            question_type="open"
        )
        
        self.ask_question(
            "Personal Philosophy", 
            "Complete this sentence: 'The most important thing in software development is...'",
            question_type="open"
        )
        
        self.ask_question(
            "Personal Philosophy",
            "What's your biggest programming pet peeve?",
            question_type="open"
        )
        
        print(f"\n{'='*60}")
        print("🎉 Quiz Complete! Thank you for your thoughtful responses.")
        print(f"{'='*60}")
        
    def save_results(self, filename: str = None):
        """Save quiz results to JSON file."""
        if filename is None:
            timestamp = self.start_time.strftime("%Y%m%d_%H%M%S")
            filename = f"nathan_programming_philosophy_{timestamp}.json"
            
        results = {
            "quiz_metadata": {
                "start_time": self.start_time.isoformat(),
                "end_time": datetime.datetime.now().isoformat(),
                "total_questions": sum(len(questions) for questions in self.responses.values())
            },
            "responses": self.responses
        }
        
        Path(filename).write_text(json.dumps(results, indent=2))
        print(f"\n📄 Results saved to: {filename}")
        return filename
    
    def analyze_patterns(self):
        """Analyze response patterns to extract insights."""
        insights = {
            "preference_patterns": {},
            "philosophy_themes": [],
            "decision_making_style": "",
            "risk_tolerance": "",
            "collaboration_style": ""
        }
        
        # This would contain analysis logic based on responses
        # For now, just structure for manual analysis
        
        return insights

if __name__ == "__main__":
    quiz = ProgrammingPhilosophyQuiz()
    quiz.run_quiz()
    filename = quiz.save_results()
    
    print(f"\n🤖 SonicCyclops will now analyze these results to better understand")
    print(f"your programming philosophy and decision-making patterns!")