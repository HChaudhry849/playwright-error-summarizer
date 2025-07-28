# 🔍 Playwright Error Summarizer (with OpenAI GPT)

This Python script helps you **summarize Playwright test errors** using OpenAI’s GPT model.  
It reads test output from a file, detects error blocks, and generates concise summaries and hints for fixing each error.

---

## 📦 Features

- Parses Playwright test logs from `playwright-errors.txt`
- Automatically splits logs into individual errors
- Sends each error block to OpenAI's GPT model
- Prints concise **summaries and hints** to the terminal

---

## 🧱 Prerequisites

- Python 3.8 or higher  
- Node.js and Playwright installed in your project  
- An OpenAI API key

---

## 🚀 Setup Guide

### 1. 📁 Place the Script

Place the provided folder (e.g., `playwright-error-summarizer`) in the root of your Playwright project, where `package.json` and your Playwright config are located.

---

### 2. 🧪 Modify Your `package.json`

Add custom script entries so you can run Playwright tests and log errors automatically. This helps you capture test output and run the summarizer with a single command.

---

Under the `"scripts"` section, add:

```json
"scripts": {
  "test": "powershell -Command \"npx playwright test | Tee-Object -FilePath playwright-errors.txt; Get-Content playwright-errors.txt\"",
  "logerror": "python playwright-error-summarizer/playwright_error_summarizer/main.py"
}
```

#### 💡 `npm run test`:
- Runs all Playwright tests  
- Saves terminal output to `playwright-errors.txt`  
- Displays output in the terminal

#### 💡 `npm run logerror`:
- Runs `main.py`  
- Sends errors to OpenAI GPT  
- Outputs summaries and fix hints in the terminal

---

### 3. 🔑 Set Up Your OpenAI API Key

Create a `.env` file in the root of the `playwright-error-summarizer` folder and add:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

Get your API key from: [OpenAI API Keys](https://platform.openai.com/account/api-keys)

> ⚠️ **Important:** Never commit your `.env` file to version control.

---

### 4. 📄 Install Python Dependencies

```bash
pip install -r requirements.txt
pip install -e .
```

---

### 5. ▶️ Run the Script

Once your Playwright tests are complete and `playwright-errors.txt` has been generated, run:

```bash
npm run logerror
```

This will generate and print GPT summaries of each detected error.

---

## 🧪 Example Output

**GPT response:**
```
- TimeoutError: Waiting for selector "#submit" failed.
  Hint: Check if the element appears only after a delay or under specific conditions.

- AssertionError: Expected text 'Success' but got 'Error'.
  Hint: Verify that your backend is returning the expected data.
```
