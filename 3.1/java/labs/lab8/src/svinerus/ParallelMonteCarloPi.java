package svinerus;


import java.util.ArrayList;
import java.util.Random;

public class ParallelMonteCarloPi {

    public static double run(int thread_count, int iterations) {
        iterations /= thread_count;

        GetPIRunnable runnable = new GetPIRunnable(iterations);

        ArrayList<Thread> threads = new ArrayList<>();
        for (int i=0; i<thread_count; i++) {
            Thread t = new Thread(runnable);
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

        return (double) GetPIRunnable.count / iterations / thread_count * 4;
    }

}

class GetPIRunnable implements Runnable {
    final static Random random = new Random();

    static int count = 0;
    int iterations;

    public GetPIRunnable(int iterations) {
        this.iterations = iterations;
    }

    @Override
    public void run() {
        int count_ = 0;

        for (int i=0; i<iterations; i++)
            if (is_in_circle(random.nextDouble(), random.nextDouble()))
                count_++;

        synchronized (GetPIRunnable.class) {
            count += count_;
        }

    }

    boolean is_in_circle(double x, double y) {
        return Math.sqrt(x*x+y*y) <= 1;
    }

}
