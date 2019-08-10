# phpsap

still learning how to upload python modules to PYPI so for now you will have to 
manually download and place the phpsap.py into your project directory :o

PHP SAP - SMS, AIRTIME, PAYMENTS

PHP SAP is an API gateway class that enables php developers to easily integrate SMS,Airtime and Mobile payments using MPESA into their dynamic web applications.It is very easy to get started by creating an account and grabbing an API Key.Upon creation of an account a SAP wallet is automatically created for you,you will have to top it up with cash to start using our API to send SMS and distribute airtime.For mobile payments using MPESA a payments wallet is also automatically created for you, this is where all payments made to your application will be collected and managed. Simply hit this link to get started https://renthero.co.ke/phpsap

    Join our Developers Forum here https://php-sap.mn.co

    New Feature- You can now schedule or automate task execution on any of your web servers using SAP.All you need to do is to define when to call a url with what queries and how many times, and our API will do exactly that. This is built on top of A TRIGER.

Getting started

    DOWNLOAD our fantastic gateway class and place it in your project directoy

Sending SMS

    You can send SMSs from your application by making a HTTP POST request to the SMS API. For each request sent from your application, we respond with a notification back indicating whether the SMS transaction was successful or failed.

require_once 'PHPSAPGateway.php';
$gateway= new PhpSapGateway;

//Set your authentication credentials below(Required)
$username="username";
$apiKey="api key";

//Set SMS Receiver(in international format for this case +254) and Message below(Required)
$Receiver="+254708344101";
$Message="i love nerds";

//Pass authentication credentials and your SMS data into an array
$SMSData = array(
	'Receiver' => $Receiver,
	'Message' => $Message,
	'username'=>$username,
	'apiKey'=>$apiKey
);

	//Convert the array to JSON String.
$SMSDataEncoded = json_encode($SMSData);

	//Thats it,from here we will take care of the rest.
try {
	$result=$gateway->ProcessSMS($SMSDataEncoded);
	print_r($result);
} catch (Exception $e) {
	echo $e->getMessage();
}

Sending Airtime

    Your application sends Airtime by making a HTTP POST request to the airtime API. For each request sent from your application, we respond with a notification back indicating whether the airtime transaction was successful or failed.

require_once 'PHPSAPGateway.php';
$gateway= new PhpSapGateway;

//Set your authentication credentials below(Required)
$username="username";
$apiKey="api key";

//Set airtime Receiver and Amount below(Required)
$Receiver="+254708344101";
$Amount="10";

//Pass authentication credentials and your airtime data into an array
$AirtimeData = array(
	'Receiver' => $Receiver,
	'Amount' => $Amount,
	'username'=>$username,
	'apiKey'=>$apiKey
);

	//Convert the array into JSON string.
$AirtimeDataEncoded = json_encode($AirtimeData);

	//Thats it,from here we will take care of the rest.
try {
	$result=$gateway->ProcessAirtime($AirtimeDataEncoded);
	print_r($result);
} catch (Exception $e) {
	echo $e->getMessage();
}

Checking Your SAP Wallet Balance

    You can send a request to out APIs to get your SAP Wallet Balance. Make sure you provide the required parameters.

require_once 'PHPSAPGateway.php';
$gateway= new PhpSapGateway;

//Set your authentication credentials below(Required)
$username="username";
$apiKey="api key";

//Pass authentication into an array
$SAPWalletBalanceData = array(
	'username'=>$username,
	'apiKey'=>$apiKey
);

//Convert the array to JSON String.
$SAPWalletBalanceDataEncoded = json_encode($SAPWalletBalanceData);

//Thats it,from here we will take care of the rest.
try {
	$result=$gateway->ProcessSAPWalletBalance($SAPWalletBalanceDataEncoded);
	print_r($result);
} catch (Exception $e) {
	echo $e->getMessage();
}
