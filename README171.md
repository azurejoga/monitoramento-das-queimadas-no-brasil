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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe8293bb-0f95-3ee8-af90-c6bb9d1df2ad | -7.73078 | -43.88665 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 45f654ea-4c2d-3a81-bfcd-cec3d6fe9e46 | -7.07155 | -44.30984 | 2026-09-21 16:03:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fae9eb4f-09a6-3ff0-bcf0-a6b91e4348de | -5.98871 | -45.25013 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4b12e7d4-a2a1-32ae-bcba-90f554ae114f | -6.80733 | -47.88975 | 2026-09-21 16:03:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 47369e8c-7d79-3804-9278-62db260baa6c | -8.49123 | -47.02027 | 2026-09-21 16:03:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 60277bb6-2dd8-3e28-91f7-4d98a027ecee | -6.81393 | -43.7326 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b4a34b8-6ebc-38c6-8f5c-1a242f170d5e | -7.40622 | -44.79977 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 29.9 |
| cc590e84-3f9f-3ad3-8f1f-711eaf7dbbd8 | -3.34293 | -42.53478 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| e7a822e7-f117-348a-bffc-1c7702161cc4 | -4.31388 | -43.90554 | 2026-09-21 16:03:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7f5971a6-f6b0-3a96-9a36-427fb4fca9a6 | -4.90347 | -43.46604 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c71797c0-3bfa-3a21-916e-0862f7d3f439 | -8.39053 | -46.51716 | 2026-09-21 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a91bef59-76a4-394d-8a61-3eb81281705c | -7.05867 | -43.65897 | 2026-09-21 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a8845707-7051-3e40-a411-f364cf07b432 | -8.31117 | -46.00711 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| f80728e1-0581-3817-876e-b1cf38ff952e | -5.82108 | -43.86077 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c6cbefe2-b4e6-321c-b3c7-1bd860641986 | -6.88553 | -41.70702 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| e70ed73d-3aa7-3c3e-810b-d468165e4f9f | -1.36983 | -49.32366 | 2026-09-21 16:03:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 9ee71f09-b7ca-3f9a-b1fa-7b7e61f03dad | -6.85349 | -44.57397 | 2026-09-21 16:03:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dd8a01e5-b83f-346c-8783-50e1b710c8c6 | -2.17289 | -48.31977 | 2026-09-21 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fd4b0796-a03c-3e07-a130-118e8fbd9b24 | -6.84979 | -43.71183 | 2026-09-21 16:03:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 4d776fb2-6c6b-3682-a112-d1f888bdfc2e | -7.12321 | -43.71868 | 2026-09-21 16:03:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e45b8e0b-08ad-3553-b32b-128be9f05b58 | -6.99076 | -44.71471 | 2026-09-21 16:03:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 519ebe11-e7cd-3107-b370-f0f5123bdd77 | -6.00121 | -44.77739 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b4e711f0-fe6a-3203-ab73-6dc4e62de0cc | -5.58732 | -45.5465 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 102.3 |
| cd5f014e-6b30-32e5-99b0-811029f0cf38 | -3.39145 | -42.86441 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 744bab24-3340-3806-b403-e333ce176308 | -7.73196 | -43.89489 | 2026-09-21 16:03:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2b61bd30-e3f5-3a28-8af9-6143efe941f3 | -7.37268 | -44.62766 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0910b22a-bf1a-3207-a885-47ca538698d2 | -7.16712 | -37.71443 | 2026-09-21 16:03:00 | NOAA-21 | EMAS | PARAÍBA | Brasil | 2505907 | 25 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 96cae604-021a-3139-b283-caf000ee2129 | -7.34452 | -44.20375 | 2026-09-21 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 4fd81b5d-73ff-3602-a121-3131954e2b6a | -7.40897 | -44.81927 | 2026-09-21 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d687b851-f6a5-36e6-973b-c5308d2d9967 | -4.21219 | -44.66501 | 2026-09-21 16:03:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 0a4fad1d-9bc6-3f03-a554-0d0a6792a2cd | -6.29856 | -43.78619 | 2026-09-21 16:03:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b15301d-cd92-361a-9c06-84b2d54980dd | -7.6208 | -46.11993 | 2026-09-21 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 984f2b0a-6c9d-32bc-a329-4ebb9b58a633 | -6.90215 | -42.9271 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 52.1 |
| 49ccba65-01b3-32da-ae4e-374b8aef848e | -8.78093 | -49.95972 | 2026-09-21 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f7d31222-22fc-3dc9-9177-17f167df8897 | -4.05285 | -38.20713 | 2026-09-21 16:03:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| b9fde8b5-900c-3a2f-8a30-90fa2faad3b2 | -5.56345 | -45.51428 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3ce707cc-3dd9-30fd-ad1e-c5fafca3c36e | -5.61268 | -44.83672 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 410fed31-0d6a-3409-835c-28357ab605ec | -5.13564 | -49.93917 | 2026-09-21 16:03:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| a1f02f9d-9fcd-35ef-a71c-f72590b55050 | -2.47235 | -49.82299 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3083152d-c646-3fe6-901f-cdc87edd7ccb | -8.61344 | -47.30059 | 2026-09-21 16:03:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f709ad80-215c-34a2-b8f0-ca5664f7981c | -7.53138 | -45.41277 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7c9d3acc-7532-32cb-a496-456510e03e2d | -3.78138 | -40.13623 | 2026-09-21 16:03:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 73b5637c-835e-3ff3-aea4-6bb15b48861f | -6.1421 | -47.50974 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d7915c6-a03b-3ea3-9b49-36ee2bca93e1 | -6.54217 | -44.9195 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f9509bc5-b22e-3fbb-8f6c-7be9b53975b1 | -5.76653 | -43.70102 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| efd5a1b5-1965-3212-a89d-5c18292d5ca5 | -8.31549 | -46.00089 | 2026-09-21 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| dd77ce94-b2da-32a6-b020-f31c35edbc17 | -7.05981 | -49.91004 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 17ae068d-5d10-349f-ab1a-4cac43839129 | -8.72896 | -49.56024 | 2026-09-21 16:03:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 008b5733-c4e9-325f-89a1-bfe53829c830 | -6.31594 | -47.6234 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6aeb475-fc2d-3924-937d-377c0eb40308 | -5.99406 | -44.7279 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| c7be67df-077d-30e5-9886-ee5f94931858 | -6.60998 | -45.91704 | 2026-09-21 16:03:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 09816ee4-4f16-313f-a43b-7b134df4c280 | -6.37011 | -44.89877 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6fd59630-d9c3-32a7-97db-f114fc399f7c | -6.8842 | -41.71001 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 315a125b-9eb3-3efd-aab2-0ca3b6608b33 | -1.14471 | -46.78741 | 2026-09-21 16:03:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 7d8bec5e-84e4-3ab1-a6c6-4b745f89614c | -3.33196 | -42.7757 | 2026-09-21 16:03:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 381.4 |
| c39f0fc3-4ac7-35d8-8466-e1c232c52c01 | -6.8818 | -41.7076 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 47bac03f-e176-337c-a199-d454cdbc2db3 | -8.7987 | -48.74979 | 2026-09-21 16:03:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 54159bc9-9f05-3167-bff7-b190f769c679 | -6.19234 | -45.32449 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a0205fbd-4f2a-3313-9b29-42db16d6e042 | -6.46568 | -42.7622 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 642e7f4c-9dd0-33d3-8e80-21ff02e42024 | -6.42179 | -43.86118 | 2026-09-21 16:03:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f61ffdc7-7350-37cd-af90-4f94530e328e | -5.43444 | -46.61797 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3834bbb5-b0bf-3b0b-86ef-6d633e1184bc | -6.47257 | -42.78173 | 2026-09-21 16:03:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6d64b15c-0099-3f81-bfb4-c9911f1c67a4 | -5.62322 | -43.37822 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| cbb0216c-579b-32bc-911f-97594afdc037 | -5.27818 | -49.34216 | 2026-09-21 16:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| de1ac37d-42c8-363c-b762-59b6156cfc7b | -5.81687 | -43.86139 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 3824ca57-cafe-34e9-b561-3cc1bda385f8 | -6.88861 | -41.70195 | 2026-09-21 16:03:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 39ebe6ae-8e17-352e-96b8-3160163005cc | -3.32688 | -42.55546 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| def3aaab-7afc-3119-aa0a-31ef414b33b4 | -8.34198 | -50.75798 | 2026-09-21 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7342adaf-e940-3140-93c0-de09c3612b75 | -5.998 | -45.24881 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 4bd53da9-30ba-343d-8eaa-874004be0b5f | -7.08936 | -42.07892 | 2026-09-21 16:03:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| fb5b06da-f086-3a82-8b40-9e7cbfddfb62 | -6.71614 | -43.98745 | 2026-09-21 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| b2e0f3e8-3b31-349b-8b27-940768a581b4 | -5.55943 | -41.55929 | 2026-09-21 16:03:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8247f05b-9ddd-3a9f-ad30-aeca5376dfc7 | -4.76785 | -43.67737 | 2026-09-21 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 320f61f0-42a4-32cf-803c-77adbd9b16c7 | -3.58434 | -40.31744 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| b1139036-b83e-3f28-9ea0-bef85e4eec57 | -4.40871 | -43.06971 | 2026-09-21 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6134643f-d5dd-3c4b-b4bb-34c900fbcf07 | -5.61298 | -43.39516 | 2026-09-21 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| bafd0cce-87f1-3241-96b1-f7e8279f3ccb | -7.57925 | -45.44044 | 2026-09-21 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 54e2aab8-8ed5-3de5-a3c0-6b69fe79bb76 | -7.06121 | -49.92091 | 2026-09-21 16:03:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| f616c013-1140-341e-9102-a72ae547785b | -5.46104 | -45.61743 | 2026-09-21 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dad49077-66b4-3fa9-a249-9d4ddf66cfe7 | -8.64974 | -47.36026 | 2026-09-21 16:03:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 089232e1-fca1-3bec-8786-0d126622f82c | -4.5723 | -44.57791 | 2026-09-21 16:03:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b017d9b1-551e-38a2-812e-8e355fb38ba1 | -7.1259 | -43.09538 | 2026-09-21 16:03:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 213a5d57-2e8e-3a7c-ba20-071ff015b9d9 | -5.7443 | -43.72321 | 2026-09-21 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 2e153702-50f9-361c-86b4-0403b9255410 | -6.98949 | -47.48557 | 2026-09-21 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c65fdb5-9d2c-3f34-8477-e0616491f859 | -5.98894 | -44.72405 | 2026-09-21 16:03:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| c1e060ca-dac9-3071-ae88-e639a6e8a740 | -6.19306 | -45.32949 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6b8ccdff-dd95-3d79-b5fd-1c00648d3d34 | -1.86271 | -48.14676 | 2026-09-21 16:03:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa6d965f-5afc-3089-9432-c74b5fb5f127 | -7.21121 | -44.08961 | 2026-09-21 16:03:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7ad3adcc-d5d2-3267-b3fd-2bc73efc56d1 | -6.15173 | -43.84656 | 2026-09-21 16:03:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 20b96751-9af7-3fe1-9985-8ebe2e2fa433 | -6.56482 | -45.56535 | 2026-09-21 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 555d4dfb-1ac8-3c1f-8fa6-26c59dcf5fc2 | -5.99251 | -45.07431 | 2026-09-21 16:03:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| dd438e0d-f995-3fd7-8933-17e8f95f94a1 | -3.56976 | -43.47242 | 2026-09-21 16:03:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| ae7fb73f-9332-3b36-bdd2-ddd947e68a71 | -3.32622 | -42.55096 | 2026-09-21 16:03:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8980bc2e-1e6d-35e3-8c2f-456199c694e5 | -2.61865 | -51.72341 | 2026-09-21 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 985b618f-93fc-334c-8c96-14768fd197d1 | -5.53626 | -43.1819 | 2026-09-21 16:03:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5cdaa83c-1221-357a-8f10-59fd1e49a105 | -6.17805 | -47.60846 | 2026-09-21 16:03:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8b9943db-58e6-3601-a9ca-9526db890bfc | -5.27758 | -49.33775 | 2026-09-21 16:03:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6f87004f-697a-3aa6-b32a-b5fe37d2d408 | -4.18853 | -52.06789 | 2026-09-21 16:03:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7463274f-a302-346d-a2f4-a55043842778 | -6.07671 | -38.30061 | 2026-09-21 16:03:00 | NOAA-21 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| e62f257c-4037-3e6c-8187-f9d51e2ad54e | -3.58488 | -40.32106 | 2026-09-21 16:03:00 | NOAA-21 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |


[Clique aqui para ver as próximas entradas](README172.md)
