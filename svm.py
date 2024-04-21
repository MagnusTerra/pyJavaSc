import sys
import parserJS

dicConditions = {
	'<' 	: lambda x,y : int(x < y),
	'>' 	: lambda x,y : int(x > y),
	'<=' 	: lambda x,y : int(x <= y),
	'>=' 	: lambda x,y : int(x >= y),
	'===' 	: lambda x,y : int(x == y and type(y)==type(x)),
	'!==' 	: lambda x,y : int(x != y or type(y)!=type(x)),
	'==' 	: lambda x,y : int(x == y),
	'!=' 	: lambda x,y : int(x != y)
}

def parse(filename):
    code = [line.split(':') for line in open(filename)]
    adresses = {}

    for num, line in enumerate(code):
        if len(line) == 2:
            adresses[line[0]] = num
            del line[0]

    code = [line[0].split() for line in code]
    
    return code, adresses

def execute(code, adresses):
    ip = 0 # instruction pointer
    stack = [] # execution stack
    vars = {} # "central memory"

    # this is for speed optimization
    spop = stack.pop
    sappend = stack.append

    nb_instr = len(code)
    while ip < nb_instr:
        mnemo = code[ip][0]
        # Stack and memory manipulation
        if mnemo == "PUSHC":
            sappend(float(code[ip][1]))
        elif mnemo == "PUSHV":
            sappend(vars[code[ip][1]])    
        elif mnemo == "SET":
            val = spop()
            vars[code[ip][1]] = val
            
        # Printing
        elif mnemo == "PRINT":
            print (spop())
            
        # Arithmetics
        elif mnemo == "ADD":
            val2 = spop()
            val1 = spop()
            sappend(val1+val2)
        elif mnemo == "SUB":
            val2 = spop()
            val1 = spop()
            sappend(val1-val2)
        elif mnemo == "MUL":
            val2 = spop()
            val1 = spop()
            sappend(val1*val2)    
        elif mnemo == "DIV":
            val2 = spop()
            val1 = spop()
            sappend(val1/val2)    
        elif mnemo =="USUB":
            stack[-1] = -stack[-1]
        
        #conditions
        elif mnemo == "COND_OP":
            val2 = spop()
            val1 = spop()
            sappend(dicConditions[code[ip][1]](val1,val2))
        elif mnemo == "OR":
            val2 = spop()
            val1 = spop()
            sappend(val1 or val2)
        elif mnemo =="AND":
            val2 = spop()
            val1 = spop()
            sappend(val1 and val2)
        elif mnemo =="NOT":
            stack[-1] = str(not int(stack[-1]))

        # (un)conditional jumps
        elif mnemo == "JMP":
            ip = adresses[code[ip][1]]
            continue
        elif mnemo == "JINZ":
            cond = spop()
            if cond != 0:
                ip = adresses[code[ip][1]]
                continue    
        elif mnemo == "JIZ":
            cond = spop()
            if cond == 0:
                ip = adresses[code[ip][1]]
                continue     
        elif mnemo == "BREAK":
            continue
        elif mnemo =="VOID":
            try:
                code[ip+1][0]
            except :
                break
        elif mnemo=="EF":
            ip = adresses[code[ip-1 if ip >2 else ip  ][1]]
            continue
        else:
            parserJS.p_case_pro(str(sys.argv[1]))
            break
        ip += 1
        
import AST,re
from AST import addToClass

operations = {
	'+' : 'ADD',
	'-' : 'SUB',
	'*' : 'MUL',
	'/' : 'DIV'
}

operationsLambda = {
	'ADD' : lambda x,y: x+y,
	'SUB' : lambda x,y: x-y,
	'MUL' : lambda x,y: x*y,
	'DIV' : lambda x,y: x/y 
}


varValues = {} # varName : Value -> scope managed in parser
funcStorage={}

def condcounter():
	condcounter.current += 1
	return condcounter.current

condcounter.current = 0


def funcVarCounter():
	funcVarCounter.current += 1
	return funcVarCounter.current

funcVarCounter.current = 0

def functioncounter():
	functioncounter.current += 1
	return functioncounter.current

functioncounter.current = 0

#program
@addToClass(AST.ProgramNode)

def compile(self):
	bytecode = ""
	for c in self.children:
		bytecode += c.compile()
	return bytecode

#node variable
@addToClass(AST.TokenNode)
def compile(self):
	bytecode = ""
	if isinstance(self.tok, str) and self.tok !="1":
		bytecode += "PUSHV %s\n" % self.tok
	else:
		bytecode += "PUSHC %s\n" % self.tok
	return bytecode

####################################################################################################################

###################################################### FUNCTIONS ###################################################



@addToClass(AST.FunctionNode)
def compile(self):
	fcounter = functioncounter()
	bytecode=""
	funcStorage[self.children[0].tok]=fcounter
	if type(self.children[1])=="ArgNode":
		counter=funcVarCounter()
		fcounter = functioncounter()
		bytecode = "func%s: " % fcounter
		bytecode+=self.children[1].compile(counter)
		bytecode += self.children[2].compile()	
		bytecode+="EF\n"
	else :
		bytecode = "func%s: " % fcounter
		bytecode += self.children[2].compile()
		bytecode+="EF\n"
	return bytecode

@addToClass(AST.ReturnNode)
def compile(self):
	bytecode=""
	bytecode+=(self.children[0].compile())
	return bytecode

@addToClass(AST.ArgNode)
def compile(self,counter):
	bytecode = ""
	if counter :
		bytecode += "PUSHC %s" % self.children[0].tok
		bytecode+="SET funcVar"+counter+"\n"
	return bytecode

