import json

# 1. JSON faylni o'qing
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

best = ""
best_grade = 0
worst = ""
worst_grade = 100
summa = 0

for st in students:
    if st["grade"] > best_grade:
        best = st["name"]
        best_grade = st["grade"]

    if st["grade"] <= worst_grade:
        worst = st["name"]
        worst_grade = st["grade"]

    summa += st["grade"]

average = summa/len(students)

# 5. Natijani chiqarish
print(f"Eng yaxshi talaba: {best} — {best_grade}")
print(f"Eng past baho: {worst} — {worst_grade}")
print(f"O'rtacha baho: {average}")