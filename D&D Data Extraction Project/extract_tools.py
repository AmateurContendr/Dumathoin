from bs4 import BeautifulSoup
import pandas as pd
import re

def run():

    path = "./2024 PHB Data/ch6_equipment.html"
    with open(path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    tools_h2 = soup.find("h2", id="Tools")
    # collect nodes until the next h2
    section_nodes = []
    for el in tools_h2.next_siblings:
        if getattr(el, "name", None) == "h2":
            break
        section_nodes.append(el)

    rows = []
    current_category = ""
    for node in section_nodes:
        if getattr(node, "name", None) == "h3":
            current_category = node.get_text(strip=True)
        if getattr(node, "name", None) == "h4":
            # Extract name, cost, and optional link
            full = node.get_text(" ", strip=True)
            m = re.match(r"^(.*?)(?:\s*\(([^)]*)\))?$", full)  # name (cost)
            name = m.group(1).strip()
            cost = (m.group(2) or "").strip()

            # Get URL if there's a link
            link_tag = node.find("a")
            url = f"https://www.dndbeyond.com{link_tag['href']}" if link_tag else ""


            # walk forward until next h4/hr/h3 to gather <p> blocks
            p = node.next_sibling
            fields = {"Ability": "", "Weight": "", "Utilize": "", "Craft": "", "Variants": ""}
            while p and not (getattr(p, "name", None) in {"h4", "h3"}):
                if getattr(p, "name", None) == "p":
                    # grab the first <strong> tag text as the field name
                    strong = p.find("strong")
                    if strong:
                        key = strong.get_text(strip=True).rstrip(":")
                        val = p.get_text(" ", strip=True)
                        val = re.sub(rf"^{key}:\s*", "", val)  # drop the leading label
                        # split Ability/Weight line
                        if key == "Ability":
                            a = re.search(r"Ability:\s*([^<]+?)(?=\s+Weight:|$)", p.get_text(" ", strip=True))
                            w = re.search(r"Weight:\s*([^<]+)", p.get_text(" ", strip=True))
                            fields["Ability"] = a.group(1).strip() if a else ""
                            fields["Weight"]  = w.group(1).strip() if w else ""
                        else:
                            fields[key] = val
                p = p.next_sibling

            rows.append({
                "Category": current_category,
                "Name": name,
                "Cost": cost,
                "URL": url,
                **fields
            })


    df = pd.DataFrame(rows)
    df.to_csv("./data_tables/tools_table.csv", index=False, encoding="utf-8-sig")

    print("✅ Tool data extraction complete with", len(df), "rows. Data saved to tools_table.csv.")

if __name__ == "__main__":
    run()