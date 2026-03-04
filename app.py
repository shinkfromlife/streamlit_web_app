import streamlit as st
from PIL import Image
import pandas as pd
import matplotlib.pyplot as pit

st.title('サンプル')
st.caption('サンプルアプリ')

col1, col2 = st.columns(2)

with col1:
    st.subheader('紹介')
    st.text('Pythonサンプルアプリ')
    code = '''
    import streamlit as st

    st.title('サンプル)
    '''
    st.code(code, language='python')

    # 画像
    image = Image.open('03.jpg')
    st.image(image, width=200)

    with st.form(key='profile_form'):
        # TextBox
        name = st.text_input('名前')
        address = st.text_input('住所')

        # select
        category = st.multiselect(
            '年齢',
            ('以上', '未満')
        )

        # button
        submit_button = st.form_submit_button('送信')
        cancel_button = st.form_submit_button('キャンセル')

    if submit_button:
        st.text(f'{name}さん、住所は{address}ですね？')
        st.text(f': {", ".join(category)}')

with col2:
    st.text(f'print')