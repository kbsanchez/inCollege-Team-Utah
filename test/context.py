import os
import sys

# add source files to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import main
from src import main_menu
from src import links_menu
from src import profile_menu
from src import db_session
from src import friends