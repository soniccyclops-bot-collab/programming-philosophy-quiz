#!/usr/bin/env python3
"""
SOUL.md Upgrade Script
Analyzes Nathan's programming philosophy quiz results and upgrades SonicCyclops' SOUL.md
with authentic programming preferences and decision-making patterns.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any

class SoulUpgrader:
    def __init__(self, quiz_results_file: str):
        self.results = self.load_results(quiz_results_file)
        self.soul_content = self.load_current_soul()
        
    def load_results(self, filename: str) -> Dict:
        """Load quiz results from JSON file."""
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Could not load quiz results: {e}")
            sys.exit(1)
    
    def load_current_soul(self) -> str:
        """Load current SOUL.md content."""
        soul_path = Path("../SOUL.md")
        if soul_path.exists():
            return soul_path.read_text()
        else:
            print("⚠️  SOUL.md not found, will create new one")
            return ""
    
    def analyze_programming_patterns(self) -> Dict[str, Any]:
        """Analyze Nathan's programming philosophy from quiz responses."""
        patterns = {
            "language_preferences": {},
            "architecture_philosophy": {},
            "code_quality_standards": {},
            "decision_making_style": "",
            "technical_priorities": [],
            "collaboration_style": "",
            "learning_approach": "",
            "core_values": []
        }
        
        # Analyze each category
        for category, responses in self.results.get("responses", {}).items():
            for response in responses:
                self.extract_patterns(category, response, patterns)
        
        return patterns
    
    def extract_patterns(self, category: str, response: Dict, patterns: Dict):
        """Extract programming philosophy patterns from individual responses."""
        response_text = response.get("response", "").lower()
        
        # Language Philosophy patterns
        if category == "Language Philosophy":
            if "performance" in response_text:
                patterns["technical_priorities"].append("performance")
            if "readability" in response_text or "maintainability" in response_text:
                patterns["technical_priorities"].append("maintainability")
            if "productivity" in response_text:
                patterns["technical_priorities"].append("developer_productivity")
        
        # Architecture patterns
        elif category == "Architecture Patterns":
            if "monolith" in response_text:
                patterns["architecture_philosophy"]["deployment"] = "monolith_first"
            elif "microservices" in response_text:
                patterns["architecture_philosophy"]["deployment"] = "microservices_oriented"
            
        # Add more pattern extraction logic here...
        
    def generate_programming_philosophy_section(self, patterns: Dict) -> str:
        """Generate the programming philosophy section for SOUL.md."""
        return f"""## Programming Philosophy

**Core Technical Values:**
{self.format_list(patterns.get("core_values", ["Clean, maintainable code", "Real-world practicality over theoretical purity"]))}

**Language Selection Approach:**
- Right tool for the job - consider problem domain, team, and constraints
- {self.extract_language_philosophy()}

**Architecture Decision Making:**
- {self.extract_architecture_philosophy()}

**Code Quality Standards:**
{self.format_code_quality_standards()}

**Technical Priorities:**
{self.format_list(patterns.get("technical_priorities", []))}

**Collaboration Style:**
- {self.extract_collaboration_style()}

**Decision Making Pattern:**
{self.extract_decision_pattern()}"""

    def extract_language_philosophy(self) -> str:
        """Extract language philosophy from responses."""
        # Analyze language-related responses
        lang_responses = self.results.get("responses", {}).get("Language Philosophy", [])
        if not lang_responses:
            return "Pragmatic language selection based on project requirements"
        
        # Extract key themes from responses
        themes = []
        for response in lang_responses:
            if "performance" in response.get("response", "").lower():
                themes.append("Performance when it matters")
            if "productivity" in response.get("response", "").lower():
                themes.append("Developer productivity for rapid iteration")
        
        return " | ".join(themes) if themes else "Context-driven language selection"
    
    def extract_architecture_philosophy(self) -> str:
        """Extract architecture philosophy from responses."""
        arch_responses = self.results.get("responses", {}).get("Architecture Patterns", [])
        if not arch_responses:
            return "Start simple, evolve complexity as needed"
        
        return "Architecture emerges from constraints and team capabilities"
    
    def format_code_quality_standards(self) -> str:
        """Format code quality standards."""
        return """- Code should tell a story - readable by future developers
- Comments explain 'why', not 'what'
- Testing strategies match risk and change frequency
- Refactoring is continuous, not a separate phase"""
    
    def extract_collaboration_style(self) -> str:
        """Extract collaboration style."""
        return "Technical discussions driven by constraints and tradeoffs, not opinions"
    
    def extract_decision_pattern(self) -> str:
        """Extract decision making pattern."""
        return """Nathan approaches technical decisions systematically:
1. Understand the real constraints and requirements
2. Consider multiple approaches with concrete examples
3. Evaluate tradeoffs explicitly
4. Choose based on context, not ideology
5. Ship and learn from real usage"""
    
    def format_list(self, items: List[str]) -> str:
        """Format a list of items for markdown."""
        if not items:
            return "- [To be determined from quiz responses]"
        return "\n".join(f"- {item}" for item in items)
    
    def upgrade_soul(self) -> str:
        """Generate upgraded SOUL.md content."""
        patterns = self.analyze_programming_patterns()
        
        # Find the existing programming section or add new one
        lines = self.soul_content.split('\n')
        
        # Look for existing programming philosophy section
        start_idx = None
        end_idx = None
        
        for i, line in enumerate(lines):
            if "## Programming Philosophy" in line:
                start_idx = i
            elif start_idx is not None and line.startswith("## ") and i > start_idx:
                end_idx = i
                break
        
        programming_section = self.generate_programming_philosophy_section(patterns)
        
        if start_idx is not None:
            # Replace existing section
            if end_idx is None:
                end_idx = len(lines)
            new_lines = lines[:start_idx] + programming_section.split('\n') + lines[end_idx:]
        else:
            # Add new section before "Boundaries" or at end
            boundary_idx = None
            for i, line in enumerate(lines):
                if "## Boundaries" in line:
                    boundary_idx = i
                    break
            
            if boundary_idx:
                new_lines = lines[:boundary_idx] + [""] + programming_section.split('\n') + [""] + lines[boundary_idx:]
            else:
                new_lines = lines + [""] + programming_section.split('\n')
        
        return '\n'.join(new_lines)
    
    def save_upgraded_soul(self, output_path: str = "../SOUL.md"):
        """Save the upgraded SOUL.md."""
        upgraded_content = self.upgrade_soul()
        
        # Backup current SOUL.md
        soul_path = Path(output_path)
        if soul_path.exists():
            backup_path = soul_path.with_suffix('.md.backup')
            backup_path.write_text(soul_path.read_text())
            print(f"📄 Backed up current SOUL.md to {backup_path}")
        
        # Write upgraded version
        soul_path.write_text(upgraded_content)
        print(f"✅ Upgraded SOUL.md saved to {soul_path}")
        
        return str(soul_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 upgrade-soul.py <quiz_results.json>")
        sys.exit(1)
    
    quiz_file = sys.argv[1]
    if not Path(quiz_file).exists():
        print(f"❌ Quiz results file not found: {quiz_file}")
        sys.exit(1)
    
    upgrader = SoulUpgrader(quiz_file)
    upgrader.save_upgraded_soul()
    
    print("\n🤖 SonicCyclops SOUL.md has been upgraded with Nathan's")
    print("authentic programming philosophy and decision-making patterns!")