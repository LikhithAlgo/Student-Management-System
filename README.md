# Student Management System

A simple command-line student management system built with Python, using an in-memory dictionary to store student records.

## Features
- Add student records (USN, name, marks)
- View all student records
- Search for a student by USN (case-insensitive)
- Delete a student record by USN (case-insensitive)

## Tech Stack
- Python (no external libraries required)
- Dictionary-based data storage

## How to Run
1. Make sure you have Python installed
2. Run: `python main.py`

## Data Structure
Each student is stored as a dictionary entry, keyed by USN:
```python
students = {
    "1bm23cs001": {"name": "john", "marks": "85"}
}
```

## Known Limitations
- Data is stored only in memory — all records are lost when the program closes (no file or database persistence)
- Marks are stored as text, not numbers, so calculations like average or pass/fail aren't supported yet
- No input validation for empty fields or non-numeric marks

## Future Improvements
- Save and load records from a file (CSV/Excel) or database, so data persists between runs
- Store marks as integers to support sorting, averages, and grading
- Add input validation for empty or invalid entries
- Add a GUI using Tkinter or a web interface
