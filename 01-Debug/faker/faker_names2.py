from faker import Faker


faker = Faker(locale='pt_BR')  # existe no locale pt_BR, sendo usado como atributo

Faker.seed(0)  # repare que usamos a classe 'Faker', e não a instância 'faker'

print(faker.name())
print(faker.phone_number())
print(faker.cpf())

