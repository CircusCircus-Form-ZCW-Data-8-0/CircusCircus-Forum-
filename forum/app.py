from flask import Flask

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'kristofer',
    SITE_NAME="Data Cohort",
    SITE_DESCRIPTION="A Data Engineer Forum",
    SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db'
)
