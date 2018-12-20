from math import log10
#--------------------
# 25    s       l
# 20    v       h
# 25    s       l
# 45    suv     h
# 20    s       h
# 25    suv     h

#--------------------------------------------------
def Entroby_of_sets (set_measures, total, sum_of_set_measures, sum_of_measure, target_class_measures, measure_indexs):
                                                            #                        False         True
                                                            #                     25, 20, 45    25, 20, 45
                                                            # sum_of_measure =  [[2, 0, 0]   , [1, 2, 1]]

    entroby_of_set = 0;
                                                            #sum_of_set_measures[3, 2, 1]

    for i in range(len(set_measures)):                      # Set of measure( set_measures ) :  ['25', '20', '45']
        prop_of_set = []                                    # Probability of every element in the set


        for j in range(len(target_class_measures)):
            prop_of_set.append(sum_of_measure[j][i] / sum_of_set_measures[i] )         # Determiner The Probability of Each Element in The Set

        printing = set_measures[i] + " " + str(sum_of_set_measures[i]) + " --> "       #
                                                                                       #
        for j in range (len(target_class_measures)):                                   #
            printing += target_class_measures[j] + ":" + str(sum_of_measure[j][i])     # Generate Printing Statement
            if j != len(target_class_measures)-1 :                                     #
                printing += " || "                                                     #
        print(printing)                                                                #

        entroby = 0.0                                                       # <== E(D_yes, D_no)    Entroby of All Elements of the Set
        for j in range(len(target_class_measures)):                         #
            if prop_of_set[j] != 0:                                         # Generate The Entroby

            # E(D_yes, D_no) = Σ((N_yes / total) || (N_no / total))     *          E(D_yes || D_no)
                entroby += (float(sum_of_set_measures[i])/(total )) * (-prop_of_set[j] * log10(prop_of_set[j]))

        entroby_of_set += entroby                                           # Entroby of The Set

    print("Entroby( set ) = ", entroby_of_set)                              # Printing The Entroby
    return entroby_of_set,set_measures, measure_indexs

# ------------------------------------------------
#display Measures and numbers of each Measure
#       s    3 -->  l: 2 || h: 1
#       v    1 -->  l: 0 || h: 1
#       suv  2 -->  l: 0 || h: 2

def Count_and_Display_Distinct_elements(array):

    field_class=[]                      # The Output is Distinct[array]  Like ==>           array = [l, h, l, h, h, h]  ==> field_class =     [ l, h ]
    num_field_class=[]                  # The Output is Number of Distinct[array]  Like ==> array = [l, h, l, h, h, h]  ==> num_field_class = [ 2,4 ]
    temp = array.copy()                 # Take a Copy From The Set

    for i in range(len(temp)):                                  #
        if temp[i] != ".":                                      # This for Loop is making a loop around all the set to remove the redundent elements in the set and save them in `field_class` array
            field_class.append(temp[i])                         # Like ==> array = [l, h, l, h, h, h]  ==> field_class =     [ l, h ]
            num_field_class.append(1)                           # and Save The Count of Each element in the set and save them in `num_field_class` array
        for j in range(len(temp)):                              # Like ==> array = [l, h, l, h, h, h]  ==> num_field_class = [ 2,4 ]
            if temp[i]== temp[j] and temp[j]!="." and j!=i :    #
                temp[j]="."                                     #
                num_field_class[len(num_field_class)-1] += 1    #

    for i in range(len(field_class)):                           # Display The Distinct Elements in The Set      [ l, h ]  and
        print(field_class[i]," : ",num_field_class[i])          # Display The Count of Each element in This Set [ 2, 4 ]

    return num_field_class, field_class

