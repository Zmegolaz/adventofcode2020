questions = set()
count = 0
with open('input') as f:
    for line in f:
        if line.strip() == '':
            count += len(questions)
            questions = set()
        for question in line.strip():
            questions.add(question)
print(count + len(questions))
