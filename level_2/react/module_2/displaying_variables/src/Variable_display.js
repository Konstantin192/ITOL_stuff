function VariableDisplay() {
  let stringVar = "Welcome to React";
  let numberVar = 42;
  let booleanVar = true;
  let arrayVar = ["React", "JSX", "Variables"];
  let objectVar = { name: "John", age: 30, role: "Developer" };

  if (Math.random() > 0.5) {
    stringVar = "Welcome to advanced React";
  }

  return (
    <div>
      <h1>{stringVar}</h1>
      <h1>{numberVar}</h1>
      <h1>{booleanVar}</h1>
      <h1>{arrayVar}</h1>
      <h1>{objectVar.name}</h1>
    </div>
  );
}

export default VariableDisplay;