package svinerus;

import java.util.HashMap;

import static org.junit.jupiter.api.Assertions.*;

class Tests {

    @org.junit.jupiter.api.Test
    void translate() {

        HashMap<String, String> dict = new HashMap<>();
        dict.put("dog", "собака");

        Translator translator = new Translator(dict);

        assertEquals("собака", translator.translate_word("dog"));
        assertEquals("собака", translator.translate("dog"));

        translator.add("hello", "привет");
        translator.add("i", "я");
        translator.add("love", "люблю");
        translator.add("eat", "есть");

        assertEquals(translator.translate("hello i love eat"), "привет я люблю есть");

    }
}