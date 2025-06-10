# Integrity Insurance WizardForm (Client Feedback Survey)

The Integrity Insurance WizardForm is a web-based survey application designed to collect post-appointment client feedback through an automated CRM workflow. The survey is accessible via a public link sent 24 hours after an appointment and securely stores encrypted responses in Firebase Firestore.

The form adapts to user input using conditional logic, prompting satisfied clients (rating 7 or higher) to leave a Google Review, while collecting internal improvement feedback from less satisfied users. Responses are stored securely using AES encryption via CryptoJS.

## Features

- **Multi-Step Survey**  
  Guided, step-by-step interface for capturing experience ratings, written feedback, and optional contact information.

- **Conditional Logic**  
  - Ratings ≥ 9: Prompt for Google Review  
  - Ratings 7–8: Ask what went well and what could improve  
  - Ratings ≤ 6: Directly request suggestions for improvement

- **Data Security**  
  - AES encryption via CryptoJS  
  - All data stored securely in Firebase Firestore

- **Responsive Design**  
  Mobile-friendly layout using media queries for clean display across screen sizes.

- **Accessibility**  
  - ARIA-compliant error handling  
  - Keyboard navigation (Enter to proceed, Backspace to go back)

- **Firebase Integration**  
  Survey submissions are securely written to a Firestore collection.

- **Internal Decryption Tool**  
  A separate admin-only HTML tool for decrypting and exporting collected feedback.

## File Structure

- `Survey.html` – Main form interface with embedded scripts and markup  
- `styles.css` – UI styling and branding (orange/blue palette)  
- `app.js` – Survey logic, input validation, Firebase integration, encryption  
- `config.js` – Public encryption key for securing data before submission  
- `Decryption Tool.html` – Standalone internal tool for decrypting/exporting data (requires private key)

## Setup Instructions

### Prerequisites

- Firebase project with Firestore enabled  
- AES public/private key pair (asymmetric encryption)  
- Static web hosting environment (e.g., Firebase Hosting, Netlify)

### Firebase Configuration

1. In `app.js`, replace the placeholder `firebaseConfig` object with your project credentials.
2. Confirm Firestore is enabled in your Firebase console.
3. Configure Firestore Security Rules to restrict access appropriately.

### Encryption Keys

- In `config.js`, insert your public encryption key in the placeholder.
- Use the private key within the `Decryption Tool.html` (only in secure environments).

### Hosting

- Upload `Survey.html`, `styles.css`, `app.js`, and `config.js` to a static host.
- Ensure links in `app.js` point to your Google Review page and confirmation landing page.

### CRM Integration

- Configure your CRM to send the survey URL 24 hours after each client appointment via automated workflow.
- Ensure the URL points to the hosted `Survey.html`.

### Decryption Tool

- Deploy `Decryption Tool.html` separately in a restricted-access environment.
- Logic for decrypting AES-encrypted submissions must be implemented internally (not provided in this repo).
- Tool should export decrypted responses to CSV for analysis or reporting.

## Survey Flow

1. **Rating (1–10)**  
   Collected via slider input.

2. **Feedback Prompt**  
   Dynamically generated based on rating:
   - High: "What did you like most?"
   - Mid-range: "What can we do better?"
   - Low: "What went wrong?"

3. **Follow-Up Contact (Optional)**  
   User asked whether they'd like to be contacted.

4. **Google Review Prompt** (Rating ≥ 9)  
   Redirects to external review page after submission.

5. **Name Input** (If contact requested)  
   Name collected for follow-up.

6. **Review & Submit**  
   Users confirm all inputs and submit securely.

## Data Storage

- Responses are AES-encrypted and stored in the `wizardformsubmissions` collection in Firestore.
- Each document includes timestamp, rating, feedback, optional name, and follow-up preference.

## Dependencies

- Firebase SDK (v9.17.2) – App initialization and Firestore  
- CryptoJS – AES encryption  
- No backend server required

## Styling

- **Brand Colors**  
  - Orange: `#f46c1c`  
  - Light Blue: `#067797`  
  - Dark Blue: `#005ea8`

- **Responsiveness**  
  Uses CSS media queries for phone and tablet support.

- **Accessibility**  
  ARIA attributes for input validation; keyboard support for navigation.

## Security

- **Encryption**  
  All data is AES-encrypted before storage; only authorized users with the private key can decrypt responses.

- **Validation**  
  Input constraints enforce alphabetic names and character limits for feedback fields.

- **Access Control**  
  Firestore rules should be configured to prevent unauthorized access.

## Notes

- Update all placeholder URLs in `app.js`:
  - Submission redirects
  - Google Review link

- The decryption tool requires private-key logic not included here.

- This project assumes that only authorized internal personnel will access decrypted survey data.

- Test survey logic thoroughly before deployment to ensure proper branching, validation, and redirect behavior.
