1. HelloService.java
import javax.jws.WebService;
@WebService
public class HelloService {
public String sayHello(String name) {
return &quot;Hello &quot; + name + &quot;, welcome to SOAP Web Service!&quot;;
}
}



2. HelloPublisher.java
import javax.xml.ws.Endpoint;
public class HelloPublisher {
public static void main(String[] args) {
String url = &quot;http://localhost:8080/hello&quot;;
Endpoint.publish(url, new HelloService());
System.out.println(&quot;SOAP Service running at: &quot; + url + &quot;?wsdl&quot;);
}
}



<soapenv:Envelope
    xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:ser="http://soapdemo/">
    
    <soapenv:Header/>
    
    <soapenv:Body>
        <ser:sayHello>
            <name>Aruna</name>
        </ser:sayHello>
    </soapenv:Body>
    
</soapenv:Envelope>
