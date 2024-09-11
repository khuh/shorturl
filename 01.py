# 이 코드는 chatgpt의 도움으로 만들어진 코드입니다.
# 
import streamlit as st
import pyshorteners

# 타이틀 설정
st.title("URL 단축기")

# 사용자 입력을 받음
long_url = st.text_input("단축할 URL을 입력하세요:")

# 단축 버튼
if st.button("단축하기"):
    if long_url:
        # pyshorteners를 이용하여 URL 단축
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        
        # 단축된 URL을 출력
        st.success(f"단축된 URL: {short_url}")
    else:
        st.error("유효한 URL을 입력하세요.")

# 페이지 하단에 크레딧 추가
st.write("이 앱은 Streamlit과 pyshorteners를 사용하여 만들어졌습니다.")

