#!/bin/bash

LOG_FILE="/home/pi/IoT4G/update.log"
echo "----- $(date '+%Y-%m-%d %H:%M:%S') -----" >> "$LOG_FILE"

APP_DIR="/home/pi/IoT4G"
SERVICE_NAME="iot4g"

cd "$APP_DIR" || exit

LOCAL_HASH=$(git rev-parse HEAD)
REMOTE_HASH=$(git ls-remote origin -h refs/heads/master | awk '{print $1}')

if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
    echo "[IoT4G] Обновление найдено! Pull..." >> "$LOG_FILE"
    
    git pull origin master >> "$LOG_FILE" 2>&1

    echo "[IoT4G] Перезапуск сервиса..." >> "$LOG_FILE"
    sudo systemctl restart "$SERVICE_NAME" >> "$LOG_FILE" 2>&1

    echo "[IoT4G] Готово!" >> "$LOG_FILE"
else
    echo "[IoT4G] Обновлений нет" >> "$LOG_FILE"
fi