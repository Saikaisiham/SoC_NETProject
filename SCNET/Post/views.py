from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post,Comment
from .forms import CommentForm

# def posts(request):
#     post = Post.objects.all()
#     for p in post:
#         print(p.pk)
#     context = {
#         'post' : post
#     }
#     return render(request, 'Post/posts.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            return redirect('Post/create_post')
    else:
        form = PostForm()
    return render(request, 'Post/create_post.html', {'form': form})



# def like_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.user in post.likes.all():
#         post.likes.remove(request.user)
#     else:
#         post.likes.add(request.user)
#     return redirect('Post:posts', pk=post.pk)




# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     comments = post.comments.all()
#     new_comment = None

#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.author = request.user
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, 'blog/post_detail.html', {'post': post,
#                                                      'comments': comments,
#                                                      'new_comment': new_comment,
#                                                      'comment_form': comment_form})



