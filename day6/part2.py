in_group = False
count = 0
with open('input') as f:
    for line in f:
        if line.strip() == '':
            count += len(questions)
            questions = set()
            in_group = False
            continue
        if not in_group:
            questions = set(question for question in line.strip())
            in_group = True
            continue
        for question in questions.copy():
            if question not in line:
                questions.remove(question)
print(count + len(questions))
