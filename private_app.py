# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app/

# import streamlit as st
# import datajoint as dj
# from streamlit_keycloak import login

# st.title('Hi raph!')



import streamlit as st
import streamlit_keycloak
import datajoint as dj


def get_connection():
    keycloak = streamlit_keycloak.login(
        url="https://keycloak.dev.datajoint.io",
        realm="master",
        client_id='my-client',
        init_options={
            "checkLoginIframe": False
        },
    )
    if keycloak.authenticated:
        return dj.Connection(
            host=st.secrets["database_server"],
            user=keycloak.user_info['preferred_username'],
            password=keycloak.access_token
        )

conn = get_connection()

st.write(dj.list_schemas(connection=conn))


# def main():
#     st.subheader(f"Welcome {keycloak.user_info['preferred_username']}!")
#     conn = dj.Connection(host=st.secrets["database_server"], user=keycloak.user_info['preferred_username'], password=keycloak.access_token)
#     st.write(dj.list_schemas(connection=conn))
#     st.write(f"Here is your user information:")
#     st.write(asdict(keycloak))
#     if st.button("Disconnect"):
#         keycloak.authenticated = False


# st.title("Streamlit Keycloak example")
# keycloak = login(
#     url="https://keycloak.dev.datajoint.io",
#     realm="master",
#     client_id='my-client',
#     init_options={
#         "checkLoginIframe": False
#     },
# )

# if keycloak.authenticated:
#     main()