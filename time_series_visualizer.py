import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')
print(df.head)
print(len(df))

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
print(df.head)
print(len(df))


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))

    # Plot line chart
    ax.plot(df.index, df['value'])

    # Set labels and title
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().reset_index(name='avg_value')
    df_pivot = df_bar.pivot(index='year', columns='month', values='avg_value')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_pivot.plot(kind='bar', ax=ax)

    # Set labels and title on the same axes
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Monthly Page Views per Year")

    # Set legend with month names in correct order
    ax.legend(title='Month', labels=[
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ])

    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

df_box = df.copy()
df_box.reset_index(inplace=True)
df_box['year'] = [d.year for d in df_box.date]
df_box['month'] = [d.strftime('%b') for d in df_box.date]

# Draw box plots (using Seaborn)
month_order = list(calendar.month_abbr)[1:]
fig, ax = plt.subplots(figsize = (10, 6))
sns.boxplot(x='month', y='value', hue='month', data=df_box, order=month_order, palette="colorblind", legend=False, ax=ax)
ax.set_title("Month-wise Box Plot (Seasonaility)")
ax.set_ylabel("Page Views")
ax.set_xlabel("Month")
if ax.legend_ is not None:
    ax.legend_.remove()
fig.savefig('testBoxPlot.png')

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    # df_box.reset_index(inplace=True)
    # df_box['year'] = [d.year for d in df_box.date]
    # df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    # fig.savefig('box_plot.png')
    # return fig
