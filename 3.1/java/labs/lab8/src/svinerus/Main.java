package svinerus;

public class Main {

    public static void main(String[] args) {

        int threads = 8;
        int iterations = 10000000;

        long time = -System.currentTimeMillis();
        double pi = ParallelMonteCarloPi.run(threads, iterations);
        time += System.currentTimeMillis();

        System.out.println("pi is " + pi);
        System.out.println("threads " + threads);
        System.out.println("iterations " + iterations);
        System.out.println("time " + time + "ms");

    }
}
