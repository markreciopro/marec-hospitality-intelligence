import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="MAREC Insights | Hospitality Analytics & Workforce Intelligence",
    page_icon="🏨",
    layout="wide"
)

st.title("🏨 MAREC Insights: Hospitality Analytics & Workforce Intelligence Platform")
st.markdown("""
*An interactive decision-support tool built from the Aurora Mirage Resort training curriculum, 
integrating PMS, LMS, HRIS, and Revenue Management workflows.*
""")

st.sidebar.header("Navigation")
app_mode = st.sidebar.selectbox(
    "Choose Module / Tool",
    [
        "1. Workforce & Staffing Calculator (Module 1)",
        "2. Revenue & Net RevPAR Audit (Module 2)",
        "3. Competitive & Scenario Indexing (Module 3)",
        "4. Profitability & GOPPAR Dashboard (Module 4 & 6)"
    ]
)

if app_mode == "1. Workforce & Staffing Calculator (Module 1)":
    st.header("Module 1: Demand-Driven Housekeeping & Labor Optimization")
    col1, col2 = st.columns(2)
    with col1:
        departures = st.number_input("Departures (Full Clean)", min_value=0, value=250)
        dep_time_mins = st.number_input("Minutes per Departure Clean", min_value=1.0, value=30.0)
        stayovers = st.number_input("Stay-overs (Light Clean)", min_value=0, value=120)
        stay_time_mins = st.number_input("Minutes per Stay-over Clean", min_value=1.0, value=15.0)
        shift_hours = st.number_input("Standard Shift Length (Hours)", min_value=1.0, value=8.0)
    with col2:
        total_payroll_hrs = st.number_input("Total Departmental Payroll Hours (LMS/HRIS)", min_value=0.0, value=1200.0)
        blended_hourly_rate = st.number_input("Blended Hourly Rate ($)", min_value=0.0, value=22.0)
        rooms_revenue = st.number_input("Total Rooms Revenue ($)", min_value=0.0, value=140000.0)
        occupied_rooms = st.number_input("Total Occupied Rooms (PMS)", min_value=0, value=353)

    dep_hours = (departures * dep_time_mins) / 60.0
    stay_hours = (stayovers * stay_time_mins) / 60.0
    total_cleaning_hrs = dep_hours + stay_hours
    attendants_required = total_cleaning_hrs / shift_hours
    total_payroll_cost = total_payroll_hrs * blended_hourly_rate
    lpr = (total_payroll_cost / rooms_revenue) * 100 if rooms_revenue > 0 else 0
    hpor = total_payroll_hrs / occupied_rooms if occupied_rooms > 0 else 0
    revpalh = rooms_revenue / total_payroll_hrs if total_payroll_hrs > 0 else 0

    st.divider()
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Cleaning Hours", f"{total_cleaning_hrs:.1f} hrs")
    m2.metric("Attendants Required", f"{round(attendants_required, 1)} staff")
    m3.metric("LPR (Labor %)", f"{lpr:.2f}%")
    m4.metric("HPOR", f"{hpor:.2f}")

elif app_mode == "2. Revenue & Net RevPAR Audit (Module 2)":
    st.header("Module 2: Channel Mix, Distribution Costs & Net RevPAR")
    col1, col2 = st.columns(2)
    with col1:
        available_rooms = st.number_input("Total Available Rooms", min_value=1, value=400)
        room_rev = st.number_input("Room Revenue ($)", min_value=0.0, value=150000.0)
        fb_rev = st.number_input("F&B Revenue ($)", min_value=0.0, value=40000.0)
        ancillary_rev = st.number_input("Ancillary Revenue ($)", min_value=0.0, value=10000.0)
        occupied_rooms_m2 = st.number_input("Occupied Rooms", min_value=1, value=350)
    with col2:
        total_dist_cost = st.number_input("Total Distribution Costs ($)", min_value=0.0, value=27000.0)

    adr = room_rev / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    revpar = room_rev / available_rooms
    trevpar = (room_rev + fb_rev + ancillary_rev) / available_rooms
    net_revpar = (room_rev - total_dist_cost) / available_rooms

    st.divider()
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("ADR", f"${adr:.2f}")
    m2.metric("RevPAR", f"${revpar:.2f}")
    m3.metric("TRevPAR", f"${trevpar:.2f}")
    m4.metric("Net RevPAR", f"${net_revpar:.2f}")

elif app_mode == "3. Competitive & Scenario Indexing (Module 3)":
    st.header("Module 3: Competitive Set Indexing (MPI, ARI, RGI)")
    col1, col2 = st.columns(2)
    with col1:
        prop_occ = st.number_input("Property Occupancy (%)", min_value=0.0, max_value=100.0, value=68.0)
        prop_adr = st.number_input("Property ADR ($)", min_value=0.0, value=428.57)
    with col2:
        comp_occ = st.number_input("Comp-Set Occupancy (%)", min_value=0.0, max_value=100.0, value=74.0)
        comp_adr = st.number_input("Comp-Set ADR ($)", min_value=0.0, value=412.00)

    mpi = (prop_occ / comp_occ) * 100 if comp_occ > 0 else 0
    ari = (prop_adr / comp_adr) * 100 if comp_adr > 0 else 0
    rgi = (mpi * ari) / 100

    st.divider()
    i1, i2, i3 = st.columns(3)
    i1.metric("MPI", f"{mpi:.1f}")
    i2.metric("ARI", f"{ari:.1f}")
    i3.metric("RGI", f"{rgi:.1f}")

elif app_mode == "4. Profitability & GOPPAR Dashboard (Module 4 & 6)":
    st.header("Module 4 & 6: GOPPAR & Cross-Property Scorecard")
    gop_total = st.number_input("Gross Operating Profit (GOP) ($)", min_value=0.0, value=177600.0)
    avail_rooms_p4 = st.number_input("Total Available Rooms", min_value=1, value=1200)
    goppar = gop_total / avail_rooms_p4 if avail_rooms_p4 > 0 else 0

    st.divider()
    st.metric("GOPPAR", f"${goppar:.2f}")
