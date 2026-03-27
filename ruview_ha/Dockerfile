ARG BUILD_FROM

# Stage 1: extract sensing-server binary from official RuView image
FROM ruvnet/wifi-densepose:latest AS ruview-source

# Stage 2: HA add-on image (debian-based for glibc compatibility with sensing-server)
FROM $BUILD_FROM

# Install Python 3 and pip (debian base doesn't include them)
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Copy RuView sensing-server binary from official image
COPY --from=ruview-source /app/sensing-server /usr/local/bin/sensing-server
RUN chmod +x /usr/local/bin/sensing-server

# Install Python bridge dependencies
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir --break-system-packages -r /tmp/requirements.txt

# Copy bridge and UI
COPY bridge/ /app/bridge/
COPY ui/ /app/ui/

# Copy startup script
COPY run.sh /run.sh
RUN chmod +x /run.sh

WORKDIR /app
ENV BRIDGE_PORT=8099

CMD ["/run.sh"]
