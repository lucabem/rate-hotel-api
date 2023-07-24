import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spark.sql.functions._
import java.time.LocalDate
import java.time.format.DateTimeFormatter

object CSVProcessor {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("BeonX")
      .getOrCreate()

    val inputFolderPath = args(0)
    val outputFolderPath = args(1)

    val df = readCSVFiles(spark, inputFolderPath)

    val dfWithDatePartitions = addDatePartitions(df)

    writePartitionedData(dfWithDatePartitions, outputFolderPath)
    
    spark.stop()
  }

  def readCSVFiles(spark: SparkSession, path: String): DataFrame = {
    spark.read
      .option("header", "true")
      .csv(path)
  }

  def addDatePartitions(df: DataFrame): DataFrame = {
    val dateFormatter = DateTimeFormatter.ofPattern("yyyy-MM-dd")
    val dateColumn = col("check_in").cast("date")

    df.withColumn("year", year(dateColumn))
      .withColumn("month", month(dateColumn))
      .withColumn("day", dayofmonth(dateColumn))

  }

  def writePartitionedData(df: DataFrame, outputPath: String): Unit = {
    df.write
      .partitionBy("year", "month", "day")
      .format("parquet")
      .save(outputPath)
  }
}
