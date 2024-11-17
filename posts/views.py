from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

# из файла models.py импортируем класс, где описана таблица (модель)
from .models import Articles

# Create your views here.
"""
Пример динамический типизации, к таким ЯП относятся: Python, PHP, JavaScript и т.д.

name = "Dmitri"
name = 1

Пример статической типизации, к таким ЯП относятся: С++, С#, Java, Pascal

char symb = 'a'
string name = "Dmitri" -> ['D', 'm', ...]
name = 1 // в этом месте была бы ошибка
int number = 2147483648 + 5 // 4 байта = 32 бит
// -2147483648 ... + 2147483648
-5
"""

posts = [
    {
        "id": 1,
        "title": "django - это веб-фреймворк",
        "content": "Django используется практич ески в любом крупном проекте и в любой крупной компании, такие как: google, meta, twitter и т.д.",
        "main": "Здесь будет длинная статья на 1000 слов",
    }, # 0
    {
        "id": 2,
        "title": "python - это высокоуровневый язык программирования с динамической типизацией",
        "content": "Django используется практически в любом крупном проекте и в любой крупной компании, такие как: google, meta, twitter и т.д.",
        "main": "Здесь будет длинная статья на 3000 слов",
    }, # 1
]
posts = []


def abcdef(request):
    return HttpResponse("Hello, World!")


"""
import random

random.choice()
print("Hello, World!")
posts = []

#include <iostream>
#include <srand>
#include <vector>
#include <string>
"abc"
{'a', 'b', 'c'}
using namespace std;

int main() {
    vector posts<string> = {};
    srand::choice();
    cout << "Hello, World << endl;
}
"""
def home(request):
    posts = Articles.objects.order_by("-pub_date")[:10]

    return render(request, "posts/home.html", {"posts": posts})


def post(request, id):  # id=5
    post = get_object_or_404(Articles, pk=id)
    return render(request, "posts/post.html", {"post_dict": post})

    # valid_id = False
    # for post in posts:
    #     if post["id"] == id:  # posts/1
    #         post_dict = post
    #         valid_id = True
    #         break
    # if valid_id:
    #     return render(request, "posts/post.html", {"post_dict": post_dict})
    #     # html = f"""
    #     #         <div>
    #     #             <h1>{post_dict["id"]}</h1>
    #     #             <p>{post_dict["main"]}</p>
    #     #         </div>
    #     #         """
    #     # return HttpResponse(html)
    # else:
    #     return HttpResponseNotFound("Пост не найден 💀")
