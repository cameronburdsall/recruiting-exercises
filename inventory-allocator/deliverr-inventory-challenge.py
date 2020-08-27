# Created by Cameron Burdsall as a reponse to the Deliverr inventory allocation coding challenge
# Solution written in Python, tested on Python 3.7.9

# Solution assumes that the cheaptest warehouses come first, and thus will allocate where stuff is grabbed based on that principle

def findBestShipment (target, warehouses):
    #target is a dictionary holding the desired items and values
    #warehouses is a list holding dictionaries that represent the available warehouses to select goods from
    #return a list holding the names of the warehouses used and the items taken from each
    answer = []
    for i in range (0, len(warehouses)):

        takeFrom = {}
        for item in warehouses[i]['inventory'].keys():
            #take item from the warehouse if it holds an item we want
            if (item in target.keys()):
                #if there is more than we need, take only what we need
                if ((target[item] - warehouses[i]['inventory'][item]) < 0):
                    takeFrom[item] = target[item]
                #if there is less than or exactly what we need, take it all
                else:
                    takeFrom[item] = warehouses[i]['inventory'][item]
        
        #affect changes on target (if any)
        for k in takeFrom.keys():
            target[k] = target[k] - takeFrom[k]

        #if there are changes made, add the warehouse to answer
        if (len(takeFrom.keys()) != 0):
            temp = {}
            temp['name'] = warehouses[i]['name']
            temp['inventory'] = takeFrom
            answer.append(temp)
        count = 0
        #check if target has been reached
        for v in target.values():
            if (v == 0):
                count += 1
        #break out of loop early if we reach
        if (count == len(target.values())):
            break

    #final check to make sure solution was reached
    count = 0
    #check if target has been reached
    for v in target.values():
        if (v == 0):
            count += 1
    if (count == len(target.values())):
            return answer
    return []


#test solution
def testSolution ():
    #test 0, single item desired from single warehouse
    target = {'apple': 5}
    warehouses = [{'name': 'owd', 'inventory': {'apple': 5}}]
    print ("Test 0\n Desired Answer: [{'name': 'owd', 'inventory': {'apple': 5}}] \n\tSolution's Answer: "+ str(findBestShipment(target, warehouses)))

    #test 1, single item from single warehouse with multiple items
    target = {'apple': 4}
    warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 3}}]
    print ("Test 1\n Desired Answer: [{'name': 'owd', 'inventory': {'apple': 4}}] \n\tSolution's Answer: "+ str(findBestShipment(target, warehouses)))

    #test 2, multiple items from single warehouse with multiple items
    target = {'apple': 5, 'banana':2}
    warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 3}}]
    print ("Test 2\n Desired Answer: [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 2}}] \n\tSolution's Answer: "+ str(findBestShipment(target, warehouses)))

    #test 3, single item across multiple warehouses
    target = {'apple': 6}
    warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 3}}, {'name': 'dwt', 'inventory': {'apple': 3, 'banana': 3}}]
    print ("Test 3\n Desired Answer: [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dwt', 'inventory': {'apple': 1}}] \n\tSolution's Answer: "+ str(findBestShipment(target, warehouses)))

    #test 4, multiple items across multiple warehouses with many items
    target = {'apple': 6, 'banana': 7}
    warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 5}}, {'name': 'dwt', 'inventory': {'apple': 3, 'banana': 3}}]
    print ("Test 4\n Desired Answer: [{'name': 'owd', 'inventory': {'apple': 5, 'banana':5}}, {'name': 'dwt', 'inventory': {'apple': 1, 'banana': 2}}] \n\tSolution's Answer: "+ str(findBestShipment(target, warehouses)))

    #test 5, try with an invalid input
    target = {'apple': 99, 'banana': 99}
    warehouses = [{'name': 'owd', 'inventory': {'apple': 5, 'banana': 5}}, {'name': 'dwt', 'inventory': {'apple': 3, 'banana': 3}}]
    print ("Test 5\n Desired Answer: [] \n\tSolution's Answer: "+ str(findBestShipment(target, warehouses)))

    #test 6, grabbing each item from a different warehouse
    target = {'apple': 6, 'banana': 7, 'potato':3}
    warehouses = [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dwt', 'inventory': {'potato': 2}}, {'name': 'abc', 'inventory': {'banana': 6}}, {'name': 'xyz', 'inventory': {'potato': 1, 'apple':1,'banana': 1}}]
    print ("Test 6\n Desired Answer: [{'name': 'owd', 'inventory': {'apple': 5}}, {'name': 'dwt', 'inventory': {'potato': 2}}, {'name': 'abc', 'inventory': {'banana': 6}}, {'name': 'xyz', 'inventory': {'potato': 1, 'apple': 1, 'banana': 1}}] \n\tSolution's Answer: "+ str(findBestShipment(target, warehouses)))

#run tests
testSolution()