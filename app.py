import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION & EXECUTIVE THEME ---
st.set_page_config(
    page_title="MAREC Insights | Hospitality Intelligence",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    /* Global App Styling */
    .main {
        background-color: #f1f5f9;
        font-family: 'Inter', sans-serif;
    }
    
    /* Executive Header Banner */
    .executive-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -4px rgba(0, 0, 0, 0.1);
        border-left: 6px solid #3b82f6;
    }
    .executive-header h1 {
        color: #ffffff;
        font-size: 2.4rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        letter-spacing: -0.025em;
    }
    .executive-header p {
        color: #94a3b8;
        font-size: 1.15rem;
        font-weight: 400;
    }

    /* Card Containers */
    div.stNumberInput, div.stSelectbox {
        background: #ffffff;
        padding: 0.75rem;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 0.5rem;
    }
    
    /* Metric Card Styling override */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 1rem 1.25rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    section[data-testid="stSidebar"] .stMarkdown {
        color: #e2e8f0;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.markdown("### **MAREC Insights**")
st.sidebar.caption("Hospitality Workforce & Revenue Intelligence")
st.sidebar.markdown("---")

module_selection = st.sidebar.selectbox(
    "Choose Module / Tool",
    [
        "1. Workforce & Staffing Calculator (Module 1)",
        "2. Revenue & Net RevPAR Audit (Module 2)",
        "3. Competitive & Scenario Indexing (Module 3)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Executive Advisory:** Use these modules to benchmark labor efficiency, channel acquisition costs, and market share indices against luxury resort standards.")

# ==========================================
# MODULE 1: WORKFORCE & LABOR OPTIMIZATION
# ==========================================
if "1. Workforce" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 1: Demand-Driven Housekeeping & Labor Optimization</h1>
            <p>Calculate precise staffing requirements, HPOR, and labor cost ratios based on real-time property management signals.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### **Operational Demand Inputs**")
        departures = st.number_input("Departures (Full Clean)", min_value=0, value=250, step=10)
        dep_minutes = st.number_input("Minutes per Departure Clean", min_value=0.0, value=30.0, step=2.5)
        stayovers = st.number_input("Stay-overs (Light Clean)", min_value=0, value=120, step=10)
        stay_minutes = st.number_input("Minutes per Stay-over Clean", min_value=0.0, value=15.0, step=1.0)
        shift_length = st.number_input("Standard Shift Length (Hours)", min_value=1.0, value=8.0, step=0.5)

    with col2:
        st.markdown("#### **Financial & Payroll Inputs**")
        payroll_hours = st.number_input("Total Departmental Payroll Hours (LMS/HRIS)", min_value=0.0, value=1200.0, step=10.0)
        blended_rate = st.number_input("Blended Hourly Rate ($)", min_value=0.0, value=22.0, step=0.5)
        total_rooms_rev = st.number_input("Total Rooms Revenue ($)", min_value=0.0, value=140000.0, step=1000.0)
        occupied_rooms = st.number_input("Total Occupied Rooms (PMS)", min_value=0, value=353, step=5)

    # Calculations
    total_cleaning_minutes = (departures * dep_minutes) + (stayovers * stay_minutes)
    total_cleaning_hours = total_cleaning_minutes / 60.0
    required_fte = total_cleaning_hours / shift_length if shift_length > 0 else 0
    hpor = total_cleaning_hours / occupied_rooms if occupied_rooms > 0 else 0
    total_payroll_cost = payroll_hours * blended_rate
    lpr = (total_payroll_cost / total_rooms_rev) * 100 if total_rooms_rev > 0 else 0
    revpalh = total_rooms_rev / payroll_hours if payroll_hours > 0 else 0

    st.markdown("---")
    st.markdown("### **Executive Performance Dashboard**")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Required Staffing (FTE)", f"{required_fte:.1f}", delta="Optimized Shift Plan")
    m2.metric("HPOR (Hours / Occ. Room)", f"{hpor:.2f} hrs", delta="-0.15 vs Benchmark", delta_color="inverse")
    m3.metric("LPR (Labor Cost %)", f"{lpr:.1f}%", delta="Target < 28%")
    m4.metric("REVPALH", f"${revpalh:.2f}", delta="Hourly Rev Productivity")

# ==========================================
# MODULE 2: REVENUE & NET REVPAR AUDIT
# ==========================================
elif "2. Revenue" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 2: Channel Mix, Distribution Costs & Net RevPAR</h1>
            <p>Evaluate true bottom-line profitability by factoring in OTA commissions, GDS fees, and acquisition costs.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### **Property Revenue Metrics**")
        available_rooms = st.number_input("Total Available Rooms", min_value=1, value=400)
        occupied_rooms_m2 = st.number_input("Occupied Rooms", min_value=0, value=350)
        room_revenue = st.number_input("Gross Room Revenue ($)", min_value=0.0, value=150000.0)
        fnb_revenue = st.number_input("F&B Revenue ($)", min_value=0.0, value=40000.0)
        ancillary_revenue = st.number_input("Ancillary Revenue ($)", min_value=0.0, value=10000.0)

    with col2:
        st.markdown("#### **Distribution & Acquisition Costs**")
        total_dist_costs = st.number_input("Total Distribution Costs ($)", min_value=0.0, value=27000.0)
        variable_costs = st.number_input("Variable Operating Costs ($)", min_value=0.0, value=45000.0)

    # Calculations
    occupancy = (occupied_rooms_m2 / available_rooms) * 100 if available_rooms > 0 else 0
    adr = room_revenue / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    revpar = room_revenue / available_rooms if available_rooms > 0 else 0
    net_room_rev = room_revenue - total_dist_costs
    net_revpar = net_room_rev / available_rooms if available_rooms > 0 else 0
    net_adr = net_room_rev / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0

    st.markdown("---")
    st.markdown("### **Executive KPI Performance**")

    r1, r2, r3, r4 = st.columns(4)
    r1.metric("Occupancy Rate", f"{occupancy:.1f}%")
    r2.metric("ADR (Average Daily Rate)", f"${adr:.2f}")
    r3.metric("RevPAR", f"${revpar:.2f}")
    r4.metric("Net RevPAR", f"${net_revpar:.2f}", delta=f"Net ADR: ${net_adr:.2f}")

# ==========================================
# MODULE 3: COMPETITIVE & SCENARIO INDEXING
# ==========================================
elif "3. Competitive" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 3: Competitive Set Indexing (MPI, ARI, RGI)</h1>
            <p>Measure your property's market penetration, average rate performance, and revenue generation against competitive sets.</p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.markdown("#### **Your Property Performance**")
        hotel_occ = st.number_input("Your Property Occupancy (%)", 0.0, 100.0, 75.0)
        hotel_adr = st.number_input("Your Property ADR ($)", 0.0, 1000.0, 220.0)
    with c2:
        st.markdown("#### **Comp Set Average**")
        comp_occ = st.number_input("Comp Set Average Occupancy (%)", 0.0, 100.0, 70.0)
        comp_adr = st.number_input("Comp Set Average ADR ($)", 0.0, 1000.0, 200.0)
    with c3:
        st.markdown("#### **RevPAR Benchmarking**")
        hotel_revpar = hotel_occ * hotel_adr / 100
        comp_revpar = comp_occ * comp_adr / 100
        st.metric("Your RevPAR", f"${hotel_revpar:.2f}")
        st.metric("Comp Set RevPAR", f"${comp_revpar:.2f}")

    # Index Calculations
    mpi = (hotel_occ / comp_occ) * 100 if comp_occ > 0 else 0
    ari = (hotel_adr / comp_adr) * 100 if comp_adr > 0 else 0
    rgi = (hotel_revpar / comp_revpar) * 100 if comp_revpar > 0 else 0

    st.markdown("---")
    st.markdown("### **Market Penetration Indices**")

    i1, i2, i3 = st.columns(3)
    i1.metric("MPI (Occupancy Index)", f"{mpi:.1f}", delta="Fair Share = 100")
    i2.metric("ARI (Average Rate Index)", f"{ari:.1f}", delta="Fair Share = 100")
    i3.metric("RGI (RevPAR Index)", f"{rgi:.1f}", delta="Fair Share = 100")