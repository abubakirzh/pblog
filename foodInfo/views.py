from django.shortcuts import render, redirect, get_object_or_404
from foodInfo.forms import *
from foodInfo.models import *
# Create your views here.


def show_info(request):
    food_info = FoodInfo.objects.all()
    return render(request, 'info.html', {'food_info': food_info})


def info_detail(request, post_id):
    food_info_detail = get_object_or_404(FoodInfo, pk=post_id)
    comments = Comment.objects.filter(info_post=post_id).order_by('-id')
    if request.method == "POST":
        comments_form = CommentIt(request.POST)
        if comments_form.is_valid():
            content = request.POST.get('info_comment')
            comment = Comment.objects.create(info_post=food_info_detail, info_user=request.user, info_comment=content)
            comment.save()
            return redirect('/info/' + str(post_id) )
    else:
        comments_form = CommentIt()

    return render(request, 'infoplus.html', {'info': food_info_detail, 'comments': comments,
                                             'comments_form': comments_form})


def search_food_info(request):
    if request.method == "POST":
        search_food_info_start = request.POST['searchFoodInfo']
        search_food_info_complete = FoodInfo.objects.filter(info_title__contains=search_food_info_start)
        return render(request, 'info.html', {'search_food_info_complete': search_food_info_complete,
                                              'search_food_info_found': len(search_food_info_complete)})

    return redirect('/info/')
