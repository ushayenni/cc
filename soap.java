1. HelloService.java
import javax.jws.WebService;

@WebService
public class HelloService {

    public String sayHello(String name) {
        return "Hello " + name + ", welcome to SOAP Web Service!";
    }
}


2. HelloPublisher.java
import javax.xml.ws.Endpoint;

public class HelloPublisher {

    public static void main(String[] args) {
        String url = "http://localhost:8080/hello";
        Endpoint.publish(url, new HelloService());

        System.out.println("SOAP Service running at: " + url + "?wsdl");
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
