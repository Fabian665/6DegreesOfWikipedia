from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from decimal import Decimal
import wikipedia


# def main():
#     graph = nx.complete_graph(5)
#     nx.draw(graph)
#     plt.show()


if __name__ == "__main__":
    import networkx as nx
    import matplotlib.pyplot as plt
    #main()

    # appName = "Python Example - PySpark Read XML"
    # master = "local"
    # # Create Spark session
    # spark = SparkSession.builder \
    #     .appName(appName) \
    #     .master(master) \
    #     .getOrCreate()
    #
    # schema = StructType([
    #     StructField('_id', IntegerType(), False),
    #     StructField('rid', IntegerType(), False),
    #     StructField('name', StringType(), False)
    # ])
    #
    # df = spark.read.format("xml") \
    #     .option("rootTag", "data").option("rowTag", "record").load(r"C:\Users\user\Downloads\enwiki-20220101-pages-articles-multistream\enwiki-20220101-pages-articles-multistream.xml\enwiki-20220101-pages-articles-multistream.xml", schema=schema)
    #
    # df.show()

    ny = wikipedia.search("Facebook", suggestion=False)
    print(wikipedia.page(ny[0]).url)
    mz = wikipedia.page("Mark Zuckerberg")
    #print(mz.content)
    #print(ny.content)

