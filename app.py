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
    st.markdown("# Module 1: Demand-Driven Housekeeping & Labor Optimization")
    st.markdown("Calculate precise staffing requirements, HPOR, and labor cost ratios based on real-time property management signals[cite: 8].")
    st.markdown("---")

    st.info("📋 **Step 1: Input Operational & Payroll Parameters**\n\nAdjust the PMS operational inputs and HRIS payroll figures below to simulate your property's housekeeping department performance. Remember that departures drive labor workload, not occupancy alone[cite: 9].")

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
    
    total_payroll_cost = payroll_hours * blended_rate
    lpr = (total_payroll_cost / total_rooms_rev) * 100 if total_rooms_rev > 0 else 0
    hpor = payroll_hours / occupied_rooms if occupied_rooms > 0 else 0
    revpalh = total_rooms_rev / payroll_hours if payroll_hours > 0 else 0

    hour_gap = payroll_hours - total_cleaning_hours

    st.markdown("---")
    st.markdown("### **Executive Workforce Performance Dashboard**")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Calculated Clean Hours", f"{total_cleaning_hours:.1f} hrs", delta=f"Actual Logged: {payroll_hours} hrs")
    m2.metric("HPOR (Hours / Occ. Room)", f"{hpor:.2f} hrs", delta="Benchmark Target: 2.50", delta_color="inverse")
    m3.metric("LPR (Labor Cost %)", f"{lpr:.1f}%", delta="Target Ceiling: 16.0%")
    m4.metric("REVPALH", f"${revpalh:.2f}", delta="Benchmark Target: $130.00")

    # --- DYNAMIC ACTION DIRECTIVES & INTERPRETATION PROTOCOL ---
    st.markdown("### **📊 Executive Dashboard Interpretation & Action Protocol**")
    st.markdown(f"Reviewing your current inputs: **{departures} departures**, **{stayovers} stay-overs**, and **{payroll_hours} payroll hours logged**.")

    if hour_gap > 200:
        st.error(f"🚨 **Critical Overstaffing / Operational Friction Alert:** You have a massive variance of **{hour_gap:.1f} hours** between calculated net cleaning time ({total_cleaning_hours:.1f} hrs) and actual logged payroll ({payroll_hours} hrs).")
        st.markdown("""
            **Required User Actions:**
            * **Action 1 (Audit Schedules):** Investigate where department hours are pooling (excessive supervisory shifts, unoptimized laundry or houseman staffing, or bloated pre-shift hours).
            * **Action 2 (Realign with Departures):** Transition immediately from static headcounts to demand-driven scheduling. Align shift start times with the departure curve rather than flat occupancy[cite: 10].
            * **Action 3 (Cross-Departmental Flex):** If compression is low, utilize cross-departmental labor sharing or reduce overtime approvals to bring logged hours closer to the engineered standard.
        """)
    elif hour_gap > 0:
        st.warning(f"⚠️ **Moderate Variance Warning:** Logged payroll hours exceed calculated clean time by **{hour_gap:.1f} hours**. This friction accounts for setup, transit, and breaks, but should be tightly managed.")
        st.markdown("""
            **Required User Actions:**
            * **Action 1:** Review room attendant productivity standards (30 mins per departure, 15 mins per stay-over) against actual floor pacing[cite: 11].
            * **Action 2:** Ensure scheduling matches the 7-day weekly labor timeline to prevent midweek overtime spikes[cite: 9, 10].
        """)
    else:
        st.success(f"✅ **Tight Labor Alignment:** Calculated clean hours ({total_cleaning_hours:.1f} hrs) closely match or exceed logged payroll hours ({payroll_hours} hrs).")
        st.markdown("""
            **Required User Actions:**
            * **Action 1:** Ensure that tight staffing is not sacrificing room quality or guest satisfaction scores. Maintain regular quality audits.
        """)

    hpor_status = f"**HPOR Evaluation ({hpor:.2f} hrs):** Your HPOR is above the luxury benchmark target of **2.50 hours**, indicating inefficient room servicing or excess indirect labor[cite: 11]. Reduce non-cleaning hours per shift." if hpor > 2.5 else f"**HPOR Evaluation ({hpor:.2f} hrs):** Your HPOR is performing at or better than the **2.50 hours** benchmark target[cite: 11]."
    lpr_status = f"**LPR Evaluation ({lpr:.1f}%):** Your LPR exceeds the ownership target ceiling of **16.0%**[cite: 11]. Payroll overhead is actively compressing your operating margin." if lpr > 16.0 else f"**LPR Evaluation ({lpr:.1f}%):** Your LPR is within the financial target ceiling of **16.0%**[cite: 11]."
    revpalh_status = f"**REVPALH Evaluation (${revpalh:.2f}):** Your REVPALH is below the **$130.00** benchmark[cite: 11], indicating low revenue productivity per labor hour." if revpalh < 130 else f"**REVPALH Evaluation (${revpalh:.2f}):** Your REVPALH meets or exceeds the **$130.00** productivity benchmark[cite: 11]."

    st.markdown(f"- {hpor_status}")
    st.markdown(f"- {lpr_status}")
    st.markdown(f"- {revpalh_status}")
    
    st.markdown("---")
    st.markdown("🎯 **Core Executive Decision Rule:** Do not schedule based on static occupancy or last month's calendar. Use departure forecasts and time standards to publish dynamic weekly rosters that eliminate unbudgeted overtime before compression hits[cite: 8, 10, 11].")

