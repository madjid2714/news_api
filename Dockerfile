
# Use an official Python runtime as a parent image
FROM python:3.8

#RUN apt-get update && apt-get install -y postgresql-client

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create a directory for the application code
RUN mkdir -p /usr/src/app

# Set the working directory in the container
WORKDIR /usr/src/app/

# Change ownership of the directory to the user running the application
RUN chown -R root:root /usr/src/app

# Set permissions for the directory
# RUN chmod -R 755 /usr/src/app

COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set Django settings module
ENV DJANGO_SETTINGS_MODULE=news_backend.settings


COPY ./init.sh /usr/local/bin/
RUN sed -i 's/\r$//g' /usr/local/bin/init.sh
# RUN chown -R root:root /usr/local/bin/init.sh
RUN chmod +x /usr/local/bin/init.sh
#ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]


# Expose port 8000 to the outside world
# EXPOSE 8000
