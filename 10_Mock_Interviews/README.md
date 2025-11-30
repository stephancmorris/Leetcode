# Mock Interview System

A comprehensive mock interview framework designed to help you practice for technical interviews at startups and smaller companies. This system supports LeetCode-style coding problems, system design questions, and pair programming scenarios.

## Features

- **Three Interview Types**: LeetCode coding, System Design, and Pair Programming
- **Interactive CLI**: User-friendly command-line interface for conducting interviews
- **Timer Functionality**: Built-in timers to track your performance
- **Progress Tracking**: Automatic session tracking and performance metrics
- **Analytics & Reports**: Detailed analytics to identify weak areas and track improvement
- **Startup-Focused**: Questions tailored for smaller companies (practical, less theoretical)
- **Question Banks**: Curated questions with varying difficulty levels

## Quick Start

### Running a Mock Interview

```bash
cd 10_Mock_Interviews
python interview_runner.py
```

This will launch the interactive interview system. Follow the on-screen prompts to:
1. Select interview type (LeetCode, System Design, or Pair Programming)
2. Choose difficulty level
3. Start practicing!

### Viewing Analytics

```bash
python analytics.py
```

This generates and displays a comprehensive performance report showing:
- Overall statistics
- Performance by interview type
- Time trends
- Weak areas identification
- Personalized recommendations

## Directory Structure

```
10_Mock_Interviews/
├── interview_runner.py          # Main interview execution script
├── question_bank.py              # Question management and selection
├── session_tracker.py            # Session tracking and history
├── analytics.py                  # Performance analytics and reports
├── question_banks/
│   ├── leetcode_questions.json
│   ├── system_design_questions.json
│   └── pair_programming_scenarios.json
├── sessions/
│   └── session_history.json      # All session data
├── reports/
│   └── (generated performance reports)
└── README.md
```

## Interview Types

### 1. LeetCode Interview

Practice coding problems similar to those asked in technical interviews.

**Features:**
- Problems from Easy to Hard difficulty
- Categories: Arrays, Strings, Trees, Linked Lists, etc.
- Timer for each problem
- Hints available
- Integration with existing problem files

**Example Session:**
```
1. Select "Start LeetCode Interview"
2. Choose difficulty (Easy/Medium/Hard/Random)
3. Select number of questions (1-3)
4. Work on problems with timer
5. Mark as done when finished
6. Rate your performance
```

**Commands During Interview:**
- `done` - Mark question as completed
- `hint` - Get hints for the problem
- `skip` - Skip to next question
- `show` - Redisplay the question

### 2. System Design Interview

Practice designing scalable systems for startup-scale applications.

**Features:**
- Real-world system design scenarios
- Requirements clarification guidance
- Evaluation criteria provided
- Startup-scale problems (not Google-scale)
- Expected duration guidance

**Example Topics:**
- URL Shortener (bit.ly)
- Todo Application
- Real-time Chat Application
- Analytics Dashboard
- File Storage System
- Rate Limiting System

**Interview Structure:**
1. Requirements clarification (5-10 min)
2. High-level design (10-15 min)
3. Detailed design (15-20 min)
4. Scaling considerations (10-15 min)
5. Follow-up questions (5-10 min)

### 3. Pair Programming Session

Practice collaborative coding scenarios common in startup environments.

**Features:**
- Real-world coding tasks
- API endpoint implementation
- Data processing challenges
- Feature implementation
- Bug fixing and refactoring
- Integration tasks

**Example Scenarios:**
- Build a REST API endpoint
- Process and aggregate data
- Implement a search feature
- Debug performance issues
- Refactor legacy code
- Integrate third-party APIs

## Usage Guide

### Starting an Interview Session

1. **Launch the system:**
   ```bash
   python interview_runner.py
   ```

2. **Select interview type:**
   - Option 1: LeetCode Interview
   - Option 2: System Design Interview
   - Option 3: Pair Programming Session

3. **Choose difficulty:**
   - Easy: Good for warm-up and fundamentals
   - Medium: Standard interview level
   - Hard: Advanced practice
   - Random: Mix of difficulties

4. **Work through questions:**
   - Read the problem carefully
   - Think through your approach
   - Implement your solution
   - Use hints if stuck
   - Mark as done when finished

5. **Rate your performance:**
   - Provide a self-rating (1-5)
   - Add notes about what you learned
   - Review your session

### Viewing Session History

From the main menu, select "View Recent Sessions" to see:
- Recent interview sessions
- Completion status
- Duration and ratings
- Question details

### Generating Analytics Reports

Run the analytics module to get insights:

```bash
python analytics.py
```

**Report includes:**
- Overall statistics (sessions, completion rates)
- Performance by interview type
- Time trends (improvement over time)
- Weak areas identification
- Personalized recommendations

