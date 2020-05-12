class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = ["What is 2 + 2?\n(a) 6\n(b) 4\n(c) 2\n\n", "What is the square root of 9?\n(a) 4\n(b) 9\n(c) 3\n\n", "9x + 2 = 20.. What does x equal?\n(a) 2\n(b) 45\n(c) 1\n\n", "What is the slope of 2x + y = 2?\n(a) 2\n(b) -1\n(c) -2\n\n"] 
    
questions = [Question(question_prompts[0], "b"), Question(question_prompts[1], "c"), Question(question_prompts[2], "a"), Question(question_prompts[3], "c")]

def quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
        
quiz(questions)
    