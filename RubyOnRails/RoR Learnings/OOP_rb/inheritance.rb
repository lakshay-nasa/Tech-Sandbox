class Animal
    def speak
      puts "Animal speaks."
    end
  end
  
  class Dog < Animal
    def speak
      puts "Dog barks."
    end
  end
  
  class Cat < Animal
    def speak
      puts "Cat meows."
    end
  end
  
  dog = Dog.new
  cat = Cat.new
  
  dog.speak  # Output: Dog barks.
  cat.speak  # Output: Cat meows.
  