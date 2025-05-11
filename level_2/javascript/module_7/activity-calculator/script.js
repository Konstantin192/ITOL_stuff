let result = 0;
let input_field = document.querySelector("#input");
let result_field = document.querySelector("#result");


function calculate (operation) {
    let number;
    let error_message = document.querySelector("#divide_zero_error");

    if (checkInput()) {
        number = parseFloat(document.querySelector("#input").value);

        switch (operation) {
            case "add":
                result += number;

                input_field.value = "";
                result_field.value = result;

                break;
            case "subtract":
                result -= number;

                input_field.value = "";
                result_field.value = result;

                break;
            case "multiply":
                result *= number;

                input_field.value = "";
                result_field.value = result;

                break;
            case "divide":
                if (checkInput() && number != 0) {
                    error_message.style.display = "none";

                    result /= number;

                    input_field.value = "";
                    result_field.value = result;
                }
                else {
                    error_message.style.display = "inline"
                }
                break;
        }
    }
}

function checkInput() {
    let number = document.querySelector("#input").value;
    let error_message = document.querySelector("#blank_input_error");

    if (number === "") {
        error_message.style.display = "inline";
        return false;
    }
    else {
        error_message.style.display = "none";
        return true;
    }
}