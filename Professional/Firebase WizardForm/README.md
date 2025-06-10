The Integrity Insurance WizardForm is a web-based survey application designed to collect client feedback 24 hours after their appointment. It is automatically distributed via a CRM workflow and uses Firebase for secure data storage with asymmetrical encryption. The form guides users through a multi-step process to gather experience ratings, feedback, and optional names, funneling satisfied clients (rating 7 or higher) toward leaving Google Reviews to maximize positive public feedback while collecting improvement insights from less satisfied clients.

Features

Multi-Step Survey: A user-friendly, step-by-step interface for collecting ratings, feedback, and optional user information.
Conditional Logic: Users with ratings of 7 or higher are prompted to leave a Google Review, while others are directed to provide feedback for internal improvement.
Data Security: Utilizes asymmetrical encryption (via CryptoJS AES) to securely store user data in Firebase Firestore.
Responsive Design: Mobile-friendly interface with CSS media queries for optimal display across devices.
Accessibility: Supports keyboard navigation (Enter for next, Backspace for previous) and includes ARIA attributes for error handling.
Firebase Integration: Stores encrypted survey responses in a Firestore database.
Dynamic Feedback Prompts: Customizes feedback questions based on user ratings (e.g., "What did you like the most?" for high ratings).

File Structure

config.js: Contains the encryption key for securing data.
Survey.html: The main survey interface with a multi-step form for collecting user input.
Decryption Tool.html: A tool for viewing and exporting decrypted survey submissions to CSV (for internal use).
styles.css: Styles for the survey and decryption tool, featuring Integrity Insurance branding (e.g., orange borders, blue buttons).
app.js: Core logic for the survey, including Firebase integration, encryption, step navigation, and input validation.

Setup Instructions

Prerequisites:

Node.js (for local development, if needed).
A Firebase project with Firestore enabled.
Assymetrical encryption keys for data security.


Firebase Configuration:

Replace placeholders in app.js (firebaseConfig) with your Firebase project credentials (apiKey, authDomain, projectId, etc.).
Ensure Firestore is enabled in your Firebase console.


Encryption Key:

Insert your public encryption key in config.js where <INSERT_PUBLIC_KEY> is specified. Insert your private encryption key in the Decryption Tool. 


Deployment:

Host the application on a web server (e.g., Firebase Hosting, Netlify, or any static hosting service).
Update redirect URLs in app.js (submitSurveyNormal and submitSurveyGoogle) to point to your desired destinations (e.g., company website, Google Review page).


CRM Integration:

Configure your CRM to send survey links to clients 24 hours post-appointment using a workflow automation tool.
Ensure the survey URL points to the hosted Survey.html.


Decryption Tool:

Deploy Decryption Tool.html separately for internal use, ensuring only authorized personnel can access it.
Implement decryption logic (not provided in the code) to view and export survey data.



Usage

Survey Flow:
Step 1: Users rate their experience (1-10) using a slider.
Step 2: Users provide feedback based on their rating (e.g., "What can we do to improve?" for ratings 7-8).
Step 3: Users are asked if they want to be contacted (or thanked for high ratings).
Step 4 (if rating ≥ 9): Users are prompted to leave a Google Review.
Step 5 (if contact requested): Users enter their name.
Step 6: Users review and submit their responses.


Data Storage: Responses are encrypted and stored in Firestore under the wizardformsubmissions collection.
Google Review Funnel: Users with ratings ≥ 7 are encouraged to leave a Google Review, increasing 5-star visibility.
Decryption Tool: Internal tool to decrypt and export submissions to CSV for analysis.

Dependencies

Firebase SDK (v9.17.2): For Firestore database and app initialization.
CryptoJS: For AES encryption of survey data.
External Hosting: Required for serving HTML, CSS, and JS files.

Styling

Branding: Uses Integrity Insurance colors (orange: #f46c1c, blue: #067797, #005ea8).
Responsive Design: Adapts to mobile and tablet screens with media queries.
Accessibility: Includes error messaging with ARIA attributes and keyboard navigation support.

Security

Data Encryption: All survey responses are encrypted using AES before storage in Firestore.
Input Validation: Ensures valid names (alphabets and spaces only) and feedback length (< 500 characters).
Firebase Security Rules: Configure Firestore rules to restrict access to authorized users only.

Notes

Replace placeholder URLs in app.js (https://www.placeholder.com/ and https://g.placeholder.com) with actual redirect links.
The decryption tool (Decryption Tool.html) requires additional logic to decrypt and display data, which is not included in the provided code.
Ensure Firebase configuration is complete to avoid data storage issues.
Test the survey flow thoroughly to confirm step navigation and conditional logic work as expected.

Contact
For issues or inquiries, contact Integrity Insurance at (720) 990-1680.
