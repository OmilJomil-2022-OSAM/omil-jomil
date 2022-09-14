# Backend



## install

pip install fastapi
pip install "uvicorn[standard]"
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"

## 파일 구조 설명

AI : AI 코드가 들어갈 폴더
- 함수형태로 작성하시면 여기에 들어가고 아니면 최상위 폴더를 만들어야 하지 않을까 싶습니다.

app : 각종 service가 들어가는 폴더
- user(인증, 로그인, 토큰 발급), camera(실시간 동영상 받아오기)
- api endpoint가 들어갈 것 같습니다.

core : 공통적으로 사용하는 함수들
- DB, 

docker : 프로젝트 빌드할때 사용하는 파일이나 각종 설정파일등 
