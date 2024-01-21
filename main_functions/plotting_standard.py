import plotly.graph_objects as ply
import datetime
import os

os.sys.path.append('./')
import main_functions.format_yahoo as fy

def candle_plot(data, meta = None,title = None, xtitle = None, ytitle = None, colors = None):
    """Plotting candle plot

    Args:
        data (_type_): full_data from format_yahoo
        meta (_type_, optional): meta_data from format_yahoo, contains ticker name and stuff. Defaults to None.
        title (_type_, optional):  will be title name if passed, else will be ticker name and dates. Defaults to None.
        xtitle (_type_, optional): will be xtitle name if passed, else will be 'Date'. Defaults to None.
        ytitle (_type_, optional): will be ytitle name if passed, else will be 'Price'. Defaults to None.

    Returns:
        fig: plotly figure
    """

    # Chose ply because of integrated interactability (slide window and cool colors)

    plotly_data = [ply.Candlestick(
        x = data.index,
        open= data['Open'],
        high= data['High'],
        low= data['Low'],
        close= data['Close'],
        name = f'{meta['Ticker']} Stock Data'
    )]

    fig = ply.Figure(data = plotly_data)
    

    # making my plot look cool because cant fool around
    # with stock data with ugly looking plots, that makes it so much worse
    if not colors:
        bg = 'black'
        text = 'green'
        grid = 'green'
    else:
        bg = colors['bg']
        text = colors['text']
        grid = colors['grid']

    layout_dict = {'paper_bgcolor': bg,
                   'plot_bgcolor': bg,
                   
                   'title': {'font': {'color' : text}},
                   'xaxis_title':{'font': {'color' : text}},
                   'yaxis_title':{'font': {'color' : text}},

                   # green grids is mega cool
                   'xaxis' : {
                                'gridcolor': grid,
                                'tickfont': {'color': grid}
                                },

                   'yaxis' : {
                                'gridcolor': grid,
                                'tickfont': {'color': grid}
                                },

                    # only shows if more than one type of data (more than candlestick)
                    'legend': {
                                'bordercolor': 'green',
                                'borderwidth': 1,
                                'font': {'color': text}
                                }

                   }
    
    if title:
        layout_dict['title']['text'] = title
    else:
        layout_dict['title']['text'] = f'{meta['Ticker']} stock from {datetime.date.strftime(meta['Start'], '%b/%y')} to {datetime.date.strftime(meta['End'], '%b/%y')}'
    
    if xtitle:
        layout_dict['xaxis_title']['text'] = xtitle
    else:
        layout_dict['xaxis_title']['text'] = 'Date'


    if ytitle:
        layout_dict['yaxis_title']['text'] = ytitle
    else:
        layout_dict['yaxis_title']['text'] = 'Price'

    fig.update_layout(layout_dict)

    return fig


if __name__ == '__main__':
    data, meta = fy.format_yahoo('AAPL', period= '1y')
    fig = candle_plot(data, meta)
    fig.show()
    
