import streamlit as st

# layout 요소
#columns는 요소를 왼쪽에서 오른쪽으로 배치할 수 있음

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        '오늘의 날씨',
        value='35도',
        delta='+3'
    )

with col2:
    st.metric(
        '오늘의 미세먼지',
        value='좋음',
        delta='-30',
        delta_color='inverse'
    )
    
with col3:
    st.metric(
        '오늘의 습도',
        value='비키니시티',
        delta='전방에 스폰지밥 출근중'
    )    
    
# 
st.markdown('---')

data = {
    'Name': ['Sue', 'Chris', 'John'],
    'Age': [10, 20, 30]
}

import pandas as pd

df = pd.DataFrame(data)
st.dataframe(df)

st.divider()

st.table(df)

st.divider()

st.json(data)

# datafile.csv => load => print table => px.box() => st.plotly_chart()
st.divider()

df_abnb = pd.read_csv('./data/ABNB_stock.csv')
st.title('ABNB_stock')
st.table(df_abnb.head(5))

st.header('Boxplot')

import plotly.express as px
color = px.colors.sequential.Plotly3

df_abnb['YearMonth'] = pd.to_datetime(df_abnb['Date']).dt.to_period('M').astype(str)

fig = px.box(df_abnb, x= 'YearMonth', y='Volume', color="YearMonth", 
    color_discrete_sequence=color)
st.plotly_chart(fig)

######################

x_options = ['YearMonth','Open', 'Close']
y_options = ['Volume','High', 'Low']

x_option = st.selectbox(
    'Select X-axis',
    index=None, # 초기 선택값 지정 안되게 함
    options=x_options
)

y_option = st.selectbox(
    'Select Y-axis',
    index=None,
    options=y_options
)

if (x_option != None) & (y_option != None):
    fig3 = px.box(
        data_frame=df_abnb, x=x_option, y=y_option,
        color="YearMonth", color_discrete_sequence=color, 
        width=500
        )
    st.plotly_chart(fig3 , key= 2)




