#!/bin/bash
ENVIRONMENT="$1"
if [ -z "$ENVIRONMENT" ]; then
    echo "ERROR: Please provide an environment."
    echo "Usage: ./health-check.sh <environment>"
    exit 1
fi
echo "===== DEVOPS SYSTEM HEALTH CHECK ====="
echo "Environment: $ENVIRONMENT"
echo ""
echo "Hostname:"
hostname

echo ""
echo "Current user:"
whoami

echo ""
echo "Current directory:"
pwd

echo ""
echo "Disk usage:"
df -h /
echo ""
echo "Disk status:"

DISK_USAGE=$(df -P / | awk 'NR==2 {print $5}' | tr -d '%')

if [ "$DISK_USAGE" -lt 80 ]; then
    echo "OK - Disk usage is below 80%."
else
    echo "WARNING - Disk usage is 80% or higher."
fi

echo ""
echo "Memory usage:"
free -h

echo ""
echo "System uptime:"
uptime

echo ""
echo "===== CHECK COMPLETE ====="