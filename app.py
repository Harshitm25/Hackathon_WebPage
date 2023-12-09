# import streamlit as st

# st.title(':blue[Welcome to ctrl_alt_defeat]')
# choice = st.selectbox('Login/SignUp', ['Login', 'SignUp'])

# if choice == 'Login':
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type='password')

#     if st.button('Login'):
#         if not email or not password:
#             st.error('Please enter both email and password.')
#         else:
#             st.success(f'Logging in with email: {email}')
# else:
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type='password')
#     username = st.text_input('Enter your username')

#     if st.button('Create Account'):
#         if not email or not password or not username:
#             st.error('Please fill in all the fields.')
#         else:
#             st.success(f'Account created for {username} with email: {email}')


import streamlit as st

st.title(':blue[Welcome to ctrl_alt_defeat]')
st.header('Sign up')

email=st.text_input('Email Address')
password=st.text_input('password',type='password')
username=st.text_input("enter your username")

if st.button('Create Account'):
    if not email or not password or not username:
        st.error("please fill all the fields")
    else:
        st.success(f'Account created for {username} with email:{email}')

