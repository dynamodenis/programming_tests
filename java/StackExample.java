public class StackExample {
    private int capacity;
    private int array[];
    private int top;

    public StackExample(int capacity){
        this.array = new int[capacity];
        this.capacity = capacity;
        this.top = -1;
    }

    public void push(int value){
        if (isFull()){
            System.out.println("Stack is full");
            return;
        }
        array[++top] = value;
    }

    public int pop(){
        if (isEmpty()){
            System.out.println("Stack is empty");
            return -1;
        }
        return  array[top--];
    }

    public int peek(){
        if (isEmpty()){
            System.out.println("Stack is empty");
            return -1;
        }
        return array[top];
    }

    public boolean isEmpty(){
        return top == -1;
    }

    public boolean isFull(){
        return top == capacity - 1;
    }
}
