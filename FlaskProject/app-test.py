from ast import For
import os
import threading
import time

dbName = 'Database_test'
dbPath = 'FlaskProject' + os.sep + 'DB' + os.sep + dbName + '.db'

if os.path.exists(dbPath):
    os.remove(dbPath)

from app_install import installDB, create_test_data

installDB()
create_test_data()


def run_app():
    from app import app
    app.run(port=3000, debug=False)

x = threading.Thread(target=run_app, daemon=True)

x.start()

time.sleep(600)