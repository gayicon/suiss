import streamlit as st
import plotly.express as px

# Expanded list of countries that have been at war with Switzerland
countries_at_war_with_switzerland = [
    "France", "Austria", "Italy", "Germany", "Spain", "Netherlands", "Sweden"
]

# Create a dictionary with country names and war status
countries_data = {
    'Country': countries_at_war_with_switzerland,
    'War with Switzerland': ['Yes'] * len(countries_at_war_with_switzerland)
}

# Create the map using Plotly Express
fig = px.choropleth(locations=countries_data['Country'], 
                    color=countries_data['War with Switzerland'], 
                    locationmode='country names', 
                    title='Countries that Have Been at War with Switzerland',
                    hover_name=countries_data['Country'])  # Add country names on hover

# Add country names as labels
fig.update_geos(showcoastlines=True, coastlinecolor="Black", projection_type="mercator")
fig.update_traces(text=countries_data['Country'], textposition="top center", marker=dict(line=dict(width=0)))

# Streamlit app
st.title('Interactive Map of Countries at War with Switzerland')
st.plotly_chart(fig)
