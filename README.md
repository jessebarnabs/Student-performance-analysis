# Student Performance Analysis System

A Python program that reads student records from a CSV file, calculates averages and grades, checks scholarship eligibility, and prints a performance report. Built with object-oriented programming for an Africa International University assignment.

## Files
- `student_analysis.py`: the program (all classes, the CSV loader, and the demos)
- `students.csv`: the dataset (6 student records)
- `REFLECTION.md`: my reflection on the challenges I met, and my AI use declaration

## How to run
1. Install Python 3.
2. Download all the files into the **same folder**.
3. Open a terminal in that folder and run:

```
python student_analysis.py
```

(On some Windows computers the command is `py student_analysis.py`.)

## The dataset
`students.csv` has these columns:

`StudentID, FName, LName, Programme, Math, English, Science, ScholarshipAmount`

A `ScholarshipAmount` above 0 means the student holds a scholarship.

## OOP concepts demonstrated
| Concept | Where it is |
|---|---|
| **Encapsulation** | `Student` keeps its marks in a private attribute (`__marks`) and uses protected attributes (`_first_name`, etc.). Marks can only be changed through `set_mark()`, which rejects anything outside 0 to 100 |
| **Abstraction** | `Student` is an abstract class with an abstract method `get_summary()`, so a plain `Student`