**Saving reports:**
Reports are automatically saved to the `reports/` directory with timestamps.

## Best Practices

### For LeetCode Interviews

1. **Time Management:**
   - Easy: 15-20 minutes
   - Medium: 25-35 minutes
   - Hard: 40-60 minutes

2. **Problem-Solving Approach:**
   - Read the problem carefully
   - Clarify edge cases
   - Think out loud
   - Start with brute force, then optimize
   - Test with examples

3. **Communication:**
   - Explain your thought process
   - Discuss trade-offs
   - Ask clarifying questions
   - Walk through examples

### For System Design Interviews

1. **Requirements First:**
   - Always clarify requirements
   - Ask about scale and constraints
   - Understand functional vs non-functional requirements

2. **Start Simple:**
   - Begin with basic design
   - Add complexity gradually
   - Justify your decisions

3. **Key Areas to Cover:**
   - API design
   - Database schema
   - Caching strategy
   - Scaling considerations
   - Trade-off analysis

### For Pair Programming Sessions

1. **Collaboration:**
   - Think out loud
   - Discuss approach before coding
   - Ask for feedback
   - Consider edge cases together

2. **Code Quality:**
   - Write clean, readable code
   - Add comments where needed
   - Consider error handling
   - Think about testing

3. **Real-World Focus:**
   - Consider production concerns
   - Discuss performance implications
   - Think about maintainability

## Tracking Your Progress

### Session Metrics Tracked

- **Time per question**: How long you spend on each problem
- **Completion rate**: Percentage of questions completed
- **Self-ratings**: Your assessment of performance (1-5)
- **Notes**: Your observations and learnings

### Analytics Features

- **Trend Analysis**: See if you're improving over time
- **Weak Area Identification**: Automatically identifies categories/questions to focus on
- **Performance by Type**: Compare performance across interview types
- **Recommendations**: Personalized suggestions for improvement

### Regular Practice

Aim for:
- **3-5 sessions per week** for consistent improvement
- **Mix of interview types** to be well-rounded
- **Review weak areas** regularly
- **Track progress** using analytics

## Customization

### Adding Questions

Edit the JSON files in `question_banks/`:

- `leetcode_questions.json`: Add LeetCode problems
- `system_design_questions.json`: Add system design scenarios
- `pair_programming_scenarios.json`: Add pair programming tasks

**Question Format Example:**
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

### Filtering Questions

The system supports filtering by:
- Difficulty level
- Category/tags
- Startup-friendly flag
- Question type

## Integration with Existing Code

The system integrates with your existing problem files:

- **LeetCode problems**: References files in `03_Blind_75/`
- **System design materials**: Uses concepts from `08_System_Design/`
- **Test runners**: Can validate solutions using existing test infrastructure

## Tips for Success

1. **Consistency is Key**: Practice regularly, even if just 30 minutes a day
2. **Focus on Weak Areas**: Use analytics to identify and improve weak spots
3. **Time Yourself**: Get comfortable with time pressure
4. **Review Solutions**: After each session, review optimal solutions
5. **Explain Out Loud**: Practice explaining your approach (even to yourself)
6. **Start Simple**: Don't jump to complex solutions immediately
7. **Learn Patterns**: Focus on recognizing patterns, not memorizing solutions

## Troubleshooting

### No Questions Found

If you see "No questions found matching your criteria":
- Try selecting "Random" difficulty
- Check that question bank files exist in `question_banks/`
- Verify JSON files are valid

### Session Not Saving

- Check that `sessions/` directory exists and is writable
- Verify file permissions
- Check for JSON syntax errors in session history

### Analytics Not Working

- Ensure you have completed at least one session
- Check that `session_history.json` exists and is valid
- Verify all dependencies are installed

## Example Workflow

**Week 1:**
- Monday: 2 Easy LeetCode problems
- Wednesday: 1 System Design question
- Friday: 1 Pair Programming scenario

**Week 2:**
- Review analytics from Week 1
- Focus on identified weak areas
- Increase difficulty gradually

**Week 3:**
- Mix of Medium difficulty problems
- More system design practice
- Review time trends

**Week 4:**
- Full interview simulations (45-60 min)
- Hard problems for challenge
- Final analytics review

## Resources

- **LeetCode Problems**: See `03_Blind_75/` for problem files
- **System Design**: See `08_System_Design/` for design concepts
- **Study Guides**: Check `07_Study_Guides/` for interview tips

## Support

For issues or questions:
1. Check this README
2. Review the code comments
3. Check session history for debugging

## License

Part of the LeetCode Study Guide repository.

---

**Good luck with your interviews! 🚀**

Remember: The goal isn't to solve every problem perfectly, but to demonstrate problem-solving skills, communication, and continuous learning.

