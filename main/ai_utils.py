# main/ai_utils.py

import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_question(category_name):
    prompt = f"Generate a trivia question about {category_name} with four answer choices, including the correct answer and three incorrect answers."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    question_data = response.choices[0].text.strip()
    lines = question_data.split('\n')
    question_text = lines[0]
    correct_answer = lines[1].replace('Correct Answer: ', '')
    wrong_answer1 = lines[2].replace('Wrong Answer 1: ', '')
    wrong_answer2 = lines[3].replace('Wrong Answer 2: ', '')
    wrong_answer3 = lines[4].replace('Wrong Answer 3: ', '')

    return {
        'question': question_text,
        'correct_answer': correct_answer,
        'wrong_answer1': wrong_answer1,
        'wrong_answer2': wrong_answer2,
        'wrong_answer3': wrong_answer3
    }

