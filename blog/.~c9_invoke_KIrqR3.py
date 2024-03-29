from django.shortcuts import render, get_object_or_404

# '.models'=１つ上がカレントアプリケーションの為 . とファイル名だけで記述することができる。  
# そして"Post"モデルを指定してインポートする。  
from .models import Post, Comment

from django.utils import timezone

from .forms import PostForm, CommentForm

from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, authenticate

from .forms import SignUpForm

# Create your views here.

# post_list関数  
def post_list(request):
    
    # 投稿をtimezoneを参照して並べ替える。  
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # request引数 'blog/post_list.html'を組み立てる。  
    # renderという関数を呼び出して得た値をreturnする。 
    # {}の中に指定した情報をテンプレートが表示してくれる。中身は'名前'と'値'
    return render(request, 'blog/post_list.html', {'posts': posts})
    
# post_detail関数  
def post_detail(request, pk):
  
    # 与えられたpkのPostがない場合、Page Not Found 404 ページが表示されます。
    post = get_object_or_404(Post, pk=pk)
    # request引数 'blog/post_detail.html'を組み立てる。  
    # renderという関数を呼び出して得た値をreturnする。 
    # {}の中に指定した情報をテンプレートが表示してくれる。中身は'名前'と'値'
    return render(request, 'blog/post_detail.html', {'post': post})
    
# post_new関数
@login_required
def post_new(request):
    
    # 最初にページにアクセスしてきた時で空白のフォームが必要な場合。
    if request.method == "POST":
        # methodがPOSTの場合、フォームのデータを使ってPostFormを構築します。
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
            
    # すべてのフォームデータが入力された状態でビューに戻ってくる場合。  
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    
# post_edit関数
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
   
#  post_publish関数
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)
    
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
    
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
    
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
    
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')  # 登録後のリダイレクト先を設定
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})