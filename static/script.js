document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("optimizerForm");
    const resetButton = document.getElementById("resetButton");
    const resultContainer = document.getElementById("resultContainer");

    resetButton.addEventListener("click", function () {
        form.reset(); // Reset input fields
        if (resultContainer) {
            resultContainer.innerHTML = ""; // Clear the results dynamically
        }
    });
});
