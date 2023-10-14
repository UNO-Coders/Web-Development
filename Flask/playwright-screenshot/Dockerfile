# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim

#  Allow statements and log messages to immediately appear in the Knative logs
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED False
ENV PYTHONUNBUFFERED=0
ENV FLASK_ENV development
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1
ENV PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright

EXPOSE 5000

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

RUN apt-get clean
RUN apt-get update

# install manually all the missing libraries
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils
RUN PLAYWRIGHT_BROWSERS_PATH=/app/ms-playwright python -m playwright install --with-deps chromium

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
