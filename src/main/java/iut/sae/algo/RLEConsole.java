package iut.sae.algo;

import java.util.Scanner;

public class RLEConsole{

    public static void main(String[] args){
        String in="";
        
        if(args.length>0){
            in=args[0];
        }
        else{            
            in = "azerty" ;
        }

        // try{
            System.out.println("Entrée : "+in);
            System.out.println("Sortie : "+ AlgoCorriger.RLE(in));
        // } catch (AlgoException ae){
        //     System.out.println(ae);
        // }
        
    }
}