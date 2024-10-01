# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33f95295-5e40-3a15-a118-f48ba1197ecc | -13.64754 | -50.34202 | 2024-10-01 00:48:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c88c32cd-a71b-3ea2-aa87-0d56b963d4d9 | -13.64193 | -50.3484 | 2024-10-01 00:48:00 | TERRA_M-M | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c3c82a11-baaf-33c8-b5f1-f9748fa53565 | -12.27476 | -51.54107 | 2024-10-01 00:48:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 4489a7ea-08ce-30b8-ae25-d447f8b680f3 | -13.22903 | -51.23807 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| d93cf307-e4e3-3e8d-919c-3a99182376c1 | -12.98363 | -51.36678 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 569c8b7f-9f58-33cc-ba86-79b257d1fa68 | -12.98127 | -51.34662 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 960d7b91-d3cf-31d3-90f8-2a6dbc96305d | -12.97657 | -51.30652 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| db89825b-e4f5-324f-b4e2-42cb18f7bc17 | -12.97423 | -51.28659 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 186.5 |
| bd08f0ec-3c75-31a3-a20e-2926ea21d932 | -12.9719 | -51.26672 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.7 |
| ea9892cf-58bf-3d07-a3a9-6f67c5fdc643 | -12.97078 | -51.36835 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 6a05d1db-6a5a-3f35-8189-49940d87933b | -12.96957 | -51.24692 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 623f05e7-97c4-34ea-95fe-01764292cbf7 | -12.96843 | -51.34818 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 185.2 |
| 526ffb4f-4aa4-3458-998f-8cce36cdeb23 | -12.9661 | -51.32809 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 29.0 |
| d246078d-fab5-3d98-abd8-804a95d36584 | -12.96377 | -51.30808 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 3e92589f-30af-36e6-a8f6-6b48641d1cca | -12.95914 | -51.26828 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| dab8c149-8d3a-3b1b-ac30-d6232365c6cc | -12.95792 | -51.3699 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 534dad83-8cfe-37f5-8983-7aee1aa1f537 | -12.95684 | -51.24849 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 653dcebb-3644-34e6-a962-bd4d24bbfcbd | -12.9556 | -51.34975 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ca18414e-e52c-3a93-b7be-8e11b5e3b4c2 | -12.95454 | -51.22876 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 2e5045e7-0ba0-357a-97fc-c1aab626e687 | -12.95098 | -51.30964 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| b37b8c1b-3a7f-336f-94f4-b50666a762f5 | -12.91296 | -51.32073 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 5b3d91bd-f426-333a-8c92-96322db468d5 | -12.9126 | -51.31434 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 8c8f59c6-8771-332b-80a3-37ef965291d6 | -12.91057 | -51.3008 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 920d3a7f-39ca-3a52-92a3-9ee6ea66bea6 | -12.91037 | -51.2944 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| ad15ce4c-6faa-37ee-9a5f-f7187bc93d90 | -12.88737 | -51.32384 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5ffc497f-3bbc-33e9-83e6-dfa0ffb306a8 | -12.88503 | -51.30391 | 2024-10-01 00:48:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 7267ab1d-e541-319e-b610-f1cda5f72b90 | -16.63093 | -52.58892 | 2024-10-01 00:48:00 | TERRA_M-M | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 19.4 |
| b97393fa-727d-3106-8220-dc8030a72a12 | -12.60544 | -53.50912 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8db0cf83-a000-3ffe-bf5b-5b6f5c2956c0 | -12.60411 | -53.48624 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| c3baa5ce-2b76-349b-8e4d-3c9d0b3fc710 | -12.5098 | -53.18048 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 1f6dfd1c-5798-33e4-b444-cf8747bae5b5 | -12.5068 | -53.15293 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 8f8bac50-c811-3c73-822c-d78adf596378 | -12.50632 | -53.15843 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 7a71eabb-10c7-3d48-be50-02f735ac5315 | -12.49506 | -53.18232 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 54423c02-99ea-3df2-9201-26a8f12976aa | -12.49479 | -53.18784 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 5c5c8416-96a2-3a8e-b91b-7869231430fd | -12.49208 | -53.15464 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 27a455f6-4043-3913-9219-2b5fb98047de | -12.4916 | -53.16009 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 08b807cf-bbb6-3308-b41f-e158bbedb8f1 | -12.46528 | -53.19123 | 2024-10-01 00:48:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| bc4d7326-6f64-3144-bf02-853dff22a393 | -12.31074 | -54.10381 | 2024-10-01 00:48:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| b2afaf82-91ce-3e7d-a710-d1eff05d2c39 | -12.30794 | -54.12997 | 2024-10-01 00:48:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| c776b907-6cab-341b-ab50-42502c50b37f | -9.87334 | -36.26962 | 2024-10-01 00:48:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 45.8 |
| d8ea86e7-9e8f-3429-b227-5e2ecfe7748e | -9.25779 | -40.81812 | 2024-10-01 00:48:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f451418e-7e9a-3527-9726-a3a8c6e97edf | -9.5774 | -40.3469 | 2024-10-01 00:48:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 48308710-1fd9-36de-b513-a394701801ac | -9.57626 | -40.35686 | 2024-10-01 00:48:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 2d8d6576-fdef-3367-943f-977a635038ce | -9.5737 | -40.34093 | 2024-10-01 00:48:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| b4428b69-4bff-3ee9-a8ef-7bbdf8cc466d | -16.96983 | -42.2464 | 2024-10-01 00:48:00 | TERRA_M-M | FRANCISCO BADARÓ | MINAS GERAIS | Brasil | 3126505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 76577e87-0689-37b0-9390-f525c79ef5a0 | -15.79907 | -43.32632 | 2024-10-01 00:48:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 21144658-60c3-3902-9750-e3047742d7a2 | -15.771 | -43.58407 | 2024-10-01 00:48:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fd882632-d75c-3bcf-9a0c-18fb4cfbb773 | -15.4458 | -43.62441 | 2024-10-01 00:48:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b92600d8-5299-3a6b-8ee9-d11828e69ce7 | -11.25318 | -43.38804 | 2024-10-01 00:48:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 25c6be49-bf1a-32fd-bbb7-3513d0d99349 | -11.25174 | -43.37826 | 2024-10-01 00:48:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| aaaf459d-dc84-32ba-ad0e-1d8e727991c9 | -13.45003 | -43.78338 | 2024-10-01 00:48:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| caff9ae6-5e1f-364c-96d2-5ba4b1989b51 | -13.44869 | -43.77411 | 2024-10-01 00:48:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0926f4e2-6dba-33ca-b89e-07c716ed2dca | -17.35577 | -44.917 | 2024-10-01 00:48:00 | TERRA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3c193350-c77f-3f87-ad75-73737d49554b | -13.1686 | -46.34156 | 2024-10-01 00:48:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 25097994-801a-32e6-b0bb-eadd7aa132af | -10.86663 | -44.80362 | 2024-10-01 00:48:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| f652f442-4724-3264-9b52-b56e1aedac97 | -10.86536 | -44.7946 | 2024-10-01 00:48:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 22b24e18-bc9d-3aac-b9a4-746028998a25 | -12.09212 | -45.00201 | 2024-10-01 00:48:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2cba845e-4023-3fed-9714-ca06bb42235d | -12.09087 | -44.99302 | 2024-10-01 00:48:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79562dd7-7087-3597-890c-b4068203e765 | -12.08454 | -45.01231 | 2024-10-01 00:48:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b5df16a-662c-3432-ac44-9e90432e1543 | -12.08328 | -45.00332 | 2024-10-01 00:48:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 7158af6b-9477-35ad-a898-0c57fd3d7cba | -12.06816 | -44.95964 | 2024-10-01 00:48:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 045547a5-f815-35f9-9840-0e766dd7ee29 | -11.92828 | -44.87606 | 2024-10-01 00:48:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4d9cbc51-0066-3e42-a652-359b9a36ce36 | -11.26261 | -45.66121 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 5f06d6a2-199f-3703-b4af-437cd3cd013f | -11.26136 | -45.6522 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| accb79b5-41b2-3873-bd03-cc3b9f5a82c2 | -11.25375 | -45.66253 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f3e9a426-eb3b-3255-95e9-98efe4207a2a | -11.25251 | -45.65351 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d1340791-21c2-364a-a149-7e789483e0a0 | -11.20962 | -45.6047 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 09a12f99-b8a1-39b7-82f0-aa696dc1e171 | -11.20838 | -45.59573 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 626780b9-3765-3662-bbc8-fb7a0aa363d0 | -11.16414 | -45.74569 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e8ae2d81-ac8d-3467-aa17-829a53cc8a7a | -11.14658 | -45.68391 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d380d326-c496-3adb-9693-ae747c303cdf | -11.14517 | -45.73924 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2d8fce88-c66e-3416-a2a8-fd7d072e7d6a | -11.13772 | -45.6852 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| affba527-c4d4-3334-bde4-6bb5f76cec08 | -11.1239 | -45.65049 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 2f34b921-8e57-35cb-b49c-935c1143230a | -11.12266 | -45.6415 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d90b93fd-c38e-3354-9a6b-7916dcf8a8cc | -11.12142 | -45.63251 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| a2fee821-2fb5-36ce-9308-91a5c63dd7c2 | -11.11876 | -45.67876 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4c14bcb7-8ab2-30ec-9b03-2a2fc8db1827 | -11.11114 | -45.68906 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 937d1744-6fba-3c81-9d70-a7a455d43a7d | -11.1099 | -45.68006 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 2cde594f-d39e-3c86-aac9-98cca4e6a7af | -11.10866 | -45.67105 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 70b64217-f7f8-3c95-a7d3-711896ddfa20 | -13.1764 | -46.3305 | 2024-10-01 00:48:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3f49abce-5490-3fb3-aa69-a0303f09c68f | -13.16988 | -46.35117 | 2024-10-01 00:48:00 | TERRA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6eea3af6-5498-3d5c-83dc-a502fd808c07 | -14.18616 | -46.45894 | 2024-10-01 00:48:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fb78de8d-8613-3636-9a89-20a1102c725d | -14.17822 | -46.47019 | 2024-10-01 00:48:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1a3805d4-288e-3a49-8288-d5686c21cdfe | -14.17691 | -46.46022 | 2024-10-01 00:48:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4763d816-9f1c-3eb5-9703-f4a0355cb73e | -14.16766 | -46.46143 | 2024-10-01 00:48:00 | TERRA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9c4d8fe7-1ac9-3ce8-99e6-59d6e8c1d7eb | -14.43731 | -45.71873 | 2024-10-01 00:48:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f83db2b7-944b-3263-9ec8-f18382c63099 | -15.20425 | -46.22734 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 19cf4f10-1e9c-39e9-bfef-7f3e6f30daf5 | -17.58182 | -46.77898 | 2024-10-01 00:48:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6c51b2c9-7392-369f-b75e-5d8dcf908e5a | -17.47899 | -47.00954 | 2024-10-01 00:48:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 65557cb7-f0bc-3703-a1bf-f41a9bfb35a5 | -14.71895 | -48.76225 | 2024-10-01 00:48:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c4cee9c9-3d2e-3a63-88c8-241f22e7cd8f | -10.70656 | -46.17148 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2de5c81e-e744-3c78-ad3c-c3da8fcf6d51 | -10.69764 | -46.17273 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ae96b7e1-5375-3223-9317-8c8c7473b665 | -10.68747 | -46.16489 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6f272039-10a7-363f-bf14-359f3b6d5b3e | -10.67731 | -46.15708 | 2024-10-01 00:48:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| be7b3fa7-6d4f-3ef6-9122-3474e5403c17 | -10.7758 | -46.5409 | 2024-10-01 00:48:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 77177a2b-4fc4-31c3-b5e5-45b3b2894cd9 | -11.44042 | -46.96385 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 29d38c5e-596b-38a0-b399-3d57510aa689 | -11.43911 | -46.95412 | 2024-10-01 00:48:00 | TERRA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| ff404f23-b9a0-3493-8e5e-d3964eb266de | -10.9986 | -46.48761 | 2024-10-01 00:48:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ed39b0e6-8dae-3426-8272-62676c6113e9 | -10.99729 | -46.47807 | 2024-10-01 00:48:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a3ad8312-65b8-3fe9-b644-f9b2a5ebe47e | -10.99339 | -46.51689 | 2024-10-01 00:48:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |


[Clique aqui para ver as próximas entradas](README8.md)
