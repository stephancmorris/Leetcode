# Mock Interview System

A comprehensive mock interview framework designed to help you practice for technical interviews. This system supports LeetCode-style coding problems, system design questions, and pair programming scenarios.

## 📚 Contents

### Core Scripts
- **interview_runner.py**: Main script to run mock interviews interactively
- **question_bank.py**: Question management and selection logic
- **session_tracker.py**: Session tracking and history management
- **analytics.py**: Performance analytics and report generation

### Question Banks
- **question_banks/leetcode_questions.json**: LeetCode-style coding problems
- **question_banks/system_design_questions.json**: System design scenarios
- **question_banks/pair_programming_scenarios.json**: Pair programming tasks

### Data Storage
- **sessions/session_history.json**: All interview session data
- **reports/**: Generated performance reports (created automatically)

## 🎯 Purpose

This folder provides:
- **Interview practice**: Simulate real interview conditions with timers and tracking
- **Progress tracking**: Monitor your performance over time
- **Analytics**: Identify weak areas and track improvement
- **Multiple interview types**: Practice coding, system design, and pair programming

## 📖 Features

### Three Interview Types

1. **LeetCode Interviews**
   - Coding problems from Easy to Hard difficulty
   - Categories: Arrays, Strings, Trees, Linked Lists, etc.
   - Built-in timer functionality
   - Hints available for problems
   - Integration with existing problem files

2. **System Design Interviews**
   - Real-world system design scenarios
   - Requirements clarification guidance
   - Evaluation criteria provided
   - Startup-scale problems
   - Expected duration guidance

3. **Pair Programming Sessions**
   - Real-world coding tasks
   - API endpoint implementation
   - Data processing challenges
   - Feature implementation scenarios
   - Bug fixing and refactoring tasks

### Analytics and Tracking

- **Session metrics**: Time per question, completion rates, self-ratings
- **Performance analysis**: Trends over time, weak area identification
- **Personalized recommendations**: Suggestions for improvement
- **Report generation**: Detailed performance reports saved automatically

## 🔧 Usage

### Running an Interview
```bash
python interview_runner.py
```

### Viewing Analytics
```bash
python analytics.py
```

### Session Commands
- `done` - Mark question as completed
- `hint` - Get hints for the problem
- `skip` - Skip to next question
- `show` - Redisplay the question

## 📖 What's Included

### Interview Types Details

**LeetCode Interviews:**
- Problems organized by difficulty and category
- Timer tracking for each problem
- Performance rating system
- Notes and observations tracking

**System Design Interviews:**
- Topics: URL shorteners, chat systems, analytics dashboards, file storage, rate limiting
- Structured interview format guidance
- Scale estimation practice
- Architecture design scenarios

**Pair Programming Sessions:**
- REST API endpoint implementation
- Data processing and aggregation
- Search feature implementation
- Performance debugging
- Code refactoring scenarios
- Third-party API integration

### Analytics Features

- Overall statistics (total sessions, completion rates)
- Performance breakdown by interview type
- Time trend analysis
- Weak area identification
- Personalized improvement recommendations

## 🔗 Integration

This system integrates with:
- **03_Blind_75/**: References existing LeetCode problem files
- **08_System_Design/**: Uses system design concepts and examples
- **07_Study_Guides/**: Complements study guide materials

## 📝 Customization

### Adding Questions
Edit the JSON files in `question_banks/` to add new questions following the existing format.

### Question Format
```json
{
  "id": "unique_id",
  "title": "Question Title",
  "difficulty": "easy|medium|hard",
  "category": "category_name",
  "description": "Problem description",
  "startup_friendly": true
}
```

### Filtering Options
Questions can be filtered by:
- Difficulty level
- Category/tags
- Startup-friendly flag
- Question type

## 🎯 Key Capabilities

- **Interactive CLI**: User-friendly command-line interface
- **Timer functionality**: Track time spent on each problem
- **Progress tracking**: Automatic session history
- **Analytics reports**: Detailed performance insights
- **Question management**: Curated question banks with varying difficulty
- **Session history**: Review past interviews and performance
