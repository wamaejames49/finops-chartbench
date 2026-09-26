import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json
import os

st.set_page_config(page_title="FinOps-ChartBench Explorer", layout="wide", page_icon="📊")

st.title("📊 FinOps-ChartBench: Multi-Step Quantitative Reasoning")
st.markdown("""
**An evaluation benchmark for multimodal AI models (Vision-Language Models).**  
Constructed by **James Njogu Wamae** | Financial & Operations SME  
*Tests AI reasoning across complex axes, unit calibrations, and multi-step Chain-of-Thought derivations.*
""")

# Load Benchmark Dataset
DATA_FILE = "benchmark_tasks.json"
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        tasks = json.load(f)
else:
    st.error("benchmark_tasks.json file not found in repository.")
    st.stop()

# Helper Functions to Render Charts Dynamically
def render_spc():
    np.random.seed(42)
    batches = np.arange(1, 21)
    throughput = np.random.normal(loc=400, scale=20, size=20)
    throughput[5] = 330
    throughput[13] = 465

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(batches, throughput, marker='o', color='#1f77b4', linewidth=2, label='Hourly Throughput')
    ax.axhline(400, color='green', linestyle='--', label='Nominal Target (400 u/h)')
    ax.axhline(450, color='red', linestyle=':', linewidth=1.5, label='Upper Control Limit (UCL: 450)')
    ax.axhline(350, color='red', linestyle=':', linewidth=1.5, label='Lower Control Limit (LCL: 350)')
    ax.set_title('Assembly Line Throughput — Statistical Process Control (SPC)', fontsize=12, fontweight='bold')
    ax.set_xlabel('Production Batch ID')
    ax.set_ylabel('Throughput (Units / Hour)')
    ax.set_xticks(batches)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right')
    plt.tight_layout()
    return fig

def render_drawdown():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
    portfolio_value = [100000, 110000, 115000, 120000, 95000, 85000, 78000, 90000, 98000, 105000]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(months, portfolio_value, marker='s', color='#2ca02c', linewidth=2, label='Portfolio Value (USD)')
    ax.axvline(x=3, color='grey', linestyle='--', alpha=0.6, label='Peak (Apr: $120,000)')
    ax.axvline(x=6, color='red', linestyle='--', alpha=0.6, label='Trough (Jul: $78,000)')
    ax.fill_between(range(3, 7), [portfolio_value[i] for i in range(3, 7)], 120000, color='red', alpha=0.15, label='Drawdown Phase')
    ax.set_title('Multi-Period Portfolio Valuation & Drawdown Profile', fontsize=12, fontweight='bold')
    ax.set_xlabel('Fiscal Month')
    ax.set_ylabel('Capital Valuation (USD)')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left')
    plt.tight_layout()
    return fig

def render_pareto():
    categories = ['Packaging', 'Seal Breach', 'Label Misprint', 'Weight Deficit', 'Contamination']
    counts = [142, 68, 35, 14, 6]
    df = pd.DataFrame({'reason': categories, 'count': counts})
    df['cum_percentage'] = df['count'].cumsum() / df['count'].sum() * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.bar(df['reason'], df['count'], color='#3470a3', alpha=0.8, label='Defect Frequency')
    ax1.set_ylabel('Defect Frequency (Units)', color='#3470a3', fontweight='bold')
    
    ax2 = ax1.twinx()
    ax2.plot(df['reason'], df['cum_percentage'], color='#d95f02', marker='D', linewidth=2, label='Cumulative %')
    ax2.set_ylabel('Cumulative Percentage (%)', color='#d95f02', fontweight='bold')
    ax2.axhline(80, color='grey', linestyle='--', alpha=0.7, label='80% Cutoff')
    ax2.set_ylim(0, 105)
    plt.title('Operational Defect Distribution — Pareto Analysis', fontsize=12, fontweight='bold')
    plt.tight_layout()
    return fig

# UI Layout
task_map = {t["task_id"]: t for t in tasks}
selected_id = st.sidebar.selectbox("Select Evaluation Task:", list(task_map.keys()))
task = task_map[selected_id]

col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown(f"### Visual Visualization: `{task['chart_type']}`")
    if selected_id == "OPS_SPC_001":
        st.pyplot(render_spc())
    elif selected_id == "FIN_DD_001":
        st.pyplot(render_drawdown())
    elif selected_id == "OPS_PAR_001":
        st.pyplot(render_pareto())

with col2:
    st.markdown("### Target Reasoning Prompt")
    st.info(task["question"])

    st.markdown("#### 🔒 Ambiguity Controls & Rubrics")
    st.json(task["ambiguity_controls"])

    with st.expander("🔍 Show Step-by-Step Chain-of-Thought (CoT) Derivation", expanded=True):
        st.markdown(f"**Step-by-Step Proof:**\n\n```text\n{task['chain_of_thought']}\n```")
        st.success(f"**Verified Ground Truth:** {task['ground_truth']}")

st.divider()
st.caption("Engineered for evaluating Multimodal Frontier AI Models | Author: James Njogu Wamae")
