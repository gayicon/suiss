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
                    title='Countries that Have Been at War with Switzerland')

# Add annotations (country names) to the map
annotations = []
for country in countries_data['Country']:
    annotations.append(
        dict(
            x=fig.data[0].locationlat[countries_data['Country'].index(country)],  # Get the latitude of the country
            y=fig.data[0].locationlon[countries_data['Country'].index(country)],  # Get the longitude of the country
            text=country,  # Country name
            showarrow=False,  # Do not show an arrow
            font=dict(size=10, color='black'),  # Font size and color
            align='center'
        )
    )

# Add the annotations to the map
fig.update_layout(annotations=annotations)

# Streamlit app
st.title('Interactive Map of Countries at War with Switzerland')
st.plotly_chart(fig)
