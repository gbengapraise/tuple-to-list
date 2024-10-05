
def tuple_to_list(input_tuple):
   
    return list(input_tuple)



def main():
   
    input_tuple = eval(input("Enter a tuple (e.g., (1, 2, 3)): "))

 
    if isinstance(input_tuple, tuple):
     
        output_list = tuple_to_list(input_tuple)

       
        print(f"Tuple: {input_tuple}")
        print(f"Converted List: {output_list}")
    else:
        print("Invalid input. Please enter a tuple.")


if __name__ == "__main__":
    main()