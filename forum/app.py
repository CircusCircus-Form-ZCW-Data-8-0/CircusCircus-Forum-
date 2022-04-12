from flask import Flask

app = Flask(__name__)
app.config.update(
    TESTING=True,
    SECRET_KEY=b'kristofer',
	SITE_NAME = "Schooner1",
	SITE_DESCRIPTION = "a schooner forum",
	SQLALCHEMY_DATABASE_URI='sqlite:////tmp/database.db',
	COPYRIGHT = 'DATA 3.0-8.0? © 2022'
)
