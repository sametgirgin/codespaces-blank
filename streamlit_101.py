import streamlit as st

st.title("Henry Hub Gas Price 2005-2024")

# Import matplotlib.pyplot with alias plt
import pandas as pd
import requests
import numpy as np
@st.cache_data
def fetch_henry_hub():
    import requests
    import pandas as pd
    import matplotlib.pyplot as plt

    # Replace 'YOUR_API_KEY' with your actual API key
    api_key = 'kWuSgOkckExQKmklnYjNgrbadIlKtZLzfIrWiXTR'
    series_id = 'frequency=weekly&data[0]=value&start=2000-01-02&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000'  # Example series ID for WTI crude oil prices
    url = f'https://api.eia.gov/v2/natural-gas/pri/fut/data/?api_key={api_key}&' + series_id

    response = requests.get(url)
    data = response.json()
    df = pd.json_normalize(data['response']['data'])
    df['period'] = pd.to_datetime(df['period'])
    #df.set_index('period', inplace=True)
    return df

#def load_data():
 #   return pd.read_csv('https://raw.githubusercontent.com/kzavrazhnyi/pythonthefirst/master/avocados_2016.csv')

st.header("Henry Hub Natural Gas Spot Price (Dollars per Million Btu)")
st.write("'st.data_editor' allow us to display and edit the dataset")

henry_hub = fetch_henry_hub()
#henry_hub_values = pd.DataFrame(henry_hub["value"])
st.line_chart(henry_hub, x="period", y="value", color="#ffaa0088")
#st.bar_chart(henry_hub["value"])
