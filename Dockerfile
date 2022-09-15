### Build and install packages
FROM python:3.10

# Install Python dependencies
# WORKDIR /app
# COPY 
COPY src src
COPY setup.cfg setup.cfg
COPY setup.py setup.py
# COPY app.py  app.py

RUN python setup.py install

CMD ["monolith_web"]