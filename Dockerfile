FROM  python:3.11.3-slim-bullseye

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Coy package.json and package-lock.json to container
COPY  requirements.txt  requirements.txt


COPY * .

# Install dependencies

RUN pip install --upgrade pip && pip install mysqlclient  &&  pip install -r requirements.txt




# Expose the port your app runs on

EXPOSE 5002


# Command to run your application
CMD ["python", "app.py" ]