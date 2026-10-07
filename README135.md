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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3025e022-45c1-3e83-ae70-22c466d44d45 | -7.1891 | -44.3042 | 2026-10-07 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| ec38f54d-a1e0-3d7b-bf22-e0b7c67b5281 | -9.1356 | -65.4145 | 2026-10-07 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| c66dc17c-4973-3bd2-b567-d460557742dd | -17.5269 | -45.4622 | 2026-10-07 14:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 223.5 |
| 8ba9650c-bf1e-30a7-953d-3a618a3d13aa | -8.339 | -72.6194 | 2026-10-07 14:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 5c93450c-fb27-31ee-945d-8f1807e49a33 | -9.1362 | -65.3022 | 2026-10-07 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 772986d6-6807-37fe-b8b1-68eee078273a | -9.1363 | -65.2835 | 2026-10-07 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| e6369644-1d42-37a1-b60a-c35da4914ef8 | -6.6753 | -44.9674 | 2026-10-07 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| aee50eb9-2171-31a3-9e1c-e922d219a161 | -1.2086 | -49.0412 | 2026-10-07 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 41428d17-88cf-3e0d-bea5-89f5193cb620 | -11.8315 | -43.5391 | 2026-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.2 |
| b4ec9d76-a669-3097-bda0-b0a9f4a7adc9 | -9.6757 | -65.0401 | 2026-10-07 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 40ae0559-8d4f-35e4-a63e-53ac04d52fca | -8.8891 | -66.7445 | 2026-10-07 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c8805644-6078-34e5-8084-f3577cf34552 | -6.2162 | -52.7876 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| b05e3d42-db7b-31f3-91bd-bf20d03259e9 | -11.7335 | -43.649 | 2026-10-07 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| bb07883c-b5ca-3717-afff-bc746cb9f7d4 | -9.3619 | -45.4288 | 2026-10-07 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e4298df7-0ffa-3cb4-81f3-3e88f54d8823 | -9.0058 | -65.4373 | 2026-10-07 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.1 |
| fce5f3d5-416b-35f4-a4d7-9196fe246297 | -6.4756 | -52.8142 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 0a63f1fe-8ae7-3e0f-ae10-6b601d6819ca | -6.1431 | -52.6481 | 2026-10-07 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 399379da-3912-3848-9107-5e20f17976be | 1.6385 | -55.785 | 2026-10-07 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 0d39c7f5-c8f2-301e-a230-1e2542553941 | -8.5426 | -54.5975 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d803666c-a31a-38b5-a0e9-74253a1d4a7d | -7.2179 | -55.1817 | 2026-10-07 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2da38ca8-8001-361e-aec0-ac3b25614dc9 | -9.3394 | -65.4638 | 2026-10-07 14:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 029625cb-ee3d-3b76-a8e8-0a2ed8f61836 | -11.1051 | -45.689 | 2026-10-07 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 312d19f8-d53f-3749-9d75-efb2ad02fa13 | 1.8768 | -55.7227 | 2026-10-07 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 62812dde-a0e4-36e7-b792-144254bffedb | -6.2053 | -49.3826 | 2026-10-07 14:40:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 3688b67e-1514-3c3d-9d44-91bd2d9882ed | 1.9134 | -55.7024 | 2026-10-07 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| d0b4d711-ea43-384b-a71e-bfb2972c92e7 | -8.8892 | -66.7259 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 29aaf179-4365-384b-adf8-c1d8b568193f | 1.7121 | -55.6261 | 2026-10-07 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 76b7ee93-b30f-3936-86b0-948ef1e11b7e | -7.3935 | -46.2144 | 2026-10-07 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 95633070-a3c1-3575-9204-f3695036b6d6 | -8.3391 | -72.6012 | 2026-10-07 14:50:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 290045a9-5e5a-3907-90cf-403ddcc6abde | -6.1431 | -52.6481 | 2026-10-07 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 1fa4de40-5350-37f3-a5d2-d67f42b13daf | -8.0019 | -47.1825 | 2026-10-07 14:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 05b9c2e5-d0e9-390d-96ae-25ee46c3d033 | -7.8146 | -45.5009 | 2026-10-07 14:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 1c24c9c0-6a57-326f-89d8-14e8adf5ad29 | -7.8789 | -72.3492 | 2026-10-07 14:50:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 3a6788b1-e735-316a-b781-99c551605fce | -9.3394 | -65.4638 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| d7f315df-9105-305b-8bf7-16f81beb2866 | -7.7653 | -48.2334 | 2026-10-07 14:50:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 8ffb290a-a99a-3da5-a907-61049553734c | -6.0076 | -53.4919 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 9260212b-f2c9-38a2-a90b-4cfcdef0d4da | -11.1051 | -45.689 | 2026-10-07 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| f7cfbaa9-1900-3080-8c7a-a80fcec9e41b | -8.7866 | -47.5713 | 2026-10-07 14:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 98.4 |
| d0b7436c-2367-3705-b034-e7492ed9e9e1 | -6.217 | -52.6851 | 2026-10-07 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 117ef3f6-835a-3b81-a5f0-375fd323993e | -11.0867 | -45.6459 | 2026-10-07 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| aa189248-136a-3c7d-98a7-f93a8d32af7b | -7.7579 | -54.9499 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 646ff1b0-8ddd-31cd-8db5-432aec40e3ed | -9.1356 | -65.4145 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 42f3526c-c784-3ef8-ba26-2f2bc97cf3b4 | -9.4492 | -44.6167 | 2026-10-07 14:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 44c05369-e50f-3a2c-969d-b70d526beb92 | -9.1257 | -67.8322 | 2026-10-07 14:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b9de875e-ebbd-3dba-a1b3-422605facfdd | -12.1746 | -44.7051 | 2026-10-07 14:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 525.0 |
| cd3f273d-20a1-3473-9a6f-f6acb1991211 | -11.7143 | -43.652 | 2026-10-07 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 250.3 |
| 515b781d-ab4e-3e7a-9e89-20c21a95c96e | -8.5238 | -54.619 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a9b4a793-ba0f-3e6c-9409-b22adb85159b | -7.2179 | -55.1817 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| c67c1ea2-9d66-384f-840f-c4317e031c0e | -0.3768 | -51.9947 | 2026-10-07 14:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 55.8 |
| efca028f-e50e-3874-b00b-fe053e8dd282 | -8.524 | -54.5987 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b5bd0452-84a8-30a2-843b-cd7b9731b5e2 | -1.4569 | -54.7761 | 2026-10-07 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 357aee7e-5d08-38fa-848d-63960f84e43c | 1.6385 | -55.785 | 2026-10-07 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 1dd463a7-8cf4-3889-85ea-8466231380bd | -2.9903 | -42.8689 | 2026-10-07 14:50:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| f9d35c56-7e75-331a-9d31-d16012351264 | 1.7121 | -55.6063 | 2026-10-07 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e88c7302-1fb8-3a98-a292-806a1f68fb27 | -4.3285 | -43.8032 | 2026-10-07 14:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 2a8db8ba-47d1-3993-b27c-12c2dde6e48a | -11.0935 | -47.6019 | 2026-10-07 14:50:00 | GOES-19 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 5f1fe1b5-c46d-3fe0-b0f7-8cd2d60b655c | -11.6186 | -43.6433 | 2026-10-07 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 275.0 |
| 91264ea6-2b7b-3b36-9e7a-a92f3ca25468 | -11.6382 | -43.6166 | 2026-10-07 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 36ebc5c9-9049-3c78-909f-34fa0295b6eb | 3.1098 | -60.5943 | 2026-10-07 14:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 579965fd-8d7e-3cd4-aa43-e7d13d5a3182 | -6.4756 | -52.8142 | 2026-10-07 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 9fe28e5a-bcf8-3fb6-a80a-587abdde3f0e | -8.7503 | -69.6474 | 2026-10-07 14:50:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 11c0c87d-681c-34aa-8eb2-b510c7e34708 | -8.7293 | -70.7677 | 2026-10-07 14:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7032b9bc-f18f-34ce-a7ec-40b92050cf92 | 1.7671 | -55.5661 | 2026-10-07 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7f2118a5-42e0-33fc-ad99-1beda6652a12 | -8.339 | -72.6194 | 2026-10-07 14:50:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 122.6 |
| acf5cba0-bad2-34e5-8221-b4d669d9faf9 | -6.1041 | -55.7162 | 2026-10-07 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7815650c-80ff-3811-ae41-1acebd150e45 | -6.6468 | -47.9078 | 2026-10-07 14:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1047319f-36ea-3998-bea0-01c6c182bd7b | -5.7319 | -41.6589 | 2026-10-07 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 210.3 |
| 989510ad-3f76-355a-bc6f-4b5af89dc6cc | -11.8508 | -43.5361 | 2026-10-07 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 323.7 |
| b26639b5-7e2d-347f-a121-d502fe307ba0 | -6.4598 | -55.0215 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| eda796e1-57b9-3607-b40f-9065ca3e2fab | -2.1361 | -54.4671 | 2026-10-07 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 8b67103f-590c-3162-8cd1-7ccc5e1db1f2 | -8.5844 | -45.6729 | 2026-10-07 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 170.8 |
| 81cad3ab-27ab-3490-949e-180588d606b2 | -11.1054 | -45.6662 | 2026-10-07 14:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| e94dcb49-2a61-3d06-b7c1-a60b9b246712 | -5.7317 | -41.6829 | 2026-10-07 14:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 153.5 |
| 6b82a40d-b325-3b9d-a5a3-e1b35188fdc4 | -10.6199 | -60.4852 | 2026-10-07 14:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 2a62c5ea-3ebf-3c38-b24e-af5546f2558c | -12.2136 | -44.6758 | 2026-10-07 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 46bcdb6e-90b2-38bb-9c23-a697cd4e60a9 | -12.1948 | -44.6554 | 2026-10-07 14:50:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 09cb7211-a28a-3cd7-9570-7a3b6d79f54b | -9.3619 | -45.4288 | 2026-10-07 14:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 2f9fa22d-e700-31e8-8ae9-21f94d3a1e5d | -10.5287 | -47.2711 | 2026-10-07 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 9449431b-55a4-3eaa-9eea-5abb76505981 | -7.5847 | -55.7205 | 2026-10-07 14:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 487bbeee-f2d6-3cff-be39-0b664be5c795 | -8.6033 | -45.6709 | 2026-10-07 14:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| de5ef7fe-f3ab-37ee-bff5-cf7efa27ca2c | -10.5097 | -47.2733 | 2026-10-07 14:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| e9828d8b-397b-342d-a0dc-1eeaaae91e3a | -1.4752 | -54.7759 | 2026-10-07 14:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 173.2 |
| 0ce2a9fd-7be7-329d-accd-69621fe2e41d | -7.89 | -54.7206 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 1ec1f92b-8b77-3642-a686-4d2d7feb3d2e | -7.5568 | -46.7128 | 2026-10-07 14:50:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 785f0fdb-ed71-31a9-bf3f-277937f28801 | -2.0447 | -54.3085 | 2026-10-07 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 6cdbc570-ce92-33f2-a090-4905e039d4ab | -7.2816 | -46.1571 | 2026-10-07 14:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| a2474337-f220-325c-9bab-367beec601ad | -1.2455 | -49.062 | 2026-10-07 14:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 0147676a-53ac-30b2-8d32-c17963591343 | -9.0046 | -65.6988 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b216a8d7-d28c-3b08-b0c7-075a00534ee0 | -6.0075 | -53.5122 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.0 |
| e646ba54-f032-3f70-8837-ccbfe8577e69 | -11.6566 | -43.661 | 2026-10-07 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 97a4eb47-234d-3da0-8891-67096fa57921 | -1.2922 | -54.5585 | 2026-10-07 14:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 89a9c09a-13a6-3bde-8e6e-6c0953cee4de | -11.6378 | -43.6403 | 2026-10-07 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.5 |
| f93d7681-b241-3c76-ab57-cd6df5889502 | -6.6943 | -44.9431 | 2026-10-07 14:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 44f1f3b4-cb15-33c3-8a24-7d310f4b5689 | 1.6385 | -55.8047 | 2026-10-07 14:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| eb06f924-1c31-389d-a264-e269a5919b2a | -8.8364 | -62.4321 | 2026-10-07 14:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 37a83f57-795b-3579-8a11-91961ba3a767 | -9.1363 | -65.2835 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d38eef79-081c-369e-9ef4-e80adc41d09c | -9.1362 | -65.3022 | 2026-10-07 14:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 6ff0b207-f3b6-3d78-b17e-59032316a009 | -9.8245 | -65.0348 | 2026-10-07 14:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 6e2da22e-3797-33b5-b123-aad8474ed63c | -7.1813 | -55.1237 | 2026-10-07 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.2 |
| a45f884b-43e8-334c-a145-40add5538fce | -11.7774 | -46.5726 | 2026-10-07 14:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |


[Clique aqui para ver as próximas entradas](README136.md)
