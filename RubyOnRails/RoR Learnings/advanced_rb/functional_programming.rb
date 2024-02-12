numbers = [1, 2, 3, 4, 5]
squared_numbers = numbers.map { |n| n * n }
puts squared_numbers.inspect

even_numbers = numbers.select(&:even?)
puts even_numbers.inspect

sum = numbers.reduce(0) { |acc, n| acc + n }
puts sum
