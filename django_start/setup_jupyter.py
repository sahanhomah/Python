"""Bootstrap Django for notebooks and ad hoc scripts."""

import os
import sys
from pathlib import Path

import django

PROJECT_ROOT = Path(__file__).resolve().parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "merosite.settings")
django.setup()
