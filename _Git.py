# =====================
# Git 초기 설정
# =====================

# 1.로컬 폴더 >> 우클릭 >> Git Bash Here 실행 -----

# 2.코드 작성자와 연락처를 등록 -----
# git config --global user.name "Merge"
# git config --global user.email "Merge@gmail.com"

# 3.브랜치명을 main 으로 설정(default 명칭은 master) -----
# git config --global init.defaultBranch main

# 4.로컬저장소를 관리하는 폴더(.git) 생성 -----
# git init

# 5.로컬저장소와 원격저장소 연결(원격저장소 이름에 흔히 origin 사용) -----
# git remote add origin https://원격저장소주소

# 6.연결 확인 -----
# git remote -v


# =====================
# Git History 삭제
# =====================

# 1.Clone the project(e.g. 'myproject' is my project repository):
# git clone https://github/heiswayi/myproject.git

# 2.And delete the '.git' folder:
# 탐색기에서 삭제
# # git rm -rf .git

# 3.Now, re-initialize the repository:
# git init
# git remote add origin https://github.com/heiswayi/myproject.git
# git remote -v

# 4.Add all the files and commit the changes:
# git add --all
# git commit -am "Initial commit"

# 5.Force push update to the master branch of our project repository:
# git push -f origin master


# =====================
# Git 명령어
# =====================

# 환경 설정 확인 -----
# git config --list
# git config --global user.name
# git config --global user.email

# 브랜치명 변경 -----
# git remote rm origin 변경전브랜치명 https://원격저장소주소
# git remote add origin 변경후브랜치명 https://원격저장소주소
# git push -u origin 변경후브랜치명

# ssl 인증서 끄기 -----
# git config --global http.sslVerify false


# =====================
# 원격관리(동기화) 제외 설정
# =====================

# .git 폴더가 있는 폴더에 .gitignore 파일을 생성 후 파일 안에 제외할 폴더와 파일을 기록 -----

# #              주석
# *              /를 제외한 모든 문자열
# /              /부터 시작하는 경로패턴은 하위폴더를 포함하지 않음
# folder/        /를 마지막에 적는 경로패턴은 폴더에 있는 모든 파일을 무시
# !              !로 시작하는 패턴은 무시하지 않음
# **             특정폴더 하위에 위치한 모든 디렉토리
# {,}            {}안에 ,로 구분된 각각의 문자열과 매칭
# [-]            []안에서 -사이의 모든문자에 매칭

# *.txt          모든 txt 파일
# /*.txt         현재 폴더의 모든 txt 파일
# !this.txt      모든 .txt를 제외하더라도 this.txt는 포함
# B              B 란 이름의 폴더와 그 내용들과 파일들
# B/             B 폴더의 모든 파일
# B/debug.log    B 폴더 바로 안의 debug.log
# B/*.txt        B 폴더 바로 안의 .txt 파일들
# B/**/*.pdf     B 폴더 및 모든 하위폴더의 모든 pdf 파일
# /*.{js,ts}     현재폴더의 모든 js, ts 확장자 파일 무시 (하위폴더에는 미적용)
# /ex[1-3].js    현재폴더의 ex1.js ex2.js ex3.js 파일 무시
# *.[oa]         확장자가 '.o' 나 '.a' 인 모든 파일


# =====================
# vscode에서 local로 clone 복제
# =====================

# F1 > 'git clone' 입력 > 'Git: Clone' 메뉴 선택 또는 왼쪽 'Source Control' 메뉴 >> 'Clone Repository' 선택
# git 주소 입력
# 로컬저장소 위치 선택(※ 빈 디렉토리 생성 주의!!, 기존 파일 옮겨와야 함)
# 참조: https://technote.kr/352


# =====================
# 자료 이동 개념
# =====================

# [Working Directory] ----(add)---->> [Staging Area] --(commit)->> [Repository] ---(push)->> [github]
# [Working Directory] <<-(restore)--- [Staging Area]

# [Working Directory] <<------------(checkout, merge)------------- [Repository] <<-(pull)--- [github]

# [Working Directory] <<------------------(clone)------------------------------------------- [github]


# --------------------
# 파일 상태 추적
# --------------------

# 워킹디렉토리의 모든 파일은 비추적(Untracked files)대상이었다가
# add 명령으로 추적(Tracked)대상으로 바뀌며 3가지로 구분관리된다.
# Changes to be committed: 커밋준비된 상태
# Changes not staged for commit: Modified: 커밋된 후 수정된 상태(add 명령으로 다시 스테이지로 올려야함)
# Unmodified: 커밋된 후 비수정상태

# git status


