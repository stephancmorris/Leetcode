#!/usr/bin/env python3
"""
Analytics Module
Generates performance reports, identifies weak areas, and shows progress trends.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict

from session_tracker import SessionTracker
from question_bank import QuestionBank


class Analytics:
    """Generates analytics and reports from interview sessions."""
    
    def __init__(self, base_path: Optional[str] = None):
        """Initialize analytics.
        
        Args:
            base_path: Base path to the sessions directory.
        """
        self.session_tracker = SessionTracker(base_path)
        self.question_bank = QuestionBank(base_path)
        self.base_path = Path(base_path) if base_path else Path(__file__).parent
        self.reports_path = self.base_path / "reports"
        self.reports_path.mkdir(exist_ok=True)
    
    def generate_performance_report(self) -> Dict[str, Any]:
        """Generate a comprehensive performance report.
        
        Returns:
            Dictionary containing performance metrics and analysis.
        """
        sessions = self.session_tracker.get_all_sessions(completed_only=True)
        
        if not sessions:
            return {
                "summary": "No completed sessions found.",
                "recommendations": ["Start practicing to generate analytics!"]
            }
        
        # Overall statistics
        total_sessions = len(sessions)
        total_questions = sum(len(s["question_ids"]) for s in sessions)
        completed_questions = sum(
            s["metrics"]["questions_completed"] for s in sessions
        )
        
        # Performance by type
        by_type = defaultdict(lambda: {
            "sessions": [],
            "total_questions": 0,
            "completed_questions": 0,
            "ratings": [],
            "durations": []
        })
        
        for session in sessions:
            interview_type = session["interview_type"]
            by_type[interview_type]["sessions"].append(session)
            by_type[interview_type]["total_questions"] += len(session["question_ids"])
            by_type[interview_type]["completed_questions"] += session["metrics"]["questions_completed"]
            
            if session["overall_performance"].get("rating"):
                by_type[interview_type]["ratings"].append(
                    session["overall_performance"]["rating"]
                )
            if session.get("duration_seconds"):
                by_type[interview_type]["durations"].append(
                    session["duration_seconds"]
                )
        
        # Calculate averages by type
        type_stats = {}
        for interview_type, data in by_type.items():
            type_stats[interview_type] = {
                "session_count": len(data["sessions"]),
                "completion_rate": (
                    data["completed_questions"] / data["total_questions"]
                    if data["total_questions"] > 0 else 0
                ),
                "average_rating": (
                    sum(data["ratings"]) / len(data["ratings"])
                    if data["ratings"] else None
                ),
                "average_duration_minutes": (
                    sum(data["durations"]) / len(data["durations"]) / 60
                    if data["durations"] else None
                )
            }
        
        # Time trends
        time_trends = self._calculate_time_trends(sessions)
        
        # Weak areas
        weak_areas = self._identify_weak_areas(sessions)
        
        # Recommendations
        recommendations = self._generate_recommendations(
            type_stats, weak_areas, time_trends
        )
        
        return {
            "generated_at": datetime.now().isoformat(),
            "summary": {
                "total_sessions": total_sessions,
                "total_questions": total_questions,
                "completed_questions": completed_questions,
                "overall_completion_rate": (
                    completed_questions / total_questions
                    if total_questions > 0 else 0
                )
            },
            "by_type": type_stats,
            "time_trends": time_trends,
            "weak_areas": weak_areas,
            "recommendations": recommendations
        }
    
    def _calculate_time_trends(self, sessions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate time-based trends.
        
        Args:
            sessions: List of completed sessions.
            
        Returns:
            Dictionary with trend analysis.
        """
        if len(sessions) < 2:
            return {"message": "Need at least 2 sessions to calculate trends"}
        
        # Sort by date
        sorted_sessions = sorted(
            sessions,
            key=lambda x: x["start_time"]
        )
        
        # Calculate improvement over time
        first_half = sorted_sessions[:len(sorted_sessions)//2]
        second_half = sorted_sessions[len(sorted_sessions)//2:]
        
        def avg_rating(sessions_list):
            ratings = [
                s["overall_performance"]["rating"]
                for s in sessions_list
                if s["overall_performance"].get("rating")
            ]
            return sum(ratings) / len(ratings) if ratings else None
        
        def avg_duration(sessions_list):
            durations = [
                s["duration_seconds"]
                for s in sessions_list
                if s.get("duration_seconds")
            ]
            return sum(durations) / len(durations) / 60 if durations else None
        
        first_rating = avg_rating(first_half)
        second_rating = avg_rating(second_half)
        first_duration = avg_duration(first_half)
        second_duration = avg_duration(second_half)
        
        rating_improvement = None
        if first_rating and second_rating:
            rating_improvement = second_rating - first_rating
        
        duration_change = None
        if first_duration and second_duration:
            duration_change = second_duration - first_duration
        
        return {
            "rating_trend": {
                "first_half_avg": first_rating,
                "second_half_avg": second_rating,
                "improvement": rating_improvement,
                "improving": rating_improvement > 0 if rating_improvement else None
            },
            "duration_trend": {
                "first_half_avg_minutes": first_duration,
                "second_half_avg_minutes": second_duration,
                "change_minutes": duration_change,
                "getting_faster": duration_change < 0 if duration_change else None
            }
        }
    
    def _identify_weak_areas(self, sessions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Identify weak areas based on performance.
        
        Args:
            sessions: List of completed sessions.
            
        Returns:
            Dictionary identifying weak areas.
        """
        # Track question performance
        question_performance = defaultdict(lambda: {
            "attempts": 0,
            "completed": 0,
            "ratings": [],
            "times": []
        })
        
        for session in sessions:
            for question in session.get("questions", []):
                q_id = question["question_id"]
                question_performance[q_id]["attempts"] += 1
                if question["status"] == "completed":
                    question_performance[q_id]["completed"] += 1
                if question.get("rating"):
                    question_performance[q_id]["ratings"].append(question["rating"])
                if question.get("time_taken"):
                    question_performance[q_id]["times"].append(question["time_taken"])
        
        # Find weak questions (low completion rate or low ratings)
        weak_questions = []
        for q_id, perf in question_performance.items():
            completion_rate = perf["completed"] / perf["attempts"] if perf["attempts"] > 0 else 0
            avg_rating = (
                sum(perf["ratings"]) / len(perf["ratings"])
                if perf["ratings"] else None
            )
            
            if completion_rate < 0.5 or (avg_rating and avg_rating < 3):
                weak_questions.append({
                    "question_id": q_id,
                    "completion_rate": completion_rate,
                    "average_rating": avg_rating,
                    "attempts": perf["attempts"]
                })
        
        # Track performance by category (for LeetCode)
        category_performance = defaultdict(lambda: {
            "total": 0,
            "completed": 0,
            "ratings": []
        })
        
        for session in sessions:
            if session["interview_type"] == "leetcode":
                for question in session.get("questions", []):
                    q_id = question["question_id"]
                    q_data = self.question_bank.get_question_by_id("leetcode", q_id)
                    if q_data:
                        category = q_data.get("category", "unknown")
                        category_performance[category]["total"] += 1
                        if question["status"] == "completed":
                            category_performance[category]["completed"] += 1
                        if question.get("rating"):
                            category_performance[category]["ratings"].append(
                                question["rating"]
                            )
        
        weak_categories = []
        for category, perf in category_performance.items():
            if perf["total"] > 0:
                completion_rate = perf["completed"] / perf["total"]
                avg_rating = (
                    sum(perf["ratings"]) / len(perf["ratings"])
                    if perf["ratings"] else None
                )
                
                if completion_rate < 0.6 or (avg_rating and avg_rating < 3):
                    weak_categories.append({
                        "category": category,
                        "completion_rate": completion_rate,
                        "average_rating": avg_rating,
                        "total_attempts": perf["total"]
                    })
        
        return {
            "weak_questions": sorted(
                weak_questions,
                key=lambda x: x["completion_rate"]
            )[:10],  # Top 10 weakest
            "weak_categories": sorted(
                weak_categories,
                key=lambda x: x.get("completion_rate", 0)
            )
        }
    
    def _generate_recommendations(
        self,
        type_stats: Dict[str, Dict[str, Any]],
        weak_areas: Dict[str, Any],
        time_trends: Dict[str, Any]
    ) -> List[str]:
        """Generate recommendations based on analytics.
        
        Args:
            type_stats: Statistics by interview type.
            weak_areas: Identified weak areas.
            time_trends: Time-based trends.
            
        Returns:
            List of recommendation strings.
        """
        recommendations = []
        
        # Check completion rates
        for interview_type, stats in type_stats.items():
            if stats["completion_rate"] < 0.7:
                recommendations.append(
                    f"Focus on completing more {interview_type} questions. "
                    f"Current completion rate: {stats['completion_rate']*100:.1f}%"
                )
        
        # Check weak categories
        if weak_areas.get("weak_categories"):
            categories = [w["category"] for w in weak_areas["weak_categories"][:3]]
            recommendations.append(
                f"Practice more in these categories: {', '.join(categories)}"
            )
        
        # Check weak questions
        if weak_areas.get("weak_questions"):
            recommendations.append(
                f"Revisit {len(weak_areas['weak_questions'])} questions where you struggled. "
                "Consider reviewing solutions and trying again."
            )
        
        # Check time trends
        if time_trends.get("rating_trend"):
            rating_trend = time_trends["rating_trend"]
            if not rating_trend.get("improving") and rating_trend.get("improving") is not None:
                recommendations.append(
                    "Your ratings haven't improved recently. Consider reviewing "
                    "fundamentals or focusing on specific problem patterns."
                )
        
        # General recommendations
        total_sessions = sum(s["session_count"] for s in type_stats.values())
        if total_sessions < 5:
            recommendations.append(
                "Practice more regularly! Aim for at least 3-5 sessions per week."
            )
        
        if not recommendations:
            recommendations.append(
                "Great job! Keep practicing to maintain your skills."
            )
        
        return recommendations
    
    def print_report(self, report: Optional[Dict[str, Any]] = None):
        """Print a formatted performance report.
        
        Args:
            report: Report dictionary. If None, generates a new report.
        """
        if report is None:
            report = self.generate_performance_report()
        
        print("\n" + "=" * 70)
        print(" " * 20 + "PERFORMANCE REPORT")
        print("=" * 70)
        print(f"\nGenerated: {report.get('generated_at', 'N/A')}")
        
        # Summary
        if "summary" in report:
            summary = report["summary"]
            if isinstance(summary, dict):
                print("\n" + "-" * 70)
                print("SUMMARY")
                print("-" * 70)
                print(f"Total Sessions: {summary.get('total_sessions', 0)}")
                print(f"Total Questions: {summary.get('total_questions', 0)}")
                print(f"Completed Questions: {summary.get('completed_questions', 0)}")
                completion_rate = summary.get('overall_completion_rate', 0)
                print(f"Completion Rate: {completion_rate*100:.1f}%")
            else:
                print(f"\n{summary}")
                return
        
        # By type
        if "by_type" in report and report["by_type"]:
            print("\n" + "-" * 70)
            print("PERFORMANCE BY INTERVIEW TYPE")
            print("-" * 70)
            for interview_type, stats in report["by_type"].items():
                print(f"\n{interview_type.upper()}:")
                print(f"  Sessions: {stats['session_count']}")
                print(f"  Completion Rate: {stats['completion_rate']*100:.1f}%")
                if stats.get('average_rating'):
                    print(f"  Average Rating: {stats['average_rating']:.2f}/5")
                if stats.get('average_duration_minutes'):
                    print(f"  Average Duration: {stats['average_duration_minutes']:.1f} minutes")
        
        # Time trends
        if "time_trends" in report and isinstance(report["time_trends"], dict):
            trends = report["time_trends"]
            if "rating_trend" in trends:
                print("\n" + "-" * 70)
                print("RATING TREND")
                print("-" * 70)
                rt = trends["rating_trend"]
                if rt.get("improving") is not None:
                    if rt["improving"]:
                        print("✓ Your ratings are improving!")
                    else:
                        print("⚠️  Your ratings need improvement")
                    print(f"  First half average: {rt.get('first_half_avg', 'N/A')}")
                    print(f"  Second half average: {rt.get('second_half_avg', 'N/A')}")
        
        # Weak areas
        if "weak_areas" in report:
            weak_areas = report["weak_areas"]
            print("\n" + "-" * 70)
            print("WEAK AREAS")
            print("-" * 70)
            
            if weak_areas.get("weak_categories"):
                print("\nCategories to focus on:")
                for cat in weak_areas["weak_categories"][:5]:
                    print(f"  • {cat['category']}: "
                          f"{cat['completion_rate']*100:.1f}% completion, "
                          f"{cat.get('average_rating', 'N/A')} avg rating")
            
            if weak_areas.get("weak_questions"):
                print(f"\nQuestions to revisit ({len(weak_areas['weak_questions'])}):")
                for q in weak_areas["weak_questions"][:5]:
                    print(f"  • {q['question_id']}: "
                          f"{q['completion_rate']*100:.1f}% completion")
        
        # Recommendations
        if "recommendations" in report:
            print("\n" + "-" * 70)
            print("RECOMMENDATIONS")
            print("-" * 70)
            for i, rec in enumerate(report["recommendations"], 1):
                print(f"{i}. {rec}")
        
        print("\n" + "=" * 70)
    
    def save_report(self, filename: Optional[str] = None) -> str:
        """Save a performance report to a JSON file.
        
        Args:
            filename: Optional filename. If None, generates one based on timestamp.
            
        Returns:
            Path to the saved report file.
        """
        report = self.generate_performance_report()
        
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"performance_report_{timestamp}.json"
        
        if not filename.endswith(".json"):
            filename += ".json"
        
        file_path = self.reports_path / filename
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, default=str)
        
        return str(file_path)


if __name__ == "__main__":
    analytics = Analytics()
    
    print("Generating performance report...")
    report = analytics.generate_performance_report()
    analytics.print_report(report)
    
    # Save report
    report_path = analytics.save_report()
    print(f"\n✓ Report saved to: {report_path}")

