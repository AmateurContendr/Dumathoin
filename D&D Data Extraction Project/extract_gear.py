from bs4 import BeautifulSoup
import pandas as pd
import re

def run():
    # Load HTML
    with open("./2024 PHB Data/ch6_equipment.html", "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Find the gear table
    gear_table = soup.find("h3", id="AdventuringGearTable").find_parent("table")
    all_rows = gear_table.find_all("tr")

    data = []
    current_category = ""

    for row in all_rows:
        cols = row.find_all("td")

        # Category row (like "Ammunition")
        if len(cols) == 1:
            em = cols[0].find("em")
            if em:
                current_category = em.get_text(strip=True)

        # Data row (3 columns: Name, Weight, Cost)
        elif len(cols) == 3:
            # Extract name and link
            link_tag = cols[0].find("a")
            if link_tag:
                name = link_tag.get_text(strip=True)
                url = f"https://www.dndbeyond.com{link_tag['href']}"
            else:
                name = cols[0].get_text(strip=True)
                url = ""

            data.append({
                "Category": current_category,
                "Name": name,
                "Weight": cols[1].get_text(strip=True),
                "Cost": cols[2].get_text(strip=True),
                "URL": url
            })

    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv("./data_tables/gear_table.csv", index=False, encoding="utf-8-sig")
    print("✅ Gear data extraction complete with", len(df), "rows. Data saved to gear_table.csv.")

if __name__ == "__main__":
    run()
