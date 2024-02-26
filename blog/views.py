from django.shortcuts import render, get_object_or_404

# '.models'=１つ上がカレントアプリケーションの為 . とファイル名だけで記述することができる。  
# そして"Post"モデルを指定してインポートする。  
from .models import Post

from django.utils import timezone

from .forms import PostForm

from django.shortcuts import redirect

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