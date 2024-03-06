from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
	path('', views.IndexView.as_view(), name="home"),

	]

	# path('portfolio/', views.PortfolioView.as_view(), name="portfolios"),
