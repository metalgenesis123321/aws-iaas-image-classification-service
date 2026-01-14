# AWS IaaS Image Classification Service

A cloud-based image classification web service built on AWS IaaS (Infrastructure as a Service). This application provides an HTTP endpoint that accepts image uploads, stores them in S3, and retrieves pre-computed classification results from AWS SimpleDB.

## Architecture Overview

The system follows a simple request-response pattern:

1. Client sends an image via HTTP POST request
2. Web tier uploads the image to an S3 input bucket
3. Classification result is retrieved from SimpleDB (pre-populated lookup table)
4. Result is returned to the client

## Components

### Web Tier

A Flask-based web server running on EC2 that handles incoming HTTP requests.

**Responsibilities:**
- Accept multipart form data containing image files
- Upload received images to the designated S3 bucket
- Query SimpleDB for classification results
- Return classification results to clients

### AWS Services Used

| Service | Purpose |
|---------|---------|
| EC2 | Hosts the Flask web server |
| S3 | Stores uploaded image files |
| SimpleDB | Stores image classification mappings |

## Technical Details

**Framework:** Flask with Waitress WSGI server

**Endpoint:** `POST /`

**Request Format:** Multipart form data with `inputFile` field

**Response Format:** `{filename}:{classification}`

**Port:** 8000

**Concurrency:** 8 threads

## Prerequisites

- AWS Account with appropriate IAM permissions
- EC2 instance with Python 3.x installed
- Configured AWS credentials
- S3 bucket created and named appropriately
- SimpleDB domain populated with classification data

## Dependencies

```
flask
boto3
waitress
```

## Deployment

1. Launch an EC2 instance (Amazon Linux 2 or Ubuntu recommended)
2. Install Python dependencies
3. Configure AWS credentials on the instance
4. Create the S3 bucket and SimpleDB domain
5. Populate SimpleDB with image classification mappings
6. Run the server script

## Usage

```bash
curl -X POST -F "inputFile=@image.jpg" http://<ec2-public-ip>:8000/
```

## Project Context

This project was developed as part of a Cloud Computing course at Arizona State University, demonstrating fundamental concepts of IaaS deployment including EC2 instance management, S3 storage integration, and NoSQL database queries with SimpleDB.
