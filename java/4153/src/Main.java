import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        StringTokenizer st;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] inputdata = new int[4];
        List<String> output = new ArrayList<String>();

        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < 3; i++){
            inputdata[i] = Integer.parseInt(st.nextToken());
        }

        while(inputdata[0] != 0 && inputdata[1] != 0 && inputdata[2] != 0) {
            if((Math.pow(inputdata[0], 2) + Math.pow(inputdata[1], 2) == Math.pow(inputdata[2], 2))) {
                output.add("right");
            }
            else {
                output.add("wrong");
            }

            st = new StringTokenizer(br.readLine());
            for(int i = 0; i < 3; i++){
                inputdata[i] = Integer.parseInt(st.nextToken());
            }
        }        

        for(int i = 0; i < output.size(); i++) {
            System.out.println(output.get(i));
        }
    }
}
