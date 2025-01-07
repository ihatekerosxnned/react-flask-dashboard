import pandas as pd
import plotly.graph_objects as go
import json
import plotly

# Define the file to read from
input_file = 'FinalCsv-Prelim.csv'
df = pd.read_csv(input_file)

def bar_graph_11_male_female():
    # Summing Grade 11 and Grade 12 male counts for each strand
    abm_m = df['ABM-11-M'] + df['ABM-12-M']
    humss_m = df['HUMSS-11-M'] + df['HUMSS-12-M']
    stem_m = df['STEM-11-M'] + df['STEM-12-M']
    gas_m = df['GAS-11-M'] + df['GAS-12-M']
    maritime_m = df['MARITIME-11-M'] + df['MARITIME-12-M']
    tvl_m = df['TVL-11-M'] + df['TVL-12-M']
    sports_m = df['Sports-11-M'] + df['Sports-12-M']
    arts_design_m = df['Arts&Design-11-M'] + df['Arts&Design-12-M']

    # Summing Grade 11 and Grade 12 female counts for each strand
    abm_f = df['ABM-11-F'] + df['ABM-12-F']
    humss_f = df['HUMSS-11-F'] + df['HUMSS-12-F']
    stem_f = df['STEM-11-F'] + df['STEM-12-F']
    gas_f = df['GAS-11-F'] + df['GAS-12-F']
    maritime_f = df['MARITIME-11-F'] + df['MARITIME-12-F']
    tvl_f = df['TVL-11-F'] + df['TVL-12-F']
    sports_f = df['Sports-11-F'] + df['Sports-12-F']
    arts_design_f = df['Arts&Design-11-F'] + df['Arts&Design-12-F']
    
    # Create traces for Male and Female distribution
    trace1 = go.Bar(
        x=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        y=[abm_m.sum(), humss_m.sum(), stem_m.sum(), gas_m.sum(), maritime_m.sum(), tvl_m.sum(), sports_m.sum(), arts_design_m.sum()],
        name='Grade 11 & 12 Male'
    )
    trace2 = go.Bar(
        x=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        y=[abm_f.sum(), humss_f.sum(), stem_f.sum(), gas_f.sum(), maritime_f.sum(), tvl_f.sum(), sports_f.sum(), arts_design_f.sum()],
        name='Grade 11 & 12 Female'
    )

    layout = go.Layout(
        barmode='group',
        title="Grade 11 & 12 Male vs Female Distribution",
        xaxis={'title': 'Sector'},
        yaxis={'title': 'Count'}
    )
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

#PIE CHART OVERALL STRAND
def piechart_by_gender():
    # Summing Grade 11 and Grade 12 male counts for each strand
    abm_m = df['ABM-11-M'] + df['ABM-12-M']
    humss_m = df['HUMSS-11-M'] + df['HUMSS-12-M']
    stem_m = df['STEM-11-M'] + df['STEM-12-M']
    gas_m = df['GAS-11-M'] + df['GAS-12-M']
    maritime_m = df['MARITIME-11-M'] + df['MARITIME-12-M']
    tvl_m = df['TVL-11-M'] + df['TVL-12-M']
    sports_m = df['Sports-11-M'] + df['Sports-12-M']
    arts_design_m = df['Arts&Design-11-M'] + df['Arts&Design-12-M']

    # Summing Grade 11 and Grade 12 female counts for each strand
    abm_f = df['ABM-11-F'] + df['ABM-12-F']
    humss_f = df['HUMSS-11-F'] + df['HUMSS-12-F']
    stem_f = df['STEM-11-F'] + df['STEM-12-F']
    gas_f = df['GAS-11-F'] + df['GAS-12-F']
    maritime_f = df['MARITIME-11-F'] + df['MARITIME-12-F']
    tvl_f = df['TVL-11-F'] + df['TVL-12-F']
    sports_f = df['Sports-11-F'] + df['Sports-12-F']
    arts_design_f = df['Arts&Design-11-F'] + df['Arts&Design-12-F']

    # Pie chart for Male and Female distribution across strands
    trace1 = go.Pie(
        labels=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        values=[abm_m.sum(), humss_m.sum(), stem_m.sum(), gas_m.sum(), maritime_m.sum(), tvl_m.sum(), sports_m.sum(), arts_design_m.sum()],
        name='Male (Grade 11 & 12)'
    )
    
    trace2 = go.Pie(
        labels=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        values=[abm_f.sum(), humss_f.sum(), stem_f.sum(), gas_f.sum(), maritime_f.sum(), tvl_f.sum(), sports_f.sum(), arts_design_f.sum()],
        name='Female (Grade 11 & 12)'
    )
    
    # Layout configuration
    layout = go.Layout(
        title="Pie Chart for Overall Strand by Gender (Grade 11 & 12)",
        showlegend=True
    )
    
    # Create figure with both pie charts
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    
    # Return the figure as a JSON object
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

