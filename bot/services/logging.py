import logging
from typing import Optional

def setup_logging(log_level: str, log_file: Optional[str] = None) -> None:
    """
    Configure logging for the bot.
    
    Args:
        log_level: The logging level (e.g., 'DEBUG', 'INFO', 'WARNING', 'ERROR')
        log_file: Optional path to log file. If None, only console logging is used.
    """
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level.upper())
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level.upper())
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)
    
    # File handler (if log file is specified)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level.upper())
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)