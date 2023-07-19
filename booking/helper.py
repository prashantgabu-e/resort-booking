from datetime import datetime, timedelta

def get_dates_between(start_date, end_date):
    # start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    # end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
    num_days = (end_date - start_date).days
    dates_between = [start_date + timedelta(days=i) for i in range(num_days + 1)]
    dates_between_str = [date.strftime("%Y-%m-%d") for date in dates_between]
    return dates_between_str
