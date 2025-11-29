#!/bin/bash

PROJECT_DIR="/home/pi/IoT4G"
LOG_FILE="/home/pi/iot4g_update.log"
SCRIPT_NAME="update_and_restart.sh"

cd "$PROJECT_DIR" || exit 1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] [IoT4G] Проверка обновлений..." >> "$LOG_FILE"

# Получаем актуальный master с GitHub
git fetch origin >> "$LOG_FILE" 2>&1

# Проверяем, есть ли изменения
LOCAL_HASH=$(git rev-parse HEAD)
REMOTE_HASH=$(git rev-parse origin/master)

if [ "$LOCAL_HASH" != "$REMOTE_HASH" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [IoT4G] Найдены обновления, применяем..." >> "$LOG_FILE"

    # Сбрасываем локальные изменения и подтягиваем master
    git reset --hard origin/master >> "$LOG_FILE" 2>&1

    # Восстанавливаем флаг +x для самого скрипта
    chmod +x "$PROJECT_DIR/$SCRIPT_NAME"

    # Активируем виртуальное окружение, если есть
    if [ -f "$PROJECT_DIR/.venv/bin/activate" ]; then
        source "$PROJECT_DIR/.venv/bin/activate"
    fi

    # Перезапускаем systemd-сервис
    sudo systemctl restart iot4g >> "$LOG_FILE" 2>&1

    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [IoT4G] Обновление завершено, сервис перезапущен." >> "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [IoT4G] Обновлений нет." >> "$LOG_FILE"
fi
