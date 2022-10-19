from Question import Question

question_prompt = [
    "what color are apples?(hint:racist)\n(a) Purple\n(b) Pink\n(c) Black\n\n",
    "What color are Bananas?(hint:caveMan)\n(a) Chimp\n(b) Monke\n(c) oogga boogga\n\n",
    "what color are colored people?\n(a) White\n(b) Holi\n(c) Black/brown\n\n"
]

questions = [
    Question(question_prompt[0], "c"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + " CORRECT bro. So why are you here , just to suffer.")
run_test(questions)
