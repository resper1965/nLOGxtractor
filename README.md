# nLOGxtractor

## Descrição
O nLOGxtractor é uma ferramenta desenvolvida por forense.io para ajudar profissionais de segurança e investigadores a filtrar e analisar logs de eventos do Windows exportados em formato Excel. Com uma interface gráfica intuitiva, permite aos usuários selecionar facilmente os tipos de eventos que desejam investigar.

## Funcionalidades
- **Seleção de Arquivo**: Escolha facilmente o arquivo Excel contendo os logs de eventos.
- **Filtro por EventID**: Filtra os logs baseado nos IDs de evento especificados.
- **Exportação de Dados**: Exporta os logs filtrados para um novo arquivo Excel.

## Como Usar
1. Inicie o aplicativo e selecione o arquivo Excel com os logs de eventos do Windows.
2. Selecione os EventIDs que deseja filtrar.
3. Clique em "Executar" para filtrar e depois salve o arquivo filtrado.

## Requisitos
- Python 3.x
- pandas
- tkinter

## Instalação
Clone este repositório e instale as dependências necessárias:
git clone https://github.com/seu_usuario/nLOGxtractor.git
cd nLOGxtractor
pip install pandas

csharp
Copiar código

## Contribuições
Contribuições são bem-vindas! Para contribuir, por favor, abra um pull request com suas mudanças ou discuta as mudanças que deseja fazer através de issues.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
Sugestão para Notas de Release
Quando você for lançar uma nova versão, as notas de release podem seguir este formato, focando nas funcionalidades e melhorias específicas relacionadas ao tratamento de logs de eventos do Windows:

Release v1.0.0 - [Data de Lançamento]

Novas Funcionalidades:

Interface gráfica para seleção fácil de arquivos Excel com logs de eventos do Windows.
Filtragem de logs baseada em EventIDs selecionados pelo usuário.
Melhorias:

Otimizações no carregamento e processamento de arquivos Excel grandes.
Melhoria na usabilidade com a adição de feedback visual durante o processamento dos dados.
Correções de Bugs:

Fixado um bug que causava a falha do aplicativo ao carregar arquivos corrompidos.
Notas:

Testes realizados em diferentes ambientes Windows para garantir a compatibilidade.
Essas informações devem ajudar a estabelecer uma boa base de documentação para seu projeto e comunicar efetivamente suas funcionalidades e melhorias para os usuários. Se precisar de mais ajuda com qualquer etapa, sinta-se à vontade para perguntar!
