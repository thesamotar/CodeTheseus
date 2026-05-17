"""Quiet logger configuration for demo - suppresses verbose warnings."""

import warnings
import logging
import os

def setup_quiet_mode():
    """Configure logging to suppress verbose output during demo."""
    
    # Suppress noisy library loggers
    logging.getLogger('httpx').setLevel(logging.ERROR)
    logging.getLogger('httpcore').setLevel(logging.ERROR)
    logging.getLogger('urllib3').setLevel(logging.ERROR)
    
    # Suppress HuggingFace warnings
    os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
    os.environ['TOKENIZERS_PARALLELISM'] = 'false'

# Made with Bob