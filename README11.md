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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6025c70-b423-3b5e-b17a-c64b5e5ad7d0 | -3.69417 | -44.64599 | 2024-12-18 04:01:00 | NOAA-21 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 863112e7-859e-354a-9cb5-5f3f1b776bde | -4.93577 | -45.09825 | 2024-12-18 04:01:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8b305e9-b61a-3eed-93bd-f59ab335b9e4 | -5.73199 | -39.53964 | 2024-12-18 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b84ab8d0-91a9-3f08-9189-722593916ae8 | -6.42838 | -39.67701 | 2024-12-18 04:01:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0438495d-a0fd-33de-8b26-3dde9abd2b56 | -4.54488 | -43.28985 | 2024-12-18 04:01:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a64530f-f873-37f1-9de7-f9c371210ae5 | -5.39263 | -43.66152 | 2024-12-18 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d4f23ad5-befa-3a28-b9d0-28c1894217cb | -3.24794 | -46.87188 | 2024-12-18 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bfe615f7-58d0-371b-a1e2-3d109acfeb2d | -4.44806 | -38.0594 | 2024-12-18 04:01:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| fe956373-91bf-30a9-9803-15baa5dceb3e | -6.28233 | -39.58698 | 2024-12-18 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 66f40246-0b0c-37c7-8653-4a5aaa761fe5 | -6.73875 | -34.98727 | 2024-12-18 04:01:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| df59f65b-cc30-32ad-a0b6-8658cd237653 | -1.62198 | -45.8485 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e299c56-f69d-3010-903a-3b912fe954ff | -5.94852 | -48.06614 | 2024-12-18 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 640885f1-a33b-3296-aeef-05cd8cde146d | -6.63821 | -47.34688 | 2024-12-18 04:01:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eb698f23-7fa6-3f18-bf31-4987b4f95c24 | -5.11473 | -43.3163 | 2024-12-18 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7cff4e1b-7bcb-3d6b-bb46-633a8b6ca443 | -2.87517 | -45.24857 | 2024-12-18 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 858769fe-0667-3baf-b6f8-f121fd9c1889 | -6.1437 | -43.91288 | 2024-12-18 04:01:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad0d0203-c079-37d6-988d-700e15ee8273 | -6.98628 | -43.57779 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ec60abb1-5fe2-3b8e-8d82-3baeabca9468 | -6.00864 | -42.34655 | 2024-12-18 04:01:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0e37a800-d879-3259-a761-9b41ee28b914 | -2.70618 | -47.73147 | 2024-12-18 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bb6c511-ad41-3bdf-8282-806162a0ed24 | -6.98016 | -43.56503 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 24ea4a42-2fe8-34b6-a964-52ce33dab5af | -6.97064 | -43.55484 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 205cf668-5108-3475-8a20-921eb53de927 | -4.15227 | -43.57208 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4416c23a-c6e8-3317-9f2a-29dde0447fee | -4.11986 | -43.55756 | 2024-12-18 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02b888bd-df36-3dd6-aed3-6f22a05481c2 | -4.1137 | -43.21856 | 2024-12-18 04:01:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eccb5532-aafe-3be8-a8b6-57a7d1cf64a0 | -5.29598 | -44.94007 | 2024-12-18 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5a19b667-db0e-3887-93a5-d241d40a96f3 | -6.9788 | -43.57349 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 60cc4561-22a6-3edd-9326-d96e5176540b | -4.85631 | -41.38629 | 2024-12-18 04:01:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f8aded80-afc2-3f84-b336-20bffb831d4b | -7.90577 | -35.22907 | 2024-12-18 04:01:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 30.9 |
| 6d3b3370-220a-337a-886e-052dadf94e9c | -4.16921 | -43.97527 | 2024-12-18 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f476c9df-e8ab-31d5-a793-01d6b9704a01 | -4.06631 | -46.58895 | 2024-12-18 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 706e7b75-ea06-398d-ba46-bd495a051385 | -6.96927 | -43.56329 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| cb8764c3-30f8-352b-8312-8fbb321af21c | -6.63441 | -47.34123 | 2024-12-18 04:01:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 327fcfed-0072-3b8b-9418-540dc4cc9a12 | -6.75895 | -40.12921 | 2024-12-18 04:01:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| df625e78-19bf-39f4-80c9-e174349f770a | -9.09082 | -40.44215 | 2024-12-18 04:01:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| fbaf8044-3fb7-3b7d-83e2-d2b4c3621949 | -2.08872 | -45.28428 | 2024-12-18 04:01:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6bf8986-db10-374a-80fd-46bb85cc97d3 | -6.61896 | -39.7392 | 2024-12-18 04:01:00 | NOAA-21 | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b70476ba-53e5-3e87-82d1-9d13cdc096b1 | -9.70122 | -36.17298 | 2024-12-18 04:01:00 | NOAA-21 | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0625c2a4-3fc9-38af-aeab-8c7374bf97d0 | -6.96202 | -43.56209 | 2024-12-18 04:01:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 269621d5-d067-326b-a788-e49a8bf46171 | -6.44007 | -40.6244 | 2024-12-18 04:01:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a7dc09c2-a020-3ccc-93ff-4f6850102978 | -4.39341 | -44.10522 | 2024-12-18 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81a81cee-dfe7-32fa-83f3-4b100cc41187 | -1.62652 | -45.8492 | 2024-12-18 04:01:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f18b8fd4-d340-395c-a6d3-ec4da7012a01 | -2.35021 | -47.42326 | 2024-12-18 04:01:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3737e07-a6dd-3dc3-b536-7b0f42047f44 | -5.49372 | -37.24337 | 2024-12-18 04:01:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 752de7e2-1a64-3a11-b11b-5fdc3e2a2e8c | -4.39419 | -44.10033 | 2024-12-18 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 060e9b1b-bfa4-366a-a595-afbc1ab25f86 | -6.76225 | -40.12973 | 2024-12-18 04:01:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e76f5e2a-7e26-3f73-bce5-4e8ffcbe0085 | -3.13771 | -44.4684 | 2024-12-18 04:01:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c756707-7964-3d4b-9920-6acaccdf957a | -5.97485 | -39.7513 | 2024-12-18 04:01:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 158c3ab8-fc5e-3487-ae44-6bd170cc7ebc | -3.06829 | -40.04224 | 2024-12-18 04:01:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 97f2130e-4915-3190-ba2a-1eaa187ee5e4 | -3.77756 | -43.00248 | 2024-12-18 04:01:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63ed1ecf-abe4-3559-91dc-9bc3bce0dcdc | -1.70173 | -45.7858 | 2024-12-18 04:01:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 19750bbd-7c0e-3747-9b03-eaeccefd1a66 | -2.92391 | -41.45746 | 2024-12-18 04:01:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| efd07991-88f3-3679-a3b8-8e2665ce8443 | -11.85509 | -43.82872 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 48b3dcd9-1639-3402-b381-652c61c7b845 | -11.85575 | -43.82479 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 60825849-5a8c-3711-8993-831dc79e1af6 | -10.05286 | -36.12408 | 2024-12-18 04:04:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| bcb69596-3419-3533-9926-466cc4a11e0e | -12.86072 | -38.36802 | 2024-12-18 04:04:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e3a4c979-0539-382b-8d51-b32dee9ec44f | -9.37043 | -47.72324 | 2024-12-18 04:04:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11142643-8c1d-322a-9c6d-feb32851a858 | -11.85791 | -43.83323 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 098a33de-6dbc-3d56-bfd6-edb7e3e64019 | -11.79983 | -37.97659 | 2024-12-18 04:04:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 88d98ba3-82e9-3130-8738-06a46f2e0ce9 | -11.85857 | -43.8293 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 81b300f4-aad2-3160-8ab6-90221d94024a | -11.8614 | -43.83381 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0add7438-a546-34d3-b668-b79b1e75934b | -12.85557 | -43.81784 | 2024-12-18 04:04:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7228f4cd-1115-3639-b143-d7b257f219f7 | -11.25705 | -39.23447 | 2024-12-18 04:04:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e267c14f-d449-34d3-b6ff-81da9de53180 | -12.33767 | -43.67656 | 2024-12-18 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2096a9e4-3627-338c-9e43-47e99faf8f00 | -11.85922 | -43.82538 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 568cf025-b8d3-3f0d-9308-2ea39c14a560 | -10.21855 | -39.24406 | 2024-12-18 04:04:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 34879193-5780-39fe-943e-f8ae543f0e7d | -11.8627 | -43.82596 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| a5943be7-f12d-3adf-9370-86cbfcf695d6 | -10.05212 | -36.12929 | 2024-12-18 04:04:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 33.6 |
| 9d41bab0-c568-36ea-9182-c2e6d2935da5 | -15.0163 | -41.11494 | 2024-12-18 04:04:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b0fb76a-488a-3a01-8db8-00c55a5236e6 | -9.46533 | -40.87576 | 2024-12-18 04:04:00 | NOAA-21 | SOBRADINHO | BAHIA | Brasil | 2930774 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 64505433-c80e-339d-85fb-1062837cbcd3 | -11.86553 | -43.83047 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d0986b01-cfdd-34d6-b7ad-c7dd9053d0f6 | -12.61074 | -38.44564 | 2024-12-18 04:04:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 0339bf17-f1d2-3bc2-a766-cdb81880673f | -10.75962 | -40.33543 | 2024-12-18 04:04:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ffc477af-b283-3fb5-80d9-c15a5e858815 | -11.86205 | -43.82989 | 2024-12-18 04:04:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7ca659c6-19fb-3fec-a5b8-344ddb0a6f28 | -12.34111 | -43.67714 | 2024-12-18 04:04:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f319576-ba78-36f1-9fcd-90e535b73b56 | -10.69746 | -37.04949 | 2024-12-18 04:04:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 16dbb496-7fd9-3f35-be28-f25b0a686be1 | -13.53351 | -40.68375 | 2024-12-18 04:04:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27d75fcf-acd8-3b1a-8fef-b46dc88106dd | -14.20049 | -41.65078 | 2024-12-18 04:04:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1a7c0383-9b12-3eb1-9bb7-fa3ac2b7d944 | -20.76492 | -46.7693 | 2024-12-18 04:06:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 230f6011-ae77-3f23-9a08-f5a127a5e06d | -21.05644 | -49.22816 | 2024-12-18 04:06:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 71d295ab-131f-35be-adaf-473bffe9dc0e | -19.05789 | -52.85737 | 2024-12-18 04:06:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a35b116f-19c0-37cc-94ee-1421d1b8e49a | -21.65752 | -41.32541 | 2024-12-18 04:06:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1f1fade9-ac5d-367b-b33c-92f2c2699e7f | -19.71107 | -49.86509 | 2024-12-18 04:06:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cace6386-b336-3a12-902e-8844815b8e48 | -19.06915 | -52.85663 | 2024-12-18 04:06:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4619c951-15e1-3da3-a8dd-b70ac80c9a53 | -20.73106 | -54.42339 | 2024-12-18 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 22f904df-635c-31cc-81b9-979fcf6249d9 | -21.3556 | -48.61778 | 2024-12-18 04:06:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 153b4a3a-8eb3-32e4-86dc-4b9b3af27926 | -21.35463 | -48.62306 | 2024-12-18 04:06:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7a3e545b-21a9-3eb4-a256-bb149a100a89 | -19.71008 | -49.86546 | 2024-12-18 04:06:00 | NOAA-21 | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d61cdda-f240-31bc-afac-f3c4273d4f4b | -20.16072 | -47.39687 | 2024-12-18 04:06:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36d1ddb6-4355-3658-982c-d752461f901e | -20.73198 | -54.41935 | 2024-12-18 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 9593d168-1ce9-381f-a0c8-a8444a6e9a10 | -21.58892 | -49.23777 | 2024-12-18 04:06:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| de6c2c69-7981-3a78-a4e2-686af8d9574b | -20.77774 | -49.85308 | 2024-12-18 04:06:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 607fc237-6b46-32d4-970a-b9d13a8f12ca | -19.0677 | -52.86353 | 2024-12-18 04:06:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4d0d0b3-4ef8-3aa1-93fe-0b9a3044720f | -19.06241 | -52.86226 | 2024-12-18 04:06:00 | NOAA-21 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50b66ef7-b178-3fce-b681-4296da5fa263 | -21.589 | -49.23822 | 2024-12-18 04:06:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d8e849f6-3244-37b2-900e-b1a58b24dc98 | -19.76833 | -50.95338 | 2024-12-18 04:06:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b5cd3b5-489a-3ee1-a814-9135db456427 | -20.77434 | -49.8478 | 2024-12-18 04:06:00 | NOAA-21 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| ac8602cd-835c-3bec-8801-087bddbce118 | -20.72864 | -54.42395 | 2024-12-18 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 10fdd3ae-438a-3f88-8d9e-aff9b9fd4bb1 | -21.5923 | -49.24293 | 2024-12-18 04:06:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 51f42877-97b9-3b9b-ad10-2bd8075f3b2e | -20.72953 | -54.4199 | 2024-12-18 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3b2ef377-77a9-3ed6-9299-44f24caae04b | -20.73015 | -54.42739 | 2024-12-18 04:06:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |


[Clique aqui para ver as próximas entradas](README12.md)
