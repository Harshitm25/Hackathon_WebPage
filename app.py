# import streamlit as st

# st.title(':blue[Welcome to ctrl_alt_defeat]')
# choice = st.selectbox('Login/SignUp', ['Login', 'SignUp'])
# if choice == 'Login':
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type = 'password')
#     st.button('Login')
# else:
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type = 'password')
#     username = st.text_input('Enter your username')
#     st.button('Create Account')

# import streamlit as st

# st.title(':blue[Welcome to ctrl_alt_defeat]')
# choice = st.selectbox('Login/SignUp', ['Login', 'SignUp'])

# if choice == 'Login':
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type='password')

#     if st.button('Login'):
#         # Basic validation: check if email and password are not empty
#         if not email or not password:
#             st.error('Please enter both email and password.')
#         else:
#             # Add your login logic here
#             # For now, just display a success message
#             st.success(f'Logging in with email: {email}')
# else:
#     email = st.text_input('Email Address')
#     password = st.text_input('Password', type='password')
#     username = st.text_input('Enter your username')

#     if st.button('Create Account'):
#         # Basic validation: check if email, password, and username are not empty
#         if not email or not password or not username:
#             st.error('Please fill in all the fields.')
        # else:
        #     # Add your account creation logic here
        #     # For now, just display a success message
        #     st.success(f'Account created for {username} with email: {email}')



import streamlit as st

st.title(':blue[Welcome to ctrl_alt_defeat]')
choice = st.selectbox('Login/SignUp', ['Login', 'SignUp'])

if choice == 'Login':
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if not email or not password:
            st.error('Please enter both email and password.')
        else:
            # Add your login logic here
            # For now, just display a success message
            st.success(f'Logging in with email: {email}')
else:
    email = st.text_input('Email Address')
    password = st.text_input('Password', type='password')
    username = st.text_input('Enter your username')

    if st.button('Create Account'):
        if not email or not password or not username:
            st.error('Please fill in all the fields.')
        else:
            st.success(f'Account created for {username} with email: {email}')


