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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6bda9e4c-d5a7-33b7-9434-d236b3dcb92a | -6.95874 | -43.53711 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 32a01020-e0b0-3f7e-80af-ad5be34e231a | -12.80755 | -42.72855 | 2025-02-04 04:01:00 | NOAA-21 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b6a79d44-8134-3cac-97f3-8457276fc8ba | -6.95139 | -43.53595 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 71a8667e-b13b-3b04-b809-15392ba5787c | -8.61549 | -35.71773 | 2025-02-04 04:01:00 | NOAA-21 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d4aa4008-2b07-361f-9ebd-d3522eabb26f | -14.13668 | -41.69194 | 2025-02-04 04:01:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 22d66ac9-cd02-32a5-ba81-aa3897554c8e | -9.08037 | -40.25422 | 2025-02-04 04:01:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2a5d1f72-2511-3cb2-b936-5ae85dea54dc | -6.96472 | -43.56942 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1a35c38c-5515-348e-a0ce-7ca8bb20fba9 | -6.94771 | -43.53539 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 627afb26-1a95-38a3-86fe-da965b2491c6 | -6.95946 | -43.53277 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8fc72ae-6a62-31fd-8469-6607e7e3ef05 | -6.96537 | -43.54265 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 83a2c179-c7b8-36b7-a071-c8e1fbdabcd5 | -6.96912 | -43.56567 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1dec9471-f139-3972-b342-e3a421e3a903 | -6.9617 | -43.54206 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bf2f67f-e598-32f7-8979-c4750e71d2e6 | -13.41063 | -41.33105 | 2025-02-04 04:01:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee920ba5-caa1-38c1-99f1-a8e415193899 | -12.19093 | -38.16998 | 2025-02-04 04:01:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9b501040-0adb-366f-8dc9-44b6585f9565 | -8.94124 | -44.24363 | 2025-02-04 04:01:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5bedbd8-d664-3228-8a97-960bad95d95a | -6.95212 | -43.53159 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54d12267-a5db-310b-81e6-37d7aca86e79 | -14.08038 | -41.76628 | 2025-02-04 04:01:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7abb6880-325f-3744-850a-0b08c198d7ab | -6.97208 | -43.57061 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31d08f5c-8346-3a4d-bcf3-c8878f6d6eea | -8.12818 | -38.64673 | 2025-02-04 04:01:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ffbac99f-9ce5-3524-9183-c761b6f0d360 | -6.964 | -43.57382 | 2025-02-04 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9331d706-abe7-3d81-9977-f950b4d81fc4 | -6.96104 | -43.56883 | 2025-02-04 04:01:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 241e0d8f-1840-3127-91b2-58db50a60faf | -6.96176 | -43.56446 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 36d8aaf4-219e-355c-8902-1341f0299b87 | -6.96242 | -43.5377 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a325c111-b063-3704-a198-50dd97b9503f | -13.86458 | -39.41393 | 2025-02-04 04:01:00 | NOAA-21 | PIRAÍ DO NORTE | BAHIA | Brasil | 2924678 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1aa4c836-3b47-36b6-803c-0a9e1c9594ec | -8.94496 | -44.24423 | 2025-02-04 04:01:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f706636-110d-3af5-822a-92ede57067c8 | -6.96609 | -43.5383 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8ff661a-1dc2-39b2-9fe0-e4e4ed59209f | -6.95729 | -43.54586 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3bb7757a-c90d-3de6-b9bb-32c5bcf15858 | -7.72107 | -36.50401 | 2025-02-04 04:01:00 | NOAA-21 | CARAÚBAS | PARAÍBA | Brasil | 2504074 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b672dc3-1195-3896-874a-de535e6e0c50 | -8.13472 | -37.65353 | 2025-02-04 04:01:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3ec25c66-4f03-3654-8f51-ceb276790e36 | -6.94994 | -43.5447 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 80494cfa-39fb-3026-8ca7-30d7442e1c87 | -11.32876 | -41.67175 | 2025-02-04 04:01:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ac9b4bea-7c5c-3ebb-b4c7-c0d927b49edd | -6.96616 | -43.56071 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7c34068e-e63d-35a7-a451-83c467729539 | -6.95361 | -43.54529 | 2025-02-04 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3f7b840f-35e9-3f7a-a283-6b18efa158f7 | -21.17998 | -43.98094 | 2025-02-04 04:04:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 891a1426-ca99-3444-99da-1e53a77966b1 | -15.46938 | -39.50202 | 2025-02-04 04:04:00 | NOAA-21 | CAMACAN | BAHIA | Brasil | 2905602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1e870923-ca1a-3ae9-846f-1531fe1739ca | -18.45189 | -41.06846 | 2025-02-04 04:04:00 | NOAA-21 | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ab661bd-b9b9-3e63-9dd5-e647ebe67cb8 | -16.34906 | -43.69579 | 2025-02-04 04:04:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ea3c1d1-97e9-3f6a-91c4-2803697546e0 | -21.62526 | -43.46806 | 2025-02-04 04:04:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f444b506-8d34-3812-afe8-a29e2a445b5c | -19.71772 | -40.35276 | 2025-02-04 04:04:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d27dfeea-6d3e-3269-b8e3-5ad741e67cd4 | -19.83937 | -40.08176 | 2025-02-04 04:04:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 516572e8-249e-3096-8bfd-9cbda05fa39c | -21.10726 | -40.85444 | 2025-02-04 04:04:00 | NOAA-21 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 91701fb8-f8ca-383f-a984-67ce17235c95 | -19.36293 | -51.25266 | 2025-02-04 04:04:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| 1aa6619b-9601-3a38-b2d4-4939ab74e953 | -15.51573 | -42.67772 | 2025-02-04 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a7de5f11-f8e1-3ccb-a367-09b1c9809f4a | -15.44995 | -41.69028 | 2025-02-04 04:04:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 507e0eb1-b847-3539-b1eb-a72f68aff151 | -18.00526 | -39.84428 | 2025-02-04 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d8473a09-1714-3d3b-8224-cba78022b351 | -16.75119 | -41.04737 | 2025-02-04 04:04:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b0b943ab-91da-3da1-bf7f-7f68a8be52ea | -20.41758 | -43.5532 | 2025-02-04 04:04:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a155f928-34f7-3fb2-866a-2dd368420f5b | -19.96515 | -42.57331 | 2025-02-04 04:04:00 | NOAA-21 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ca7e1c26-5fcf-3f58-b01e-b4243ef00636 | -15.51631 | -42.67409 | 2025-02-04 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 33fa1a3d-4071-3190-8582-e5fc752f9c30 | -20.85864 | -43.94628 | 2025-02-04 04:04:00 | NOAA-21 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8e1818b6-e3d6-3daa-ba9c-dc5519c8c28c | -15.51962 | -42.67464 | 2025-02-04 04:04:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 04b5737d-f06b-3595-863a-c19948f046c7 | -24.94158 | -52.36036 | 2025-02-04 04:06:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7c533a9-cdfb-35d1-afae-6619bebfa1fc | -21.29694 | -55.90432 | 2025-02-04 04:06:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43d7cb01-4cb7-3b5a-8993-e288551abddc | -22.69832 | -43.34746 | 2025-02-04 04:06:00 | NOAA-21 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6bbf565-8676-32f3-ac94-b96db2c7a645 | -21.07368 | -56.39567 | 2025-02-04 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09eec241-e583-3c86-89d2-6e61d843c431 | -21.07276 | -56.39427 | 2025-02-04 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 432ba964-17ea-3bbf-a38a-f5325514cf03 | -27.15679 | -52.84133 | 2025-02-04 04:08:00 | NOAA-21 | CAXAMBU DO SUL | SANTA CATARINA | Brasil | 4204103 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 24635247-c4c2-35eb-97c8-107074876dc0 | -32.52917 | -53.34603 | 2025-02-04 04:08:00 | NOAA-21 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 07ebc73d-3588-3bd3-9b93-dd3e089cfacc | -32.53336 | -53.34731 | 2025-02-04 04:08:00 | NOAA-21 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| a79b4f96-8e43-39bf-98b7-3fef325f90d1 | -27.15974 | -52.84533 | 2025-02-04 04:08:00 | NOAA-21 | GUATAMBÚ | SANTA CATARINA | Brasil | 4206652 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3a8b49be-2f9b-36a5-979b-dc18a72f3557 | -28.66561 | -49.30906 | 2025-02-04 04:08:00 | NOAA-21 | CRICIÚMA | SANTA CATARINA | Brasil | 4204608 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9bceb979-20b2-3a51-ab45-bf2f35d3eedf | -6.9532 | -43.5384 | 2025-02-04 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| a6e265c1-720e-3be5-8f6a-9aa9ad08f41f | -6.9532 | -43.5384 | 2025-02-04 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.4 |
| cffa78c6-24fe-3c98-b6d0-d1e9cd591522 | -6.9689 | -43.56586 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 76768bd8-77b5-39a7-b85f-d6c1cdc9952a | -6.97128 | -43.56771 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 824e63a0-f6b8-3515-8a17-a1e52901dccb | -6.96472 | -43.56251 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7f6457a2-c07d-3dde-8c3c-73acd42514e9 | -6.94799 | -43.55149 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1409f2ea-3003-3658-88f2-476bf290204d | -5.13515 | -37.59619 | 2025-02-04 04:25:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0bf29ee6-7398-3089-9ec7-49e0d2805c36 | -6.95644 | -43.5444 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7310f26a-3b38-30db-9bf3-ac7eb7d0b9ab | -6.94862 | -43.54739 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff92b469-4eaa-3a66-b3cf-b009aaf1948f | -6.96829 | -43.56998 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bae8b4ea-16c1-3fca-8722-c73a1eded2ea | -6.96112 | -43.56197 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d80ca663-6f12-30b1-b476-256760eb2a1b | -6.96049 | -43.56608 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2c0aa7d-aee6-3d4b-a993-1f18c974c3b1 | -6.9541 | -43.53564 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b233d217-a087-3d36-aa8a-97814627ccd1 | -6.95582 | -43.5485 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faf18dbd-18ab-3f38-ad7c-192d01dd1663 | -6.94502 | -43.54684 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba17c674-a372-3e43-8103-0c0dd1a2fe14 | -6.9469 | -43.5345 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a65ddae7-1c45-31a2-a5e1-927f51ff0612 | -6.96408 | -43.56663 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3c94332b-fc27-3cc5-afcd-bd47673151be | -6.96705 | -43.57128 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cac59b3b-2fae-39fe-8eda-145beea2b65d | -6.95159 | -43.55206 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 334fc20a-4033-3916-b528-9c5e7fb46336 | -6.94628 | -43.53861 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76f2b3c1-1963-3edd-8d3f-3ecc8839f285 | -6.95285 | -43.54383 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f315fe49-b35c-3ce6-97c1-bb11cee93d5b | -6.96768 | -43.56717 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b5e5f401-32eb-369d-9dbd-5cca598c1ddd | -6.9653 | -43.56531 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9fbbb066-3211-3ffd-8e1e-608c85b7fb99 | -6.9613 | -43.53674 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 475ab4f0-3ea2-3f9d-a879-667831225433 | -6.95941 | -43.54906 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e12696e2-1214-3db1-b57b-9eda4564ead1 | -6.95222 | -43.54794 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a97cb01-2ae3-38d6-9046-9371c279055e | -6.96194 | -43.53261 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3093f25e-8dd2-311b-802b-869c660ba28d | -6.94987 | -43.53917 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bd7036b3-7789-3490-a76d-8ad49b7be2e8 | -6.95833 | -43.53206 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c86a65ee-9ae4-37d8-8a34-703579531751 | -6.96345 | -43.57074 | 2025-02-04 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2476be1c-b026-325f-985f-f16d2a0ce903 | -6.96409 | -43.57353 | 2025-02-04 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ef6afc4-ee66-3a6b-ba7e-9fe8fb8b32ba | -6.96469 | -43.56944 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6cf845f-e90b-39c7-a70d-00d54d04ecdf | -6.95707 | -43.5403 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5785ea39-1e36-3866-8610-0af9cc0437c1 | -6.95113 | -43.53096 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 21e382a3-9a30-3274-9e42-8eada1a9b4ae | -6.9505 | -43.53507 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b2560ae3-5886-3bfd-84a7-94b5c81a3faa | -6.95347 | -43.53974 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e5e5b3fe-33d2-3718-8c07-660d2b272d2f | -6.96067 | -43.54086 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 977291be-5673-309b-97d7-cbf3b22b7a54 | -6.96364 | -43.54552 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cd298aa-77e0-3d17-b0f2-f899c73bd147 | -6.95473 | -43.53152 | 2025-02-04 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README3.md)
