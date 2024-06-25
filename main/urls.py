from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quizzes/', views.quizzes, name='quizzes'),
    path('submit_quiz_answer/', views.submit_quiz_answer, name='submit_quiz_answer'),
    path('feedback/', views.feedback, name='feedback'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('games/', views.games, name='games'),
    path('about_us/', views.about_us, name='about_us'),
    path('creators/', views.creators, name='creators'),
    path('educational_resources/', views.educational_resources, name='educational_resources'),
    path('cultural_journeys/', views.cultural_journeys, name='cultural_journeys'),
    path('cultural_trivia/', views.cultural_trivia, name='cultural_trivia'),
    path('puzzles/', views.puzzles, name='puzzles'),
    path('submit_puzzle_answer/', views.submit_puzzle_answer, name='submit_puzzle_answer'),
    path('chatbot/', views.chatbot, name='chatbot'),
]







