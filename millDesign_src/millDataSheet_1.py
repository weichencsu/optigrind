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

    df = pd.read_csv('millDataSheet.csv')

    fig = go.Figure(data=[go.Table(
                    #columnorder = [1,2],
                    #columnwidth = [100,400],
                    header = dict(
                        values = list(df.columns),
                        line_color='darkslategray',
                        fill_color='royalblue',
                        align=['center','center'],
                        font=dict(color='white', size=10),
                        height=40
                ),
                    cells=dict(
                        values=[df.Mill_Property, df.Value, df.Description],
                        line_color='darkslategray',
                        fill=dict(color=['paleturquoise', 'white']),
                        align=['left', 'center'],
                        font_size=10,
                        height=30)
        )
    ])

    # Update xaxis properties
    """
    fig.update_layout(
        title={'text': "江西耐普 - 智能耐磨监测 - 泗洲-2#-NZJA300泵前护板",
                'y':0.975,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            #xaxis_title="时间",
            #yaxis_title="前护板剩余厚度 - [mm]",
            #yaxis_range=[0, 80],
            showlegend=False,
            #paper_bgcolor="rgb(0,0,0,0)",
            font=dict(
                family="Microsoft YaHei UI, regular",
                size=14,
                color="Black"
        )
    )
    """
    fig.update_layout(
        margin=dict(l=1, r=1, t=1, b=1),
        font=dict(
                family="Ubuntu, regular",
                size=10
        )
        #paper_bgcolor="LightSteelBlue",
    )




    fig.write_html("millDataSheet.html")
    ##divs = plotly.offline.plot(fig, include_plotlyjs=False, output_type='div')
    #f_dev = open('millDataSheet.div', 'w')
    #f_dev.write(divs)
    #f_dev.close()


if __name__ == "__main__":
    main()

