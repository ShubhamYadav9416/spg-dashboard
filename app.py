import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from io import StringIO

# Define the CSV data
data = """
Team Members,EXTROVERTED,INTROVERTED,INTUITIVE,OBSERVANT,THINKING,FEELING,JUDGING,PROSPECTING,ASSERTIVE,TURBULENT
Ashish,17,83,65,35,23,77,35,65,36,64
Mukesh,28,72,69,31,61,39,56,44,56,44
Nikhil,47,53,73,27,48,52,46,54,36,64
Shubham,66,34,59,41,46,54,47,53,51,49
Yukti,61,39,51,49,25,75,90,10,33,67
"""

# Create a DataFrame from the CSV data
df = pd.read_csv(StringIO(data))

# Streamlit app
st.title("Personality Traits Analysis")

# Dropdown menu to select team member
selected_team_member = st.selectbox("Select Team Member:", df["Team Members"])

# Filter data based on the selected team member
selected_data = df[df["Team Members"] == selected_team_member].squeeze()

# Create a bar chart using Plotly
fig = go.Figure()

for i, trait in enumerate(selected_data.index[1:]):
    fig.add_trace(go.Bar(
        x=[trait],
        y=[selected_data[trait]],
        name=trait,
        marker=dict(color=f'rgba({i * 30}, 50, 190, 0.7)'),  # Adjust color
        text=[f'{selected_data[trait]}'],
        textposition='auto',
    ))

fig.update_layout(
    title=f"Personality Traits for {selected_team_member}",
    xaxis=dict(title="Traits"),
    yaxis=dict(title="Values"),
    barmode='group'
)

# Display brief descriptions of each personality trait
trait_descriptions = {
    "EXTROVERTED": "😄 Extroverted individuals are outgoing, energetic, and enthusiastic. They enjoy social interactions and thrive in group settings.",
    "INTROVERTED": "🤫 Introverted individuals are reserved, quiet, and thoughtful. They prefer solitary activities and find social interactions draining.",
    "INTUITIVE": "🧠 Intuitive individuals rely on gut feelings, instincts, and imagination. They focus on possibilities and the future.",
    "OBSERVANT": "👀 Observant individuals notice and focus on physical details. They are attentive to their surroundings and notice small changes.",
    "THINKING": "🤔 Thinking individuals make decisions based on logic, analysis, and reason. They are objective and value fairness in decision-making.",
    "FEELING": "❤️ Feeling individuals make decisions based on emotions, values, and personal beliefs. They consider the impact on others and seek harmony.",
    "JUDGING": "🗂️ Judging individuals are organized, structured, and decisive. They prefer clear plans and order in their lives.",
    "PROSPECTING": "🔄 Prospecting individuals are adaptable, spontaneous, and flexible. They enjoy new experiences and prefer to go with the flow.",
    "ASSERTIVE": "💪 Assertive individuals are confident, self-assured, and proactive. They are comfortable taking charge and making decisions.",
    "TURBULENT": "😰 Turbulent individuals are emotionally sensitive, self-conscious, and prone to self-doubt. They may experience higher levels of stress and anxiety."
}

st.plotly_chart(fig)

# Display trait descriptions with emojis and expanded descriptions
st.header("Trait Descriptions")
for trait, description in trait_descriptions.items():
    st.write(f"**{trait}** : {description}")
