import datetime
from dateutil.relativedelta import relativedelta

# Calculate your dynamic uptime (e.g., your birthday or when you started coding)
start_date = datetime.datetime(2005, 1, 1) # Set your own date here
now = datetime.datetime.now()
diff = relativedelta(now, start_date)

uptime_str = f'"{diff.years} years, {diff.months} months, {diff.days} days"'

# Construct your template
readme_template = f"""
```text
      .yhmnMdhyy,                 ////++         yourname@computer
   .DmmmNMMNNNNNNmmdhy.         :/+/:*....--://// ---------------------
   ,hmNNNNNNNNNNNNNNNNNddh.    /-..............:-:/ OS: "Windows 11, macOS"
  hNNNNNMMNNNNNNNNNNNNMMNNNmn  ...................  Uptime: {uptime_str}
 'hNNNNNNMMmmddddhdhhdhddmNNNN ...................  Host: "Your University"
                                                    Languages: "Python, JS, C++"
```
"""

# Overwrite README.md with the compiled content
with open("README.md", "w") as f:
    f.write(readme_template)
