from jinja2 import Template


# Carrega um template a partir de uma string
template_string = "Eu sou um {{ nome }}!"
template = Template(template_string)

# Renderiza o template com um contexto específico
output = template.render(nome='template')

# Imprime o resultado
print(output)
