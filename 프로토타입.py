import os
import streamlit as st
from PIL import Image
import pydeck as pdk  

st.title('방구 - 맞춤 방 구하기 서비스')

# ---------------- 세션 상태 초기화 ----------------
if "menu" not in st.session_state:
    st.session_state.menu = "방구 소개"
if "section" not in st.session_state:
    st.session_state.section = "기본 정보"

def _sync_menu():
    st.session_state.menu = st.session_state.menu_select

def _sync_section():
    st.session_state.section = st.session_state.section_radio

# ------- 지도 함수 -------
def show_radii_map(lat, lon, selected_km=None, custom_m=None):
    """중심 좌표 기준으로 1/3/5km 또는 커스텀(m) 원을 pydeck으로 표시"""
    base = [
        {"lat": lat, "lon": lon, "radius": 1000, "label": "1 km"},
        {"lat": lat, "lon": lon, "radius": 3000, "label": "3 km"},
        {"lat": lat, "lon": lon, "radius": 5000, "label": "5 km"},
    ]
    circles = list(base)

    highlight = None
    if custom_m:
        circles.append({
            "lat": lat, "lon": lon, "radius": int(custom_m),
            "label": f"{custom_m/1000.0:.1f} km (custom)"
        })
        highlight = int(custom_m)
    elif selected_km:
        highlight = int(selected_km * 1000)

    for c in circles:
        c["is_selected"] = (highlight is not None and c["radius"] == highlight)

    layer_circles = pdk.Layer(
        "ScatterplotLayer",
        circles,
        get_position='[lon, lat]',
        get_radius="radius",
        filled=True,
        opacity=0.15,
        stroked=True,
        get_fill_color='[0, 122, 255, 90]',
        # 선택된 원은 라인 색 더 진하게
        get_line_color='[is_selected ? 0 : 0, is_selected ? 0 : 122, is_selected ? 0 : 255, is_selected ? 230 : 150]',
        line_width_min_pixels=2,
        pickable=True,  
    )

    layer_center = pdk.Layer(
        "ScatterplotLayer",
        [{"lat": lat, "lon": lon, "radius": 60, "label": "중심"}],
        get_position='[lon, lat]',
        get_radius="radius",
        filled=True,
        get_fill_color='[220, 20, 60, 220]',
        stroked=False,
    )

    view_state = pdk.ViewState(latitude=lat, longitude=lon, zoom=12)
    st.pydeck_chart(pdk.Deck(
        layers=[layer_circles, layer_center],
        initial_view_state=view_state,
        tooltip={"text": "{label}"},
    ))

# ---------------- 사이드바: 메뉴/섹션 선택 + 완료 ----------------
st.sidebar.header('메뉴')
st.sidebar.selectbox(
    '메뉴선택',
    ['방구 소개', '방 찾기', '매물'],
    index=['방구 소개', '방 찾기', '매물'].index(st.session_state.menu),
    key='menu_select',
    on_change=_sync_menu
)

def sidebar_nav():
    st.sidebar.subheader("방 찾기")
    st.sidebar.radio(
        "필터",
        ['기본 정보', '예산', '방', '상세조건'],
        index=['기본 정보', '예산', '방', '상세조건'].index(st.session_state.section),
        key="section_radio",
        on_change=_sync_section
    )
    if st.sidebar.button("완료"):
        st.session_state.menu = "매물"
        st.rerun()

# ---------------- 매물(메인 영역) ----------------
def result():
    tab1, tab2, tab3 = st.tabs(['종합', '가격', '거리'])

    with tab1:
        st.subheader('종합필터 적용 결과')
        st.text('선택하신 필터를 종합적으로 봤을 때 가장 잘 맞는 매물입니다')
        for i in range(1, 5):
            with st.container(border=True):
                st.write(f"**매물 {i}: 선택한 지역 {i}순위로 반영**")
                st.write("매물의 특징: 거리가 가깝습니다!")
                st.write("배경: 방 사진")
                st.write("뜨는 정보: 지역, 평수, 방 개수, 보증금, 월세")

    with tab2:
        st.subheader('가격필터 적용 결과')
        st.text('선택하신 필터를 가격면에서 봤을 때 가장 잘 맞는 매물입니다')
        for i in range(1, 5):
            with st.container(border=True):
                st.write(f"**매물 {i}: 가격순 {i}위**")
                st.write("매물의 특징: 저렴합니다!")
                st.write("배경: 방 사진")
                st.write("뜨는 정보: 지역, 평수, 방 개수, 보증금, 월세")

    with tab3:
        st.subheader('거리필터 적용 결과')
        st.text('선택하신 필터를 거리 기준으로 봤을 때 가장 잘 맞는 매물입니다')
        for i in range(1, 5):
            with st.container(border=True):
                st.write(f"**매물 {i}: 선택한 지역 {i}순위로 반영**")
                st.write("매물의 특징: 거리가 가깝습니다!")
                st.write("배경: 방 사진")
                st.write("뜨는 정보: 지역, 평수, 방 개수, 보증금, 월세")

