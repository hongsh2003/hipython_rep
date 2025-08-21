import streamlit as st
from PIL import Image

st.title('방구 - 맞춤 방 구하기 서비스')

# 사이드 바
st.sidebar.header('메뉴')
menu = st.sidebar.selectbox('메뉴선택',
                            ['방구 소개', '방 찾기', '매물'])

# 방찾기 구성함수
def room_search():
    tab1, tab2, tab3, tab4 = st.tabs(['기본 정보', '예산', '방', '상세조건'])
    
    with tab1:
        # 동네 찾기
        st.subheader('원하는 동네 기준 선택')
        check_work = st.checkbox('회사 근처가 좋아요')
        if check_work:
            work_input = st.text_input('회사 주소를 입력해주세요')
            st.text(f'입력하신 회사 주소는 {work_input}입니다')
        
        check_town = st.checkbox('원하는 동네가 있어요')
        if check_town:
            town_input = st.text_input('원하는 동네를 입력해주세요')
            st.text(f'입력하신 동네는 {town_input}입니다')

        # 연령대 선택
        st.subheader('연령대 선택')
        st.selectbox('연령대를 선택하세요',
                    ['선택안함', '20대', '30대', '40대', '50대 이상'])

    with tab2:
        # 보증금 선택
        st.subheader('보증금 선택')
        min_deposit, max_deposit = st.slider('원하는 보증금 범위를 선택하세요 (단위: 만원)',
                                    min_value=0,
                                    max_value=10000,
                                    value=(50, 200)) # start, end, init value
        st.text(f'선택하신 보증금은 {min_deposit} ~ {max_deposit} 만원입니다')
        
        st.divider()
        
        # 월세 선택
        st.subheader('월세 선택')
        min_rent, max_rent = st.slider('원하는 보증금 범위를 선택하세요 (단위: 만원)',
                                min_value=0,
                                max_value=200,
                                value=(30, 50)) # start, end, init value
        st.text(f'선택하신 보증금은 {min_rent} ~ {max_rent} 만원입니다') 
    
    with tab3:
        # 평수 선택
        st.subheader('평수 선택')
        min_size, max_size = st.slider('원하는 평수 범위를 선택하세요',
                                min_value=0,
                                max_value=200,
                                value=(10, 30)) # start, end, init value
        st.text(f'선택하신 평수는 {min_size} ~ {max_size} 평입니다') 

        st.divider()
        
        # 방 개수 선택
        st.subheader('방 개수 선택')
        st.selectbox('방 개수를 선택하세요',
                    ['상관없음', '1개', '2개', '3개', '4개', '5개 이상'])
        
    with tab4:
        # 상세필터 선택
        st.subheader('상세필터 선택')
        filters = st.multiselect('상세필터를 선택하세요',
                                 ['선택안함',
                                  '주차 가능',
                                  '관리비 없음',
                                  '반려동물 가능',
                                  '반지하 상관없음',
                                  '세탁기',
                                  '건조기',
                                  '에어컨',
                                  '가스레인지',
                                  '인덕션',
                                  '엘리베이터'])

        st.text(f'선택하신 상세필터는 {filters} 입니다') 

# 매물 구성함수
def result():
    tab1, tab2, tab3 = st.tabs(['종합', '가격', '거리'])
    
    with tab1:
        # 종합적으로 봤을 때 가장 suitable한 매물
        st.subheader('종합필터 적용 결과')
        st.text('선택하신 필터를 종합적으로 봤을 때 가장 잘 맞는 매물입니다')
        for i in range(1, 5):
            with st.container(border=True): 
                st.write(f"**매물 {i}: 선택한 지역 {i}순위로 반영**")
                st.write("매물의 특징: 거리가 가깝습니다!")
                st.write("배경: 방 사진")
                st.write("뜨는 정보: 지역, 평수, 방 개수, 보증금, 월세")

    with tab2:
        # 가격면에서 봤을 때 가장 suitable한 매물
        st.subheader('가격필터 적용 결과')
        st.text('선택하신 필터를 가격면에서 봤을 때 가장 잘 맞는 매물입니다')
        for i in range(1, 5):
            with st.container(border=True): 
                st.write(f"**매물 {i}: 선택한 지역 {i}순위로 반영**")
                st.write("매물의 특징: 거리가 가깝습니다!")
                st.write("배경: 방 사진")
                st.write("뜨는 정보: 지역, 평수, 방 개수, 보증금, 월세")
                
    with tab3:
        # 거리적으로 봤을 때 가장 suitable한 매물
        st.subheader('거리필터 적용 결과')
        st.text('선택하신 필터를 거리 기준으로 봤을 때 가장 잘 맞는 매물입니다')
        for i in range(1, 5):
            with st.container(border=True):
                st.write(f"**매물 {i}: 선택한 지역 {i}순위로 반영**")
                st.write("매물의 특징: 거리가 가깝습니다!")
                st.write("배경: 방 사진")
                st.write("뜨는 정보: 지역, 평수, 방 개수, 보증금, 월세")

# 페이지별 화면 구성
if menu == '방구 소개':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        img = Image.open('./data/images/image3.png')
        st.image(img, width=200, caption='방구 마스코트')
    st.write('방구에 대한 소개 - 방구는 무엇인가? 우리의 강점')

elif menu == '방 찾기':
    st.subheader('방 찾기')
    st.write('방구에 오신걸 환영합니다!')
    room_search()
      
else:
    st.subheader('매물')
    st.write('선택하신 필터에 따른 매물 리스트입니다!')
    result()
    
