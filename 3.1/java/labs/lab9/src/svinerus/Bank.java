package svinerus;

import java.util.ArrayList;

public class Bank {

    ArrayList<Account> accounts = new ArrayList<>();

    public synchronized void transfer(Account from, Account to,  int amount){
        from.withdraw(amount);
        to.deposit(amount);
    }

    public int getSum() {
        return accounts.stream().mapToInt(Account::getBalance).sum();
    }

    public void addAccount(int balance) {
        accounts.add(new Account(balance));
    }
}
