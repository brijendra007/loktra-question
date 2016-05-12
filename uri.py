import re

class Uri():
    
    parameter=dict()
    path=''
    params=''
    scheme=''
    authority = None
    # i make all the regex of test cases of rfc3986 except tel+-192-2722 somethink like 
    #this and urn.oasis.... 
    urlfinders = [
    "([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?/[-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]*[^]'\\.}>\\),\\\"]",
    "([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}|(((news|telnet|nttp|file|http|ftp|https)://)|(www|ftp)[-A-Za-z0-9]*\\.)[-A-Za-z0-9\\.]+)(:[0-9]*)?",
    "(~/|/|\\./)([-A-Za-z0-9_\\$\\.\\+\\!\\*\\(\\),;:@&=\\?/~\\#\\%]|\\\\)+",
    "^([a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+.*)$",
    "((mailto\:|(www|news|(ht|f)tp(s?))\://){1}\S+)",
    "^([a-zA-Z0-9]*(\:[a-zA-Z0-9]+)+.*)$"
    ]
    def __init__(self,uri):
        self.uri1 = uri.strip()
        valid = self.validation(uri)
        if( valid == False):
            print "please enter the valid uri";
            return ;
        else:
            print "its valid Uri"
            scheme=self.getscheme()
            if(scheme):
                print " Scheme: " +scheme
                path=self.getpath()
            if(path):
                print " Path: " +path
            self.getparams()
            self.getAuthority();
            fragment=self.getfragment()
            if(fragment):
                print " Fragment: "  +fragment 
        
    def validation(self,uri):
        # valid the uri
        for regex in self.urlfinders:
            if(re.match(regex,uri)):
                return True
        return False
        
    def getscheme(self):
        #get the scheme using :
        if(':' in self.uri1):
            self.scheme=self.uri1.split(':')[0].lower()
            return self.scheme
        else:
            return "Scheme not found"
    def updatescheme(self,scheme):
        #update Scheme        
        if(':' in self.uri1):
            self.uri1.split(':')[0]=scheme
        else:
            self.uri1=list(self.uri1)
            self.uri1.insert(0,scheme+':\\\\')       
            return ''.join(self.uri1)
            
    def getpath(self):
        
        if(':' in self.uri1 or '.' in self.uri1):
            self.path=self.uri1[len(self.scheme) + 1:]
            return self.uri1[len(self.scheme) + 1:]
        else:
            print "Path not found"
    
    def updatespath(self,path):
        self.uri1[len(self.scheme) + 1:]=path
            
    def getfragment(self):
        
        if('#' in self.path):
            self.path, self.fragment = self.path.split('#')
            return self.fragment
        else:
            print "Fragment not found"    
            
    def updatesfragment(self,fragment):
        
        if(self.path.split('#')[1]):
            self.path.split('#')[1] = fragment
        else:
            print "Fragment not found"
            
    def getparams(self):
        if '?' in self.path:
            #find the parameter of query with seperator on the basis of & ;
            separator = '&' if '&' in self.path else ';' 
            query_params = self.path.split('?')[-1].split(separator)
            query_params = map(lambda p : p.split('='), query_params)
            self.parameters = {key : value for key, value in query_params}
            print "Parameter are" + self.parameters,
        else:
            print "Params not found"
            
    def getAuthority(self):
        
        if self.path.startswith('//') or '.' in self.path:
            self.path = self.path.lstrip('//')
            uri_tokens = self.path.split('/')

            self.authority = uri_tokens[0]
            self.hostname = self.authority
            self.path = self.path[len(self.authority):]
            self.authenticated = '@' in self.authority
            #fetching User Information
            if self.authenticated:
                self.user_information, self.hostname = self.authority.split('@', 1)
                print "User Information:" +self.user_information;
            # Fetching port
            self.port = None
            if ':' in self.hostname:
                self.hostname, self.port = self.hostname.split(':')
                self.port = int(self.port)
                print self.port+':',    
            # Hostnames are case-insensitive
            self.hostname = self.hostname.lower()
            print "Hostname:" +self.hostname
        
        else:
            print "Authorisation not found"
            
if __name__ == "__main__":                   
    inp=raw_input('Enter th Uri you want to check\n')
    obj=Uri(inp);
   
        
