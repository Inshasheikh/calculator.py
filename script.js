// Example: Square Root function add karna
function squareRoot() {
    let num = parseFloat(currentNumber);
    if (num < 0) {
        alert("Negative number ka square root nahi nikalta!");
        return;
    }
    currentNumber = Math.sqrt(num).toString();
    updateDisplay();
}

// Example: Memory functions
let memory = 0;
function memoryAdd() {
    memory += parseFloat(currentNumber);
}
function memoryRecall() {
    currentNumber = memory.toString();
    updateDisplay();
}

// Example: Dark mode toggle
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
}

document.getElementById('sqrtBtn').addEventListener('click', () => {
    let num = parseFloat(currentNumber);
    if (num < 0) alert("Negative number!");
    else currentNumber = Math.sqrt(num).toString();
    updateDisplay();
});