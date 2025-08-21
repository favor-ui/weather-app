from app_core import app
from layout import layout
import callbacks  # noqa: E402,F401

# set layout
app.layout = layout

# register callbacks after app exists

if __name__ == '__main__':
    app.run(debug=True)
