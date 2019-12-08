package atm;
import java.util.Scanner;
public class CH10 {
  private Scanner s;
CH10(){
System.out.print("Enter an ID : ");
}
   Scanner X = new Scanner (System.in);
    public static int id[] = { 0,1,2,3,4,5,6,7,8,9} ;
    public static double balance = 100 ;
   static boolean isfound = true;
   public  double withdrow = 0 ;
   public  void menu ()
           {
     System.out.println("Main menu");
     System.out.println("1 : check the balace");
     System.out.println("2 : withdrow");
     System.out.println("3 : deposit");
     System.out.println("4 : Exit");
     System.out.print("Enter ur choisse : ");
     int K = X.nextInt();
        ATMloop(K);
          
   }
   public void withdrow(){
     System.out.print(" Enter the amount you wanna deposit :");
          double Withdrow = X.nextDouble();
          balance -=Withdrow; 
   System.out.println("UR balance is : " + balance );}
   public void checkBalance(){
       System.out.println("The balance is " + balance );
   }
   public void deposit (){
   System.out.print(" Enter the amount you wanna deposit :");
          double Deposit = X.nextDouble();
          balance -=Deposit ;
          System.out.println("UR balance now" + balance);

   }
   
  // to check if the ID is in
   public  boolean foundID (int ID){
       for ( int i =0 ; i < 9 ; i++){
           if(id[i] == ID)
           {     System.out.println("Valid ID");

        menu();
       return true ;}
       }

       return false ;
   }
   
     public void Exit (){
      System.out.println("UR balance is " + balance );
        balance = 100;
        System.out.print("Enter an ID : ");

        int ID = X.nextInt();
    boolean valid = foundID(ID);
    if (valid == true) menu();
    else{
        while( valid != true )
        {            
       System.out.print("Enter a valid ID :");
       ID = X.nextInt();
       valid = foundID(ID);
        }      } 
        
     }
 

   
   
    public  void ATMloop(int k ){
    if (k == 1 )
    {       if(k ==1 ) checkBalance();
              menu(); }
    
    if (k ==2){
        withdrow();
               menu();

    }
   if (k == 4){
   Exit();
    } }
    
    
    
}
    
   
















   
   
    
    
    
    

