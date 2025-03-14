async function generateAlContent() {
  // ... (rest of your code)
  try {
    let response = await fetch("http://localhost:5000/generate", { ... });
    let data = await response.json();
    outputDiv.innerHTML = "<p>" + data.generatedText + "</p>";
  } catch (error) {
    outputDiv.innerHTML = "<p>Error generating content. Please try again.</p>";
    console.error(error);
  }
}
