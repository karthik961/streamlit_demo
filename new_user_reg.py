import streamlit as st

# Create a session state to store user registration data
if "registered_users" not in st.session_state:
    st.session_state.registered_users = []

def registration():
    st.title("User Registration")

    username = st.text_input("Username:")
    email = st.text_input("Email:")
    password = st.text_input("Password:", type="password")
    confirm_password = st.text_input("Confirm Password:", type="password")

    if st.button("Register"):
        if password == confirm_password:
            st.success("Registration successful!")
            st.session_state.registered_users.append({"username": username, "email": email, "password": password})
        else:
            st.error("Passwords do not match. Please try again.")

def main():
    st.sidebar.title("Navigation")
    selected_page = st.sidebar.radio("Select Page", ["Home", "Register"])

    if selected_page == "Home":
        st.title("Home Page")
        st.write("Welcome to the home page!")

    elif selected_page == "Register":
        registration()

if __name__ == "__main__":
    main()
