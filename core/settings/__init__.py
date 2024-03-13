import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# READING ENV
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))

STAGE = env.str("STAGE", "develop")
if STAGE == "develop":
    from .develop import *  # noqa
elif STAGE == "production":
    from .production import *  # noqa
