import streamlit as st

# checkbox
active = st.checkbox('I agree')

if active:
    st.text('Welcome...')
    
# 함수, on_change = checkbox_write
def checkbox_write():
    st.write('확인')
    
st.checkbox('체크해', on_change=checkbox_write)

# 세션-상태 값에 저장
if 'checkbox_state' not in st.session_state:
    st.session_state.checkbox_state=False
    
def checkbox_write1():
    st.session_state.checkbox_state=True
    
if st.session_state.checkbox_state:
    st.write('ㅇㅇ')
    
st.checkbox('찐으로 누름?', on_change=checkbox_write1)

st.divider()

# 토글버튼
selected = st.toggle('Turn on the switch')
if selected:
    st.text('turn on')
else:
    st.text('turn off')

# selectbox 선택지
option = st.selectbox(
        'Lunch menu selection',
        options=['두찜', '햄버거', '한뷔', '무공'],
        index=None,
        placeholder='Choose one'
)
st.text(f"Today's lunch menu is: {option}")

# radio
genre = st.radio(
        '어떤 영화 좋아함?', ['멜로', '스릴러', '판타지'],
        captions=['봄날은 간다', '트리거', '웬즈데이']
    )

st.text(f'당신이 좋아하는 장르는 {genre}')

# multiselect
menus = st.multiselect(
        'Choose whatever u want', ['두찜', '햄버거', '한뷔', '무공']
    )
st.text(f'I chose ...{menus}')

# slider
score = st.slider('Choose your score', 0, 100, 1) # start, end, init value
st.text(f'score: {score}')

from datetime import time
st_time, end_time = st.slider(
                    'Study hour',
                    min_value=time(0),
                    max_value=time(23),
                    value=(time(8), time(18)),
                    format='HH:mm'
                )
st.text(f'Study hour: {st_time} ~ {end_time}')

# text_input
txt1 = st.text_input('Movie title', placeholder='제목 입력')
txt2 = st.text_input('Password', placeholder='비번 입력', type='password')

st.text(f'텍스트 입력 결과: {txt1}, {txt2}')

# file uploader
# 업로드한 파일은 사용자의 세션에 있습니다. 화면을 갱신하면 사라집니다.
# 서버에 저장하려면 별도로 구현해야합니다
# 데이터베이스에 저장하는 로직도 구현할 수 있습니다
import pandas as pd

file = st.file_uploader(
    '파일 선택', type='csv', accept_multiple_files=False
)

if file is not None:
    df = pd.read_csv(file)
    st.write(df)
    
    with open(file.name, 'wb') as out:
        out.write(file.getbuffer())