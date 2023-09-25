import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(page_icon=" :bar_chart:",page_title="Visualizations",layout="wide")
css="""
    <style>
    div.block-container {
        padding-top:1rem;
        text-align: center;
    .custom-text {
        color: #C16F56 !important; /* Change the color to your desired color */
    }
    .custom-text a {
        color: #C16F56 !important; /* Change the color to your desired color */
        text-decoration: none !important; /* Remove the underline */
    }
"""
st.markdown(css,unsafe_allow_html=True)
st.title(":chart_with_downwards_trend: Telecom Customer churn  ")


st.write('<span class="custom-text">Data source: <a class="custom-text" href="https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/input" target="_blank"> https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/input</a></span>', unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")

#'<span class="custom-text">This text has a custom color.</span>', unsafe_allow_html=True

#df=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df=pd.read_csv("https://raw.githubusercontent.com/AbeerDib/Final/main/WA_Fn-UseC_-Telco-Customer-Churn.csv")
st.subheader("1-Interactive dataframe ")
col1,col2=st.columns([1.3,1])
with col2:
    rows = st.slider('Select the range of rows you want to see', 
                    min_value=1,max_value= len(df),value=(1, 5),step=1)
with col1:
    selected_columns1 = st.multiselect(
        "Select Columns:",
        df.columns,
        default=["gender","SeniorCitizen","Contract","Churn"]
    )
sliced_df = df.iloc[rows[0] :rows[1], :][selected_columns1]
# Display the sliced DataFrame as a table
st.write("")
st.write("")
st.write("Selected Data:")
st.dataframe(sliced_df)
 

#df.loc[rows]
#filtered_df=df[(df['Value'] >= rows[0]) & (df['Value'] <= rows[1])]
#filtered_df
st.write("")
st.write("")
st.write("")


st.subheader("2-Interactive piechart ")
#col1, col2 = st.columns([1,3])


  #  st.write('<style>div.st-d5{margin-left: 0%;}</style>', unsafe_allow_html=True)  #
#with col1:
 #   st.write("")
  #  st.write("")
   # st.write("")
    #st.write("")
    #st.write("")
   # st.write("")
    #st.write("")
    #st.write("")
    #st.write("")
selected_columns = [col for i, col in enumerate(df.columns) if i not in [0,5,18,19]]
feature=st.sidebar.selectbox("Pick your filter for the pie chart ",selected_columns,key="feature")
fig = px.pie(df, names=feature, title=f'Pie Chart of {feature}',template="seaborn")
    #fig.update_layout(legend=dict(orientation="h", y=1.2, x=0))
fig.update_layout(
        title=dict(text=f'Bar Chart of {feature}',x=0.36),  # Title position (x=0.5 centers it)
        title_font=dict(color='grey'),
          margin=dict(l=50, r=50, b=50, t=50),  # Title color
        )
st.plotly_chart(fig)
st.subheader("3-Interactive bar chart")
col1,col2=st.columns([1,3])
col1.write("")
col1.write("")
col1.write("")
with col1:
    col1.write("")
    col1.write("")
    col1.write("")
    col1.write("")
    col1.write("")
    col1.write("")


    feature1=st.selectbox("Pick your filter for the bar chart ",selected_columns,key="feature1",index=1)
    feature2=st.selectbox("Pick your filter for the bar chart ",selected_columns,key="feature2",index=15)
with col2:
    if feature1 != feature2: 
        grouped = df.groupby([feature1, feature2]).size().reset_index(name='Count')
            # grouped bar chart 
        fig = px.bar(grouped, x=feature1, y='Count', color=feature2, barmode='group',template="seaborn")
            # Customize the chart


        fig.update_layout(
        title_font=dict(color='grey'),  # Title color
        title=dict(text=f' {feature1} and  {feature2} ',x=0.135),
        xaxis_title=feature1,
        yaxis_title='Count',
        legend_title=feature2,
        #legend=dict(orientation="h", y=1,x=-0.1)
        )
        st.plotly_chart(fig)
    else:
        st.markdown("<h2 style='color:red;'>Columns must be different!!</h2>", unsafe_allow_html=True)
        st.markdown("<h2 style='color:red;'>Please select another column</h2>", unsafe_allow_html=True)
        
#st.write(":chart_with_upwards_trend: :telephone_receiver: :chart_with_downwards_trend:")
col1.write("")
col1.write("")
col1.write("")
check=st.checkbox("Check for the box plots!")
if check:
   # st.write('Feature activated!')
   col1,col2=st.columns(2)
   with col1:
    on1=st.toggle('Total charges')
    if on1:
    
        fig = px.box(df, y="TotalCharges")
        fig.update_layout(
                title=dict(text='Box Plot for the customers total charges',x=0.28),  # Title position (x=0.5 centers it)
                title_font=dict(color='grey') ,
                 width=450 # Title color
            )
        st.plotly_chart(fig)
    else:
        st.write("")
    with col2:
        on2=st.toggle('Monthly charges')
        if on2:
        
            fig = px.box(df, y="MonthlyCharges")
            fig.update_layout(
                    title=dict(text='Box Plot for the customers monthly charges',x=0.28),  # Title position (x=0.5 centers it)
                    title_font=dict(color='grey') , # Title color
                    width=450,
                    
                )
            st.plotly_chart(fig)
        else:
            st.write("")
   