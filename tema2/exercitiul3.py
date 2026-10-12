import pandas as pd

date = pd.DataFrame({
    "Dificultate": ["Usor", "Usor", "Greu", "Greu"],
    "Metoda": ["A", "B", "A", "B"],
    "Promovati": [72, 9, 2, 27],
    "Evaluati": [90, 10, 10, 90]
})


date["Rata (%)"] = date["Promovati"] / date["Evaluati"] * 100

print("Ratele separate:")
print(date)


totaluri = date.groupby("Metoda")[["Promovati", "Evaluati"]].sum()

totaluri["Rata (%)"] = (
    totaluri["Promovati"] / totaluri["Evaluati"] * 100
)

print("\nRatele globale:")
print(totaluri)