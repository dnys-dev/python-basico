# O que é script

são comandos encadeado ( um em baixo do outro ) de não depende de outros para exercutar uma tarefa.

## comentário no Python

usamos o comando # na frente da frases ou caracteres

**São três contexto**

1 - Informar a intenção do seu código.

2 - Comentar um controle de alguma coisa, tem feramenta de teste que permite colocar um comentário na frente do código para mostrar o que deve ser feito naquela linha ( comentario de forma de tag).

3 - `Shebangd` - é um comentário do universo Unix, sempre na primeira linha `#!/usr/bin/env python3`.

## Shebang
Em ambientes Linux é muito importante definir o comentário especial Shebang, nele especificamos qual interpretador será usado para executar o programa

```python
#!/usr/bin/env python3

print("Hello, World!")
```

A primeira linha informa o terminal que aquele programa roda com o Python3 da env em execução, esta forma é possivel omitir o interpretador e executar o script diretamente pelo seu nome.

# primeiro damos parmissão de execução ao script
chmod +x hello.py
Agora podemos executar de 2 formas

# especificando o interpretador na linha de comando
python3 hello.py
# usando o interpretador especificado na linha `#!/usr/bin/env python`
./hello.py
A vantagem da segunda forma é que podemos mudar a extensão de .py para .exe por exemplo, ou podemos até remover a extensão e executar ./hello