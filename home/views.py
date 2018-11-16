from django.shortcuts import render

def home(request):
	return render(request, 'index.html', {})



def perfil_user(request):
	return render(request, 'perfil.html')

def quiz_home(request):
	return render(request, 'quiz.html')
