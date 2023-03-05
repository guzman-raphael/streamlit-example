# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app?database_host=example.com

import streamlit as st
import streamlit_keycloak
import datajoint as dj


def get_connection():
    keycloak = streamlit_keycloak.login(
        url="https://keycloak.dev.datajoint.io",
        realm="master",
        client_id='my-client',
    )
    host = st.experimental_get_query_params().get("database_host", [None])[0]
    if keycloak.authenticated and host:
        return dj.Connection(
            host=host,
            user=keycloak.user_info['preferred_username'],
            password=keycloak.access_token
        )

conn = get_connection()
if conn:
    st.write(f"{conn.conn_info['user']}'s schemas:")
    st.write(dj.list_schemas(connection=conn))
else:
    st.write("Not ready")
