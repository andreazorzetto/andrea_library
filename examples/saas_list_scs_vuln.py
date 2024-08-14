import sys
import json
from dotenv import load_dotenv
import os
from andrea_library.aqua_functions import get_token, get_scan_results
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables from .env file
load_dotenv()

# API details
base_url = os.getenv('BASE_URL')
scs_base_url = os.getenv('SCS_BASE_URL')
csp_url = os.getenv('CSP_URL')
api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
api_methods = os.getenv('API_METHODS')
aqua_role = os.getenv('AQUA_ROLE')

# Authentication
try:
    token = get_token(base_url, api_key, api_secret, aqua_role, api_methods)

except Exception as e:
    logger.error(f"Error occurred during authentication: {e}")
    sys.exit(1)

# Initialize pagination variables
page = 1
page_size = 100  # Increase page size for efficiency
all_results = []

try:
    api_url = f"{scs_base_url}/api/v1/scans/results"
    
    while True:
        results = get_scan_results(api_url, token, scan_category="vulnerabilities", page=page, size=page_size)
        
        current_data = results.get('data', [])
        
        # Extend all_results list with the current page's data
        all_results.extend(current_data)
        
        logger.info(f"Retrieved {len(current_data)} results from page {page}.")
        
        # Break if no more results are returned
        if not current_data or len(current_data) < 1:
            break
        
        page += 1  # Move to the next page

    # Write all results to a JSON file
    with open('scan_results.json', 'w') as json_file:
        json.dump(all_results, json_file, indent=4)

    logger.info(f"All {len(all_results)} results have been saved to scan_results.json.")

except Exception as e:
    logger.error(f"Failed to retrieve scan results: {e}")
    sys.exit(1)