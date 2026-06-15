import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import time

from telemetry import get_sensor
from simulator import generate_data
from logger import save


st.set_page_config(
    page_title="Rocket Telemetry Portal",
    layout="wide"
)


st.markdown(
"""
<style>

.stApp{
background:
linear-gradient(
180deg,
#72B7FF,
#F5FAFF
);
}

.block-container{
max-width:1450px;
padding-top:12px;
}

[data-testid="stSidebar"]{
background:white;
}

</style>
""",
unsafe_allow_html=True
)
# -----------------
# SESSION
# -----------------

if "history" not in st.session_state:

    st.session_state.history=[]



# -----------------
# SIDEBAR
# -----------------

with st.sidebar:

    st.title(
        "🚀 Data Source"
    )

    mode=st.radio(

        "",

        [

            "Sensor Data",

            "Virtual Data"

        ],

        index=0
    )
    # -----------------
# DATA
# -----------------

data=None


if mode=="Sensor Data":

    try:

        data=get_sensor()

    except:

        data=None


    if data is None:

        st.title(
            "Rocket Telemetry Portal"
        )

        st.error(
"""
NO SENSOR DETECTED

Connect ESP8266
and restart.
"""
        )

        st.stop()


else:

    data=generate_data()



save(
    data
)



st.session_state.history.append(
    data
)



if len(
    st.session_state.history
)>20:

    st.session_state.history=(
        st.session_state.history[-20:]
    )



df=pd.DataFrame(
    st.session_state.history
)



temp=data[
    "temperature"
]


acc=data[
    "acceleration"
]


alt=data[
    "altitude"
]



healthy=(

temp<45

and

acc<12

)
# -----------------
# HEADER
# -----------------

st.title(
    "Rocket Telemetry Portal"
)

st.caption(
    "Real-Time Flight Monitoring"
)



# -----------------
# LAYOUT
# -----------------

left,right=st.columns(
    [3,1]
)
# -----------------
# LEFT
# GRAPH
# -----------------

with left:


    st.subheader(
        mode
    )


    fig=go.Figure()


    fig.add_trace(

        go.Scatter(

            x=list(
                range(
                    len(df)
                )
            ),

            y=df[
                "altitude"
            ],

            mode=
            "lines+markers",

            fill=
            "tozeroy"

        )

    )


    fig.update_layout(

        height=450,

        paper_bgcolor=
        "white",

        plot_bgcolor=
        "white",

        margin=dict(

            l=10,

            r=10,

            t=20,

            b=10

        )

    )


    st.plotly_chart(

        fig,

        use_container_width=True
    )
    # -----------------
# RIGHT
# STATUS
# -----------------

with right:


    st.subheader(
        "Status"
    )


    st.metric(

        "Source",

        "🟢 SENSOR"

        if

        mode=="Sensor Data"

        else

        "🟡 VIRTUAL"

    )



    st.metric(

        "Health",

        "🟢 HEALTHY"

        if healthy

        else

        "🔴 WARNING"

    )



    st.metric(

        "Temperature",

        f"{temp:.1f} °C"

    )



    st.metric(

        "Acceleration",

        f"{acc:.1f}"

    )



    st.metric(

        "Altitude",

        f"{alt:.1f}"

    )



    if acc<5:

        msg="""
Stable movement.

System operating
normally.
"""


    elif acc<10:

        msg="""
Moderate motion.

Vehicle responding.
"""


    else:

        msg="""
High movement.

Monitor stability.
"""


    st.info(
        msg
    )



# -----------------
# REFRESH
# -----------------

time.sleep(
    0.5
)

st.rerun()