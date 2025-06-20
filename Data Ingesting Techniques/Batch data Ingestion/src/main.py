import load_data as ld
import generate_data as gd
import transform_data as td
import time 
import pandas as pd
from IPython.display import display
# Main Function
def main():
    # Parameters
    num_records = 30  # Total number of records to generate
    batch_size = 10    # Number of records per batch

    # Generate data
    data = gd.generate_sample_data_with_uuid(num_records)
    print("Original data:",data)
    
    # Process and load data in batches
    for batch in gd.process_in_batches(data, batch_size):
        transformed_batch = td.transform_data(batch)
        print("Batch before loading:")
        for record in transformed_batch:
            df = pd.DataFrame(data)
            display(df)
        ld.load_data(transformed_batch)
        time.sleep(1)  # Simulate time delay between batches

if __name__ == "__main__":
    main()