# ==========================================
# MODULE 2: CHANNEL MIX & NET REVPAR AUDIT
# ==========================================
elif "2. Channel" in module_selection:
    st.markdown("# Module 2: Channel Mix, Distribution Costs & Net RevPAR")
    st.markdown("Isolate true bottom-line retention by factoring in OTA and distribution commissions[cite: 17].")
    st.markdown("---")

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

    adr = room_revenue / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    revpar = room_revenue / available_rooms if available_rooms > 0 else 0
    trevpar = (room_revenue + fnb_revenue + ancillary_revenue) / available_rooms if available_rooms > 0 else 0
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
    st.markdown("# Module 3: Competitive Set Indexing & Scenario Modeling")
    st.markdown("Calculate MPI, ARI, RGI, Price Elasticity of Demand (PED), and probability-weighted forecasts[cite: 26, 33].")
    st.markdown("---")

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

    mpi = (hotel_occ / comp_occ) * 100 if comp_occ > 0 else 0
    ari = (hotel_adr / comp_adr) * 100 if comp_adr > 0 else 0
    hotel_revpar = (hotel_occ / 100.0) * hotel_adr
    comp_revpar = (comp_occ / 100.0) * comp_adr
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
    st.markdown("# Module 4: AI Governance, Variance Limits & GOPPAR Analytics")
    st.markdown("Monitor forecast accuracy (MAPE), evaluate profit-per-room (GOPPAR), and enforce human-in-the-loop guardrails[cite: 40].")
    st.markdown("---")

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
    st.markdown("# Module 5: Demand Resilience, DRI & ACR")
    st.markdown("Measure demand recapture without discounting using the Demand Redistribution Index (DRI) and Ancillary Capture Rate (ACR)[cite: 46].")
    st.markdown("---")

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Demand Redistribution Inputs**")
        rooms_lost = st.number_input("Room-Nights Lost (Exposed Segment)", min_value=1, value=340)
        rooms_recaptured = st.number_input("Room-Nights Recaptured (Alternate Segment)", min_value=0, value=207)

    with col2:
        st.markdown("#### **Ancillary Capture Rate Inputs**")
        fnb_spa_rev = st.number_input("F&B + Spa + Ancillary Revenue ($)", min_value=0.0, value=460000.0, step=5000.0)
        total_prop_rev = st.number_input("Total Property Revenue ($)", min_value=0.0, value=2150000.0, step=10000.0)

    dri = (rooms_recaptured / rooms_lost) * 100 if rooms_lost > 0 else 0
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
    st.markdown("# Module 6: Portfolio Scorecard & Boardroom Strategy")
    st.markdown("Audit multi-property performance using the GOPPAR gap benchmark and evaluate capital projects via ROI and payback[cite: 53, 54].")
    st.markdown("---")

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
