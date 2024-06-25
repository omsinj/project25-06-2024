import openai
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .utils import generate_african_cities_quiz, generate_historical_puzzle_questions

openai.api_key = settings.OPENAI_API_KEY

def generate_quiz_question(level):
    prompt = f"Generate a {level}-level quiz question with four answer choices and indicate the correct answer."
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        question = response.choices[0].text.strip()
    except Exception as e:
        error_message = f"Error generating quiz question: {str(e)}"
        question = error_message
        import logging
        logging.error(error_message)
    return question

def moderate_content(text):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Moderate the following text for inappropriate content:\n\n{text}",
            max_tokens=50
        )
        moderation_result = response.choices[0].text.strip()
        return "inappropriate" not in moderation_result.lower()
    except Exception as e:
        error_message = f"Error moderating content: {str(e)}"
        import logging
        logging.error(error_message)
        return False

def quizzes(request):
    if request.method == 'GET':
        quiz = generate_african_cities_quiz()
        if 'error' in quiz:
            return render(request, 'quizzes.html', {'error': quiz['error']})
        else:
            return render(request, 'quizzes.html', {
                'question': quiz['question'],
                'options': quiz['options'],
                'correct_answer': quiz['correct_answer'],
                'answer_given': quiz['answer_given']
            })

def submit_quiz_answer(request):
    if request.method == 'POST':
        selected_answer = request.POST.get('answer')
        correct_answer = request.POST.get('correct_answer')
        if selected_answer == correct_answer:
            return HttpResponse('Correct answer! Well done.')
        else:
            return HttpResponse('Incorrect answer. Please try again.')
    else:
        return HttpResponse('Invalid request method.')

def feedback(request):
    return render(request, 'feedback.html')

def submit_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if not moderate_content(message):
            return HttpResponse('Your message contains inappropriate content. Please revise and submit again.')
        
        print(f'Feedback received from {name} ({email}): {message}')
        return HttpResponse('Thank you for your feedback!')
    return redirect('feedback')

def puzzles(request):
    questions = generate_historical_puzzle_questions()
    return render(request, 'puzzles.html', {'questions': questions})

def submit_puzzle_answer(request):
    if request.method == 'POST':
        submitted_answer = request.POST.get('answer')
        correct_answers = [
            {"question": "Who was the first President of the United States?", "answer": "George Washington"},
            {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
            {"question": "Who discovered gravity?", "answer": "Isaac Newton"},
            {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
            {"question": "Who invented the light bulb?", "answer": "Thomas Edison"}
        ]

        for answer in correct_answers:
            if submitted_answer.lower() == answer["answer"].lower():
                return HttpResponse('Correct answer! Well done.')

        return HttpResponse('Incorrect answer. Please try again.')
    else:
        return HttpResponse('Invalid request method.')

def home(request):
    return render(request, 'home.html')

def games(request):
    return render(request, 'games.html')

def about_us(request):
    return render(request, 'about_us.html')

def creators(request):
    return render(request, 'creators.html')

def educational_resources(request):
    return render(request, 'educational_resources.html')

def cultural_journeys(request):
    return render(request, 'cultural_journeys.html')

def cultural_trivia(request):
    return render(request, 'cultural_trivia.html')

def chatbot(request):
    return render(request, 'chatbot.html')

