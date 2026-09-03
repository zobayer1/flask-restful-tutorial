# -*- coding: utf-8 -*-
from enum import Enum


class Availability(str, Enum):
    """Availability states a book can be in"""

    AVAILABLE = "available"
    BORROWED = "borrowed"
    LOST = "lost"
