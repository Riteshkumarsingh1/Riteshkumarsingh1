import datetime
import platform

# Apni birthday yahan daalo (Year, Month, Day)
birth_date = datetime.date(2004, 1, 1) 
today = datetime.date.today()
uptime_days = (today - birth_date).days

# Aapka OS (Ye system se detect hoga ya aap manually bhi likh sakte ho)
os_name = "Windows 10 / Linux"

# README ka terminal block yahan generate hoga
content = f"""
OS: {os_name}
Uptime: {uptime_days} days
Kernel: CAM Operator
IDE: VSCode 1.96.0
Languages: Java, Python, JavaScript
...
"""
# Ab ye content README.md mein write karo
# with open("README.md", "w") as f:
#     f.write(content)
