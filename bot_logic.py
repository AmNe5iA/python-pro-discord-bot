import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

jokes = {
"Why do programmers prefer dark mode?": "Because light attracts bugs.",
"Why did the computer go to the doctor?": "It had a virus.",
"What do you call a snake that writes code?": "A Python developer.",
"Why was the JavaScript developer sad?": "Because he didn't Node how to Express himself.",
"How do you comfort a Python programmer?": "You say: it's okay, indentation is not the end of the world."
}

def get_joke():
    question = random.choice(list(jokes))
    return question, jokes[question]