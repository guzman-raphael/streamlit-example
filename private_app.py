# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app/

# import streamlit as st
# import datajoint as dj
# from streamlit_keycloak import login

# st.title('Hi raph!')



from dataclasses import asdict
from streamlit_keycloak import login
import streamlit as st


def main():
    st.subheader(f"Welcome {keycloak.user_info['preferred_username']}!")
    st.write(f"Here is your user information:")
    st.write(asdict(keycloak))
    if st.button("Disconnect"):
        keycloak.authenticated = False


st.title("Streamlit Keycloak example")
keycloak = login(
    url="https://accounts.datajoint.com",
    realm="master",
    client_id=st.secrets["auth"]["client_id"],
    client_secret=st.secrets["auth"]["client_secret"],
)

if keycloak.authenticated:
    main()