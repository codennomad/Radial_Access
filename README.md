# Radial Menu com Tkinter

![Funcionamento do Menu](https://github.com/seu-usuario/seu-repositorio/raw/main/demo.gif)

Este é um projeto de um menu radial interativo criado com **Tkinter** em Python. O menu radial é ideal para acessar rapidamente comandos ou programas pré-configurados de forma visual e intuitiva. 

## 🌟 Recursos

- **Interface Intuitiva**: Menu radial com design moderno e responsivo.
- **Configuração Personalizável**: Os itens do menu são definidos via um arquivo JSON.
- **Execução de Comandos**: Suporte a execução de processos e envio de teclas.
- **Atalho Prático**: Ativado com clique do botão do meio do mouse.
- **Hover Dinâmico**: Realce visual ao passar o mouse sobre os itens.

---

## 🖥️ Pré-requisitos

Certifique-se de ter instalado em sua máquina:

- Python 3.7 ou superior
- Bibliotecas utilizadas:
  - `tkinter` (já incluso na instalação padrão do Python)
  - `keyboard`
  - `mouse`
  - `json`
  - `subprocess`

Para instalar as dependências externas, você pode usar:
```bash
pip install keyboard mouse
```

---

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Configure o arquivo `radial_config.json` com as opções do menu radial. Exemplo de configuração:
   ```json
   {
       "opcoes": [
           { "nome": "Navegador", "tipo": "processo", "comando": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" },
           { "nome": "Bloco de Notas", "tipo": "processo", "comando": "notepad.exe" },
           { "nome": "Fechar", "tipo": "tecla", "comando": "alt+f4" }
       ]
   }
   ```

3. Execute o programa:
   ```bash
   python radial.py
   ```

4. Clique com o botão do meio do mouse para abrir o menu radial.

---

## 🎯 Funcionalidades

- **Execução de Programas:** Abra aplicativos ou arquivos específicos configurados no JSON.
- **Envio de Atalhos:** Envie comandos de teclado automaticamente.
- **Design Personalizável:** Altere as cores, tamanhos e itens diretamente no código.

---

## 📂 Estrutura do Projeto

```
.
├── radial.py                # Código principal do projeto
├── radial_config.json       # Configuração personalizada do menu
└── demo.gif                 # Demonstração do funcionamento
```

---

## 🛠️ Melhorias Futuras

- Adicionar suporte para animações mais suaves.
- Tornar o menu ainda mais personalizável através de um editor gráfico.
- Adicionar suporte a ícones gráficos no menu.

---

## 🎥 Demonstração

Veja o menu radial em ação:

![Demo](https://github.com/seu-usuario/seu-repositorio/raw/main/demo.gif)

---

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Siga os passos abaixo:

1. Faça um fork do projeto
2. Crie uma branch para suas modificações: `git checkout -b minha-feature`
3. Faça commit das alterações: `git commit -m 'Adiciona minha feature'`
4. Envie para o repositório remoto: `git push origin minha-feature`
5. Abra um Pull Request

---

## 📝 Licença

Este projeto está licenciado sob a licença MIT. Sinta-se à vontade para usar e modificar como desejar.

---

## 📧 Contato

Para dúvidas ou sugestões, entre em contato:

- Email: (shadowindev@gmail.com)
- GitHub: (https://github.com/codennomad)

---

Feito com 💖 por [Seu Nome].
