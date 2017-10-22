import time

def showCommands():
    cmds = "Command list:\n"
    cmds += "- exit\n"
    cmds += "- add <value><type><description(1 word)>\n"
    cmds += "- remove <day> / <start day> to <end day> / <type>\n"
    cmds += "- replace <day><type><description> with <value>\n"
    cmds += "\n"

    print(cmds)

def initializeCmdList():
    cmds = {"add":addTransaction, "insert":insertTransaction, "remove":removeTransaction, "replace":replaceTransaction}

    return cmds

def readCommand():
    cmd = input("Type command:\n")

    if cmd.find(' ') == -1:
        command = cmd
        params = ""
    else:
        command = cmd[0:cmd.find(' ')]
        params = cmd[cmd.find(' ')+1:]

        params = params.split(' ')
        for i in params:
            i.strip(' ')

    return (command, params)

def testGiveInt():
    assert giveInt("2343") == 2343
    assert giveInt("3d331") == False

def giveInt(x):
    '''
        Checks if a string can be an integer and returns it if so.
        I: string
        O: integer value or False
    '''
    try:
        val = int(x)
        return val
    except ValueError:
        return False

def testValidType():
    assert validType("in") == "in"
    assert validType("out") == "out"
    assert not validType("in") == "out"
    assert validType("indaw") == False

def validType(tp):
    '''
        Checks if the transaction type was correctly introduced.
        I: type
        O: type or
            False, if it's incorrect
    '''
    if tp == "in" or tp == "out":
        return tp
    else:
        return False

def testAddTrans():
    t = []
    initTrans(t)

    last = addTransaction(t, ["233", "out", "food"])
    assert last[0] == 22
    assert last[1] == 233
    assert last[2] == "out"
    assert last[3] == "food"

    last = addTransaction(t, ["233", "outw", "food"])
    assert last == False

    last = addTransaction(t, ["33dw2", "out", "food"])
    assert last == False

def addTransaction(t, p):
    '''
        Appends a trasaction to the transaction list for the current day.
        I: t(transaction list), p(parameters of the transaction)
        O: last transaction added
    '''
    if len(p) == 3:
        day = int(time.strftime("%d"))
        value = giveInt(p[0])
        type = validType(p[1])
        description = p[2]

        if value != False and type != False:
            t.append([day, value, type, description])
            return t[len(t) - 1]
        else:
            print("Invalid command.")
            return False
    else:
        print("Invalid command.")
        return False

def testInsertTrans():
    t = []
    initTrans(t)

    last = insertTransaction(t, ["12", "233", "out", "food"])
    assert last[0] == 12
    assert last[1] == 233
    assert last[2] == "out"
    assert last[3] == "food"

    last = insertTransaction(t, ["4", "233", "outw", "food"])
    assert last == False

    last = insertTransaction(t, ["13", "33dw2", "out", "food"])
    assert last == False

    last = insertTransaction(t, ["3 13", "332", "out", "food"])
    assert last == False

def insertTransaction(t, p):
    '''
        Appends a trasaction to the transaction list for a given day.
        I: t(transaction list), p(parameters of the transaction)
        O: last transaction added
    '''
    if len(p) == 4:
        day = giveInt(p[0])
        value = giveInt(p[1])
        type = validType(p[2])
        description = p[3]

        if day != False and value != False and type != False:
            t.append([day, value, type, description])
            return t[len(t) - 1]
        else:
            print("Invalid command.", len(t))
            return False
    else:
        print("Invalid command.")
        return False

def posToRemove(t, p):
    '''
        Finds the positions of the transactions that have to be removed.
        I: t(transaction list), p(parameters of the transaction)
        O: list of positions
    '''
    pos = []

    if p[0] == "in":
        for i in range(len(t)):
            if t[2] == "in":
                pos.append(i)
    elif len(p) == 1:
        day = giveInt(p[0])

        if day == False:
            return False
        else:
            for i in range(len(t)):
                if t[0] == day:
                    pos.append(i)
    elif len(p) == 3:
        day_start = giveInt(p[0])
        day_end= giveInt(p[2])

        if day_start == False or day_end == False or p[1] != "to":
            return False
        else:
            for i in range(len(t)):
                if t[0] >= day_start and t[0] <= day_end:
                    pos.append(i)
    else:
        return False

    return pos


def removeTransaction(t, p):
    '''
        Removes transactions.
        I: t(transaction list), p(parameters of the transaction)
    '''
    pos = posToRemove(t, p)

    if pos == False:
        print("Invalid command.")
    else:
        for i in pos:
            t.remove(i)

def testFindTrans():
    t = []
    initTrans(t)

    #assert findTransaction(t, ["13", "in", "found"]) == 7
    assert findTransaction(t, ["23", "in", "found"]) == False
    assert findTransaction(t, ["1g3", "in", "found"]) == False

def findTransaction(t, p):
    if len(p) == 5:
        day = giveInt(p[0])
        type = validType(p[1])
        description = p[2]

        if day != False and type != False:
            for i in range(len(t)):
                if t[i][0] == day and t[i][2] == type and t[i][3] == description:
                    print(i, "\n")
                    return i
        else:
            print("Invalid command.")
            return False
    else:
        print("Invalid command.")
        return False

    return False

def replaceTransaction(t, p):
    pos = findTransaction(t, p)
    new_value = giveInt(p[4])

    if pos != False:
        t[pos][1] =  new_value

def initTrans(t):
    addTransaction(t, ["2342", "in", "salary"])
    addTransaction(t, ["300", "in", "stuff"])
    addTransaction(t, ["50", "out", "kfc"])
    addTransaction(t, ["43", "in", "gambling"])
    addTransaction(t, ["544", "out", "gambling"])
    insertTransaction(t, ["31", "40", "out", "borrowed"])
    insertTransaction(t, ["11", "200", "in", "salary"])
    insertTransaction(t, ["13", "1000", "in", "found"])
    insertTransaction(t, ["12", "243", "out", "leftover"])
    #insertTransaction(t, ["12", "10000", "in", "gambling"])


def runTests():
    testGiveInt()
    testValidType()
    testAddTrans()
    testInsertTrans()
    testFindTrans()

def run():
    print("Welcome!")

    commands = initializeCmdList()
    transactions = []

    initTrans(transactions)

    while True:
        showCommands()

        cmd = readCommand()

        command = cmd[0]
        params = cmd[1]

        if command == "exit":
            return
        elif command in commands:
            commands[command](transactions, params)
            for t in transactions:
                print(t)
        else:
            print("Invalid command!")
        print('\n')

runTests()
run()