import io
import boto3
import pandas as pd

def main():
    # Specify your bucket and key (S3 object path)
    bucket_name = "prodyot-edu-data-mlproject"
    s3_key = "data/raw/reviews.csv"

    # Initialize S3 client
    s3_client = boto3.client("s3")

    # Fetch object from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=s3_key)
    
    # Read the bytes into Pandas
    df = pd.read_csv(io.BytesIO(response["Body"].read()))

    print("Total rows:", len(df))
    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nClass distribution:")
    print(df["sentiment"].value_counts())

if __name__ == "__main__":
    main()