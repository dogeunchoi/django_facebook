from django.shortcuts import render, redirect
from facebook.models import Article, Comment

# Create your views here.
def play(request):
    return render(request, 'play.html')

count = 0
def play2(request):
    choidogeun = '최도근'

    global count
    count = count + 1

    age = 10
    if age > 19:
        status = '성인'
    else:
        status = '청소년'


    diary = ['오늘을 맑았따', '오늘은 춥다', '오늘은 배부르다', 'ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ!']

    return render(request, 'play2.html',
                  { 'name2': choidogeun,
                    'cnt': count,
                    'age': status,
                    'diary': diary})

def profile(request):
    return render(request, 'profile.html')

def event(request):
    choidogeun = '최도근'

    global count
    count = count + 1

    if count == 7:
        lotto = '당첨'
    else:
        lotto = '꽝'

    age = 10
    if age > 19:
        status = '성인'
    else:
        status = '청소년'


    diary = ['오늘을 맑았따', '오늘은 춥다', '오늘은 배부르다', 'ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ!']

    return render(request, 'event.html',
                  { 'name2': choidogeun,
                    'cnt': count,
                    'age': status,
                    'diary': diary,
                    'lotto': lotto })

def newsfeed(request):
    articles = Article.objects.all()


    return render(request, 'newsfeed.html', { 'articles': articles })

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)

    # 코멘트 쓰기 버튼이 눌러졌으면 코멘트 DB에 넣기
    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST['author'],
            text=request.POST['text'],
            password=request.POST['password']
        )

    return render(request, 'detail_feed.html', { 'feed': article })

def new_feed(request):
    # 데이터를 받아서 글을 생성하기
    if request.method == 'POST':
        myText = request.POST['content']
        myText = myText + '추신:감사합니다'

        Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=myText,
            password=request.POST['password']
        )

    return render(request, 'new_feed.html')

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':

        article.author = request.POST['author']
        article.title = request.POST['title']
        article.text = request.POST['content']
        article.save()
        #저장되었으니 해당 글 페이지로 이동

        return redirect(f'/feed/{ article.pk }/')
        # return redirect('/feed/' + str(article.pk))
        # return redirect(f'/feed/{ pk }/')
        # return redirect('/feed/' + str(pk))

    return render(request, 'edit_feed.html',
                  {'feed': article})

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    # 글 삭제 로직
    if request.method == 'POST':
        if article.password == request.POST['password']:
            # 비번이 같다면 삭제 처리
            article.delete()
            return redirect('/')
        else:
            # 비밀번호 같지 않다면 '비밀번호 오류페이지로 이동시키기'
            pass

    return render(request, 'remove_feed.html',
                  { 'feed':article })