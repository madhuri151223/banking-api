set -e

source deploy.conf

echo "Starting deployment validation..."
echo "Application: $APP_NAME"
echo "Environment: $ENVIRONMENT"

if [ "$ENVIRONMENT" = "production" ] && [ "$MIN_INSTANCES" -lt 3 ]; then
    echo "ERROR: Production requires at least 3 instances"
    exit 1
fi

echo "Deployment validation passed"
echo "Deploying $APP_NAME on port $PORT..."
