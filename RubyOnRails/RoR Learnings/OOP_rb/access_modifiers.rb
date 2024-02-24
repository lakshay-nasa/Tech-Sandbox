class Car
    def initialize(speed)
      @speed = speed
    end
  
    def accelerate
      @speed += 10
      puts "Accelerating to #{@speed} km/h."
    end
  
    private
  
    def check_speed
      puts "Checking speed: #{@speed} km/h."
    end
  end
  
  car = Car.new(50)
  
  car.accelerate
#   car.check_speed
  