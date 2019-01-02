#Project Flask MVC

__author__ = "indhifarhandika"
__version__ = "1"
__email__ = "indhifarhandika@gmail.com"

from project import app

if __name__ == '__main__':
    app.run(host="192.168.1.26", port=8000, debug=True)
