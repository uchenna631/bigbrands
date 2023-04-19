from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm, AddPostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": comment_form
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def add_post(request):
    """ A view function to add post """
    context = dict(form=AddPostForm())
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        context['posted'] = form.instance
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            form = AddPostForm()
    return render(request, 'blog/add_post.html', context)


@login_required
def edit_post(request, slug):
    """
    A view function to edit post function
    """
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, slug=slug)
    form = AddPostForm(
        request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'profiles/edit_post.html', {
        'post': post,
        'form': form
    })


@login_required
def delete_post(request, slug):
    """
    A view function to deletes user's post
    """
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('profile')
