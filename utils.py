import json
import streamlit as st
import streamlit_keycloak
import datajoint as dj


def get_session(**kwargs):
    if (host:=st.experimental_get_query_params().get("database_host")) and (
        keycloak:=streamlit_keycloak.login(**kwargs)
    ).authenticated:
        return {
            'connection': dj.Connection(
                host=host[0],
                user=keycloak.user_info["preferred_username"],
                password=keycloak.access_token,
            ),
            'context': json.loads(
                st.experimental_get_query_params().get("context", ["{}"])[0]
            ),
        }
    else:
        st.warning("Waiting for credentials...")
        st.stop()