# This Function To Generate The Entroby
def measures_of_sets(set, target_set, target_class_measures):

    print("Target Set = ", set)   # Print The Set Which I work on Now
    total = 0                     # total of sum_of_measure
    set_measures = []
    sum_of_set_measures = []

    measures_count = len(target_class_measures)  # The Length of The Target Class Measures " it's Common To be Equal to Two ==> [Yes , No] "

    sum_of_measure = []     # True or False or Any Thing  ==> I'm not sure that the target class just True and False
    for i in range(measures_count):  # Here For Each Element in The Set will Generate an Empty Set and Push
        sum_of_measure.append([])    # it in `sum_of_measure` Array Like ==> sum_of_measure = [[], [], []]

    measure_indexes = []            # Each Set Has many Number of Elements, and Each Element Repeated along The Rows
                                    # This Array Will Contain Number of arrayes Equlas to The Number Of Elements In the Set
                                    # Each Array of Each Element Has The Indexes of Rows tha the Element Exist on

    temp =set.copy()                                        #
    for index in range(len(temp)):                          #
                                                            #
        current_measure_indexes = []                        #
        if temp[index] != ".":                              #
            set_measures.append(temp[index])                # This Loop Do What The Loop at `Count_and_Display_Distinct_elements` Function do
            current_measure_indexes.append( index )         # Generate Array Of Distince Elements in The Set And Another Array With The Indexes That that Element Exist on
        for subIndex in range(len(temp)):                   #
                                                            #
            if (temp[index] == temp[subIndex]) and (temp[subIndex] != ".") and (subIndex != index):
                temp[subIndex] = "."                        #
                current_measure_indexes.append(subIndex)    #
        if current_measure_indexes != []:                   #
            measure_indexes.append(current_measure_indexes) #

    for i in range( len(set_measures) ):

        for j in range(measures_count):    #                   True        False
            sum_of_measure[j].append(0)    # sum_of_measure = [[0], [0]]
                                           # sum_of_measure = [[2, 0], [1, 0]]
                                           # sum_of_measure = [[2, 0, 0], [1, 2, 0]]

        sum_of_set_measures.append(0)      # sum_of_set_measures = [0]          #
        for j in range(len(set)):                                               #
                                                                                #
            if set_measures[i] == set[j] :                                      #
                for m in range(measures_count):                                 # Number of Measures Exist in Target Class Label
                                                                                #
                    if target_set[j] == target_class_measures[m]:               # Sum Of Each Element Occur
                        sum_of_measure[m][ len( sum_of_measure[m] )-1 ] += 1    #
                        #----------------      ------------------

        for j in range(measures_count):
            sum_of_set_measures[len(sum_of_set_measures) - 1] += sum_of_measure[j][ len( sum_of_measure[j] )-1 ]

        total += sum_of_set_measures[len(sum_of_set_measures)-1]

    return Entroby_of_sets(set_measures, total, sum_of_set_measures, sum_of_measure, target_class_measures, measure_indexes)
# ------------------------------------------------
def Draw_Tree(num_of_measures, measures):
    print("")


    print("           set")
    print("=========================")
    side_mark = "||                  "
    for i in range(3):
        for counter in range(num_of_measures-1):
            print(side_mark,end='')
        print(side_mark)
    for i in range(len(measures)-1):
        print(measures[i],"        ",end="")

    print(measures[len(measures)-1])


def Branches(tree_tables_array, treeArray, bure_measures):
    for p in range(len(tree_tables_array)):                                 # Loop to Every Element in The Root or The Set

        if len(tree_tables_array[p][len(tree_tables_array[p])-1]) <= 1:     # Stop If The Length of The Array of The Class Label of This Branch <= 1
            treeArray.append(['.'])
            continue

        class_label = tree_tables_array[p][len(tree_tables_array[p])-1][0]      # Take a sample of the class lable of this set to
                                                                                # ensure that all class lables of this branch are the same or not
        print("class_label ", class_label)
        print("All Class Labels Of This Pranch = ", tree_tables_array[p][len(tree_tables_array[p])-1])
        flag = 0
        for check_finish in tree_tables_array[p][len(tree_tables_array[p])-1]:  #
                                                                                #
            if check_finish != class_label:                                     #
                flag = 1                                                        # If all class lables of this branch are the same, append `.`
                                                                                # as a delemeter to finish this Branch
        if (flag != 1) or (len(tree_tables_array[p][0]) <= 0):                  #
            flag = 0                                                            #
            treeArray.append(['.'])                                             #
            continue                                                            #

        copy_branch_tables_array = []

        for j in range(len(tree_tables_array[p])):                              #
            if tree_tables_array[p][j][0] not in bure_measures :                # Remove The Set of The Root From The Old Dataset and Create New Dataset
                copy_branch_tables_array.append(tree_tables_array[p][j])        # With all Values in The Old Dataset Withour Root Set
        print("copy_branch_tables_array = ", copy_branch_tables_array)                   #
                                                                                #
        if len(copy_branch_tables_array) <= 1:                                  # If The Length of The New Dataset <= 1
            treeArray.append(['.'])                                             # append `.` as a delemeter to finish this Branch
            continue                                                            #

        dataset = []
        for j in range(len(copy_branch_tables_array[0])):       #
            cols = []                                           #
            for c in range(len(copy_branch_tables_array)):      # Prepare The Dataset To Be Logic
                cols.append(copy_branch_tables_array[c][j])     # Modify Columns as Rows and Rows as Columns
            dataset.append(cols)                                #


        print("The New Dataset = ", dataset)
        numRows = len(dataset)      # Number of Rows = length of array
        numbCols = len(dataset[0])  # Number of Columns = length of array[0]

        if numbCols <= 1:           # If The Length of The New Dataset <= 1 means There is Only one Column in The Dataset
            continue                # finish this Branch

