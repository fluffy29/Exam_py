from flask import Flask, render_template
from faker import Faker

app = Flask(__name__)

fake = Faker()


def generate_fake_data():
    subject_names = ["Math", "Science", "History", "English", "Geography"]

    students = [{"id": i + 1, "name": fake.name()} for i in range(10)]

    subjects = [
        {"id": i + 1, "name": subject_names[i], "code": fake.unique.bothify("??###")}
        for i in range(len(subject_names))
    ]

    grades = []
    for student in students:
        for subject in subjects:
            for _ in range(3):
                grades.append(
                    {
                        "student": student["id"],
                        "subject": subject["id"],
                        "grade": fake.random_int(min=50, max=100),
                    }
                )

    return students, subjects, grades


students, subjects, grades = generate_fake_data()


@app.route("/")
def dashboard():
    try:

        student_grades = {student["id"]: [] for student in students}
        for grade in grades:
            student_grades[grade["student"]].append(grade["grade"])

        averages = {
            student_id: sum(grades) / len(grades) if grades else 0
            for student_id, grades in student_grades.items()
        }

        student_data = [
            {
                "id": student["id"],
                "name": student["name"],
                "average": averages[student["id"]],
            }
            for student in students
        ]

        ranked_students = sorted(student_data, key=lambda x: x["average"], reverse=True)

        student_subject_grades = {}
        for student in students:
            student_subject_grades[student["id"]] = {
                "name": student["name"],
                "grades": {subject["id"]: [] for subject in subjects},
            }

        for grade in grades:
            student_id = grade["student"]
            subject_id = grade["subject"]
            student_subject_grades[student_id]["grades"][subject_id].append(
                grade["grade"]
            )

        student_subject_averages = {}
        for student in students:
            student_subject_averages[student["id"]] = {
                "name": student["name"],
                "averages": {},
            }
            for subject in subjects:
                subject_grades = [
                    grade["grade"]
                    for grade in grades
                    if grade["student"] == student["id"]
                    and grade["subject"] == subject["id"]
                ]
                student_subject_averages[student["id"]]["averages"][subject["id"]] = (
                    sum(subject_grades) / len(subject_grades) if subject_grades else 0
                )

        subject_averages = {}
        for subject in subjects:
            subject_grades = [
                grade["grade"] for grade in grades if grade["subject"] == subject["id"]
            ]
            subject_averages[subject["id"]] = {
                "name": subject["name"],
                "average": (
                    sum(subject_grades) / len(subject_grades) if subject_grades else 0
                ),
            }

        return render_template(
            "dashboard.html",
            students=ranked_students,
            subjects=subjects,
            student_subject_grades=student_subject_grades,
            student_subject_averages=student_subject_averages,
            subject_averages=subject_averages,
        )

    except Exception as e:
        return f"An error occurred: {e}", 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
