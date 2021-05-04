# -*- coding: utf-8 -*-
import os

from myapi.app import create_app

app = create_app(os.getenv("FLASK_ENV", "development"))
