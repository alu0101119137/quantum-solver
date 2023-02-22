FROM python:3.8.16-bullseye

WORKDIR /app

ENV FLASK_APP=flask-server/server.py
ENV FLASK_DEBUG=development

# Bundle app source
COPY flask-server/ ./flask-server
COPY pyproject.toml/ ./pyproject.toml
COPY setup.cfg ./setup.cfg
COPY README.md ./README.md
COPY src/ ./src


RUN python -m pip install -e .
RUN pip install flask && pip install -U flask-cors && pip install APScheduler && pip install pylatexenc

COPY . .

EXPOSE 5000

CMD [ "python3", "flask-server/server.py" ]