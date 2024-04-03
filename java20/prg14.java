public class Cuboid
{
    public double length;
    public double breadth;
    public double height;
}

class Application 
{    
    public double get_total_volume(Cuboid geo_objects[]) 
    {

        double vol_sum = 0;
        for (Cuboid geo_obj : geo_objects) 
        {
            vol_sum += geo_obj.length * geo_obj.breadth * geo_obj.height;
        }
        return vol_sum;
    }
}

public class OCP 
{

    public static void main(String[] args) {
        {
            Cuboid cb1 = new Cuboid();
            cb1.length = 5;
            cb1.breadth = 10;
            cb1.height = 15;

            Cuboid cb2 = new Cuboid();
            cb1.length = 2;
            cb1.breadth = 4;
            cb1.height = 6;

            Cuboid cb3 = new Cuboid();
            cb1.length = 6;
            cb1.breadth = 18;
            cb1.height = 1;

            Cuboid c_arr[] = new Cuboid[3];
            c_arr[0] = cb1;
            c_arr[1] = cb2;
            c_arr[2] = cb3;

            Application app = new Application();
            double Volume = app.get_total_volume(c_arr);
            System.out.println("The total Volume is :" + Volume);

        }
    }
}