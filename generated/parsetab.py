
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "programleftNEWLINEELSEORIDENTIFIER,;nonassocLTGTEQUALVEQUALVTNOTEQUALVNOTEQUALVTLTEGTEleftANDleftADD_OPleftMUL_OPrightUMINUS!ADD_OP AND BREAK CASE CONTINUE DEFAULT DO ELSE EQUALV EQUALVT FOR FUNCTION GT GTE IDENTIFIER IF LET LOG LT LTE MUL_OP NEWLINE NOTEQUALV NOTEQUALVT NUMBER OR RETURN SWITCH VAR WHILEnew_scope :  program : NEWLINE program program : statement  ';' NEWLINE\n    | statement NEWLINE  program : statement ';' program \n    | statement NEWLINE program  programBlock : '{' new_scope program '}'  programBlock : NEWLINE programBlockcaseProgram : ':' new_scope program programStatement : statementstatement : NEWLINE statement statement : assignation\n    | structure \n    | structureIf\n    | structureTernary\n    | logStatement\n    | breakStatement\n    | continueStatement \n    | functionDeclaration\n    | functionCall\n    | returnStatement\n    | varListstructureIf : IF '(' condition ')' programStatement NEWLINE\n    | IF '(' condition ')' programBlock structureElse : ELSE programStatement \n    | ELSE programBlock structure : structureIf structureElsestructureTernary : condition '?' returnValues ':' returnValues structure : FOR new_scope '(' assignation ';' condition ';' assignation ')' programBlock \n    | FOR new_scope '(' assignation ';' condition ';' assignation ')' programStatement  structure : WHILE '(' condition ')' programStatement \n    | WHILE '(' condition ')' programBlockstructure : DO programBlock WHILE '(' condition ')' structure : DO programStatement NEWLINE WHILE '(' condition ')'  structure : SWITCH '(' IDENTIFIER ')' '{' new_scope caseList '}'  structure : SWITCH '(' IDENTIFIER ')' '{' '}' caseList : NEWLINE caseListcaseStructure : CASE expression caseProgram caseList : caseStructure caseStructure : DEFAULT caseProgram caseList : caseList NEWLINE caseStructure caseList : caseList caseStructure conditionSymbol : LT\n    | GT\n    | LTE\n    | GTE\n    | EQUALV\n    | EQUALVT\n    | NOTEQUALV\n    | NOTEQUALVT\n    condition : '!' conditioncondition : condition AND conditioncondition : condition OR conditioncondition : expression conditionSymbol expressioncondition : '(' condition ')'  breakStatement : BREAK  continueStatement : CONTINUE  logStatement : LOG '(' returnValues ')' varCreation : VAR IDENTIFIER\n    | LET IDENTIFIERvarList : varCreationvarList : varList ',' IDENTIFIERarrayDeclaration : '[' ']' arrayDeclaration : '[' tokenList ']' tokenList : IDENTIFIER\n    | NUMBER tokenList : tokenList ',' IDENTIFIER\n    | tokenList ',' NUMBER  expression : IDENTIFIER '[' NUMBER ']' expression : NUMBER expression : IDENTIFIER expression : '(' expression ')' expression : expression ADD_OP expression\n    | expression MUL_OP expression expression : ADD_OP expression %prec UMINUSassignation : IDENTIFIER ADD_OP '=' expression\n    | IDENTIFIER MUL_OP '=' expression \n    | IDENTIFIER ADD_OP '=' functionCall\n    | IDENTIFIER MUL_OP '=' functionCallassignation : IDENTIFIER ADD_OP ADD_OP assignation : IDENTIFIER '=' returnValues assignation : varList '=' returnValues\n    | varList '=' structureTernaryfunctionDeclaration : FUNCTION IDENTIFIER '(' new_scope argList ')' programBlockfunctionDeclaration : FUNCTION IDENTIFIER '(' ')' programBlockargList : IDENTIFIERargList : argList ',' IDENTIFIERfunctionCall : IDENTIFIER '(' expressionList ')' functionCall : IDENTIFIER '(' ')' expressionList : expressionexpressionList : expressionList ',' expression returnStatement : RETURN returnStatement : RETURN returnValues\n    | RETURN conditionreturnValues : expression\n    | arrayDeclaration\n    | functionCall"
    
