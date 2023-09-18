"""
Quick access for catppuccin colors as a seaborn palette

based on: mplcatppuccin

Usage:

```
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

"""

import seaborn as sns
import mplcatppuccin
from mplcatppuccin.palette import load_color
from mplcatppuccin.colormaps import get_colormap_from_list


def catppuccin_colorlist():
    cat_colors = [        
        "blue", 
        "peach", 
        "green", 
        "red", 
        "mauve", 
        "flamingo", 
        "pink",
        "subtext0",
        "yellow", 
        "sapphire"
    ]
    return cat_colors


def catppuccin_grayscale():
    return ["text", "base"]


def catppuccin_cmap(cat="mocha"):
    cmap = get_colormap_from_list(cat, catppuccin_colorlist())
    return cmap


def catppuccin_cmap_gray(cat="mocha"):
    cmap = get_colormap_from_list(cat, catppuccin_grayscale())
    return cmap


def color_palette(cat="mocha", n=None):
    if n is None or n==10:
        cat_colors = catppuccin_colorlist()
        clrs = [load_color(cat, cl) for cl in cat_colors]
        colors = sns.blend_palette(clrs, n_colors=len(cat_colors))
    else:
        cmap = catppuccin_cmap(cat=cat)
        colors = []
        for i in range(n):
            j = i/(n-1)
            rgba = cmap(j)
            colors.append(rgba)
        colors = sns.blend_palette(colors, n_colors=n)
    return colors


def gray_palette(cat="mocha", n=None):
    if n is None or n==2:
        cat_colors = catppuccin_grayscale()
        clrs = [load_color(cat, cl) for cl in cat_colors]
        colors = sns.blend_palette(clrs, n_colors=len(cat_colors))
    else:
        cmap = catppuccin_cmap_gray(cat=cat)
        colors = []
        for i in range(n):
            j = i/(n-1)
            rgba = cmap(j)
            colors.append(rgba)
        colors = sns.blend_palette(colors, n_colors=n)
    return colors