# --------------------
# 파일 변경 내용 확인
# --------------------

# 워킹 디렉토리에 있는 것과 Staging Area에 있는 것을 비교(수정해서 unstaged 상태인 파일과 비교) -----
# git diff 파일명

# Staging Area에 있는 것과 저장소에 커밋한 것을 비교 -----
# git diff --staged 파일명


# --------------------
# add : 파일을 집파일(Staging Area)에 압축
# --------------------

# 모든 파일을 압축 -----
# git add .

# 특정 파일을 압축 -----
# git add A.txt B.txt

# 최근 압축 취소 -----
# git reset HEAD

# 특정 파일 압축 취소 -----
# git reset HEAD 파일명

# 워킹디렉토리에는 남겨두고 Staging Area에서만 제거 옵션 -----
# git rm --cached 파일명


# --------------------
# restore : Staging Area에서 다운로드
# --------------------

# git restore --staged 파일명


# --------------------
# commit : Staging Area의 집파일을 로컬저장소로 복제(개별파일단위 작업불가)
# --------------------

# >>> 커밋 -----

# 커밋할 때 메세지를 입력하는 방법
# git commit -m "Replace B with C"

# add 와 commit을 한꺼번에 하는 방법
# git commit -am "Replace B with C"

# >>> commit을 하면 시간순으로 log가 기록됨 -----

# 로그 확인
# git log (※ 종료는 q)

# >>> 커밋 취소 -----

# Reset : 원하는 시점으로 돌아간 이후 내역들을 삭제(3 -> 1번째로 되돌아간 후 2,3 commit 내역 삭제) -----
# git reset 옵션 돌아갈커밋해시 : 해시값은 앞 6 ~ 7자리만 입력해도 됨
#    mixed 옵션 : add 전 상태인 unstaged 상태, 워킹 디렉터리에 파일 보존(디폴트)
#    soft  옵션 : add 후 상태인 staged   상태, 워킹 디렉터리에 파일 보존
#    hard  옵션 : add 전 상태인 unstaged 상태, 워킹 디렉터리의 파일 삭제

# log명령어로 돌아갈 commit 의 해쉬값을 확인
# git log

# [방법 1]
# commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에 보존
# git reset HEAD^     # ^ (한단계 앞)
# git reset HEAD~1    # 마지막 commit을 취소. 하나를 되돌림
# git reset HEAD^^    # ^^ (두단계 앞)
# git reset HEAD~2    # 마지막 2개의 commit을 취소

# [방법 2]
# commit을 취소하고 해당 파일들은 staged 상태로 워킹 디렉터리에 보존
# git reset --soft HEAD^

# [방법 3]
# commit을 취소하고 해당 파일들은 unstaged 상태로 워킹 디렉터리에서 삭제
# git reset --hard HEAD^
# git reset --hard e71342c0bbe83

# >>> 커밋 삭제 -----

# 커밋 정보 확인
# git log --oneline

# 커밋 되돌리기
# git reset --hard HEAD~200000

# 원격저장소에 커밋 history 밀어 넣기
# git push origin main --force

# >>> 첫번째 커밋 삭제 -----

# 커밋 정보 삭제
# git update-ref -d HEAD

# 로컬 저장소의 커밋 히스토리로 원격 저장소의 커밋 히스토리를 강제로 덮어 씌우기
# git push --force


# --------------------
# checkout : 작업디렉토리의 변경내용 되돌리기
# --------------------

# git checkout .
# git checkout -- 파일명


# --------------------
# push : 원격저장소 업로드
# --------------------

# git push -u origin 브랜치명

# 한번 git push -u origin main을 실행한 후에는 push만 가능
# git push

# 원격 목록 보기
# git remote

# 원격 목록 상세 보기
# git remote -v

# >>> 충돌 해결 방법 -----

# 팀원이 먼저 push를 한 후, 내가 동기화가 안된 상태에서 push한 경우, pull 후 push 하여 해결
# git pull --no-rebase
# git push

# 로컬 저장소의 커밋 히스토리로 원격 저장소의 커밋 히스토리를 강제로 덮어 씌우기
# git push --force


# --------------------
# pull : 원격저장소 다운로드
# --------------------

# git pull origin main


# --------------------
# clone
# --------------------

# git clone URL주소
# git clone URL주소 로컬의디렉토리명

# 원격저장소의 특정branch를 clone 하기
# git clone -b 브랜치명 --single-branch URL주소


# --------------------
# 원격저장소 연결 끊기
# --------------------

# 로컬과 원격간 연결만 없애는 것으로 GitHub의 레포지토리는 보존
# git remote remove origin(원격저장소이름)
