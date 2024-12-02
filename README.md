# **Pay Microservice Project**

## **📜 Overview**

Pay is a microservice-based financial transaction management system. It features a robust architecture to handle user authentication, service verification, money transfer, and payment scheduling. With the integration of **Celery Beat**, the system now supports automatic periodic payments post successful transactions, ensuring seamless and reliable auto-payment processes.

---

## **🚀 Key Features**

* **Authentication Services**:  
  * User Registration and Login.  
  * Token-based authentication using **access** and **refresh tokens**.  
* **Service Verification**:  
  * Verifies service credentials and generates authentication tokens.  
* **Money Transfer Service**:  
  * Facilitates secure financial transactions.  
  * Option for enabling automatic recurring payments with scheduled service integration.  
* **Payment Scheduling**:  
  * Stores scheduled payments to be executed periodically using **Celery Beat**.


---

## **🛠️ Technology Stack**

* **Backend Framework**: Django, Django Rest Framework  
* **Task Queue**: Celery  
* **Task Scheduler**: Celery Beat  
* **Database**: PostgreSQL 
* **Communication**: RESTful APIs  

---

## **🔄 Auto Payment Process**

### **Workflow**

1. Upon successful money transfer, if **auto pay** is enabled, a scheduled task is created in the `scheduler_service`.  
2. **Celery Beat** periodically checks and triggers payments as per the schedule.  
3. Payments are processed securely, ensuring compliance with user preferences and transaction records are updated in real-time.

---

## **🧪 API Endpoints**

### **Auth Service**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | `/auth/register/` | Register a new user. |
| POST | `/auth/login/` | Login and get tokens. |

### **Authenticate Service**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | `/service/verify/` | Verify service credentials. |
| POST | `/service/get-token/` | Generate access and refresh tokens. |

### **Money Transfer Service**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | `/transfer/` | Transfer money with optional auto-pay. |

### **Scheduler Service**

| Method | Endpoint | Description |
| ----- | ----- | ----- |
| POST | `/scheduler/create/` | Schedule a recurring payment. |

---

## **📝 Future Enhancements**

* Real-time notifications for payment status.  
* Enhanced analytics dashboard for transaction monitoring.  
* Integration with third-party services for extended functionality.

---

## **🤝 Contribution**

Feel free to submit issues or pull requests to improve the project.
