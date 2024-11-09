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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 82017348-3857-3957-b7ab-faad8c2b2e6b | -2.94046 | -52.51311 | 2024-11-09 04:33:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7fc2ae7-db71-33b8-a607-4d5573ed6810 | -8.84534 | -47.67658 | 2024-11-09 04:33:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e152070d-b2a9-3bfc-a005-531c74325832 | -4.43389 | -47.26466 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| acd36a11-03b6-3038-93cb-6b8e71e9d4ba | -4.05505 | -48.25368 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3c28cab-ef75-3d32-b090-0bba63c004c1 | -2.303 | -53.81883 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ed08ddf3-0777-3a43-b85f-71058af092c2 | -4.39395 | -50.97205 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5102dfb0-632f-36f0-a977-b56cf688ae45 | -3.95929 | -46.7092 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 562d566f-e268-3ddf-9f71-a448d1a3c514 | -7.12854 | -49.28358 | 2024-11-09 04:33:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 7de1767e-f895-3b0c-99f4-f2f4ed92f2fb | -3.27343 | -51.06524 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b3fb404-dca8-3807-96d1-c60b44c28b6a | -6.19644 | -43.42714 | 2024-11-09 04:33:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc57a530-71ce-395e-8419-32e8f96c848b | -2.76841 | -54.04937 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 83c9d0bb-0f56-3425-a46b-f909311ae4e3 | -4.75869 | -48.92701 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ebc373b-5fc2-35f7-8547-f51a79344809 | -4.38203 | -47.22844 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8398ea0-8ab7-3490-aa22-f6b85a3daf34 | -5.13514 | -48.24317 | 2024-11-09 04:33:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9b720622-99d6-3b98-b6c2-479bc40b934a | -5.47053 | -41.92978 | 2024-11-09 04:33:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0e66c1b5-c7f4-3a85-b889-975f85ed319b | -2.84013 | -49.53393 | 2024-11-09 04:33:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8fdb15a-a1ec-358f-b92c-a7c46af3cc3e | -3.98377 | -46.41999 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad3b115c-6a4e-35be-9adf-f2d1a5e798d0 | -2.8455 | -49.82455 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be173c34-67af-3412-b7e9-81cd63bd32fb | -3.24749 | -46.49571 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cff44064-6450-372b-9352-59afbd7cfc9f | -5.84138 | -44.52146 | 2024-11-09 04:33:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62fe456d-b9b7-37ff-bed2-4461748399cd | -4.7812 | -48.67657 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b4d6064-aa2d-3d0e-a06d-c6c5c5355c94 | -3.66752 | -54.65776 | 2024-11-09 04:33:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c4e25a0-1ac7-3f6d-b872-56d0f144d8ad | -2.86573 | -50.31834 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bea0d348-31a1-3cd4-95ab-756bbbfeca31 | -3.18857 | -50.58241 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 398b832f-4f16-3b9f-b7d4-cb8d96c64fe8 | -3.64004 | -50.18729 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 05a83038-64a7-3d51-aa37-a225e94adc59 | -4.28566 | -48.64893 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99ae483c-749a-3750-a438-10fc50acf246 | -3.84323 | -49.82421 | 2024-11-09 04:33:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0a07b006-c8fc-395f-b35a-ae13e923c4bc | -5.43897 | -43.2583 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b0f1b91-0e55-308d-a22b-7a5fed48d773 | -3.95249 | -48.14869 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a274222-7ff1-3afa-8d57-9ab03bb7a6c7 | -3.29455 | -46.03993 | 2024-11-09 04:33:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98f01a75-c2fa-3c14-9e78-815c540a14e6 | -3.33291 | -50.08823 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11cc234f-53a6-3114-a30b-85c48859de70 | -3.23607 | -53.39609 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de183333-6b62-3fc1-8726-5fdb8c6bb59f | -3.0541 | -47.69227 | 2024-11-09 04:33:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f66bd440-c01d-310a-be30-44094fb254e9 | -3.5818 | -51.2007 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f104ea95-5ac9-3036-a128-bb70f1328584 | -2.87956 | -51.47153 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 03652339-c5dc-3979-b401-f98207c2bd8b | -2.71545 | -51.99532 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d0382257-623f-3a8f-a149-810f2dcae22a | -3.78151 | -46.49657 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afc98bea-2b5e-3061-9601-ebb85e651380 | -2.83436 | -49.43556 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 359a6d1f-ebaf-36a5-b99e-733e1e67b5a3 | -4.19869 | -48.55258 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc7123ee-f78a-3138-ac2c-40ab6761304f | -4.37882 | -47.24909 | 2024-11-09 04:33:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 886ea0fb-5b6c-394d-b6c7-783c68a0bd55 | -3.44099 | -45.98972 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21833ef0-170c-350c-a2e1-5f678f1a1a3a | -4.8473 | -48.64731 | 2024-11-09 04:33:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1a745a8-01d5-3f3f-acd8-900039ca15cb | -2.84021 | -51.34934 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d635c2e-da1d-3c37-918f-66ca553ca412 | -4.56356 | -46.34353 | 2024-11-09 04:33:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76e59e51-39f8-393d-a317-e24d68063400 | -3.03425 | -50.32519 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 85dd2f1d-897d-323a-89fa-89de0de4e3bc | -4.11058 | -50.44338 | 2024-11-09 04:33:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd327886-4683-3de6-9da0-a1b1501adc16 | -3.46308 | -50.18113 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23fa1bda-9375-3931-92af-063f39fe2268 | -5.44658 | -44.8235 | 2024-11-09 04:33:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b170e51c-05a2-3504-8a15-7f44f588a751 | -2.66777 | -49.8909 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0d6c12c-7123-36fa-a906-3ae87358564d | -3.7881 | -51.32503 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77c7e821-5f86-35d7-b446-e1a8abc3bb2d | -3.21426 | -50.23886 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 69ea6f9a-9c07-3ddf-9353-79820a8891df | -5.16631 | -45.28089 | 2024-11-09 04:33:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1d03d50-979b-3787-8163-935895f26209 | -2.68722 | -51.82442 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 78e0fb10-17a1-3915-80b9-af47ae6fdb1c | -2.87815 | -51.30741 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 234a76e0-37d6-32b3-96c9-ed79fa5a1494 | -5.43969 | -43.25344 | 2024-11-09 04:33:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20f9e9ea-d187-3d31-aeca-3e888e66aa5e | -4.20339 | -45.85953 | 2024-11-09 04:33:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| adcade2b-7ea9-3614-9aef-9e352182a26a | -3.85522 | -51.24314 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd8d0c8b-b8a1-3b54-aa18-b218dfd97131 | -2.56599 | -54.16825 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55351981-8b72-3b26-b310-668b859e037b | -3.61406 | -48.92015 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b86a4f02-111f-37b3-9c47-01cb66d9e0be | -3.23821 | -50.45719 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 704437f1-3526-3edf-9b5e-5ef714217ee7 | -2.84128 | -49.23634 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f534552c-85f5-3a91-946f-252f69315fe1 | -3.04989 | -53.27576 | 2024-11-09 04:33:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f57d89b0-8e19-37b3-b649-82dd30f0328e | -3.37398 | -46.38306 | 2024-11-09 04:33:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d197b9d4-b25e-3765-a987-559713200f98 | -4.08635 | -48.50984 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ceb21c7d-11e9-319a-bbb5-1d3c4c1c3d42 | -2.86909 | -49.81216 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b87df5b-8545-3bbb-a61f-60aa6a032f34 | -3.95507 | -48.99224 | 2024-11-09 04:33:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cfc1acd-dbf7-3f60-b8fc-781f2242e1fd | -3.81582 | -51.2968 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3666cf34-83fc-37c2-a84f-4e2df66133e8 | -6.31267 | -42.75687 | 2024-11-09 04:33:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53e12d96-4507-3c22-a935-7ccbcc0c5a9b | -3.04866 | -50.37395 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 890d5ad1-0083-39eb-90bd-7738c9a4e610 | -3.95519 | -48.13138 | 2024-11-09 04:33:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 30c50360-2564-3584-b114-c70d5f539059 | -3.89111 | -52.39117 | 2024-11-09 04:33:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30fd02cb-8e85-368f-98f8-979fb55e15d6 | -3.88871 | -46.61643 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 394a2777-d2f5-3c08-ba0b-22dd51ce7f84 | -3.54725 | -51.53788 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c42bb8a2-c7d8-3760-bd48-67de6fa06855 | -4.60488 | -48.69554 | 2024-11-09 04:33:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa3c97e7-8932-3768-bdfd-8dd9e96fbc81 | -5.81476 | -44.119 | 2024-11-09 04:33:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 060df5fa-9acc-3935-b258-67f63a00c0a2 | -3.2011 | -46.50992 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce5d1a25-6afd-3ae1-aa5a-fc2ee3dfa488 | -3.19716 | -46.49152 | 2024-11-09 04:33:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5010140-d812-3b43-a241-9b6c0af9f2c0 | -2.18883 | -53.64184 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b92eb73e-c7e5-317e-bd2d-70aa52efe042 | -3.53442 | -51.60039 | 2024-11-09 04:33:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00204398-2dac-3f71-b085-d4430ce8b701 | -3.78991 | -51.82066 | 2024-11-09 04:33:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9441b46d-69c2-338e-ad19-3c5828a5d211 | -6.10856 | -44.75621 | 2024-11-09 04:33:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c83bbb4-21e6-3916-8922-0024c704a7ff | -3.16968 | -49.09351 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c31b92f-fb8b-3ac7-b962-ce6085d79a28 | -3.04801 | -50.37809 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 008cb4e4-0c3b-3ce8-9af3-66fd1ce371ab | -2.66589 | -49.9028 | 2024-11-09 04:33:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9809402-5c19-324c-884a-dea52a334386 | -4.65475 | -49.26851 | 2024-11-09 04:33:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4f1635b-c8f9-3d57-bc58-be035ab38c26 | -3.03672 | -48.04404 | 2024-11-09 04:33:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c74568eb-09a9-341e-ac48-644f7097e556 | -2.61924 | -51.74516 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fd9e4c7-3d1b-3af6-a149-13be23caccf4 | -2.96678 | -49.28664 | 2024-11-09 04:33:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 882ad894-78e6-3e43-9b4a-cd55be395e7c | -2.30628 | -53.81676 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 23186169-30ec-352f-8fd3-1f40c73fb934 | -3.78932 | -46.13754 | 2024-11-09 04:33:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1366481-f172-32d2-b4ba-967a68a1d1a9 | -2.25612 | -53.72512 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 51fcf786-f72b-3a13-b4ed-4b1a07f5f7e2 | -3.24534 | -48.74866 | 2024-11-09 04:33:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6279d70-53ad-30c5-9da1-ca7636952a17 | -2.46485 | -53.68925 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| cc389d70-229e-3cb8-b105-ab86f086c0b7 | -3.40432 | -46.05644 | 2024-11-09 04:33:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c21ae4e9-4fc1-3bd3-ac3e-bb2be45d5f62 | -2.23739 | -53.72675 | 2024-11-09 04:33:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7cb41985-fdfb-362e-866c-9b23a4c3a1b4 | -3.27447 | -50.34429 | 2024-11-09 04:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fac91bab-c02c-376d-ba51-a790364c8630 | -3.35985 | -50.12411 | 2024-11-09 04:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 391bf861-fafe-3657-8e5b-97e466173d0c | -3.59042 | -47.3543 | 2024-11-09 04:33:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c7ab148e-3d34-342f-b98f-960bd5214372 | -4.12668 | -46.92352 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99569fb1-d994-3f68-a161-b132e0f53b9e | -3.98431 | -46.41649 | 2024-11-09 04:33:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |


[Clique aqui para ver as próximas entradas](README59.md)
