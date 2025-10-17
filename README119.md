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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c81d215-a704-3805-9bef-f8b77f5a0737 | -7.11067 | -44.74434 | 2025-10-17 12:36:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| de7a5235-39a2-3599-a904-403c5477bcaf | -8.56822 | -45.44543 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 6db956e1-e01a-32a9-88cd-d7ab6f2789b6 | -5.26321 | -43.25994 | 2025-10-17 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 9822cf52-57cf-3077-8310-816d4daaeb52 | -4.01592 | -44.18025 | 2025-10-17 12:36:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 73260036-8b1d-3a70-a878-c9446f53f62a | -7.48033 | -47.02887 | 2025-10-17 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| d9faf88d-bb89-3a53-a3cf-719396005317 | -9.01922 | -46.62687 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 4edfb608-d125-37ca-b358-6927690edc0d | -7.37079 | -44.21986 | 2025-10-17 12:36:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e5eae1eb-ce2d-36dc-bdb6-bddc01d524eb | -8.31132 | -43.44954 | 2025-10-17 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.1 |
| af9cff29-1e57-3434-bbc9-76e6059c4534 | -3.51118 | -52.49023 | 2025-10-17 12:36:00 | TERRA_M-T | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 6cd1447a-9324-3cc2-84f4-859b3bfe0587 | -2.9459 | -47.30463 | 2025-10-17 12:36:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3c4b5b2f-0267-3b15-a623-7fed0f4fee31 | -5.30752 | -43.0404 | 2025-10-17 12:36:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| c1c81d27-9791-33af-b1df-6490104ac534 | -7.349 | -44.15328 | 2025-10-17 12:36:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 33.5 |
| bbe969ab-1ed3-3cf6-ba29-8a10a965b0b4 | -8.134 | -45.55485 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 213.9 |
| 2ab09872-5b5e-33ee-bf21-e5421df3c0ee | -2.87775 | -50.73032 | 2025-10-17 12:36:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 73a1b0a7-cb2a-31a6-a454-a13483d2773f | -3.44732 | -41.45758 | 2025-10-17 12:36:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 82da5744-80d2-329d-8db9-067b709876c4 | -1.17109 | -49.18638 | 2025-10-17 12:36:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 112a1710-cd3c-3259-9b6c-e42525cc7c34 | -5.99885 | -44.14678 | 2025-10-17 12:36:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 586abc6c-6fa9-3973-84cf-389ab1a2358e | -8.20228 | -43.32648 | 2025-10-17 12:36:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| b41bbe17-c0c6-317c-9e26-8a95c3be5510 | -9.24855 | -44.3614 | 2025-10-17 12:36:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| df8efab7-5108-350b-91f2-6af2829869aa | -7.07973 | -44.24339 | 2025-10-17 12:36:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 11091ad0-4490-3d15-ad8e-bfcb11e1edfe | -5.84257 | -42.23758 | 2025-10-17 12:36:00 | TERRA_M-T | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 38.6 |
| 4c44ca4f-a718-3d7f-b72e-33ddd5df40ae | -8.13678 | -45.53215 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 32.9 |
| a88be57e-69a2-3c90-b14b-42effdaac1f9 | -8.12037 | -45.55331 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 21a8fefb-b06c-3ce0-a8c2-fe08edffbf38 | -8.70037 | -46.9824 | 2025-10-17 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 8763ef08-b371-3162-bfd2-cd52df511837 | -8.1266 | -45.54741 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 306.0 |
| 5a47e802-82bf-3557-80bc-e3a12760ba84 | -7.99143 | -49.96572 | 2025-10-17 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4bc2ef2c-c0e9-3692-9467-a0e86979d3f1 | -8.57435 | -45.4517 | 2025-10-17 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.4 |
| ba8b4329-2516-3d8e-b0d0-351c8858a79b | -7.48248 | -47.01194 | 2025-10-17 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 994005e5-8525-3c1f-821e-d17428042ff7 | -4.44864 | -43.2269 | 2025-10-17 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| d8fa4553-bea9-39e7-8670-b090b74da4c1 | -6.93788 | -43.67914 | 2025-10-17 12:36:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 46dd84d1-c57a-3ee1-9e30-26275830460d | -8.11765 | -45.5757 | 2025-10-17 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 62989c8f-e173-387f-b37e-343a5932ceff | -3.44541 | -41.45229 | 2025-10-17 12:36:00 | TERRA_M-T | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 41.0 |
| 6b5b03be-ec23-35c0-8dfe-4b51f5838e3c | -8.38918 | -46.23872 | 2025-10-17 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 955cb346-78ea-3f43-a3df-99e2095606d4 | -12.48275 | -45.46101 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 5ee8b357-946c-3071-a68d-cca0f544cfac | -11.01559 | -47.35057 | 2025-10-17 12:38:00 | TERRA_M-T | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| e1d85d7c-5e01-3192-b19f-8bca4b7a984f | -9.85845 | -49.54276 | 2025-10-17 12:38:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6666739b-3acd-39db-bed6-96ae45af851d | -12.70483 | -48.62962 | 2025-10-17 12:38:00 | TERRA_M-T | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e99df547-93ad-39fe-8962-4fd68576e17c | -12.96347 | -47.11706 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| b6621e9d-16ab-32d7-8dcf-6a013681a937 | -11.48764 | -44.20086 | 2025-10-17 12:38:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4e7e5c54-e1b8-349e-a4bd-b7dda29324f9 | -13.38665 | -46.95353 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 5f340b14-422f-3492-b2be-76a541453b6e | -15.70914 | -48.15662 | 2025-10-17 12:38:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 9b655d40-8acf-3e9e-860d-b6c6f0d1d8d8 | -10.58547 | -48.64277 | 2025-10-17 12:38:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9ebd06ce-7274-3ea7-ad09-066f2bc13647 | -12.48201 | -45.45417 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ab79969d-d440-31b7-8d7b-dea42b23f8bd | -13.26436 | -47.10741 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 99c7b0b4-6535-313f-85a2-f8a87ea4af08 | -11.87702 | -54.60387 | 2025-10-17 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 45d377b6-61ca-3ff2-b7d9-d4daf1b4f3b9 | -12.47983 | -45.48819 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 6fb4df01-b5be-3765-93f3-53fefb37a507 | -12.4789 | -45.48129 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 7473dd17-ea1c-3dc0-92d4-af9afaed1f0e | -11.40555 | -44.17954 | 2025-10-17 12:38:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| e16903f5-d19b-392f-a0df-1a904672da6c | -13.42092 | -48.58751 | 2025-10-17 12:38:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 16c88ba5-2b62-378f-8754-73eb2a248428 | -13.92995 | -45.63105 | 2025-10-17 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 652c15c2-d55e-3d40-8283-0fb2866791d1 | -10.14988 | -44.53579 | 2025-10-17 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f6521305-dbaf-3c1c-93cb-9aefd905168d | -12.08065 | -47.42961 | 2025-10-17 12:38:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 44.4 |
| 23997639-75eb-36bd-ab77-63bba1f609b5 | -10.14855 | -44.55976 | 2025-10-17 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| d99fff82-8c09-30df-8419-f319166d90dd | -13.41764 | -48.59311 | 2025-10-17 12:38:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 4e05eae2-4892-32b7-b8e5-2f3671fcfbd6 | -13.41943 | -48.57815 | 2025-10-17 12:38:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 40.7 |
| 827292cb-a567-3c0e-9b7f-6f8b0047684c | -10.61678 | -45.22453 | 2025-10-17 12:38:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 58d41054-8a5e-3c85-bedd-6720cce9598e | -11.26826 | -52.74999 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| a0aee25d-4620-3f6e-a672-3fe260de9870 | -9.96287 | -47.022 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 44.6 |
| ccf1060c-2474-32ac-aaa4-ae767ae68de9 | -9.98778 | -47.02478 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 5f6e0492-d571-3b2a-9d58-1e52aa3e2937 | -12.2288 | -54.46797 | 2025-10-17 12:38:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b66f9546-cd94-3bb5-84cd-d5594fd68208 | -11.94404 | -54.21161 | 2025-10-17 12:38:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3aea87ee-4895-3e3c-a4f8-c62b69dbc81f | -9.97763 | -47.00467 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 302b5b30-e3de-3dae-8942-0bc1d0920b56 | -12.16151 | -45.07881 | 2025-10-17 12:38:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e7845e07-ed22-3474-b5f6-efaf78e6e32b | -10.14338 | -44.59338 | 2025-10-17 12:38:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 269.3 |
| e50d0cd6-0177-3711-ae54-e6b8d1243c95 | -10.75314 | -47.28738 | 2025-10-17 12:38:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fff5fb4e-daf9-36d4-b4e4-14e19f03121c | -10.26846 | -44.04874 | 2025-10-17 12:38:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 109.8 |
| de1debdb-469f-3a49-8473-03ee8bac942d | -13.4794 | -47.96148 | 2025-10-17 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 34ea750a-a60e-3ce5-b868-3d622ebcea1b | -9.95845 | -47.0339 | 2025-10-17 12:38:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 8e790fb4-b830-3c0d-b689-290a87350b46 | -10.46018 | -50.86277 | 2025-10-17 12:38:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| d36d18db-5f7f-3c50-9b82-02b50aa05c24 | -11.73917 | -51.1439 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 6efa23e1-978f-3efe-afa4-9d2819eacffb | -10.98816 | -47.90239 | 2025-10-17 12:38:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 500fc557-0173-366d-95d6-188199f7f451 | -12.10352 | -45.87041 | 2025-10-17 12:38:00 | TERRA_M-T | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 8c865ae1-a71f-302a-8d9f-41de9b834ec7 | -11.71755 | -54.17786 | 2025-10-17 12:38:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 98e42b69-800d-36a7-947c-1cbafa90316a | -10.29725 | -44.0252 | 2025-10-17 12:38:00 | TERRA_M-T | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 19ed0b52-8abb-3f6a-b31a-057c828ab0b8 | -10.25256 | -44.04752 | 2025-10-17 12:38:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 184.6 |
| b87c9072-cb7c-343b-a40e-801452642cd2 | -10.10335 | -47.6605 | 2025-10-17 12:38:00 | TERRA_M-T | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 742e83ec-d09e-3991-ba8f-acc45ee50671 | -11.39503 | -44.21855 | 2025-10-17 12:38:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| ddcc53ac-8a40-3463-9719-ad524cca8694 | -12.9595 | -47.9342 | 2025-10-17 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 92bafa0a-f8bc-3feb-bb54-59a849fe2f91 | -13.43889 | -47.95112 | 2025-10-17 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 38.4 |
| f9fb8a77-94d1-308f-81da-a9be766a2479 | -14.41187 | -47.89424 | 2025-10-17 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 26.9 |
| c33151a4-7089-3cdc-ac02-b07ec62aa127 | -13.93003 | -45.63782 | 2025-10-17 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 75e8fa44-d922-3f1f-964b-d4b4d91b56fc | -13.40935 | -48.5861 | 2025-10-17 12:38:00 | TERRA_M-T | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 53e1440b-0bfb-3cb5-a6b9-0ba8f51e1772 | -11.24901 | -55.41138 | 2025-10-17 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 47124e46-65e2-3fa1-8961-5476ab5a74d3 | -10.46155 | -50.85249 | 2025-10-17 12:38:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a1d029c5-e911-3a46-8a53-d8fe79729501 | -14.42441 | -47.89471 | 2025-10-17 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 34.1 |
| ff940d30-058d-334e-8726-7f775fa3b827 | -14.42208 | -47.88908 | 2025-10-17 12:38:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 17153471-b291-3092-b93b-6fea561ea2fa | -12.49445 | -45.4901 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 8bbd92e1-dd17-3bad-ac94-01465303ce76 | -12.92147 | -47.14394 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| eb5fc979-2747-3104-86b0-6e44c4da2a08 | -13.47738 | -47.97906 | 2025-10-17 12:38:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 44.9 |
| ffebc75f-0bd6-3275-be7a-5209b2a6cbe9 | -10.8617 | -51.29778 | 2025-10-17 12:38:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fd892f9f-9dfe-3de3-a882-883afa308355 | -11.11551 | -45.88399 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| a77ecefe-b689-389a-b7e5-35e92feac25a | -10.95105 | -49.77287 | 2025-10-17 12:38:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 187064c0-08ab-3022-b4e7-f22681609eed | -12.50906 | -45.49193 | 2025-10-17 12:38:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 1a9a83f5-5538-3fc9-91a6-08c0af08dbff | -10.28441 | -44.04956 | 2025-10-17 12:38:00 | TERRA_M-T | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| cc72a5d6-ed4b-3946-915e-b58d6bf3a694 | -11.59079 | -44.08337 | 2025-10-17 12:38:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 86cd1a50-0763-347c-b841-9f5ed42fed6f | -11.47832 | -44.19435 | 2025-10-17 12:38:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 206.2 |
| 778d5a83-21b0-375f-9572-e8e285a0c172 | -13.18985 | -46.41296 | 2025-10-17 12:38:00 | TERRA_M-T | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 89fde66f-62bc-32c3-a6d6-d90e5994c57c | -13.05765 | -47.31518 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 220.8 |
| 8e7651a5-de74-3f7f-8dd0-8584b14a3729 | -13.0426 | -47.33334 | 2025-10-17 12:38:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 5549562f-5b28-3cad-9722-95d722ed4e21 | -11.09575 | -45.87615 | 2025-10-17 12:38:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |


[Clique aqui para ver as próximas entradas](README120.md)
