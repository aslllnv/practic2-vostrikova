import requests
import matplotlib.pyplot as plt
import pandas as pd


def make_dataframe(hours, temps):
    df = pd.DataFrame({
        "time": pd.to_datetime(hours),
        "temperature_c": temps
    })
    return df.sort_values("time").reset_index(drop=True)


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 55.75,
    "longitude": 37.61,
    "hourly": "temperature_2m"
}

response = requests.get(url, params=params, timeout=10)
response.raise_for_status()

data = response.json()

hours = data["hourly"]["time"][:24]
temps = data["hourly"]["temperature_2m"][:24]

df = make_dataframe(hours, temps)

df.to_csv("temperature_24h.csv", index=False)

plt.plot(df["time"], df["temperature_c"], marker="o")
plt.xticks(rotation=45)
plt.title("Температура в Москве (24 часа)")
plt.xlabel("Время")
plt.ylabel("°C")
plt.tight_layout()
plt.savefig("temperature_24h.png")
plt.show()

print("Сохранено в temperature_24h.csv")
print("Сохранено в temperature_24h.png")