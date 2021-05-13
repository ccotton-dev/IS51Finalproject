##code to determine which vice president served alongside a president 

def main():
    pres = []
    with open("/Users/CCott_000/Desktop/Spring2021/Project/presidents.txt", "r") as f:
        pres = [line.strip() for line in f]
    """for i in a_file:
        pres.append(str(i))
    """
    vp = []
    with open("/Users/CCott_000/Desktop/Spring2021/Project/vps.txt", "r") as f:
        vp = [line.strip() for line in f]
    #for i in pres:  
    #    print(i)
    """for i in b_file:
        vp.append(str(i))
    """
    #for i in vp:
    #    print(i)
    president = input("Name a current or former president (first and last name with capitalization): ")
    for i in range(len(pres)):
        if(president == pres[i]):
            print (vp[i]) 
    #print(vp[30])
if __name__ == "__main__":
    main()
