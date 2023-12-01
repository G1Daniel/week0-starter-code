import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.set_page_config(page_title='Dashboard', layout='wide')
    st.title('My Shop Dashboard')

    st.sidebar.title('Menu')
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            background-color: black;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    button_states = {
        'Home': True,
        'Sales': False,
        'Buy': False
    }

    button_states['Home'] = st.sidebar.button('Home')
    button_states['Sales'] = st.sidebar.button('Sales')
    button_states['Buy'] = st.sidebar.button('Buy')

    if button_states['Home']:
        display_home()
    elif button_states['Sales']:
        display_sales()
    elif button_states['Buy']:
        display_buy()

def display_home():
    labels = ['Sales', 'Buy']
    sizes = [65, 35]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)   

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')   
    fig1.set_size_inches(3, 3)  

    st.pyplot(fig1)

def display_sales():
    st.write('This is the Sales page.')
    

def display_buy():
    st.write('Here is the Buy page.')

if __name__ == '__main__':
    main()