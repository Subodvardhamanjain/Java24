class Animal
{
    void eat()
    {
        System.out.println("animal is eating...");
    }
}
class Dog1 extends Animal
{
    void eat()
    {
        System.out.println("dog is eating...");
    }
    public static void main(String[] args) {
        {
            Animal a=new Dog1();
            a.eat();
        }
    }
}