📄 Document Summarizer using Amazon Bedrock & Streamlit

A simple and fast PDF summarization app built with Amazon Bedrock (Claude Sonnet) and a clean Streamlit UI.
Upload a document → Enter a prompt → Get an instant AI-generated summary.

---
⚠️ Important Note About Usage & Billing

This project was created as part of an educational workshop environment, where Amazon Bedrock usage was free and pre-configured.

If you run this application on your personal AWS account, you will incur charges
because Amazon Bedrock is NOT included in the AWS Free Tier.

💰 Bedrock Pricing Reference

Please review the official pricing before running this application: 🔗 https://aws.amazon.com/bedrock/pricing/

📘 Bedrock Model Billing Documentation

🔗 https://docs.aws.amazon.com/bedrock/latest/userguide/pricing.html

If you want to avoid unexpected charges:

Disable Bedrock model access in your AWS account

Set up an AWS Billing Budget alert

Or run the UI without calling the Bedrock API

---
✨ Features

Upload PDF files

Custom summary instructions

AI-powered summarization using Amazon Bedrock

Clean two-column UI (input → output)

Lightweight and easy to run



---

🏗 Architecture



User → Streamlit UI → Backend (boto3) → Amazon Bedrock → Summary Output


---

🖥 UI Preview

[Final UI](docs/Final UI.jpg)


---

🚀 Run the App

pip install -r requirements.txt
aws configure
streamlit run app/app.py


---

🧰 Tech Stack

Amazon Bedrock – Converse API

Claude 3 Sonnet Model

Streamlit

Python 3

boto3



---

📌 Project Structure

app/                # Streamlit frontend
├── app.py
└── summarization_lib.py

docs/               # Screenshots & diagrams
├── Final UI.jpg
└── Archietecture.png

requirements.txt
.gitignore
README.md


⭐ Like this project?

Consider giving it a star ⭐ to support.

