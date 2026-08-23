import datetime
import html

# ================== APNI DETAILS YAHAN BADLO ==================
USERNAME = "YOUR_USERNAME"
DISPLAY_NAME = "your_name"
BIRTH_DATE = datetime.date(2000, 1, 1)  # Apni date of birth yahan daalo (Year, Month, Date)
OS_NAME = "Windows 10, Android 14, Linux"
HOST = "Your Company / PC Name"
KERNEL = "CAM Operator"
IDE = "IDEA 2023.3.2, VSCode 1.96.0"
LANGS_PROG = "Java, Python, JavaScript, C++"
LANGS_COMP = "HTML, CSS, JSON, LaTeX, YAML"
LANGS_REAL = "English, Spanish"
HOBBIES_SW = "Minecraft Modding, iOS Jailbreaking"
HOBBIES_HW = "Overclocking, Undervolting"
EMAIL_PERSONAL = "your_email@gmail.com"
EMAIL_WORK = "your_work_email@tech.com"
LINKEDIN = "Your.LinkedIn"
DISCORD = "your_discord"

# ASCII ART (Yahan apna ascii art paste karo, jaisa screenshot mein hai)
# Google par "ASCII art generator" daal kar apna naam generate karo.
ASCII_ART = """
g@M%@@%@@N%w,
.M*|!**%gNM=1mbt%g|%N,
p!    |!''|''|'|!|jh1j%W
.@L_          '''''!|j%M}%M
]j'   .,wp@pw,        |%Wg
./|!|@@@@@@@@@@pp.   |@@N
|@@@@@@@@@@@@@@@
.'.|@@@@@@@@@@@@@@@.
"""
# ==============================================================

# Calculate Uptime
today = datetime.date.today()
uptime_days = (today - BIRTH_DATE).days
uptime_years = uptime_days // 365
uptime_months = (uptime_days % 365) // 30
uptime_str = f"{uptime_years} years, {uptime_months} months, {uptime_days % 30} days"

# Terminal Content format karo
content = f"""
{DISPLAY_NAME}@{USERNAME} ---------------------------
OS: ........................ {OS_NAME}
Uptime: ..................... {uptime_str}
Host: ....................... {HOST}
Kernel: ..................... {KERNEL}
IDE: ........................ {IDE}

Languages.Programming: ...... {LANGS_PROG}
Languages.Computer: ......... {LANGS_COMP}
Languages.Real: ............. {LANGS_REAL}

Hobbies.Software: ........... {HOBBIES_SW}
Hobbies.Hardware: ........... {HOBBIES_HW}

- Contact -------------------
Email.Personal: ............. {EMAIL_PERSONAL}
Email.Work: ................. {EMAIL_WORK}
LinkedIn: ................... {LINKEDIN}
Discord: .................... {DISCORD}
"""

# SVG Generate karne ka function
def create_svg(text_block, dark_mode=True):
    if dark_mode:
        bg_color = "#0d1117"  # Dark background
        text_color = "#c9d1d9" # Light text
    else:
        bg_color = "#ffffff"  # Light background
        text_color = "#24292f" # Dark text
    
    # HTML entities escape karo taaki formatting na toote
    safe_text = html.escape(text_block)
    
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" width="800" height="450" viewBox="0 0 800 450">
  <rect width="100%" height="100%" fill="{bg_color}" />
  <text x="20" y="40" font-family="monospace" font-size="14" fill="{text_color}" white-space="pre">{safe_text}</text>
</svg>'''
    return svg_content

# Save Light and Dark SVG files
with open("dark_mode.svg", "w") as f:
    f.write(create_svg(content, dark_mode=True))
with open("light_mode.svg", "w") as f:
    f.write(create_svg(content, dark_mode=False))

# README.md Generate karo (ye automatically update hoga)
readme_content = f"""# {DISPLAY_NAME}

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="dark_mode.svg">
  <source media="(prefers-color-scheme: light)" srcset="light_mode.svg">
  <img alt="Terminal Profile" src="light_mode.svg">
</picture>

## About Me
I am a passionate developer specializing in {LANGS_PROG}.
"""

with open("README.md", "w") as f:
    f.write(readme_content)

print("README, dark_mode.svg aur light_mode.svg successfully update ho gaye!")
