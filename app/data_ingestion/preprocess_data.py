from app.data_ingestion.load_data import htd
import os
import pandas as pd
import base64


tax_data = htd.load()
# take the data from full data frame and convert it into a base64 encoded string.
def encode_data_to_base64(df: pd.DataFrame) -> str:
    """
    Encode the given Dataframe to a base64 string.
    Args:
        df (pd.DataFrame): Dataframe to be encoded.
    Returns:
        str: Base64 encoded string of the Dataframe.
    """
    # Convert the DataFrame to a CSV string
    csv_string = df.to_csv(index=False)

    # Encode the CSV string to bytes
    csv_bytes = csv_string.encode()

    # Convert the bytes to a base64 string
    base64_string = base64.b64encode(csv_bytes).decode()

    return base64_string


encoded_tax_data = encode_data_to_base64(tax_data)
print(encoded_tax_data)

