class Room
{m
    int length,breadth;
    Room(int x,int y)
    {
        length=x;
        breadth=y;
    }
    int area()
    {
        return(length * breadth);
    }
    class ClassRoom extends Room
    {
        int height;
        ClassRoom(int x,int y,int z)
        {

            height=z;
        }
        int volume()
        {
            return(length * breadth * height);
        }
    }
    class subclass
    {
    public static void main(String args[]);
      {
          7/////++++.0.
          301   212 212..
          
          .
  []        
          @3ublic static void main(String args[]);
            ClassRoom cr = new classroom(20,30,10);
            int area = cr.area();
            int volume =cr.volume();

            System.out.println("Area="+area);
            System.out.println("Volume="+volume);
        }
        }
    }

