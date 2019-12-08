package stack;

/**
 *
 * @author Rowida Nagah
 */
public class StackofInt {
    private int[] elements ;
    private int size ;
    private static  int capacity = 16; // static >- as we r gonna change it and 16 considered as a defual 
    StackofInt(){
    this(capacity);
    }
    StackofInt(int capacity ){
    //this.capacity= capacity;
    elements = new int [capacity];
    }
  // create stack basic options
    public  void push(int val ){
    if(size >= elements.length){
    int [] temp = new int[elements.length *2]; // expand and duplicate the stack size
      System.arraycopy(elements, 0, temp, 0, elements.length);     
              elements = temp;
    }
     elements[size++] = val; 
    }
    // Drope the last element element from the stack */ 
    public int pop(){
        // pro sub
    return elements[--size]; }
    /** Return the top element from the stack */
    public int peak(){
    return elements[size-1];}
    // to check whether the stack i empty or not
    public boolean empty(){
        // rather than check the lenght of stack check the value of size
        return size ==0 ;
    }
    // return the final size
    public int getsize(){
    return elements.length ;}
}
