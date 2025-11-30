#!/usr/bin/env python3
"""
Mock Interview Runner
Interactive CLI for conducting mock interviews with timer functionality.
"""

import sys
import time
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any

from question_bank import QuestionBank
from session_tracker import SessionTracker


class InterviewRunner:
    """Main class for running mock interviews."""
    
    def __init__(self):
        """Initialize the interview runner."""
        self.question_bank = QuestionBank()
        self.session_tracker = SessionTracker()
        self.current_session_id: Optional[str] = None
        self.current_questions: List[Dict[str, Any]] = []
        self.question_start_time: Optional[float] = None
    
    def display_welcome(self):
        """Display welcome message."""
        print("\n" + "=" * 70)
        print(" " * 20 + "MOCK INTERVIEW SYSTEM")
        print("=" * 70)
        print("\nWelcome! Let's practice for your upcoming interviews.")
        print("This system supports LeetCode, System Design, and Pair Programming interviews.\n")
    
    def display_menu(self):
        """Display main menu."""
        print("\n" + "-" * 70)
        print("MAIN MENU")
        print("-" * 70)
        print("1. Start LeetCode Interview")
        print("2. Start System Design Interview")
        print("3. Start Pair Programming Session")
        print("4. View Recent Sessions")
        print("5. View Statistics")
        print("6. Exit")
        print("-" * 70)
    
    def get_user_choice(self, prompt: str, valid_choices: List[str]) -> str:
        """Get user input with validation.
        
        Args:
            prompt: Prompt to display.
            valid_choices: List of valid choice strings.
            
        Returns:
            User's choice.
        """
        while True:
            choice = input(f"\n{prompt} ").strip().lower()
            if choice in valid_choices:
                return choice
            print(f"Invalid choice. Please enter one of: {', '.join(valid_choices)}")
    
    def select_difficulty(self) -> Optional[str]:
        """Let user select difficulty level.
        
        Returns:
            Selected difficulty or None for random.
        """
        print("\nSelect difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Random (any difficulty)")
        
        choice = self.get_user_choice("Enter choice (1-4):", ["1", "2", "3", "4"])
        
        difficulty_map = {
            "1": "easy",
            "2": "medium",
            "3": "hard",
            "4": None
        }
        return difficulty_map[choice]
    
    def start_leetcode_interview(self):
        """Start a LeetCode-style coding interview."""
        print("\n" + "=" * 70)
        print("LEETCODE INTERVIEW")
        print("=" * 70)
        
        # Select difficulty
        difficulty = self.select_difficulty()
        
        # Select number of questions
        print("\nHow many questions? (1-2 recommended for 45-60 min session)")
        num_questions = int(self.get_user_choice("Enter number (1-3):", ["1", "2", "3"]))
        
        # Select questions
        questions = self.question_bank.select_questions_for_session(
            "leetcode",
            count=num_questions,
            difficulty=difficulty,
            startup_friendly=True
        )
        
        if not questions:
            print("\nNo questions found matching your criteria. Try different settings.")
            return
        
        question_ids = [q["id"] for q in questions]
        self.current_session_id = self.session_tracker.start_session(
            "leetcode",
            question_ids,
            difficulty
        )
        self.current_questions = questions
        
        print(f"\n✓ Session started: {self.current_session_id}")
        print(f"✓ Selected {len(questions)} question(s)")
        
        # Conduct interview
        self._conduct_leetcode_interview()
    
    def start_system_design_interview(self):
        """Start a system design interview."""
        print("\n" + "=" * 70)
        print("SYSTEM DESIGN INTERVIEW")
        print("=" * 70)
        
        # Select difficulty
        difficulty = self.select_difficulty()
        
        # Select question
        question = self.question_bank.select_random_question(
            "system_design",
            difficulty=difficulty,
            startup_friendly=True
        )
        
        if not question:
            print("\nNo questions found matching your criteria. Try different settings.")
            return
        
        self.current_session_id = self.session_tracker.start_session(
            "system_design",
            [question["id"]],
            difficulty
        )
        self.current_questions = [question]
        
        print(f"\n✓ Session started: {self.current_session_id}")
        
        # Conduct interview
        self._conduct_system_design_interview()
    
    def start_pair_programming_session(self):
        """Start a pair programming session."""
        print("\n" + "=" * 70)
        print("PAIR PROGRAMMING SESSION")
        print("=" * 70)
        
        # Select difficulty
        difficulty = self.select_difficulty()
        
        # Select scenario
        scenario = self.question_bank.select_random_question(
            "pair_programming",
            difficulty=difficulty,
            startup_friendly=True
        )
        
        if not scenario:
            print("\nNo scenarios found matching your criteria. Try different settings.")
            return
        
        self.current_session_id = self.session_tracker.start_session(
            "pair_programming",
            [scenario["id"]],
            difficulty
        )
        self.current_questions = [scenario]
        
        print(f"\n✓ Session started: {self.current_session_id}")
        
        # Conduct session
        self._conduct_pair_programming_session()
    
    def _conduct_leetcode_interview(self):
        """Conduct a LeetCode interview session."""
        session_start = time.time()
        
        for idx, question in enumerate(self.current_questions, 1):
            print("\n" + "=" * 70)
            print(f"QUESTION {idx} of {len(self.current_questions)}")
            print("=" * 70)
            
            # Display question
            self._display_leetcode_question(question)
            
            # Start timer
            self.question_start_time = time.time()
            print("\n⏱️  Timer started. Work on the problem...")
            print("Type 'done' when finished, 'hint' for a hint, or 'skip' to move on.")
            
            # Interactive loop
            while True:
                action = input("\n> ").strip().lower()
                
                if action == "done":
                    elapsed = time.time() - self.question_start_time
                    print(f"\n✓ Time taken: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")
                    
                    # Get self-rating
                    rating = self._get_rating("How would you rate your solution? (1-5):")
                    
                    # Get notes
                    notes = input("Any notes about this problem? (press Enter to skip): ").strip()
                    
                    # Update tracker
                    self.session_tracker.update_question(
                        self.current_session_id,
                        question["id"],
                        "completed",
                        time_taken=elapsed,
                        rating=rating,
                        notes=notes
                    )
                    break
                
                elif action == "hint":
                    self._show_hint(question)
                
                elif action == "skip":
                    print("\n⏭️  Skipping this question...")
                    self.session_tracker.update_question(
                        self.current_session_id,
                        question["id"],
                        "skipped"
                    )
                    break
                
                elif action == "show":
                    self._display_leetcode_question(question)
                
                else:
                    print("Commands: 'done', 'hint', 'skip', 'show'")
        
        # End session
        self._end_session()
    
    def _conduct_system_design_interview(self):
        """Conduct a system design interview session."""
        question = self.current_questions[0]
        
        print("\n" + "=" * 70)
        print("SYSTEM DESIGN QUESTION")
        print("=" * 70)
        
        # Display question
        print(f"\n📋 {question['title']}")
        print(f"\n{question['description']}")
        
        # Display requirements
        if "requirements" in question:
            reqs = question["requirements"]
            print("\n📝 REQUIREMENTS:")
            
            if "functional" in reqs:
                print("\n  Functional Requirements:")
                for req in reqs["functional"]:
                    print(f"    • {req}")
            
            if "non_functional" in reqs:
                print("\n  Non-Functional Requirements:")
                for req in reqs["non_functional"]:
                    print(f"    • {req}")
            
            if "scale" in reqs:
                print("\n  Scale:")
                for key, value in reqs["scale"].items():
                    print(f"    • {key}: {value}")
        
        # Display evaluation criteria
        if "evaluation_criteria" in question:
            print("\n✅ EVALUATION CRITERIA:")
            for criterion in question["evaluation_criteria"]:
                print(f"    • {criterion}")
        
        # Start timer
        expected_duration = question.get("expected_duration", 45)
        print(f"\n⏱️  Recommended time: {expected_duration} minutes")
        print("Type 'done' when finished, 'hint' for a hint, or 'skip' to move on.")
        
        self.question_start_time = time.time()
        
        # Interactive loop
        while True:
            action = input("\n> ").strip().lower()
            
            if action == "done":
                elapsed = time.time() - self.question_start_time
                print(f"\n✓ Time taken: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")
                
                rating = self._get_rating("How would you rate your design? (1-5):")
                notes = input("Any notes about this design? (press Enter to skip): ").strip()
                
                self.session_tracker.update_question(
                    self.current_session_id,
                    question["id"],
                    "completed",
                    time_taken=elapsed,
                    rating=rating,
                    notes=notes
                )
                break
            
            elif action == "hint":
                self._show_hint(question)
            
            elif action == "skip":
                print("\n⏭️  Skipping this question...")
                self.session_tracker.update_question(
                    self.current_session_id,
                    question["id"],
                    "skipped"
                )
                break
            
            else:
                print("Commands: 'done', 'hint', 'skip'")
        
        # End session
        self._end_session()
    
    def _conduct_pair_programming_session(self):
        """Conduct a pair programming session."""
        scenario = self.current_questions[0]
        
        print("\n" + "=" * 70)
        print("PAIR PROGRAMMING SCENARIO")
        print("=" * 70)
        
        # Display scenario
        print(f"\n📋 {scenario['title']}")
        print(f"\n{scenario['description']}")
        
        if "task" in scenario:
            print(f"\n📝 TASK:")
            print(f"  {scenario['task']}")
        
        if "requirements" in scenario:
            print("\n📋 REQUIREMENTS:")
            for req in scenario["requirements"]:
                print(f"    • {req}")
        
        if "evaluation_criteria" in scenario:
            print("\n✅ EVALUATION CRITERIA:")
            for criterion in scenario["evaluation_criteria"]:
                print(f"    • {criterion}")
        
        # Start timer
        expected_duration = scenario.get("expected_duration", 30)
        print(f"\n⏱️  Recommended time: {expected_duration} minutes")
        print("Type 'done' when finished, 'hint' for a hint, or 'skip' to move on.")
        
        self.question_start_time = time.time()
        
        # Interactive loop
        while True:
            action = input("\n> ").strip().lower()
            
            if action == "done":
                elapsed = time.time() - self.question_start_time
                print(f"\n✓ Time taken: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")
                
                rating = self._get_rating("How would you rate your implementation? (1-5):")
                notes = input("Any notes about this session? (press Enter to skip): ").strip()
                
                self.session_tracker.update_question(
                    self.current_session_id,
                    scenario["id"],
                    "completed",
                    time_taken=elapsed,
                    rating=rating,
                    notes=notes
                )
                break
            
            elif action == "hint":
                self._show_hint(scenario)
            
            elif action == "skip":
                print("\n⏭️  Skipping this scenario...")
                self.session_tracker.update_question(
                    self.current_session_id,
                    scenario["id"],
                    "skipped"
                )
                break
            
            else:
                print("Commands: 'done', 'hint', 'skip'")
        
        # End session
        self._end_session()
    
    def _display_leetcode_question(self, question: Dict[str, Any]):
        """Display a LeetCode question."""
        print(f"\n📋 {question['title']}")
        print(f"   Difficulty: {question['difficulty'].upper()}")
        print(f"   Category: {question['category']}")
        print(f"   Tags: {', '.join(question.get('tags', []))}")
        
        print(f"\n📝 Description:")
        print(f"   {question['description']}")
        
        if "examples" in question:
            print("\n💡 Examples:")
            for i, example in enumerate(question["examples"], 1):
                print(f"\n   Example {i}:")
                print(f"   Input: {example['input']}")
                print(f"   Output: {example['output']}")
                if "explanation" in example:
                    print(f"   Explanation: {example['explanation']}")
        
        if "constraints" in question:
            print("\n⚠️  Constraints:")
            for constraint in question["constraints"]:
                print(f"   • {constraint}")
        
        if "time_complexity" in question:
            print(f"\n⏱️  Expected Time Complexity: {question['time_complexity']}")
        if "space_complexity" in question:
            print(f"💾 Expected Space Complexity: {question['space_complexity']}")
        
        # Check if solution file exists
        if "file_path" in question:
            file_path = question["file_path"]
            print(f"\n📁 Solution file: {file_path}")
            print("   (You can reference this file for the problem statement)")
    
    def _show_hint(self, question: Dict[str, Any]):
        """Show hints for a question."""
        if "hints" in question:
            print("\n💡 HINTS:")
            for i, hint in enumerate(question["hints"], 1):
                print(f"   {i}. {hint}")
        else:
            print("\n💡 No hints available for this question.")
            print("   Try thinking about:")
            print("   • What data structures might be useful?")
            print("   • Can you break the problem into smaller subproblems?")
            print("   • What patterns have you seen in similar problems?")
    
    def _get_rating(self, prompt: str) -> Optional[int]:
        """Get a rating from the user.
        
        Args:
            prompt: Prompt to display.
            
        Returns:
            Rating (1-5) or None.
        """
        while True:
            try:
                rating_str = input(f"{prompt} ").strip()
                if not rating_str:
                    return None
                rating = int(rating_str)
                if 1 <= rating <= 5:
                    return rating
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a valid number.")
    
    def _end_session(self):
        """End the current interview session."""
        if not self.current_session_id:
            return
        
        print("\n" + "=" * 70)
        print("SESSION COMPLETE")
        print("=" * 70)
        
        overall_rating = self._get_rating("Overall session rating (1-5, press Enter to skip):")
        notes = input("Overall session notes (press Enter to skip): ").strip()
        
        self.session_tracker.end_session(
            self.current_session_id,
            overall_rating=overall_rating,
            notes=notes
        )
        
        print("\n✓ Session saved!")
        print(f"  Session ID: {self.current_session_id}")
        
        # Reset state
        self.current_session_id = None
        self.current_questions = []
        self.question_start_time = None
    
    def view_recent_sessions(self):
        """View recent interview sessions."""
        print("\n" + "=" * 70)
        print("RECENT SESSIONS")
        print("=" * 70)
        
        sessions = self.session_tracker.get_recent_sessions(10)
        
        if not sessions:
            print("\nNo sessions found.")
            return
        
        for i, session in enumerate(sessions, 1):
            print(f"\n{i}. {session['session_id']}")
            print(f"   Type: {session['interview_type']}")
            print(f"   Date: {session['start_time']}")
            if session['overall_performance']['completed']:
                print(f"   Status: ✓ Completed")
                if session.get('duration_seconds'):
                    mins = session['duration_seconds'] / 60
                    print(f"   Duration: {mins:.1f} minutes")
                if session['overall_performance'].get('rating'):
                    print(f"   Rating: {session['overall_performance']['rating']}/5")
            else:
                print(f"   Status: ⏸ In Progress")
    
    def view_statistics(self):
        """View overall statistics."""
        print("\n" + "=" * 70)
        print("STATISTICS")
        print("=" * 70)
        
        stats = self.session_tracker.get_statistics()
        
        print(f"\nTotal Sessions: {stats['total_sessions']}")
        print(f"Completed Sessions: {stats['completed_sessions']}")
        
        if stats['average_rating']:
            print(f"\nAverage Rating: {stats['average_rating']:.2f}/5")
        if stats['average_accuracy']:
            print(f"Average Accuracy: {stats['average_accuracy']*100:.1f}%")
        if stats['average_duration']:
            mins = stats['average_duration'] / 60
            print(f"Average Duration: {mins:.1f} minutes")
        
        if stats['by_type']:
            print("\nBy Interview Type:")
            for interview_type, type_stats in stats['by_type'].items():
                print(f"\n  {interview_type.upper()}:")
                print(f"    Sessions: {type_stats['count']}")
                if type_stats.get('average_rating'):
                    print(f"    Avg Rating: {type_stats['average_rating']:.2f}/5")
                if type_stats.get('average_duration'):
                    mins = type_stats['average_duration'] / 60
                    print(f"    Avg Duration: {mins:.1f} minutes")
    
    def run(self):
        """Run the main interview loop."""
        self.display_welcome()
        
        while True:
            self.display_menu()
            choice = self.get_user_choice("Enter choice (1-6):", ["1", "2", "3", "4", "5", "6"])
            
            if choice == "1":
                self.start_leetcode_interview()
            elif choice == "2":
                self.start_system_design_interview()
            elif choice == "3":
                self.start_pair_programming_session()
            elif choice == "4":
                self.view_recent_sessions()
            elif choice == "5":
                self.view_statistics()
            elif choice == "6":
                print("\n👋 Good luck with your interviews!")
                if self.current_session_id:
                    print("⚠️  You have an active session. Ending it now...")
                    self._end_session()
                sys.exit(0)


if __name__ == "__main__":
    runner = InterviewRunner()
    try:
        runner.run()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user.")
        if runner.current_session_id:
            print("⚠️  You have an active session. Ending it now...")
            runner._end_session()
        sys.exit(0)

