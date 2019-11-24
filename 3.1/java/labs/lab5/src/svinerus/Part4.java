package svinerus;

import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Scanner;

import static java.util.Map.Entry.comparingByKey;
import static java.util.Map.Entry.comparingByValue;
import static java.util.stream.Collectors.toMap;

public class Part4 {

    private static String[] tags = new String[] {
            "a",            "abbr",           "address",      "area",          "article",        "aside",          "audio",        "b",
            "base",         "bdi",            "bdo",          "big",           "blockquote",     "body",           "br",           "button",
            "canvas",       "caption",        "cite",         "code",          "col",            "colgroup",       "data",         "datalist",
            "dd",           "del",            "details",      "dfn",           "dialog",         "div",            "dl",           "dt",
            "em",           "embed",          "fieldset",     "figcaption",    "figure",         "footer",         "form",         "h1",
            "head",         "header",         "hr",           "html",          "i",              "iframe",         "img",          "input",
            "ins",          "kbd",            "label",        "legend",        "li",             "link",           "main",         "map",
            "mark",         "meta",           "meter",        "nav",           "noscript",       "object",         "ol",           "optgroup",
            "option",       "output",         "p",            "param",         "picture",        "pre",            "progress",     "q",
            "rp",           "rt",             "ruby",         "s",             "samp",           "script",         "section",      "select",
            "small",        "source",         "span",         "strong",        "style",          "sub",            "summary",      "sup",
            "svg",          "table",          "tbody",        "td",            "template",       "textarea",       "tfoot",        "th",
            "thead",        "time",           "title",        "tr",            "track",          "tt",             "u",            "ul",
            "var",          "video",          "wbr",
    };

    HashMap<String, Integer> tags_count;

    public Part4(String url) throws IOException {
        String html = read_webpage(url);
        tags_count = count_tags(html);

    }

    public HashMap<String, Integer> sortByCount() {
        return tags_count
            .entrySet().stream()
            .sorted(comparingByValue())
            .collect(
                    toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e2, LinkedHashMap::new)
            );
    }

    public HashMap<String, Integer> sortByTag() {
        return tags_count
            .entrySet().stream()
            .sorted(comparingByKey())
            .collect(
                    toMap(Map.Entry::getKey, Map.Entry::getValue, (e1, e2) -> e2, LinkedHashMap::new)
            );
    }

    private String read_webpage(String url) throws IOException {
        Scanner scanner =new Scanner(new URL(url).openStream(), "UTF-8");
        String out = scanner.useDelimiter("\\A").next();
        scanner.close();
        return out;
    }

    private HashMap<String, Integer> count_tags(String html) {
        HashMap<String, Integer> tags_count = new HashMap<>();

        for (String tag: tags) {
            int count = html.split("<" + tag, -1).length - 1;
            if (count > 0)
                tags_count.put(tag, count);
        }
        return tags_count;
    }


}
