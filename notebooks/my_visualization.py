#!/usr/bin/env python
__author__ = "Wayne Decatur" #fomightez on GitHub
__license__ = "MIT"
__version__ = "0.1.0"
#-----------

# This code became rather long because I had developed some early visual steps
# that though adapting this may find useful. I have moved it to a separate 
# script in the interest of real estate in the notebook. There is a similar plot
# to the original barplot in the notebook farther down.
#
#*******************************************************************************
# Starting point for early visualization.
# This first block was the original code to show the data in a straightforward 
# manner. Then based on what it showed and what I wanted to emphasize I adapted 
# it to the code found below. This produced a reasonable plot, however, it 
# it morphed into a nicer one as determined what to show.
'''
import seaborn as sns
import matplotlib.pyplot as plt

def simplifytags(tag):
    """
    remove some of the consistent part at the start of the tag
    """
    special_additional_name_part_to_not_include = "TSL4_"
    if special_additional_name_part_to_not_include in tag:
        new_tag = tag.split(special_additional_name_part_to_not_include,1)[1]
    else:
        new_tag = tag.split("_",1)[1]
    return new_tag

def plot_homo_sapiens_counts(dfs, labels=None, palette='husl', order=None, legend_text=None):
    """
    Plot the count of 'Homo sapiens' in the 'organism' column for multiple dataframes.
    
    Parameters:
    dfs (list): List of pandas DataFrames
    labels (list): Optional list of labels for each DataFrame. If None, will use index numbers
    palette (str or list): Color palette to use
    order (list): Optional list specifying the desired order of labels
    legend_text (str): Optional custom legend text
    """
    # Calculate counts for each dataframe
    counts = [df['organism'].value_counts()['Homo sapiens'] if 'Homo sapiens' in df['organism'].values else 0 
             for df in dfs]
    
    # Create a DataFrame for plotting
    plot_df = pd.DataFrame({
        'Dataset': labels if labels else [f'Dataset {i+1}' for i in range(len(dfs))],
        'Count': counts
    })
    
    # If order is specified, convert Dataset to ordered categorical
    if order is not None:
        plot_df['Dataset'] = pd.Categorical(plot_df['Dataset'], categories=order, ordered=True)
        
    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.barplot(data=plot_df, x='Dataset', y='Count', hue='Dataset', palette=palette, legend=False)
    #print(plot_df) #Uncomment this to show the counts!
    
    # Customize the plot
    plt.title(('Number of $\mathit{Homo\ sapiens}$ SRA Datasets Containing the '
           'Query Sequences from $\mathit{' + gene_name + '}$ Transcripts'))
    #plt.xticks(rotation=45)
    plt.xlabel('Query Sequence Identifier\n(length = 31 nt & for k-mer index, $\mathit{k}$ = 31)')
    plt.ylabel('Count')

    if legend_text:
        # Position the text in the upper right corner
        # Adjust the x and y values (0.95, 0.95) to change position
        ax = plt.gca()
        plt.figtext(0.95, 0.95, legend_text, 
                   transform=ax.transAxes,
                   horizontalalignment='right',
                   verticalalignment='top',
                   bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()

# Example usage:
labels = [simplifytags(x) for x in file_tags_per_file]
desired_order = [labels[3],labels[2],labels[0], labels[1]]  # Replace with your actual k-mer names in desired order
#colors = ['#1f77b4','#ff7f0e', '#2ca02c', '#d62728']
colors = ['#1f77b4', 'cornflowerblue','#ff7f0e', '#ef6f2e']
legend_text = "blues: TSL1\noranges: TSL4"
plot_homo_sapiens_counts(dfs, labels, palette=colors, order=desired_order,legend_text=legend_text)
plt.show()
'''
#*******************************************************************************
#
#
#
#
#
#*******************************************************************************
# Second phase for early visualization.
# This second block was the original idea of grouped barplots.
# It gives the idea using Seaborn's examples. (see more about it below this 
# block and just above the current actual code)

