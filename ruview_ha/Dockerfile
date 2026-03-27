# ruview-ha-addon/Dockerfile
ARG BUILD_FROM
FROM $BUILD_FROM

ARG TARGETARCH

# Install RuView binary (TARGETARCH is injected by Docker buildx)
RUN apk add --no-cache curl && \
    ARCH=$([ "$TARGETARCH" = "arm64" ] && echo "aarch64" || echo "x86_64") && \
    curl -fsSL https://github.com/ruvnet/RuView/releases/latest/download/ruview-linux-${ARCH}.tar.gz \
    | tar -xz -C /usr/local/bin/ && \
    chmod +x /usr/local/bin/ruview

# Install Python bridge deps
COPY requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Copy bridge and UI
COPY bridge/ /app/bridge/
COPY ui/ /app/ui/

WORKDIR /app
ENV BRIDGE_PORT=8099
CMD ["python3", "-m", "bridge.main"]
