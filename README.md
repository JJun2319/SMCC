# **SMCC Automation Process**  

## **Core Mechanism**  
The key `XHR` file is received as a URL response, where the URL follows a structured pattern with predictable variations based on lesson progression.  

For a given **Week X** and **Problem Y**, the request follows this format:  

https://www.scholars.kr/pc/dictation_play_data.php?bookno=XXXX&bpage=YYYY

The response is in `JSON` format, which needs to be parsed into a dictionary.  

### **Example Response:**  

```json
{
  "etxt": "How many things do you throw away everyday?",
  "ktxt": "",
  "epara": "",
  "kmean": "",
  "filename1": "b511206442413.mp3"
}

Automation Workflow
	1.	Determine the Current Week:
	•	Identify the current lesson week and store its corresponding bookno.
	2.	Retrieve Problem Count & Current Progress:
	•	Extract the total number of problems in the lesson and track the current problem index.
	3.	Automate Answer Submission:
	•	Iterate through all problems sequentially.
	•	Extract the etxt field from the parsed dictionary.
	•	Automatically copy and paste the extracted text into the answer input field.
	•	Simulate an Enter key press to submit the answer.

This structured approach ensures a fully automated workflow for handling dictation exercises efficiently.

