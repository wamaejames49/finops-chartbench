# 📊 FinOps-ChartBench: Multi-Step Quantitative Reasoning Benchmark

An open-source evaluation benchmark designed to stress-test **Multimodal AI / Vision-Language Models (VLMs)** on complex financial and operational charts.

Authored by **James Njogu Wamae** | *Subject Matter Expert – Financial & Operations Chart Analysis*

---

## 🎯 Overview & Objectives
Current frontier models (such as GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5 Pro) frequently hallucinate or miscalculate when interpreting complex visual charts with non-zero Y-axes, dual-unit scales, and multi-factor trends. 

**FinOps-ChartBench** provides a structured evaluation dataset to test:
1. **Multi-Step Quantitative Reasoning:** Requiring multi-stage calculations rather than surface-level optical reading.
2. **Ambiguity Elimination:** Enforcing strict unit definitions, rounding rules, and coordinate constraints.
3. **Chain-of-Thought (CoT) Verification:** Producing single-answer verifiable ground truths with explicit step-by-step mathematical proofs.

---

## 📈 Supported Chart Families
* **Financial Risk & Valuation:** Drawdown profiles, Yield Curves, Candlestick patterns, Cash-flow distributions.
* **Operations & Process Control:** Statistical Process Control (SPC / X-bar charts), Pareto distributions, Capacity/Throughput models.

---

## 🔬 Benchmark Methodology Example

### Task Sample: `FIN_DD_001` (Drawdown & Recovery Analysis)
* **Question:** *Calculate the peak-to-trough percentage drawdown between Month 4 ($120,000) and Month 7 ($78,000). By Month 10, capital recovered to $105,000. What percentage of the initial drawdown loss was successfully recovered?*
* **Ambiguity Controls:** Units in `%`, rounded to 2 decimal places, indexed to Month 4 baseline.
* **Chain-of-Thought Derivation:**
  * **Step 1:** Peak-to-Trough Loss = $\$120,000 - \$78,000 = \$42,000$
  * **Step 2:** Drawdown Percentage = $(\$42,000 / \$120,000) \times 100 = \mathbf{35.00\%}$
  * **Step 3:** Regained Capital = $\$105,000 - \$78,000 = \$27,000$
  * **Step 4:** Loss Recovery Ratio = $(\$27,000 / \$42,000) \times 100 = \mathbf{64.29\%}$
* **Ground Truth:** `Drawdown: 35.00%; Loss Recovered: 64.29%`

---

## 🚀 Running Locally or Deploying
To launch the interactive explorer:
```bash
pip install -r requirements.txt
streamlit run app.py
