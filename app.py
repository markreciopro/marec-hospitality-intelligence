import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION & EXECUTIVE THEME ---
st.set_page_config(
    page_title="MAREC Insights | Hospitality Intelligence & Workforce Analytics",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f1f5f9;
        font-family: 'Inter', sans-serif;
    }
    .executive-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        border-left: 6px solid #3b82f6;
    }
    .executive-header h1 {
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .executive-header p {
        color: #94a3b8;
        font-size: 1.1rem;
    }
    .instruction-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        border-left: 4px solid #3b82f6;
        margin-bottom: 1.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .action-card {
        background-color: #ffffff;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #cbd5e1;
        border-left: 4px solid #0f172a;
        margin-top: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 1rem 1.25rem;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
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
        "2. Channel Mix & Net RevPAR Audit (Module 2)",
        "3. Competitive Indexing & Scenario Modeling (Module 3)",
        "4. AI Governance & GOPPAR Analytics (Module 4)",
        "5. Demand Resilience, DRI & ACR (Module 5)",
        "6. Portfolio Scorecard & Boardroom Strategy (Module 6)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Executive Guidance:** Built on the Aurora Mirage manuscript curriculum (CRME-aligned operational and commercial intelligence)[cite: 4, 5].")

# ==========================================
# MODULE 1: WORKFORCE & LABOR OPTIMIZATION
# ==========================================
if "1. Workforce" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 1: Demand-Driven Housekeeping & Labor Optimization</h1>
            <p>Calculate precise staffing requirements, HPOR, and labor cost ratios based on real-time property management signals[cite: 8].</p>
        </div>
    """, unsafe_allow_html=True)

    # --- TOP SETUP INSTRUCTION CARD ---
    st.markdown("""
        <div class="instruction-card">
            <h4 style="margin-top:0; color:#0f172a;">📋 Step 1: Input Operational & Payroll Parameters</h4>
            <p style="color:#334155; margin-bottom:0.75rem;">
                Adjust the PMS operational inputs and HRIS payroll figures below to simulate your property's housekeeping department performance. Remember that departures drive labor workload, not occupancy alone[cite: 9].
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### **Operational Demand Inputs (PMS Signal)**")
        departures = st.number_input("Departures / Full Cleans (30 mins std)", min_value=0, value=280, step=10)
        dep_minutes = st.number_input("Minutes per Departure Clean", min_value=0.0, value=30.0, step=2.5)
        stayovers = st.number_input("Stay-overs / Light Cleans (15 mins std)", min_value=0, value=120, step=10)
        stay_minutes = st.number_input("Minutes per Stay-over Clean", min_value=0.0, value=15.0, step=1.0)
        occupied_rooms = st.number_input("Total Occupied Rooms (PMS)", min_value=1, value=361, step=5)

    with col2:
        st.markdown("#### **Financial & Payroll Inputs (HRIS/PMS Signal)**")
        payroll_hours = st.number_input("Total Departmental Payroll Hours (LMS/HRIS)", min_value=0.0, value=1300.0, step=10.0)
        blended_rate = st.number_input("Blended Hourly Rate ($)", min_value=0.0, value=22.0, step=0.5)
        total_rooms_rev = st.number_input("Total Rooms Revenue ($)", min_value=0.0, value=140000.0, step=1000.0)

    # Core Calculations based on Manuscript Formulas
    total_cleaning_minutes = (departures * dep_minutes) + (stayovers * stay_minutes)
    total_cleaning_hours = total_cleaning_minutes / 60.0
    
    # LPR = (Total Payroll / Total Revenue) * 100[cite: 8]
    total_payroll_cost = payroll_hours * blended_rate
    lpr = (total_payroll_cost / total_rooms_rev) * 100 if total_rooms_rev > 0 else 0
    
    # HPOR = Housekeeping Hours / Occupied Rooms[cite: 8]
    hpor = payroll_hours / occupied_rooms if occupied_rooms > 0 else 0
    
    # REVPALH = Departmental Revenue / Total Labor Hours[cite: 8]
    revpalh = total_rooms_rev / payroll_hours if payroll_hours > 0 else 0

    st.markdown("---")
    st.markdown("### **Executive Workforce Performance Dashboard**")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Calculated Clean Hours", f"{total_cleaning_hours:.1f} hrs", delta=f"Actual Logged: {payroll_hours} hrs")
    m2.metric("HPOR (Hours / Occ. Room)", f"{hpor:.2f} hrs", delta="Benchmark Target: 2.50", delta_color="inverse")
    m3.metric("LPR (Labor Cost %)", f"{lpr:.1f}%", delta="Target Ceiling: 16.0%")
    m4.metric("REVPALH", f"${revpalh:.2f}", delta="Benchmark Target: $130.00")

    # --- DETAILED EXPLANATION & ACTION PROTOCOL FOR THE DASHBOARD ---
    st.markdown(f"""
        <div class="action-card">
            <h4 style="margin-top:0; color:#0f172a;">📊 How to Interpret & Act on This Dashboard</h4>
            <p style="color:#334155; margin-bottom:0.75rem;">
                Review your metric outputs above against the operational standards established at Aurora Mirage Resort:
            </p>
            <ul style="color:#334155; margin-bottom:1rem;">
                <li><b>Calculated Clean Hours ({total_cleaning_hours:.1f} hrs) vs. Logged Payroll Hours ({payroll_hours} hrs):</b> 
                    The difference represents your department's <i>operational friction</i> (supervision, setup, transit, and potential overstaffing or overtime waste). If logged hours significantly exceed calculated hours, adjust shift schedules to align with actual departure curves[cite: 10, 11].
                </li>
                <li><b>HPOR ({hpor:.2f} hrs/room):</b> 
                    Measures total housekeeping payroll hours per occupied room. The luxury benchmark target is <b>2.50 hours</b>[cite: 11]. An HPOR above 2.50 signals inefficient scheduling or excessive non-cleaning hours.
                </li>
                <li><b>LPR ({lpr:.1f}%):</b> 
                    Shows what percentage of room revenue goes straight to housekeeping payroll. The financial ceiling target is <b>16.0%</b>[cite: 11]. If your LPR is higher, payroll costs are eroding your operating margins.
                </li>
                <li><b>REVPALH (${revpalh:.2f}):</b> 
                    Measures rooms revenue generated per available labor hour. The benchmark target is <b>$130.00</b>[cite: 11]. Lower productivity per hour indicates either soft room pricing or excess labor overhead.
                </li>
            </ul>
            <p style="color:#0f172a; font-weight:600; margin-bottom:0;">
                🎯 <b>Executive Decision Rule:</b> Do not schedule based on static occupancy or last month's calendar. Use departure forecasts and time standards to publish dynamic weekly rosters that eliminate unbudgeted overtime before compression hits[cite: 8, 10, 11].
            </p>
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# MODULE 2: CHANNEL MIX & NET REVPAR AUDIT
# ==========================================
elif "2. Channel" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 2: Channel Mix, Distribution Costs & Net RevPAR</h1>
            <p>Isolate true bottom-line retention by factoring in OTA and distribution commissions[cite: 17].</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### **Property Revenue Metrics**")
        available_rooms = st.number_input("Total Available Rooms", min_value=1, value=400)
        occupied_rooms_m2 = st.number_input("Rooms Sold / Occupied Rooms", min_value=0, value=350)
        room_revenue = st.number_input("Gross Room Revenue ($)", min_value=0.0, value=150000.0, step=1000.0)
        fnb_revenue = st.number_input("F&B Revenue ($)", min_value=0.0, value=40000.0, step=1000.0)
        ancillary_revenue = st.number_input("Ancillary Revenue ($)", min_value=0.0, value=10000.0, step=500.0)

    with col2:
        st.markdown("#### **Distribution & Channel Costs**")
        total_dist_costs = st.number_input("Total Distribution / Commission Costs ($)", min_value=0.0, value=27000.0, step=500.0)

    # Core Calculations based on Manuscript Formulas
    adr = room_revenue / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    revpar = room_revenue / available_rooms if available_rooms > 0 else 0
    
    # TRevPAR = (Room + F&B + Ancillary) / Available Rooms[cite: 17]
    trevpar = (room_revenue + fnb_revenue + ancillary_revenue) / available_rooms if available_rooms > 0 else 0
    
    # Net RevPAR = (Room Rev - Distribution Costs) / Available Rooms[cite: 17]
    net_room_rev = room_revenue - total_dist_costs
    net_revpar = net_room_rev / available_rooms if available_rooms > 0 else 0
    net_adr = net_room_rev / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    blended_dist_pct = (total_dist_costs / room_revenue) * 100 if room_revenue > 0 else 0

    st.markdown("---")
    st.markdown("### **Executive Commercial KPI Audit**")

    r1, r2, r3, r4, r5 = st.columns(5)
    r1.metric("ADR", f"${adr:.2f}")
    r2.metric("RevPAR", f"${revpar:.2f}")
    r3.metric("TRevPAR", f"${trevpar:.2f}")
    r4.metric("Net RevPAR", f"${net_revpar:.2f}", delta=f"Net ADR: ${net_adr:.2f}")
    r5.metric("Blended Dist. Cost", f"{blended_dist_pct:.1f}%")

# ==========================================
# MODULE 3: COMPETITIVE INDEXING & SCENARIO MODELING
# ==========================================
elif "3. Competitive" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 3: Competitive Set Indexing & Scenario Modeling</h1>
            <p>Calculate MPI, ARI, RGI, Price Elasticity of Demand (PED), and probability-weighted forecasts[cite: 26, 33].</p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("#### **Market Share & Index Inputs (MPI, ARI, RGI)**")
        hotel_occ = st.number_input("Your Property Occupancy (%)", 0.0, 100.0, 68.0)
        comp_occ = st.number_input("Comp-Set Average Occupancy (%)", 0.0, 100.0, 74.0)
        hotel_adr = st.number_input("Your Property ADR ($)", 0.0, 1000.0, 428.57)
        comp_adr = st.number_input("Comp-Set Average ADR ($)", 0.0, 1000.0, 412.00)

    with c2:
        st.markdown("#### **Probability-Weighted Scenario Model**")
        prob_best = st.slider("Best Case Probability (%)", 0, 100, 25)
        gop_best = st.number_input("Best Case GOP %", 0.0, 100.0, 36.5)
        prob_base = st.slider("Base Case Probability (%)", 0, 100, 55)
        gop_base = st.number_input("Base Case GOP %", 0.0, 100.0, 32.0)
        prob_down = 100 - (prob_best + prob_base)
        st.text(f"Downside Case Probability (Auto-balanced): {prob_down}%")
        gop_down = st.number_input("Downside Case GOP %", 0.0, 100.0, 26.0)

    # Core Calculations based on Manuscript Formulas
    mpi = (hotel_occ / comp_occ) * 100 if comp_occ > 0 else 0
    ari = (hotel_adr / comp_adr) * 100 if comp_adr > 0 else 0
    
    hotel_revpar = (hotel_occ / 100.0) * hotel_adr
    comp_revpar = (comp_occ / 100.0) * comp_adr
    
    # RGI = (Property RevPAR / Comp-Set RevPAR) * 100 = (MPI * ARI) / 100[cite: 26]
    rgi = (hotel_revpar / comp_revpar) * 100 if comp_revpar > 0 else (mpi * ari) / 100

    weighted_gop = ((prob_best / 100.0) * gop_best) + ((prob_base / 100.0) * gop_base) + ((max(0, prob_down) / 100.0) * gop_down)

    st.markdown("---")
    st.markdown("### **Competitive Penetration Indices & Weighted Forecast**")

    i1, i2, i3, i4 = st.columns(4)
    i1.metric("MPI (Occupancy Index)", f"{mpi:.1f}", delta="Fair Share = 100")
    i2.metric("ARI (Rate Index)", f"{ari:.1f}", delta="Fair Share = 100")
    i3.metric("RGI (RevPAR Index)", f"{rgi:.1f}", delta="Fair Share = 100")
    i4.metric("Weighted Expected GOP %", f"{weighted_gop:.2f}%", delta="Scenario-Adjusted")

# ==========================================
# MODULE 4: AI GOVERNANCE & GOPPAR ANALYTICS
# ==========================================
elif "4. AI Governance" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 4: AI Governance, Variance Limits & GOPPAR Analytics</h1>
            <p>Monitor forecast accuracy (MAPE), evaluate profit-per-room (GOPPAR), and enforce human-in-the-loop guardrails[cite: 40].</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Profitability & GOPPAR Inputs**")
        gross_op_profit = st.number_input("Gross Operating Profit (GOP) ($)", min_value=0.0, value=59200.0, step=1000.0)
        total_avail_rooms_m4 = st.number_input("Total Available Rooms (Monthly)", min_value=1, value=400)
        
    with col2:
        st.markdown("#### **Algorithmic Variance & MAPE Inputs**")
        actual_demand = st.number_input("Actual Occupied Rooms", min_value=1, value=361)
        forecast_demand = st.number_input("Model Forecasted Rooms", min_value=1, value=350)
        variance_limit_pct = st.number_input("Configured Variance Limit (%)", min_value=0.0, value=8.0, step=0.5)

    # Core Calculations based on Manuscript Formulas
    # GOPPAR = Gross Operating Profit / Total Available Rooms[cite: 40]
    goppar = gross_op_profit / total_avail_rooms_m4 if total_avail_rooms_m4 > 0 else 0
    
    abs_error_pct = (abs(actual_demand - forecast_demand) / actual_demand) * 100 if actual_demand > 0 else 0
    proposed_move_pct = abs_error_pct * 1.5

    st.markdown("---")
    st.markdown("### **Governance & Profitability Dashboard**")

    g1, g2, g3, g4 = st.columns(4)
    g1.metric("GOPPAR", f"${goppar:.2f}", delta="Bottom-Line Yield per Room")
    g2.metric("Forecast Error (Abs %)", f"{abs_error_pct:.2f}%", delta="Healthy target < 3-5%")
    g3.metric("Proposed Algorithmic Move", f"{proposed_move_pct:.1f}%", delta=f"Limit: {variance_limit_pct}%")
    g4.metric("Governance Action Status", "ESCALATE" if proposed_move_pct > variance_limit_pct else "Auto-execute", delta_color="inverse" if proposed_move_pct > variance_limit_pct else "normal")

# ==========================================
# MODULE 5: DEMAND RESILIENCE, DRI & ACR
# ==========================================
elif "5. Demand" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 5: Demand Resilience, DRI & ACR</h1>
            <p>Measure demand recapture without discounting using the Demand Redistribution Index (DRI) and Ancillary Capture Rate (ACR)[cite: 46].</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Demand Redistribution Inputs**")
        rooms_lost = st.number_input("Room-Nights Lost (Exposed Segment)", min_value=1, value=340)
        rooms_recaptured = st.number_input("Room-Nights Recaptured (Alternate Segment)", min_value=0, value=207)

    with col2:
        st.markdown("#### **Ancillary Capture Rate Inputs**")
        fnb_spa_rev = st.number_input("F&B + Spa + Ancillary Revenue ($)", min_value=0.0, value=460000.0, step=5000.0)
        total_prop_rev = st.number_input("Total Property Revenue ($)", min_value=0.0, value=2150000.0, step=10000.0)

    # Core Calculations based on Manuscript Formulas
    # DRI = (Room-Nights Recaptured Elsewhere / Room-Nights Lost) * 100[cite: 46]
    dri = (rooms_recaptured / rooms_lost) * 100 if rooms_lost > 0 else 0
    
    # ACR = ((F&B + Spa + Ancillary Rev) / Total Property Rev) * 100[cite: 46]
    acr = (fnb_spa_rev / total_prop_rev) * 100 if total_prop_rev > 0 else 0

    st.markdown("---")
    st.markdown("### **Resilience & Wallet Share Dashboard**")

    d1, d2 = st.columns(2)
    d1.metric("DRI (Demand Redistribution Index)", f"{dri:.1f}%", delta="Recapture Performance vs Target > 60%")
    d2.metric("ACR (Ancillary Capture Rate)", f"{acr:.1f}%", delta="Guest Wallet Share Cushion")

# ==========================================
# MODULE 6: PORTFOLIO SCORECARD & BOARDROOM STRATEGY
# ==========================================
elif "6. Portfolio" in module_selection:
    st.markdown("""
        <div class="executive-header">
            <h1>Module 6: Portfolio Scorecard & Boardroom Strategy</h1>
            <p>Audit multi-property performance using the GOPPAR gap benchmark and evaluate capital projects via ROI and payback[cite: 53, 54].</p>
        </div>
    """, unsafe_allow_html=True)

    portfolio_data = pd.DataFrame({
        "Property": ["Aurora Mirage (Las Vegas)", "Property B (Reno)", "Property C (Phoenix)", "Property D (San Diego)"],
        "Actual GOPPAR ($)": [148.0, 121.0, 133.0, 156.0],
        "Achievable GOPPAR ($)": [150.0, 138.0, 135.0, 158.0]
    })
    
    portfolio_data["Gap ($)"] = portfolio_data["Actual GOPPAR ($)"] - portfolio_data["Achievable GOPPAR ($)"]

    st.markdown("#### **Cross-Property Portfolio GOPPAR Gap Analysis**")
    st.dataframe(portfolio_data, use_container_width=True)

    fig = px.bar(
        portfolio_data.melt(id_vars="Property", value_vars=["Actual GOPPAR ($)", "Achievable GOPPAR ($)"]),
        x="Property",
        y="value",
        color="variable",
        barmode="group",
        title="Actual vs. Achievable GOPPAR by Property",
        labels={"value": "GOPPAR ($)", "variable": "Metric"}
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("#### **Capital Project ROI & Payback Ranking**")
    capex_data = pd.DataFrame({
        "Project": ["PMS Upgrade", "Direct-Booking Engine", "Solar + Efficiency", "Spa Expansion", "New Tower Wing"],
        "3-Yr ROI (%)": [34, 28, 19, 14, 9],
        "Payback Period (Years)": [0.8, 1.4, 3.2, 4.5, 7.8],
        "Scope": ["All Properties", "All Properties", "Reno & Phoenix", "Aurora Mirage", "San Diego"]
    })
    st.dataframe(capex_data, use_container_width=True)
