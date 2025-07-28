# This file marks the directory as a python package.
# It can be left empty, or used to expose modules for cleaner imports.

# For cleaner imports
from .chat import ask_openai
from .web_search import web_search
from .prompt_router import needs_web_search