begin
    puts 10 / 0
  rescue ZeroDivisionError => e
    puts "Error: #{e.message}"
  end
  
  def raise_custom_error
    raise ArgumentError.new("This is a custom error.")
  end
  
  begin
    raise_custom_error
  rescue ArgumentError => e
    puts "Custom Error: #{e.message}"
  end  