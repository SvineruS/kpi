package svinerus.Task2;

import java.util.concurrent.ArrayBlockingQueue;

public class Task2 {

    ArrayBlockingQueue<String> buf1 = new ArrayBlockingQueue<>(5000);
    ArrayBlockingQueue<String> buf2 = new ArrayBlockingQueue<>(5000);

    public void run() {

        for (int i=0; i<5; i++) {
            Thread t = new Thread(() -> {
                while (true) {
                    try {
                        buf1.add("Thread " + Thread.currentThread().getName() + " created this message");
                    } catch (Exception ignored) {}
                }
            });
            t.setDaemon(true);
            t.start();
        }

        for (int i=0; i<5; i++) {
            Thread t = new Thread(() -> {
                while (true) {
                    try {
                        String msg = buf1.poll();
                        buf2.add("Thread " + Thread.currentThread().getName() + " moved message '" + msg + "'");
                    } catch (Exception ignored) {}
                }
            });
            t.setDaemon(true);
            t.start();
        }

        while (buf2.size() < 100) {

        }


        for (int i=0; i<100; i++) {
            String msg = buf2.poll();
            System.out.println(msg);
        }


    }


}
