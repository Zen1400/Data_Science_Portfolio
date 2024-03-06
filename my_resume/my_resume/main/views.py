from django.shortcuts import render
from django.contrib import messages
from .models import (
		UserProfile,
		Portfolio,
	)

from django.views import generic


class IndexView(generic.TemplateView):
	template_name = "main/index.html"

	def get_context_data(self, **kwargs):
     # retrieve additional context data to be passed to the template when rendering
		context = super().get_context_data(**kwargs)

		userprofile = UserProfile.objects.all()
		portfolio = Portfolio.objects.all()
		context["userprofile"] = userprofile
		context["portfolio"] = portfolio
		return context




# class PortfolioView(generic.ListView):
# 	model = Portfolio
# 	template_name = "main/portfolio.html"
# 	paginate_by = 10
# #  get_queryset method is used to retrieve the queryset of objects that will be displayed by the view.
# 	def get_queryset(self):
# 		return super().get_queryset().filter(is_active=True)
