ARG BUILD_FROM
FROM $BUILD_FROM

# Install Python bridge dependencies
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copy bridge and UI
COPY bridge/ /app/bridge/
COPY ui/ /app/ui/

# Register s6 service
COPY services/bridge/run /etc/services.d/bridge/run
RUN chmod +x /etc/services.d/bridge/run

WORKDIR /app
ENV BRIDGE_PORT=8099
ENV RUVIEW_URL=http://localhost:3000
