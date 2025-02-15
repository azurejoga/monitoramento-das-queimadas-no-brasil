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
| ce5d5495-e605-3bb4-8469-f7e95ebefbe1 | -10.6 | -45.1158 | 2025-02-15 00:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| c9900f8f-9536-3219-910d-cf1233cabdf6 | -10.6195 | -45.0902 | 2025-02-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 14ed1023-6856-3d38-911e-c20dc0b3eedf | -10.6191 | -45.1132 | 2025-02-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 5240a099-2282-37f0-931f-811aa9848a6d | -10.6004 | -45.0928 | 2025-02-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 5b02adce-2fd8-30e0-be06-8e21cbf7be14 | -10.6 | -45.1158 | 2025-02-15 00:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.2 |
| ca51af93-45fb-3781-b838-c35d63059740 | -10.6195 | -45.0902 | 2025-02-15 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 22220429-e3f8-3f8b-875a-c774c86f06ac | -10.6191 | -45.1132 | 2025-02-15 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 0a0080ef-f53d-3cf1-8ed1-f8b5172127e5 | -10.6 | -45.1158 | 2025-02-15 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| eb4a2685-0e64-3e30-b27a-e11d283eb269 | -10.6004 | -45.0928 | 2025-02-15 01:00:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9fdc113a-81c8-3b8f-9cc5-a509fa28cf26 | -21.774599 | -57.499001 | 2025-02-15 01:02:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 420b5b0b-4d62-3198-8272-41ed35de1c0a | -14.459 | -45.836201 | 2025-02-15 01:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7b3b818e-a530-32b4-a006-e66750841099 | -14.4493 | -45.838799 | 2025-02-15 01:02:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17205b71-6707-3fb2-95e7-78f5eed72218 | -15.0122 | -43.4114 | 2025-02-15 01:02:00 | METOP-C | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 4c274685-830a-32f7-88b8-c48b378e03a2 | -15.0068 | -43.3918 | 2025-02-15 01:02:00 | METOP-C | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| c10fdc6c-7008-3931-ba60-5339c0db9f0c | -14.4201 | -45.846699 | 2025-02-15 01:04:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b164416c-5230-3a3b-b409-0f173f73784d | -14.4298 | -45.844101 | 2025-02-15 01:04:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ac2fbc92-4788-34d3-817d-2b560820fb06 | -14.978 | -43.400002 | 2025-02-15 01:04:00 | METOP-C | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3ea7fb0f-15a8-3522-a854-496aaa65f693 | -21.7453 | -57.504902 | 2025-02-15 01:04:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 32cc31a7-6bfc-3725-b520-0654db1c1925 | -14.9833 | -43.419701 | 2025-02-15 01:04:00 | METOP-C | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| c1cddefe-eb55-3d52-959a-978cc8f871a0 | -10.6195 | -45.0902 | 2025-02-15 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 5ebc63c0-63a2-3fd3-ab4a-c7d28a4b4533 | -10.6004 | -45.0928 | 2025-02-15 01:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 53ccbb25-ec46-3d7f-a586-2ba6e26d041b | -10.6195 | -45.0902 | 2025-02-15 01:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 226a5042-d86e-3804-83ae-675fe7e93573 | -10.6195 | -45.0902 | 2025-02-15 01:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8174a934-8157-3acb-85fb-06094433f031 | -10.6004 | -45.0928 | 2025-02-15 01:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 9b8ecb47-e326-323a-b518-bb95a89cc0a9 | -10.6191 | -45.1132 | 2025-02-15 01:40:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.3 |
| f43c745f-8251-3e21-9f5b-f3e281dc7eca | -21.79507 | -57.49098 | 2025-02-15 01:45:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 33b4254c-a4cd-35d7-a608-ece15dbf0526 | -10.6195 | -45.0902 | 2025-02-15 01:50:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| a191aeab-e11e-3d02-a038-15be606fa4dc | -10.1384 | -36.4921 | 2025-02-15 02:00:00 | GOES-16 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 79.9 |
| 98647d60-bac2-30ce-8506-4403ae494015 | -10.6195 | -45.0902 | 2025-02-15 02:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 5ee9ad0a-4da4-3a11-8ef1-09be42ff684f | -10.6191 | -45.1132 | 2025-02-15 02:10:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| d80f9283-f544-3b5a-b953-993ec0696a1b | -10.6195 | -45.0902 | 2025-02-15 02:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fdf74e92-a5ec-3145-a35a-a218b3b5c133 | -10.6191 | -45.1132 | 2025-02-15 02:20:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 078049d0-84f4-38c9-b728-43505dbbdb80 | -10.6195 | -45.0902 | 2025-02-15 02:30:00 | GOES-16 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 26484187-7d46-3145-8c16-b39fc9c721b9 | -9.90883 | -38.10615 | 2025-02-15 03:04:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 4ccb7165-3146-30f0-a3d1-a66e3b499203 | -10.29087 | -36.77577 | 2025-02-15 03:04:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b98d5baf-448b-351a-af72-ad969fd97904 | -9.90786 | -38.11109 | 2025-02-15 03:04:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9f9ef7df-29da-300f-a0cd-c16035797c45 | -10.29645 | -36.77718 | 2025-02-15 03:04:00 | NOAA-20 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 76f7075f-859d-3716-8bb2-054c2a764f01 | -15.46212 | -42.15059 | 2025-02-15 03:06:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b884cb9c-e77c-3a9c-a07c-79c8528b6da4 | -15.46528 | -42.15204 | 2025-02-15 03:06:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b947e58-a6b5-3fe2-a262-2e409483848b | -19.82448 | -40.10568 | 2025-02-15 03:06:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9a03ccad-7984-311e-ac7c-9312da775ed7 | -19.82547 | -40.10133 | 2025-02-15 03:06:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 16235f26-9763-314a-9729-5399e93d753c | -15.46689 | -42.14488 | 2025-02-15 03:06:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89f9c7bf-1f0d-3bbf-8a11-02dcab0236b9 | -15.46374 | -42.14357 | 2025-02-15 03:06:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a17f7e9f-c7be-3698-8e5c-6ab9ddcc6533 | -19.82594 | -40.10356 | 2025-02-15 03:06:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4aaee651-271b-31df-8608-7d93783836e6 | -4.64086 | -37.97859 | 2025-02-15 03:53:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e3efe195-64f6-3b61-8c06-db3de3a65f37 | -7.2851 | -39.73049 | 2025-02-15 03:53:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8387a62c-c62b-3d4a-ab57-d975fe145195 | -5.43127 | -38.14945 | 2025-02-15 03:53:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| a6e15d8d-4042-3d0d-abf7-89ce75be8617 | -5.14843 | -35.62677 | 2025-02-15 03:53:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 172b403b-dedb-3e0c-a027-f8a52ccbeb7b | -5.67703 | -39.26877 | 2025-02-15 03:53:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1b6506b6-6e6d-33ba-9dc3-f6843c0de019 | -7.01048 | -37.63957 | 2025-02-15 03:53:00 | NOAA-21 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 73cf8511-124b-3e96-94ca-287cb5fade2e | -5.46063 | -36.90618 | 2025-02-15 03:53:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9e96f1c5-f64b-3358-9719-4f5b2365107b | -7.25362 | -34.94012 | 2025-02-15 03:53:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cfa4d8a1-d068-3085-b8e3-11db1835bc43 | -4.05119 | -38.2664 | 2025-02-15 03:53:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f53b8109-f296-33c6-b8d0-5ad95e527b87 | -5.68037 | -39.26931 | 2025-02-15 03:53:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 90441cff-6da2-3892-9d55-9445eab6b508 | -12.25826 | -38.89231 | 2025-02-15 03:55:00 | NOAA-21 | FEIRA DE SANTANA | BAHIA | Brasil | 2910800 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e6af4f3-995c-3b6b-9d40-731649a8d42e | -14.41713 | -44.47541 | 2025-02-15 03:55:00 | NOAA-21 | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cae9fb8-b0f7-33a6-abd4-19b2178aaea6 | -11.69024 | -43.91679 | 2025-02-15 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7926110f-f97d-3bec-bda1-dd365cf26a5a | -10.78078 | -40.31056 | 2025-02-15 03:55:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b3001a6e-1622-3292-b165-b2f5828667ee | -9.56324 | -35.6932 | 2025-02-15 03:55:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 34e5a5c1-2131-35ca-b10e-b37299ab9b3d | -11.56298 | -44.85311 | 2025-02-15 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a685b60-1580-317e-813c-3ba78b6ba8bf | -11.75379 | -38.52457 | 2025-02-15 03:55:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c0e66b2-4dbe-341a-9133-760dbd7cbdf4 | -9.90675 | -38.10853 | 2025-02-15 03:55:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca5d4eda-5640-37d4-9340-b39b7374ade1 | -13.48297 | -44.02132 | 2025-02-15 03:55:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db782128-dfa8-39c8-967a-ab115bddff4b | -10.60855 | -45.10556 | 2025-02-15 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| dc04d3cf-4762-3373-8dff-eb3dc4825302 | -8.97962 | -40.58393 | 2025-02-15 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7c90329c-6bd5-33fd-bdc8-d4093961a9c5 | -10.61206 | -45.11024 | 2025-02-15 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2eab6d49-b860-3bfd-aece-11b0520e0692 | -9.91062 | -38.10551 | 2025-02-15 03:55:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e46d1926-feb9-3a03-bee4-c9f128a0fd22 | -11.69108 | -43.91194 | 2025-02-15 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7d3edd1-7d6d-316a-9dbd-1f1df927f7f9 | -7.38601 | -42.78664 | 2025-02-15 03:55:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa086446-7299-3f9a-bb6e-0280f9c537f4 | -12.86166 | -38.36722 | 2025-02-15 03:55:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3070fb1b-b3ae-3d1e-b956-06a080b26858 | -7.82256 | -41.37186 | 2025-02-15 03:55:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 443e3e03-5296-31f5-97a6-4d448223bcf4 | -9.90729 | -38.10499 | 2025-02-15 03:55:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9bb29a72-8048-3b7b-8be0-51b4cf772d96 | -12.35408 | -47.99164 | 2025-02-15 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2770e05-0303-3859-a889-60480b6711c3 | -8.87919 | -38.13598 | 2025-02-15 03:55:00 | NOAA-21 | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4a05b45e-23be-366f-9c15-17dcc2340e57 | -11.57432 | -40.60551 | 2025-02-15 03:55:00 | NOAA-21 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1893ae96-93e4-3d8b-9cd5-816ecb1da295 | -11.93943 | -38.15454 | 2025-02-15 03:55:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c62b01b9-3a38-35c0-837a-4a33b22a557e | -8.87865 | -38.13948 | 2025-02-15 03:55:00 | NOAA-21 | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f73cd87-db57-3643-8707-c69c79584f14 | -10.61276 | -45.10632 | 2025-02-15 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dd0fa4e5-444a-31ea-890d-352b88666cb7 | -11.85856 | -37.81088 | 2025-02-15 03:55:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d2e095b7-daa3-3454-927c-c7d2bfc36233 | -14.11944 | -41.679 | 2025-02-15 03:55:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 43720a5d-1003-3f40-ab06-458e8fdd2da9 | -11.69492 | -43.91261 | 2025-02-15 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf7dc3e0-55bb-3475-a734-9ecd026d2542 | -12.84846 | -38.24857 | 2025-02-15 03:55:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 8353f63c-692a-3f1f-a581-5a54514cd460 | -10.64988 | -44.49263 | 2025-02-15 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fa5d8ed-e1db-3d7a-948f-32f5a2fb8ac3 | -10.61345 | -45.1024 | 2025-02-15 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c6304e99-7c9a-377f-8bac-0bda397fb6a7 | -12.85466 | -38.25331 | 2025-02-15 03:55:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c9878005-cacb-3ccc-b27d-444ff78f93e0 | -13.33445 | -39.16848 | 2025-02-15 03:55:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5e780c85-60a4-377b-8f50-bfe46ad65e99 | -12.85184 | -38.2491 | 2025-02-15 03:55:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4a7d1468-0d03-3499-8176-c2b4275ee9ce | -10.29291 | -36.77558 | 2025-02-15 03:55:00 | NOAA-21 | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1a989f8e-45d9-39e1-b64d-b493ad805130 | -11.11074 | -45.11926 | 2025-02-15 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d29be209-01fc-3cd0-a0f6-1b3a463cbb06 | -9.91008 | -38.10905 | 2025-02-15 03:55:00 | NOAA-21 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 91b063c0-1f23-312a-92a7-30c1aa4f57a0 | -9.93983 | -37.46806 | 2025-02-15 03:55:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 358dced4-b021-3680-adfd-a3111c6f682a | -10.19452 | -36.21801 | 2025-02-15 03:55:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0d2c4da5-c285-3e9c-b717-8055e3cfd288 | -12.26473 | -43.42707 | 2025-02-15 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 14745a56-da18-3b9d-910e-b65e15dd1835 | -11.56234 | -44.8568 | 2025-02-15 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 18cd2bcd-0c61-3d85-9315-fd2c66e7ec60 | -10.64647 | -44.48834 | 2025-02-15 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e24327ba-93ca-3288-ad09-d1d2df6d2151 | -14.17868 | -44.36665 | 2025-02-15 03:55:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b7edd21-3571-3e1f-a8df-30d248a98737 | -13.97274 | -38.95007 | 2025-02-15 03:55:00 | NOAA-21 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fe72475d-e13c-3e88-87ea-a4ccd53c32b7 | -11.69623 | -43.92782 | 2025-02-15 03:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 49c4e153-a36f-3405-b3bf-3d2f69a18ab9 | -10.7841 | -40.31111 | 2025-02-15 03:55:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3175bfe-0a3c-3882-995d-f691ab10b9bb | -11.75433 | -38.521 | 2025-02-15 03:55:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
