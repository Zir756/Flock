from django.shortcuts import render

# Create your views here.

# post_list関数  
def post_list(request):
    # request引数 'blog/post_list.html'を組み立てる。  
    # renderという関数を呼び出して得た値をreturnする。  
    return render(request, 'blog/post_list.html', {})
    
    