'''
import seaborn as sns
import matplotlib.pyplot as plt

def simplifytags(tag):
    """
    remove some of the consistent part at the start of the tag
    """
    special_additional_name_part_to_not_include = "TSL4_"
    if special_additional_name_part_to_not_include in tag:
        new_tag = tag.split(special_additional_name_part_to_not_include,1)[1]
    else:
        new_tag = tag.split("_",1)[1]
    return new_tag

def plot_homo_sapiens_counts(dfs, labels=None, palette='husl', order=None, legend_text=None):
    """
    Plot the count of 'Homo sapiens' in the 'organism' column for multiple dataframes.
    
    Parameters:
    dfs (list): List of pandas DataFrames
    labels (list): Optional list of labels for each DataFrame. If None, will use index numbers
    palette (str or list): Color palette to use
    order (list): Optional list specifying the desired order of labels
    legend_text (str): Optional custom legend text
    """
    # Calculate counts for each dataframe
    counts = [df['organism'].value_counts()['Homo sapiens'] if 'Homo sapiens' in df['organism'].values else 0 
             for df in dfs]

    # Categorize by Transcript Support Level (TSL) rating
    ratings = ['TSL1' if x.startswith('SJ_') else 'TSL4' for x in labels]
    
    # Create a DataFrame for plotting
    plot_df = pd.DataFrame({
        'Dataset': labels if labels else [f'Dataset {i+1}' for i in range(len(dfs))],
        'Count': counts,
        'Rating': ratings
    })
    
    # If order is specified, convert Dataset to ordered categorical
    if order is not None:
        plot_df['Dataset'] = pd.Categorical(plot_df['Dataset'], categories=order, ordered=True)
        
    # Create the plot
    plt.figure(figsize=(10, 6))
    #sns.barplot(data=plot_df, x='Dataset', y='Count', hue='Dataset', palette=palette, legend=False)
    sns.set_theme(style="whitegrid")
    g = sns.catplot(
            data=plot_df, x='Rating', y='Count', hue='Dataset', order = ['TSL1','TSL4'],
            kind="bar", palette=palette,
        )
    g.despine(left=True)
    g.set_axis_labels("Transcript Support Level Rating","Count" )
    g.legend.set_title('Query Sequence Identifier\n(length = 31 nt & for k-mer index, $\mathit{k}$ = 31)')
    
    # Customize the plot
    plt.title(('Number of $\mathit{Homo\ sapiens}$ SRA Datasets Containing the '
           'Query Sequences from $\mathit{' + gene_name + '}$ Transcripts'))
    #plt.xticks(rotation=45)
    #plt.xlabel('Query Sequence Identifier\n(length = 31 nt & for k-mer index, $\mathit{k}$ = 31)')
    #plt.ylabel('Count')

    if legend_text:
        # Position the text in the upper right corner
        # Adjust the x and y values (0.95, 0.95) to change position
        ax = plt.gca()
        plt.figtext(0.95, 0.95, legend_text, 
                   transform=ax.transAxes,
                   horizontalalignment='right',
                   verticalalignment='top',
                   bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    

# Example usage:
labels = [simplifytags(x) for x in file_tags_per_file]
desired_order = [labels[3],labels[2],labels[0], labels[1]]  # Replace with your actual k-mer names in desired order
#colors = ['#1f77b4','#ff7f0e', '#2ca02c', '#d62728']
colors = ['#1f77b4', 'cornflowerblue','#ff7f0e', '#ef6f2e']
legend_text = "blues: TSL1\noranges: TSL4"
plot_homo_sapiens_counts(dfs, labels, palette=colors, order=desired_order,legend_text=False)
plt.show()
'''

# That above looked overall like what I want to make but had issues. Issues: 1) for some odd reason 
# the object code `<Figure size 1000x600 with 0 Axes>` was coming out above the plot. 2)  The legend 
# is over the final bar and I want it more off to the left.  3) The group labels looked to be centered 
# on an imaginary four bar plots when each group only has two plots. Issues #2 and #3 being the most 
# critical! Not really useable with them like that.
#*******************************************************************************
#
#
#
#
#
#*******************************************************************************






#######***************THIRD AND FINAL SECTION*****************************######
# BELOW IS THE FINAL BLOCK AND THIS IS CODE THAT ISN'T COMMENTED OUT AND SO IT
# IS THE ONE THAT CURRENTLY GETS RUN.
# Reconstructed Matplotlib version of that grouped barplot fixing the issues of 
# the legend and  centering of the group labels (worked out with Claude.ai's 
# help). The issue of the object code was eliminated in the course of this.
# It hardcoded things a lot more than I liked and I fixed it some, andI can 
# maybe work on  generalizing it more at some point, but for now it works.
import matplotlib.pyplot as plt
import numpy as np

def simplifytags(tag):
    special_additional_name_part_to_not_include = "TSL4_"
    if special_additional_name_part_to_not_include in tag:
        new_tag = tag.split(special_additional_name_part_to_not_include,1)[1]
    else:
        new_tag = tag.split("_",1)[1]
    return new_tag

