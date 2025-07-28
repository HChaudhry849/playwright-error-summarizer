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
Save the provided folder (e.g., playwright-error-summarizer) in the root of your Playwright project, where package.json and your Playwright config are located.
2. 🧪 Modify Your package.json Script
In package.json, under "scripts", add the following commands:
"test": "powershell -Command \"npx playwright test | Tee-Object -FilePath playwright-errors.txt; Get-Content playwright-errors.txt\""
"logerror":"python playwright-error-summarizer/playwright_error_summarizer/main.py" 
💡 "npm run test" command:
Runs all your Playwright tests
Saves the terminal output to playwright-errors.txt
Displays the output in the terminal as well
💡 "npm run logerror" command:
Runs the main.py
It will send the errors to OpenAI GPT
It will get a response back in the form of a error summary and fix hints
3. 🔑 Set Up Your OpenAI API Key
a. Create a .env file in the root of the playwright-error-summarizer and add open api key:
OPENAI_API_KEY=your_openai_api_key_here
You can get your API key from: https://platform.openai.com/account/api-keys
⚠️ Important: Never commit your .env file to version control.
4. 📄 Install Python Dependencies
pip install -r requirements.txt
pip install -e .
5. ▶️ Run the Script
Once your Playwright tests are complete and playwright-errors.txt has been generated, run the summarizer:
npm run logerror
This will output a GPT-generated summary of each detected error in the terminal.
🧪 Example Output
GPT response:
1. TimeoutError: Waiting for selector "#submit" failed. Hint: Check if the element appears only after a delay or under specific conditions.
2. AssertionError: Expected text 'Success' but got 'Error'. Hint: Verify that your backend is returning the expected data.