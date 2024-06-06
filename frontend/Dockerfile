# Dockerfile for PHP Frontend
FROM php:7.4-apache

# Install dependencies
RUN apt-get update && apt-get install -y \
    libcurl4-openssl-dev \
    pkg-config \
    && docker-php-ext-install curl

# Copy application files
COPY . /var/www/html/

# Expose port 80
EXPOSE 80

