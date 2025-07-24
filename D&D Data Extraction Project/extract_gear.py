from bs4 import BeautifulSoup
import pandas as pd
import re

def run():
    # Load HTML
    with open("./2024 PHB Data/ch6_equipment.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Step 2: Find the coin table by heading ID
    coin_table = soup.find("h3", id="AdventuringGearTable").find_parent("table")

    # Step 3: Find all rows just in that table
    rows = coin_table.find_all("tr")

    # Step 4: Extract the data
    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) == 3:
            data.append({
                "Item": cols[0].get_text(strip=True),
                "Weight": cols[1].get_text(strip=True),
                "Cost (GP)": cols[2].get_text(strip=True)
            })
        print(row)

    # Step 5: Convert and save
    df = pd.DataFrame(data)
    df.to_csv("./data_tables/gear_table.csv", index=False, encoding="utf-8-sig")

    print("✅ Gear data extraction complete.")

if __name__ == "__main__":
    run()