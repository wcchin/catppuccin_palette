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


def catppuccin_cmap(cat="mocha"):
    cmap = get_colormap_from_list(cat, catppuccin_colorlist())
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


### for gray scale sequential
def catppuccin_grayscale():
    return ["text", "base"]


def catppuccin_cmap_gray(cat="mocha"):
    cmap = get_colormap_from_list(cat, catppuccin_grayscale())
    return cmap


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



### for diverging
def catppuccin_diverging(cat, clr_set=None, clr1=None, clr2=None, clr3=None):
    if not(clr_set is None) or (clr1 is None) or (clr2 is None) or (clr3 is None):
        if clr_set==1:
            clr1 = 'blue'
            clr3 = 'red'
            if cat=='latte':
                clr2 = 'base'
            else:
                clr2 = 'text'
        elif clr_set==2:
            clr1 = 'sapphire'
            clr3 = 'peach'
            if cat=='latte':
                clr2 = 'base'
            else:
                clr2 = 'text'
        else:
            clr1 = 'blue'
            clr3 = 'red'
            if cat=='latte':
                clr2 = 'base'
            else:
                clr2 = 'text'
        return [clr1, clr2, clr3]
    else:
        return [clr1, clr2, clr3]


def catppuccin_cmap_diverging(cat="mocha", clr_set=None, clr1=None, clr2=None, clr3=None):
    if not(clr_set is None):
        cmap = get_colormap_from_list(cat, catppuccin_diverging(cat, clr_set=clr_set))
    elif (clr1 is not None) and (clr2 is not None) and (clr3 is not None):
        cmap = get_colormap_from_list(cat, catppuccin_diverging(cat, clr_set=None, clr1=clr1, clr2=clr2, clr3=clr3))
    else:
        clr_set = 1
        cmap = get_colormap_from_list(cat, catppuccin_diverging(cat, clr_set=clr_set))
    return cmap


def diverging_palette(cat="mocha", n=None, clr_set=None, clr1=None, clr2=None, clr3=None):
    if n is None or n==3:
        cat_colors = catppuccin_diverging(cat, clr_set=clr_set, clr1=clr1, clr2=clr2, clr3=clr3)
        clrs = [load_color(cat, cl) for cl in cat_colors]
        colors = sns.blend_palette(clrs, n_colors=len(cat_colors))
    else:
        cmap = catppuccin_cmap_diverging(cat=cat, clr_set=clr_set, clr1=clr1, clr2=clr2, clr3=clr3)
        colors = []
        for i in range(n):
            j = i/(n-1)
            rgba = cmap(j)
            colors.append(rgba)
        colors = sns.blend_palette(colors, n_colors=n)
    return colors