# From Now and From This Point, All of The Statements Will be As Like As Generating A Root Like in Main Function
        target_class = []                                   #
        for i in range(numRows):                            # This for Loop to Generate Another Array to keep the Class
            target_class.append(dataset[i][numbCols - 1])   # Label of The Dataset ==> dataset[i][last-column]

        num_target_class_measures, target_class_measures = Count_and_Display_Distinct_elements(target_class)

        total = 0                                      # Variable to Calculate The Total Length of The Target Set to Use
        for i in range(len(num_target_class_measures)):# It To Generate The Probability of Each Element in The Set
            total += num_target_class_measures[i]      #

        prop_class = []
        for i in range(len(num_target_class_measures)):              # Determine The Probability of each Element
            prop_class.append(num_target_class_measures[i] / total)  # and store in `prop_class` Array

        entroby = 0                                               #
        for i in range(len(prop_class)):                          # Generat The Entroby
            entroby += (-(prop_class[i]) * log10(prop_class[i]))  #

        print("Entroby(D) = ", entroby)

        numberOfSets = numbCols - 1  # Determine The Count Of Sets in The Dataset Without Counting The Target Class
        set = []

        for N_sets in range(numberOfSets):      # N_sets ==> Number Of Sets
            temp = []                           # generate each column as itself
            for N_rows in range(numRows):       # N_rows ==> Number Of Rows
                temp.append(                    #
                    dataset[N_rows][N_sets])    # temp = 1'st [ 25, 20, 25, 45, 20, 25 ]  |  2'nd [ s, v, s, suv, s, suv ]
            set.append(temp)                    # set = [[ 25, 20, 25, 45, 20, 25 ], [ s, v, s, suv, s, suv ]]

        smallest_val = 0

        flag = 0

        for i in range(numberOfSets):   # Foreach Set In The Dataset Except The Target Set, I Will Get The Entroby and The
                                        #  Set Which Has The Smallest Entroby Will Be The Root Of The Algorithm

            entroby_of_set, set_measures, measure_indexs = measures_of_sets(set[i], target_class, target_class_measures)

            if flag == 0:                                   #
                smallest_val = entroby_of_set               #
                final_measures = set_measures               #
                final_measures_indexs = measure_indexs      #
                flag = 1                                    #
            else:                                           #
                if smallest_val > entroby_of_set:           # Get The Smallest Entroby
                    smallest_val = entroby_of_set           #
                    final_measures = set_measures           #
                    final_measures_indexs = measure_indexs  #

        print("Gain( set ) = ", format(entroby, "3f"), " - ", format(smallest_val, "3f"), " = ", entroby - smallest_val)

        set.append(target_class)

        tree_tables_array1 = []

        for i in range(len(final_measures_indexs)):                 #
            table = []                                              #
            for m in range(len(set)):                               # Extract The Root Set From The Dataset In An Array
                col = []                                            #
                for n in range(len(final_measures_indexs[i])):      #
                    col.append(set[m][final_measures_indexs[i][n]]) # take the values that equivilant to these indexes in dataset ==> then save Then in a column
                table.append(col)                                   #
                                                                    #
            tree_tables_array1.append(table)                        #

        print("Branch ", tree_tables_array1)

        treeArray.append(final_measures)                            # Add This Branch To Be Within The Final Tree

        print("The Updated Tree = ",treeArray)
        treeArray = Branches(tree_tables_array1, treeArray, final_measures)  # Make a Recursion To Get The Remainder Brancher in This Branch Till Stopping

    return treeArray

