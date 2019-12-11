package svinerus;

import java.util.ArrayList;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

class Tests {

    @org.junit.jupiter.api.Test
    void test() {
        Bank bank = new Bank();
        Random random = new Random();

        for (int i=0; i<10000; i++) {
            bank.addAccount(random.nextInt(1000));
        }


        int START_SUM = bank.getSum();

        int thread_count = 1000;

        ArrayList<Thread> threads = new ArrayList<>();
        for (int i=0; i<thread_count; i++) {
            Thread t = new Thread(() -> {
                Account acc1 = bank.accounts.get(random.nextInt(bank.accounts.size()));
                Account acc2 = bank.accounts.get(random.nextInt(bank.accounts.size()));
                bank.transfer(acc1, acc2, random.nextInt(100));
            });

            t.start();
            threads.add(t);
        }
        for (Thread t: threads) {
            try {
                t.join();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        int END_SUM = bank.getSum();

        assertEquals(START_SUM, END_SUM);

    }
}