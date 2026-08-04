import shutil
from pathlib import Path
from datetime import datetime

# Directory to back up
SOURCE = Path("/var/www")

# Where snapshots are stored
BACKUP_ROOT = Path("/backups")

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
snapshot_dir = BACKUP_ROOT / f"snapshot_{timestamp}"

BACKUP_ROOT.mkdir(parents=True, exist_ok=True)

print(f"Creating snapshot: {snapshot_dir}")

shutil.copytree(SOURCE, snapshot_dir)

print("Snapshot completed successfully.")