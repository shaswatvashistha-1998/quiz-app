from django.shortcuts import render
from app.models import Question,Genre
from django.views.generic import TemplateView,ListView,CreateView
from . import models

def q_list(request):
	selected_option = request.POST['poll']
	obj=Question.objects.filter(genre1__icontains=selected_option)
	context={'questions':obj}
	return render(request, 'q_list.html', context)
	#context={'genre':genre_name}
'''def q_list(request):
	questions = Question.objects.all()
	return render(request, 'q_list.html', {'questions': questions})'''

def result(request):
	questions = Question.objects.all()
	total_score = get_score(request, questions)
	return render(request, 'result.html', {'total_score': total_score,'get_asnwer':get_answer})

def get_score(request, questions):
	total_score = 0
	for question in questions:
		answer = question.answer#fetching the correct answer
		user_answer = request.POST.get(str(question.id))#fetching the answer submitted by the user
		if(user_answer == answer):#evaluating the answer
			total_score += 1
	return total_score
def get_answer(request, questions):
	total_score = 0
	for question in questions:
		answer = question.answer#fetching the correct answer
		user_answer = request.POST.get(str(question.id))#fetching the answer submitted by the user
		print(user_answer)
		if(user_answer == answer):#evaluating the answer
			total_score += 1
	return user_answer
class firstview(ListView):
	template_name='start.html'
	model=models.Genre
	context_object_name='questions'
class createquestion(CreateView):
	model=models.Question
	template_name='create.html'
	fields=('question_num','question','choice1','choice2','choice3','choice4','choice5','answer','genre1')
