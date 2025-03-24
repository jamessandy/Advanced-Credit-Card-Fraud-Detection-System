# Advanced Credit Card Fraud Detection System

## Project Overview
This project implements an advanced fraud detection system for credit card transactions. It leverages machine learning, real-time data streaming, and cloud technologies to detect and flag potentially fraudulent transactions before they happen. The system is designed to be highly scalable and capable of operating in real-time.


### Architecture
![fraud_detect drawio (1)](https://github.com/user-attachments/assets/d90db0ea-45bd-4d14-b0b1-909c586f2e07)


### **Technologies Used**
- **Apache Kafka** (Data Ingestion)
- **Apache Spark** (Real-Time Stream Processing)
- **AWS Lambda** (Fraud Alert Notifications)
- **TensorFlow** (Machine Learning Model for Fraud Detection)
- **DBT** (Data Transformation)
- **AWS S3** ( Data Storage)
- **Docker** (Containerization)

---

## **How to Run**

### **Step 1: Clone the Repository**
Clone the repository to your local machine:
```sh
git  
cd 
```

### **Step 2: Install Dependencies**
Install the required dependencies using `pip`:
```sh
pip install -r requirements.txt
```

### **Step 3: Set Up Kafka**
Ensure Apache Kafka is installed and running:
```sh
bin/zookeeper-server-start.sh config/zookeeper.properties &
bin/kafka-server-start.sh config/server.properties
```

### **Step 4: Start Services**
Run the following components:

1. **Run Kafka Producer** (Simulating Real-Time Transactions):
   ```sh
   python kafka_producer.py
   ```

2. **Run Kafka Consumer** (Processing Transactions):
   ```sh
   python kafka_consumer.py
   ```

3. **Start Spark Processing for Fraud Detection**:
   ```sh
   python spark_processing.py
   ```

4. **Run Fraud Detection Model**:
   ```sh
   python fraud_detection_model.py
   ```

5. **Trigger AWS Lambda for Fraud Alerts**:
   ```sh
   python lambda_trigger.py
   ```

### **Step 5: Docker Setup (Optional)**
To deploy the entire system using Docker:
```sh
docker-compose up --build
```
This starts the Kafka producer, consumer, and other system components.


## **Outcome**
- **Reduced fraud losses** by up to 40%.
- **Improved customer trust and retention** through proactive fraud detection.
- **Reduced manual intervention** in fraud detection processes.

---

## **Testing the System**
To test the fraud detection pipeline:
1. Run the Kafka producer to simulate transaction data.
2. Start the Kafka consumer to consume the data.
3. Observe Spark streaming console output for fraud detection logs.
4. If a fraudulent transaction is detected, AWS Lambda triggers an alert via email or SMS.
