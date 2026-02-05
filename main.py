import os
from src.cost_models import manual_cost_model, ai_cost_model
from src.roi_engine import calculate_roi
from src.scenario_simulation import run_scenarios
from src.export_tools import export_excel, export_report

os.makedirs("outputs", exist_ok=True)

# Manual process
employees = 6
hours_per_day = 6
cost_per_hour = 350
days_per_month = 22

monthly_manual, annual_manual = manual_cost_model(
    employees, hours_per_day, cost_per_hour, days_per_month
)

# AI system
one_time_cost = 400000
monthly_ai_cost = 45000 + 15000

annual_ai = ai_cost_model(one_time_cost, monthly_ai_cost)

# ROI
roi, savings, payback = calculate_roi(
    annual_manual,
    annual_ai,
    one_time_cost,
    monthly_manual,
    monthly_ai_cost
)

# Export Excel
excel_data = {
    "Manual Annual Cost": [annual_manual],
    "AI Annual Cost": [annual_ai],
    "Savings": [savings],
    "ROI %": [roi],
    "Payback (months)": [payback]
}

export_excel(excel_data, "outputs/AI_ROI_Calculator.xlsx")

# Scenarios
scenario_df = run_scenarios(annual_manual, one_time_cost)
print("\nScenario Analysis:")
print(scenario_df)

# Business report
summary = f"""
AI ROI ANALYSIS – DOCUMENT PROCESSING

Manual annual cost: ₹{annual_manual:,.0f}
AI system annual cost: ₹{annual_ai:,.0f}

Annual savings: ₹{savings:,.0f}
ROI: {roi:.2f}%
Payback period: {payback:.1f} months

Conclusion:
AI automation is financially viable with strong cost recovery within first year.
"""

export_report(summary, "outputs/business_report.txt")

print(summary)
