

<apex:page controller="CustomLoginController">
    <apex:form >
        <apex:pageMessages />
        <apex:pageBlock title="Login Page">
            <apex:pageBlockSection columns="1">
                <apex:inputText value="{!username}" label="Username"/>
                <apex:inputSecret value="{!password}" label="Password"/>
                <apex:commandButton value="Login" action="{!login}"/>
            </apex:pageBlockSection>
        </apex:pageBlock>
    </apex:form>
</apex:page>






##controller : 

public class CustomLoginController {
    public String username { get; set; }
    public String password { get; set; }

    public PageReference login() {
        // Simulated check (you can't validate real passwords in Apex)
        User u = [SELECT Id, Username FROM User WHERE Username = :username LIMIT 1];

        if (u != null && password == 'test123') { // Dummy check
            ApexPages.addMessage(new ApexPages.Message(ApexPages.Severity.CONFIRM, 'Login Successful!'));
            return null; // Can return a redirect page
        } else {
            ApexPages.addMessage(new ApexPages.Message(ApexPages.Severity.ERROR, 'Invalid Username or Password'));
            return null;
        }
    }
}





