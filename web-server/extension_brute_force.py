import requests
from prettytable import PrettyTable
from prettytable.colortable import ColorTable, Themes

# First install PrettyTable and requests
# python3 -m pip install prettytable or apt install python3-prettytable
# python3 -m pip install requests or apt install python3-requests
# https://pypi.org/project/prettytable/
# https://pypi.org/project/requests/

# Timeout for requests
TIMEOUT = 5

# Base URL
base_url = "http://challenge01.root-me.org/web-serveur/ch11/index.php"

# Comprehensive extension list
backup_extensions = [
    "~", ".bak", ".backup", ".bkp", ".old", ".tmp", ".dmp", ".arc", ".ab",
    ".snap", ".dif", ".bkf", ".dmg", ".swp", ".swo", ".part", ".crdownload",
    ".cfg.bak", ".zip", ".tar", ".tar.gz", ".tar.bz2", ".tar.xz", ".gz",
    ".bz2", ".xz", ".7z", ".rar", ".iso", ".wim", ".dmg", ".cab", ".sql",
    ".dump", ".db", ".sqlite", ".mdb", ".accdb", ".rdb", ".ldf", ".bak",
    ".frm", ".ibd", ".cfg", ".ini", ".json", ".xml", ".yaml", ".yml",
    ".toml", ".properties", ".conf", ".log", ".err", ".out", ".enc",
    ".aes", ".gpg", ".pgp", ".crypt", ".sec", ".key", ".code-workspace",
    ".idea", ".iml", ".project", ".settings", ".classpath", ".iso", ".vhd",
    ".vhdx", ".qcow", ".qcow2", ".ova", ".vmdk", ".img", ".dmg", ".git",
    ".svn", ".hg", ".cvs", ".gitignore", ".gitattributes", ".php.bak",
    ".index.bak", ".php~", ".php.old", ".config.php", ".htaccess", ".htpasswd",
    ".env", "wp-config.php", ".autosave", ".temp", ".cache", ".retry", ".debug",
    ".test", ".bkp"
]

# Table setup
table_data = ColorTable(theme=Themes.OCEAN,padding_width=1)
table_data.field_names = ["Url payload", "Response status code"]
table_data.align["Url payload"] = "l" # align left by default is center

print("\nLooking for URLs with status code 200 or those below 400...\n")

# Process each extension
for el in backup_extensions:
    url = f"{base_url}{el}"
    try:
        response = requests.get(url, timeout=TIMEOUT)
        if response.status_code < 400:  # Filter only relevant codes
            table_data.add_row([url, response.status_code])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Sort the table by status code
table_data.sortby = "Response status code"

# Print the sorted table
print(table_data)

"""
with open("backup_fuzz_results.txt", "w") as file:
    file.write(str(table_data))
print("\nResults saved to 'backup_fuzz_results.txt'.")
"""
