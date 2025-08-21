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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6adca40e-30bb-3cc5-98ed-7442cbfa40b3 | -14.4875 | -45.943 | 2025-08-21 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 40.8 |
| dcbc33ed-4355-33cd-9015-dba6c66e9374 | -8.8736 | -62.4115 | 2025-08-21 00:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 87e6b2cc-20cf-3877-b01c-1af8d8742878 | -15.0193 | -54.832 | 2025-08-21 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 52.3 |
| c1280939-53d6-3c71-b662-67a38fa48cfa | -8.5556 | -66.9389 | 2025-08-21 00:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 80e83e7a-c646-3e0e-86d9-4fc5687c6763 | -13.1367 | -54.9171 | 2025-08-21 00:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| f5021e0e-0e12-3109-85d5-3252d57d7efa | -14.507 | -45.9396 | 2025-08-21 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 7a32eb74-77c3-3ad2-80e2-219ef27bfb5e | -12.9344 | -46.222 | 2025-08-21 00:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 03e27ee7-e7ee-3fe4-9a72-abea834107d6 | -11.7299 | -58.3201 | 2025-08-21 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 0168e481-2979-3b7c-ba1f-c930fec5407c | -11.7488 | -58.3187 | 2025-08-21 00:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 35d75e39-ef09-3f7a-8c18-5d0627fa315d | -12.9537 | -46.219 | 2025-08-21 00:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 217.5 |
| 54d8e0e8-5696-3595-ae91-e5372bbd3bc8 | -12.9533 | -46.2419 | 2025-08-21 00:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 9096484e-9cfb-3643-b194-456ab699d52d | -15.8849 | -49.0076 | 2025-08-21 00:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a1c9c0bb-8dcc-3f59-915d-0d387cbf7dac | -12.9726 | -46.2389 | 2025-08-21 00:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cd48787a-b145-3e92-be6a-cd6e02b9eb56 | -7.0166 | -44.6184 | 2025-08-21 00:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 53eb4e1f-4be3-39b1-b461-59642a28999f | -7.8568 | -46.7304 | 2025-08-21 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 51.2 |
| b6655e55-84dc-3a96-a718-ea4d75acf212 | -12.973 | -46.216 | 2025-08-21 00:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 109.6 |
| e1236280-f58b-3a1e-906a-d90e49b3beaa | -8.3714 | -54.9919 | 2025-08-21 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| bb48e4f2-4bee-3af5-b86b-983952dc74f2 | -14.5065 | -45.9627 | 2025-08-21 00:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 78422f9e-4337-3163-9843-b0820a5d102f | -14.9999 | -54.8343 | 2025-08-21 00:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5ef34dd4-4985-3fb8-8215-d37be42df52a | -14.8543 | -47.9279 | 2025-08-21 00:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e013b28f-af87-3aab-a92a-78bfca4f5e18 | -5.875 | -42.4104 | 2025-08-21 00:00:00 | GOES-19 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 57.4 |
| 099d21b9-afa8-38d2-9fef-db746b833d52 | -14.5065 | -45.9627 | 2025-08-21 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 7e42c9db-397d-3c16-ba1f-728c8f4f3bcb | -8.3714 | -54.9919 | 2025-08-21 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b1c08995-8421-355f-972e-4b3481ac4307 | -13.1367 | -54.9171 | 2025-08-21 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 9089db39-c99d-3f8f-91c4-68220216bb60 | -12.9533 | -46.2419 | 2025-08-21 00:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 456.1 |
| 77dbb90a-f21f-3e75-ae01-46e25462fb9f | -13.1558 | -54.9151 | 2025-08-21 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 66823bb2-cbb6-3878-9cae-75ca7815d77d | -15.8849 | -49.0076 | 2025-08-21 00:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 52.6 |
| c05fac2b-76bb-3c12-a2ed-13ad6eca3721 | -12.9726 | -46.2389 | 2025-08-21 00:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| af150276-9992-352a-86b6-4e7c6a1f7b8e | -7.0166 | -44.6184 | 2025-08-21 00:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| c3937620-bb23-33a2-b12a-a0b530ab93c3 | -14.507 | -45.9396 | 2025-08-21 00:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| c4846630-52c4-3c04-990c-a812202339f4 | -12.973 | -46.216 | 2025-08-21 00:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 1bfb2bf4-2da9-3f04-8f9f-05840e0ec752 | -12.9537 | -46.219 | 2025-08-21 00:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 594.8 |
| c0a94397-1a2d-3d2a-aa07-f4a2ed222c77 | -11.7488 | -58.3187 | 2025-08-21 00:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f4dc8dfd-f19f-34bf-9451-940690ba44dd | -12.9344 | -46.222 | 2025-08-21 00:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| f47822a5-5fdc-3eee-af31-1a9b2c43a015 | -14.8538 | -47.9504 | 2025-08-21 00:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 62.2 |
| edc8d596-814e-36f1-87c9-4ee44f2f5915 | -6.9607 | -42.858 | 2025-08-21 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.7 |
| 5a3d97a7-dea3-3a9f-8008-a83ade9c994c | -14.8543 | -47.9279 | 2025-08-21 00:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 6968598a-cc72-3a38-90fb-2d4de3250b68 | -12.934 | -46.2448 | 2025-08-21 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 09c53a9e-eea1-347c-8a47-f5bdace9940c | -14.5065 | -45.9627 | 2025-08-21 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 71b85fdd-b498-3958-9fdb-f12a10f778ae | -13.1558 | -54.9151 | 2025-08-21 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 32f78d7a-1919-3f13-94f0-1928b871656b | -8.3714 | -54.9919 | 2025-08-21 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b5a572d9-5a6c-3938-9f11-1a38a4786b23 | -12.9537 | -46.219 | 2025-08-21 00:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 367.6 |
| 961a9e1c-b6e2-36d2-98d7-f1ca60350777 | -15.9046 | -49.0043 | 2025-08-21 00:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 20c4bde5-dbd1-368d-90cb-11f4c0271713 | -12.9726 | -46.2389 | 2025-08-21 00:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 072989c9-f88a-381d-af0a-6508b88abfac | -13.1367 | -54.9171 | 2025-08-21 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| bfe1d940-5afb-3497-a925-0b69c07bb9ba | -14.507 | -45.9396 | 2025-08-21 00:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 7ab64a33-5eb0-3a25-a830-26eb3653afe3 | -15.8849 | -49.0076 | 2025-08-21 00:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 91442a38-d2a3-3083-902d-754b87646bf9 | -12.973 | -46.216 | 2025-08-21 00:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| a7199ff1-98df-350e-943c-61380dc82829 | -10.9905 | -55.2403 | 2025-08-21 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 70bdb618-09bc-31e0-b28f-e73517a559ef | -14.8543 | -47.9279 | 2025-08-21 00:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8ff15501-2800-36d6-8d63-88dd3575a584 | -14.8538 | -47.9504 | 2025-08-21 00:20:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 2eb3dac0-8bbe-3b1e-b6fd-acd7ccd42fc6 | -12.9533 | -46.2419 | 2025-08-21 00:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 577.5 |
| a65833ee-7501-398e-8454-d533f5f5b3b3 | -12.2196 | -45.3922 | 2025-08-21 00:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2d406dc4-7485-36af-8a98-928a80ce6fc8 | -7.0166 | -44.6184 | 2025-08-21 00:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 173acecc-1d87-3abc-ae1b-dd21acd57dd2 | -10.9717 | -55.2419 | 2025-08-21 00:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 84601592-36ba-36b7-b14b-73697d5f5032 | -23.69007 | -51.80498 | 2025-08-21 00:24:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 64.9 |
| c3350481-6732-35cd-997d-dd50873b56f4 | -23.68291 | -51.78473 | 2025-08-21 00:24:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 48.7 |
| c4814938-b0d1-318a-85d9-b4d61bd35c63 | -23.68784 | -51.77854 | 2025-08-21 00:24:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.7 |
| 182bc47f-c900-32c2-a8f1-3cb3e36ecfe6 | -22.94091 | -43.70879 | 2025-08-21 00:24:00 | TERRA_M-M | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 9c90d6a1-f839-30e3-b45f-22740a994a27 | -22.44609 | -43.85145 | 2025-08-21 00:24:00 | TERRA_M-M | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8830fbab-cd57-346b-8204-f838258c571c | -23.6853 | -51.81107 | 2025-08-21 00:24:00 | TERRA_M-M | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 42.1 |
| 49ebe403-cad2-3cfc-a842-3ce7bcf95933 | -21.98332 | -42.87574 | 2025-08-21 00:26:00 | TERRA_M-M | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 20.5 |
| 41e5568b-1142-3c5c-9725-40a2f63cc781 | -15.92117 | -48.10672 | 2025-08-21 00:26:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ad097c50-c4f8-3b70-a364-eb40aefc57dd | -16.04981 | -49.07576 | 2025-08-21 00:26:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f57c3c58-d1cb-330f-9beb-c4ea0c1b4d26 | -17.39012 | -44.25205 | 2025-08-21 00:26:00 | TERRA_M-M | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2c065f9f-c43d-3170-ba5c-c75311dfaaf0 | -19.78365 | -44.30464 | 2025-08-21 00:26:00 | TERRA_M-M | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c4ea30d5-48da-359a-88d4-4525455499fe | -15.51365 | -48.05297 | 2025-08-21 00:26:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.9 |
| bc18dda7-753d-3533-8bfe-9cd71d1b6cfc | -18.1306 | -43.95203 | 2025-08-21 00:26:00 | TERRA_M-M | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7258c570-5373-3693-bf7c-7a2cc0ef6333 | -21.56086 | -41.17374 | 2025-08-21 00:26:00 | TERRA_M-M | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| aba60071-e67b-33fa-b401-31e185e50e50 | -20.71933 | -43.05709 | 2025-08-21 00:26:00 | TERRA_M-M | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 2ddd55fa-d355-3364-a1c8-37117bfddafb | -16.01179 | -43.71019 | 2025-08-21 00:26:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e3e0e252-e66c-3ba0-b213-5eb8dc1ff794 | -18.6708 | -46.97417 | 2025-08-21 00:26:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 191dbb8e-045a-3e10-9b9c-afc7b7aa7abd | -15.04813 | -42.47723 | 2025-08-21 00:26:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 516fbff9-c942-3568-9927-73c8c124d630 | -15.88945 | -49.00915 | 2025-08-21 00:26:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 97.9 |
| d6d50069-2bbf-3771-8db4-c8f914d5e380 | -15.97328 | -48.13334 | 2025-08-21 00:26:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 8ba3ce0a-bb0b-3b47-8181-1ab8ddab5be7 | -15.9719 | -48.12252 | 2025-08-21 00:26:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e3115829-f849-38d4-b485-4c7231a7456a | -22.30448 | -43.18295 | 2025-08-21 00:26:00 | TERRA_M-M | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8a88c701-0c0b-3193-9c52-d9bf060c8f6d | -19.30102 | -46.02872 | 2025-08-21 00:26:00 | TERRA_M-M | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9106dbda-2417-3cbd-bd95-56a917dedbe9 | -15.89097 | -49.0215 | 2025-08-21 00:26:00 | TERRA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 7fa1c684-e08c-3753-940b-7d6e1c6868f5 | -15.91792 | -48.11366 | 2025-08-21 00:26:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 14e33304-6d18-31af-8c72-22fbadfd4d6c | -15.92255 | -48.11781 | 2025-08-21 00:26:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 308e873a-7350-3f91-ad74-152fb6212333 | -15.04632 | -42.46563 | 2025-08-21 00:26:00 | TERRA_M-M | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 21.0 |
| 26a5d235-9c88-3dd1-97e7-7533293e1cec | -17.57946 | -42.28125 | 2025-08-21 00:26:00 | TERRA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 8459b530-9d8f-3d77-aee1-6cb8b48e01a2 | -18.73256 | -39.8659 | 2025-08-21 00:26:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| d86cc13e-21ca-3fef-8c0b-c1c89f357690 | -13.01564 | -45.17446 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 6343687c-c5fd-3075-8641-87fd819ab122 | -8.84755 | -52.04982 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| a145ae63-750f-3558-a2a1-38b30b2d7973 | -9.10847 | -45.181 | 2025-08-21 00:28:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9b8a2399-32bb-329b-9d4e-57a19ca9605e | -9.48423 | -47.3234 | 2025-08-21 00:28:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e554b997-007d-358e-afd2-9fbae9475b73 | -9.29333 | -48.4287 | 2025-08-21 00:28:00 | TERRA_M-M | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f2b79616-de7c-34f6-b92b-955470d921ac | -13.03111 | -45.21928 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 709e747d-6666-3533-994b-a3068842851d | -9.92151 | -49.29548 | 2025-08-21 00:28:00 | TERRA_M-M | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 4123b571-8fc2-3c96-9852-3665952515ed | -13.59058 | -43.35184 | 2025-08-21 00:28:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| b112d4ad-d62f-38e9-b66d-5b627f072a0e | -13.03482 | -45.18097 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 372d10c3-8751-34c2-b901-dfae5a2c60c7 | -13.01695 | -45.1837 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fe08a925-8a66-3830-b84c-22f2e12a2f21 | -14.12353 | -45.38291 | 2025-08-21 00:28:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| d8fda387-a653-3a00-8e2a-07a11e5c2cb8 | -9.55481 | -48.11578 | 2025-08-21 00:28:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9fd3a82c-8906-3022-9b08-9807086e3fdc | -13.0424 | -45.16448 | 2025-08-21 00:28:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 8547ab35-62d2-3f78-9745-837e10649763 | -10.99059 | -55.24171 | 2025-08-21 00:28:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8cb9b923-5908-3392-a022-e197acbd071c | -13.33338 | -54.40847 | 2025-08-21 00:28:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 39ac6893-a1ff-387d-af3d-f2041c22c6ca | -13.38159 | -47.49591 | 2025-08-21 00:28:00 | TERRA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |


[Clique aqui para ver as próximas entradas](README2.md)
