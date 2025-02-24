#!/bin/bash

FILE=$1
BUCKET=$2
EXPIRATION=$3

aws s3 cp "$FILE" "s3://$BUCKET/$FILE"
aws s3 presign "s3://$BUCKET/$FILE" --expires-in "$EXPIRATION"

