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

## Dados Diários - Página 282

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0235c904-96e5-3d46-884b-5013c4aedb6d | -6.63037 | -44.89435 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| dac13216-1c13-3dac-9f83-01b6845b8669 | -6.16117 | -39.42922 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 01a174c7-3809-3757-bc26-792f9fe0c1c7 | -7.53861 | -42.08313 | 2026-10-08 16:20:00 | NPP-375 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d67eaa47-d2cf-3c67-a0e2-1ccf5a8eb970 | -6.83418 | -39.56377 | 2026-10-08 16:20:00 | NPP-375 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 20.1 |
| f84a58b0-4a4a-3bed-903a-9e559f0af670 | -5.29892 | -45.71676 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c52017d5-3d70-31f8-897c-d220c61667f2 | -4.79584 | -43.138 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| bca01eed-75f3-3334-a0f0-3a1cb246d1b1 | -5.69213 | -53.48228 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 98e93f37-b894-3654-9072-4122a51f1e61 | -1.70974 | -49.8388 | 2026-10-08 16:20:00 | NPP-375 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fc6b0986-4355-318b-badf-70480674e407 | -5.70083 | -53.48713 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 47eca85e-2c37-3385-bf97-74c32d600a07 | -3.8962 | -42.11296 | 2026-10-08 16:20:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 20.1 |
| c3641966-7eee-3aa3-8c22-1742174aef01 | -5.47934 | -44.60624 | 2026-10-08 16:20:00 | NPP-375 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 129f3f85-df9c-3b05-bc48-4e350d375630 | -6.86196 | -41.79638 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a0bb44d9-8e01-39af-b952-f7defedfe43c | -5.47881 | -44.60263 | 2026-10-08 16:20:00 | NPP-375 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bd5a74c2-8872-3483-8ae3-c10e419fb1ae | -6.77594 | -44.12609 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4957a5c7-0d2b-3fbc-b25a-af2073eba92f | -6.22533 | -44.86134 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 185.1 |
| aa466137-49a4-3ce1-864f-1dfd11fad4c9 | -5.18091 | -38.44742 | 2026-10-08 16:20:00 | NPP-375 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| ef94b042-3e59-3418-90cc-340f226b83f0 | -6.5084 | -42.03379 | 2026-10-08 16:20:00 | NPP-375 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 8acf170b-c311-3253-8486-9ef5fc752819 | -4.77092 | -49.12469 | 2026-10-08 16:20:00 | NPP-375 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 73d059c7-eee6-31ca-814f-2cc2bf8355ae | -6.82256 | -38.54361 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a7f00911-2884-3b2e-8dd9-9709916add89 | -5.51075 | -42.83934 | 2026-10-08 16:20:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| c9ab0587-d0c0-33de-9df5-c907586e9610 | -7.17082 | -44.82747 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f8632418-1302-36ae-98a5-6e43c199871f | -7.46414 | -42.82535 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 54878834-9182-3aca-b8cb-68ed031f1100 | -6.92632 | -43.66755 | 2026-10-08 16:20:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 4e60b990-e6c6-31bc-b34d-208906130d37 | -6.53507 | -45.38031 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 81ce1d93-313d-3386-a578-e1e430d5eca5 | -3.00012 | -49.21636 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4f6ccdaa-3f5a-316d-bb80-ade6872a1162 | -3.00305 | -54.08172 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| af19c8f4-ecdf-37e2-8331-50e8afc9ccb8 | -5.74523 | -42.0792 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 129b3181-9e75-3a1e-a6ac-6f3dc2546189 | -1.09514 | -48.05542 | 2026-10-08 16:20:00 | NPP-375 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 376be66b-dd50-3c20-9410-c7583e0fdd3d | -3.74213 | -44.70092 | 2026-10-08 16:20:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| e5ef7b22-b7d4-393c-86a7-b3f8490d0020 | -6.14743 | -47.957 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25825530-0bf7-34af-a094-054bbfcb264d | -5.74019 | -53.45537 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 726af859-d321-3269-9afd-8197e99790e3 | -5.71787 | -41.6555 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 8dee53cd-6364-3f03-847c-6242259640c2 | -5.45052 | -42.90782 | 2026-10-08 16:20:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 289d5088-d0aa-3e95-94b3-d30a77c06633 | -3.80992 | -45.41033 | 2026-10-08 16:20:00 | NPP-375 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0714f66c-bd59-36b1-9409-0ff6bb023bf3 | -3.85953 | -38.50996 | 2026-10-08 16:20:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| b5c4fe45-c5d1-32ad-8cf3-1d05f885855d | -5.94003 | -44.32801 | 2026-10-08 16:20:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f8aa77cc-8275-3ecb-97a0-240f18d537ef | -7.0408 | -44.33266 | 2026-10-08 16:20:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ea1956d3-cc0b-393c-a36f-f9bcd263f5e7 | -5.74795 | -41.59669 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f94532c5-1bfe-3055-bdb1-66e8439f0c0d | -7.10277 | -41.74568 | 2026-10-08 16:20:00 | NPP-375 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2b20416c-5cc2-3ce2-93a1-9c23703984a3 | -6.32695 | -46.55312 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 86ee8f98-0c33-308b-b3a9-65bf31d3d47e | -5.47913 | -45.63024 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b392c48-acd8-3808-a2ff-16aad718a46c | -6.45435 | -42.80117 | 2026-10-08 16:20:00 | NPP-375 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 28d78566-1f20-311d-80f7-0c85a2e2b62e | -6.85042 | -41.76568 | 2026-10-08 16:20:00 | NPP-375 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a5a589de-5c37-3d5c-b18f-d28c89d9af46 | -7.19151 | -52.62853 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 32d98bbd-c243-3154-ba6b-426f783ce9c8 | -5.95804 | -46.38471 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8fa0ef75-608f-3b18-bc09-554b8df846cc | -5.54407 | -43.23227 | 2026-10-08 16:20:00 | NPP-375 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a06eb483-06d9-3fd3-bbe0-b2d07e84cc66 | -2.07113 | -46.57426 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bf10413f-bc32-30c4-848a-c5fca947d530 | -4.89877 | -43.37368 | 2026-10-08 16:20:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7546ae9a-e72f-31dc-a29c-79ef4dbeb90c | -8.3114 | -47.64042 | 2026-10-08 16:20:00 | NPP-375 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e25e0305-e169-396b-a7e6-09b7f50475cc | -5.37274 | -44.20555 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 74fed83d-1f64-3638-b21e-4a286d9d1631 | -5.99427 | -37.38088 | 2026-10-08 16:20:00 | NPP-375 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 61.0 |
| a4decc5f-fc91-39bd-b3a2-15b4da138fac | -8.19273 | -46.35742 | 2026-10-08 16:20:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a325bfce-f3ea-3420-a41e-28ea331238d5 | -4.093 | -44.09877 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d03d5e80-9141-375c-b8ee-1e2cd8baef02 | -5.72313 | -41.61979 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 036857f4-63a7-3acb-b621-f93bb4aa3d5f | -5.99486 | -37.38463 | 2026-10-08 16:20:00 | NPP-375 | JANDUÍS | RIO GRANDE DO NORTE | Brasil | 2405207 | 24 | 33 | nan | nan | nan | Caatinga | 61.0 |
| 79d1522c-102a-3ffd-b712-6aedf9134ef6 | -6.21975 | -53.27831 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 811f502a-6b7e-32d1-a201-accb21677991 | -3.02216 | -54.04828 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f2662a26-10de-3738-9e62-31b1799bda8f | -7.34364 | -44.4769 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 63192ad5-d198-30bd-b508-ce1f0ad4572f | -6.69575 | -45.2865 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 6d2573df-6769-3be9-8d22-4200f48cfb93 | -3.37189 | -43.02655 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 01f881bf-ae01-3525-b061-8b533a64b4c3 | -6.15121 | -39.43074 | 2026-10-08 16:20:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2bfe03ba-ff6b-3041-82d3-edc82c8b9d77 | -7.4755 | -42.85127 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| a1caf5d5-5cda-3b27-8e99-b6145a9b606b | -6.92268 | -38.55605 | 2026-10-08 16:20:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8fca00a3-c107-369e-b3c2-959d98a35662 | -6.15521 | -47.93701 | 2026-10-08 16:20:00 | NPP-375 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 540aba84-2819-37a9-bc85-b2b4f7c5212c | -6.23594 | -43.85583 | 2026-10-08 16:20:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 04ea159e-b358-30c7-883c-d791ec40d9f2 | -3.81656 | -44.6275 | 2026-10-08 16:20:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 21ac6d59-1e7c-3951-a168-6c385892e7cc | -3.28808 | -49.12634 | 2026-10-08 16:20:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| afffdb93-5b5a-3ef1-a24d-055249ad93c8 | -7.39802 | -44.45756 | 2026-10-08 16:20:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 79d87fe5-423c-3665-a8c2-84065ecf5b35 | -6.67108 | -45.36149 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 78eb57de-bd15-3f47-889e-167206806690 | -5.74232 | -42.05946 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 3d2ab1e3-003a-3d0d-b1a1-553b61671274 | -6.77241 | -44.13006 | 2026-10-08 16:20:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| e8da0aff-139d-3d9d-92d8-eabbff3ccedf | -5.4854 | -43.96344 | 2026-10-08 16:20:00 | NPP-375 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| c969571e-9cb0-3eae-93a5-374bf981572d | -4.16074 | -43.1947 | 2026-10-08 16:20:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 696ae6b4-efa2-307c-8a55-5777e2d55cfa | -6.72642 | -45.1825 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| b3b905fa-0d2d-362b-9827-bd44c1fd1e96 | -7.25237 | -39.40154 | 2026-10-08 16:20:00 | NPP-375 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| cd7748d9-39f4-3ed7-b4c5-f0e440ef5c22 | -6.26311 | -44.73399 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b965aad5-cf5e-36f3-adb3-877a52a2e5c2 | -4.10212 | -44.10722 | 2026-10-08 16:20:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7e7874ed-5e7d-3e6f-ad4c-8d2895585cea | -5.49763 | -40.53613 | 2026-10-08 16:20:00 | NPP-375 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 35d768cf-3711-381d-8cd4-20d09199d015 | -6.15863 | -42.5895 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 5a42d043-367f-3f27-a56b-c76cc2049750 | -6.20093 | -53.26495 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 1dc1c7bc-6d4b-3309-a1fb-5e11105c1d0e | -6.46563 | -46.53639 | 2026-10-08 16:20:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2aa2e9c4-9044-3fb2-b2c2-19b5608df604 | -5.09631 | -46.19836 | 2026-10-08 16:20:00 | NPP-375 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 9b9ad7b3-9a3b-38dd-9971-0bf33db179bf | -5.69357 | -53.4882 | 2026-10-08 16:20:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 1c840105-b000-3672-809c-450b9ffb3f7a | -1.58924 | -47.35802 | 2026-10-08 16:20:00 | NPP-375 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| bdc6ed65-f746-32b7-b95b-a66f51ab836b | -3.18664 | -50.58822 | 2026-10-08 16:20:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 468e6e26-b33b-3747-87c6-81f5e04020e0 | -6.15438 | -42.58587 | 2026-10-08 16:20:00 | NPP-375 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 29.3 |
| 33e0280d-ed74-350c-ba72-79508d37be45 | -6.38503 | -42.53577 | 2026-10-08 16:20:00 | NPP-375 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| e77a158e-e7b4-31b4-89ad-df1eaa080104 | -7.4724 | -42.85632 | 2026-10-08 16:20:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 0d17b2f5-97eb-39e4-8c50-d7ce69898c8c | -7.73803 | -49.60023 | 2026-10-08 16:20:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e270cad4-65dc-3f96-a92e-577e87b0d85e | -6.18872 | -52.8717 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8e357024-b251-3e36-94cb-45c970c7385a | -3.35499 | -43.01227 | 2026-10-08 16:20:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f89924e6-42dc-3ce6-b3fe-78f6a82ca1d6 | -6.53246 | -45.39334 | 2026-10-08 16:20:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| ba072e6e-ff53-3ca1-b603-5ab25510a64c | -7.31391 | -43.98082 | 2026-10-08 16:20:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 0517dab1-2e87-3827-8ab1-427d4a538256 | -2.86566 | -54.15966 | 2026-10-08 16:20:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a6625911-a1fa-3676-8f37-b374081b42ba | -5.30332 | -45.71634 | 2026-10-08 16:20:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 53a12fd4-8e2b-330d-8d76-1ee5c09edd84 | -5.88397 | -45.96062 | 2026-10-08 16:20:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f3a762c6-e43f-3cd1-85eb-d2d6b76b05a0 | -7.33553 | -50.82871 | 2026-10-08 16:20:00 | NPP-375 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 06d99e6e-c961-3546-b28a-0da3e861c4ac | -6.59112 | -41.54936 | 2026-10-08 16:20:00 | NPP-375 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| ccdaab67-c991-3527-8bc7-521bfee37d23 | -7.037 | -44.7323 | 2026-10-08 16:20:00 | NPP-375 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2891f5ab-9f86-3b7f-bfa0-e2e62edf2487 | -6.83902 | -45.12411 | 2026-10-08 16:20:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |


[Clique aqui para ver as próximas entradas](README283.md)
