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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d9c0b04-9e90-3d44-a93e-7a54aeb6ca58 | -6.982 | -44.77262 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dfab812-2a9b-3092-979a-a1f20fd9f6d9 | -7.08238 | -44.55404 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02d3a4fc-e16a-3634-b3d3-f0f28905e9b3 | -6.16171 | -45.11641 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 158d8cde-d399-37e9-ade9-3638b95b02a3 | -5.53458 | -42.6597 | 2025-09-16 04:27:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 45.3 |
| be645a84-05ee-333d-9c40-e481f413e9d2 | -5.66369 | -45.06076 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac94b5e9-0ce1-3dfa-b11b-2930fb9a84a0 | -5.3471 | -44.81221 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba089f38-5e1b-37fe-8077-869fe120d5ef | -5.89676 | -45.75434 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf338ba7-9171-31b3-9e11-76dec6091031 | -5.09504 | -43.82881 | 2025-09-16 04:27:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d985147-396a-3bdd-9bc1-2800ba244402 | -5.53878 | -46.41282 | 2025-09-16 04:27:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d916c3a6-5b9d-3e7c-86ad-d3a9d768a37d | -5.89229 | -45.73938 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93c2feb3-9c20-3916-99e2-e0a0bb401e2f | -4.061 | -46.9417 | 2025-09-16 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 052f43a2-b347-3450-9f35-45fcf6a37743 | -4.81077 | -47.34253 | 2025-09-16 04:27:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 527ce0cd-dd27-3755-9e8c-07dbe094b69a | -5.93607 | -45.7139 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1cd46e2-8d7e-3136-adf1-499f3cfdfca1 | -3.81975 | -44.11086 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad07883d-191b-3b8b-be54-73d843093a55 | -5.67542 | -45.05173 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d23b5ed7-cbcc-324d-a463-b15715452c94 | -5.38893 | -42.61843 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 97c1e53a-221a-3cc5-9560-6c3a749fd658 | -6.22262 | -43.90014 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e033cc8-8a97-3a32-896c-1f8934e4e5ab | -6.46159 | -46.01037 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6871e4ab-7b08-3b2e-9469-8381199724cc | -4.16194 | -46.79406 | 2025-09-16 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dece721-2c5d-3665-aa7c-0ee1fd6f6ff5 | -6.43797 | -43.31166 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e3b6942-59e4-316a-a8d1-34f9a54dda3f | -6.34177 | -43.15807 | 2025-09-16 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b518ef07-558d-33e1-8910-f0f748a89907 | -3.65557 | -54.06255 | 2025-09-16 04:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| febc06a0-4405-30a5-b697-5b88ad88c0d7 | -7.27442 | -46.60555 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74e5beff-0088-3c27-94e7-df417e4a5b51 | -3.80975 | -41.57838 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4049cbf0-bb68-3d69-abeb-b29a6947299b | -6.62122 | -44.73714 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b019e9fe-0b0a-3f3f-8b3a-054092e90c2c | -5.78353 | -45.93584 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b49f754-5ec2-3a5f-a7a6-4b1632b7c1e5 | -2.44831 | -49.36475 | 2025-09-16 04:27:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b28a0d09-ccb2-36be-97f4-77c511e93da2 | -3.83845 | -44.1026 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5000616c-a126-3737-8948-8cac28e96565 | -7.25022 | -44.47967 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61100647-a114-3b02-9015-137396032a7e | -5.76636 | -43.96585 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9bdb77b-6870-3c57-a913-8fa88942dbfa | -6.3556 | -43.16448 | 2025-09-16 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7f362d1-567d-3de4-8be2-72c5540ed8ec | -6.55435 | -43.99256 | 2025-09-16 04:27:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4925e9db-3b3c-3405-b2cc-4725107ca414 | -7.13543 | -47.98089 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b72578b-f9fe-3f3f-9d2d-32174b4643fc | -6.52793 | -41.82295 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d8daf809-186c-3d12-a4bf-6907f6edf4d8 | -5.97797 | -45.83805 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b0ace50-7ddf-31a9-b6da-c15f2e615cee | -7.42047 | -40.079 | 2025-09-16 04:27:00 | NPP-375D | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 496cc394-1ae9-39e6-a0d3-d5eb767f7d86 | -6.98747 | -44.57726 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| acee6309-d7fb-3d00-b640-8c51b4903be2 | -5.93346 | -44.87294 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c84857a8-ee86-36b0-9560-52a4b747923d | -7.27219 | -46.59806 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fffa46e9-5e17-3d61-95b5-d862e55cf2da | -5.77622 | -45.89563 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 266086c8-2e90-3178-a5c8-a7719f81098f | -5.58862 | -43.80753 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 371e2f3c-f029-3f43-90c2-1deb93adee15 | -5.97742 | -45.84153 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7aa444f-a669-3cf5-9f79-f7c8d542176a | -6.349 | -43.15921 | 2025-09-16 04:27:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d172ba25-17bd-3cf8-9ab3-6e2f0f3f5b32 | -6.50834 | -41.82032 | 2025-09-16 04:27:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c360a46-3b07-383a-933f-d1ba26df00c0 | -3.85043 | -48.97829 | 2025-09-16 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a9e3b38-3f3c-3d6c-a785-4f4c6a471851 | -7.07895 | -44.55348 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 089f9f2a-c842-35b9-b5b4-563c083b1ff0 | -6.13022 | -43.37184 | 2025-09-16 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9781f63e-d72a-3255-b113-120cbcb9232e | -6.91914 | -44.79725 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a2386f1-1d83-3295-9561-4a2c48847dd7 | -5.90936 | -42.74662 | 2025-09-16 04:27:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a317dfda-cb19-3cc9-86b5-218ffe3a49ad | -3.7419 | -49.04997 | 2025-09-16 04:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 971db90e-9de2-327c-b476-617909fa9180 | -3.13891 | -44.42497 | 2025-09-16 04:27:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 786874de-06f1-3d73-8011-530878f04b28 | -6.315 | -44.21414 | 2025-09-16 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71967a8f-2557-3fbb-a0a5-4c5aadade0fd | -5.76579 | -43.96963 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6cdb624-2735-3552-a538-8afa26031ca5 | -1.97607 | -47.98292 | 2025-09-16 04:27:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d0b1081-359e-396b-a08e-9a3ec88faa2d | -2.13349 | -48.00969 | 2025-09-16 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d9a706a-05f3-3a28-8e01-fe96eaaf47c5 | -3.82768 | -44.10465 | 2025-09-16 04:27:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2944e73-8016-350c-8ac1-3b081e8fe890 | -6.82896 | -47.84649 | 2025-09-16 04:27:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c117961a-8f5b-382b-9618-ee44f55c4661 | -5.89343 | -45.75381 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c86a0d0-70a2-3d74-b650-c21593159c20 | -7.27772 | -46.58467 | 2025-09-16 04:27:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 237d8af5-e406-3bc4-8923-bf0081b058a0 | -6.10053 | -46.49788 | 2025-09-16 04:27:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dee5bd89-54af-3f48-bfc3-35abc20f91bf | -6.31296 | -44.56765 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a7c7e43-b875-3110-a984-1922fb4907c2 | -5.8359 | -44.15802 | 2025-09-16 04:27:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 262766b4-7a56-3bb6-8520-4ac75f686678 | -5.36768 | -43.34486 | 2025-09-16 04:27:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8432e2e6-7f75-3480-8da9-3be631f305b1 | -6.63081 | -45.57609 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1d0a0f90-199b-3148-8859-e1e1e892412c | -5.64551 | -45.9534 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 926db45f-d8da-3cbf-940a-579e200b20f1 | -6.14506 | -41.18124 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| acff1e21-1efd-331f-afbd-7fc2aefee473 | -3.81046 | -41.57372 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ba8d1e37-618b-3802-8d9a-13d9a512a072 | -7.51084 | -44.66678 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d70067e7-5264-3de1-8ed5-25a77fc56619 | -7.29757 | -43.93307 | 2025-09-16 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 620e077d-7382-3ce4-bbfa-503be4611b56 | -5.83043 | -45.26771 | 2025-09-16 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac8a01e3-ac43-3c18-ae49-cbfa7ee9039c | -6.44935 | -43.30927 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d26b213-0084-3030-bf07-f9835ad64829 | -5.98686 | -45.84657 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ba7007b-14f7-34d6-9eac-082f6c96ff5f | -2.80299 | -48.62667 | 2025-09-16 04:27:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f54a20c1-9ae4-3fab-a34c-d19a62de8e4a | -7.08011 | -44.54604 | 2025-09-16 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a85a20e2-66c5-3025-8477-92110707c12c | -7.43495 | -45.83749 | 2025-09-16 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 14adfe16-80cc-3207-bf0f-0ba3ae766572 | -6.44186 | -46.11403 | 2025-09-16 04:27:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04149915-8e14-36b4-acfc-72418124c725 | -6.1578 | -45.11941 | 2025-09-16 04:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b0f5c289-1774-3d6e-af9c-a89517f87d7b | -6.94344 | -46.49279 | 2025-09-16 04:27:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f96a43b-13e9-3633-9a0e-4595a9ec19a3 | -7.42166 | -44.86159 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31050bdc-39d3-33e2-811e-063abdbf17a7 | -4.49241 | -50.50322 | 2025-09-16 04:27:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56250028-7895-3e06-9b5f-5001fb4b04ec | -5.76784 | -43.97081 | 2025-09-16 04:27:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19c6267e-532b-3295-8d28-573465f70248 | -5.90063 | -45.75138 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 965d376b-bde8-3643-882e-d7158fc92421 | -6.42789 | -44.34177 | 2025-09-16 04:27:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93efa9ef-08bf-3e59-bbb2-2a009c1efa72 | -7.01212 | -44.91537 | 2025-09-16 04:27:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea93fb9b-5cd8-3d52-bfa1-d3965c07ac6f | -6.22204 | -43.90398 | 2025-09-16 04:27:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 61e96ac6-f96b-30a9-977c-f398ba5427b4 | -3.42195 | -43.1635 | 2025-09-16 04:27:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38ad18f1-45ae-3d19-a4b6-7f02de37c97b | -5.79488 | -44.8702 | 2025-09-16 04:27:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 204d781c-e810-3cbc-a64c-70d54a742188 | -7.13765 | -47.98875 | 2025-09-16 04:27:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0ca5b8d-26dd-3fc0-a838-86ac1ed21c49 | -6.18287 | -41.20491 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3a737194-2859-3d80-a902-b8ef91950d73 | -4.86111 | -42.54271 | 2025-09-16 04:27:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e44215b1-10c3-3372-891a-e285f1acda81 | -5.78629 | -45.93624 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 130e2b6a-20cb-36be-9e2d-b2aacac9954a | -6.18227 | -41.20799 | 2025-09-16 04:27:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae2dd078-96db-3225-911a-899ca454e653 | -6.42656 | -43.31418 | 2025-09-16 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f41775f-dfb4-3c20-b57b-87079426450b | -5.79003 | -45.87291 | 2025-09-16 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3bb7c022-c663-3180-af1e-d2a537bc2774 | -3.8126 | -41.55971 | 2025-09-16 04:27:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ed243cbc-5c99-3eb4-b488-e3a11ff2c914 | -6.62221 | -44.73322 | 2025-09-16 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa73d073-0a07-39af-b85c-5c7ffa65c24f | -6.25731 | -40.62761 | 2025-09-16 04:27:00 | NPP-375D | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 84b7472e-f4b2-3582-9a38-9ed40286e2c4 | -7.43019 | -44.87415 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f34c9717-1678-320c-a2b5-ab62f0a388c1 | -3.64997 | -54.06465 | 2025-09-16 04:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ad3ad7-0d7a-3a8d-9829-5bd5f46b83ec | -7.5217 | -44.66466 | 2025-09-16 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README35.md)
