from dataclasses import dataclass
from pathlib import Path

#this is same as config.yaml
@dataclass(frozen=True)
class DataIngestionConfig: #entity name
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path