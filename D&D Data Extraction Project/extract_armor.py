from bs4 import BeautifulSoup
import pandas as pd
import re

def run():
    # Load HTML
    with open("./2024 PHB Data/ch6_equipment.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Step 2: Find the armor table by heading ID
    armor_table = soup.find("h3", id="ArmorTable").find_parent("table")

    # Step 3: Find all rows just in that table
    all_rows = armor_table.find_all("tr")


    # Step 3: Initialize variables
    data = []
    current_category = ""

    # Step 4: Loop through all table rows
    for row in all_rows:
        cols = row.find_all("td")

        # Check if it's a category row (like "Light Armor")
        if len(cols) == 1:
            em = cols[0].find("em")
            if em:
                current_category = em.text.strip()

        # If it’s an armor row (6 columns), extract the data
        elif len(cols) == 6:
            data.append({
                "Category": current_category,
                "Name": cols[0].get_text(strip=True),
                "Armor Class (AC)": cols[1].get_text(strip=True),
                "Strength": cols[2].get_text(strip=True),
                "Stealth": cols[3].get_text(strip=True),
                "Weight": cols[4].get_text(strip=True),
                "Cost": cols[5].get_text(strip=True),
            })

    # Clean up the Category names
    for entry in data:
        # Remove anything in parentheses
        entry["Category"] = re.sub(r"\s*\(.*?\)", "", entry["Category"]).strip()
        # Remove " Armor" from the end
        entry["Category"] = entry["Category"].removesuffix(" Armor")

    # Step 5: Convert to a pandas DataFrame
    df = pd.DataFrame(data)

    # Step 6: Save the output to CSV
    df.to_csv("./data_tables/armor_table.csv", index=False, encoding="utf-8-sig")

    print("✅ Armor data extraction complete with", len(df), "rows. Data saved to armor_table.csv.")

if __name__ == "__main__":
    run()