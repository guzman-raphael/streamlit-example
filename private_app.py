# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app?database_host=example.com&context={"workflow_template":"template1","organization":"org1","workflow":"wf1"}
# http://localhost:8501?database_host=example.com&context={"workflow_template":"template1","organization":"org1","workflow":"wf1"}

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

session = get_session(
    url="https://keycloak.dev.datajoint.io", realm="master", client_id="my-client"
)

st.write("App context:")
st.write(session['context'])

st.write(f"{session['connection'].conn_info['user']}'s schemas:")
st.write(dj.list_schemas(connection=session['connection']))

schema_name = "guzman-raphael_fizzle-proj_ephys"
ephys = dj.VirtualModule(schema_name, schema_name, connection=session['connection'])
st.image(dj.Di(ephys).make_png(), caption=f"{schema_name}'s diagram")