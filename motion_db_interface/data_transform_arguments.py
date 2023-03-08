import os
import json
import argparse

def load_json_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as in_file:
            return json.load(in_file)
    
def parse_arguments():
    parser = argparse.ArgumentParser(description="Run Data Transform")
    parser.add_argument("--work_dir", type=str, default=None, nargs='?')
    parser.add_argument("--input_skeleton", type=str, default=None, nargs='?')
    parser.add_argument("--output_id", type=int, default=None, nargs='?')
    parser.add_argument("--output_type", type=str, default=None, nargs='?')
    parser.add_argument("--output_skeleton", type=str, default=None, nargs='?')
    parser.add_argument("--input_ids", type=int, default=None, nargs='?')
    parser.add_argument("--input_types",type=str, default=None, nargs='?')
    parser.add_argument("--store_log", type=bool, default=False, nargs='?')
    parser.add_argument("--exp_name", type=str, default=None, nargs='?')
    parser.add_argument("--url", type=str, default="localhost", nargs='?')
    parser.add_argument("--port", type=int, default=8888, nargs='?')
    parser.add_argument("--user", type=str, default="", nargs='?')
    parser.add_argument("--token", type=str, default=None, nargs='?')
    parser.add_argument("--hparams_file", type=str, default=None, nargs='?')
    
    args = parser.parse_args()
    kwargs = vars(args)
    hparams_file = kwargs.get("hparams_file", None)
    if hparams_file is not None and os.path.isfile(hparams_file):
        hparams = load_json_file(hparams_file)
        print(hparams, kwargs, len(kwargs))
        if len(hparams) > 0:
            kwargs.update(hparams)
    return kwargs
