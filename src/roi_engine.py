def calculate_roi(manual_annual, ai_annual, one_time_cost, manual_monthly, ai_monthly):
    savings = manual_annual - ai_annual
    roi = (savings / ai_annual) * 100
    payback = one_time_cost / (manual_monthly - ai_monthly)

    return roi, savings, payback
