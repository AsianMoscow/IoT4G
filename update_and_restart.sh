#!/bin/bash

PROJECT_DIR="/home/pi/IoT4G"
LOG_FILE="/home/pi/iot4g_update.log"
SCRIPT_NAME="update_and_restart.sh"

cd "$PROJECT_DIR" || exit 1

echo "[$(date '+%Y-%m-%d %H:%M:%S')] [IoT4G] Проверка обновлений..." >> "$LOG_FILE"

# Сбрасываем все локальные изменения и подтягиваем master
git fetch origin >> "$LOG_FILE" 2>&1
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
chmod +x ./update_and_restart.sh

