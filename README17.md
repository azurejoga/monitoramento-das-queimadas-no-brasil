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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fee15ef-58b8-3322-854c-70b34816f9be | -4.00017 | -46.18762 | 2024-11-16 04:01:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97ec103d-9e28-3819-b08e-efe1a9c92a6f | -3.99584 | -45.85428 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1fd83da-cea1-3fed-ab60-590ec8bbc9e8 | -2.77441 | -48.57527 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 65c0973d-b699-3ef9-beb5-5a38a8fe1101 | -6.50657 | -39.70767 | 2024-11-16 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f2814db9-4fa3-3a53-80d5-5934d095aa35 | -4.37418 | -48.0843 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9cf052aa-a438-3d3f-962e-f05c6423c255 | -2.15149 | -46.55869 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 165986c2-1d5a-376f-a5f3-392b00b0b621 | -4.5455 | -42.97414 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bab9f9aa-6c0d-34aa-9ec0-6890b6fd2080 | -3.08322 | -45.60556 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2116fc47-2558-3011-9604-486686876404 | -2.62604 | -46.18876 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd0acd3e-080d-3ebc-95c5-9a1565f86edb | -3.58478 | -44.85128 | 2024-11-16 04:01:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 926b7c66-46e4-3b28-874c-55b96cab4dff | -7.55537 | -35.22701 | 2024-11-16 04:01:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ac159f2f-6b0a-3ff4-b9ba-e6e5a2b5bf3f | -3.56774 | -50.23557 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1afbe1b-558b-32c6-9b3e-5804e3df5c1e | -2.34783 | -47.46646 | 2024-11-16 04:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a11182f9-1cef-3c13-bae7-c32f40b4d2c8 | -3.27266 | -45.50189 | 2024-11-16 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 4b4cb863-0914-3998-9ef1-d0172f80637b | -2.27978 | -47.91639 | 2024-11-16 04:01:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d7cf340-f4f2-3739-a74d-d939147485f8 | -2.18222 | -47.95135 | 2024-11-16 04:01:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0edda8e2-8a91-308e-93b9-cc67464da43c | -2.43685 | -47.042 | 2024-11-16 04:01:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cf95117-aae0-366f-96d3-1fb82017a9a9 | -5.85314 | -38.45475 | 2024-11-16 04:01:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 250ab6df-c4db-3069-891d-4b85e8988663 | -4.13755 | -49.36606 | 2024-11-16 04:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f8683dae-3d53-322a-b8ae-8a445beadab7 | -6.16427 | -39.91939 | 2024-11-16 04:01:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4791641a-5e16-3273-af58-7bfabe747d9f | -4.51789 | -37.8984 | 2024-11-16 04:01:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 68027e0b-427e-35a8-868a-de3473ef988d | -6.97839 | -38.4788 | 2024-11-16 04:01:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 09e12e73-a492-3d40-97c9-4a7407099dd2 | -7.39962 | -40.39411 | 2024-11-16 04:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 8f86d2a8-7384-3636-bae0-e4e286cb330f | -3.9501 | -46.41031 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 781e95e2-1ab2-349b-bef8-6d8c937892de | -4.4063 | -40.69561 | 2024-11-16 04:01:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6fd2cb6b-d665-3778-bf67-abe2297eed57 | -5.448 | -43.33718 | 2024-11-16 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 25542e36-017c-3ace-a5c2-74359b821be1 | -3.76124 | -50.79294 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4bb1911-2aa8-3294-b508-5a99b65e162a | -2.3575 | -47.14477 | 2024-11-16 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 88954b1e-1fbb-36ac-ac60-9950c765e4ef | -6.50272 | -39.71061 | 2024-11-16 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd1ca6c4-7d62-3296-8d1c-6dd66a0cfb63 | -4.00525 | -44.33041 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccd4ca5a-f346-325f-813c-498942e0d3a3 | -4.81385 | -42.91994 | 2024-11-16 04:01:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0534c824-7dc3-3207-af43-6190c6d04ed8 | -3.24978 | -51.52132 | 2024-11-16 04:01:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7557c9db-aa05-35e2-9534-1742a0568c15 | -6.05919 | -39.14878 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab2ff1fb-c57e-3f55-b4d5-e835a3d2a58e | -2.55359 | -46.89581 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2c4d2775-2911-38a1-807f-4c16c6a0528d | -2.77326 | -48.58211 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 235818e6-1b00-3e61-9406-b9d37ed40921 | -4.18909 | -42.38244 | 2024-11-16 04:01:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebf2c375-d77c-3c4f-b333-17627bb83052 | -3.9887 | -43.72286 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3ba71686-b234-3ec9-a267-22ae685a1d52 | -5.00508 | -44.32336 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4b60615-8a6e-3bb2-93c1-cb70cc80df9f | -4.99342 | -44.32147 | 2024-11-16 04:01:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 9002e492-a1e4-348c-80de-46d7e0be2631 | -2.19232 | -46.6063 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9509c98c-19eb-331b-923c-80f6d3dde21b | -3.73428 | -45.65668 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 6e157841-3991-32f7-b2dc-962b29839289 | -4.00177 | -46.49928 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0ea5ccd1-2f7a-39d4-8653-3fa1fbe9be16 | -5.50707 | -39.13526 | 2024-11-16 04:01:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7951df27-c7d4-324e-98fe-93bebd03e8ae | -5.67599 | -35.64542 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 65.1 |
| d4317d2f-0320-31f0-97e8-79861675291f | -3.76817 | -50.78905 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdd33918-a0be-325f-867b-ca009bf28376 | -3.42337 | -46.09385 | 2024-11-16 04:01:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e450ff47-377f-3416-8e3d-5f3dc508f543 | -6.97688 | -39.9875 | 2024-11-16 04:01:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 4ecfa8d0-f40d-35ed-b771-f0f3401ec478 | -2.35448 | -48.42143 | 2024-11-16 04:01:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c958ba6-f249-3875-9b37-e2e5b95d6ab3 | -4.539 | -43.55951 | 2024-11-16 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1209eb0e-e2df-3686-9b07-178b0e6378b1 | -4.22037 | -47.22222 | 2024-11-16 04:01:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e97289f4-1fb4-38f5-8fec-2c20e192b9ae | -4.4898 | -41.50022 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 84578ab9-9775-3ba2-bbd4-00feef75e85e | -3.84604 | -46.61754 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2116795e-0cac-38dc-9148-8f2496915ffd | -6.1694 | -41.16494 | 2024-11-16 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6dff019b-3049-37cb-8f86-ebe20323f3d2 | -6.80785 | -39.29768 | 2024-11-16 04:01:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 87603c32-7230-3b3c-b1d6-511111524361 | -5.67141 | -35.64961 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 25992896-964b-3a98-87e3-049def37905a | -3.56131 | -50.24951 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 164aecc9-df6f-3534-a517-6e021a2685de | -4.81812 | -42.91637 | 2024-11-16 04:01:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ccee9828-a1dc-38ef-aab4-6e366950a678 | -2.10314 | -46.58714 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26ba8f4b-aad3-32f0-8233-16b4e3002936 | -3.88215 | -44.49243 | 2024-11-16 04:01:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 970089a0-7957-38a4-906b-6c30428fe078 | -3.65162 | -45.49781 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44e12b79-bac1-35bc-8cdd-3f3f44452502 | -4.14959 | -50.77531 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3857701f-385e-300c-b734-7b8a16be5f1e | -4.79859 | -41.48138 | 2024-11-16 04:01:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72e3d58d-a945-38b1-8c8c-8d315a8c873a | -3.49974 | -45.4413 | 2024-11-16 04:01:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 844dc57d-9a4b-3e0e-812f-8e593b685e7d | -3.74359 | -45.65401 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 07b96dd6-388a-3eff-8ca4-0e44e3106c50 | -6.54696 | -41.96579 | 2024-11-16 04:01:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6781f22d-6942-3a1c-a164-89598a4bfe9e | -3.68681 | -40.77421 | 2024-11-16 04:01:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4222f0d9-93ac-39e2-8592-a8a40f83f185 | -7.93035 | -39.55772 | 2024-11-16 04:01:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a95ce64c-e818-3b14-9212-cd94f3e8842b | -2.14759 | -46.55289 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d808e69-8980-3e02-b2a6-e591cc232cb6 | -3.94712 | -46.71305 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 171db953-ba13-32c3-a919-2d1447978fce | -3.98262 | -43.71242 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7e49d512-0e69-338e-a51c-8bf68842192a | -6.11564 | -40.01419 | 2024-11-16 04:01:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3f6e2ee9-0c3f-35a0-8312-16fde5cc0416 | -3.0682 | -45.34624 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.8 |
| ddceb7a9-0c15-316a-88ec-e56c14176e5e | -7.93674 | -41.13398 | 2024-11-16 04:01:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f246ce3-eb21-3456-8c66-7eae785747db | -3.97731 | -46.70322 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 002cd060-1a36-3fde-9fc9-9986472f16f4 | -2.35448 | -49.11748 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 88cef281-1a23-3563-b5d8-c96cb535a54b | -3.31419 | -45.3303 | 2024-11-16 04:01:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2189712c-6495-3eac-bd7b-fcff434ba56a | -2.5584 | -46.89656 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 56ee322b-58f7-376f-856a-3b8f6b5745eb | -4.83638 | -44.5392 | 2024-11-16 04:01:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d178462f-80da-3e2f-84b8-d624edc5a67b | -7.39908 | -40.39757 | 2024-11-16 04:01:00 | NOAA-21 | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0288834e-97ec-34ec-a76c-5fabb4051981 | -4.81879 | -42.91222 | 2024-11-16 04:01:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1fdcbc86-6689-3317-81ac-26a5b0d3ccfd | -4.55647 | -48.01285 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 8a2c8cfd-5c38-3fbd-9a3f-3f1be129389f | -2.64538 | -48.4846 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 690451f6-4479-3278-9044-e91d3a4b8671 | -3.73927 | -45.65328 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 322cb1f0-49c6-32dd-ba06-e685191f86f5 | 0.79703 | -50.73948 | 2024-11-16 04:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5cb82a9-49c4-3067-aaf5-604dedc35c07 | -5.96024 | -38.30667 | 2024-11-16 04:01:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10a7a66b-9f71-3169-82e8-7930ef8c1030 | -7.40189 | -41.43777 | 2024-11-16 04:01:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ae962916-f4d1-3a5d-8ed5-fccd9097cc77 | -5.91507 | -38.27717 | 2024-11-16 04:01:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ff404fdf-3a94-39d6-9649-b5289af258d8 | -4.22918 | -50.67307 | 2024-11-16 04:01:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c0b1155-7a72-39b7-b502-f9bc1a94e89c | -4.55402 | -45.76026 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63462c3e-1ad4-37bb-9fad-dda5de2822c4 | -5.33367 | -40.89888 | 2024-11-16 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d318fa9f-da03-31ae-9ba3-a57d2239186b | -4.73007 | -43.25264 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35b73cde-5ac5-3e15-bcc7-b1e46a59d130 | -4.38123 | -45.62558 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 789d996c-b60b-3dd6-a79e-361e10636202 | -5.24126 | -44.91693 | 2024-11-16 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2647f29d-52d4-369b-9c1b-e020a9b51639 | -2.66177 | -46.17076 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4d3ec70a-047c-33bd-b5a3-a319b5eb88c8 | -4.03356 | -44.11027 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c443fb6-a917-36a5-8dc9-93a4ac4919ec | -3.78082 | -50.11108 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7878f67-07cb-3217-8d37-39c5916a443b | -3.57367 | -50.23641 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1609d45f-e420-3705-9d4c-85f7fa9ed73f | -2.03716 | -46.37339 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bbfe9e1-04c9-3c58-a683-de752cf3d3a1 | -7.83401 | -34.85557 | 2024-11-16 04:01:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2ba77243-3bfd-3b70-aec3-a0da33334970 | -6.9818 | -38.87328 | 2024-11-16 04:01:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |


[Clique aqui para ver as próximas entradas](README18.md)
