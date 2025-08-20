import streamlit as st

############################################## button click

st.button('Reset', type='primary')

def button_write():
    st.write('버튼이 클릭되었습니다')

st.button('activate', on_click=button_write)

clicked = st.button('activate2', type='primary')
if clicked:
    st.write('버튼2가 클릭되었습니다')

##############################################

st.header('같은 버튼 여러개 만들기')
# key 속성으로 activate button 나누기

for i in range (5):
    st.button('activate', type='primary', key={i})

##############################################

st.divider()

st.title('Title')
st.header('header')
st.subheader('subheader')

st.write('write 문장입니다') # 디양한 요소 포함 가능
st.text('text 문장입니다') # 말 그대로 그냥 텍스트
st.markdown(
    '''
    여기는 메인 텍스트입니다 \n
    :red[Red], :blue[Blue], :green[Green] \n
    **굵게도 할 수 있고** *Italic*체로도 표현할 수 있다
    '''
) # 다양한 형식으로 출력 가능 (eg. json, 표, etc)

st.code(
    '''
    st.title('Title')
    st.header('header')
    st.subheader('subheader')
    ''', language='python'
)

st.divider()

st.button('Hello', icon='💋') # type 지정 안하면 secondary 타입으로 기본 타입임
st.button('Hello', type='primary')
st.button('Hello', type='primary', disabled=True, key=1)

st.divider()



