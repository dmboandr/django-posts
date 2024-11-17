from django.urls import path

from . import views  # подключаю весь файл views

# чтобы были разные переходы в приложении,
# нам нужно прописывать ссылки
# и делать связи функции и адреса по ссылке

# для этого и нужен файл urls.py и переменная urlpatters
urlpatterns = [
    # .../polls/
    path("", views.index, name="index"),
    # .../polls/3/
    path("<int:question_id>/", views.detail, name="detail"),
    # .../polls/results
    path("<int:question_id>/results/", views.results, name="results"),
# .../polls/results
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
# http://127.0.0.1:8000/polls/3/
#