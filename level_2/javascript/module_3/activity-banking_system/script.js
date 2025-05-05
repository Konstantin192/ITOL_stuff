import BankAccount from "./bankAccount.js";

const bankAccount_1 = new BankAccount(123, "John", 100);
const bankAccount_2 = new BankAccount(321, "Doe", 400);

bankAccount_1.checkBalance();
bankAccount_1.deposit(300);
bankAccount_1.withdraw(25);
