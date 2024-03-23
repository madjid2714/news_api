from dateutil.relativedelta import relativedelta
from .models import NewsArticle
from psqlextra.partitioning import (
    PostgresPartitioningManager,
    PostgresCurrentTimePartitioningStrategy,
    PostgresTimePartitionSize,
    partition_by_current_time,
)
from psqlextra.partitioning.config import PostgresPartitioningConfig

manager = PostgresPartitioningManager([
    # 2 partitions ahead, each partition is one month
    # partitions will be named `[table_name]_[year]_[1-letter month name]`.
    PostgresPartitioningConfig(
        model=NewsArticle,
        strategy=PostgresCurrentTimePartitioningStrategy(
            size=PostgresTimePartitionSize(months=1),
            count=2,
            # max_age=relativedelta(months=6),
        ),
    ),

])