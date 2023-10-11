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


### for sequential color
def catppuccin_sequential(cat, clr_base=None, clr=None):
    if (clr_base is None):
        if cat=='latte':
            clr_base = 'base'
        else:
            clr_base = 'text'
    if (clr is None):
        clr = 'blue'
    return [clr_base, clr]


def catppuccin_cmap_sequential(cat="latte", clr_base=None, clr=None):
    cmap = get_colormap_from_list(cat, catppuccin_sequential(cat, clr_base=clr_base, clr=clr))
    return cmap


def sequential_palette(cat="latte", n=None, clr_base=None, clr=None):
    if n is None:
        n = 5
    if n==2:
        cat_colors = catppuccin_sequential(cat, clr_base=clr_base, clr=clr)
        clrs = [load_color(cat, cl) for cl in cat_colors]
        colors = sns.blend_palette(clrs, n_colors=len(cat_colors))
    else:
        cmap = catppuccin_cmap_sequential(cat=cat, clr_base=clr_base, clr=clr)
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
        elif clr_set==3:
            clr1 = 'lavender'
            clr3 = 'rosewater'
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



def gen_named_cmap(cat, colors):
    cmap = get_colormap_from_list(cat, colors)
    return cmap


def gen_named_palette(cat, colors, n=10, n1=1, n2=-1):
    cmap = gen_named_cmap(cat, colors)
    m = n+abs(n1)+abs(n2)
    pal = []
    for i in range(m):
        j = i/(m-1)
        rgba = cmap(j)
        pal.append(rgba)
    #print(len(pal))
    pal = pal[n1:n2]
    pal = sns.blend_palette(pal, n_colors=n)
    return pal


def get_catppuccin_named_sequential(name, cmap=False, n=10):
    if name=='Oranges':
        cat = 'latte'
        colors = ['base', 'peach']
        n1 = 1
        n2 = -1
    elif name=='Yellows':
        cat = 'latte'
        colors = ['base', 'yellow', 'text']
        n1 = 1
        n2 = -1
    elif name=='Blues':
        cat = 'latte'
        colors = ['base', 'lavender', 'text']
        n1 = 1
        n2 = -1
    elif name=='Reds':
        cat = 'latte'
        colors = ['base', 'red']
        n1 = 1
        n2 = -1
    elif name=='Maroons':
        cat = 'latte'
        colors = ['base', 'maroon', 'text']
        n1 = 1
        n2 = -1
    elif name=='Flamingos':
        cat = 'latte'
        colors = ['base', 'flamingo', 'red']
        n1 = 1
        n2 = -2
    elif name=='Greens':
        cat = 'latte'
        colors = ['base', 'green', 'text']
        n1 = 1
        n2 = -1
    elif name=='PuBu':
        cat = 'latte'
        colors = ['base', 'pink', 'lavender', 'text']
        n1 = 1
        n2 = -2
    elif name=='Purples':
        cat = 'latte'
        colors =  ['base', 'pink', 'mauve', 'text']
        n1 = 1
        n2 = -2
    elif name=='YlOr':
        cat = 'frappe'
        colors = ['text', 'yellow', 'peach', 'base']
        n1 = 1
        n2 = -1
    elif name=='Rosewaters':
        cat = 'frappe'
        colors = ['text', 'rosewater', 'red', 'base']
        n1 = 3
        n2 = -1
    elif name=='YlOrRd':
        cat = 'macchiato'
        colors = ['subtext1', 'yellow', 'peach', 'red', 'surface1']
        n1 = 1
        n2 = -2
    elif name=='YlGnBu':
        cat = 'frappe'
        colors = ['subtext1', 'yellow', 'green', 'teal', 'blue', 'base']
        n1 = 1
        n2 = -1
    elif name=='YlGn':
        cat = 'frappe'
        colors = ['subtext1', 'yellow', 'green', 'base']
        n1 = 1
        n2 = -1
    else:
        print('Color map name not found, please check')
        cmapnames = ['Oranges', 'Yellows', 'Blues', 'Reds', 'Maroons', 'Flamingos', 'Greens', 'PuBu', 'Purples', 'YlOr', 'Rosewaters', 'YlOrRd', 'YlGnBu', 'YlGn']
        print('Current available named colormap:', ', '.join(cmapnames))
        print('Returning None')
        return None
    #print(cat, colors)
    if cmap:
        cmap = gen_named_cmap(cat, colors)
        return cmap
    else:
        pal = gen_named_palette(cat=cat, colors=colors, n=n, n1=n1, n2=n2)
    return pal

