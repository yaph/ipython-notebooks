# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def barh(df, value_col, filename, figsize=(10, 10), title=None, footer=None):
    fig = plt.figure(figsize=figsize)
    R = range(len(df))

    rects = plt.barh(
        R,
        df[value_col],
        height=.7,
        color='#4682B4',
        alpha=.8)

    for i, rect in enumerate(rects):
        width = rect.get_width()
        label = '  ' + str(df.values[i][0])
        plt.text(width + 0.25,
                 rect.get_y() + rect.get_height() / 2.,
                 label,
                 va='center',
                 fontsize=13,
                 color='#666666')

    # Move y ticks down a bit to align with the bars.
    ypos = [y + 0.35 for y in R]

    # Fix possible problems with unicode chars.
    labels = df.index.map(lambda x: x.decode('utf-8'))

    plt.yticks(ypos, labels)

    # Hide x tick labels.
    plt.xticks(np.arange(0, 5, 1), [''])

    # Hide borders around plot.
    ax = plt.axes()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    if title:
        plt.title(title, color='#444444')

    if footer:
        ax.text(
            df.values.max() / 2.,
            0,
            footer,
            fontsize=12.5,
            va='top',
            color='#444444')

    plt.savefig(filename, bbox_inches='tight')