# ---------------- 페이지 라우팅 ----------------
if st.session_state.menu == '방구 소개':
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        img = Image.open('./data/images/image3.png')
        st.image(img, width=200, caption='방구 마스코트')
    st.write('방구에 대한 소개 - 방구는 무엇인가? 우리의 강점')

elif st.session_state.menu == '방 찾기':
    sidebar_nav()

    # --- 메인: 섹션별 UI ---
    if st.session_state.section == '기본 정보':
        st.subheader('원하는 동네 기준 선택')

        check_work = st.checkbox('회사 근처가 좋아요', key="check_work_main")
        if check_work:
            work_input = st.text_input('회사 주소를 입력해주세요', key="work_input_main")
            st.caption(f'입력하신 회사 주소: {work_input or "-"}')

            st.markdown("##### 지도와 반경")

            col_lat, col_lon = st.columns(2)
            with col_lat:
                lat_str = st.text_input("위도(lat) 입력 (예: 37.5665)", key="lat_input", placeholder="37.5665")
            with col_lon:
                lon_str = st.text_input("경도(lon) 입력 (예: 126.9780)", key="lon_input", placeholder="126.9780")

            lat = lon = None
            if lat_str and lon_str:
                try:
                    lat = float(lat_str)
                    lon = float(lon_str)
                except ValueError:
                    st.error("위도/경도는 숫자로 입력해 주세요. 예: 37.5665 / 126.9780")

            # 반경 선택 
            colA, colB = st.columns(2)
            with colA:
                # 라벨은 "1 km" 형태로 표시, 내부 값은 숫자 km로 사용
                radius_label = st.radio("반경 선택", ["1 km", "3 km", "5 km"], index=0, horizontal=True)
                radius_km = int(radius_label.split()[0])
            with colB:
                custom_on = st.checkbox("커스텀 반경(m)", value=False)
            custom_m = st.slider("커스텀 반경(미터)", 200, 10000, 2000, 100) if custom_on else None

            if custom_on:
                st.caption(f"커스텀 반경: {custom_m} m ({custom_m/1000:.2f} km)")


            # 위도/경도가 유효할 때만 지도 표시
            if (lat is not None) and (lon is not None):
                show_radii_map(lat, lon, selected_km=None if custom_on else radius_km, custom_m=custom_m)
            else:
                st.info("위도와 경도를 입력하면 지도에 반영됩니다.")

        check_town = st.checkbox('원하는 동네가 있어요', key="check_town_main")
        if check_town:
            town_input = st.text_input('원하는 동네를 입력해주세요', key="town_input_main")
            st.caption(f'입력하신 동네: {town_input or "-"}')

        st.divider()
        
        st.subheader('연령대 선택')
        st.selectbox('연령대를 선택하세요',
                     ['선택안함', '20대', '30대', '40대', '50대 이상'],
                     key="age_main")

    elif st.session_state.section == '예산':
        st.subheader('보증금 선택')
        min_deposit, max_deposit = st.slider(
            '원하는 보증금 범위 (만원)',
            min_value=0, max_value=10000, value=(50, 200), key="deposit"
        )
        st.caption(f'보증금: {min_deposit} ~ {max_deposit} 만원')

        st.divider()

        st.subheader('월세 선택')
        min_rent, max_rent = st.slider(
            '원하는 월세 범위 (만원)',
            min_value=0, max_value=200, value=(30, 50), key="rent"
        )
        st.caption(f'월세: {min_rent} ~ {max_rent} 만원')

    elif st.session_state.section == '방':
        st.subheader('평수 선택')
        min_size, max_size = st.slider(
            '원하는 평수 범위',
            min_value=0, max_value=200, value=(10, 30), key="size"
        )
        st.caption(f'평수: {min_size} ~ {max_size} 평')

        st.divider()

        st.subheader('방 개수 선택')
        st.selectbox(
            '방 개수를 선택하세요',
            ['상관없음', '1개', '2개', '3개', '4개', '5개 이상'],
            key="rooms"
        )

    elif st.session_state.section == '상세조건':
        st.subheader('상세필터 선택')
        filters = st.multiselect(
            '상세필터를 선택하세요',
            ['선택안함','주차 가능','관리비 없음','반려동물 가능','반지하 상관없음',
             '세탁기','건조기','에어컨','가스레인지','인덕션','엘리베이터'],
            key="filters"
        )
        st.caption(f'선택한 상세필터: {", ".join(filters) if filters else "-"}')

else:  # '매물'
    st.subheader('매물')
    st.write('선택하신 필터에 따른 매물 리스트입니다!')
    result()
