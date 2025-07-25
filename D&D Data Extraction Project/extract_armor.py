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

    # Step 4: Initialize variables
    data = []
    current_category = ""

    # Step 5: Loop through all table rows
    for row in all_rows:
        cols = row.find_all("td")

        # Category row (e.g., "Light Armor")
        if len(cols) == 1:
            em = cols[0].find("em")
            if em:
                current_category = em.text.strip()

        # Armor row
        elif len(cols) == 6:
            link_tag = cols[0].find("a")
            if link_tag:
                armor_name = link_tag.get_text(strip=True)
                armor_href = link_tag["href"]
                armor_url = f"https://www.dndbeyond.com{armor_href}"
            else:
                armor_name = cols[0].get_text(strip=True)
                armor_url = ""

            data.append({
                "Category": current_category,
                "Name": armor_name,
                "Armor Class (AC)": cols[1].get_text(strip=True),
                "Strength": cols[2].get_text(strip=True),
                "Stealth": cols[3].get_text(strip=True),
                "Weight": cols[4].get_text(strip=True),
                "Cost": cols[5].get_text(strip=True),
                "URL": armor_url
            })

    # Clean up the Category names
    for entry in data:
        entry["Category"] = re.sub(r"\s*\(.*?\)", "", entry["Category"]).strip()
        entry["Category"] = entry["Category"].removesuffix(" Armor")

    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv("./data_tables/armor_table.csv", index=False, encoding="utf-8-sig")
    print("✅ Armor data extraction complete with", len(df), "rows. Data saved to armor_table.csv.")

if __name__ == "__main__":
    run()
