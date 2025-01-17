import streamlit as st
import plotly.express as px

# List of countries at war with Switzerland
countries_at_war_with_switzerland = [
    "France", "Austria", "Italy", "Germany", "Spain", "Netherlands", "Sweden",
    "Russia", "Portugal", "Turkey"
]

# Manually defined latitude and longitude for countries
coordinates = {
    "France": (46.603354, 1.888334),
    "Austria": (47.516231, 13.550072),
    "Italy": (41.87194, 12.56738),
    "Germany": (51.165691, 10.451526),
    "Spain": (40.463667, -3.74922),
    "Netherlands": (52.3676, 4.9041),
    "Sweden": (60.128161, 18.643501),
    "Russia": (55.7558, 37.6176),  # Moscow coordinates
    "Portugal": (39.399872, -8.224454),  # Lisbon coordinates
    "Turkey": (38.963745, 35.243322),  # Coordinates for Turkey (Ankara)
}

# Create the map using Plotly Express
fig = px.choropleth(locations=countries_at_war_with_switzerland, 
                    color=['Yes'] * len(countries_at_war_with_switzerland), 
                    locationmode='country names', 
                    title='Countries that Have Been at War with Switzerland')

# Add annotations (country names) to the map
annotations = []
for country in countries_at_war_with_switzerland:
    lat, lon = coordinates[country]  # Get the latitude and longitude of the country
    annotations.append(
        dict(
            x=lon,
            y=lat,
            text=country,  # Country name
            showarrow=False,  # No arrow
            font=dict(size=10, color='black'),  # Font size and color
            align='center'
        )
    )

# Add the annotations to the map
fig.update_layout(annotations=annotations)

# Streamlit app
st.title('Interactive Map of Countries at War with Switzerland')
st.plotly_chart(fig)
