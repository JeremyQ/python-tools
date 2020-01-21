import pandas as pd
from pandas.tseries.holiday import USFederalHolidayCalendar as holidayCal


def create_date_dim(holidays, start, end):
  df = pd.DataFrame({"date": pd.date_range(start, end)})
  df["day"] = df.date.dt.day
  df["week"] = df.date.dt.weekofyear
  df["month"] = df.date.dt.month
  df["quarter"] = df.date.dt.quarter
  df["year"] = df.date.dt.year
  df["day_name"] = df.date.dt.weekday_name
  df["month_name"] =  df.date.dt.month_name()
  df["is_weekend"] = df.date.dt.dayofweek.isin([5,6])
  df["is_holiday"] = df["date"].isin(holidays) 
  df.insert(0, 'date_key', (df.year.astype(str) + df.month.astype(str).str.zfill(2) \
            + df.day.astype(str).str.zfill(2)).astype(int))
  return df


def write_df_to_csv(df):
  df.to_csv('/Users/jeremyquesada/src/python/data/date_dim.csv', index=None, header=True)


if __name__ == "__main__":
  start = '1900-01-01'
  end = '2100-12-31'
  cal = holidayCal()
  holidays = cal.holidays(start=start,end=end)
  write_df_to_csv(create_date_dim(holidays, start, end))
