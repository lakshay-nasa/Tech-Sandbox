class MyClass
    define_method :my_method do
      puts "dynamically defined method"
    end
  end
  
  obj = MyClass.new
  obj.my_method
  