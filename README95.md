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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a46a721-6987-330b-b23f-1be32f8daeaa | -6.81138 | -55.29797 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 4a882413-2c57-32d6-b53c-665200c3e8fc | -4.37264 | -43.91608 | 2026-10-05 16:39:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2b045647-47c1-36b7-ab0e-619bc63e2f4b | -4.43827 | -43.42547 | 2026-10-05 16:39:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 3abe991f-7f89-358c-9d54-e1055a21ba45 | -3.67485 | -54.5361 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f1495ad9-8d8b-383d-9cda-d6bb7f2e5e19 | -5.83954 | -45.01658 | 2026-10-05 16:39:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 165.7 |
| b0a25a0f-4a23-393a-8b0f-6bee1adb957d | -4.56939 | -39.58482 | 2026-10-05 16:39:00 | NOAA-21 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 8c18377b-821c-37f8-bae0-75d645207feb | -4.84294 | -41.81565 | 2026-10-05 16:39:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 8590df7a-b872-3490-879b-4ba5e35003ed | -3.63453 | -38.77362 | 2026-10-05 16:39:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bd50d5e3-7af5-3b4a-8240-e639ad56890d | -3.8416 | -50.31464 | 2026-10-05 16:39:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8fedb474-78d2-318f-ac0c-6d6c85a1b635 | -7.33364 | -55.7353 | 2026-10-05 16:39:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c8beaadd-3eea-3699-9dc9-4e6937122193 | -4.4578 | -54.9662 | 2026-10-05 16:39:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 575ed5da-6025-39a2-a9ff-8fd4b8a135c8 | -2.04698 | -54.30376 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a6affa8c-3809-3c4f-8810-b32bc4540f2e | -3.50982 | -54.60711 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 06fe5568-2e21-36ca-b66d-938dd9f356a5 | -1.05439 | -53.59076 | 2026-10-05 16:39:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ffbc99cf-5156-3337-ba41-c10f89b668b4 | -4.07089 | -55.77116 | 2026-10-05 16:39:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 3239668e-a8f8-34c8-8434-efc30bbf3760 | -3.72139 | -45.4031 | 2026-10-05 16:39:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88347a4f-1b5d-300c-a540-70a40b8f0f10 | -4.33903 | -44.38375 | 2026-10-05 16:39:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b3f0513e-d6fb-36f1-b44f-4afddec8692f | -1.78127 | -53.77551 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 66cfc2cc-f1d8-3db9-8e5b-9e4abd35b3d9 | -1.32996 | -46.82599 | 2026-10-05 16:39:00 | NOAA-21 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 85026b44-5b6a-3e5a-b630-902a999dc979 | -3.29931 | -53.84944 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e7c8769-cb43-30e9-8226-862dff3f8a1b | -4.13962 | -44.99567 | 2026-10-05 16:39:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 48862904-b6dc-3578-8d13-930e0e402522 | -3.6775 | -60.61479 | 2026-10-05 16:39:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cf546e6b-eae4-3e13-83a5-3e3d3555e039 | -2.92804 | -54.14772 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c7cf23b6-1ace-3f66-ac56-9f2e90fb79f9 | -5.03277 | -42.75991 | 2026-10-05 16:39:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0fda3f25-3526-3309-9924-3d23e2bf06e3 | -2.9468 | -54.15715 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 338fd4e0-cdbe-3059-8ffa-e553d21ddeeb | -2.63129 | -49.3101 | 2026-10-05 16:39:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c3450aac-ba25-3eda-8e03-734b02321694 | -2.98525 | -54.03629 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 80ebcb4f-aefa-3ca5-a188-9bab5102b1fc | -5.94536 | -41.3474 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| ca0f3a72-2c1a-3750-a7ac-dd412b943855 | -3.20951 | -42.87122 | 2026-10-05 16:39:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| c0607c43-5193-3872-a1c5-3eacee910fd6 | -4.62214 | -38.93642 | 2026-10-05 16:39:00 | NOAA-21 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 583d1a8d-1354-39e3-ad7e-934925daf590 | -3.13855 | -53.72167 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| f0fce731-22ad-316e-b1ad-fdae559dcf20 | -2.04333 | -54.30828 | 2026-10-05 16:39:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2b2cc988-7c53-397b-9e02-29c6056841f9 | -4.29953 | -42.18608 | 2026-10-05 16:39:00 | NOAA-21 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 95a9ca51-ec7f-39c6-8518-ae5e35037a5b | -3.76954 | -39.84624 | 2026-10-05 16:39:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 901efde6-1504-3f44-81d1-12ae869a8b35 | -3.62272 | -55.28524 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 663e7b28-eceb-331b-a365-8e856ed7f0ac | -2.76562 | -57.6615 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 227f2291-8e69-352c-bf59-f2df5e4ff71b | -3.96657 | -53.46532 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8c70738d-772d-321b-ae96-f05c22edf393 | -3.37247 | -58.1921 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f8a452b3-6e89-37d1-ba5b-6d614a7419b4 | -1.63656 | -55.52989 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 3a31da2b-d1f4-396a-b643-1e1560ae0c8c | -2.15995 | -50.23012 | 2026-10-05 16:39:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a834b5a2-5721-3b5d-9de1-4c0be3508c39 | -2.00257 | -55.62523 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e99e0ee4-b028-32a1-b3b6-f94f10bbcae1 | -4.96219 | -40.55844 | 2026-10-05 16:39:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 40.0 |
| a0d704a5-7d11-31c6-8a1e-57b8f17fdab2 | -3.583 | -39.23212 | 2026-10-05 16:39:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 10.6 |
| be5438cf-c661-36b8-a1cb-07c4841fc351 | -1.10574 | -46.64692 | 2026-10-05 16:39:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3f2e872e-a0d8-3931-96ad-825faaf0ae66 | -3.5885 | -54.31571 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ac4f37ef-77d3-32ad-8a38-737494f2da87 | -1.62115 | -47.6753 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 60833094-5821-38ae-abf4-7f19ab942b38 | -3.31218 | -44.22601 | 2026-10-05 16:39:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 569bc94c-c46a-36b5-af58-8df82c8c5aac | -4.23886 | -42.13013 | 2026-10-05 16:39:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2e313319-eecc-3b4c-8c30-e91e8c054217 | -5.95046 | -41.35097 | 2026-10-05 16:39:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 04e36491-29ba-32a8-a897-1339e8d6ed29 | -1.72389 | -55.36311 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| ac93efb0-05b2-3526-8983-791ef79b435e | -7.23555 | -55.19549 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 4d3dfca8-5f04-3a93-badc-abed1f4c7cfd | -3.59181 | -55.29367 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| fd78a83a-c179-3ddd-bff1-89a85b84cf61 | -1.99874 | -55.62429 | 2026-10-05 16:39:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 408ab6fa-bef9-33ea-9a3e-a4df1af7133a | -2.80269 | -54.08974 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 06a42dd5-5118-3f03-a314-72ddd0e27989 | -2.77252 | -57.671 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| f3bfba66-c6ab-3593-96b2-5d01658c6cf6 | -4.32785 | -43.82518 | 2026-10-05 16:39:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 59074d1d-5cc0-3b84-aa6e-0c8407c3b846 | -1.4562 | -55.26581 | 2026-10-05 16:39:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 900c7f34-a8af-3800-9a10-b1b311b063d1 | -4.8947 | -43.46335 | 2026-10-05 16:39:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9871b55c-5521-3ae0-979f-283ef139a8fe | -3.6698 | -54.53246 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 17d9a486-d062-3fe3-aaac-addfbdafa30e | -3.53513 | -39.89124 | 2026-10-05 16:39:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 9fc72e15-530b-3909-9588-050bf71d14cd | -3.07347 | -58.42701 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 58861997-e782-3676-ad3c-192389282bb2 | -6.27682 | -43.25071 | 2026-10-05 16:39:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f50908e6-c7d8-32e8-8c68-596f96d9b5b7 | -3.3792 | -58.19896 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 8c423bb2-2b37-39fc-818b-b06972575dd6 | -3.2401 | -58.7606 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 4547dba0-e30a-3721-890b-1e7e70ccba84 | -2.77053 | -57.65736 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 7e3ccb4a-1b08-3747-804b-3b37c61ad732 | -3.1343 | -53.71162 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 442c5827-46f8-38aa-b286-574b43a636c2 | -2.77152 | -57.66417 | 2026-10-05 16:39:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 327dc5ab-4001-38b0-9179-3cd7068fee55 | -3.5092 | -54.60285 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 76db90f0-421c-3061-9e9f-0e054a18d9c1 | -3.49844 | -54.62198 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 8f2fdbd9-5c87-33b6-b338-2a2f9b3be4d6 | -3.62306 | -58.61718 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d9d252ee-0717-3772-a7bb-8061295081b7 | -3.57311 | -41.24382 | 2026-10-05 16:39:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 19.1 |
| f4a4ea42-a539-35eb-96ec-fbf7bd22b951 | -3.51107 | -54.61568 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 85864852-b45d-38cd-a34a-7756659d03e4 | -5.8304 | -44.89128 | 2026-10-05 16:39:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6a029e53-ee70-3628-9436-c505fcb73535 | -1.05543 | -53.58824 | 2026-10-05 16:39:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 40ce3385-21be-3f3a-b80d-fbba15117cc4 | -2.9806 | -41.80103 | 2026-10-05 16:39:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 6ab0bac3-4616-3654-b92f-ff012a224090 | -4.18098 | -44.30103 | 2026-10-05 16:39:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| fa485ae8-09cb-371e-b6ef-982cfa69f184 | -3.1651 | -41.39846 | 2026-10-05 16:39:00 | NOAA-21 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5a8fe380-47f7-35d3-881d-10c599a8926b | -3.13278 | -53.71106 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 307ebfa7-0361-33d2-aa32-36b9f96121fb | -2.78159 | -54.09282 | 2026-10-05 16:39:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| b4b96081-1c37-329a-9063-dd6518b8a2bf | -3.06383 | -54.15736 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e66a97f5-9b36-39af-a8f0-cead071aa3a1 | -3.37619 | -54.10552 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 084c60d1-048e-3806-ab2c-de0edb930921 | -2.19112 | -56.64106 | 2026-10-05 16:39:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a124ee69-7de5-3d98-b831-14694dae5ff4 | -4.24643 | -44.81776 | 2026-10-05 16:39:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2db57124-f27e-3792-8ffb-2c6c6c892afb | -1.61694 | -55.91907 | 2026-10-05 16:39:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 941b06ac-3085-3188-8344-eca4cdc49493 | -2.05849 | -56.88424 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 173c3e35-803f-3897-89ce-fea6205b43fc | -2.8985 | -54.12374 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7ad6666e-6d24-3efa-9471-1edc3b17f787 | -3.05573 | -54.21943 | 2026-10-05 16:39:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| d166ea1c-1165-3fe6-aa09-ca3dfc89e05b | -2.28016 | -56.79015 | 2026-10-05 16:39:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| de6c0382-e114-3f17-8b30-517be5632ce5 | -3.87345 | -55.83241 | 2026-10-05 16:39:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e520fd26-d40f-3319-a1d8-ffa7e17e2af4 | -7.22067 | -55.18459 | 2026-10-05 16:39:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 8b19a4a1-c26d-3bb4-8de2-a76dffcfbfd0 | -0.38123 | -52.072 | 2026-10-05 16:39:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| cdbc9899-d0d2-3a76-81c1-d947eb176078 | -3.61302 | -54.60601 | 2026-10-05 16:39:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 5812c549-2fb1-3517-b92e-804b1207fe09 | -3.12455 | -53.75872 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 752261d2-ae4f-34a7-bb03-11ab40c3c959 | -3.97742 | -42.8688 | 2026-10-05 16:39:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b145cb4-aa2d-3840-8c00-dd45765c7598 | -1.40474 | -47.21988 | 2026-10-05 16:39:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a0dbd892-75e9-3280-b576-0237c3a97c4c | -3.54017 | -39.89041 | 2026-10-05 16:39:00 | NOAA-21 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 4f2f066c-bc28-3cdb-af4d-bbf1112c7b93 | -3.37301 | -58.19589 | 2026-10-05 16:39:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 2a31f572-b6c7-345c-a304-a902e294f65f | -5.60957 | -42.92525 | 2026-10-05 16:39:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f666c157-adb1-3430-a13c-9c0fd948d767 | -3.30349 | -53.84883 | 2026-10-05 16:39:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f16a3afe-4331-3dea-af20-d1b2f1b64def | -3.82032 | -41.80282 | 2026-10-05 16:39:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 133.9 |


[Clique aqui para ver as próximas entradas](README96.md)
