from netmiko import ConnectHandler 



router = {
	"device_type" : "cisco_ios",
	"host" : "10.10.10.1",
	"username" : "v_rono",
	"password" : "2xcvbbvuy",
}

connect = ConnectHandler(**router)

list_config = [
    "int lo0",
    "ip address 10.1.1.1 255.255.255.255",
    "int lo1",
    "ip address 10.1.1.2 255.255.255.255"

]

output = connect.send_config_set(list_config)
print(output)

output = connect.send_command("show ip int brief")
print(f"interface for router {router['host']}")
print(output)