import { encryptionKey } from "./config.js";
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-app.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/9.17.2/firebase-firestore.js";
const firebaseConfig = {
	apiKey: "PLACEHOLDER",
	authDomain: "PLACEHOLDER",
	projectId: ""PLACEHOLDER"",
	storageBucket: ""PLACEHOLDER"",
	messagingSenderId: "143816382294",
	appId: "1:143816382294:web:9a6800e35eae32b06028f7",
	measurementId: "G-9Z2RB12JJF"
};	
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);		
let userRating = null;
let userFeedback = "NA";
let userName = "Anonymous";
let currentStep = null;
let step3offered = false;
let step4offered = false;
const DEBUG = false;
const stepButtons = {
	1: { next: 'nextButton1' },
	2: { next: 'nextButton2', back: 'backButton2' },
	3: { nextYes: 'yesButton3', nextNo: 'noButton3', back: 'backButton3' },
	4: { nextYes: 'yesButton4', nextNo: 'noButton4', back: 'backButton4' },
	5: { next: 'nextButton5', back: 'backButton5' },
	6: { back: 'backButton6' }
};
const headers = {
	high: "What did you like the most?",
	medium: "What can we do to improve the experience?",
	low: "What is the main reason for your score?",
};		
function log(message) {
	if (DEBUG) console.log(message);
}		
function encryptData(data, key) {
	return CryptoJS.AES.encrypt(JSON.stringify(data), key).toString();
}		
async function createNewSubmission(rating, feedback, name) {
	if (!firebaseConfig.apiKey) {
		console.warn("Firebase not configured. Data will not be saved.");
		return "debug-id";
	}
	const encryptedData = encryptData({ rating, feedback, name }, encryptionKey);
	try {
		const docRef = await addDoc(collection(db, "wizardformsubmissions"), {
			encryptedPayload: encryptedData
		});
		console.log(`New document created with ID: ${docRef.id}`);
		return docRef.id;
	} catch (error) {
		console.error("Error creating document:", error);
		alert("We're having trouble saving your response. Please try again or contact us at (720) 990-1680. We apologize for the inconvenience.");
		throw error;
	}
}
function clearErrors(fieldId) {
	const field = document.getElementById(fieldId);
	const error = field.parentNode.querySelector('.error');
	if (error) {
		error.remove();
	}
}				
function showError(message, fieldId) {
	clearErrors(fieldId);
	const field = document.getElementById(fieldId);
	const error = document.createElement('span');
	error.className = 'error';
	error.setAttribute('aria-live', 'polite');
	error.textContent = message;
	field.parentNode.insertBefore(error, field.nextSibling);
	field.focus();
	field.setAttribute('aria-describedby', `${fieldId}-error`);
	error.id = `${fieldId}-error`;
}				
document.addEventListener('keydown', (e) => {
	const activeElement = document.activeElement;
    	if (
        	(e.key === 'Enter' && activeElement.tagName !== 'TEXTAREA') ||
        	(e.key === 'Backspace' && activeElement.tagName !== 'INPUT' && activeElement.tagName !== 'TEXTAREA')
    	) {
        	e.preventDefault();
        	if (e.key === 'Enter') {
            		const nextButton = document.querySelector(`#divStep${currentStep} button[id^="nextButton"]`);
            		if (nextButton) nextButton.click();
        	} else if (e.key === 'Backspace') {
            		const backButton = document.querySelector(`#divStep${currentStep} button[id^="backButton"]`);
            		if (backButton) backButton.click();
        	}
    	}
});	
function goTo(stepNumber) {
	const currentStepElement = document.getElementById(`divStep${stepNumber}`);
	if (!currentStepElement) {
		log(`Invalid step: ${stepNumber}`);
		return;
	}
	document.querySelectorAll('.step').forEach(step => {
		step.style.display = 'none';
		step.classList.remove('active');
	});
	currentStepElement.style.display = 'block';
	currentStepElement.classList.add('active');
	currentStep = stepNumber;
	const firstInput = currentStepElement.querySelector('input, button');
	if (firstInput) firstInput.focus();
}		
function updateStep2Header(rating) {
	const step2header = document.getElementById('step2header');
	step2header.textContent = rating >= 9 ? headers.high : rating >= 7 ? headers.medium : headers.low;
}			
function updateStep3Prompt(rating) {
	const step3prompt = document.getElementById('step3prompt');
	if (rating === 7 || rating === 8) {
		step3prompt.textContent = "Do you want us to connect with you and let you know about improvements based on your feedback? Clicking 'No' submits your feedback anonymously.";
	} else if (rating === 9 || rating === 10) {
		step3prompt.textContent = "We really appreciate you taking the time to share your confidence in our team. Would you like to share your name so that we can follow up with you?";
	} else {
		step3prompt.textContent = "We're sorry to hear you didn't receive the 10-star experience we strive for. Would you like us to connect with you about improvements? Clicking 'No' submits your feedback anonymously.";
	}
}		
function validateInput(name) {
	if (typeof name !== 'string' || name.trim() === '') {
		console.error("Name is required");
		return false;
	}
	return true;
}	
async function submitSurveyNormal(x, y, z) {
	try {
		const docId = await createNewSubmission(x, y, z);
		log(`Document written with ID: ${docId} for user ${userName}`);
		log("Now get outta' here!");
		window.top.location.href = "https://www.placeholder.com/";
	} catch (error) {
		console.error("Error creating document:", error);
		alert("We're having trouble saving your response. Please try again or contact us at (720) 990-1680. We apologize for the inconvenience.");
	}
}	
async function submitSurveyGoogle(x, y, z) {
	const docId = await createNewSubmission(x, y, z);
	log(`Document written with ID: ${docId} for user ${userName}`);
	log("Now get outta' here!");
	window.top.location.href = "https://g.placeholder.com";
}
function handleNextStep() {
	log("Next button clicked");
	if (currentStep === 1) {
		userRating = parseInt(document.getElementById('htmlRating').value, 10);
		if (isNaN(userRating) || userRating < 1 || userRating > 10) {
			clearErrors("htmlRating");
			showError("Please select a valid rating between 1 and 10.", "htmlRating");
			return;
		}
		log(`userRating is ${userRating}`);
		updateStep2Header(userRating);
	} else if (currentStep === 2) {
		clearErrors("htmlFeedback");
		userFeedback = document.getElementById('htmlFeedback').value.trim() || "NA";
		if (userFeedback.length > 500) {
			showError("Feedback must be under 500 characters.", "htmlFeedback");
			return;
		}
		log(`userFeedback is ${userFeedback}`);
		updateStep3Prompt(userRating);
	} else if (currentStep === 5) {
		clearErrors("htmlName");
		const nameInput = document.getElementById('htmlName').value.trim();
		const namePattern = /^[A-Za-z\s]+$/;
		if (!validateInput(nameInput) || !namePattern.test(nameInput)) {
			clearErrors("htmlName");
			showError("Please enter a valid name. Only alphabets and spaces are allowed.", "htmlName");
			return;
		}
		userName = nameInput;
		log(`userName is ${userName}`);
		const reviewContent = `
			<p><strong>Rating:</strong> ${userRating || "Not Provided"}</p>
			<p><strong>Feedback:</strong> ${userFeedback !== "NA" && userFeedback.trim() ? userFeedback : "Not Provided"}</p>
			<p><strong>Name:</strong> ${userName || "Anonymous"}</p>
		`;
		document.getElementById('reviewContent').innerHTML = reviewContent;
		if (userRating <= 8) {
			const reviewContent = `
				<p><strong>Rating:</strong> ${userRating || "Not Provided"}</p>
				<p><strong>Feedback:</strong> ${userFeedback !== "NA" && userFeedback.trim() ? userFeedback : "Not PRovided"}</p>
				<p><strong>Name:</strong> ${userName || "Anonymous"}</p>
			`;
			document.getElementById('reviewContent').innerHTML = reviewContent;
			goTo(6);
			return;
		} else {
			goTo(4);
			return;
		}
	}
	const nextStep = currentStep === 4 && userRating >= 9 ? 4 : currentStep + 1;
	goTo(nextStep);
}		
function handlePreviousStep() {
	log("Back button clicked");
	if (currentStep === 4) {
		if (step3offered === false) {
			goTo(3);
		} else {
			goTo(5);
		}
	} else if (currentStep === 5) {
		step3offered = false;
		goTo(3);
	} else if (currentStep === 6) {
		if (userRating <= 8) {
			if (step3offered === false) {
				goTo(3);
			} else {
				goTo(5);
			}
		} else {
			step4offered = false;
			goTo(4);
		}
	} else {
		goTo(currentStep - 1);
	}
}	
function handleYesClick() {
	console.log("Yes button clicked");
	if (currentStep === 3) {
		step3offered = true;
		goTo(5);
	} else if (currentStep === 4) {
		log("User agreed to leave a Google review.");
		step4offered = true;
		const reviewContent = `
			<p><strong>Rating:</strong> ${userRating || "Not Provided"}</p>
			<p><strong>Feedback:</strong> ${userFeedback !== "NA" && userFeedback.trim() ? userFeedback : "Not Provided"}</p>
			<p><strong>Name:</strong> ${userName || "Anonymous"}</p>
		`;
		document.getElementById('reviewContent').innerHTML = reviewContent;
		goTo(6);
	}
}	
function handleNoClick() {
	console.log("No button clicked");
	if (currentStep === 3) {
		if (userRating >= 9) {
			goTo(4);
		} else {
			const reviewContent = `
				<p><strong>Rating:</strong> ${userRating || "Not Provided"}</p>
				<p><strong>Feedback:</strong> ${userFeedback !== "NA" && userFeedback.trim() ? userFeedback : "Not Provided"}</p>
				<p><strong>Name:</strong> ${userName || "Anonymous"}</p>
			`;
			document.getElementById('reviewContent').innerHTML = reviewContent;
			goTo(6);
		}
	} else if (currentStep === 4) {
		log("User did not agree to leave a Google review.");
		const reviewContent = `
			<p><strong>Rating:</strong> ${userRating || "Not Provided"}</p>
			<p><strong>Feedback:</strong> ${userFeedback !== "NA" && userFeedback.trim() ? userFeedback : "Not Provided"}</p>
			<p><strong>Name:</strong> ${userName || "Anonymous"}</p>
		`;
		document.getElementById('reviewContent').innerHTML = reviewContent;
		goTo(6);
	}
}		
function updateSliderValue(value) {
	document.getElementById('sliderValue').textContent = value;
}	
document.getElementById('htmlRating').addEventListener('input', e => {
	updateSliderValue(e.target.value);
});		
document.getElementById('htmlRating').value = 5;
document.getElementById('submitButton6').addEventListener('click', () => {
	if (userRating >= 9) {
		if (step4offered === true) {
			submitSurveyGoogle(userRating, userFeedback, userName);
		} else {
			submitSurveyNormal(userRating, userFeedback, userName);
		}
	} else {
		submitSurveyNormal(userRating, userFeedback, userName);
	}
});
document.addEventListener('DOMContentLoaded', () => {
	const CryptoJS = window.CryptoJS;
	updateSliderValue(document.getElementById('htmlRating').value);
	goTo(1);
	Object.entries(stepButtons).forEach(([step, buttons]) => {
		if (buttons.next) document.getElementById(buttons.next).addEventListener('click', handleNextStep);
		if (buttons.back) document.getElementById(buttons.back).addEventListener('click', handlePreviousStep);
		if (buttons.nextYes) document.getElementById(buttons.nextYes).addEventListener('click', handleYesClick);
		if (buttons.nextNo) document.getElementById(buttons.nextNo).addEventListener('click', handleNoClick);
	});
});