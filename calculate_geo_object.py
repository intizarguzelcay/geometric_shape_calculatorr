# İntizar Güzelçay 
# Question5

import geometry_shapes as shape

print("Selecta geometric shape to calculate: ")
print("1 : Rectangle","2 : Square","3 : Triangle")

select = int(input("Enter your choice: "))

if select == 1:

   long_side_value=float(input ("Please enter long_side the restangle: ")) 
   short_edge_value=float(input(" Please ebter your shorta_edge : "))

   rectangle1 = shape.Rectangle(long_side_value,short_edge_value)

   calculate_area = rectangle1.rectangle_area()
   calculate_perimeter = rectangle1.rectangle_perimeter()

   print("Rectangle area:", calculate_area)
   print("Recentangle perimeter:" , calculate_perimeter)



elif select == 2:
   
   side_value = float(input("Please enter square side value:"))

   square1 = shape.Square(side_value)

   calculate_area_sq = square1.square_area()
   calculate_perimeter_sq = square1.square_perimeter()

   print("Square area : " ,calculate_area_sq)
   print("Square perimeter: " ,calculate_perimeter_sq)



else :

  side1_value = float(input("Please enter  side1 value triangle: "))
  side2_value = float(input("Please enter  side2 value of triangle: "))
  base_lenght_value = float(input("Please enter  side3 value of triangle : "))
  height_value = float(input("Please enter height value of triangle: "))
 
  triangle1 = shape.Triangle(side1_value,side2_value,base_lenght_value,height_value)

  calculate_area_triangle = triangle1.triangle_area()
  calculate_perimeter_triangle = triangle1.triangle_perimeter()

  print("Triangle area :",calculate_area_triangle)
  print("Triangle perimeter: " ,calculate_perimeter_triangle)