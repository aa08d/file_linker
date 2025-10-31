const expiryInput = document.getElementById('expiryDate');
const today = new Date();
const plus30days = new Date(
	today.getFullYear(),
	today.getMonth(),
	today.getDate() + 30
);
expiryInput.valueAsDate = plus30days;
