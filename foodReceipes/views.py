from django.shortcuts import render, redirect, get_object_or_404
from foodReceipes.forms import *
from foodReceipes.models import *
# Create your views here.


def show(request):
    return render(request, 'index.html')


def show_receipts(request):
    food_learn = FoodReceipts.objects.all()
    return render(request, 'learn.html', {'food_learn': food_learn})


def learn_detail(request, post_id):
    food_learn_detail = get_object_or_404(FoodReceipts, pk=post_id)
    comments = Comment.objects.filter(learn_post=post_id).order_by('-id')
    if request.method == "POST":
        comments_form = CommentIt(request.POST)
        if comments_form.is_valid():
            content = request.POST.get('learn_comment')
            comment = Comment.objects.create(learn_post=food_learn_detail, learn_user=request.user, learn_comment=content)
            comment.save()
            return redirect('/learn/' + str(post_id) )
    else:
        comments_form = CommentIt()
    return render(request, 'learnplus.html', {'learn': food_learn_detail, 'comments': comments,
                                              'comments_form': comments_form})
