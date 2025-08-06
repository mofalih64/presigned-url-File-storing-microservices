#!/bin/bash
set -e

# Connect params
POSTGRES_USER="${POSTGRES_USER:-user}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-password}"
export PGPASSWORD="$POSTGRES_PASSWORD"

function create_db_if_not_exists() {
  local db=$1
  echo "Checking if database '$db' exists..."
  if psql -U "$POSTGRES_USER" -d postgres -tc "SELECT 1 FROM pg_database WHERE datname = '$db'" | grep -q 1; then
    echo "Database '$db' already exists."
  else
    echo "Creating database '$db'..."
    createdb -U "$POSTGRES_USER" "$db"
  fi
}

create_db_if_not_exists "commerce_db"
create_db_if_not_exists "files_db"
