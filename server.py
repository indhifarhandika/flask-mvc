# Project Flask MVC

__author__ = "indhifarhandika"
__version__ = "1"
__email__ = "indhifarhandika@gmail.com"

from src import app

if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)
