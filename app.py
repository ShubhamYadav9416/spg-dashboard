import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from io import StringIO
import matplotlib.pyplot as plt
# Define the CSV data
import pandas as pd
from io import StringIO
import streamlit as st
import plotly.graph_objs as go

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

st.title("Team Personality Traits Analysis")

dict_trait_pairs = {"EXTROVERTED-INTROVERTED":['INTROVERTED', 'EXTROVERTED'] ,"INTUITIVE-OBSERVANT":['INTUITIVE', 'OBSERVANT'],"THINKING-FEELING":['THINKING', 'FEELING'],"JUDGING-PROSPECTING":['JUDGING', 'PROSPECTING'],"ASSERTIVE-TURBULENT":['ASSERTIVE', 'TURBULENT']}
trait_pairs_comb = st.selectbox("Select Traits for Comparison:", list(dict_trait_pairs.keys()), key="select_traits")

if trait_pairs_comb:
    trait_pairs = dict_trait_pairs[trait_pairs_comb]
    st.write(f"You selected: {trait_pairs}")

# Ring chart for selected traits
# Ring chart for selected traits
if trait_pairs:
    st.header("Team Trait Distribution")

    # Initialize a dictionary to store the counts for each trait
    trait_counts = {trait: 0 for trait in trait_pairs}

    for trait in trait_pairs:
        # Create a data frame for trait distribution
        trait_distribution = df[trait].gt(50).sum()

        # Increment the count for the trait
        trait_counts[trait] += trait_distribution

    # Create a ring chart
    fig = go.Figure(go.Pie(
        labels=list(trait_counts.keys()),
        values=list(trait_counts.values()),  # Use the counts directly
        hole=0.4,
        pull=[0.1]*len(trait_counts)
    ))

    # Display the ring chart
    st.plotly_chart(fig)

    st.header("Dominant Traits for Each Team Member")

    # Display dominant trait for each person
    for index, row in df.iterrows():
        max_trait = max(trait_pairs, key=lambda trait: row[trait])
        st.write(f"**{row['Team Members']}**: {max_trait}")


    # Stacked bar chart for selected traits
    if trait_pairs:
        st.header("Stacked Bar Chart for Selected Traits")
    
        # Create a DataFrame with selected traits for plotting
        selected_data_plot = df.set_index('Team Members')[trait_pairs]
    
        # Create a stacked bar chart
        fig = selected_data_plot.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))
        plt.title("Selected Traits for Each Team Member")
        plt.xlabel("Team Members")
        plt.ylabel("Trait Value")
        st.pyplot(fig.figure)



# st.title("Team Dominant Personality Traits Analysis")

# trait_pairs = st.multiselect("Select Traits for Comparison:", df.columns[1:], key="select_traits_for_comparision")

# if trait_pairs:
#     st.write(f"You selected: {trait_pairs}")

# # Ring chart for selected traits
# # Ring chart for selected traits
# if trait_pairs:
#     st.header("Team Trait Distribution")

#     # Initialize a dictionary to store the counts for each trait
#     trait_counts = {trait: 0 for trait in trait_pairs}

#     for trait in trait_pairs:
#         # Create a data frame for trait distribution
#         trait_distribution = df[trait].gt(50).sum()

#         # Increment the count for the trait
#         trait_counts[trait] += trait_distribution

#     # Create a ring chart
#     fig = go.Figure(go.Pie(
#         labels=list(trait_counts.keys()),
#         values=list(trait_counts.values()),  # Use the counts directly
#         hole=0.4,
#         pull=[0.1]*len(trait_counts)
#     ))

#     # Display the ring chart
#     st.plotly_chart(fig)

#     st.header("Dominant Traits for Each Team Member from selected")

st.title("Team Dominant Personality Traits Analysis")

trait_pairs = st.multiselect("Select Traits for Comparison:", df.columns[1:], key="select_traits_for_comparison")

if trait_pairs:
    st.write(f"You selected: {trait_pairs}")

    if trait_pairs:
        st.header("Team Trait Distribution")

        # Initialize a dictionary to store the counts for each dominant trait
        dominant_trait_counts = {trait: 0 for trait in trait_pairs}

        for index, row in df.iterrows():
            max_trait = max(trait_pairs, key=lambda trait: row[trait])
            dominant_trait_counts[max_trait] += 1

        # Create a ring chart
        fig = go.Figure(go.Pie(
            labels=list(dominant_trait_counts.keys()),
            values=list(dominant_trait_counts.values()),
            hole=0.4,
            pull=[0.1]*len(dominant_trait_counts)
        ))

        # Display the ring chart
        st.plotly_chart(fig)
    # Display dominant trait for each person
    for index, row in df.iterrows():
        max_trait = max(trait_pairs, key=lambda trait: row[trait])
        st.write(f"**{row['Team Members']}**: {max_trait}")


# Streamlit app
st.title("Individual Personality Traits Analysis")

# Trait explanations and belonging
selected_team_member = st.selectbox("Select Team Member:", df["Team Members"], key="select_member_1")
selected_data = df[df["Team Members"] == selected_team_member].squeeze()

data = [[selected_data.EXTROVERTED, selected_data.INTROVERTED],
         [selected_data.INTUITIVE, selected_data.OBSERVANT],
         [selected_data.THINKING, selected_data.FEELING],
         [selected_data.JUDGING, selected_data.PROSPECTING],
         [selected_data.ASSERTIVE, selected_data.TURBULENT]] 


df_stack = pd.DataFrame(data, index=["EXTROVERTED-INTROVERTED","INTUITIVE-OBSERVANT","THINKING-FEELING","JUDGING-PROSPECTING","ASSERTIVE-TURBULENT"])

trait_colors = {
    "EXTROVERTED": "rgba(255, 0, 0, 0.7)",
    "INTROVERTED": "rgba(0, 0, 255, 0.7)",
    "INTUITIVE": "rgba(0, 255, 0, 0.7)",
    "OBSERVANT": "rgba(255, 0, 255, 0.7)",
    "THINKING": "rgba(255, 255, 0, 0.7)",
    "FEELING": "rgba(0, 255, 255, 0.7)",
    "JUDGING": "rgba(128, 128, 0, 0.7)",
    "PROSPECTING": "rgba(0, 128, 0, 0.7)",
    "ASSERTIVE": "rgba(0, 0, 128, 0.7)",
    "TURBULENT": "rgba(128, 0, 128, 0.7)"
}

df_stack.plot(kind='bar', 
                    stacked=True, 
                    colormap='tab10', 
                    figsize=(10, 6))

# plt.legend(loc="upper left", ncol=2)
plt.xlabel("Personality traits")
plt.ylabel("Percentage")


for n, x in enumerate([*df_stack.index.values]):
    for (proportion, y_loc) in zip(df_stack.loc[x],
                                   df_stack.loc[x].cumsum()):
                
        plt.text(x=n - 0.17,
                 y=(y_loc - proportion) + (proportion / 2),
                 s=f'{np.round(proportion , 1)}%', 
                 color="black",
                 fontsize=12,
                 fontweight="bold")

st.pyplot(plt)


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
st.header("Trait Explanations")

for trait, description in trait_descriptions.items():
    st.write(f"**{trait}** : {description}")

