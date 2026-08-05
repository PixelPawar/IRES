import os

from config import INDEX_FOLDERS
from utils.cache_manager import save_cache

def build_file_index():
    """
    Scan configured folders and build a searchable file index.
    """

    files = {}

    for folder in INDEX_FOLDERS:

        if not folder.exists():
            continue

        for root, dirs, filenames in os.walk(folder):

            for filename in filenames:

                key = filename.lower()

                if key not in files:

                    full_path = os.path.join(root, filename)
                    
                    files[key] = {
                        "name": filename,
                        "path": full_path,
                        "directory": root,
                        "extension": os.path.splitext(filename)[1].lower(),
                        "size": os.path.getsize(full_path),
                        "modified": os.path.getmtime(full_path)
                    }

    save_cache("files", files)

    print(f"Indexed {len(files)} files.")