from pymongo import MongoClient
import time

def connect_mongodb(max_retries=3, retry_delay=2):
    """
    Establish MongoDB connection with retry logic
    
    Args:
        max_retries (int): Maximum number of connection attempts
        retry_delay (int): Delay in seconds between retries
        
    Returns:
        tuple: (MongoClient, database) or (None, None) on failure
    """
    for attempt in range(max_retries):
        try:
            client = MongoClient('mongodb://localhost:27017/',
                               serverSelectionTimeoutMS=5000,
                               connectTimeoutMS=5000)
            
            # Test connection
            client.server_info()
            print(f"[SUCCESS] MongoDB connection successful (attempt {attempt + 1})")
            
            # Get database
            db = client['sih2573']
            
            # Initialize collections and indexes
            users = db['users']
            height_videos = db['height_videos']
            exercise_sessions = db['exercise_sessions']
            exercise_results = db['exercise_results']
            
            # Create indexes
            users.create_index('email', unique=True)
            exercise_sessions.create_index([('user_id', 1), ('date', -1)])
            exercise_results.create_index([('session_id', 1)])
            exercise_results.create_index([('user_id', 1), ('analyzed_at', -1)])
            
            return client, db
            
        except Exception as e:
            print(f"MongoDB connection attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print("Failed to connect to MongoDB after all retries")
                return None, None
                
    return None, None

def get_db():
    """
    Get database connection, handling reconnection if needed
    """
    client, db = connect_mongodb()
    return db if db else None