import streamlit as st
import preproccessor,helper
st.sidebar.title("Whatsapp Chat Analyzer")
uploaded_file = st.sidebar.file_uploader("choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data = bytes_data.decode("utf-8")
    df = preproccessor.preproccess(data)
    st.dataframe(df)
    user_list = df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt",user_list)
    if st.sidebar.button("Show Analysis"):

         num_messages = helper.fetch_stats(selected_user, df)

         col1, col2, col3, col4 = st.columns(4)

         with col1:
             st.header("Total Messages")
             st.title(num_messages)