import requests
import time


def fetcher(url, session):
    max_attempts = 3
    retryable_status_codes = {429, 500, 503}
    for attempt in range(1, max_attempts + 1):
        try:
            response = session.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.HTTPError as e:
            status_code = e.response.status_code
            if status_code in retryable_status_codes:
                if attempt < max_attempts:
                    time.sleep(2 ** attempt)
                    continue
                else:
                    raise
            else:
                raise    
        except requests.RequestException as e:
            if attempt < max_attempts:
               time.sleep(2 ** attempt)
               continue
            else:
                raise

    