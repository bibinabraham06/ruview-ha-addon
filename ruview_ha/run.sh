#!/usr/bin/with-contenv bashio

# Read add-on options
LOG_LEVEL=$(bashio::config 'log_level' 'info')
SCAN_INTERVAL=$(bashio::config 'scan_interval' '1')
INTRUSION_MODE=$(bashio::config 'intrusion_mode' 'false')

# Export env vars consumed by the Python bridge
export LOG_LEVEL="${LOG_LEVEL^^}"
export SCAN_INTERVAL="$SCAN_INTERVAL"
export INTRUSION_MODE="$INTRUSION_MODE"
export BRIDGE_PORT="${BRIDGE_PORT:-8099}"
export RUVIEW_URL="http://localhost:3000"

bashio::log.info "Starting RuView sensing-server (simulation mode)..."

# Start RuView sensing-server in the background
/usr/local/bin/sensing-server \
    --source simulation \
    --tick-ms 100 \
    --http-port 3000 \
    --ws-port 3001 &

# Wait for sensing-server to be ready
bashio::log.info "Waiting for sensing-server to initialize..."
sleep 3

bashio::log.info "Starting bridge server on port ${BRIDGE_PORT}..."

# Run bridge in foreground (container exits if bridge dies)
exec python3 -m bridge.main
