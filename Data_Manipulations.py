from pyspark.sql import SparkSession
from faker import Faker
import pyspark.sql.functions as F
from pyspark.sql.window import Window
from datetime import datetime, timedelta
from helpers import *
from pyspark.sql.functions import rand, date_add, lit, col, when
import random

def z_score(dataframe, column_name, window=None):
    from pyspark.sql import functions as F
    from pyspark.sql.window import Window
    
    if window is None:
        mean_value = dataframe.select(F.mean(F.col(column_name))).first()[0]
        std_dev = dataframe.select(F.stddev(F.col(column_name))).first()[0]
    else:
        if isinstance(window, str):
            window_spec = Window.partitionBy(F.col(window))  # Convert the window string to a column object
        else:
            window_spec = window
        
        mean_value = F.mean(F.col(column_name)).over(window_spec)
        std_dev = F.stddev(F.col(column_name)).over(window_spec)

    df_score = dataframe.withColumn("z_score", (F.col(column_name) - mean_value) / std_dev)

    min_zscore = df_score.agg(F.min("z_score")).collect()[0][0]
    max_zscore = df_score.agg(F.max("z_score")).collect()[0][0]

    df_score = df_score.withColumn(
        "normalized_score",
        (F.col("z_score") - min_zscore) / (max_zscore - min_zscore)
    )

    return df_score


# window for local rank, if no window, then only global rank to be present
# global_rank_window for global rank

def rank(dataframe, count, amount, global_rank_window, local_window = None):

    if local_window != None:
        df = dataframe.withColumn('CountValue', F.sum(count).over(local_window))
        df = df.withColumn('AmountValue',  F.sum(amount).over(local_window))
        df = df.withColumn('LocalRank', F.rank().over(local_window))
    else:
        df = dataframe.withColumn('CountValue', F.sum(count))
        df = df.withColumn('AmountValue',  F.sum(amount))
    
    df = df.withColumn('GlobalRank', F.rank().over(global_rank_window))

    return df


# Add random dates
def random_dates(dataframe, years, seed=None):
    if seed is not None:
        random.seed(seed)
    current_date = datetime.now().date()  
    start_date = current_date - timedelta(days=years * 365)
    end_date = current_date 
    mid_date = current_date - timedelta(days=365)

    # Random days between start and end
    df = dataframe.withColumn('random_days', when(rand() < 0.5, (rand() * (end_date - mid_date).days).cast('integer')).otherwise((rand() * (mid_date - start_date).days).cast('integer')))

    # Add the random number of days to start_date or mid_date to get random dates within the specified range
    df = df.withColumn('TransactionDate', when(col('random_days') < (end_date - mid_date).days, date_add(lit(mid_date), col('random_days'))).otherwise(date_add(lit(start_date), col('random_days'))))
    df = df.drop('random_days')

    return df


def random_ID(dataframe, column):
    df = dataframe.withColumn(column, rand() * 10 )

####################################################### Employee #######################################################

####### Employee


####### Customer