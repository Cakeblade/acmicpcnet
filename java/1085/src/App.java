import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class App {
    public static void main(String[] args) throws Exception {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int [] data = new int[4];
        StringTokenizer st = new StringTokenizer(sc.readLine()," ");
        for(int i = 0 ; i < 4 ; i++){
            data[i] = Integer.parseInt(st.nextToken());
        }

        int[] calcData = new int[4];
        calcData[0] = data[0];
        calcData[1] = data[1];
        calcData[2] = data[2] - data[0];
        calcData[3] = data[3] - data[1];

        int min = 1001;
        for(int i = 0; i < 4; i++){
            if(min > calcData[i]){
                min = calcData[i];
            }
        }

        System.out.println(min);
    }
}
