import streamlit as st
import pandas as pd
import plotly.express as px

# --- PAGE CONFIGURATION & EXECUTIVE THEME ---
st.set_page_config(
    page_title="MAREC Insights | CHRM Mastery & Revenue Intelligence",
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
    
    /* Protocol and Formula Cards */
    .protocol-card {
        background-color: #ffffff;
        padding: 1.75rem;
        border-radius: 14px;
        border: 1px solid #e2e8f0;
        border-left: 5px solid #2563eb;
        margin-top: 1.25rem;
        margin-bottom: 1.25rem;
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
st.sidebar.caption("CHRM Prep & Commercial Intelligence Engine")
st.sidebar.markdown("---")

module_selection = st.sidebar.selectbox(
    "Choose Module / Exam Tool",
    [
        "0. CHRM Exam Prep & Core Formulas",
        "1. Group Displacement & Transient Cutoff (CHRM Ch. 3 & 7)",
        "2. Workforce & Labor Optimization (CHRM Ch. 2)",
        "3. Channel Mix, Merchant/Wholesale & Net RevPAR (CHRM Ch. 3 & 8)",
        "4. STR Indexing (MPI, ARI, RGI) & Scenario Modeling (CHRM Ch. 6)",
        "5. GOPPAR, Flow-Through & AI Governance (CHRM Ch. 4 & 5)",
        "6. Demand Resilience & Portfolio Strategy (CHRM Ch. 7 & 8)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("🎓 **Certified Hospitality Revenue Manager (AHLEI)**")
st.sidebar.caption("⚡ Operating Sandbox: Aurora Mirage Resort Executive Model")

# ==========================================
# MODULE 0: CHRM EXAM PREP & CORE FORMULAS
# ==========================================
if "0. CHRM Exam Prep" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 0: AHLEI CHRM Exam Mastery Center</h1>
            <p>Review core AHLEI formulas, key revenue management principles, and interactive test prep flashcards.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📚 **Core CHRM Formulas Reference Cheat-Sheet**")
    
    f1, f2, f3 = st.columns(3)
    with f1:
        st.markdown("""
        <div class="protocol-card">
            <h4><b>1. Basic Key Metrics</b></h4>
            <ul>
                <li><b>Occupancy %:</b> <code>(Rooms Occupied ÷ Rooms Available) × 100</code></li>
                <li><b>ADR:</b> <code>Total Room Revenue ÷ Rooms Sold</code></li>
                <li><b>RevPAR:</b> <code>Room Revenue ÷ Total Available Rooms</code> OR <code>Occupancy % × ADR</code></li>
                <li><b>TRevPAR:</b> <code>(Room Rev + F&B Rev + Ancillary Rev) ÷ Available Rooms</code></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with f2:
        st.markdown("""
        <div class="protocol-card">
            <h4><b>2. STR Penetration Indices</b></h4>
            <ul>
                <li><b>MPI (Occupancy Share):</b> <code>(Property Occupancy ÷ Comp Set Occupancy) × 100</code></li>
                <li><b>ARI (Rate Index):</b> <code>(Property ADR ÷ Comp Set ADR) × 100</code></li>
                <li><b>RGI (RevPAR Share):</b> <code>(Property RevPAR ÷ Comp Set RevPAR) × 100</code> OR <code>(MPI × ARI) ÷ 100</code></li>
                <li><i>Note: 100.0 is Fair Market Share.</i></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with f3:
        st.markdown("""
        <div class="protocol-card">
            <h4><b>3. Financial & Yield Calculations</b></h4>
            <ul>
                <li><b>GOPPAR:</b> <code>Gross Operating Profit ÷ Total Available Rooms</code></li>
                <li><b>Net RevPAR:</b> <code>(Gross Room Rev - Distribution Costs) ÷ Available Rooms</code></li>
                <li><b>HPOR:</b> <code>Housekeeping Labor Hours ÷ Occupied Rooms</code></li>
                <li><b>LPR:</b> <code>(Department Payroll $ ÷ Rooms Revenue) × 100</code></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📝 **AHLEI CHRM Practice Questions & Key Concepts**")

    q1, q2 = st.columns(2)
    with q1:
        with st.expander("❓ **Q1: What is displacement analysis used for?**"):
            st.write("""
            **Answer:** Displacement analysis determines whether accepting a group block at a discounted rate generates more total net profit than the transient business that would be turned away (displaced) as a result.
            """)
        with st.expander("❓ **Q2: Explain the difference between Merchant and Wholesaler distribution models.**"):
            st.write("""
            **Answer:** 
            * **Merchant Model (Markup):** OTA buys rooms at a net rate discounted by 20–30% and marks them up before selling to consumers.
            * **Wholesaler Model:** Hotel sets the selling price and pays a fixed commission percentage or fixed fee to the intermediary.
            """)
        with st.expander("❓ **Q3: What does an RGI score of 108.5 indicate on an STR report?**"):
            st.write("""
            **Answer:** The property is outperforming its competitive set by **8.5%** in RevPAR (yielding 8.5% above its fair market share).
            """)

    with q2:
        with st.expander("❓ **Q4: What is the difference between constrained and unconstrained demand?**"):
            st.write("""
            **Answer:** 
            * **Unconstrained Demand:** Total potential demand for a hotel regardless of capacity limitations.
            * **Constrained Demand:** Actual demand capped by the physical number of available rooms in the hotel.
            """)
        with st.expander("❓ **Q5: What are Opaque booking sites?**"):
            st.write("""
            **Answer:** Websites (like Priceline or Hotwire) where hotel brand details are hidden until payment is completed, shielding public rate integrity while clearing distressed inventory.
            """)
        with st.expander("❓ **Q6: Why is RevPAR alone sometimes misleading?**"):
            st.write("""
            **Answer:** RevPAR ignores distribution commissions, acquisition costs, non-room revenues (F&B/Spa), and operating labor expenses. Metrics like Net RevPAR, TRevPAR, and GOPPAR provide a complete profit picture.
            """)

# ==========================================
# MODULE 1: GROUP DISPLACEMENT & TRANSIENT CUTOFF
# ==========================================
elif "1. Group Displacement" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 1: Group Displacement Analysis & Wash Down (AHLEI Ch. 3 & 7)</h1>
            <p>Calculate whether to accept a group block by evaluating displaced transient revenue and non-room profit contribution.</p>
        </div>
    """, unsafe_allow_html=True)

    st.info("📋 **CHRM Core Concept:** Displacement analysis evaluates whether accepting group business generates higher net profitability than retaining transient room inventory.")

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Proposed Group Contract Parameters**")
        group_rooms = st.number_input("Group Rooms Requested (per night)", min_value=1, value=50)
        group_rate = st.number_input("Offered Group Room Rate ($)", min_value=0.0, value=140.0, step=5.0)
        group_fnb_profit = st.number_input("Expected Group F&B / Banquet Net Profit ($)", min_value=0.0, value=3500.0, step=250.0)
        wash_rate_pct = st.number_input("Historical Group Wash Rate (%)", min_value=0.0, max_value=50.0, value=10.0, step=2.5)

    with col2:
        st.markdown("#### **Displaced Transient Demand Parameters**")
        displaced_transient_rooms = st.number_input("Transient Rooms Displaced (per night)", min_value=0, value=45)
        transient_adr = st.number_input("Forecasted Transient ADR ($)", min_value=0.0, value=195.0, step=5.0)
        transient_fnb_profit_per_room = st.number_input("Average Transient Non-Room Profit per Room ($)", min_value=0.0, value=25.0, step=2.5)

    # Wash calculation
    effective_group_rooms = group_rooms * (1.0 - (wash_rate_pct / 100.0))
    group_room_rev = effective_group_rooms * group_rate
    total_group_profit = group_room_rev + group_fnb_profit

    transient_room_rev_lost = displaced_transient_rooms * transient_adr
    transient_fnb_profit_lost = displaced_transient_rooms * transient_fnb_profit_per_room
    total_transient_profit_lost = transient_room_rev_lost + transient_fnb_profit_lost

    net_displacement_gain = total_group_profit - total_transient_profit_lost

    st.markdown("---")
    st.markdown("### **Displacement Analysis Summary**")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Effective Group Rooms (Post-Wash)", f"{effective_group_rooms:.0f} rooms", delta=f"{wash_rate_pct}% Wash Applied")
    m2.metric("Total Group Revenue Contribution", f"${total_group_profit:,.2f}", delta=f"F&B Profit: ${group_fnb_profit:,.2f}")
    m3.metric("Displaced Transient Profit Lost", f"${total_transient_profit_lost:,.2f}", delta=f"Transient Rooms: {displaced_transient_rooms}", delta_color="inverse")
    m4.metric("Net Financial Impact", f"${net_displacement_gain:,.2f}", delta="ACCEPT GROUP" if net_displacement_gain >= 0 else "REJECT GROUP", delta_color="normal" if net_displacement_gain >= 0 else "inverse")

    df_disp = pd.DataFrame({
        "Revenue Stream": ["Total Group Contribution", "Displaced Transient Revenue Lost", "Net Gain / (Loss)"],
        "Amount ($)": [total_group_profit, total_transient_profit_lost, net_displacement_gain]
    })
    fig_disp = px.bar(
        df_disp, x="Revenue Stream", y="Amount ($)", color="Revenue Stream",
        color_discrete_map={"Total Group Contribution": "#10B981", "Displaced Transient Revenue Lost": "#EF4444", "Net Gain / (Loss)": "#3B82F6" if net_displacement_gain >= 0 else "#DC2626"},
        title="<b>Group vs. Transient Displacement Financial Comparison</b>",
        text_auto=',.2f'
    )
    fig_disp.update_layout(template="plotly_white", showlegend=False, height=350)
    st.plotly_chart(fig_disp, use_container_width=True)

    if net_displacement_gain >= 0:
        st.success(f"✅ **CHRM Decision Recommendation: ACCEPT CONTRACT.** Accepting this group block produces a net positive gain of **${net_displacement_gain:,.2f}** compared to transient forecasts.")
    else:
        st.error(f"🚨 **CHRM Decision Recommendation: REJECT OR RENEGOTIATE.** Accepting this block results in a net profit loss of **${abs(net_displacement_gain):,.2f}**. Negotiate a higher group rate or demand minimum F&B spend.")

# ==========================================
# MODULE 2: WORKFORCE & LABOR OPTIMIZATION
# ==========================================
elif "2. Workforce" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 2: Housekeeping & Labor Cost Optimization (AHLEI Ch. 2)</h1>
            <p>Calculate engineered cleaning hours, HPOR, and labor cost ratios directly from PMS shift demand.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Operational Demand Signals (PMS)**")
        departures = st.number_input("Departures / Full Cleans", min_value=0, value=280, step=10)
        dep_minutes = st.number_input("Minutes per Departure Clean", min_value=0.0, value=30.0, step=2.5)
        stayovers = st.number_input("Stay-overs / Light Cleans", min_value=0, value=120, step=10)
        stay_minutes = st.number_input("Minutes per Stay-over Clean", min_value=0.0, value=15.0, step=1.0)
        occupied_rooms = st.number_input("Total Occupied Rooms (PMS)", min_value=1, value=361, step=5)

    with col2:
        st.markdown("#### **Financial & Payroll Signals**")
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
    st.markdown("### **Housekeeping Efficiency & Labor Metrics**")

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Engineered Clean Hours", f"{total_cleaning_hours:.1f} hrs", delta=f"Logged: {payroll_hours} hrs", delta_color="inverse" if hour_gap > 0 else "normal")
    m2.metric("HPOR (Hours / Occ. Room)", f"{hpor:.2f} hrs", delta="Target: 2.50 hrs", delta_color="inverse" if hpor > 2.5 else "normal")
    m3.metric("LPR (Labor Cost Ratio)", f"{lpr:.1f}%", delta="Ceiling Target: 16.0%", delta_color="inverse" if lpr > 16.0 else "normal")
    m4.metric("REVPALH", f"${revpalh:.2f}", delta="Target: $130.00", delta_color="normal" if revpalh >= 130 else "inverse")

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

# ==========================================
# MODULE 3: CHANNEL MIX, MERCHANT/WHOLESALE & NET REVPAR
# ==========================================
elif "3. Channel" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 3: Channel Mix, Distribution Costs & Net RevPAR (AHLEI Ch. 3 & 8)</h1>
            <p>Examine distribution model costs (Merchant vs. Wholesaler), GDS fees, and true Net RevPAR yield.</p>
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
        st.markdown("#### **Distribution & Commission Cost Inputs**")
        ota_commissions = st.number_input("OTA / Merchant Commissions ($)", min_value=0.0, value=18000.0, step=500.0)
        gds_crs_fees = st.number_input("GDS / CRS Switch Fees ($)", min_value=0.0, value=6000.0, step=250.0)
        travel_agent_commissions = st.number_input("Travel Agent Commissions ($)", min_value=0.0, value=3000.0, step=250.0)

    total_dist_costs = ota_commissions + gds_crs_fees + travel_agent_commissions
    adr = room_revenue / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    revpar = room_revenue / available_rooms if available_rooms > 0 else 0
    trevpar = (room_revenue + fnb_revenue + ancillary_revenue) / available_rooms if available_rooms > 0 else 0
    net_room_rev = room_revenue - total_dist_costs
    net_revpar = net_room_rev / available_rooms if available_rooms > 0 else 0
    net_adr = net_room_rev / occupied_rooms_m2 if occupied_rooms_m2 > 0 else 0
    blended_dist_pct = (total_dist_costs / room_revenue) * 100 if room_revenue > 0 else 0

    st.markdown("---")
    st.markdown("### **Commercial Yield & Distribution Metrics**")

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

# ==========================================
# MODULE 4: STR INDEXING & SCENARIO MODELING
# ==========================================
elif "4. STR Indexing" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 4: Competitive Set Indexing & Forecast Modeling (AHLEI Ch. 6)</h1>
            <p>Calculate MPI, ARI, RGI penetration indices against STR competitive benchmarks.</p>
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
    st.markdown("### **Competitive Penetration Summary**")

    i1, i2, i3, i4 = st.columns(4)
    i1.metric("MPI (Occupancy Share)", f"{mpi:.1f}", delta="Fair Share = 100")
    i2.metric("ARI (Rate Leadership)", f"{ari:.1f}", delta="Fair Share = 100")
    i3.metric("RGI (RevPAR Share)", f"{rgi:.1f}", delta="Fair Share = 100", delta_color="normal" if rgi >= 100 else "inverse")
    i4.metric("Weighted GOP Forecast", f"{weighted_gop:.2f}%")

    df_m3 = pd.DataFrame({
        "Index Metric": ["MPI (Occupancy Share)", "ARI (Rate Leadership)", "RGI (RevPAR Share)"],
        "Index Score": [mpi, ari, rgi]
    })
    fig_m3 = px.bar(
        df_m3, x="Index Metric", y="Index Score", color="Index Metric",
        color_discrete_sequence=["#3B82F6", "#10B981", "#1E3A8A"],
        title="<b>STR Penetration Index Performance (Fair Market Share = 100.0)</b>",
        text_auto='.1f'
    )
    fig_m3.add_hline(y=100, line_dash="dash", line_color="#EF4444", annotation_text="Fair Share Benchmark (100.0)")
    fig_m3.update_layout(template="plotly_white", showlegend=False, height=350)
    st.plotly_chart(fig_m3, use_container_width=True)

# ==========================================
# MODULE 5: GOPPAR, FLOW-THROUGH & AI GOVERNANCE
# ==========================================
elif "5. GOPPAR" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 5: GOPPAR, Flow-Through & AI Governance (AHLEI Ch. 4 & 5)</h1>
            <p>Evaluate gross operating profit per room, flow-through percentage, and automated pricing governance limits.</p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown("#### **Profitability & Flow-Through Inputs**")
        gross_op_profit = st.number_input("Gross Operating Profit (GOP) ($)", min_value=0.0, value=59200.0, step=1000.0)
        total_avail_rooms_m4 = st.number_input("Total Available Rooms (Monthly)", min_value=1, value=400)
        prior_gop = st.number_input("Prior Period GOP ($)", min_value=0.0, value=48000.0, step=1000.0)
        curr_revenue = st.number_input("Current Period Revenue ($)", min_value=0.0, value=150000.0, step=5000.0)
        prior_revenue = st.number_input("Prior Period Revenue ($)", min_value=0.0, value=125000.0, step=5000.0)

    with col2:
        st.markdown("#### **AI Algorithmic Audit Inputs**")
        actual_demand = st.number_input("Actual Occupied Rooms Realized", min_value=1, value=361)
        forecast_demand = st.number_input("Model Forecasted Occupied Rooms", min_value=1, value=350)
        variance_limit_pct = st.number_input("Configured Governance Limit (%)", min_value=0.0, value=8.0, step=0.5)

    goppar = gross_op_profit / total_avail_rooms_m4 if total_avail_rooms_m4 > 0 else 0
    rev_change = curr_revenue - prior_revenue
    gop_change = gross_op_profit - prior_gop
    flow_through = (gop_change / rev_change) * 100 if rev_change != 0 else 0

    abs_error_pct = (abs(actual_demand - forecast_demand) / actual_demand) * 100 if actual_demand > 0 else 0
    proposed_move_pct = abs_error_pct * 1.5

    st.markdown("---")
    st.markdown("### **Profitability & Algorithmic Governance Metrics**")

    g1, g2, g3, g4 = st.columns(4)
    g1.metric("GOPPAR", f"${goppar:.2f}", delta="Profit / Avail Room")
    g2.metric("Flow-Through %", f"{flow_through:.1f}%", delta="Target: 50-60%")
    g3.metric("Forecast Error (MAPE)", f"{abs_error_pct:.2f}%", delta="Target < 3.0%")
    g4.metric("Governance Action", "ESCALATE TO HUMAN" if proposed_move_pct > variance_limit_pct else "AUTO-EXECUTE", delta_color="inverse" if proposed_move_pct > variance_limit_pct else "normal")

# ==========================================
# MODULE 6: DEMAND RESILIENCE & PORTFOLIO STRATEGY
# ==========================================
elif "6. Demand" in module_selection:
    st.markdown("""
        <div class="executive-banner">
            <h1>Module 6: Demand Resilience & Boardroom Strategy (AHLEI Ch. 7 & 8)</h1>
            <p>Analyze segment demand redistribution (DRI) and multi-property GOPPAR portfolio gaps.</p>
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

    st.markdown("### **📊 Boardroom Strategic Directives**")
    st.success("✅ **Portfolio Execution Directive:** Focus capital deployment toward Property B (Reno) to close its GOPPAR gap and fast-track high-ROI technology upgrades (PMS & Direct-Booking Engine) showing sub-1.5 year payback periods.")
