# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app?database_host=example.com&context={"workflow_template":"template1","organization":"org1","workflow":"wf1"}
# http://localhost:8501?database_host=example.com&context={"workflow_template":"template1","organization":"org1","workflow":"wf1"}

# https://guzman-raphael-streamlit-example-private-app-qhzxwd.streamlit.app?database_host=example.com&context={"workflow_template":"template1","organization":"org1","workflow":"wf1"}
# http://localhost:8501?database_host=example.com&context={"workflow_template":"template1","organization":"org1","workflow":"wf1"}

import streamlit as st
import datajoint as dj
import utils

session = utils.get_session(
    url="https://keycloak.dev.datajoint.io", realm="master", client_id="my-client"
)

st.write("App context:")
st.write(session['context'])

st.write(f"{session['connection'].conn_info['user']}'s schemas:")
st.write(dj.list_schemas(connection=session['connection']))

schema_name = "guzman-raphael_fizzle-proj_ephys"
ephys = dj.VirtualModule(schema_name, schema_name, connection=session['connection'])
st.image(dj.Di(ephys).make_png(), caption=f"{schema_name}'s diagram")