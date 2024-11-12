import tkinter as tk

def addy():
	num1=int(entry_num1.get())
	num2=int(entry_num2.get()) 
	result= num1+num2 
	return result_label.config(text="Our result is %d "%(result))
	
	
	
   
       

root=tk.Tk()
root.title("Add numbers")    
label_num1=tk.Label(root ,text="Enter first number") 
label_num1.pack(pady=10) 
entry_num1=tk.Entry(root)
entry_num1.pack(pady=10)
label_num2=tk.Label(root ,text="Enter second number")
label_num2.pack(pady=10) 
entry_num2=tk.Entry(root)
entry_num2.pack(pady=10)
calculate_button=tk.Button(root, text="Addition", command=addy)
calculate_button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)
root.geometry("600x300")
root.mainloop()
