document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("uploadForm");
  const fileInput = document.getElementById("fileInput");
  const workerCount = document.getElementById("workerCount");
  const submitBtn = document.getElementById("submitBtn");
  const resultsDiv = document.getElementById("results");
  const resultsTable = document.getElementById("resultsTable");
  const statsDiv = document.getElementById("stats");
  const errorDiv = document.getElementById("error");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const file = fileInput.files[0];
    if (!file) {
      showError("Please select a file");
      return;
    }

    // Show loading state
    submitBtn.disabled = true;
    submitBtn.innerHTML =
      '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Processing...';

    try {
      const formData = new FormData();
      formData.append("file", file);
      formData.append("workers", workerCount.value);

      const response = await fetch("/api/wordcount", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "An error occurred");
      }

      displayResults(data);
    } catch (error) {
      showError(error.message);
    } finally {
      // Reset button state
      submitBtn.disabled = false;
      submitBtn.textContent = "Process File";
    }
  });

  function displayResults(data) {
    // Hide error if visible
    errorDiv.style.display = "none";

    // Clear previous results
    resultsTable.innerHTML = "";

    // Display stats
    statsDiv.innerHTML = `
            <div class="alert alert-info">
                <strong>Total unique words:</strong> ${data.total_words}
            </div>
        `;

    // Display results in table
    data.results.forEach((item) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${item.word}</td>
                <td>${item.count}</td>
            `;
      resultsTable.appendChild(row);
    });

    // Show results
    resultsDiv.style.display = "block";
  }

  function showError(message) {
    errorDiv.textContent = message;
    errorDiv.style.display = "block";
    resultsDiv.style.display = "none";
  }
});
