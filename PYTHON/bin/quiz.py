from questions import Questions

question_prompts = [
    "What color are apples? \n(a) Red/Green\n(b) Purple\n(c) Orange\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n"
]

Question = [
    Questions(question_prompts[0], "a"),
    Questions(question_prompts[1], "c"),
    Questions(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f"You've got {score}/3 !")


run_test(Question)
