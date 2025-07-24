# main.py
from extract_coins import run as coins_run
from extract_weapons import run as weapons_run
from extract_armor import run as armor_run
from extract_tools import run as tools_run

def main():
    coins_run()
    weapons_run()
    armor_run()
    tools_run()
    print("✅ All extracts done.")

if __name__ == "__main__":
    main()
