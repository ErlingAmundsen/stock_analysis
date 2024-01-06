import plotly.graph_objects as ply
import datetime

import format_yahoo as fy

def candle_plot(data, meta = None,title = None, xtitle = None, ytitle = None):
    

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
    bg = 'black'
    text = 'green'
    grid = 'green'
  

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
    