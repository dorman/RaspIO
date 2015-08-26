#First build of Rasp.IO v0.0.1

    .~~.   .~~.
  '. \ ' ' / .'
   .~ .~~~..~.
  : .~.'~'.~. :
 ~ (   ) (   ) ~
( : '~'.~.'~' : )
 ~ .~ (   ) ~. ~
  (  : '~' :  ) Rasp.IO is built for Raspberry Pi
   '~ .~~~. ~'
       '~'


 *******                                **   *******  
/**////**                    ******    /**  **/////** 
/**   /**   ******    ******/**///**   /** **     //**
/*******   //////**  **//// /**  /**   /**/**      /**
/**///**    ******* //***** /******    /**/**      /**
/**  //**  **////**  /////**/**///   **/**//**     ** 
/**   //**//******** ****** /**     /**/** //*******  
//     //  //////// //////  //      // //   ///////   

import socket

import portscanner

#Create the socket with the IPv4 address family and connection based stream as TCP 
s = socket(AF_INET, SOCK_STREAM)
port = 9000
s.bind(("127.0.0.1",port))


s.listen(1000) #Rasp.IO by default accepts 1000 client connections
while True:
	c, addr = s.accept() #Accepts clients connection
	print 'Rasp.IO recieved a connection from', addr
	c.send('Dear client, I have recieved your connection to my wonderful server')

 s.message("Welcome to Rasp.IO!")

 
 


