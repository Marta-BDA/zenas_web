
import streamlit
streamlit.title ('Zenas catalog')
import snowflake.connector

snowflake_credentials = st.secrets["snowflake"]
my_cnx = snowflake.connector.connect(**snowflake_credentials)
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
