
system_password = "1203"
system_user = "edison"
system_email = "edison.marin25@gmail.com"


username = input("Ingrese su usuario: ")
password_user = input("Ingrese su contraseña: ")
email_user = input("Ingrese su correo electrónico: ")


# CAPTCHA
num1 = 7
num2 = 5
captcha_result = num1 + num2
captcha_input = int(input(f"Resuelva la suma: {num1} + {num2} = "))


if (
    username == system_user
    and password_user == system_password
    and email_user == system_email
    and captcha_input == captcha_result
):
    print("Puede ingresar al martillo")
else:
    print("No cumple los requisitos de autenticación o el resultado de la suma es incorrecto")