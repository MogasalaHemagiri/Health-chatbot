# **Health Chatbot **

## **Overview**

This project is a **Mental Health Chatbot** that uses OpenAI's API to provide conversational support for mental health. It is built using **Flask** for the backend and **ReactJS** for the frontend. The bot responds to users' messages with empathetic and supportive responses to aid in mental wellness.

- **Backend**: Flask (Python)
- **Frontend**: ReactJS
- **API**: OpenAI's GPT model for generating responses
- **Docker**: Used for containerizing the app
- **Cloud Hosting**: Deployable on AWS, GCP, Azure, Heroku, Koyeb, and other cloud platforms.

## **Features**
- **AI-powered mental health support**: Provides conversational responses based on input.
- **Real-time chat interface**: Interactive chat UI built with ReactJS.
- **Secure API key handling**: The OpenAI API key is securely handled using environment variables.
- **Scalable and portable**: Can be containerized with Docker and deployed on cloud platforms.

---

## **Technologies Used**
- **Languages**: Python (Flask), JavaScript (ReactJS)
- **Backend Framework**: Flask (Python)
- **Frontend Framework**: ReactJS
- **API**: OpenAI's GPT (for generating responses)
- **Containerization**: Docker
- **Cloud Hosting**: AWS, GCP, Azure, Heroku, Koyeb
- **Environment Variable Handling**: Python-dotenv for securing API keys

---

## **How It Works**

1. **Frontend (ReactJS)**:
   - The ReactJS frontend collects the user’s input (message) from the text box.
   - The message is sent to the Flask backend via a **POST** request.
   - The frontend displays the bot’s response once it’s received from the backend.

2. **Backend (Flask)**:
   - The Flask backend receives the user input and sends it to OpenAI’s API.
   - OpenAI’s GPT model processes the input and returns a response.
   - The response is then sent back to the frontend to be displayed to the user.

3. **Environment Variables**:
   - The OpenAI API key is stored securely in a `.env` file.
   - The `.env` file is not committed to version control and is used to securely load the API key.

---

## **How to Run Locally**

### **Backend (Flask) Setup**
1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/mental-health-chatbot.git
   cd mental-health-chatbot/backend
   ```

2. **Install dependencies**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
   - Install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configure environment variables**:
   - Create a `.env` file in the `backend/` directory:
     ```bash
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Run the Flask app**:
   ```bash
   python app.py
   ```

5. The Flask API should now be running at `http://127.0.0.1:5000`.

### **Frontend (ReactJS) Setup**
1. **Navigate to the frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Run the React app**:
   ```bash
   npm start
   ```

4. The React app should now be accessible at `http://localhost:3000`.

---

## **Deploying with Docker**

### **Docker Setup**

1. **Build the Docker images**:
   - Make sure you are in the project root directory.
   - Run the following command to build both the frontend and backend Docker images:
     ```bash
     docker-compose build
     ```

2. **Run the Docker containers**:
   ```bash
   docker-compose up
   ```

   This will run the Flask backend and ReactJS frontend in separate containers and you will be able to access the app locally at `http://localhost:3000` (for React) and `http://localhost:5000` (for Flask).

---

## **Deploying to the Cloud**

You can deploy this project to various cloud platforms. Below are some brief instructions on how to deploy it to **AWS**, **GCP**, **Azure**, **Heroku**, and **Koyeb**.

### **1. AWS (Amazon Web Services)**
1. **Backend**:
   - Use **AWS Elastic Beanstalk** or **AWS EC2** to deploy the Flask API.
   - Set the environment variables for the OpenAI API key in the EC2 environment.

2. **Frontend**:
   - Deploy the React app to **AWS S3** or **AWS Amplify**.

### **2. GCP (Google Cloud Platform)**
1. **Backend**:
   - Deploy the Flask API on **Google App Engine** or **Google Compute Engine**.
   - Set the OpenAI API key in the GCP environment settings.

2. **Frontend**:
   - Deploy the React app using **Google Cloud Storage** or **Google Firebase Hosting**.

### **3. Azure**
1. **Backend**:
   - Deploy the Flask API using **Azure App Service**.
   - Set the OpenAI API key as an environment variable in the Azure configuration.

2. **Frontend**:
   - Host the React app on **Azure Blob Storage** or **Azure Static Web Apps**.

### **4. Heroku**
1. **Backend**:
   - Push the backend to **Heroku**:
     ```bash
     heroku create
     git push heroku master
     ```
   - Set the OpenAI API key in Heroku’s environment settings.

2. **Frontend**:
   - Deploy the React app using **Heroku**'s static buildpack.

### **5. Koyeb**
1. **Backend**:
   - Deploy the Flask app directly to **Koyeb** as a Docker container.
   - Set the OpenAI API key in Koyeb’s environment variables.

2. **Frontend**:
   - Deploy the React app using Koyeb's platform as a static site.

---

## **How to Ask Questions**

If you have any queries or need further assistance regarding this project, feel free to reach out via Telegram:

- **Telegram Contact**: [@networkdefender](https://t.me/networkdefender)

---

## **Requirements**

### **Backend (Flask)**
- **Python** 3.8 or above
- **Flask**
- **openai**
- **python-dotenv**

### **Frontend (ReactJS)**
- **Node.js** (v14 or above)
- **npm**

---

## **License**

This project is licensed under the Apache v3 License - see the [LICENSE](LICENSE) file for details.

---
