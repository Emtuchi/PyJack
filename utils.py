import random
import time

# Random delay to mimic human behavior
def random_delay(min_sec=2, max_sec=5):
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)

# Clean text from HTML
def clean_text(text):
    return text.strip().replace('\n', ' ').replace('\r', '')

# Simple retry decorator for error handling
def retry(times=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e}. Retrying {attempt + 1}/{times}...")
                    time.sleep(2)
            return None
        return wrapper
    return decorator
