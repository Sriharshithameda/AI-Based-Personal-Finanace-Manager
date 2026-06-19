**📊 AI Based Personal Financial Manager**

An AI-powered personal finance management system built using FastAPI, Streamlit, SQLAlchemy, SQLite, and Gemini AI. The application helps users track expenses, categorize transactions, monitor budgets, visualize spending patterns, and receive AI-generated financial insights.

**🚀 Features**
**-->🔐 User Authentication**
User Registration
Login with JWT Authentication
Secure access to personal data
**-->💸 Expense Management**
Add transactions
Delete transactions
View transaction history
Automatic expense categorization
**-->🎤 Voice Expense Entry**
Add expenses using speech recognition
Converts voice to text automatically
**-->📊 Analytics Dashboard**
Category-wise expense distribution
Pie chart visualization
Monthly spending analysis
**-->💰 Budget Tracking**
Set monthly budget

**View:**
Total spent amount
Remaining budget
Budget exceeded warnings
**🤖 AI Features**
AI Spending Advice
AI Monthly Financial Report
AI Financial Chat Assistant
**📈 Data Visualization**
Matplotlib Pie Charts
Category-wise analysis

**🏗 System Architecture**
User
   ↓
Streamlit Frontend
   ↓
FastAPI Backend
   ↓
SQLAlchemy ORM
   ↓
SQLite Database
   ↓
Gemini AI API


**🛠 Technologies Used**
Frontend
Streamlit
Matplotlib
SpeechRecognition
Backend
FastAPI
Uvicorn
Database
SQLite
SQLAlchemy
AI
Google Gemini API
Authentication
JWT Token Authentication
Programming Language
Python 3.12

**📂 Project Structure**
AI_FIN/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   ├── utils.py
│
├── frontend/
│   └── app.py
│
├── requirements.txt
├── README.md
└── finance.db

**⚙ Installation**
1. Clone Repository
git clone https://github.com/your-username/AI-Financial-Manager.git
cd AI-Financial-Manager
2. Install Dependencies
pip install -r requirements.txt
3. Start Backend
cd backend
uvicorn main:app --reload
Backend runs on:
http://127.0.0.1:8000
4. Start Frontend
cd frontend
streamlit run app.py
Frontend runs on:
http://localhost:8501

**📊 Modules**
Authentication Module
Register user
Login user
JWT token generation
Transaction Module
Add expenses
Delete expenses
Fetch transaction history
Analytics Module
Monthly spending summary
Category-wise expenditure
Budget Module
Budget setting
Remaining budget calculation
AI Module
AI Spending Advice
AI Financial Reports
Financial Chat Assistant
Voice Module
Speech-to-text expense entry

**🧠 Algorithms Used**
Rule-Based Expense Categorization Automatically classifies expenses into categories like:
->Food
->Travel
->Shopping
->Entertainment
->Utilities
->Budget Analysis Algorithm
->Remaining Budget = Budget − Total Spent
->Pie Chart Generation

**Using Matplotlib:**

ax.pie(amounts, labels=categories, autopct="%1.1f%%")
JWT Authentication Algorithm

Secure user authentication and authorization.

SQLAlchemy ORM

Database interaction and CRUD operations.

Speech Recognition Algorithm

Converts spoken expenses into text input.

Generative AI Algorithm

**Google Gemini generates:**

Financial advice
Monthly reports
Answers to financial queries
💻 Hardware Requirements
Component	Requirement
Processor	Intel i3 or above
RAM	4 GB minimum
Storage	1 GB free space
Internet	Required for AI services
Microphone	For voice expense entry

**🖥 Software Requirements**
Software	Version
Python	3.12
Streamlit	Latest
FastAPI	Latest
SQLAlchemy	Latest
Uvicorn	Latest
Matplotlib	Latest
Pandas	Latest
SpeechRecognition	Latest
SQLite	Built-in
VS Code	Recommended


**👩‍💻 Author**

Meda Sri Harshitha
B.Tech Student
AI & Full Stack Enthusiast
