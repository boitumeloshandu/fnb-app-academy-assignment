let rootPath = "https://mysite.itvarsity.org/api/ContactBook/";
let apiKey = checkApiKey();

function checkApiKey() {
    const key = localStorage.getItem("apiKey");
    if (!key) {
        // If no key, send the user to the enter key page
        window.location.replace("enter-api-key.html");
    }
    return key;
}