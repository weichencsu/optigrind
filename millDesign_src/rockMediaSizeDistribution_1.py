import os
import pandas as pd
import numpy as np
import glob
import time
from datetime import datetime

import plotly.graph_objs as go
from plotly.subplots import make_subplots
from PIL import Image

from IPython.display import HTML
from scipy.signal import savgol_filter


def main():

    df = pd.read_csv('rockMediaSizeDistribution.csv')

    x1 = df["Rock_Size_[mm]"]
    y1 = df["Cumulative_Rock_Fraction_[%]"]

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=x1, y=y1, name="spline",
                    line_shape='spline',
                    line=dict(color='royalblue', width=4),
                    marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                    
                )
    )

    # Update xaxis properties
    fig1.update_layout(
            xaxis_title="Size - [mm]",
            yaxis_title="Percent Finer - [%]",
            xaxis_range=[0, 250],
            yaxis_range=[0, 100],
            showlegend=False,
            #paper_bgcolor="rgb(0,0,0,0)",
            font=dict(
                family="Ubuntu, regular",
                size=10,
                color="Black"
        )
    )

    fig1.update_layout(
        margin=dict(l=1, r=1, t=1, b=1)
        #paper_bgcolor="LightSteelBlue",
    )

    x2 = df["Media_Size_[mm]"]
    y2 = df["Media_Fraction_[%]"]


    fig2 = go.Figure()
    fig2.add_trace(go.Bar(x=x2, y=y2, name="media_size_distribution",
                    #line_shape='spline',
                    #line=dict(color='royalblue', width=4),
                    marker_color='rgb(26, 118, 255)'
                )
    )

    # Update xaxis properties
    fig2.update_layout(
            xaxis_title="Size - [mm]",
            yaxis_title="Percent - [%]",
            #xaxis_range=[0, 200],
            yaxis_range=[0, 100],
            showlegend=False,
            #paper_bgcolor="rgb(0,0,0,0)",
            font=dict(
                family="Ubuntu, regular",
                size=10,
                color="Black"
        )
    )

    fig2.update_layout(
        margin=dict(l=1, r=1, t=1, b=1),
        #paper_bgcolor="LightSteelBlue",
    )


    fig1.write_html("rockSD.html")
    fig2.write_html("mediaSD.html")
    ##divs = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    #f_dev = open('millDataSheet.div', 'w')
    #f_dev.write(divs)
    #f_dev.close()


if __name__ == "__main__":
    main()

