# ruview-ha-addon/Dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

# Install RuView binary
RUN apk add --no-cache curl && \
    curl -fsSL https://github.com/ruvnet/RuView/releases/latest/download/ruview-linux-$(uname -m).tar.gz \
    | tar -xz -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/ruview

# Install Python bridge deps
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copy bridge and UI
COPY bridge/ /app/bridge/
COPY ui/ /app/ui/

WORKDIR /app
CMD ["python3", "-m", "bridge.main"]
