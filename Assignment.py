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

st.write("<h9>Welcome to our webpage all about the Kaggle customer churn dataset! This dataset has lots of details about customers and whether they leave a service or not. Our visuals will help you see the important things in this dataset and make smart choices to stop customers from leaving.</h9>",unsafe_allow_html=True)

st.write("")


#'<span class="custom-text">This text has a custom color.</span>', unsafe_allow_html=True

#df=pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df=pd.read_csv("https://raw.githubusercontent.com/AbeerDib/Final/main/WA_Fn-UseC_-Telco-Customer-Churn.csv")
st.write("<h3 style='color: #FA2A55;'>1-Interactive dataframe </h3>",unsafe_allow_html=True)
text1 = '<h9 style="line-height: 0.5;">The telecom customer churn dataset originally has  contains 7043 rows (customers) and 21 columns (features) while only 2 columns are numercial (Monthly and total charges).</h9>'
text2 = '<h9 style="line-height: 0.5;">Use the side bars to choose the columns and rows you want to see.</h9>'

# Display both lines in a single st.write() call
st.write(text1 + text2, unsafe_allow_html=True)
st.sidebar.markdown("**Each visual is interactive.Choose the values that you're interested to intvestigate**")
st.sidebar.markdown("Dataframe")

rows = st.sidebar.slider('Select the range of rows', 
     min_value=1,max_value= len(df),value=(1, 5),step=1)

selected_columns1 = st.sidebar.multiselect(
        "Select Columns:",
        df.columns,
        default=["gender","SeniorCitizen","Contract","Churn"]
    )
sliced_df = df.iloc[rows[0] :rows[1], :][selected_columns1]
# Display the sliced DataFrame as a table


st.dataframe(sliced_df)
custom_text = "Data source: [https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/input](https://www.kaggle.com/code/bhartiprasad17/customer-churn-prediction/input)"
st.markdown(f'<span style="color: blue;">{custom_text}</span>', unsafe_allow_html=True)



#df.loc[rows]
#filtered_df=df[(df['Value'] >= rows[0]) & (df['Value'] <= rows[1])]
#filtered_df
st.write("")



st.write("<h3 style='color: #FA2A55;'>2-Interactive piechart </h3>",unsafe_allow_html=True)
text1 = '<p style="line-height: 0.5;">This piechart represents the ditribution of categorical data in this dataset.</p>'
text2 = '<p style="line-height: 0.5;">Choose a categorical column from the sidebar to visualze its distribution</p>'

# Display both lines in a single st.write() call
st.write(text1 + text2, unsafe_allow_html=True)


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
default1="Churn"
st.sidebar.markdown("")
st.sidebar.markdown("Piechart")
feature=st.sidebar.selectbox("Pick a categorical column  ",selected_columns,selected_columns.index(default1),key="feature")


fig = px.pie(df, names=feature, title=f'Pie Chart of {feature}',template="plotly_dark")
    #fig.update_layout(legend=dict(orientation="h", y=1.2, x=0))
fig.update_layout(
        title=dict(text=f'Bar Chart of {feature}',x=0.35),  # Title position (x=0.5 centers it)
        title_font=dict(color='grey'),
        margin=dict(l=60, r=60, b=60, t=60),  # Title color
            )
st.plotly_chart(fig)
    


st.write("<h3 style='color: #FA2A55;'>3-Interactive barchart </h3>",unsafe_allow_html=True)
st.sidebar.markdown("")
st.sidebar.markdown("Side by side boxplot")

feature1=st.sidebar.selectbox("Pick your filter for the bar chart ",selected_columns,key="feature1",index=15)
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
    

    text1 = '<p style="line-height: 1;">This barchart helps visualize the relationship between the customers churn and the other chosen categorical variables. <b>You might find intersting patterns!</b> </p>'
    text2 = '<p style="line-height: 1;">Choose your variables that you want to visualize with the customer churn from the sidebar</p>'

    # Display both lines in a single st.write() call
    st.write(text1 + text2, unsafe_allow_html=True)


    
with col2:
    grouped = df.groupby(["Churn", feature1]).size().reset_index(name='Count')
            # grouped bar chart 
    fig = px.bar(grouped, x="Churn", y='Count', color=feature1, barmode='group',template="plotly_dark")
            # Customize the chart


    fig.update_layout(
        title_font=dict(color='grey'),  # Title color
        title=dict(text=f' Churn and  {feature1} ',x=0.135),
        xaxis_title="Churn",
        yaxis_title='Count',
        legend_title=feature1,
        #legend=dict(orientation="h", y=1,x=-0.1)
        )
    st.plotly_chart(fig)

        
#st.write(":chart_with_upwards_trend: :telephone_receiver: :chart_with_downwards_trend:")
col1.write("")
col1.write("")
col1.write("")


   # st.write('Feature activated!')
col1,col2=st.columns(2)
with col1:
    on1=st.toggle('Total charges',value=True)
    if on1:
    
        fig = px.box(df, y="TotalCharges")
        fig.update_layout(
                title=dict(text='Box Plot for the customers total charges',x=0.28),  # Title position (x=0.5 centers it)
                title_font=dict(color='grey') ,
                 width=450 # Title color
            )
        st.plotly_chart(fig)
        st.write("Distribution of the customers' total charges within the company in usd")
   
with col2:
    on2=st.toggle('Monthly charges',value=True)
    if on2:
        
        fig = px.box(df, y="MonthlyCharges")
        fig.update_layout(
            title=dict(text='Box Plot for the customers monthly charges',x=0.28),  # Title position (x=0.5 centers it)
            title_font=dict(color='grey') , # Title color
            width=450,
                    
                )
        st.plotly_chart(fig)
        st.write("Distribution of the customers' monthly charges within the company in usd")
    else:
        st.write("")
   
  
   
