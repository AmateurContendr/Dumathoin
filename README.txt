DUMATHOIN – D&D EQUIPMENT DATA EXTRACTION

Dumathoin is a small Python project designed to parse the Equipment chapter of the 2024 Dungeons & Dragons Player’s Handbook and turn it into machine-readable tables. The generated data can then be fed into a database to power loot tables, shop inventories or other in‑game tools.

This is project is dependant on the html file from the Equipment chapter of the Player Handbook on D&D Beyond.
URL: https://www.dndbeyond.com/sources/dnd/phb-2024/equipment#Equipment

Overview:
The project expects a local copy of the equipment chapter’s HTML (downloaded from D&D Beyond) and extracts several tables from it:

- Coins – values for different coin denominations.
- Armor – categories (light, medium, heavy) and individual armor entries with AC, strength requirements, stealth disadvantage, weight and cost.
- Weapons – weapon categories (simple melee, simple ranged, martial melee, martial ranged), damage, properties, mastery, weight and cost.
- Adventuring gear – miscellaneous gear items with weight and cost.
- Tools – tools and kits with cost, weight and any special abilities or variants.

Each extractor lives in the directory “D&D Data Extraction Project” and can be run independently. The convenience script “extract_all.py” orchestrates all of them so you can generate every CSV in one command. Outputs are written to the folder “data_tables”.

Project structure:

- 2024 PHB Data/ – contains the input HTML file (ch6_equipment.html). You must download this from D&D Beyond and place it here manually.
- D&D Data Extraction Project/extract_all.py – runs every extractor sequentially.
- D&D Data Extraction Project/extract_coins.py – parses the Coin Values table and writes coins_table.csv.
- D&D Data Extraction Project/extract_armor.py – reads the Armor Table, keeps track of category headers and outputs armor_table.csv.
- D&D Data Extraction Project/extract_weapons.py – extracts the Weapons Table and writes weapons_table.csv.
- D&D Data Extraction Project/extract_gear.py – parses the Adventuring Gear Table to produce gear_table.csv.
- D&D Data Extraction Project/extract_tools.py – walks the Tools section, capturing tool names, cost, weight and variants into tools_table.csv.
- data_tables/ – destination for generated CSVs.

Requirements:

This project uses Python 3 and the following libraries:

- beautifulsoup4 – for parsing HTML
- pandas – for building and exporting data frames

Install them via pip:

python3 -m pip install beautifulsoup4 pandas

Usage:

1. Download the HTML file. Navigate to the Equipment chapter at D&D Beyond and save the page as ch6_equipment.html into the “2024 PHB Data” directory.
2. Run the extraction script. Execute the following command from the repository root:

python3 "D&D Data Extraction Project/extract_all.py"

The script will parse the HTML and generate CSV files in the “data_tables” folder. Each extractor prints progress messages and the number of rows written.

You can also run individual extractors if you only need a subset of the data:

python3 "D&D Data Extraction Project/extract_armor.py"

Caveats and legal notice:

The data extracted originates from the Dungeons & Dragons Player’s Handbook (2024). These materials are owned by Wizards of the Coast LLC. This project is provided for personal use and learning; redistribute or publish extracted data only in accordance with the book’s license and terms of service.

License:

This repository doesn’t currently include an explicit license. If you plan to extend or redistribute the code, consider adding an open‑source license (for example, MIT) and ensure your use complies with Wizards of the Coast’s policies.
