from pipeline.extract import extract_from_csv
from pipeline.transform import concat_dataframes
from pipeline.load import load_csv

if __name__ == "__main__":
    data_frame_list = extract_from_csv("data/input")
    print(type(data_frame_list))
    data_frame = concat_dataframes(data_frame_list)
    print(type(data_frame))
    load_csv(data_frame, "data/output", "output")