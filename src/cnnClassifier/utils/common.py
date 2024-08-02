#store of repeatative or most frequrent codes
import os
from box.exceptions import BoxValueError
from yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import config_box
from pathlib import Path
from typing import Any
import base64

#simple Read yaml file
@ensure_annotations   #decorator used to debug the issues or errors
#configBox convert file into convenient or in easy way ie. Refer research->trails.ipynb
def read_yaml(path_to_yaml: Path) -> configBox:
    """
    Read yaml file and returns

    Args:
        path_to_yaml(str): path like input
    Raise:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
    ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return configBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


#Create list of directories
@ensure_annotations
def create_directories(path_to_directories: list, verbose = True):
    """
    Create list of directories
    Args:
        path_to_directories(list) : list of path of directories
        ignore_log(bool, optional) : ignore if multiple dirs is to be created, default is false.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


#json is used to save loss and accracy metrics
#simple save json data
@ensure_annotations
def save_json(path: Path, data: dict):
    """
    save json data
    Args:
        Path(Path): Path to json file
        data(dict): data to be saved in json file
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file save at: {path}")


#load json files data
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json files data
    Args:
        path(Path): Path to json file
    Returns:
        ConfigBox: Data as class attributes instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from: {path}")
    return configBox(content)


#save the file into binary format
@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    save binary file
    Args:
        data(Any):data to be saved as binary
        path(Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


#load binary files data
@ensure_annotations
def load_bin(path:Path)->Any:
    """
    load binary data
    Args:
        path(Path):path to binary file
    Returns:
        Any : object stored in the file
    """
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data


#get file size in KB
@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB
    Args:
        path(Path) : path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb}KB"


#decode image from base64 string and save into file
def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()


#encode image into base64 string
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())











