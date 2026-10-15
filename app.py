import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION & EXECUTIVE THEME ---
st.set_page_config(
    page_title="MAREC Insights | Hospitality Workforce & Revenue Intelligence",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- ADVANCED EXECUTIVE CSS STYLING ---
st.markdown("""
    <style>
    /* Global Page Styling */
    .main {
        background-color: #f8fafc;
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Executive Header Banner */
    .executive-banner {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 60%, #1e40af 100%);
        padding: 2.25rem 2.5rem;
        border-radius: 16px;
        color: #ffffff;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px -5px rgba(15, 23, 42, 0.25);
        border-left: 6px solid #3b82f6;
    }
    .executive-banner h1 {
        color: #ffffff !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
        margin-bottom: 0.5rem !important;
    }
    .executive-banner p {
        color: #94a3b8 !important;
        font-size: 1.1rem !important;
        margin-bottom: 0 !important;
    }
    
    /* Styled Action & Insight Cards */
    .protocol-card {
        background-color: #ffffff;
        padding: 1.75rem;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #2563eb;
        margin-top: 1.5rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    
    /* Streamlit Metric Styling Overrides */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 1.25rem 1.5rem;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(15, 23, 42, 0.03);
    }
    div[data-testid="stMetric"] label {
        color: #64748b !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
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
st.sidebar.markdown("## 🏨 **MAREC Insights**")
st.sidebar.caption("Hospitality Workforce & Commercial Intelligence Platform")
st.sidebar.markdown("---")

module_selection = st.sidebar.selectbox(
    "Choose Executive Tool",
    [
        "1. Workforce & Labor Optimization (Module 1)",
        "2. Channel Mix & Net RevPAR Audit (Module 2)",
        "3. Competitive Indexing & Scenario Modeling (Module 3)",
        "4. AI Governance & GOPPAR Analytics (Module 4)",
        "5. Demand Resilience, DRI & ACR (Module 5)",
        "6. Portfolio Scorecard & Boardroom Strategy (Module 6)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("⚡ Operating Model: Aurora Mirage Resort Executive Framework")

# ==========================================
# MODULE 1: WORKFORCE & LABOR OPTIMIZATION
# ==========================================
if "1. Workforce" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 1: Demand-Driven Housekeeping & Labor Optimization</h1>
            <p>Calculate precise staffing requirements, HPOR, and labor cost ratios directly from property management signals.</p>
        </div>
    """, unsafe_allow_html=True)

    st.info("📋 **Step 1: Operational Demand & Payroll Setup**\n\nEnter today's PMS room turn numbers and total payroll hours below. Departures drive room attendant workload and scheduling requirements, not occupancy alone.")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("#### **Operational Demand Signals (PMS)**")
        departures = st.number_input("Departures / Full Cleans (30 min standard)", min_value=0, value=280, step=10)
        dep_minutes = st.number_input("Minutes per Departure Clean", min_value=0.0, value=30.0, step=2.5)
        stayovers = st.number_input("Stay-overs / Light Cleans (15 min standard)", min_value=0, value=120, step=10)
        stay_minutes = st.number_input("Minutes per Stay-over Clean", min_value=0.0, value=15.0, step=1.0)
        occupied_rooms = st.number_input("Total Occupied Rooms (PMS)", min_value=1, value=361, step=5)

    with col2:
        st.markdown("#### **Financial & Payroll Signals (HRIS / LMS)**")
        payroll_hours = st.number_input("Total Housekeeping Payroll Hours Logged", min_value=0.0, value=1300.0, step=10.0)
        blended_rate = st.number_input("Blended Hourly Rate ($)", min_value=0.0, value=22.0, step=0.5)
        total_rooms_rev = st.number_input("Total Rooms Revenue ($)", min_value=0.0, value=140000.0, step=1000.0)

    # Core Calculations
    total_cleaning_minutes = (departures * dep_minutes) + (stayovers * stay_minutes)
    total_cleaning_hours = total_cleaning_minutes / 60.0
    total_payroll_cost = payroll_hours * blended_rate
    lpr = (total_payroll_cost / total_rooms_rev) * 100 if total_rooms_rev > 0 else 0
    hpor = payroll_hours / occupied_rooms if occupied_rooms > 0 else 0
    revpalh = total_rooms_rev / payroll_hours if payroll_hours > 0 else 0
    hour_gap = payroll_hours - total_cleaning_hours

    st.markdown("---")
    st.markdown("### **Executive Workforce Performance Metrics**")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Engineered Clean Hours", f"{total_cleaning_hours:.1f} hrs", delta=f"Actual Logged: {payroll_hours} hrs", delta_color="inverse" if hour_gap > 0 else "normal")
    m2.metric("HPOR (Hours / Occ. Room)", f"{hpor:.2f} hrs", delta="Benchmark Target: 2.50 hrs", delta_color="inverse" if hpor > 2.5 else "normal")
    m3.metric("LPR (Labor Cost Ratio)", f"{lpr:.1f}%", delta="Target Ceiling: 16.0%", delta_color="inverse" if lpr > 16.0 else "normal")
    m4.metric("REVPALH", f"${revpalh:.2f}", delta="Benchmark Target: $130.00", delta_color="normal" if revpalh >= 130 else "inverse")

    # High-Impact Visual Chart
    df_m1 = pd.DataFrame({
        "Labor Metric": ["Engineered Cleaning Hours", "Logged Payroll Hours"],
        "Hours": [total_cleaning_hours, payroll_hours]
    })
    fig_m1 = px.bar(
        df_m1, x="Labor Metric", y="Hours", color="Labor Metric",
        color_discrete_map={"Engineered Cleaning Hours": "#10B981", "Logged Payroll Hours": "#EF4444" if hour_gap > 100 else "#3B82F6"},
        title="<b>Labor Demand Gap Analysis: Engineered Cleaning vs. Logged Payroll</b>",
        text_auto='.1f'
    )
    fig_m1.update_layout(template="plotly_white", showlegend=False, height=350)
    st.plotly_chart(fig_m1, use_container_width=True)

    # Dynamic Interpretation & Action Directives
    st.markdown("### **📊 Dynamic Action Recommendations & Operational Protocol**")
    if hour_gap > 200:
        st.error(f"🚨 **Critical Labor Overhead Alert:** Logged payroll exceeds calculated room cleaning time by **{hour_gap:.1f} hours**. Overhead, supervisory pools, or overtime are eroding department profitability.")
        st.markdown("""
            **Executive Action Plan:**
            1. **Audit Supervisory & Support Hours:** Review floor supervisor shift overlays and houseman staging hours.
            2. **Publish Departure-Driven Roster:** Shift room attendant start times to mirror checkout waves rather than flat 8:00 AM clock-ins.
            3. **Restrict Unbudgeted Overtime:** Freeze non-essential overtime approvals and deploy cross-departmental labor sharing.
        """)
    elif hour_gap > 0:
        st.warning(f"⚠️ **Moderate Labor Variance:** Logged payroll exceeds engineered cleaning time by **{hour_gap:.1f} hours**.")
        st.markdown("""
            **Executive Action Plan:**
            1. **Monitor Room Attendant Pacing:** Validate actual floor room cleans against standards (30 mins departure / 15 mins stay-over).
            2. **Align Mid-Week Scheduling:** Adjust staffing schedules to smooth out midweek checkout peaks.
        """)
    else:
        st.success(f"✅ **Optimal Labor Efficiency:** Logged payroll hours ({payroll_hours} hrs) are fully aligned with engineered cleaning workload ({total_cleaning_hours:.1f} hrs).")
        st.markdown("""
            **Executive Action Plan:**
            1. **Maintain Quality Control:** Perform spot checks on cleaned rooms to ensure speed does not degrade cleanliness scores.
        """)

    st.markdown("---")
    st.markdown("💡 **Core Decision Directive:** Base housekeeping shift schedules on predicted PMS departure curves rather than overall occupancy or historical calendars.")

# ==========================================
# MODULE 2: CHANNEL MIX & NET REVPAR AUDIT
# ==========================================
elif "2. Channel" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 2: Channel Mix, Distribution Costs & Net RevPAR</h1>
            <p>Isolate true revenue retention by factoring OTA commissions, GDS fees, and channel distribution costs.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Property Performance Signals**")
        available_rooms = st.number_input("Total Available Rooms", min_value=1, value=400)
        occupied_rooms_m2 = st.number_input("Rooms Sold / Occupied Rooms", min_value=0, value=350)
        room_revenue = st.number_input("Gross Room Revenue ($)", min_value=0.0, value=150000.0, step=1000.0)
        fnb_revenue = st.number_input("F&B Revenue ($)", min_value=0.0, value=40000.0, step=1000.0)
        ancillary_revenue = st.number_input("Ancillary Revenue ($)", min_value=0.0, value=10000.0, step=500.0)
    with col2:
        st.markdown("#### **Channel Distribution & Commission Inputs**")
        total_dist_costs = st.number_input("Total Distribution / Commission Costs ($)", min_value=0.0, value=27000.0, step=500.0)

    adr = room_revenue / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    revpar = room_revenue / available_rooms if available_rooms > 0 else 0
    trevpar = (room_revenue + fnb_revenue + ancillary_revenue) / available_rooms if available_rooms > 0 else 0
    net_room_rev = room_revenue - total_dist_costs
    net_revpar = net_room_rev / available_rooms if available_rooms > 0 else 0
    net_adr = net_room_rev / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    blended_dist_pct = (total_dist_costs / room_revenue) * 100 if room_revenue > 0 else 0

    st.markdown("---")
    st.markdown("### **Executive Commercial Performance Metrics**")

    r1, r2, r3, r4, r5 = st.columns(5)
    r1.metric("Gross ADR", f"${adr:.2f}")
    r2.metric("Gross RevPAR", f"${revpar:.2f}")
    r3.metric("TRevPAR", f"${trevpar:.2f}")
    r4.metric("Net RevPAR", f"${net_revpar:.2f}", delta=f"Net ADR: ${net_adr:.2f}")
    r5.metric("Distribution Cost %", f"{blended_dist_pct:.1f}%", delta_color="inverse" if blended_dist_pct > 15 else "normal")

    df_m2 = pd.DataFrame({
        "KPI Category": ["Gross ADR", "Net ADR", "Gross RevPAR", "Net RevPAR"],
        "Revenue ($)": [adr, net_adr, revpar, net_revpar]
    })
    fig_m2 = px.bar(
        df_m2, x="KPI Category", y="Revenue ($)", color="KPI Category",
        color_discrete_sequence=["#1E3A8A", "#3B82F6", "#059669", "#10B981"],
        title="<b>Gross vs. Net Commercial Yield Comparison</b>",
        text_auto='.2f'
    )
    fig_m2.update_layout(template="plotly_white", showlegend=False, height=350)
    st.plotly_chart(fig_m2, use_container_width=True)

    st.markdown("### **📊 Executive Channel Strategy Action Protocol**")
    if blended_dist_pct > 15.0:
        st.warning(f"⚠️ **High Acquisition Cost Warning:** Distribution costs are consuming **{blended_dist_pct:.1f}%** of gross room revenue. Net RevPAR retention is diluted by **${(revpar - net_revpar):.2f} per available room**.")
        st.markdown("""
            **Recommended Actions:**
            * **Shift OTA Demand:** Implement restricted rate parity or exclusive loyalty add-ons (e.g., resort credits) on direct web channels.
            * **Audit Channel Margins:** Re-evaluate high-commission OTA market growth packages during peak demand dates.
        """)
    else:
        st.success(f"✅ **Healthy Distribution Efficiency:** Blended distribution cost ({blended_dist_pct:.1f}%) is performing within optimal retention targets.")

# ==========================================
# MODULE 3: COMPETITIVE INDEXING & SCENARIO MODELING
# ==========================================
elif "3. Competitive" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 3: Competitive Set Indexing & Scenario Modeling</h1>
            <p>Calculate MPI, ARI, RGI, and build probability-weighted commercial forecasts.</p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown("#### **Market Share Inputs (STR Benchmarks)**")
        hotel_occ = st.number_input("Property Occupancy (%)", 0.0, 100.0, 68.0)
        comp_occ = st.number_input("Comp-Set Average Occupancy (%)", 0.0, 100.0, 74.0)
        hotel_adr = st.number_input("Property ADR ($)", 0.0, 1000.0, 428.57)
        comp_adr = st.number_input("Comp-Set Average ADR ($)", 0.0, 1000.0, 412.00)
    with c2:
        st.markdown("#### **Probability-Weighted GOP Forecast**")
        prob_best = st.slider("Best Case Probability (%)", 0, 100, 25)
        gop_best = st.number_input("Best Case GOP %", 0.0, 100.0, 36.5)
        prob_base = st.slider("Base Case Probability (%)", 0, 100, 55)
        gop_base = st.number_input("Base Case GOP %", 0.0, 100.0, 32.0)
        prob_down = max(0, 100 - (prob_best + prob_base))
        st.caption(f"Downside Case Probability (Auto-balanced): **{prob_down}%**")
        gop_down = st.number_input("Downside Case GOP %", 0.0, 100.0, 26.0)

    mpi = (hotel_occ / comp_occ) * 100 if comp_occ > 0 else 0
    ari = (hotel_adr / comp_adr) * 100 if comp_adr > 0 else 0
    hotel_revpar = (hotel_occ / 100.0) * hotel_adr
    comp_revpar = (comp_occ / 100.0) * comp_adr
    rgi = (hotel_revpar / comp_revpar) * 100 if comp_revpar > 0 else (mpi * ari) / 100
    weighted_gop = ((prob_best / 100.0) * gop_best) + ((prob_base / 100.0) * gop_base) + ((prob_down / 100.0) * gop_down)

    st.markdown("---")
    st.markdown("### **Market Penetration & Forecast Summary**")

    i1, i2, i3, i4 = st.columns(4)
    i1.metric("MPI (Occupancy Index)", f"{mpi:.1f}", delta="Fair Share = 100")
    i2.metric("ARI (Rate Index)", f"{ari:.1f}", delta="Fair Share = 100")
    i3.metric("RGI (RevPAR Index)", f"{rgi:.1f}", delta="Fair Share = 100", delta_color="normal" if rgi >= 100 else "inverse")
    i4.metric("Weighted GOP Forecast", f"{weighted_gop:.2f}%")

    df_m3 = pd.DataFrame({
        "Index Metric": ["MPI (Occupancy Share)", "ARI (Rate Leadership)", "RGI (RevPAR Share)"],
        "Index Score": [mpi, ari, rgi]
    })
    fig_m3 = px.bar(
        df_m3, x="Index Metric", y="Index Score", color="Index Metric",
        color_discrete_sequence=["#3B82F6", "#10B981", "#1E3A8A"],
        title="<b>Competitive Penetration Benchmarks (Fair Share = 100.0)</b>",
        text_auto='.1f'
    )
    fig_m3.add_hline(y=100, line_dash="dash", line_color="#EF4444", annotation_text="Fair Share Target (100.0)")
    fig_m3.update_layout(template="plotly_white", showlegend=False, height=350)
    st.plotly_chart(fig_m3, use_container_width=True)

    st.markdown("### **📊 Market Share Strategy Recommendations**")
    if rgi < 100.0:
        st.warning(f"⚠️ **RevPAR Underpenetration:** Property RGI of **{rgi:.1f}** is below fair market share. {'Occupancy index (MPI) is lagging.' if mpi < 100 else 'Rate index (ARI) is underperforming.'}")
    else:
        st.success(f"✅ **Market Leadership:** RGI of **{rgi:.1f}** indicates your property is generating above its fair share of revenue.")

# ==========================================
# MODULE 4: AI GOVERNANCE & GOPPAR ANALYTICS
# ==========================================
elif "4. AI Governance" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 4: AI Governance, Variance Limits & GOPPAR Analytics</h1>
            <p>Monitor forecast accuracy (MAPE), evaluate profit-per-room (GOPPAR), and enforce automated guardrails.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Profitability & GOP Inputs**")
        gross_op_profit = st.number_input("Gross Operating Profit (GOP) ($)", min_value=0.0, value=59200.0, step=1000.0)
        total_avail_rooms_m4 = st.number_input("Total Available Rooms (Monthly)", min_value=1, value=400)
    with col2:
        st.markdown("#### **AI Algorithmic Audit Inputs**")
        actual_demand = st.number_input("Actual Occupied Rooms Realized", min_value=1, value=361)
        forecast_demand = st.number_input("Model Forecasted Occupied Rooms", min_value=1, value=350)
        variance_limit_pct = st.number_input("Configured Governance Limit (%)", min_value=0.0, value=8.0, step=0.5)

    goppar = gross_op_profit / total_avail_rooms_m4 if total_avail_rooms_m4 > 0 else 0
    abs_error_pct = (abs(actual_demand - forecast_demand) / actual_demand) * 100 if actual_demand > 0 else 0
    proposed_move_pct = abs_error_pct * 1.5

    st.markdown("---")
    st.markdown("### **Governance & Profitability Dashboard**")

    g1, g2, g3, g4 = st.columns(4)
    g1.metric("GOPPAR", f"${goppar:.2f}", delta="Profit / Avail Room")
    g2.metric("Forecast Error (MAPE)", f"{abs_error_pct:.2f}%", delta="Target < 3.0%")
    g3.metric("Proposed Rate Move", f"{proposed_move_pct:.1f}%", delta=f"Limit: {variance_limit_pct}%")
    g4.metric("Governance Action", "ESCALATE TO HUMAN" if proposed_move_pct > variance_limit_pct else "AUTO-EXECUTE", delta_color="inverse" if proposed_move_pct > variance_limit_pct else "normal")

    df_m4 = pd.DataFrame({
        "Category": ["Actual Occupied Rooms", "AI Model Forecast"],
        "Rooms": [actual_demand, forecast_demand]
    })
    fig_m4 = px.bar(
        df_m4, x="Category", y="Rooms", color="Category",
        color_discrete_sequence=["#10B981", "#3B82F6"],
        title="<b>AI Model Demand Forecast vs. Realized Room Sales</b>",
        text_auto=True
    )
    fig_m4.update_layout(template="plotly_white", showlegend=False, height=350)
    st.plotly_chart(fig_m4, use_container_width=True)

    st.markdown("### **📊 Governance Protocol Directives**")
    if proposed_move_pct > variance_limit_pct:
        st.error(f"🚨 **Guardrail Triggered (Escalation Required):** The proposed rate move of **{proposed_move_pct:.1f}%** exceeds the maximum automated threshold of **{variance_limit_pct}%**. Requires manual sign-off by Revenue Director before publishing.")
    else:
        st.success("✅ **Governance Clear:** Forecast variance is within parameters. System authorized to auto-publish rate recommendations.")

# ==========================================
# MODULE 5: DEMAND RESILIENCE, DRI & ACR
# ==========================================
elif "5. Demand" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 5: Demand Resilience, DRI & ACR</h1>
            <p>Track demand recapture across guest segments without blanket discounting using DRI and Ancillary Capture Rate.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Demand Redistribution Inputs**")
        rooms_lost = st.number_input("Room-Nights Lost (Softened Segment)", min_value=1, value=340)
        rooms_recaptured = st.number_input("Room-Nights Recaptured (Alternate Segment)", min_value=0, value=207)
    with col2:
        st.markdown("#### **Ancillary Revenue Wallet Share**")
        fnb_spa_rev = st.number_input("F&B + Spa + Ancillary Revenue ($)", min_value=0.0, value=460000.0, step=5000.0)
        total_prop_rev = st.number_input("Total Property Revenue ($)", min_value=0.0, value=2150000.0, step=10000.0)

    dri = (rooms_recaptured / rooms_lost) * 100 if rooms_lost > 0 else 0
    acr = (fnb_spa_rev / total_prop_rev) * 100 if total_prop_rev > 0 else 0

    st.markdown("---")
    st.markdown("### **Resilience & Wallet Share Metrics**")

    d1, d2 = st.columns(2)
    d1.metric("DRI (Demand Redistribution Index)", f"{dri:.1f}%", delta="Recapture Benchmark > 60.0%")
    d2.metric("ACR (Ancillary Capture Rate)", f"{acr:.1f}%", delta="Total Wallet Share Yield")

    df_m5 = pd.DataFrame({
        "Resilience Benchmark": ["DRI (Demand Recapture %)", "ACR (Ancillary Contribution %)"],
        "Percentage": [dri, acr]
    })
    fig_m5 = px.bar(
        df_m5, x="Resilience Benchmark", y="Percentage", color="Resilience Benchmark",
        color_discrete_sequence=["#10B981", "#3B82F6"],
        title="<b>Resilience Indices: Demand Recapture vs. Non-Room Yield</b>",
        text_auto='.1f'
    )
    fig_m5.update_layout(template="plotly_white", showlegend=False, height=350)
    st.plotly_chart(fig_m5, use_container_width=True)

    st.markdown("### **📊 Resilience Strategy Directives**")
    if dri < 60.0:
        st.warning(f"⚠️ **Recapture Gap:** DRI is **{dri:.1f}%** (target > 60.0%). Boost targeted promotional efforts in secondary segments (e.g., regional drive-in markets) rather than un-fencing primary rates.")
    else:
        st.success("✅ **Strong Resilience:** Demand recapture mechanisms are buffering transient volume fluctuations.")

# ==========================================
# MODULE 6: PORTFOLIO SCORECARD & BOARDROOM STRATEGY
# ==========================================
elif "6. Portfolio" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 6: Portfolio Scorecard & Boardroom Strategy</h1>
            <p>Audit multi-property yield using GOPPAR gap analysis and evaluate capital expenditure projects via 3-Year ROI.</p>
        </div>
    """, unsafe_allow_html=True)

    portfolio_data = pd.DataFrame({
        "Property": ["Aurora Mirage (Las Vegas)", "Property B (Reno)", "Property C (Phoenix)", "Property D (San Diego)"],
        "Actual GOPPAR ($)": [148.0, 121.0, 133.0, 156.0],
        "Achievable GOPPAR ($)": [150.0, 138.0, 135.0, 158.0]
    })
    portfolio_data["GOPPAR Gap ($)"] = portfolio_data["Actual GOPPAR ($)"] - portfolio_data["Achievable GOPPAR ($)"]

    st.markdown("#### **Cross-Property Portfolio GOPPAR Gap Analysis**")
    st.dataframe(portfolio_data, use_container_width=True)

    fig_m6_1 = px.bar(
        portfolio_data.melt(id_vars="Property", value_vars=["Actual GOPPAR ($)", "Achievable GOPPAR ($)"]),
        x="Property", y="value", color="variable", barmode="group",
        color_discrete_sequence=["#1E3A8A", "#10B981"],
        title="<b>Actual vs. Target GOPPAR Benchmarks Across Properties</b>",
        labels={"value": "GOPPAR ($)", "variable": "Benchmark"}
    )
    fig_m6_1.update_layout(template="plotly_white", height=380)
    st.plotly_chart(fig_m6_1, use_container_width=True)

    st.markdown("#### **Capital Expenditure ROI & Payback Prioritization**")
    capex_data = pd.DataFrame({
        "Project": ["PMS Upgrade", "Direct-Booking Engine", "Solar Efficiency", "Spa Expansion", "Tower Wing"],
        "3-Yr ROI (%)": [34, 28, 19, 14, 9],
        "Payback Period (Years)": [0.8, 1.4, 3.2, 4.5, 7.8]
    })
    
    fig_m6_2 = px.bar(
        capex_data, x="Project", y="3-Yr ROI (%)", color="Payback Period (Years)",
        color_continuous_scale="Viridis",
        title="<b>Capital Project Portfolio ROI & Payback Ranking</b>",
        text_auto=True
    )
    fig_m6_2.update_layout(template="plotly_white", height=380)
    st.plotly_chart(fig_m6_2, use_container_width=True)

    st.markdown("### **📊 Boardroom Capital Directives**")
    st.info("💡 **Resource Allocation Strategy:** Prioritize capital deployments to projects with payback periods under 2.0 years (PMS Upgrades and Direct Booking Engines) to accelerate portfolio cash flow.")
