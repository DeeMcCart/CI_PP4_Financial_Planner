from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Article
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm


class ArticleList(generic.ListView):
    model = Article
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class ArticleDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
            '-created_on')
        actions = article.actions.order_by('action_seq')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        commented = False
        print('User ', self.request.user.id)
        if article.comments.filter(id=self.request.user.id,
                                   approved=False).exists():
            print('Unapproved comments exist for this user!')
            commented = True

        return render(
            request,
            "article_detail.html",
            {
             "article": article,
             "comments": comments,
             "commented": commented,
             "actions": actions,
             "liked": liked,
             "comment_form": CommentForm()
             },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Article.objects.filter(status=1)
        article = get_object_or_404(queryset, slug=slug)
        comments = article.comments.filter(approved=True).order_by(
            '-created_on')
        actions = article.actions.order_by('action_seq')
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
                    request,
                    "article_detail.html",
                    {
                        "article": article,
                        "comments": comments,
                        "commented": True,
                        "comment_form": CommentForm(),
                        "liked": liked,
                        "actions": actions,
                    },
                    )


class ArticleLike(View):
    def article(self, request, slug):
        article = get_object_or_404(Post, slug=slug)
        if article.likes.filter(id=request.user.id).exists():
            article.like.remove(request.user)
        else:
            article.likes.add(request.user)
        return HttpResponseRedirect(reverse('article_detail', args=[slug]))
