public class Main {
    public static void main(String[] args) {
        int[] arreglo = {0,1,2,3,4,5,6,7,8,9};
        for(int x=0; x<10;x++){
            System.out.println(arreglo[x]);
        }
        System.out.println("*********");
        //Foreach
        for(int x : arreglo){
            System.out.println(x);
        }
    }
}