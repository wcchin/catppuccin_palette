
Quick access for catppuccin colors as a seaborn palette

depends on: catppuccin-matplotlib and seaborn

Usage:

```python
from catppuccin_palette import catppuccin as cpc

cpc.color_palette(cat='latte')
cpc.color_palette(cat='frappe')
cpc.color_palette(cat='macchiato')
cpc.color_palette(cat='mocha')  # default

cpc.gray_palette(cat='latte', n=5)
cpc.gray_palette(cat='frappe', n=5)
cpc.gray_palette(cat='macchiato', n=5)
cpc.gray_palette(cat='mocha', n=5)
cpc.gray_palette(cat='mocha', n=2)  # default

```
