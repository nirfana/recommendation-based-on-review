# Contents of `app1.py`
import streamlit as st

def app():
    st.title('Exploratory Data Analysis')

    st.header('Target Label Proportion')
    st.image('target label proportion.png', caption='Picture 1: Target Label Proportion')
    st.write('''The plot shows the distribution of user suggestions for a yes or no question. The left pie chart shows that 83.8% of users suggesting yes, while 16.2% suggesting no. 
                The plot also shows a class imbalance, where one class has a significantly higher proportion of data points compared to the other. In this case, it's a binary classification problem with:''')
    st.write('''- **Majority Class**: This is the dominant class, represented by the larger pie slice (83.8%) who responded `Yes` in your example.''')
    st.write('''- **Minority Class**: This is the smaller class, represented by the smaller pie slice (16.2%) who responded `No`.''')
    
    
    st.header('Most Words Appear In Review')
    st.image('wordcloud.png', caption='Picture 2: Most Words Appear In Review')
    st.write('''The word cloud depicts words commonly found in skincare product reviews. Here are some of the most prominent words:''')
    st.write('''- **Moisturizer**: This suggests that the reviews are about a product that hydrates the skin.''')
    st.write('''- **Skin**: This is not surprising as the word cloud is about product reviews.''')
    st.write('''- **Love**: People seem to really like this product!''')
    st.write('''- **Dry**: This might be an indicator that the product is effective for dry skin.''')
    st.write('''- **Soft**: Another positive descriptor for the product’s effect on skin.''')
    st.write('''- **Cream**: This could be the type of product being reviewed.''')
    st.write('''- **Face**: This again reinforces that the reviews are about a facial skin care product.''')
    st.write('''- **Buy**: This indicates positive sentiment towards the product.''')
    st.write('''- **Price**: People are considering the price of the product in their reviews.''')
    st.write('''- **Breakout**: This suggests that some reviewers experienced irritation from the product.''')
    st.write('''- **Sensitive**: This indicates that the product might not be suitable for all skin types.''')



if __name__ == '__main__':
    app()