def plot_homo_sapiens_counts(dfs, labels=None, palette=None, order=None, gene_name=gene_name):
    """
    Plot the count of 'Homo sapiens' in the 'organism' column for multiple dataframes.
    """
    # Calculate counts for each dataframe
    counts = [df['organism'].value_counts()['Homo sapiens'] if 'Homo sapiens' in df['organism'].values else 0 
             for df in dfs]

    # Categorize by Transcript Support Level (TSL) rating
    ratings = ['TSL1' if x.startswith('SJ_') else 'TSL4' for x in labels]
    
    # Create a DataFrame for plotting
    plot_df = pd.DataFrame({
        'Dataset': labels if labels else [f'Dataset {i+1}' for i in range(len(dfs))],
        'Count': counts,
        'Rating': ratings
    })

    # Create the figure and axis explicitly
    fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')
    
    # Prepare data for plotting
    #tsl_groups = ['TSL1', 'TSL4'] # would hardcode what I want as order
    #tsl_groups = list(set(ratings)) # gives same as what I would otherwise 
    # hardcode (I thought originally!!); the set step must order in some way or 
    # just 50-50 chance came out how I wanted?  ANSWER: Turns out just was 
    # chance. I started seeing it come out wrong! Make sure to add sort:
    tsl_groups = sorted(list(set(ratings)))
    
    '''
    # Explicitly order the data
    tsl1_labels = [label for label in labels if label.startswith('SJ_')]
    tsl1_counts = [counts[labels.index(label)] for label in tsl1_labels]
    
    tsl4_labels = [label for label in labels if not label.startswith('SJ_')]
    tsl4_counts = [counts[labels.index(label)] for label in tsl4_labels]
    '''
    
    # Ensure SJ_34 is first in TSL1, and order matches original color assignment & desired_order
    tsl1_labels = order[:int(len(order)/2)]
    tsl1_counts = [counts[labels.index(tsl1_labels[0])], counts[labels.index(tsl1_labels[1])]]
    
    # Ensure order for TSL4 matches original color assignment & desired_order
    tsl4_labels = order[int(len(order)/2):]
    tsl4_counts = [counts[labels.index(tsl4_labels[0])], counts[labels.index(tsl4_labels[1])]]
    
    # Bar width and positions
    bar_width = 0.35
    
    # Add grid BEFORE plotting bars
    ax.grid(axis='y', linestyle='-', linewidth=0.5, color='#cccccc', zorder=0)
    
    # Plot bars for TSL1 group
    ax.bar(0 - bar_width/2, tsl1_counts[0], bar_width, 
           label=tsl1_labels[0], color=palette[0], zorder=3)  # SJ_34
    ax.bar(0 + bar_width/2, tsl1_counts[1], bar_width, 
           label=tsl1_labels[1], color=palette[1], zorder=3)  # SJ_14n15
    
    # Plot bars for TSL4 group
    ax.bar(1 - bar_width/2, tsl4_counts[0], bar_width, 
           label=tsl4_labels[0], color=palette[2], zorder=3)  # altSJ
    ax.bar(1 + bar_width/2, tsl4_counts[1], bar_width, 
           label=tsl4_labels[1], color=palette[3], zorder=3)  # SJ
    
    # Customize the plot
    ax.set_xlabel('Transcript Support Level Rating')
    ax.set_ylabel('Count')
    ax.set_title(('Number of $\mathit{Homo\ sapiens}$ SRA Datasets Containing the '
           '\nQuery Sequences from $\mathit{' + gene_name + '}$ Transcripts'))
    
    # Set x-ticks exactly at the center of the groups
    ax.set_xticks([0, 1])
    ax.set_xticklabels(tsl_groups)
    
    # Despine the plot (remove top and right spines)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Remove y-axis line
    ax.spines['left'].set_visible(False)
    
    # Remove y-axis ticks
    ax.tick_params(axis='y', length=0)
    
    # Create legend with no border and positioned to the right of the plot
    legend = ax.legend(title='            Query Sequence Identifier\n(length = 31 nt & for k-mer index, $\mathit{k}$ = 31)', 
                       loc='center left', bbox_to_anchor=(1, 0.5), frameon=False)
    
    # Adjust layout to make room for legend
    plt.tight_layout()    
    return fig

# Example usage:
labels = [simplifytags(x) for x in file_tags_per_file]
desired_order = [labels[3],labels[2],labels[0], labels[1]]  # Replace with your actual k-mer names in desired order
colors = ['#1f77b4', 'cornflowerblue', '#ff7f0e', '#ef6f2e']

# Call the function
plot = plot_homo_sapiens_counts(dfs, labels, palette=colors, order=desired_order)
plt.show()