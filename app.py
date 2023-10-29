from main import *

st.set_page_config(page_title='Text Extractor',layout='wide',page_icon='icon.jpeg')
st.header('EXTRACT TEXT FROM IMAGE - (ENGLISH ONLY)')
# st.markdown("<h1 style='text-align: center; color: white;'>EXTRACT TEXT FROM IMAGE</h1>", unsafe_allow_html=True)
st.subheader('Start By Uploading A File')
uploaded_file = st.file_uploader("Choose a file",type = ['png', 'jpg'])
show_file = st.empty()
if uploaded_file is not None:
    try:
        bytes_data = uploaded_file.getvalue()
        if isinstance(uploaded_file, BytesIO):
            show_file.image(uploaded_file)
        with st.spinner('Wait for it...'):
            text = extractTextFromImg(bytes_data) 
            st.write(text)
    except:
        st.write('An Error Occured. Try Again Later')