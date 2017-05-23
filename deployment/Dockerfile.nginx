FROM nginx:alpine

# Replace the default nginx configuration with our own
RUN rm /etc/nginx/conf.d/default.conf
COPY deployment/nginx.conf /etc/nginx/conf.d/default.conf
