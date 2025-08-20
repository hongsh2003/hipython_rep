import streamlit as st

# sidebar, columns, tabs, expander

from PIL import Image

# 분석페이지의 분석탭 구성함수
st.header('탭 추가')
def make_anal_tab():

    tab1, tab2, tab3 = st.tabs(['차트', '데이터', '설정'])
    with tab1:
        st.subheader('차트 탭')
        st.bar_chart({'데이터': [1,2,3,4,5]})
        
    with tab2:
        st.subheader('데이터 탭')
        st.bar_chart({'기준': ['a','b','c','d','e'], '값': [1,2,3,4,5]})
        
    with tab3:
        st.subheader('설정 탭')
        active = st.checkbox('활성화 여부')
        if active:
            active_slide = st.slider('수현이 전재산 - 단위: 조', 10, 100, 50)
            st.text(f'홍수현님의 전재산은 {active_slide}조입니다')

st.title('스트림릿 앱 페이지 구성하기')

st.sidebar.header('웰컴 메뉴')
selected_menu = st.sidebar.selectbox(
                '메뉴선택', ['메인', '분석', '설정']
                )

img = Image.open('./data/images/image1.png')
img2 = Image.open('./data/images/image2.png')

# 페이지별 화면 구성
if selected_menu == '메인':
    st.subheader('*메인 페이지*')
    st.write('환영합니다')
    col1, col2 = st.columns(2)
    with col1:
        st.image(img, width=200, caption='짱구')
    with col2:
        st.image(img2, width=300, caption='리바이')
    
elif selected_menu == '분석':
    st.subheader('분석 보고서')
    st.write('여기서 데이터를 선택하실 수 있습니다')
    
    make_anal_tab()
else:
    st.subheader('설정 변경')
    st.write('앱 설정을 수정하실 수 있습니다')
    
if st.sidebar.button('선택'):
    st.sidebar.write('선택을 클릭하셨습니다')

# 슬라이드바 추가 0~100, 50이 디폴트
slide = st.slider('오늘의 기분', 0, 100, 50) # start, end, init value
st.text(f'기분 점수: {slide}')

st.divider()

# 확장영역 추가
st.header('익스팬더 추가')

with st.expander('Hidden space'):
    st.write('Cannot see this part unless you click it')
