#ruby weight and balance checker

totalmoment = 0
totalweight = 0 #for some reason it gives an error when i dont do this


puts "Input the weight (lbs) and arm (inches) for each item in the aircraft, enter a blank line to finish"

imput = gets.chomp #get the first W&B input, assume it won't be a blank line
imput = imput.split(" ") #split the input to make it a list
ended = false #just incase
while ended == false ; #while it isn't a blank do this: 

    imput[0] = Integer(imput[0]) #There are probably more efficient ways to change the things in a list into an integer
    imput[1] = Integer(imput[1]) 
    
    moment = imput[0] * imput[1] #Calculate the moment for this item
   
    totalmoment = totalmoment + moment #Add to the total moment
    totalweight = totalweight + imput[0] #Add to the total weight

    puts "The moment for this mass is "+ String(moment) + "lb ins" #Probably could have used Ruby's equivalent of Python's F strings but im on a plane and cant google
    puts "The total moment so far is "+ String(totalmoment) + "lb ins"
    puts "The total weight so far is "+ String(totalweight) + "lb"
    
    puts "Please input next item" #Or else the user won't know what to do
    
    imput = gets.chomp #For some reason it breaks if i dont put the .chomp and i dont know why
    
    if imput == ""; #and for some reason if I put this at the top (after line 10) it breaks so that why i assume the first input wont be blank
        ended = true
        break
    end
    
    imput = imput.split(" ") #placing this after the check for blank because it breaks if i dont

end

puts "The total weight is "+ String(totalweight)+ "lbs" #Why cant Ruby allow str(variable) or int(variable) like a normal language
puts "The total moment is "+ String(totalmoment) + "lb ins"
CG = totalmoment/totalweight
puts "Your CG is "+ String(CG)
puts "Remember to check the CG against the operating limitations given in the POH"

#Thank you for looking at my first ruby program

#TODO: Validate inputted data, allow the use of non integers,    don't assume the first input is a blank, make the code look nice with fstrings and such, and find out why all the 'for some reasons' are the way they are

