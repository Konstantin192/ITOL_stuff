let scores = [1, 5, 20, 50, 75];
let mean = Math.round(calculate_mean(scores));

function calculate_mean(array_of_numbers) {
    let sum = 0;
    let result;

    array_of_numbers.forEach(element => {
        sum += element;
    });

    result = sum / array_of_numbers.length

    return result;
}

console.log(`The mean of the scores is ${mean}`);