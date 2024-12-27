from api import app
from dotenv import load_dotenv
import os

#Load environment variables
load_dotenv()

if __name__ == '__main__':
    debug_mode = os.getenv("DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode)
