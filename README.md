🔍 Playwright Error Summarizer (with OpenAI GPT)
This Python script helps you summarize Playwright test errors using OpenAI’s GPT model. It reads test output from a file, detects error blocks, and uses the OpenAI API to generate short summaries and hints for fixing each error.
📦 Features
Parses Playwright test logs from playwright-errors.txt
Automatically splits logs into individual errors
Sends each error block to OpenAI's GPT model for summarization
Prints concise summaries and hints to the terminal
🧱 Prerequisites
Python 3.8 or higher
Node.js and Playwright installed in your project
An OpenAI API key
🚀 Setup Guide
1. 📁 Place the Script
Save the provided Python script (e.g., summarise_errors.py) in the root of your Playwright project, where package.json and your Playwright config are located.
2. 🧪 Modify Your package.json Script
In package.json, under "scripts", add the following command:
json
CopyEdit
"test": "powershell -Command \"npx playwright test | Tee-Object -FilePath playwright-errors.txt; Get-Content playwright-errors.txt\""
💡 This command:
Runs all your Playwright tests
Saves the terminal output to playwright-errors.txt
Displays the output in the terminal as well
Run this test with:
bash
CopyEdit
npm run test
3. 🔑 Set Up Your OpenAI API Key
a. Create a .env file in the root of your project:
env
CopyEdit
OPENAI_API_KEY=your_openai_api_key_here
You can get your API key from: https://platform.openai.com/account/api-keys
⚠️ Important: Never commit your .env file to version control.
4. 📄 Install Python Dependencies
a. Create a requirements.txt file:
txt
CopyEdit
openai
python-dotenv
b. Install the dependencies:
bash
CopyEdit
pip install -r requirements.txt
5. ▶️ Run the Script
Once your Playwright tests are complete and playwright-errors.txt has been generated, run the summarizer:
bash
CopyEdit
python summarise_errors.py
This will output a GPT-generated summary of each detected error in the terminal.
🧪 Example Output
sql
CopyEdit
GPT response:
1. TimeoutError: Waiting for selector "#submit" failed. Hint: Check if the element appears only after a delay or under specific conditions.
2. AssertionError: Expected text 'Success' but got 'Error'. Hint: Verify that your backend is returning the expected data.
✅ Tips
Make sure summarise_errors.py is in the same directory as your Playwright package.json.
If the script cannot find the playwright-errors.txt file, ensure that you've run npm run test and that PowerShell is available on your system.
🛠 File Overview
File
Purpose
summarise_errors.py
Python script that parses and summarizes errors
.env
Stores your OpenAI API key securely
requirements.txt
List of Python dependencies
playwright-errors.txt
Generated after running Playwright tests