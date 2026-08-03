import io
import boto3
import pandas as pd

def main():
    # S3 Configuration
    bucket_name = "prodyot-edu-data-mlproject"
    raw_s3_key = "data/raw/reviews.csv"
    processed_s3_key = "data/processed/clean.csv"

    # Initialize S3 client
    s3_client = boto3.client("s3")

    # 1. Read raw CSV from S3
    print(f"Fetching s3://{bucket_name}/{raw_s3_key}...")
    response = s3_client.get_object(Bucket=bucket_name, Key=raw_s3_key)
    df = pd.read_csv(io.BytesIO(response["Body"].read()))

    # 2. Basic text normalization
    df["review_text"] = df["review_text"].str.lower()

    # 3. Write processed DataFrame back to S3
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)

    s3_client.put_object(
        Bucket=bucket_name,
        Key=processed_s3_key,
        Body=csv_buffer.getvalue()
    )

    print(f"✅ Preprocessing completed. Uploaded to s3://{bucket_name}/{processed_s3_key}")

if __name__ == "__main__":
    main()