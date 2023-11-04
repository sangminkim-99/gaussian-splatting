import numpy as np
import pandas as pd
from plyfile import PlyData
import sys
from argparse import ArgumentParser


def convert_ply(input_path, output_path):
    plydata = PlyData.read(input_path)  # read file
    data = plydata.elements[0].data  # read data
    data_pd = pd.DataFrame(data)  # convert to DataFrame
    property_names = data[0].dtype.names  # read names of properties
    breakpoint()
    property_names = ['x', 'y', 'z', 'red', 'green', 'blue']  # read names of properties
    # property_names = ['x', 'y', 'z', 'opacity']  # read names of properties
    data_np = np.zeros((data_pd.shape[0], len(property_names)), dtype=np.float32)  # initialize array to store data
    for i, name in enumerate(
            property_names):  # read data by property
        data_np[:, i] = data_pd[name]
    # opacity_mask = data_np[:, 3] > 0.5
    # data_np[opacity_mask].astype(np.float32).tofile(output_path)
    # data_np.astype(np.float32).tofile(output_path)

    
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--input_ply', type=str, required=True)
    parser.add_argument('--output_ply', type=str, required=True)
    args = parser.parse_args()
    convert_ply(args.input_ply, args.output_ply)