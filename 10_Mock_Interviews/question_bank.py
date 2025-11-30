"""
Question Bank Manager
Loads, filters, and selects questions from the question banks.
"""

import json
import random
import os
from pathlib import Path
from typing import List, Dict, Optional, Any


class QuestionBank:
    """Manages question banks for different interview types."""
    
    def __init__(self, base_path: Optional[str] = None):
        """Initialize the question bank manager.
        
        Args:
            base_path: Base path to the question banks directory.
                      If None, uses the directory containing this file.
        """
        if base_path is None:
            base_path = Path(__file__).parent
        else:
            base_path = Path(base_path)
        
        self.base_path = base_path
        self.question_banks_path = base_path / "question_banks"
        
        # Load all question banks
        self.leetcode_questions = self._load_json("leetcode_questions.json")
        self.system_design_questions = self._load_json("system_design_questions.json")
        self.pair_programming_scenarios = self._load_json("pair_programming_scenarios.json")
    
    def _load_json(self, filename: str) -> Dict[str, Any]:
        """Load a JSON question bank file.
        
        Args:
            filename: Name of the JSON file to load.
            
        Returns:
            Dictionary containing the question bank data.
        """
        file_path = self.question_banks_path / filename
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: {filename} not found at {file_path}")
            return {}
        except json.JSONDecodeError as e:
            print(f"Error parsing {filename}: {e}")
            return {}
    
    def get_leetcode_questions(
        self,
        difficulty: Optional[str] = None,
        category: Optional[str] = None,
        tags: Optional[List[str]] = None,
        startup_friendly: bool = False,
        exclude_ids: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Get LeetCode questions matching the specified criteria.
        
        Args:
            difficulty: Filter by difficulty (easy, medium, hard).
            category: Filter by category (arrays, strings, trees, etc.).
            tags: Filter by tags (list of tag strings).
            startup_friendly: If True, only return startup-friendly questions.
            exclude_ids: List of question IDs to exclude.
            
        Returns:
            List of question dictionaries matching the criteria.
        """
        questions = self.leetcode_questions.get("questions", [])
        exclude_ids = exclude_ids or []
        
        filtered = []
        for q in questions:
            # Skip excluded questions
            if q.get("id") in exclude_ids:
                continue
            
            # Filter by difficulty
            if difficulty and q.get("difficulty") != difficulty:
                continue
            
            # Filter by category
            if category and q.get("category") != category:
                continue
            
            # Filter by tags
            if tags:
                question_tags = q.get("tags", [])
                if not any(tag in question_tags for tag in tags):
                    continue
            
            # Filter by startup_friendly
            if startup_friendly and not q.get("startup_friendly", False):
                continue
            
            filtered.append(q)
        
        return filtered
    
    def get_system_design_questions(
        self,
        difficulty: Optional[str] = None,
        category: Optional[str] = None,
        startup_friendly: bool = False,
        exclude_ids: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Get system design questions matching the specified criteria.
        
        Args:
            difficulty: Filter by difficulty (easy, medium, hard).
            category: Filter by category (web-services, real-time, etc.).
            startup_friendly: If True, only return startup-friendly questions.
            exclude_ids: List of question IDs to exclude.
            
        Returns:
            List of system design question dictionaries matching the criteria.
        """
        questions = self.system_design_questions.get("questions", [])
        exclude_ids = exclude_ids or []
        
        filtered = []
        for q in questions:
            # Skip excluded questions
            if q.get("id") in exclude_ids:
                continue
            
            # Filter by difficulty
            if difficulty and q.get("difficulty") != difficulty:
                continue
            
            # Filter by category
            if category and q.get("category") != category:
                continue
            
            # Filter by startup_friendly
            if startup_friendly and not q.get("startup_friendly", False):
                continue
            
            filtered.append(q)
        
        return filtered
    
    def get_pair_programming_scenarios(
        self,
        difficulty: Optional[str] = None,
        category: Optional[str] = None,
        startup_friendly: bool = False,
        exclude_ids: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Get pair programming scenarios matching the specified criteria.
        
        Args:
            difficulty: Filter by difficulty (easy, medium, hard).
            category: Filter by category (backend, frontend, etc.).
            startup_friendly: If True, only return startup-friendly scenarios.
            exclude_ids: List of scenario IDs to exclude.
            
        Returns:
            List of pair programming scenario dictionaries matching the criteria.
        """
        scenarios = self.pair_programming_scenarios.get("scenarios", [])
        exclude_ids = exclude_ids or []
        
        filtered = []
        for s in scenarios:
            # Skip excluded scenarios
            if s.get("id") in exclude_ids:
                continue
            
            # Filter by difficulty
            if difficulty and s.get("difficulty") != difficulty:
                continue
            
            # Filter by category
            if category and s.get("category") != category:
                continue
            
            # Filter by startup_friendly
            if startup_friendly and not s.get("startup_friendly", False):
                continue
            
            filtered.append(s)
        
        return filtered
    
    def select_random_question(
        self,
        question_type: str,
        **kwargs
    ) -> Optional[Dict[str, Any]]:
        """Select a random question from the specified type.
        
        Args:
            question_type: Type of question ('leetcode', 'system_design', 'pair_programming').
            **kwargs: Additional filter criteria passed to the getter methods.
            
        Returns:
            A random question dictionary, or None if no questions match.
        """
        if question_type == "leetcode":
            questions = self.get_leetcode_questions(**kwargs)
        elif question_type == "system_design":
            questions = self.get_system_design_questions(**kwargs)
        elif question_type == "pair_programming":
            questions = self.get_pair_programming_scenarios(**kwargs)
        else:
            raise ValueError(f"Unknown question type: {question_type}")
        
        if not questions:
            return None
        
        return random.choice(questions)
    
    def select_questions_for_session(
        self,
        question_type: str,
        count: int = 1,
        **kwargs
    ) -> List[Dict[str, Any]]:
        """Select multiple questions for an interview session.
        
        Args:
            question_type: Type of question ('leetcode', 'system_design', 'pair_programming').
            count: Number of questions to select.
            **kwargs: Additional filter criteria.
            
        Returns:
            List of question dictionaries.
        """
        if question_type == "leetcode":
            questions = self.get_leetcode_questions(**kwargs)
        elif question_type == "system_design":
            questions = self.get_system_design_questions(**kwargs)
        elif question_type == "pair_programming":
            questions = self.get_pair_programming_scenarios(**kwargs)
        else:
            raise ValueError(f"Unknown question type: {question_type}")
        
        if not questions:
            return []
        
        # Select random questions without replacement
        selected = random.sample(questions, min(count, len(questions)))
        return selected
    
    def get_question_by_id(
        self,
        question_type: str,
        question_id: str
    ) -> Optional[Dict[str, Any]]:
        """Get a specific question by its ID.
        
        Args:
            question_type: Type of question ('leetcode', 'system_design', 'pair_programming').
            question_id: ID of the question to retrieve.
            
        Returns:
            Question dictionary if found, None otherwise.
        """
        if question_type == "leetcode":
            questions = self.leetcode_questions.get("questions", [])
        elif question_type == "system_design":
            questions = self.system_design_questions.get("questions", [])
        elif question_type == "pair_programming":
            questions = self.pair_programming_scenarios.get("scenarios", [])
        else:
            raise ValueError(f"Unknown question type: {question_type}")
        
        for q in questions:
            if q.get("id") == question_id:
                return q
        
        return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about the question banks.
        
        Returns:
            Dictionary with statistics for each question type.
        """
        leetcode = self.leetcode_questions.get("questions", [])
        system_design = self.system_design_questions.get("questions", [])
        pair_programming = self.pair_programming_scenarios.get("scenarios", [])
        
        def count_by_difficulty(questions):
            counts = {"easy": 0, "medium": 0, "hard": 0}
            for q in questions:
                diff = q.get("difficulty", "unknown")
                if diff in counts:
                    counts[diff] += 1
            return counts
        
        return {
            "leetcode": {
                "total": len(leetcode),
                "by_difficulty": count_by_difficulty(leetcode),
                "startup_friendly": sum(1 for q in leetcode if q.get("startup_friendly", False))
            },
            "system_design": {
                "total": len(system_design),
                "by_difficulty": count_by_difficulty(system_design),
                "startup_friendly": sum(1 for q in system_design if q.get("startup_friendly", False))
            },
            "pair_programming": {
                "total": len(pair_programming),
                "by_difficulty": count_by_difficulty(pair_programming),
                "startup_friendly": sum(1 for s in pair_programming if s.get("startup_friendly", False))
            }
        }


if __name__ == "__main__":
    # Test the question bank
    qb = QuestionBank()
    
    print("Question Bank Statistics:")
    print("=" * 50)
    stats = qb.get_statistics()
    for q_type, data in stats.items():
        print(f"\n{q_type.upper()}:")
        print(f"  Total: {data['total']}")
        print(f"  By Difficulty: {data['by_difficulty']}")
        print(f"  Startup Friendly: {data['startup_friendly']}")
    
    print("\n" + "=" * 50)
    print("\nSample LeetCode Question (Easy, Startup Friendly):")
    sample = qb.select_random_question("leetcode", difficulty="easy", startup_friendly=True)
    if sample:
        print(f"  Title: {sample.get('title')}")
        print(f"  Category: {sample.get('category')}")
        print(f"  Description: {sample.get('description', '')[:100]}...")

