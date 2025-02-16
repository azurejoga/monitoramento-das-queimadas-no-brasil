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
| 5a46e094-75d5-39e1-96b8-f9b44832f639 | -20.9207 | -56.5392 | 2025-02-16 00:00:00 | GOES-16 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 19394529-6a5f-3ac7-8e8b-20dbf848b543 | -20.9207 | -56.5392 | 2025-02-16 00:10:00 | GOES-16 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 606308c3-aa77-32f8-8873-eca070286444 | -6.8476 | -35.044 | 2025-02-16 00:10:00 | GOES-16 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 61.4 |
| 86ec6d96-285c-3482-b70b-461dfbd0ed0b | -20.9207 | -56.5392 | 2025-02-16 00:20:00 | GOES-16 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 26b53f7f-eb19-3b12-b233-5f25befaad2d | -20.9207 | -56.5392 | 2025-02-16 00:30:00 | GOES-16 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3af04760-a1ed-38da-b169-985b0907b6a3 | -21.45501 | -43.81363 | 2025-02-16 00:45:00 | TERRA_M-M | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 90af0792-1b0f-3592-8a0a-4eb3044d51d2 | -15.56174 | -46.27845 | 2025-02-16 00:47:00 | TERRA_M-M | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b8bd484c-b377-3dcc-b802-6532fcf8dff1 | -14.23428 | -41.59812 | 2025-02-16 00:47:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 0fd7dfed-93ba-33ce-9198-32efdf88c558 | -15.6769 | -42.43229 | 2025-02-16 00:47:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| aafb2f72-8caa-3da7-ab44-07a9cf361310 | -16.34519 | -45.69395 | 2025-02-16 00:47:00 | TERRA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 19.2 |
| de6b15f0-e714-3c44-bf9b-3fd231fb573e | -20.55968 | -43.80943 | 2025-02-16 00:47:00 | TERRA_M-M | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.9 |
| 359d5ebf-d10e-393b-b72d-530416d61e27 | -20.54892 | -43.80082 | 2025-02-16 00:47:00 | TERRA_M-M | CONSELHEIRO LAFAIETE | MINAS GERAIS | Brasil | 3118304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| efafb4ba-452e-330f-9202-0579af1c5a48 | -16.79838 | -42.51427 | 2025-02-16 00:47:00 | TERRA_M-M | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 583a25fe-bf0a-3933-bb35-e06fdc25e73c | -15.67921 | -42.44645 | 2025-02-16 00:47:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 71568b22-affe-380f-993d-22176bc48880 | -17.72746 | -46.5468 | 2025-02-16 00:47:00 | TERRA_M-M | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e0c2b275-57a5-3a10-ab4e-79e9a751477e | -20.91504 | -56.57591 | 2025-02-16 00:47:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f450de55-9048-39e6-9ec0-824802dd8618 | -15.83362 | -42.62649 | 2025-02-16 00:47:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| fcc748ac-92b3-364e-bb4c-05933f030df8 | -14.22842 | -41.60489 | 2025-02-16 00:47:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 21.0 |
| fc397f68-f111-3907-b521-e6ebbcc1cfc2 | -13.30374 | -44.29374 | 2025-02-16 00:49:00 | TERRA_M-M | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 89a17c79-293f-396c-af77-a1ec68b345d8 | -20.9207 | -56.5392 | 2025-02-16 00:50:00 | GOES-16 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 35738ffe-326d-3468-bf76-85eaf657deb6 | -20.9207 | -56.5392 | 2025-02-16 01:00:00 | GOES-16 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| def3a43e-a02b-34d1-b65c-1c2021e6a701 | -16.8101 | -42.5146 | 2025-02-16 01:50:00 | GOES-16 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 78.7 |
| f7f927b4-66d4-3d10-a283-4005e16a3452 | -16.8101 | -42.5146 | 2025-02-16 02:00:00 | GOES-16 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 77.5 |
| f71a4428-e62d-3d16-9079-83b783d4a7dc | -5.63352 | -39.77061 | 2025-02-16 03:36:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| dd6a2e27-3535-3227-b820-111f5078a90f | -6.74681 | -38.74624 | 2025-02-16 03:36:00 | NOAA-21 | BAIXIO | CEARÁ | Brasil | 2301802 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9f1856b7-7997-3797-8039-4d24896385a8 | -7.22517 | -35.78701 | 2025-02-16 03:36:00 | NOAA-21 | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e964fe5-3adb-37d8-a530-e28198119012 | -5.61574 | -35.68259 | 2025-02-16 03:36:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd6e9b2a-6223-35e8-b70d-24a92993b9b5 | -5.70651 | -38.41266 | 2025-02-16 03:36:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9748a1a-f9be-32fd-865e-04a27ac0f298 | -6.91022 | -37.86495 | 2025-02-16 03:36:00 | NOAA-21 | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 40f1e218-bbc2-37bb-8a9f-288f2ed328b7 | -10.69634 | -37.04988 | 2025-02-16 03:36:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d2f9089-0e18-3c5a-8350-fb1fdc9199f7 | -8.40351 | -37.0366 | 2025-02-16 03:36:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 712912da-e403-37b1-a9ad-575423e91e6d | -9.87721 | -41.80537 | 2025-02-16 03:36:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7296d0d0-1297-3d29-bef3-7e41151946ed | -9.49926 | -42.9917 | 2025-02-16 03:36:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 15445a40-d00e-3d83-8962-71bc69175f42 | -10.73577 | -37.6055 | 2025-02-16 03:36:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7670f2ca-aaa6-34d7-a332-7c620ce2bd21 | -10.73148 | -37.60926 | 2025-02-16 03:36:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6a879d69-727c-3765-9b08-b50085e7b5bd | -10.73433 | -37.61426 | 2025-02-16 03:36:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 96521e85-37a8-363a-9308-770a54b321c9 | -8.40705 | -37.03732 | 2025-02-16 03:36:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b94206b5-c393-38c7-97e4-279ae5ff7025 | -10.74006 | -37.60176 | 2025-02-16 03:36:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff84a875-0d64-33f9-a17c-18a530d2ad1f | -10.73505 | -37.6099 | 2025-02-16 03:36:00 | NOAA-21 | SÃO DOMINGOS | SERGIPE | Brasil | 2806800 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3bbf4887-2203-3397-b35d-9f9f8204a72c | -17.30846 | -39.25175 | 2025-02-16 03:38:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 20f55dba-c427-34f4-bed1-65c304ca1733 | -15.87088 | -38.94402 | 2025-02-16 03:38:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7528233e-0abe-3186-8dfd-88fd28bd3690 | -17.11782 | -39.50798 | 2025-02-16 03:38:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c987f9dc-9d72-31a5-8e27-b9077a73296c | -14.47958 | -45.82145 | 2025-02-16 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4b477f6e-c64f-3b91-bb8e-71d8520b5b85 | -14.23007 | -41.60192 | 2025-02-16 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f1703e0e-6dff-3e66-9430-057a6e699726 | -12.86357 | -38.36856 | 2025-02-16 03:38:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 21291cdb-3b99-3c02-ac5f-9b8842711946 | -16.79989 | -42.51237 | 2025-02-16 03:38:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 077d2f3b-1735-3cc7-b1d7-b8298d9c7b8b | -15.68276 | -42.43708 | 2025-02-16 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 679b54d6-6f1d-3573-b07d-40130604bd52 | -14.47699 | -45.82054 | 2025-02-16 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1145b217-82b9-3d07-baf9-3040a103b967 | -11.70294 | -37.532 | 2025-02-16 03:38:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 20bb197b-349a-3b22-8df1-131c2df0e312 | -15.46382 | -42.14831 | 2025-02-16 03:38:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77db5d20-f4f8-3e8b-ab5b-59815858cdda | -15.82851 | -42.62725 | 2025-02-16 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 054b9c49-ccf4-34c8-b806-410f69caed1f | -18.12023 | -39.69242 | 2025-02-16 03:38:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 316cc198-759a-311f-b63a-738979662809 | -14.47617 | -45.82446 | 2025-02-16 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4990409-5e61-3d27-8c08-0e58118ef702 | -14.13565 | -41.69242 | 2025-02-16 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9a7f62c0-c6f1-3327-9f26-de9858b3afc1 | -10.33168 | -41.80077 | 2025-02-16 03:38:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e84d18b6-5170-3d82-bcd9-8096d0bc1f6e | -12.03987 | -43.83215 | 2025-02-16 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9c9a8ac-91b7-3a31-9db6-ed5261795544 | -14.23433 | -41.60289 | 2025-02-16 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e9aae5f4-5241-3c2b-8182-8d0c01fd9487 | -16.8078 | -42.51825 | 2025-02-16 03:38:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6be6baf-3352-3fd6-937b-6e822e67cb09 | -15.68193 | -42.44158 | 2025-02-16 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da1762f3-0fc7-3640-b06b-fb52b8764ff6 | -15.68215 | -42.43619 | 2025-02-16 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c0cff8b-29f3-3933-9081-bcc9bc0de8b9 | -17.67454 | -42.7417 | 2025-02-16 03:38:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7bfc07ef-9d00-3376-bdbf-14409a13618d | -16.81215 | -42.51915 | 2025-02-16 03:38:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3d59c06-9685-31a7-9455-ac91f873a26f | -16.86828 | -40.79337 | 2025-02-16 03:38:00 | NOAA-21 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 176a14a0-ece7-31bf-bdbf-71a88aae8afb | -16.80428 | -42.51303 | 2025-02-16 03:38:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84486a53-a520-3372-a2f3-b0bebcbb5966 | -15.82939 | -42.6226 | 2025-02-16 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 3537d9f1-a6b4-3a23-ae00-df4f596f52db | -16.86812 | -40.61192 | 2025-02-16 03:38:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1fb8d5d4-f354-3495-b90c-36d4a659f720 | -15.36556 | -43.16809 | 2025-02-16 03:38:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3df1e58e-906d-329f-8a6c-48498e67e0f3 | -17.73633 | -39.52512 | 2025-02-16 03:38:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3c24f159-4ab7-3c5b-b365-432783cf5e85 | -15.86801 | -38.9391 | 2025-02-16 03:38:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8227cc96-ee6b-38a3-9096-417fdfac74c0 | -17.095 | -43.80533 | 2025-02-16 03:38:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a115c61-be56-34c6-a803-4e83aa758039 | -12.44061 | -38.15911 | 2025-02-16 03:38:00 | NOAA-21 | MATA DE SÃO JOÃO | BAHIA | Brasil | 2921005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e14c6895-6c1c-32cb-aee3-f58e8dc97dea | -14.47397 | -45.82025 | 2025-02-16 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f344d757-519a-352f-9aca-80eb64c29665 | -14.22662 | -41.59655 | 2025-02-16 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5508bc17-354b-388d-a487-5b47dc06f03c | -14.2258 | -41.60096 | 2025-02-16 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d94de7df-cdd5-328e-80ac-a3d3103feedc | -16.34846 | -43.69455 | 2025-02-16 03:38:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3a1c32b-5925-3bb8-814b-ae7b6b239893 | -11.70228 | -37.53603 | 2025-02-16 03:38:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c9e92acc-9ba1-30e9-85da-5ac450adcd1c | -10.47336 | -42.46409 | 2025-02-16 03:38:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 3481ffa0-d3ef-37e7-b0a1-5a2a4330e393 | -17.73835 | -39.52714 | 2025-02-16 03:38:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0f6ddba7-d1e9-3778-a4f3-2845de216905 | -12.03827 | -43.83418 | 2025-02-16 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70ef94d4-c9a0-3399-9ef4-55630577f809 | -15.68129 | -42.44068 | 2025-02-16 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af27ffdd-c6f9-3adf-8964-70e35d77d2bf | -21.10765 | -40.91827 | 2025-02-16 03:40:00 | NOAA-21 | MARATAÍZES | ESPÍRITO SANTO | Brasil | 3203320 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9a80d9ef-f47a-30f4-876d-6724286e833c | -19.71753 | -40.35229 | 2025-02-16 03:40:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| de3826a5-2eff-32d1-a646-f66cc74f97c4 | -22.90398 | -43.75456 | 2025-02-16 03:40:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 6d6f5335-843e-30ac-acfc-a23a62f001f3 | -20.35928 | -40.88935 | 2025-02-16 03:40:00 | NOAA-21 | DOMINGOS MARTINS | ESPÍRITO SANTO | Brasil | 3201902 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| da11a6a2-ebe5-36e8-9b6e-2ed8d77f68a4 | -22.58907 | -43.64083 | 2025-02-16 03:40:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8dc84eb2-4091-3929-a54f-6da7d16e3d9b | -19.83708 | -40.0833 | 2025-02-16 03:40:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 02c41c94-377e-3090-80cb-39bced0fd217 | -22.8568 | -42.98194 | 2025-02-16 03:40:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2dfc8ead-1328-3895-b0cf-6343f6f75dd4 | -22.78482 | -43.75848 | 2025-02-16 03:40:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bca1b196-4415-349f-bd2f-286767388463 | -22.67859 | -42.85598 | 2025-02-16 03:40:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d41b103d-eb9b-3c25-8db5-a1126e165095 | -18.7457 | -40.44183 | 2025-02-16 03:40:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b9e1472e-342f-3421-ae5e-07f1dd0a8ef1 | -20.89842 | -44.21352 | 2025-02-16 03:40:00 | NOAA-21 | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0c201e69-cc10-3083-9dce-4b84c70e213c | -22.67387 | -42.85886 | 2025-02-16 03:40:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 345e6b51-7350-3703-9a77-75baed0e0045 | -19.80724 | -40.33507 | 2025-02-16 03:40:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 32d2415a-e8d6-3a2d-b741-dae6134968e7 | -18.52279 | -39.9316 | 2025-02-16 03:40:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 30.1 |
| 13923931-4d4b-3b1d-8a15-1b222f43bcd8 | -3.23703 | -42.07845 | 2025-02-16 03:59:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 70001259-96da-3c27-b410-16736f47aa64 | -3.23596 | -42.07697 | 2025-02-16 03:59:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4c5a315-5ca3-3b20-a4b2-325397805d32 | -3.00185 | -39.89665 | 2025-02-16 03:59:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b51e3fac-e8f2-39a5-8757-eea1c2a2056a | -3.2395 | -42.07755 | 2025-02-16 03:59:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c860840-ad85-3bd1-8af0-9cad240f6db8 | -7.22416 | -35.78789 | 2025-02-16 04:01:00 | NPP-375D | MASSARANDUBA | PARAÍBA | Brasil | 2509206 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dd76f9f3-b7c1-3fbb-b7cf-b677c09351e5 | -9.49887 | -42.99055 | 2025-02-16 04:01:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README2.md)
