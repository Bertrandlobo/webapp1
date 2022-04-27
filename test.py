#!/usr/bin/env python
# coding: utf-8

# In[8]:


import yfinance as yf
import streamlit as st


st.write("""# Stock Price and Volume of Chevron Corporation after Russias invasion of Ukraine""")
tickersymbol = 'CVX'
tickerdata = yf.Ticker(tickersymbol) 
data = tickerdata.history(Period='', start='2022-02-01', end='2022-03-15')



st.write("""## Opening Price""")
st.line_chart(data.Open)
st.write("""## Closing Price""")
st.line_chart(data.Close)
st.write("""## Volume""")
st.line_chart(data.Volume)




# In[ ]:





# In[ ]:





# In[9]:


data


# In[ ]:




