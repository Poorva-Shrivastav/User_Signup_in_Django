from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse

from .models import User
from .forms import SignupForm
from django.views import View

from django.contrib.auth import authenticate


	
class LoginCreateView(View):
 	template_name = "signup.html"
 	def get(self, request, *args, **kwargs):
 		form = SignupForm()
 		context = {"form":form}
 		return render(request, self.template_name, context)

 	def post(self, request, *args, **kwargs):
 		form = SignupForm(request.POST)
 		if form.is_valid():
 			form.save()
 			first_name = form.cleaned_data.get('firstname')
 			last_name = form.cleaned_data.get('lastname')
 			email = form.cleaned_data.get('email')
 	
 			user = authenticate(firstname=first_name, lastname=last_name, email=email)
 			
 			return HttpResponse("<h2 style=color:blue> Thank you for signing up</h2>")
 			#form = SignupForm()

 		else:
 		 	form = SignupForm()
 		 	return redirect('signup-detail')	
 		return render(request, self.template_name, {'form':form})
 		


class LoginDetailView(View):
	template_name = "signup_detail.html"

	def get(self, request, id=None, *args, **kwargs):
		context = {}
		if id is not None:
			obj = get_object_or_404(User, id=id)
			context['object'] = obj
		return render(request, self.template_name, context)


	def post(self, request, *args, **kwargs):
		form = SignupForm(request.POST)
		if form.is_valid():
				form.save()
		return redirect('/login')
		