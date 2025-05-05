class BankAccount {
    constructor(accountNumber, accountHolder, balance) {
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    deposit(amount) {
        this.balance += amount;
        this.checkBalance();
    }

    withdraw(amount) {
        this.balance -= amount;
        this.checkBalance();
    }

    checkBalance() {
        console.log(`Current balance ${this.balance}`);
    }
}

export default BankAccount;