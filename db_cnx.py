import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError


# Initialize connection.
conn = streamlit.connection("snowflake")

# Perform query.
df = conn.query("SELECT * from PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST;", ttl=600)

# Print results.
st.write(df)

# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
# my_data_row = my_cur.fetchone()
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
