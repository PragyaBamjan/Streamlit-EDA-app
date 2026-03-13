import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Exploratory Data Analysis App')

uploaded_file = st.file_uploader('Upload a CSV file', type='csv')

if uploaded_file is not None:
    @st.cache_data
    def load_data(file):
        return pd.read_csv(file)

    df = load_data(uploaded_file)
    st.write('### Data Preview', df.head())

    numeric_columns = df.select_dtypes('number').columns

    selected_var = st.sidebar.selectbox('Select Variable', numeric_columns)
    bins = st.sidebar.slider('Number of Bins', 5, 50, 20)

    fig, ax = plt.subplots()
    ax.hist(df[selected_var], bins=bins)
    ax.set_xlabel(selected_var)
    ax.set_ylabel('Frequency')
    st.pyplot(fig)

    st.subheader('Summary Statistics')
    st.write(df[selected_var].describe())