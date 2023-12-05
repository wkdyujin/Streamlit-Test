import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px
import xlsxwriter # pip install XlsxWriter

@st.cache_resource
def get_stock_info():
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"    
    method = "download"
    url = "{0}?method={1}".format(base_url, method)   
    df = pd.read_html(url, header=0, encoding='euc-kr')[0] # ---> chrome 임시 저장소에 담아둘 수 있음(캐싱)
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")     
    df = df[['회사명','종목코드']]
    return df

def get_ticker_symbol(company_name):     
    df = get_stock_info()
    code = df[df['회사명']==company_name]['종목코드'].values
    if len(code) != 0: # 검색 결과가 있을 때
        ticker_symbol = code[0]
        return ticker_symbol

# 코드 조각 추가
st.sidebar.header("회사 이름과 기간을 입력하세요")
stock_name = st.sidebar.text_input('회사 이름')
today = datetime.datetime.now()
date_range = st.sidebar.date_input(
    label = "시작일 - 종료일",
    value = (datetime.date(2000, 1, 1), today), # 튜플로 값을 2개 넣으면 시작-종료일 설정 가능
    max_value = today,
    format="YYYY/MM/DD",
)

is_click = st.sidebar.button('주가 데이터 확인')
st.header("무슨 주식을 사야 부자가 되려나 ....")

if is_click:
    ticker_symbol = get_ticker_symbol(stock_name)

    start_p = date_range[0].strftime("%Y-%m-%d") # 파라미터: 2000-00-00 형태        
    end_p = (date_range[1] + datetime.timedelta(days=1)).strftime("%Y-%m-%d") 

    df = fdr.DataReader(ticker_symbol, start_p, end_p)
    df.index = df.index.date
    st.subheader(f"[{stock_name}] 주가 데이터")
    st.dataframe(df.head())

    df_to_graph = df.rename_axis('Date').reset_index()
    # st.line_chart(
    #     df, x='Date', y='Close', color="#0000FF"
    # )

    fig = px.line(
        df_to_graph,
        x = 'Date',
        y = 'Close',
    )
    st.plotly_chart(fig, use_container_width=True)
    
    col1, col2, = st.columns(2)
    with col1:
        st.download_button('CSV 다운로드', df.to_csv().encode('utf-8'), 'app.csv', 'text/csv')
    with col2:
        buffer = BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Sheet1', index=False)
            download2 = st.download_button(
                label="엑셀 파일 다운로드",
                data=buffer,
                file_name='large_df.xlsx',
                mime='application/vnd.ms-excel'
            )