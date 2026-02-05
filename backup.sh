#!/bin/bash
DATE=$(date +"%Y-%m-%d")
cp database.json backups/db_$DATE.json
