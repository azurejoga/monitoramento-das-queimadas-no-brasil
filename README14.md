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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5621cb24-d733-371b-af5c-a4beda32fd90 | -3.92434 | -38.6572 | 2024-12-12 04:14:00 | NOAA-21 | MARACANAÚ | CEARÁ | Brasil | 2307650 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| d8bb87de-4ac8-31ac-9bb6-d53fd95c928d | -6.12568 | -42.54107 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9a4ae657-bdbd-3297-817d-9e3a405f0bf1 | -6.129 | -42.54158 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 797cb5b9-51e9-3bde-b90d-abef6f2f6dfa | -3.85251 | -40.45321 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6fc22fa2-ead5-3b42-9853-e9fb9cb77a61 | -6.14298 | -43.91224 | 2024-12-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fb15cfb-9b2c-3ea9-a368-f88908fa9d9c | -4.01158 | -46.64803 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4668f942-4e3e-3678-b749-c9895feea6d9 | -4.20806 | -50.66065 | 2024-12-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d2a9949-a1f0-3123-887e-14d32a8d9d88 | -4.02296 | -47.03101 | 2024-12-12 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 38a9e612-af52-38f3-a76e-a4bf3a5685e6 | -4.83278 | -44.21614 | 2024-12-12 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bcc9fe25-2b8b-3b63-910c-351627c60387 | -2.57099 | -51.88488 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d290b22b-a3ea-3576-995a-2a36bbeaadfa | -3.83147 | -41.5688 | 2024-12-12 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 676d96cf-f62d-304c-98c6-75fc160df7dc | -4.19081 | -42.43059 | 2024-12-12 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7117f937-b941-3287-ae87-5fbc6a3666d3 | -4.03391 | -46.89536 | 2024-12-12 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f20f30c8-ccd1-3362-b306-22d82e97d08f | -5.10386 | -37.59959 | 2024-12-12 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fb42680e-86be-3aa3-aa91-02d7ae99537f | -4.3759 | -48.08093 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03dd0c9d-e529-3f9b-b54c-7d6ff66f573a | -3.46069 | -42.29193 | 2024-12-12 04:14:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7b4a4a05-51aa-3b09-8fda-be79d851125d | -5.30297 | -43.28292 | 2024-12-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5230e001-9aa2-3a37-bd22-e4f973e5bbf9 | -4.18473 | -42.42612 | 2024-12-12 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 003fdd73-4a93-3dff-990d-7bdf5960fd17 | -3.99401 | -46.50891 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18ea7b0f-ec54-38c7-a525-bd1834cc08f7 | -3.99685 | -46.9566 | 2024-12-12 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86a12131-8686-318e-bbb8-d03de71501f3 | -4.20517 | -47.79198 | 2024-12-12 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e35baf3e-f526-35fc-9b1f-283360d07f91 | -5.70109 | -46.33806 | 2024-12-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3093f960-72d1-3fca-9e8a-79c6a876759a | -4.56973 | -48.47391 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1c68533e-28d2-3ee6-8465-05e9d556e90a | -4.07712 | -46.12634 | 2024-12-12 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d87346f-fb1c-39d4-9472-a01b8000137d | -4.08793 | -46.61188 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 40e1af07-a1d8-385d-b821-6b4ada744b45 | -4.17182 | -48.75764 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9bf1e21-3a38-330c-9896-503873ee2b23 | -4.36516 | -48.21935 | 2024-12-12 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b906bd6f-8d56-3c14-83b2-a9c86dc8cf8b | -4.2539 | -47.58286 | 2024-12-12 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2c07092-0992-3401-93d3-bd603af00902 | -6.53366 | -39.28447 | 2024-12-12 04:14:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 166e2c7b-cf0d-33fa-9d2d-3656eb9b3c83 | -5.30627 | -43.28344 | 2024-12-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3eb8e135-2642-348c-b02e-761982eb4d40 | -5.30376 | -45.27107 | 2024-12-12 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ecc0ef3-d555-3419-be63-d2eb60036d69 | -4.05514 | -46.6639 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9062ab6-784d-3f65-aa32-7d94ad8d2961 | -4.85102 | -42.495 | 2024-12-12 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 430d2be3-47bd-3790-8050-245b676eeb24 | -3.98673 | -48.39791 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc4d737c-d0f0-3b90-b469-fc62ec88dd7a | -2.71098 | -47.55678 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b286ecb5-f5ea-3b83-8eaf-cf3c4db4f5e0 | -2.6713 | -44.29326 | 2024-12-12 04:14:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f1585668-08ee-3ba0-b94b-6b3e3eb6e539 | -3.75713 | -38.93945 | 2024-12-12 04:14:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8c4b830a-bb58-3be3-871f-13b72351254f | -4.01531 | -47.02971 | 2024-12-12 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 064a83d2-0323-36c2-8ba9-9ef33c1180aa | -4.80246 | -50.81918 | 2024-12-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55323978-09a9-31b3-bcdd-71c24fbb3c40 | -5.15924 | -44.36949 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71598a69-1166-3181-ab98-534eab21ab19 | -5.29418 | -48.31386 | 2024-12-12 04:14:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9a1628e-3365-351c-aa8c-090642875f58 | -5.30351 | -43.27948 | 2024-12-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b657bd2f-27f1-3c88-8187-f8c8a897eb22 | -6.28847 | -43.85311 | 2024-12-12 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35b66931-fc38-3563-9c5e-7bc14b0bd49c | -5.97408 | -42.68508 | 2024-12-12 04:14:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b69f060-a5c3-399a-a1d9-2c2cadc423ec | -3.84963 | -40.44888 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c67aa3b5-05b8-3d07-bd14-d55aa3e8eebd | -4.15058 | -46.29817 | 2024-12-12 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 976a4b53-ecf9-3093-b529-cb1d6080eb54 | -6.05636 | -44.05211 | 2024-12-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc6e36fe-b6f4-3be1-9fdb-150627e9962a | -6.4171 | -39.65391 | 2024-12-12 04:14:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20876f5e-0da3-3bfc-91a5-e4c648e0e3f3 | -2.58141 | -51.92254 | 2024-12-12 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd07ec11-f117-3b9c-a3c5-5fcaa8602b1f | -5.15588 | -44.36898 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d23a3c1-610d-3cdb-8cd5-757ff5b5ee11 | -2.3394 | -45.22765 | 2024-12-12 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 086a0a8c-4af1-3d05-8216-3fbc9e960cc9 | -4.17246 | -48.75368 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdd0457e-de1b-38d0-8ea1-b88cadede341 | -3.89642 | -42.55375 | 2024-12-12 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad8f1a75-7088-3fc7-b09c-393e7afb5e90 | -3.81748 | -44.12275 | 2024-12-12 04:14:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72ee8ffe-4078-37da-83ae-98bb8721589a | -2.58865 | -47.48724 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f95cbd6-9f3e-3952-a25f-c5ed60b5052a | -5.1726 | -44.43762 | 2024-12-12 04:14:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e44ddb05-f01b-36b7-829d-6d5f419a6d49 | -4.49575 | -46.10698 | 2024-12-12 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a779158b-cc2b-3ba2-a00f-3102e924e408 | -3.24516 | -46.8772 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 1c72932e-13a3-3ed2-a924-b6dae37b74bc | -3.99303 | -46.95601 | 2024-12-12 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a79bd4a9-3324-33b5-9813-be13a4bce76b | -5.30681 | -43.27999 | 2024-12-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2786f6a6-d36e-30d8-8624-9fa749b7ddd3 | -1.87369 | -54.6881 | 2024-12-12 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6408512f-eff7-3f62-ae6f-fd91e9d0e71e | -7.10811 | -39.08038 | 2024-12-12 04:14:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cd56bc32-6940-37dc-bf0c-cc22a5a047f8 | -4.09055 | -46.60969 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 191ae181-c518-35ca-aa48-d64f86c917b6 | -2.04458 | -45.44096 | 2024-12-12 04:14:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36cc679f-107e-33e8-947e-74cbc9fee19a | -2.52924 | -51.78932 | 2024-12-12 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 568c3cb1-e362-34bd-a4c9-51066b80e4f7 | -6.29233 | -43.85016 | 2024-12-12 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8abea123-ff91-3331-bd27-0044e0b92422 | -3.21317 | -42.70405 | 2024-12-12 04:14:00 | NOAA-21 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91d29115-4a70-39f0-9501-3dc10a21b84a | -4.90245 | -42.0757 | 2024-12-12 04:14:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 594ea7b4-6eb5-3920-8caf-8471c7d46bfe | -3.21023 | -53.00872 | 2024-12-12 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31f905e6-7de9-312a-9d4f-4b997ca71b33 | -4.08279 | -46.66661 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e0c0ff3-e549-3a5c-a0f1-06f447fa9c82 | -2.99383 | -48.07759 | 2024-12-12 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e4b5b1d4-90c5-3c5d-8954-f3b620d4a758 | -4.54781 | -43.56398 | 2024-12-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 58f5449c-97c7-34ca-bb61-c2741701e638 | -3.78602 | -47.10111 | 2024-12-12 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b7465ad-acbd-30da-9869-8ecfcad43561 | -3.8531 | -40.44941 | 2024-12-12 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 7dae47ed-2664-34fd-9aa6-125a666999d8 | -4.04397 | -43.34942 | 2024-12-12 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f6120ff7-b20e-35e5-bff6-7d9ecf62a782 | -5.10331 | -37.60332 | 2024-12-12 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1fae0375-e29a-353e-8b0b-e79b689ae430 | -5.59608 | -41.38487 | 2024-12-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 4996883b-1b8b-33ab-89be-e3699a263ae3 | -4.02854 | -46.8801 | 2024-12-12 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af4a2a41-b3d0-3ed7-8c57-9260b1899bb8 | -6.0419 | -42.1585 | 2024-12-12 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f0e5a5ad-2cbc-311d-b180-864719b4803c | -4.90632 | -42.07272 | 2024-12-12 04:14:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5cbb0bbd-23e6-3d7f-baaa-a4e0d35f188f | -5.51477 | -46.25861 | 2024-12-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fde1f78d-4f21-382e-8ca9-33a68ba7ac93 | -5.85263 | -39.04686 | 2024-12-12 04:14:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| db4e9997-4112-3d7d-ad67-37b39977a922 | -2.7903 | -47.63529 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b2ea966-6b4a-38f7-8226-b0bd1ceb3cd2 | -3.21091 | -53.00465 | 2024-12-12 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4789060d-4526-348b-8d8a-4fc4b2543ade | -4.03086 | -46.89005 | 2024-12-12 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7a3ed34-9ad9-3054-baf6-6f7a54d80ef4 | -4.13387 | -46.70731 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a9a92452-95eb-36e7-aa86-cf03a194ccf9 | -3.78455 | -47.09856 | 2024-12-12 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 864a476f-5361-325c-94f8-7bb31bf9826b | -5.34353 | -42.12281 | 2024-12-12 04:14:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d985ebe5-ad21-3b7e-b4d2-eb25a00f6c8d | -4.48601 | -46.71205 | 2024-12-12 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd94734a-d3f9-314a-b32b-1ae36cafaaf3 | -4.09166 | -46.61251 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3500ed9-d638-31a8-90fe-1d7f5255b0f7 | -6.12622 | -42.53757 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| bf94eb01-241f-3cf6-819f-6cb89d7f2874 | -2.27317 | -53.48457 | 2024-12-12 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2fc9563b-da0f-3802-80c7-ffc687fca39d | -5.90596 | -44.01383 | 2024-12-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a94bc0d5-b118-3a95-8b40-ba27047ea59a | -4.18527 | -42.42267 | 2024-12-12 04:14:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 04de8828-2d49-31a2-9c6a-86812c8c2abc | -4.0376 | -46.74995 | 2024-12-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46421bd0-e2d2-3015-9302-c5d4d5df929a | -4.18619 | -49.28263 | 2024-12-12 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72441467-9b00-3b2a-862d-7b131bbea746 | -2.92247 | -41.4685 | 2024-12-12 04:14:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39fd9b02-f75e-3c87-82e8-c8d8c3e5bca3 | -6.12845 | -42.54507 | 2024-12-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 73bf0967-e8e5-34b4-baa3-e8514d8a2a8c | -3.24441 | -46.88187 | 2024-12-12 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 52e70a1b-3806-303c-9d60-eec38cd70114 | -5.26417 | -44.77433 | 2024-12-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README15.md)
