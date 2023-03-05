# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app?database_host=example.com

import streamlit as st
import streamlit_keycloak
import datajoint as dj


def get_connection(**kwargs):
    if (host:=st.experimental_get_query_params().get("database_host")) and (
        keycloak:=streamlit_keycloak.login(**kwargs)
    ).authenticated:
        return dj.Connection(
            host=host[0],
            user=keycloak.user_info["preferred_username"],
            password=keycloak.access_token,
        )


if (conn:=get_connection(
    url="https://keycloak.dev.datajoint.io", realm="master", client_id="my-client"
)):
    st.write(f"{conn.conn_info['user']}'s schemas:")
    st.write(dj.list_schemas(connection=conn))
else:
    st.write("Incomplete credentials")