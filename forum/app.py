from flask import Flask

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'kristofer',
    SITE_NAME="Schooner",
    SITE_DESCRIPTION="a schooner forum",
    IMAGES_PATH=['images'],
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db'
)
