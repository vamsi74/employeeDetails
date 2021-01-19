from python_employee.xmltojson import xmltojson, homerun

class SortByName(xmltojson):
    def tryof(sortKey):

        home = homerun()
        condition = True

        #Check for id
        if sortKey == 'id':
            sortKey = '@id'

        for i in range (len(home['employees']['employee'])-1):
            # Check for tags present for all employees
            if home['employees']['employee'][i].get(sortKey)!=None and (home['employees']['employee'][i+1].get(sortKey)==None or home['employees']['employee'][i-1].get(sortKey)==None):
                output=f"{sortKey} is not present for all employees to sort"
                condition=False
                break
            # Check for tags present for none of employee details
            elif home['employees']['employee'][i].get(sortKey)==None:
                output= f"OOPS! {sortKey} is not present in data to sort"
                condition=False
        # Sorting by input key
        if condition:
            home['employees']['employee'] = sorted(home['employees']['employee'], key=lambda x: x[sortKey])
            output= home

        return output

def sortFirst(sortKey):
    t=SortByName.tryof(sortKey)
    return t

