function sendRequest(book_id) {
    let formData = new FormData();
    let token = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formData.append("book_id", book_id);
    return fetch('/read/', {
        method: "POST",
        headers: {'X-CSRFToken': token},
        body: formData,
    })
    .then(response => response.text())
    .then(htmlBody => htmlBody);
};

function replaceContent(target, content) {
    let new_btn = document.createRange().createContextualFragment(content).children[0];
    target.textContent = new_btn.textContent;
    target.className = new_btn.className;
    if (new_btn.disabled) {
        target.disabled = true;
        alert('Упс, эту книгу уже успели взять')
    };
};


function handler(event) {
    let target = event.target;
    if (target.id) {
        if (target.id === "clipboard"){
            navigator.clipboard.writeText(target.textContent);
            return;
        } else if (parseInt(target.id)) {
            let res = sendRequest(target.id);
            res.then((htmlBody) => replaceContent(target, htmlBody))
        }
    }  
};


document.addEventListener('click', handler);
