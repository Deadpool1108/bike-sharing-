import pandas as pd
from datetime import datetime
from streamlit import st

url = "https://storage.googleapis.com/scsu-data-science/bike_sharing.csv"
df = pd.read_csv(url)

df["date"] = pd.to_datetime(df["dteday"], format="%Y-%m-%d")


def rolling_average(data, window):
  return data.rolling(window=window).mean()


st.title("Bike Sharing Ridership Analysis")
st.header("Exploring ridership patterns")


st.subheader("Total Ridership Over Time")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df["date"], df["cnt"])
ax.set_xlabel("Date")
ax.set_ylabel("Total Ridership")
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m"))
plt.xticks(rotation=45)
st.pyplot(fig)


st.subheader("Total Ridership by Season")
season_counts = df["cnt"].groupby(df["season"]).sum().reset_index()
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(season_counts["season"], season_counts["cnt"])
ax.set_xlabel("Season")
ax.set_ylabel("Total Ridership")
st.pyplot(fig)


st.subheader("Ridership Over Time with Rolling Average")
rolling_window = st.radio("Select Rolling Average Window", (7, 14))
average_data = rolling_average(df["cnt"], rolling_window)

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df["date"], df["cnt"], label="Daily Ridership")
ax.plot(df["date"], average_data, label=f"{rolling_window}-Day Average")
ax.set_xlabel("Date")
ax.set_ylabel("Ridership")
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter("%Y-%m"))
plt.xticks(rotation=45)
ax.legend()
st.pyplot(fig)