# Function to generate pie chart for 11 and 12 grade students
def pie_chart_11_12_students():
    labels = ['11th Grade', '12th Grade']
    values = [df['Grand Total 11 M'].sum() + df['Grand Total 11 F'].sum(), 
              df['Grand Total 12 M'].sum() + df['Grand Total 12 F'].sum()]
    
    trace = go.Pie(labels=labels, values=values, hole=0.3)
    layout = go.Layout(title="Grade 11 vs Grade 12 Students Distribution")
    fig = go.Figure(data=[trace], layout=layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

# FUNCTION TO CREATE BAR GRAPH OF ALL STRAND FUCKING HELL BRO
# Function to generate combined bar chart for all ABM-M and ABM-F (total counts)
def bar_graph_all_strand():
    # Combine all ABM-M and ABM-F values for Grade 11 and Grade 12
    abm_m = df[['ABM-11-M', 'HUMSS-11-M', 'STEM-11-M', 'GAS-11-M', 'MARITIME-11-M', 'TVL-11-M', 'Sports-11-M', 'Arts&Design-11-M']].sum().sum() + df[['ABM-12-M', 'HUMSS-12-M', 'STEM-12-M', 'GAS-12-M', 'MARITIME-12-M', 'TVL-12-M', 'Sports-12-M', 'Arts&Design-12-M']].sum().sum()
    abm_f = df[['ABM-11-F', 'HUMSS-11-F', 'STEM-11-F', 'GAS-11-F', 'MARITIME-11-F', 'TVL-11-F', 'Sports-11-F', 'Arts&Design-11-F']].sum().sum() + df[['ABM-12-F', 'HUMSS-12-F', 'STEM-12-F', 'GAS-12-F', 'MARITIME-12-F', 'TVL-12-F', 'Sports-12-F', 'Arts&Design-12-F']].sum().sum()

    
    trace1 = go.Bar(
        x=['Male'],
        y=[abm_m],
        name='Male'
    )
    
    trace2 = go.Bar(
        x=['Female'],
        y=[abm_f],
        name='Female'
    )

    layout = go.Layout(
        barmode='group',
        title="Overall Gender by Strand",
        xaxis={'title': 'Gender'},
        yaxis={'title': 'Count'}
    )
    
    fig = go.Figure(data=[trace1, trace2], layout=layout)
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

def line_chart_by_gender():
    # Create traces for each gender and grade
    trace1 = go.Scatter(
        x=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        y=df['ABM-11-M'],
        mode='lines+markers',
        name='Grade 11 Male'
    )
    
    trace2 = go.Scatter(
        x=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        y=df['ABM-11-F'],
        mode='lines+markers',
        name='Grade 11 Female'
    )
    
    trace3 = go.Scatter(
        x=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        y=df['ABM-12-M'],
        mode='lines+markers',
        name='Grade 12 Male'
    )
    
    trace4 = go.Scatter(
        x=['ABM', 'HUMSS', 'STEM', 'GAS', 'MARITIME', 'TVL', 'Sports', 'Arts&Design'],
        y=df['ABM-12-F'],
        mode='lines+markers',
        name='Grade 12 Female'
    )
    
    # Layout configuration
    layout = go.Layout(
        title="Gender Distribution Across Strands (Grade 11 & 12)",
        xaxis={'title': 'Strand'},
        yaxis={'title': 'Count'},
        showlegend=True
    )
    
    # Create figure with all the traces
    fig = go.Figure(data=[trace1, trace2, trace3, trace4], layout=layout)
    
    # Return the figure as a JSON object
    return json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


# Main function to generate all plots for the Flask route
def generate_all_graphs():
    try:
        graph_11_male_female = bar_graph_11_male_female()
        graph_11_12 = pie_chart_11_12_students()
        bargraph_all = bar_graph_all_strand()
        piechart_gender = piechart_by_gender()
        line_chart_gender = line_chart_by_gender()
        # Add other graph functions as needed
        return {
            "graph_11_male_female": graph_11_male_female,
            "graph_11_12": graph_11_12,
            "bargraph_all": bargraph_all,
            "piechart_gender" : piechart_gender,
            "line_chart_gender" : line_chart_gender
        }
    except Exception as e:
        # Log the error and return a proper response
        print(f"Error generating graphs: {e}")
        return {"error": "Error generating graphs", "message": str(e)}
