"""
Session Tracker
Tracks and manages mock interview sessions, storing performance metrics and history.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any


class SessionTracker:
    """Manages interview session tracking and history."""
    
    def __init__(self, base_path: Optional[str] = None):
        """Initialize the session tracker.
        
        Args:
            base_path: Base path to the sessions directory.
                      If None, uses the directory containing this file.
        """
        if base_path is None:
            base_path = Path(__file__).parent
        else:
            base_path = Path(base_path)
        
        self.base_path = base_path
        self.sessions_path = base_path / "sessions"
        self.sessions_path.mkdir(exist_ok=True)
        self.history_file = self.sessions_path / "session_history.json"
        
        # Load existing session history
        self.sessions = self._load_history()
    
    def _load_history(self) -> List[Dict[str, Any]]:
        """Load session history from file.
        
        Returns:
            List of session dictionaries.
        """
        if not self.history_file.exists():
            return []
        
        try:
            with open(self.history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load session history: {e}")
            return []
    
    def _save_history(self):
        """Save session history to file."""
        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(self.sessions, f, indent=2, default=str)
        except IOError as e:
            print(f"Error saving session history: {e}")
    
    def start_session(
        self,
        interview_type: str,
        question_ids: List[str],
        difficulty: Optional[str] = None
    ) -> str:
        """Start a new interview session.
        
        Args:
            interview_type: Type of interview ('leetcode', 'system_design', 'pair_programming').
            question_ids: List of question IDs for this session.
            difficulty: Overall difficulty level.
            
        Returns:
            Session ID string.
        """
        session_id = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{interview_type}"
        
        session = {
            "session_id": session_id,
            "interview_type": interview_type,
            "question_ids": question_ids,
            "difficulty": difficulty,
            "start_time": datetime.now().isoformat(),
            "end_time": None,
            "duration_seconds": None,
            "questions": [],
            "overall_performance": {
                "completed": False,
                "time_taken": None,
                "accuracy": None,
                "rating": None,
                "notes": ""
            },
            "metrics": {
                "total_questions": len(question_ids),
                "questions_attempted": 0,
                "questions_completed": 0,
                "average_time_per_question": None
            }
        }
        
        self.sessions.append(session)
        self._save_history()
        
        return session_id
    
    def update_question(
        self,
        session_id: str,
        question_id: str,
        status: str,
        time_taken: Optional[float] = None,
        notes: Optional[str] = None,
        rating: Optional[int] = None
    ):
        """Update a question's status in a session.
        
        Args:
            session_id: ID of the session.
            question_id: ID of the question.
            status: Status ('attempted', 'completed', 'skipped').
            time_taken: Time taken in seconds.
            notes: Optional notes about the question.
            rating: Optional self-rating (1-5).
        """
        session = self._get_session(session_id)
        if not session:
            return
        
        # Find or create question entry
        question_entry = None
        for q in session["questions"]:
            if q["question_id"] == question_id:
                question_entry = q
                break
        
        if not question_entry:
            question_entry = {
                "question_id": question_id,
                "status": status,
                "time_taken": time_taken,
                "notes": notes or "",
                "rating": rating,
                "updated_at": datetime.now().isoformat()
            }
            session["questions"].append(question_entry)
        else:
            question_entry["status"] = status
            if time_taken is not None:
                question_entry["time_taken"] = time_taken
            if notes is not None:
                question_entry["notes"] = notes
            if rating is not None:
                question_entry["rating"] = rating
            question_entry["updated_at"] = datetime.now().isoformat()
        
        # Update session metrics
        session["metrics"]["questions_attempted"] = len([
            q for q in session["questions"]
            if q["status"] in ["attempted", "completed"]
        ])
        session["metrics"]["questions_completed"] = len([
            q for q in session["questions"]
            if q["status"] == "completed"
        ])
        
        # Calculate average time
        times = [q["time_taken"] for q in session["questions"] if q.get("time_taken")]
        if times:
            session["metrics"]["average_time_per_question"] = sum(times) / len(times)
        
        self._save_history()
    
    def end_session(
        self,
        session_id: str,
        overall_rating: Optional[int] = None,
        notes: Optional[str] = None
    ):
        """End an interview session.
        
        Args:
            session_id: ID of the session.
            overall_rating: Overall self-rating for the session (1-5).
            notes: Optional overall notes about the session.
        """
        session = self._get_session(session_id)
        if not session:
            return
        
        session["end_time"] = datetime.now().isoformat()
        session["overall_performance"]["completed"] = True
        
        # Calculate duration
        start_time = datetime.fromisoformat(session["start_time"])
        end_time = datetime.fromisoformat(session["end_time"])
        duration = (end_time - start_time).total_seconds()
        session["duration_seconds"] = duration
        
        # Update overall performance
        if overall_rating is not None:
            session["overall_performance"]["rating"] = overall_rating
        
        if notes:
            session["overall_performance"]["notes"] = notes
        
        # Calculate accuracy (completion rate)
        total = session["metrics"]["total_questions"]
        completed = session["metrics"]["questions_completed"]
        if total > 0:
            session["overall_performance"]["accuracy"] = completed / total
        
        session["overall_performance"]["time_taken"] = duration
        
        self._save_history()
    
    def _get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get a session by ID.
        
        Args:
            session_id: ID of the session.
            
        Returns:
            Session dictionary or None if not found.
        """
        for session in self.sessions:
            if session["session_id"] == session_id:
                return session
        return None
    
    def get_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get a session by ID (public method).
        
        Args:
            session_id: ID of the session.
            
        Returns:
            Session dictionary or None if not found.
        """
        return self._get_session(session_id)
    
    def get_all_sessions(
        self,
        interview_type: Optional[str] = None,
        completed_only: bool = False
    ) -> List[Dict[str, Any]]:
        """Get all sessions, optionally filtered.
        
        Args:
            interview_type: Filter by interview type.
            completed_only: If True, only return completed sessions.
            
        Returns:
            List of session dictionaries.
        """
        sessions = self.sessions.copy()
        
        if interview_type:
            sessions = [s for s in sessions if s["interview_type"] == interview_type]
        
        if completed_only:
            sessions = [
                s for s in sessions
                if s["overall_performance"]["completed"]
            ]
        
        # Sort by start time (most recent first)
        sessions.sort(key=lambda x: x["start_time"], reverse=True)
        
        return sessions
    
    def get_recent_sessions(self, count: int = 10) -> List[Dict[str, Any]]:
        """Get the most recent sessions.
        
        Args:
            count: Number of sessions to return.
            
        Returns:
            List of session dictionaries.
        """
        all_sessions = self.get_all_sessions()
        return all_sessions[:count]
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get overall statistics from all sessions.
        
        Returns:
            Dictionary with statistics.
        """
        completed_sessions = self.get_all_sessions(completed_only=True)
        
        if not completed_sessions:
            return {
                "total_sessions": 0,
                "completed_sessions": 0,
                "by_type": {},
                "average_rating": None,
                "average_accuracy": None,
                "average_duration": None
            }
        
        # Statistics by type
        by_type = {}
        for session in completed_sessions:
            interview_type = session["interview_type"]
            if interview_type not in by_type:
                by_type[interview_type] = {
                    "count": 0,
                    "ratings": [],
                    "accuracies": [],
                    "durations": []
                }
            
            by_type[interview_type]["count"] += 1
            if session["overall_performance"].get("rating"):
                by_type[interview_type]["ratings"].append(
                    session["overall_performance"]["rating"]
                )
            if session["overall_performance"].get("accuracy"):
                by_type[interview_type]["accuracies"].append(
                    session["overall_performance"]["accuracy"]
                )
            if session.get("duration_seconds"):
                by_type[interview_type]["durations"].append(
                    session["duration_seconds"]
                )
        
        # Calculate averages
        for interview_type in by_type:
            stats = by_type[interview_type]
            stats["average_rating"] = (
                sum(stats["ratings"]) / len(stats["ratings"])
                if stats["ratings"] else None
            )
            stats["average_accuracy"] = (
                sum(stats["accuracies"]) / len(stats["accuracies"])
                if stats["accuracies"] else None
            )
            stats["average_duration"] = (
                sum(stats["durations"]) / len(stats["durations"])
                if stats["durations"] else None
            )
            # Remove raw lists
            del stats["ratings"]
            del stats["accuracies"]
            del stats["durations"]
        
        # Overall averages
        all_ratings = [
            s["overall_performance"]["rating"]
            for s in completed_sessions
            if s["overall_performance"].get("rating")
        ]
        all_accuracies = [
            s["overall_performance"]["accuracy"]
            for s in completed_sessions
            if s["overall_performance"].get("accuracy")
        ]
        all_durations = [
            s["duration_seconds"]
            for s in completed_sessions
            if s.get("duration_seconds")
        ]
        
        return {
            "total_sessions": len(self.sessions),
            "completed_sessions": len(completed_sessions),
            "by_type": by_type,
            "average_rating": (
                sum(all_ratings) / len(all_ratings) if all_ratings else None
            ),
            "average_accuracy": (
                sum(all_accuracies) / len(all_accuracies) if all_accuracies else None
            ),
            "average_duration": (
                sum(all_durations) / len(all_durations) if all_durations else None
            )
        }
    
    def get_question_performance(self, question_id: str) -> Dict[str, Any]:
        """Get performance statistics for a specific question.
        
        Args:
            question_id: ID of the question.
            
        Returns:
            Dictionary with performance statistics.
        """
        attempts = []
        for session in self.sessions:
            for q in session.get("questions", []):
                if q["question_id"] == question_id:
                    attempts.append({
                        "session_id": session["session_id"],
                        "status": q["status"],
                        "time_taken": q.get("time_taken"),
                        "rating": q.get("rating"),
                        "date": session["start_time"]
                    })
        
        if not attempts:
            return {
                "question_id": question_id,
                "total_attempts": 0,
                "completion_rate": None,
                "average_time": None,
                "average_rating": None
            }
        
        completed = [a for a in attempts if a["status"] == "completed"]
        times = [a["time_taken"] for a in attempts if a.get("time_taken")]
        ratings = [a["rating"] for a in attempts if a.get("rating")]
        
        return {
            "question_id": question_id,
            "total_attempts": len(attempts),
            "completion_rate": len(completed) / len(attempts) if attempts else 0,
            "average_time": sum(times) / len(times) if times else None,
            "average_rating": sum(ratings) / len(ratings) if ratings else None,
            "attempts": attempts
        }


if __name__ == "__main__":
    # Test the session tracker
    tracker = SessionTracker()
    
    print("Session Tracker Test")
    print("=" * 50)
    
    # Create a test session
    session_id = tracker.start_session(
        interview_type="leetcode",
        question_ids=["two_sum", "contains_duplicate"],
        difficulty="easy"
    )
    print(f"Created session: {session_id}")
    
    # Update a question
    tracker.update_question(
        session_id,
        "two_sum",
        status="completed",
        time_taken=15.5,
        rating=4
    )
    print("Updated question: two_sum")
    
    # End session
    tracker.end_session(session_id, overall_rating=4, notes="Good session!")
    print("Ended session")
    
    # Get statistics
    stats = tracker.get_statistics()
    print(f"\nStatistics:")
    print(f"  Total sessions: {stats['total_sessions']}")
    print(f"  Completed sessions: {stats['completed_sessions']}")