def main():

    with open('input.txt', 'r') as f:           # read file as f
        dataset = [r.split() for r in f]        # copy file dataset into `dataset` 2D Array

    num_rows = len(dataset)                      # Number of Rows = length of dataset
    numb_cols = len(dataset[0])                  # Number of Columns = length of dataset[0]

    target_class = []                                    #
    for i in range(num_rows):                            # This for Loop to Generate Another Array to keep the Class
        target_class.append(dataset[i][numb_cols - 1])   # Label of The Dataset ==> dataset[i][last-column]

    # This Function will return Two Arrays one of them carry The Distinct Elements
    # and The Other One Carry The Count of each of these Elements
    num_target_class_measures, target_class_measures = Count_and_Display_Distinct_elements(target_class)

    total = 0                                        # Variable to Calculate The Total Length of The Target Set to Use
    for i in range(len(num_target_class_measures)):  # It To Generate The Probability of Each Element in The Set
        total += num_target_class_measures[i]        #

    prop_class = []                                              # Determine The Probability of each Element
    for i in range(len(num_target_class_measures)):              # and store in `prop_class` Array
        prop_class.append(num_target_class_measures[i] / total)  # prop_class= [3/5, 2/5 ]

    entroby = 0                                                  #
    for i in range(len(prop_class)):                             # Generate The Entroby Of The All Set
        entroby += (-(prop_class[i]) * log10(prop_class[i]))     # According to This Low: entroby = -Σ(P[i] * log(P[i]))

    print("Entroby(D) = ", entroby)    # Print The Entroby Of The Target Class

    numberOfSets = numb_cols - 1       # Determine The Count Of Sets in The Dataset Without Counting The Target Class

    set = []                           # This Array Will Contain All Sets in Dataset Except The Target Class Set

    for N_sets in range(numberOfSets):              # N_sets ==> Number Of Sets
        temp = []                                   # Generate each column as itself
        for N_rows in range(num_rows):              # N_rows ==> Number Of Rows
            temp.append(dataset[N_rows][N_sets])    # temp = 1'st [ 25, 20, 25, 45, 20, 25 ]  |
                                                    # 2'nd [ s, v, s, suv, s, suv ]
        set.append(temp)                            # set = [[ 25, 20, 25, 45, 20, 25 ], [ s, v, s, suv, s, suv ]]

    smallest_val = 0

    tree_array = []     # This Array Will Contain All Elements Of The Final Tree and Its Branches
    flag = 0

    for i in range(numberOfSets):   # Foreach Set In The Dataset Except The Target Set, I Will Get The Entroby and The
                                    #  Set Which Has The Smallest Entroby Will Be The Root Of The Algorithm

        entroby_of_set, set_measures, measure_indexs = measures_of_sets(set[i], target_class, target_class_measures)

        if flag == 0:                                   #
            smallest_val = entroby_of_set               #
            final_measures = set_measures               #
            final_measures_indexs = measure_indexs      #
            flag = 1                                    #
        else:                                           #
            if smallest_val > entroby_of_set:           # Ge The Smallest Entroby To Be The Root
                smallest_val = entroby_of_set           #
                final_measures = set_measures           #
                final_measures_indexs = measure_indexs  #
    # Printing The Gain According To Low ==> Gain(D) = Entroby( Target_Class) - Entroby( D_yes, D_no )
    print("Gain( set ) = ", format(entroby, "3f"), " - ", format(smallest_val, "3f"), " = ", entroby - smallest_val)

    set.append(target_class)

    tree_tables_array = []

    for i in range(len(final_measures_indexs)):                 #
        table = []                                              #
        for m in range(len(set)):                               # Extract The Root Set From The Dataset In An Array
            col=[]                                              #
            for n in range(len(final_measures_indexs[i])):      #
                col.append(set[m][final_measures_indexs[i][n]]) # take the values that equivilant to these indexes in dataset ==> then save Then in a column
            table.append(col)                                   #
                                                                #
        tree_tables_array.append(table)                         #

    tree_array.append(final_measures)                           # Add The Root To Be Within The Final Tree

    print("Root ", tree_array)  # Printing The Root

    print("Tree Table Array ", tree_tables_array )
    tree_array = Branches(tree_tables_array, tree_array, final_measures)    # This Function Will Generate The Branches Of The Tree To Leafs

    print("Final Tree = ",tree_array)

    for i in range(len(tree_array)):                # Drawing The Tree
        Draw_Tree(len(tree_array[i]),tree_array[i]) #

main()