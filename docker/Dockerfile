# Use the official Nginx image as the base image
FROM nginx:latest

# Remove the default Nginx welcome page
RUN rm /usr/share/nginx/html/*

# Copy your custom HTML and application code into the Nginx server directory
COPY index.html /usr/share/nginx/html/
COPY app.py /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start Nginx when the container runs
CMD ["nginx", "-g", "daemon off;"]
