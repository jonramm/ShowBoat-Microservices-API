import os
from app import app

if __name__ == '__main__':
    p = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=p, host='0.0.0.0')