_lr_action_items = {'NEWLINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,22,26,27,29,30,34,35,36,37,38,39,40,48,49,70,71,72,73,78,79,80,81,82,83,85,86,87,88,89,90,91,92,93,94,95,97,98,100,101,104,108,109,110,112,113,115,116,120,121,122,127,132,133,134,135,136,138,143,148,149,151,152,156,157,158,161,162,163,164,167,168,172,174,175,176,177,180,181,182,183,186,189,191,192,194,195,196,197,198,199,200,201,202,],[2,2,38,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,71,-56,-57,-92,-61,-70,-2,-11,88,-4,-27,71,-75,-71,119,71,-1,-10,-93,-94,-95,-96,-97,-71,-51,-59,-60,-3,-5,-6,-25,-26,-82,-83,-95,-62,-80,-81,-95,-89,-54,-73,-74,-55,-72,-52,-53,-8,-11,2,-63,-76,-78,-77,-79,-88,-69,71,71,-58,168,-64,-28,-31,-32,-7,-1,176,-24,-85,168,-33,182,-36,-23,168,-34,190,182,-39,-84,-35,-42,-37,-40,-1,71,-41,-38,2,-29,-30,-9,]),'IDENTIFIER':([0,2,16,19,22,28,29,31,32,33,37,38,40,41,42,44,46,50,51,52,53,54,55,56,57,58,59,60,61,65,66,67,68,71,72,74,75,76,84,88,96,99,102,111,122,126,137,142,143,144,148,150,153,155,160,178,179,184,195,196,199,],[15,15,49,49,15,77,83,49,86,87,15,15,15,83,97,83,49,49,49,49,49,-43,-44,-45,-46,-47,-48,-49,-50,83,49,49,49,15,-1,123,49,83,129,15,49,83,83,140,15,-1,49,83,15,49,15,165,169,49,49,187,140,49,-1,15,15,]),'FOR':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[18,18,18,18,18,18,18,-1,18,18,18,18,-1,18,18,]),'WHILE':([0,2,22,37,38,40,69,71,72,88,119,120,122,143,148,161,195,196,199,],[21,21,21,21,21,21,118,21,-1,21,145,-8,21,21,21,-7,-1,21,21,]),'DO':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[22,22,22,22,22,22,22,-1,22,22,22,22,-1,22,22,]),'SWITCH':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[23,23,23,23,23,23,23,-1,23,23,23,23,-1,23,23,]),'IF':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[24,24,24,24,24,24,24,-1,24,24,24,24,-1,24,24,]),'LOG':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[25,25,25,25,25,25,25,-1,25,25,25,25,-1,25,25,]),'BREAK':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[26,26,26,26,26,26,26,-1,26,26,26,26,-1,26,26,]),'CONTINUE':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[27,27,27,27,27,27,27,-1,27,27,27,27,-1,27,27,]),'FUNCTION':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[28,28,28,28,28,28,28,-1,28,28,28,28,-1,28,28,]),'RETURN':([0,2,22,37,38,40,71,72,88,122,143,148,195,196,199,],[29,29,29,29,29,29,29,-1,29,29,29,29,-1,29,29,]),'!':([0,2,19,22,29,31,37,38,40,41,66,67,68,71,72,75,88,96,122,143,144,148,155,160,195,196,199,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,-1,31,31,31,31,31,31,31,31,31,-1,31,31,]),'(':([0,2,15,16,18,19,21,22,23,24,25,29,31,37,38,40,41,44,46,50,51,52,53,54,55,56,57,58,59,60,61,62,65,66,67,68,71,72,75,76,77,83,88,96,99,102,118,122,137,142,143,144,145,148,155,160,184,195,196,199,],[19,19,46,50,-1,19,68,19,74,75,76,19,19,19,19,19,96,50,50,50,50,50,50,-43,-44,-45,-46,-47,-48,-49,-50,111,50,19,19,19,19,-1,19,50,126,46,19,96,50,50,144,19,50,50,19,19,160,19,19,19,50,-1,19,19,]),'VAR':([0,2,22,37,38,40,71,72,88,111,122,143,148,179,195,196,199,],[32,32,32,32,32,32,32,-1,32,32,32,32,32,32,-1,32,32,]),'LET':([0,2,22,37,38,40,71,72,88,111,122,143,148,179,195,196,199,],[33,33,33,33,33,33,33,-1,33,33,33,33,33,33,-1,33,33,]),'NUMBER':([0,2,16,19,22,29,31,37,38,40,41,44,46,47,50,51,52,53,54,55,56,57,58,59,60,61,65,66,67,68,71,72,75,76,84,88,96,99,102,122,137,142,143,144,148,153,155,160,184,195,196,199,],[34,34,34,34,34,34,34,34,34,34,34,34,34,106,34,34,34,34,-43,-44,-45,-46,-47,-48,-49,-50,34,34,34,34,34,-1,34,34,130,34,34,34,34,34,34,34,34,34,34,170,34,34,34,-1,34,34,]),'ADD_OP':([0,2,15,16,17,19,22,29,31,34,37,38,40,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,64,65,66,67,68,71,72,75,76,80,83,88,95,96,99,101,102,105,107,108,109,110,113,122,131,132,134,137,138,140,142,143,144,148,154,155,160,184,193,195,196,199,],[16,16,43,16,52,16,16,16,16,-70,16,16,16,16,98,16,16,-75,-71,16,16,16,16,-43,-44,-45,-46,-47,-48,-49,-50,52,16,16,16,16,16,-1,16,16,52,-71,16,52,16,16,52,16,52,52,52,-73,-74,-72,16,52,52,52,16,-69,43,16,16,16,16,52,16,16,16,52,-1,16,16,]),'$end':([1,35,38,88,89,90,],[0,-2,-4,-3,-5,-6,]),';':([3,4,5,6,7,8,9,10,11,12,13,14,26,27,29,30,34,36,39,48,49,73,78,79,80,81,82,83,85,86,87,91,92,93,94,95,97,98,100,101,104,108,109,110,112,113,115,116,120,121,127,132,133,134,135,136,138,139,149,152,156,157,158,161,164,167,171,172,175,176,180,186,189,200,201,],[37,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-56,-57,-92,-61,-70,-11,-27,-75,-71,-10,-93,-94,-95,-96,-97,-71,-51,-59,-60,-25,-26,-82,-83,-95,-62,-80,-81,-95,-89,-54,-73,-74,-55,-72,-52,-53,-8,-11,-63,-76,-78,-77,-79,-88,-69,155,-58,-64,-28,-31,-32,-7,-24,-85,179,-33,-36,-23,-34,-84,-35,-29,-30,]),'ELSE':([6,120,161,164,176,],[40,-8,-7,-24,-23,]),'=':([14,15,30,43,45,86,87,97,140,141,],[41,44,-61,99,102,-59,-60,-62,44,41,]),',':([14,30,34,48,49,86,87,97,103,105,109,110,113,128,129,130,138,141,154,165,166,169,170,187,],[42,-61,-70,-75,-71,-59,-60,-62,137,-90,-73,-74,-72,153,-65,-66,-69,42,-91,-86,178,-67,-68,-87,]),'MUL_OP':([15,17,34,48,49,64,80,83,95,101,105,107,108,109,110,113,131,132,134,138,140,154,193,],[45,53,-70,-75,-71,53,53,-71,53,53,53,53,53,53,-74,-72,53,53,53,-69,45,53,53,]),'[':([15,29,41,44,49,65,76,83,142,],[47,84,84,84,47,84,84,47,84,]),'LT':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,54,-70,-75,-71,54,54,-71,54,-73,-74,-72,54,-69,]),'GT':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,55,-70,-75,-71,55,55,-71,55,-73,-74,-72,55,-69,]),'LTE':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,56,-70,-75,-71,56,56,-71,56,-73,-74,-72,56,-69,]),'GTE':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,57,-70,-75,-71,57,57,-71,57,-73,-74,-72,57,-69,]),'EQUALV':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,58,-70,-75,-71,58,58,-71,58,-73,-74,-72,58,-69,]),'EQUALVT':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,59,-70,-75,-71,59,59,-71,59,-73,-74,-72,59,-69,]),'NOTEQUALV':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,60,-70,-75,-71,60,60,-71,60,-73,-74,-72,60,-69,]),'NOTEQUALVT':([15,17,34,48,49,64,80,83,95,109,110,113,131,138,],[-71,61,-70,-75,-71,61,61,-71,61,-73,-74,-72,61,-69,]),'?':([20,34,48,49,85,108,109,110,112,113,115,116,138,],[65,-70,-75,-71,-51,-54,-73,-74,-55,-72,-52,-53,-69,]),'AND':([20,34,48,49,63,79,85,108,109,110,112,113,115,116,117,124,138,159,171,173,],[66,-70,-75,-71,66,66,-51,-54,-73,-74,-55,-72,-52,66,66,66,-69,66,66,66,]),'OR':([20,34,48,49,63,79,85,108,109,110,112,113,115,116,117,124,138,159,171,173,],[67,-70,-75,-71,67,67,-51,-54,-73,-74,-55,-72,-52,-53,67,67,-69,67,67,67,]),'{':([22,40,71,143,147,148,151,168,177,196,],[72,72,72,72,162,72,72,72,72,72,]),')':([34,46,48,49,63,64,81,82,83,85,93,94,95,98,100,101,103,104,105,107,108,109,110,112,113,115,116,117,123,124,125,126,127,131,132,133,134,135,136,138,152,154,156,159,165,166,173,187,188,],[-70,104,-75,-71,112,113,-96,-97,-71,-51,-82,-83,-95,-80,-81,-95,136,-89,-90,113,-54,-73,-74,-55,-72,-52,-53,143,147,148,149,151,-63,113,-76,-78,-77,-79,-88,-69,-64,-91,-28,172,-86,177,180,-87,196,]),':':([34,48,49,81,82,83,101,104,109,110,113,114,127,136,138,152,185,193,],[-70,-75,-71,-96,-97,-71,-95,-89,-73,-74,-72,142,-63,-88,-69,-64,195,195,]),'}':([35,38,88,89,90,146,162,181,183,191,192,194,197,198,202,],[-2,-4,-3,-5,-6,161,175,189,-39,-42,-37,-40,-41,-38,-9,]),'CASE':([35,38,88,89,90,162,174,181,182,183,190,191,192,194,197,198,202,],[-2,-4,-3,-5,-6,-1,184,184,184,-39,184,-42,-37,-40,-41,-38,-9,]),'DEFAULT':([35,38,88,89,90,162,174,181,182,183,190,191,192,194,197,198,202,],[-2,-4,-3,-5,-6,-1,185,185,185,-39,185,-42,-37,-40,-41,-38,-9,]),']':([84,106,128,129,130,169,170,],[127,138,152,-65,-66,-67,-68,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,2,37,38,88,122,199,],[1,35,89,90,35,146,202,]),'statement':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[3,36,73,3,3,73,121,36,3,73,73,73,3,]),'assignation':([0,2,22,37,38,40,71,88,111,122,143,148,179,196,199,],[4,4,4,4,4,4,4,4,139,4,4,4,188,4,4,]),'structure':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[5,5,5,5,5,5,5,5,5,5,5,5,5,]),'structureIf':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[6,6,6,6,6,6,6,6,6,6,6,6,6,]),'structureTernary':([0,2,22,37,38,40,41,71,88,122,143,148,196,199,],[7,7,7,7,7,7,94,7,7,7,7,7,7,7,]),'logStatement':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[8,8,8,8,8,8,8,8,8,8,8,8,8,]),'breakStatement':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[9,9,9,9,9,9,9,9,9,9,9,9,9,]),'continueStatement':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[10,10,10,10,10,10,10,10,10,10,10,10,10,]),'functionDeclaration':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[11,11,11,11,11,11,11,11,11,11,11,11,11,]),'functionCall':([0,2,22,29,37,38,40,41,44,65,71,76,88,99,102,122,142,143,148,196,199,],[12,12,12,82,12,12,12,82,82,82,12,82,12,133,135,12,82,12,12,12,12,]),'returnStatement':([0,2,22,37,38,40,71,88,122,143,148,196,199,],[13,13,13,13,13,13,13,13,13,13,13,13,13,]),'varList':([0,2,22,37,38,40,71,88,111,122,143,148,179,196,199,],[14,14,14,14,14,14,14,14,141,14,14,14,141,14,14,]),'expression':([0,2,16,19,22,29,31,37,38,40,41,44,46,50,51,52,53,65,66,67,68,71,75,76,88,96,99,102,122,137,142,143,144,148,155,160,184,196,199,],[17,17,48,64,17,80,17,17,17,17,95,101,105,107,108,109,110,101,17,17,17,17,17,101,17,131,132,134,17,154,101,17,17,17,17,17,193,17,17,]),'condition':([0,2,19,22,29,31,37,38,40,41,66,67,68,71,75,88,96,122,143,144,148,155,160,196,199,],[20,20,63,20,79,85,20,20,20,20,115,116,117,20,124,20,63,20,20,159,20,171,173,20,20,]),'varCreation':([0,2,22,37,38,40,71,88,111,122,143,148,179,196,199,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'structureElse':([6,],[39,]),'conditionSymbol':([17,64,80,95,131,],[51,51,51,51,51,]),'new_scope':([18,72,126,162,195,],[62,122,150,174,199,]),'programBlock':([22,40,71,143,148,151,168,177,196,],[69,92,120,158,164,167,120,186,200,]),'programStatement':([22,40,143,148,196,],[70,91,157,163,201,]),'returnValues':([29,41,44,65,76,142,],[78,93,100,114,125,156,]),'arrayDeclaration':([29,41,44,65,76,142,],[81,81,81,81,81,81,]),'expressionList':([46,],[103,]),'tokenList':([84,],[128,]),'argList':([150,],[166,]),'caseList':([174,182,],[181,192,]),'caseStructure':([174,181,182,190,192,],[183,191,183,197,191,]),'caseProgram':([185,193,],[194,198,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('new_scope -> <empty>','new_scope',0,'p_new_scope','parserJS.py',30),
  ('program -> NEWLINE program','program',2,'p_newline_program','parserJS.py',42),
  ('program -> statement ; NEWLINE','program',3,'p_program','parserJS.py',46),
  ('program -> statement NEWLINE','program',2,'p_program','parserJS.py',47),
  ('program -> statement ; program','program',3,'p_program_recursive','parserJS.py',51),
  ('program -> statement NEWLINE program','program',3,'p_program_recursive','parserJS.py',52),
  ('programBlock -> { new_scope program }','programBlock',4,'p_program_block','parserJS.py',56),
  ('programBlock -> NEWLINE programBlock','programBlock',2,'p_newline_program_block','parserJS.py',61),
  ('caseProgram -> : new_scope program','caseProgram',3,'p_case_program','parserJS.py',65),
  ('programStatement -> statement','programStatement',1,'p_program_statement','parserJS.py',70),
  ('statement -> NEWLINE statement','statement',2,'p_newline_statement','parserJS.py',77),
  ('statement -> assignation','statement',1,'p_statement','parserJS.py',81),
  ('statement -> structure','statement',1,'p_statement','parserJS.py',82),
  ('statement -> structureIf','statement',1,'p_statement','parserJS.py',83),
  ('statement -> structureTernary','statement',1,'p_statement','parserJS.py',84),
  ('statement -> logStatement','statement',1,'p_statement','parserJS.py',85),
  ('statement -> breakStatement','statement',1,'p_statement','parserJS.py',86),
  ('statement -> continueStatement','statement',1,'p_statement','parserJS.py',87),
  ('statement -> functionDeclaration','statement',1,'p_statement','parserJS.py',88),
  ('statement -> functionCall','statement',1,'p_statement','parserJS.py',89),
  ('statement -> returnStatement','statement',1,'p_statement','parserJS.py',90),
  ('statement -> varList','statement',1,'p_statement','parserJS.py',91),
  ('structureIf -> IF ( condition ) programStatement NEWLINE','structureIf',6,'p_if','parserJS.py',98),
  ('structureIf -> IF ( condition ) programBlock','structureIf',5,'p_if','parserJS.py',99),
  ('structureElse -> ELSE programStatement','structureElse',2,'p_else','parserJS.py',103),
  ('structureElse -> ELSE programBlock','structureElse',2,'p_else','parserJS.py',104),
  ('structure -> structureIf structureElse','structure',2,'p_if_else','parserJS.py',108),
  ('structureTernary -> condition ? returnValues : returnValues','structureTernary',5,'p_ternary_operator','parserJS.py',112),
  ('structure -> FOR new_scope ( assignation ; condition ; assignation ) programBlock','structure',10,'p_for','parserJS.py',117),
  ('structure -> FOR new_scope ( assignation ; condition ; assignation ) programStatement','structure',10,'p_for','parserJS.py',118),
  ('structure -> WHILE ( condition ) programStatement','structure',5,'p_while','parserJS.py',124),
  ('structure -> WHILE ( condition ) programBlock','structure',5,'p_while','parserJS.py',125),
  ('structure -> DO programBlock WHILE ( condition )','structure',6,'p_do_while','parserJS.py',129),
  ('structure -> DO programStatement NEWLINE WHILE ( condition )','structure',7,'p_do_while_without_bracket','parserJS.py',133),
  ('structure -> SWITCH ( IDENTIFIER ) { new_scope caseList }','structure',8,'p_case_pro','parserJS.py',139),
  ('structure -> SWITCH ( IDENTIFIER ) { }','structure',6,'p_switch_void','parserJS.py',151),
  ('caseList -> NEWLINE caseList','caseList',2,'p_newline_case_list','parserJS.py',159),
  ('caseStructure -> CASE expression caseProgram','caseStructure',3,'p_case','parserJS.py',163),
  ('caseList -> caseStructure','caseList',1,'p_case_list','parserJS.py',167),
  ('caseStructure -> DEFAULT caseProgram','caseStructure',2,'p_default','parserJS.py',171),
  ('caseList -> caseList NEWLINE caseStructure','caseList',3,'p_case_list_recursive_newline','parserJS.py',175),
  ('caseList -> caseList caseStructure','caseList',2,'p_case_list_recursive','parserJS.py',179),
  ('conditionSymbol -> LT','conditionSymbol',1,'p_conditionSymbol','parserJS.py',186),
  ('conditionSymbol -> GT','conditionSymbol',1,'p_conditionSymbol','parserJS.py',187),
  ('conditionSymbol -> LTE','conditionSymbol',1,'p_conditionSymbol','parserJS.py',188),
  ('conditionSymbol -> GTE','conditionSymbol',1,'p_conditionSymbol','parserJS.py',189),
  ('conditionSymbol -> EQUALV','conditionSymbol',1,'p_conditionSymbol','parserJS.py',190),
  ('conditionSymbol -> EQUALVT','conditionSymbol',1,'p_conditionSymbol','parserJS.py',191),
  ('conditionSymbol -> NOTEQUALV','conditionSymbol',1,'p_conditionSymbol','parserJS.py',192),
  ('conditionSymbol -> NOTEQUALVT','conditionSymbol',1,'p_conditionSymbol','parserJS.py',193),
  ('condition -> ! condition','condition',2,'p_condition_not','parserJS.py',198),
  ('condition -> condition AND condition','condition',3,'p_condition_and','parserJS.py',202),
  ('condition -> condition OR condition','condition',3,'p_condition_or','parserJS.py',206),
  ('condition -> expression conditionSymbol expression','condition',3,'p_condition','parserJS.py',210),
  ('condition -> ( condition )','condition',3,'p_condtition_paren','parserJS.py',214),
  ('breakStatement -> BREAK','breakStatement',1,'p_break','parserJS.py',221),
  ('continueStatement -> CONTINUE','continueStatement',1,'p_continue','parserJS.py',225),
  ('logStatement -> LOG ( returnValues )','logStatement',4,'p_log','parserJS.py',229),
  ('varCreation -> VAR IDENTIFIER','varCreation',2,'p_var_creation','parserJS.py',236),
  ('varCreation -> LET IDENTIFIER','varCreation',2,'p_var_creation','parserJS.py',237),
  ('varList -> varCreation','varList',1,'p_var_creation_list','parserJS.py',246),
  ('varList -> varList , IDENTIFIER','varList',3,'p_var_creation_list_recursive','parserJS.py',250),
  ('arrayDeclaration -> [ ]','arrayDeclaration',2,'p_array_empty','parserJS.py',260),
  ('arrayDeclaration -> [ tokenList ]','arrayDeclaration',3,'p_array_declaration','parserJS.py',264),
  ('tokenList -> IDENTIFIER','tokenList',1,'p_token_list','parserJS.py',268),
  ('tokenList -> NUMBER','tokenList',1,'p_token_list','parserJS.py',269),
  ('tokenList -> tokenList , IDENTIFIER','tokenList',3,'p_token_list_recursive','parserJS.py',273),
  ('tokenList -> tokenList , NUMBER','tokenList',3,'p_token_list_recursive','parserJS.py',274),
  ('expression -> IDENTIFIER [ NUMBER ]','expression',4,'p_array_access','parserJS.py',278),
  ('expression -> NUMBER','expression',1,'p_expression_num','parserJS.py',303),
  ('expression -> IDENTIFIER','expression',1,'p_expression_var','parserJS.py',307),
  ('expression -> ( expression )','expression',3,'p_expression_paren','parserJS.py',315),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parserJS.py',319),
  ('expression -> expression MUL_OP expression','expression',3,'p_expression_op','parserJS.py',320),
  ('expression -> ADD_OP expression','expression',2,'p_minus','parserJS.py',324),
  ('assignation -> IDENTIFIER ADD_OP = expression','assignation',4,'p_expression_op_assignation','parserJS.py',332),
  ('assignation -> IDENTIFIER MUL_OP = expression','assignation',4,'p_expression_op_assignation','parserJS.py',333),
  ('assignation -> IDENTIFIER ADD_OP = functionCall','assignation',4,'p_expression_op_assignation','parserJS.py',334),
  ('assignation -> IDENTIFIER MUL_OP = functionCall','assignation',4,'p_expression_op_assignation','parserJS.py',335),
  ('assignation -> IDENTIFIER ADD_OP ADD_OP','assignation',3,'p_expression_op_assign_double','parserJS.py',343),
  ('assignation -> IDENTIFIER = returnValues','assignation',3,'p_assign','parserJS.py',355),
  ('assignation -> varList = returnValues','assignation',3,'p_creation_assignation','parserJS.py',363),
  ('assignation -> varList = structureTernary','assignation',3,'p_creation_assignation','parserJS.py',364),
  ('functionDeclaration -> FUNCTION IDENTIFIER ( new_scope argList ) programBlock','functionDeclaration',7,'p_function_creation','parserJS.py',371),
  ('functionDeclaration -> FUNCTION IDENTIFIER ( ) programBlock','functionDeclaration',5,'p_function_creation_without_arg','parserJS.py',381),
  ('argList -> IDENTIFIER','argList',1,'p_arglist','parserJS.py',390),
  ('argList -> argList , IDENTIFIER','argList',3,'p_arglist_recursive','parserJS.py',397),
  ('functionCall -> IDENTIFIER ( expressionList )','functionCall',4,'p_function_call','parserJS.py',408),
  ('functionCall -> IDENTIFIER ( )','functionCall',3,'p_function_call_withous_args','parserJS.py',422),
  ('expressionList -> expression','expressionList',1,'p_expression_list','parserJS.py',435),
  ('expressionList -> expressionList , expression','expressionList',3,'p_expression_list_recursive','parserJS.py',439),
  ('returnStatement -> RETURN','returnStatement',1,'p_return','parserJS.py',443),
  ('returnStatement -> RETURN returnValues','returnStatement',2,'p_return_expression','parserJS.py',447),
  ('returnStatement -> RETURN condition','returnStatement',2,'p_return_expression','parserJS.py',448),
  ('returnValues -> expression','returnValues',1,'p_return_values','parserJS.py',452),
  ('returnValues -> arrayDeclaration','returnValues',1,'p_return_values','parserJS.py',453),
  ('returnValues -> functionCall','returnValues',1,'p_return_values','parserJS.py',454),
]
