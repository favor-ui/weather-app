from app_core import app
from layout import layout

# set layout
app.layout = layout

# register callbacks after app exists
import callbacks  # noqa: E402,F401

if __name__ == '__main__':
    app.run(debug=True)