@addToClass(AST.FunctionCallNode)
def compile(self):
	if(type(self.children[0])=="ArgNode"):
		return f"JMP func{funcStorage[self.children[1].children[0].tok]}\n" 
	else:
		return f"JMP func{funcStorage[self.children[0].children[0].tok]}\n"

####################################################################################################################

################################################# OPERATIONS #######################################################

@addToClass(AST.OpNode)
def compile(self):
	bytecode = ""
	if len(self.children) == 1:
		bytecode += self.children[0].compile()
		bytecode += "USUB\n"
	else:
		for c in self.children:
			bytecode += c.compile()
		bytecode += operations[self.op] + "\n"
	return bytecode

@addToClass(AST.AssignNode)
def compile(self):
	compiledChildren = self.children[1].compile()
	search = re.search("\d+",compiledChildren)
	if search:
		if self.children[1].__class__.__name__!="OpNode": 
			varValues[self.children[0].tok] = float(search.group(0))
		else:
			searchOperation = 	'ADD' if compiledChildren.find('ADD') else \
								'MUL' if compiledChildren.find('MUL') else \
								'DIV' if compiledChildren.find('DIV') else \
								'SUB' if compiledChildren.find('SUB') else ""
			try:
				varValues[self.children[0].tok] = operationsLambda[searchOperation](float(search.group(0)),float(search.group(1)))
			except IndexError:
				varValues[self.children[0].tok] = -float(search.group(0))
	else:
		pass

	bytecode = compiledChildren
	bytecode += "SET %s\n" % self.children[0].tok
	return bytecode

@addToClass(AST.VariableNode)
def compile(self):
	return "" 

@addToClass(AST.ArrayNode)
def compile(self):
	return ""

####################################################################################################################

################################################# STRUCTURE ########################################################


@addToClass(AST.IfNode)
def compile(self):
	counter = condcounter()
	bytecode = self.children[0].compile()
	bytecode +="JMP cond%s\n" % counter 
	bytecode += "bodyThen%s: " % counter 
	bytecode += self.children[1].compile()
	bytecode +="JMP endif%s\n" % counter
	if len(self.children)>2:
		bytecode += "bodyElse%s: " % counter 
		bytecode += self.children[2].compile()
		bytecode +="JMP endif%s\n "% counter
	bytecode += "cond%s: " % counter
	bytecode += self.children[1].compile() 
	bytecode += "JINZ bodyThen%s\n" % counter
	bytecode += "cond%s: " % counter
	bytecode += self.children[1].compile() 
	bytecode += "JIZ bodyElse%s\n" % counter
	bytecode += "endif%s: VOID\n" % counter
	return bytecode

@addToClass(AST.ElseNode)
def compile(self):
	return self.children[0].compile()

@addToClass(AST.ForNode)
def compile(self):
	counter = condcounter() 
	bytecode = self.children[0].compile()
	bytecode +="JMP cond%s\n" % counter 
	bytecode += "body%s: " % counter 
	bytecode += self.children[2].compile()
	bytecode += self.children[3].compile() 
	bytecode += "cond%s: " % counter
	bytecode += self.children[1].compile() 
	bytecode += "JINZ body%s\n" % counter 
	return bytecode	

@addToClass(AST.StartForNode)
def compile(self):
	return self.children[0].compile()

@addToClass(AST.IncForNode)
def compile(self):
	return self.children[0].compile()

@addToClass(AST.WhileNode)
def compile(self):
	counter = condcounter() 
	bytecode = "JMP cond%s\n" % counter 
	bytecode += "body%s: " % counter 
	bytecode += self.children[1].compile() 
	bytecode += "cond%s: " % counter
	bytecode += self.children[0].compile() 
	bytecode += "JINZ body%s\n" % counter 
	return bytecode

@addToClass(AST.DoNode)
def compile(self):
	return self.children[0].compile() + self.children[1].compile()

@addToClass(AST.SwitchNode)
def compile(self):
	if len(self.children)==2 and self.children[1].type=='Token':return "" #void switch
	for children in self.children[1:]:
		if children.type !='Default' and float(children.children[0].tok) == varValues[self.children[0].tok]:
			return children.compile()
	for children in self.children[1:]:
		if children.type =='Default':
			return children.compile()
	return ""

@addToClass(AST.CaseNode)
def compile(self):
	return self.children[1].compile()

@addToClass(AST.DefaultNode)
def compile(self):
	return self.children[0].compile()

####################################################################################################################

################################################# STATEMENT ########################################################

@addToClass(AST.LogNode)
def compile(self):
	bytecode = ""
	bytecode += self.children[0].compile()
	bytecode += "PRINT\n"
	return bytecode

@addToClass(AST.BreakNode)
def compile(self):
	return "BREAK\n"

@addToClass(AST.ContinueNode)
def compile(self):
	return f"JMP cond{condcounter()-1}\n"

####################################################################################################################

############################################ CONDITIONS ############################################################

@addToClass(AST.ConditionNode)
def compile(self):
	bytecode = self.children[0].compile()
	bytecode += self.children[2].compile()
	bytecode += f"COND_OP {self.children[1].tok}\n"
	return bytecode
	
@addToClass(AST.AndNode)
def compile(self):
	bytecode = self.children[0].compile()
	bytecode+= self.children[1].compile()
	bytecode+="AND\n"
	return bytecode

@addToClass(AST.OrNode)
def compile(self):
	bytecode = self.children[0].compile()
	bytecode+= self.children[1].compile()
	bytecode+="OR\n"
	return bytecode

@addToClass(AST.NotNode)
def compile(self):
	bytecode = self.children[0].compile()
	bytecode+="NOT\n"
	return bytecode
        
        
if __name__ == '__main__':
    code, adresses = parse(sys.argv[1])
    execute(code, adresses)
