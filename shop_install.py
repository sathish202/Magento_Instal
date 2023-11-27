import subprocess
import os
import mysql.connector
from urllib.parse import urlparse



#Package Download from composer
folder_name = input("Enter the directory name: ")
pck_install = "composer create-project --repository-url=https://repo.magento.com/ magento/project-community-edition "+folder_name

subprocess.run(pck_install, shell=True)
print("Latest shop directory has been installed sucessfully!!!")

#Permission to the files
current_wd= os.getcwd()
print("Current working directory is: ",current_wd)
#new_path = "cd "+folder_name
#print(new_path)
new_path = os.chdir(current_wd + "//" + folder_name)

new_wd = os.getcwd()
print("New Working directory is :",new_wd)

permission_change = os.chmod(new_wd, 0o777)
permission_vendor = os.chmod(new_wd+ "//" "vendor", 0o777)
permission_setup = os.chmod(new_wd+ "//" "setup", 0o777)
permission_app = os.chmod(new_wd+ "//" "app", 0o777)
#file_info = os.stat(new_wd)
#print(file_info)


# Mysql Connection
host_name = "localhost"
user_name = "root"
password = "novalnet"
try:
    connection = mysql.connector.connect(host=host_name, user=user_name, passwd=password)
    if connection.is_connected():
        print("Your are now connected to MySql server")

    cursor = connection.cursor()
    database_name = input("Enter the database name: ")

    create_db_query = f"CREATE DATABASE {database_name}"

    cursor.execute(create_db_query)
    print(f"Database '{database_name}' created sucessfully")

    cursor.close()
    connection.close()
    print("MySql server conncetion is close")

except mysql.connector.Error as error:
    print('Error', error)
'''
#Get Domain 
def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain
'''


#Installation
base_url = input("Enter the base url for the shop. For ex. https://www.magento2.de/pub: ")
db_host = host_name
db_name = database_name
db_user = user_name
db_password = password
admin_firstname = "admin"
admin_lastname = "admin"
admin_mail = "testadmin@novalnetsolutions.com"
admin_username = "shopadmin"
admin_password = "novalnet@123"
lang = input("Select the shop language from en_US & de_DE :")
shop_currency = input("Enter the currency to use in the shop. Ex. EUR, USD: ")
time_zone = "Europe/London"
use_rewrites = "1"
ops_host = "http://192.168.2.6"
ops_port = "9200"
ops_userName = "novalnet"
ops_password = "novalnet"



def installation_magento():
    try:
        subprocess.run(['php', 'bin/magento', 'setup:install',
            '--base-url=' + base_url,
            '--db-host=' +db_host,
            '--db-name=' + db_name,
            '--db-user=' + db_user,
            '--db-password=' +db_password,
            '--admin-firstname=' + admin_firstname,
            '--admin-lastname=' +admin_lastname,
            '--admin-email=' +admin_mail,
            '--admin-user=' +admin_username,
            '--admin-password=' +admin_password,
            '--language='+ lang,
            '--currency='+ shop_currency,
            '--timezone='+ time_zone,
            '--use-rewrites=' + use_rewrites,
            '--opensearch-host=' +ops_host,
            '--opensearch-port='+ops_port,
            '--opensearch-username='+ops_userName,
            '--opensearch-password=' +ops_password], check=True)
    except subprocess.CalledProcessError as e:
        print("Error installing Magento. Command:", e.cmd)
        print("Return code:", e.returncode)
        print("Output:", e.output.decode('utf-8'))
    except Exception as e:
        print("Error installing Magento:", str(e))
installation_magento()

#if __name__ == "__main__":

#Sample data deploy

sampleData_deploy = "php bin/magento sampledata:deploy"
subprocess.run(sampleData_deploy, shell=True, check=True)


deploy_dir = os.chdir(new_wd)
print(deploy_dir)

deploy_upgrade = "php bin/magento setup:upgrade"
deploy_compile = "php bin/magento setup:di:compile"
deploy_content = "php bin/magento setup:static-content:deploy -f"
#print(deploy_commands)

try:
    subprocess.run(deploy_upgrade, shell=True, check=True)
    print(f"Deployment commands {deploy_upgrade} executed sucessfully")
    subprocess.run(deploy_compile, shell=True, check=True)
    print(f"Deployment commands {deploy_compile} executed sucessfully")
    subprocess.run(deploy_content, shell=True, check=True)
    print(f"Deployment commands {deploy_content} executed sucessfully")
except subprocess.CalledProcessError as e:
    print(f"Error during deployment {e}")






current_wd= os.getcwd()
print("The current working directory is: ", current_wd)
#new_path = os.chdir(current_wd + "//" + folder_name, "//")
#new_path = current_wd + "\\" + folder_name + "\\"
#os.chir(new_path)
#print(new_path)
#new_wd = os.getcwd()

#subprocess.run(new_wd, shell=True)


#for i in new_wd:
#permission_change = os.chmod(current_wd + "/", 0o777)


print("The current path", current_wd + "/")
permission_filesFolders = os.chmod(current_wd+ "/", 0o777)
permission_pub = os.chmod(new_wd+ "//" "pub/" , 0o777)
permission_var = os.chmod(new_wd+ "//" "var/" , 0o777)
permission_generated = os.chmod(new_wd+ "//" "generated/", 0o777)
permission_vendor = os.chmod(new_wd+ "//" "vendor/", 0o777)
permission_setup = os.chmod(new_wd+ "//" "setup/", 0o777)
permission_app = os.chmod(new_wd+ "//" "app/", 0o777)

#process = subprocess.Popen(["php bin/magento setup:upgrade"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#process.wait()
#if process.returncode != 0:
    # Handle the error condition here
 #   print("Error: Process returned non-zero exit code")
#dy_upgrade = "php bin/magento setup:upgrade"
#upgrade_process = subprocess.Popen(dy_upgrade.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#stdout, stderr = upgrade_process.communicate()
#if process.returncode != 0:
 #   print(f"Error: {stderr.decode()}")
#else:
 #   print(f"Success: {stdout.decode()}")

print("Magento shop installed sucessfully")
print("Your shop main url: " +base_url)
print("Your shop admin user name: " +admin_username)
print("Your shop admin password: " +admin_password)
print("Enjoy")

