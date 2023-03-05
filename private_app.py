# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app/

import streamlit as st
import streamlit_keycloak
import datajoint as dj


def get_connection():
    keycloak = streamlit_keycloak.login(
        url="https://keycloak.dev.datajoint.io",
        realm="master",
        client_id='my-client',
    )
    if keycloak.authenticated:
        return dj.Connection(
            host=st.secrets["database_server"],
            user=keycloak.user_info['preferred_username'],
            password=keycloak.access_token
        )

conn = get_connection()

st.title(f"{conn.conn_info['user']}'s schemas:")
st.write(dj.list_schemas(connection=conn))
