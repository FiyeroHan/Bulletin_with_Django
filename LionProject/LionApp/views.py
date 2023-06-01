# 제어를 맡는 부분
from django.shortcuts import render,redirect
from .models import Post, Reple

# Create your views here.
def home(request):
    posts = Post.objects.all() 
    context = {"posts":posts} #home.html에 내용물을 전달해줌
    return render(request, 'home.html',context=context)

def detail(request, pk): #request에는 사용자의 요청을 보낸다.
    post = Post.objects.get(pk = pk)
    # Reple.objects <- 댓글 오브젝트들에서 / .filter <-필터링을 통해/ (post=post) post가 현재 post와 같은 댓글들만 가져온다.
    reples = Reple.objects.filter(post = post)
    context = {"post" : post, "reples" : reples, }
    if request.method == "POST":
        content = request.POST.get('reple') # post.html에서 보내는 'reple'
        reple = Reple.objects.create(post= post, content = content)
        reple.save()
        return redirect('detail', pk=pk)
    else:
        return render(request, 'post.html', context=context)

def create_post(request):
    # POST 요청이 들어오면
    # 해당 내용을 저장하고, 디테일 페이지로 이동
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        post.save()
        #urls.py에서 적어둔 name과 추가적으로 달린 인자를 받는다.
        # return redirect('detail', pk=post.pk)  
        return redirect('home')
    # GET요청이 들어오면
    # post를 작성할 수 있는 페이지를 렌더링
    else:
        return render(request, 'create_post.html')

def modify_post(request, pk):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
#        post = Post.objects.update(title=title, content=content)
#        post.save()
        post = Post.objects.get(pk=pk)
        post.title = title
        post.content = content
        post.save()
        return redirect('detail', pk= post.pk)
    else:
        post = Post.objects.get(pk = pk)
        context = {"post":post}
        return render(request, 'modify_post.html', context=context)

def delete_post(request, pk):
    post=Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')

def delete_reple(request, reple_pk, post_pk):
    reple=Reple.objects.get(pk=reple_pk)
    reple.delete()
    return redirect('detail', pk=post_pk)