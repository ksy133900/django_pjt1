from django.shortcuts import render, redirect
from .models import Review

# Create your views here.


def index(request):

    reviews = Review.objects.all()

    context = {
        "reviews": reviews,
        # "completed": completed,
    }

    return render(request, "apps/index.html", context)


def detail(request, pk):
    # get() 메소드를 사용해서 특정 pk의 데이터를 불러온다.
    # 불러온 데이터를 변수에 할당
    review = Review.objects.get(id=pk)
    context = {
        "review": review,
    }

    return render(request, "apps/detail.html", context)


def new(request):

    return render(request, "apps/new.html")


def create(request):
    # 1. parameter로 날라온 데이터를 받아서
    title = request.GET.get("title")
    content = request.GET.get("content")

    # 2. DB에 저장
    Review.objects.create(title=title, content=content)

    return redirect("apps:index")


def delete(request, pk):

    review = Review.objects.get(id=pk)
    review.delete()

    return redirect("apps:index")


def edit(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        "review": review,
    }
    return render(request, "apps/edit.html", context)


def update(request, pk):
    review = Review.objects.get(id=pk)
    title_ = request.GET.get("title")
    content_ = request.GET.get("content")

    review.title = title_
    review.content = content_

    review.save()
    return redirect("apps:detail", review.pk)
