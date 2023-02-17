# Project Flask MVC

__author__ = "indhifarhandika"
__version__ = "1"
__email__ = "indhifarhandika@gmail.com"

from src import create_app

if __name__ == "__main__":
    app = create_app()

    app.run(host="localhost", debug=True)
