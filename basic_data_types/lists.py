def fillCommands(N):
    cmds = list()
    for i in range(N):
        cmds.append(input())
    return cmds

def executeCommands(cmds):
    output = list()
    for element in cmds:
        operation = element.split(" ")
        operation_type = operation[0]
        
        if operation_type == "insert":
            output.insert(int(operation[1]),int(operation[2]))

        elif operation_type == "print":
            print(output)

        elif operation_type == "remove":
            output.remove(int(operation[1]))

        elif operation_type == "append":
            output.append(int(operation[1]))

        elif operation_type == "sort":
            output.sort()

        elif operation_type == "pop":
            output.pop()

        elif operation_type == "reverse":
            output.reverse()

if __name__ == '__main__':
    N = int(input())
    executeCommands(fillCommands(N))