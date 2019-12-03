package svinerus;

import java.io.IOException;

public class Main {

    public static void main(String[] args) {

        try {
            System.out.println("html tags in google.com: ");
            Part4 tags = new Part4("https://google.com");
            System.out.println("sort by count: " + tags.sortByCount());
            System.out.println("sort by tag: " + tags.sortByTag());

        } catch (IOException e) {
            e.printStackTrace();
        }


    }
}
