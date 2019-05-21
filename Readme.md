# 멋쟁이사자처럼 7기 Debugging Contest

- 자료 검색은 웹 검색만 허용합니다. 본인이 웹에 자료를 올려 놓으신 거 찾으시면 안됩니다.
    - 추가적으로 코드 자체를 검색하는 것은 안되고 에러 코드 검색만 허용하겠습니다.
    - 세션자료 열람 불가합니다.
    - 자료 검색능력도 중요하기 때문입니다!!

- vscode에서 터미널을 여시고 아래 명령어로 clone을 하시면 됩니다.

  (그냥 zip파일로 다운받으셔서 하셔도 돼요!!)

- `$ git clone https://github.com/hooong/likelion_7_debugging_contest.git`

- 가상환경은 각자 만드시고 django만 설치하시면 됩니다.

- * 모두 정상적으로 돌아가야하는 기능을 밑에 나열하겠습니다.
  - * 최근에 작성한 글이 맨 위로 올라와야 합니다.
  - * index페이지(모든 글을 띄워주는)가 처음 화면으로 나와야합니다.
  - * 글을 쓰는 페이지에서 글을 작성할 수 있어야합니다.
  - * 특정 글을 자세히 볼 수 있는 detail을 구현해야합니다.
  - * 글을 수정할 수 있어야합니다.
  - * 글을 삭제할 수 있어야합니다.

### 그럼 열심히 고쳐봅시다~ 화이팅!!

----

# Debugging

- index.html

  > base  -->  base.html
  >
  > post.all  -->  posts.all
  >
  > {% endfor %}추가
  >
  > {% url %} 의 모든 부분에 post_id  -->  post.id로 바꿈.

- settings.py

  > 'blog'  -->  'Blogapp'
  >
  > TEMPLATES = [
  >
  > ​        'DIRS': ['debugging_contest/templates'] 추가

- urls.py

  >  path('index', Blogapp.views.index,name='index'),  --> path('', Blogapp.views.index, name='index'),
  >
  > path(new)에서 반점 추가
  >
  > path(detail)에서 post.id  -->  post_id
  >
  > import Blogapp.views 추가
  >
  > path(delete)에서 name속성 추가 -> name = 'delete'

- form.py

  > fields에서 'content' 추가

- views.py

  > def index(request, post_id):   -->  post_id제거 (함수 호출시 넘겨줄 필요없음)
  >
  > import redirect
  >
  > newpost 함수에서 if form.is_valid(): 부분 들여쓰기 한칸씩 뒤로
  >
  > edit 함수도 위에와 마찬가지.
  >
  > from .models import Blog  -->  from .models import Post
  >
  > 매개변수들의 모든 post.id  -->  post_id.
  >
  > newpost에서의 return redirect('/post/'+post.id)   -->  redirect('detail', post.id)
  >
  > edit 또한 위와 동일
  >
  > edit에서 render(request, 'new.html', {'form':form})  -->  {'forms':form}
  >
  > order_by('-pub_date') -> 최근에 작성한 글 부터 정렬

- detail.html

  > {{blog}}  -->  {{post}}

- new.html

  > method="GET"  -->  method="POST"

- models.py

  > title = models.------() --> max_length = 200 (매개변수 추가)

- admin.py

  > import 추가 (Post Model)
