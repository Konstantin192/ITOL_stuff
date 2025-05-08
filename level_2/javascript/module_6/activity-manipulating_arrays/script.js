let array = [];

function addLast() {
    let input = document.querySelector("#elementAddition").value;
    let errorMessage = document.querySelector("#elementAddition_error");
    
    if(input == "") {
        errorMessage.style.display = "inline";
    }
    else {
        errorMessage.style.display = "none";
        array.push(input);
        document.querySelector("#elementAddition").value = "";
        console.log(document.querySelector("#elementAddition").value);
        displayArray();
    }
}

function removeLast() {
    array.pop();
    displayArray();
}

function removeFirst() {
    array.shift();
    displayArray();
}

function addFirst() {
    let input = document.querySelector("#elementAddition").value;
    let errorMessage = document.querySelector("#elementAddition_error");

    if(input == "") {
        errorMessage.style.display = "inline";
    }
    else {
        errorMessage.style.display = "none";
        array.unshift(input);
        document.querySelector("#elementAddition").value = "";
        displayArray();
    }
}

function removeElement() {
    let input = document.querySelector("#elementRemoval").value;
    let errorMessage = document.querySelector("#elementRemoval_error");

    if(input == "") {
        errorMessage.style.display = "inline";
    }
    else {
        errorMessage.style.display = "none";
        array.splice(input, 1)
        input = "";
        displayArray();
    }
}

function displayArray() {
    let elementList = document.querySelector("#arrayElements");
    let element;
    let elementDisplay;

    elementList.innerHTML = "";

    array.forEach(item => {
        // var task_input = document.querySelector("#task_input").value;
        element = document.createElement("li");
        elementDisplay = document.createTextNode(`Element ${array.indexOf(item)}: ${item}`);
        
        element.appendChild(elementDisplay);
        elementList.appendChild(element);
    });
}