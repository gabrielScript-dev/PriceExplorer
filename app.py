import streamlit
from plot.interactive import plot_line_i

streamlit.title('Price Explorer App')

# Sidebar
symbol = streamlit.sidebar.text_input('Escolha um ativo:', 'AAPL')

# Plot
fig = plot_line_i(symbol)
streamlit.plotly_chart(fig)