class Animal
    def initialize(name)
      @name = name
    end
  
    def speak
      puts "#{@name} says something."
    end
  end
  
  dog = Animal.new("Dog")
  cat = Animal.new("Cat")
  
  dog.speak
  cat.speak
  