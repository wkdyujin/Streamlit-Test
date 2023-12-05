import streamlit as st
import pandas as pd

data = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


#####################################################
#                       입력                        #
#####################################################


st.title("1. 입력")
btn_res = st.button('Hit me')

is_check = st.checkbox('Check me out')
if is_check: 
    st.data_editor(data)

st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])

bird_list = ['노랑새', '비둘기', '펭귄']
img_list = ['https://i.imgur.com/e0JBf0q.jpg',
            'https://image.dongascience.com/Photo/2016/07/14694309465749.png',
               'https://i.imgur.com/6qRYLMC.jpg']

ans = st.text_input('Enter some text')
for bird in bird_list: 
    if ans in bird:
        img = img_list[bird_list.index(bird)]
        break
if ans != '':
    st.image(img)


st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')

@st.cache_data 
def convert_df(df):
    return df.to_csv().encode('utf-8')

st.download_button('Download Button', convert_df(data), 'app.csv', 'text/csv')
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')


#####################################################
#                       출력                        #
#####################################################

st.title("2. 출력")
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True