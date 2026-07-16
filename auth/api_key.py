import os
from logger import get_logger

log = get_logger(__name__)

def get_api_key(service_name: str) -> str:
    """
    Retrieve the API key for a given service from environment variables.

    Expected .env format:
        SERVICENAME_API_KEY=your_key_here
    
    Example:
        ZENDESK_API_KEY=abc123
        HUBSPOT_API_KEY=xyz789
    """

    env_var = f"{service_name.upper()}_API_KEY"
    key = os.getenv(env_var)

    if not key:
        log.error(f"Missing API key: {env_var} not set in .env")
        raise ValueError(f"Missing required env var: {env_var}")

    log.debug(f"Loaded API key for {service_name}")
    return key