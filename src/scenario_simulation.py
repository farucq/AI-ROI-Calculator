import pandas as pd

def run_scenarios(annual_manual_cost, one_time_cost):
    scenarios = {
        "Best": {"ai_monthly": 50000, "efficiency_gain": 0.9},
        "Expected": {"ai_monthly": 60000, "efficiency_gain": 0.75},
        "Worst": {"ai_monthly": 75000, "efficiency_gain": 0.6},
    }

    results = []

    for name, s in scenarios.items():
        ai_cost = s["ai_monthly"] * 12 + one_time_cost
        effective_manual = annual_manual_cost * s["efficiency_gain"]
        roi_val = ((effective_manual - ai_cost) / ai_cost) * 100
        results.append([name, round(ai_cost), round(roi_val, 2)])

    return pd.DataFrame(results, columns=["Scenario", "Annual AI Cost", "ROI %"])
