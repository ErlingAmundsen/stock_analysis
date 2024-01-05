import sys
import plotly.graph_objects as ply
import datetime

sys.path.append('./')

from main_functions import format_yahoo as fy

def candle_plot(data, meta = None,title = None, xtitle = None, ytitle = None):
    
    plotly_data = [ply.Candlestick(
        x = data.index,
        open= data['Open'],
        high= data['High'],
        low= data['Low'],
        close= data['Close']
    )]

    fig = ply.Figure(data = plotly_data)
    

    # making my plot look cool because cant fool around
    # with stock data with ugly looking plots, that makes it so much worse
    bg = 'black'
    text = 'green'
    grid = 'green'
  

    layout_dict = {'paper_bgcolor': bg,
                   'plot_bgcolor': bg,
                   
                   'title': {'title_font': text},

                   # green grids is mega cool
                   'xaxis' : {'gridcolor': grid,
                              'title_font': {'color': text},
                              'tickfont': {'color':grid}},

                   'yaxis' : {'gridcolor': grid,
                              'title_font': {'color': text},
                              'tickfont': {'color':grid}}
                
                   }
    
    if title:
        layout_dict['title'] = title
    else:
        layout_dict['title'] = f'{meta['Ticker']} stock from {datetime.date.strftime(meta['Start'], '%b/%y')} to {datetime.date.strftime(meta['End'], '%b/%y')}'
    
    if xtitle:
        layout_dict['xaxis_title'] = xtitle
    else:
        layout_dict['xaxis_title'] = 'Date'


    if ytitle:
        layout_dict['yaxis_title'] = ytitle
    else:
        layout_dict['yaxis_title'] = 'Date'

    fig.update_layout(layout_dict)

    return fig


if __name__ == '__main__':
    data, meta = fy.format_yahoo('AAPL', period= '1y')
    fig = candle_plot(data, meta)
    title = 'Title test'

    fig.show()
    
