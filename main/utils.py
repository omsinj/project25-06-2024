import random
import openai


def generate_african_cities_quiz():
    # List of African cities (you can expand this list as needed)
    cities = [
        "Cairo", "Lagos", "Nairobi", "Johannesburg", "Casablanca",
        "Accra", "Dakar", "Addis Ababa", "Abuja", "Cape Town",
        "Dar es Salaam", "Khartoum", "Kigali", "Luanda", "Maputo",
        "Mogadishu", "Tunis", "Tripoli", "Windhoek", "Yaoundé"
    ]
    
    # Choose a random city as the correct answer
    correct_answer = random.choice(cities)
    
    # Create three distractors (randomly chosen from other cities)
    distractors = random.sample(cities, 3)
    
    # Ensure the correct answer is not among the distractors
    if correct_answer in distractors:
        distractors.remove(correct_answer)
    
    # Shuffle the options (correct answer + distractors)
    options = [correct_answer] + distractors
    random.shuffle(options)
    
    # Generate the prompt for OpenAI API
    prompt = f"What is the capital city of {correct_answer}? Choose one:\n"
    for i, option in enumerate(options):
        prompt += f"{i+1}. {option}\n"
    
    # Request completion from OpenAI
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        question = {
            'question': f"What is the capital city of {correct_answer}?",
            'options': options,
            'correct_answer': correct_answer,
            'answer_given': response.choices[0].text.strip()
        }
    except Exception as e:
        # Handle specific exceptions or log errors
        error_message = f"Error generating African cities quiz: {str(e)}"
        question = {'error': error_message}  # Provide a fallback response or handle gracefully
        # Example: logging the error
        import logging
        logging.error(error_message)
    
    return question

print("utils.py loaded")

def generate_historical_puzzle_questions():
    questions = [
        {
            "question": "Who was the first President of the United States?",
            "choices": ["Thomas Jefferson", "George Washington", "John Adams", "Abraham Lincoln"],
            "answer": "George Washington"
        },
        {
            "question": "Who was the ruler of the Roman Empire at its peak?",
            "choices": ["Julius Caesar", "Augustus", "Nero", "Constantine"],
            "answer": "Augustus"
        },
        {
            "question": "Who founded the Mongol Empire in the 13th century?",
            "choices": ["Genghis Khan", "Attila the Hun", "Tamerlane", "Kublai Khan"],
            "answer": "Genghis Khan"
        },
        {
            "question": "Who was the first female Prime Minister of the United Kingdom?",
            "choices": ["Margaret Thatcher", "Theresa May", "Queen Victoria", "Elizabeth I"],
            "answer": "Margaret Thatcher"
        },
        {
            "question": "Who wrote 'The Wealth of Nations' and is considered the father of modern economics?",
            "choices": ["Adam Smith", "Karl Marx", "John Maynard Keynes", "Friedrich Hayek"],
            "answer": "Adam Smith"
        }
    ]
    
    # Shuffle the questions
    random.shuffle(questions)
    
    return questions[:5]  # Return 5 random questions