from django.shortcuts import render

# '.models'=１つ上がカレントアプリケーションの為 . とファイル名だけで記述することができる。  
# そして"Post"モデルを指定してインポートする。  
from .models import Post

from django.utils import timezone

# Create your views here.

# post_list関数  
def post_list(request):
    
    # 投稿をtimezoneを参照して並べ替える。  
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # request引数 'blog/post_list.html'を組み立てる。  
    # renderという関数を呼び出して得た値をreturnする。 
    # {}の中に指定した情報をテンプレートが表示してくれる。中身は'名前'と'値'
    return render(request, 'blog/post_list.html', {'posts': posts})
    
    