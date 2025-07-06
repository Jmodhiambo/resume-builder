#!/usr/bin/env bash
set -e

# Load environment variables
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
else
  echo ".env file not found!"
  exit 1
fi

# Install PostgreSQL if not installed
if ! command -v psql > /dev/null; then
  echo "🔧 Installing PostgreSQL..."
  sudo apt update -y
  sudo apt install -y postgresql postgresql-contrib libpq-dev
else
  echo "ℹ️ PostgreSQL already installed."
fi

# Create PostgreSQL user and database
echo "🛠️ Setting up PostgreSQL user and database..."

: "${PG_USER:?Need to set PG_USER}"
: "${PG_PASS:?Need to set PG_PASS}"
: "${PG_DB:?Need to set PG_DB}"

sudo -u postgres psql <<EOF
DO \$\$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_user
      WHERE usename = '$PG_USER'
   ) THEN
      CREATE USER $PG_USER WITH PASSWORD '$PG_PASS';
   END IF;
END
\$\$;
EOF

DB_EXISTS=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='$PG_DB'")

if [ "$DB_EXISTS" != "1" ]; then
    sudo -u postgres psql -c "CREATE DATABASE $PG_DB OWNER $PG_USER"
fi

# Create DATABASE_URL and append to .env if not present
DB_URL="postgresql://${PG_USER}:${PG_PASS}@${PG_HOST}/${PG_DB}"
if ! grep -q DATABASE_URL .env; then
  echo "DATABASE_URL=$DB_URL" >> .env
  echo "✅ DATABASE_URL added to .env"
else
  echo "ℹ️ DATABASE_URL already exists in .env"
fi

if ! grep -q '^SECRET_KEY=' .env; then
  echo "SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')" >> .env
else
    echo "SECRET_KEY already exists in .env"
fi

# Check DB connection
echo "🔗 Checking database connection..."
if PGPASSWORD="$PG_PASS" psql -h "$PG_HOST" -U "$PG_USER" -d "$PG_DB" -c '\q' 2>/dev/null; then
  echo "✅ Successfully connected to database $PG_DB."
else
  echo "❌ Could not connect to database $PG_DB. Please check your credentials and PostgreSQL service."
  exit 1
fi


# Run db.create_all() from Flask shell
echo "📦 Creating tables via db.create_all()..."
export $(grep -v '^#' .env | xargs)  # Reload after .env edit
flask shell <<EOF
from app import db, models
db.drop_all()
db.create_all()
EOF

# Check if tables exist
echo "🔍 Verifying tables were created..."
TABLE_COUNT=$(PGPASSWORD="$PG_PASS" psql -h "$PG_HOST" -U "$PG_USER" -d "$PG_DB" -tAc "SELECT count(*) FROM information_schema.tables WHERE table_schema='public';")
if [ "$TABLE_COUNT" -gt 0 ]; then
  echo "✅ $TABLE_COUNT tables found in $PG_DB."
else
  echo "❌ No tables found in $PG_DB. Please check your models and db.create_all() output."
  exit 1
fi

echo "✅ Setup complete and PostgreSQL tables created."
