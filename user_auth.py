import streamlit as st

# Define a hardcoded username and password (for demonstration purposes)
correct_username = "user123"
correct_password = "password123"

# Create a session state to store user authentication status
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

def login():
    st.title("Login Page")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        if username == correct_username and password == correct_password:
            st.success("Login successful!")
            st.session_state.authenticated = True
        else:
            st.error("Invalid username or password.")

def main():
    if st.session_state.authenticated:
        st.title("Authenticated Page")
        st.write("Welcome to the authenticated page!")
        # Add your content for authenticated users here
    else:
        login()

if __name__ == "__main__":
    main()
