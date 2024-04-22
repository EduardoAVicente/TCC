import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.URL;
import java.net.URLConnection;


public class HTMLPrinter {
    private static String urlStr = "https://portal.fei.edu.br/  ";

    public static void main(String[] args) {
        // System.out.println(getHTML());
        System.out.println(getExtractText());
    }

    public static String getHTML() {
        try {
            URL url = new URL(urlStr);
            URLConnection connection = url.openConnection();
            connection.connect();

            // Lê o conteúdo da página
            InputStream inputStream = connection.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            StringBuilder htmlBuilder = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                htmlBuilder.append(line).append("\n");
            }

            // Imprime o HTML da página
            return htmlBuilder.toString();
        } catch (IOException e) {
            System.err.println("Erro ao conectar à URL: " + e.getMessage());
            return null;
        }
    }

    private static String getExtractText() {
        String html = getHTML();
        // remove scripts
        html = html.replaceAll("(?is)<script[^>]*>.*?</script>", "");

        // remove CSS
        html = html.replaceAll("(?is)<style[^>]*>.*?</style>", "");

        // Remove tags HTML e normaliza espaços em branco
        html = html.replaceAll("<[^>]*>", "")
                .replaceAll("\\s+", " ")
                .replaceAll("> <", "><");
                
        return html;
    }
}
