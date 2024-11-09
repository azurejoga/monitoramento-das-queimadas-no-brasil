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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09cd96a5-5ad1-37ca-9f9d-1f8215a8df31 | -5.19914 | -47.45841 | 2024-11-09 05:33:00 | AQUA_M-M | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| af2c7275-933e-3404-90fd-2e705e25d4b9 | -2.21098 | -50.33832 | 2024-11-09 05:33:00 | AQUA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2d028d52-fc38-3248-8b7d-0e8aa540e250 | -3.15278 | -54.47414 | 2024-11-09 05:33:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 30671089-9c87-3566-ba99-c3e5abae023b | -3.64549 | -50.1821 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 91f80e7e-dde8-3b0d-ba46-7c66ea3fdea0 | -2.98219 | -50.29599 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9e3aee2b-4acc-3102-960c-77e5507d6257 | -3.58031 | -51.20536 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3766ec4b-fc33-3897-bfe7-13d35aefba12 | -3.98951 | -46.40811 | 2024-11-09 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ab4b9e83-f9b3-3760-bc0b-d493c7f3b813 | -4.2071 | -48.54873 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 34918f3d-85e0-3dfc-b73b-1fca60b4fa8c | -4.80772 | -44.77533 | 2024-11-09 05:33:00 | AQUA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 58f1879d-e856-3753-a447-bce8f32d06f0 | -3.73216 | -54.21212 | 2024-11-09 05:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| ad688757-38fc-3562-8f61-56c0d1026daa | -8.85546 | -47.67679 | 2024-11-09 05:33:00 | AQUA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 9e2a9552-aeea-3c1c-892b-aaed35951729 | -4.81912 | -49.01523 | 2024-11-09 05:33:00 | AQUA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 35149eba-e3d1-3780-9287-f2dd4df1037c | -3.24529 | -50.44413 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0dc3a14d-1f18-357d-9cb5-c49d7d1dac5e | -3.96777 | -48.17179 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 569fa84e-2fa6-3dc8-9887-90915b8efa1b | -2.62303 | -46.16024 | 2024-11-09 05:33:00 | AQUA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5e4060eb-feed-3838-a814-baeb65d2e13a | -3.72938 | -54.23011 | 2024-11-09 05:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f07b111c-9b0d-356e-8136-c80bc311d9d7 | -4.38861 | -48.5697 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 20fbe9bb-77b1-3f20-aefe-466d14dca917 | -3.17306 | -51.30229 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 81bb376a-3a0c-3444-8106-e8160f8a5ec7 | -2.41046 | -48.39598 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b4afe27a-0961-3fe7-816c-8558b8d980ca | -3.32746 | -49.90758 | 2024-11-09 05:33:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d3c0449b-ad3a-3302-8295-8fea09be7c6b | -3.35189 | -50.35551 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 42465e91-b3fe-3198-b42e-9bf574f09d19 | -4.62572 | -46.53291 | 2024-11-09 05:33:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78bd07ab-48c2-3cdb-8b69-748a3d571c86 | -2.92312 | -51.66804 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 37e297c3-2c6a-33ff-b080-7d6d4279890f | -4.80154 | -44.78069 | 2024-11-09 05:33:00 | AQUA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a1afc0da-63db-3e76-b405-f9aa528e4f7c | -3.11104 | -45.3474 | 2024-11-09 05:33:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6bf2a96e-7451-3c00-8909-4eed7d29d9cf | -3.142 | -52.96536 | 2024-11-09 05:33:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 77af188e-85d9-331a-b97f-fc04f9661cd6 | -2.73217 | -51.71106 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 23c91eab-ac72-3575-80f7-46b837e0c4ff | -3.31072 | -50.07848 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8d273632-22f1-336d-9cf0-dbe4c5c7dc6b | -2.37393 | -48.57945 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0c1fd9c9-e745-34a2-a5bf-c0cbdd6b84b7 | -2.31535 | -50.67757 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba79515f-3aa8-3c07-8345-ddf914157352 | -3.95138 | -48.16037 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| c43a9ed8-b13c-37a6-a415-e7e407a5bc81 | -2.84437 | -49.44104 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 92f84d19-31d6-3991-9577-c311ccda9c28 | -3.58198 | -51.19466 | 2024-11-09 05:33:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 5cae581d-ff11-3d9f-ba3a-88a5194de380 | -2.64055 | -46.79514 | 2024-11-09 05:33:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 890191fb-7cfd-32e1-9151-4b1d863e9737 | -2.25268 | -53.65669 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 5e5331a7-fcc6-3e26-bbf0-93f625348efe | -4.20634 | -45.8506 | 2024-11-09 05:33:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 96ec44ce-3de0-3a71-8f5e-ce91179280de | -2.57586 | -49.13669 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 40feee1f-e195-39a6-8135-53d62f69842a | -3.19244 | -50.43985 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 93dab3aa-8e03-3841-98af-7ff523d5854d | -2.6072 | -48.19486 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 403f5ae7-ea7a-3e74-8f9c-ebe500b47434 | -2.79723 | -48.27977 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 87c07af4-afe2-316a-bf01-079633485b82 | -4.10198 | -48.50973 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| b17014b0-10b6-3c33-b05b-acb58db19ade | -7.45499 | -43.57111 | 2024-11-09 05:33:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 052978c2-92e8-3d78-871f-4e3ac82ad68f | -3.58676 | -50.27428 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 38eacaad-ceea-3c8e-b55a-d4261fc714e2 | -3.9655 | -48.12633 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| c2877555-8e8b-38b0-b7c6-333dac2065b9 | -4.09314 | -48.50844 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f85fa4dd-3871-385f-9333-56359677a3d9 | -2.1262 | -48.56126 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 51f2267f-ee3c-3d65-a715-bc09a4de5e28 | -3.96909 | -48.16296 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bf037e5b-d092-3e69-be26-340e475d4439 | -3.65279 | -50.13462 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a8e9db79-4114-396a-af09-f834ab7ca337 | -3.97531 | -48.1819 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 208.2 |
| 74b03516-e0b9-3f69-899b-3f3f1225d26b | -3.98803 | -46.41809 | 2024-11-09 05:33:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 484ae08e-1cf3-3ed5-b66b-3d40685b7e08 | -3.58981 | -47.35817 | 2024-11-09 05:33:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 72bc48e1-34cb-36f8-9281-01d6603b825e | -3.66721 | -50.22425 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ddceb0bf-c392-3c01-8388-0aaa10fc7bae | -3.29606 | -46.40682 | 2024-11-09 05:33:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7240cc07-b392-3856-bfb3-b1fb27019314 | -7.6351 | -43.54214 | 2024-11-09 05:33:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 28f651d9-e98f-3e1f-a012-f119f1b6a607 | -3.60016 | -47.35037 | 2024-11-09 05:33:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| d2630957-3970-3424-ac25-a2630d452b3d | -2.92089 | -49.35945 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 00d72d4f-304d-33b4-9b6c-c78947bee32a | -4.05864 | -46.93581 | 2024-11-09 05:33:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4e488587-46c4-3d5f-b79e-1fc6655bdd80 | -2.99554 | -49.23788 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 81b5ee4d-749f-3da7-aeac-5f1dd26033d1 | -5.13982 | -48.24148 | 2024-11-09 05:33:00 | AQUA_M-M | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2f549e1d-02a4-3e28-8993-b91907b360d4 | -3.40464 | -50.01106 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0551e95d-b01b-3b02-a4a6-c133f77d3cf2 | -4.06731 | -48.30911 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| abe0a6c8-f66a-3daa-9f84-f96e0ed18f1e | -2.86105 | -50.31568 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| efa04aca-2072-3015-b9e1-a8a79a5dd6ec | -2.13796 | -48.7403 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 41c66850-c037-375c-a3fb-90df1c31db63 | -2.58613 | -49.12901 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c36e887d-9b5c-31bc-8fef-ed91b2fc4809 | -4.09606 | -48.85059 | 2024-11-09 05:33:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 4abd2024-bcb8-38e9-9b01-557f26c00923 | -3.69562 | -54.61386 | 2024-11-09 05:33:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b65b3037-67a2-3c78-a01f-720ab9ba91e7 | -3.59117 | -47.3491 | 2024-11-09 05:33:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 102.4 |
| 291a9c60-b59c-3c8d-961b-c5aa166aac7e | -3.61549 | -48.92005 | 2024-11-09 05:33:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4b10e351-834e-37d1-9f35-eb0dcd17be39 | -3.59258 | -50.23585 | 2024-11-09 05:33:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3232d4a7-4910-312a-be98-c3f4f66c6de9 | -2.23909 | -48.36759 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a916924d-d8fb-3be4-a424-a8a6e3c368ca | -2.31693 | -50.66721 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d42d1186-707f-3b8d-971e-c2a67935d5a4 | -4.63306 | -48.72343 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d32c9c9e-91aa-3210-ac06-d1578bd01545 | -2.4925 | -47.22699 | 2024-11-09 05:33:00 | AQUA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db3d3b8d-bbbd-3937-ad5d-332c7555c16c | -3.1252 | -50.14577 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 47131224-41c0-3aae-9543-a2975d2efc24 | -4.12097 | -48.50352 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| f3508222-54a7-33be-a455-d95b4ff50240 | -3.11745 | -50.13485 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2803b3c0-f2a4-3a28-9896-d20afbb208bb | -3.97399 | -48.19074 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 82c0b3ea-7ef4-3a0f-b6eb-998b03caa8aa | -4.3873 | -48.5785 | 2024-11-09 05:33:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3b41db77-db1e-38e1-a929-37decbfc4b45 | -2.89035 | -51.74735 | 2024-11-09 05:33:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7541cc0e-1c3d-3124-b303-62f706f8820f | -3.59253 | -47.33997 | 2024-11-09 05:33:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 53993fb1-b4eb-374c-84df-dff4ca9ba82e | -3.03788 | -50.30418 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 3e47ade8-50a0-33d6-a8f9-920ca4cd6af4 | -3.03051 | -50.35305 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cf1b667b-f70a-3645-a653-ab8c13cd7675 | -2.29532 | -48.54436 | 2024-11-09 05:33:00 | AQUA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6421800d-0b84-3a58-acd3-51fdc1f46e39 | -3.95892 | -48.17049 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| c01c6f03-e015-3210-a777-a5f34322a7b6 | -4.05846 | -48.30783 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 821af4e0-09eb-39d1-a130-f40c228ef2f3 | -3.08419 | -49.56327 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ffda556c-054a-36f4-b145-adbf2ff3fb25 | -4.07483 | -48.31922 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 562cacd2-5287-35e0-9069-02b8660325f7 | -3.34262 | -50.35414 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 16c57ebe-ae4c-30ce-b22a-909bff21e5fe | -2.68042 | -48.49942 | 2024-11-09 05:33:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0259a1a9-c367-33de-9710-91369b3a7eb8 | -3.76126 | -51.75451 | 2024-11-09 05:33:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9d179761-d633-35b0-84ce-f49ea27ad040 | -2.6518 | -48.63018 | 2024-11-09 05:33:00 | AQUA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 81812cd2-cc09-3622-8155-74cf86034a99 | -3.96514 | -48.18945 | 2024-11-09 05:33:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b25db385-58c6-337c-a979-43889bc51030 | -2.46395 | -53.68879 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| e69b7b73-4169-303a-828e-cb5a1f686561 | -3.09203 | -50.23942 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 475bffa1-69c5-3dde-9975-0b81fdacd151 | -2.23477 | -53.77445 | 2024-11-09 05:33:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0e0bef16-4dbe-3317-ba2d-d534ddbd2fa8 | -2.67504 | -51.81207 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 497f9fa5-4ba3-325a-8287-c323a46e52d0 | -2.57318 | -48.18094 | 2024-11-09 05:33:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 315e9c74-1899-3388-8373-260fa165dedb | -3.04765 | -50.36561 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9a50bdf4-75fa-39f1-be05-6aabe32caeea | -2.86836 | -49.22266 | 2024-11-09 05:33:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 99a5d02b-d92b-3557-ac5c-08bfac3012c9 | -3.08132 | -50.55959 | 2024-11-09 05:33:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |


[Clique aqui para ver as próximas entradas](README117.md)
