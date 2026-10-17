import csv
import os

from abc import ABC, abstractmethod


class Student(ABC):
    """Represents a student and stores their personal details and marks."""

    def __init__(self, student_id, first_name, last_name, programme, marks):
        """Initializes a student object with the provided details."""
        self._student_id = student_id
        self._first_name = first_name
        self._last_name = last_name
        self._programme = programme

        self.__marks = {}
        for subject, mark in marks.items():
            self.set_mark(subject, mark)

    def get_student_id(self):
        """Returns the student's ID."""
        return self._student_id

    def get_full_name(self):
        """Returns the student's full name."""
        return f"{self._first_name} {self._last_name}"

    def get_programme(self):
        """Returns the programme of the student."""
        return self._programme

    def get_marks(self):
        """Returns the marks of the student."""
        return dict(self.__marks)

    def set_mark(self, subject, mark):
        """Sets the mark for a specific subject."""
        if not isinstance(mark, (int, float)) or not 0 <= mark <= 100:
            raise ValueError(
                f"Invalid mark for {subject}: {mark}. Must be a number between 0 and 100."
            )
        self.__marks[subject] = mark

    def average(self, *marks):
            """returns the average of the marks given, or of the student's own marks if no marks are provided."""
            if marks:
                values = list(marks)
            else:
                values = list(self.get_marks() .values())

            if not values:
                raise ValueError("No marks available to calculate average.")

            for value in values:
                if not isinstance(value, (int, float)) or not 0 <= value <= 100:
                    raise ValueError(f"Invalid mark: {value}. Must be a number between 0 and 100.")

            return sum(values) / len(values)

    def get_grade(self):
                """returns the grade of the student based on their average marks."""
                avg = self.average()
                if avg >= 80:
                    return "A"
                elif avg >= 70:
                    return "B"
                elif avg >= 60:
                    return "C"
                elif avg >= 50:
                    return "D"
                else:
                    return "F"


    @abstractmethod
    def get_summary(self):
        """returns a short description of the student. This method must be implemented by subclasses."""
        pass


class AIUStudent(Student):
    """Represents a student from AIU. inherits from the Student class."""

    def get_summary(self):
        """keeps the promise made by the student's abstract method."""
        return f"{self.get_full_name()} is an AIU student."

    def scholarship_status(self):
        """Regular students are not on the scholarship programme."""
        return "Not on scholarship programme"

class ScholarshipStudent(AIUStudent):
    """A student who has received a scholarship. Inherits from AIUStudent."""

    def __init__(self, student_id, first_name, last_name, programme, marks, scholarship_amount):
        super().__init__(student_id, first_name, last_name, programme, marks)
        self.scholarship_amount = scholarship_amount

    def is_eligible(self):
        """Eligible to keep the scholarship if the average is 85 or more."""
        return self.average() >= 85

    def get_summary(self):
        """overrides the parent's get_summary method to include scholarship information."""
        base_summary = super().get_summary()
        return f"{base_summary} Scholarship: KES {self.scholarship_amount:,}. Eligible: {'Yes' if self.is_eligible() else 'No'}"

    def scholarship_status(self):
        """Overrides the parent's method: shows if the scholarship can be kept."""
        if self.is_eligible():
            return f"KES {self.scholarship_amount:,} - Eligible"
        return f"KES {self.scholarship_amount:,} - Not eligible (average below 85)"

class PerformanceAnalyzer:
    """Analyzes the performance of students."""

    def __init__(self, students):
        if not students:
            raise ValueError("The students list cannot be empty.")
        self.students = students

    def highest_average(self):
        """Returns the student with the highest average marks."""
        return max(self.students, key=lambda s: s.average())

    def lowest_average(self):
        """Returns the student with the lowest average marks."""
        return min(self.students, key=lambda s: s.average())

    def class_average(self):
        """Returns the average of all students' averages."""
        return sum(s.average() for s in self.students) / len(self.students)

    def generate_report(self):
        """Builds the full performance report as one piece of text."""
        line = "=" * 62
        report = [line, "STUDENT PERFORMANCE REPORT", line]

        for s in self.students:
            marks_text = ", ".join(f"{subject}: {mark:g}" for subject, mark in s.get_marks().items())
            report.append(f"ID: {s.get_student_id()}   Name: {s.get_full_name()}")
            report.append(f"Programme: {s.get_programme()}")
            report.append(f"Marks: {marks_text}")
            report.append(f"Average: {s.average():.2f}   Grade: {s.get_grade()}")
            report.append(f"Scholarship: {s.scholarship_status()}")
            report.append("-" * 62)

        best = self.highest_average()
        worst = self.lowest_average()
        report.append("CLASS SUMMARY")
        report.append(f"Highest average: {best.average():.2f} ({best.get_full_name()})")
        report.append(f"Lowest average : {worst.average():.2f} ({worst.get_full_name()})")
        report.append(f"Class average  : {self.class_average():.2f}")
        report.append(line)
        return "\n".join(report)

def load_students(csv_path):
    """Reads the CSV file and returns a list of student objects."""
    students = []
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            marks = {
                "Math": float(row["Math"]),
                "English": float(row["English"]),
                "Science": float(row["Science"]),
            }
            amount = int(row["ScholarshipAmount"])
            if amount > 0:
                student = ScholarshipStudent(row["StudentID"], row["FName"], row["LName"],
                                             row["Programme"], marks, amount)
            else:
                student = AIUStudent(row["StudentID"], row["FName"], row["LName"],
                                     row["Programme"], marks)
            students.append(student)
    return students

if __name__ == "__main__":
    # Find students.csv in the same folder as this script
    folder = os.path.dirname(os.path.abspath(__file__))
    try:
        students = load_students(os.path.join(folder, "students.csv"))
    except FileNotFoundError:
        print("Could not find students.csv. Keep it in the same folder as this file.")
        raise SystemExit

    analyzer = PerformanceAnalyzer(students)
    print(analyzer.generate_report())

    print("\nPOLYMORPHISM DEMO (same method, different results):")
    for student in students:
        print(f"[{type(student).__name__}] {student.get_summary()}")

    print("\nFLEXIBLE METHOD DEMO:")
    first = students[0]
    print("No arguments (own marks):", first.average())
    print("Three marks (70, 80, 90):", first.average(70, 80, 90))
    print("Five marks (60, 70, 80, 90, 55):", first.average(60, 70, 80, 90, 55))
    try:
        first.average(70, 150)
    except ValueError as exc:
        print("Validation caught an error:", exc)

    print("\nENCAPSULATION DEMO:")
    try:
        first.set_mark("Math", 120)
    except ValueError as exc:
        print("Invalid mark rejected:", exc)

    print("\nABSTRACTION DEMO:")
    try:
        Student("25/999", "Test", "Person", "MDS", {"Math": 50})
    except TypeError as exc:
        print(exc)