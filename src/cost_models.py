def manual_cost_model(employees, hours_per_day, cost_per_hour, days_per_month):
    monthly = employees * hours_per_day * cost_per_hour * days_per_month
    annual = monthly * 12
    return monthly, annual


def ai_cost_model(one_time_cost, monthly_ai_cost):
    annual = monthly_ai_cost * 12 + one_time_cost
    return annual
