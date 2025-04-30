let person = {
    name: "John",
    age: 30,
    greet: function () {
        return ("Hello, my name is " + this.name + " and I'm " + this.age + " years old.");
    },
};

console.log(person.greet());


let rectangle = {
    width: 10,
    height: 5,
    resize: function (neWidth, newHeight) {
        this.width = neWidth;
        this.height = newHeight;
    },
};

console.log("Before resizing:", rectangle.width, rectangle.height);
rectangle.resize(20, 10);
console.log("After resizing:", rectangle.width, rectangle.height);


let obj = {
    property: false,
    method: function (value) {
        this.property = value;
        return "Property value updated.";
    },
};

console.log(obj.method(true));
console.log(obj.property);