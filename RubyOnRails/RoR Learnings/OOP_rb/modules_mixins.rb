module Swimmable
    def swim
      puts "I can swim!"
    end
  end
  
  class Fish
    include Swimmable
  end
  
  fish = Fish.new
  
  fish.swim