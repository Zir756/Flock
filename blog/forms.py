# 最初にDjangoのformsをインポート
from django import forms

# Postモデルもインポート
# commentモデルもインポート
from .models import Post, Comment

# これはフォームの名前です。 このフォームが ModelForm の一種だとDjangoに伝える必要があります。  
class PostForm(forms.ModelForm):

    # Djangoにフォームを作るときにどのモデルを使えばいいか (model = Post) を伝えます。
    class Meta:
        model = Post
        fields = ('title', 'text',)
        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)