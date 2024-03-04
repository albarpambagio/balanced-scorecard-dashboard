import marimo

__generated_with = "0.2.13"
app = marimo.App()


@app.cell
def __(mo):
    mo.hstack([
        mo.stat(value="$ 84.495", label="Average Order Value", caption="the average amount customers spend per transaction", bordered=True),
        mo.stat(value="9.0", label="Order Cycle Time (in days)", caption="the total duration taken for an order to be processed, fulfilled, and delivered to the customer.", bordered=True),
        mo.stat(value="5.0", label="Average Review Score (1 to 5)", caption="median value of ratings assigned to products, services, or experiences by customers or users.", bordered=True),
        mo.stat(value="3.0", label="Job Satisfaction Score (1 to 5)", caption="measures the level of contentment and fulfillment employees feel in their roles and workplace environment.", bordered=True)
    ])
    return


@app.cell
def __():
    import marimo as mo
    import pandas as pd 
    import plotly.express as px
    return mo, pd, px


@app.cell
def __(pd):
    def read_csv_file(file_path):
        return pd.read_csv(file_path)

    file_paths = [
        'data/olist_order_items_dataset.csv',
        'data/olist_order_reviews_dataset.csv',
        'data/olist_orders_dataset.csv',
        'data/WA_Fn-UseC_-HR-Employee-Attrition.csv'
    ]


    dataframes = [read_csv_file(file_path) for file_path in file_paths]

    # Unpack the dataframes
    df_order_items, df_order_reviews, df_orders, df_people = dataframes

    return (
        dataframes,
        df_order_items,
        df_order_reviews,
        df_orders,
        df_people,
        file_paths,
        read_csv_file,
    )


@app.cell
def __():
    # Average Order Value
    return


@app.cell
def __(df_order_items):
    # Calculating the product of 'order_item_id' and 'price' for each item
    trxProduct = df_order_items['order_item_id'].mul(df_order_items['price'])

    # Adding the product to df_order_items as a column
    df_order_items2 = df_order_items.assign(trxProduct=trxProduct)
    return df_order_items2, trxProduct


@app.cell
def __(df_order_items2, px):
    #visualization of distribution
    priceDistribution = px.histogram(df_order_items2, x='trxProduct', 
                                    labels={'trxProduct': 'Total Transaction (price x quantity)'}, 
                                    title='Transaction Value Distribution'
                                    )

    priceDistribution.show()
    return priceDistribution,


@app.cell
def __():
    # Calculating the median of the resulting values
    # median_value = trxProduct.median()
    return


@app.cell
def __(mo, priceDistribution):
    plot = mo.ui.plotly(priceDistribution)
    return plot,


@app.cell
def __(mo, plot):
    # View the plot and selected data
    mo.hstack([plot, plot.value])
    return


@app.cell
def __():
    # Order Cycle Time
    return


@app.cell
def __(df_orders, pd):
    df_orders['order_approved_at'] = pd.to_datetime(df_orders['order_approved_at'])
    df_orders['order_delivered_customer_date'] = pd.to_datetime(df_orders['order_delivered_customer_date'])

    # Calculate the difference between two datetime columns
    orderCycleTime = df_orders['order_delivered_customer_date'].sub(df_orders['order_approved_at'])
    return orderCycleTime,


@app.cell
def __(orderCycleTime, px):
    #visualization of order cycle time distribution
    fig = px.histogram(x=orderCycleTime.dt.days, nbins=30, title='Order Cycle Time Histogram')
    fig.update_xaxes(title_text='Days')
    fig.update_yaxes(title_text='Frequency')
    fig.show()
    return fig,


@app.cell
def __():
    # Calculating the median of the resulting values
    # octMedian = orderCycleTime.dt.days.median()
    return


@app.cell
def __(fig, mo):
    plot_two = mo.ui.plotly(fig)
    return plot_two,


@app.cell
def __(mo, plot_two):
    # View the plot and selected data
    mo.hstack([plot_two, plot_two.value])
    return


@app.cell
def __():
    # Average Review Score
    return


@app.cell
def __(df_order_reviews, px):
    scoreCounting = df_order_reviews['review_score'].value_counts()


    # Convert the value counts series to a DataFrame and reset the index
    scoreCounting_df = scoreCounting.reset_index(name='count')

    # Sort the DataFrame by the review_score column
    scoreCounting_df = scoreCounting_df.sort_values(by='count', ascending=False)

    print(scoreCounting_df)

    # Create bar chart
    bar_chart = px.bar(scoreCounting_df, x='review_score', y='count', 
                       labels={'review_score': 'Review Score', 'count': 'Count'},
                       title='Distribution of Review Scores')


    # Show the bar chart
    bar_chart.show()
    return bar_chart, scoreCounting, scoreCounting_df


@app.cell
def __():
    # Calculating the median of the resulting values
    # df_order_reviews['review_score'].median()
    return


@app.cell
def __(bar_chart, mo):
    plot_three = mo.ui.plotly(bar_chart)
    return plot_three,


@app.cell
def __(mo, plot_three):
    mo.hstack([plot_three, plot_three.value])
    return


@app.cell
def __():
    # Job Satisfaction Score
    return


@app.cell
def __(df_people, px):
    #visualization of job satisfaction distribution
    satisfactionDistribution = px.histogram(df_people, x='JobSatisfaction', 
                                    labels={'JobSatisfaction': 'Job Satisfaction'}, 
                                    title='Job Satisfaction Distribution'
                                    )

    satisfactionDistribution.show()
    return satisfactionDistribution,


@app.cell
def __():
    # df_people['JobSatisfaction'].median()
    return


@app.cell
def __(mo, satisfactionDistribution):
    plot_four = mo.ui.plotly(satisfactionDistribution)
    return plot_four,


@app.cell
def __(mo, plot_four):
    mo.hstack([plot_four, plot_four.value])
    return


if __name__ == "__main__":
    app.run()
