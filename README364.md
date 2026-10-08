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

## Dados Diários - Página 364

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f993c58-cbbf-34bb-b1c0-54539932a2c1 | -2.77675 | -43.6325 | 2026-10-08 16:39:00 | NOAA-20 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81ee5ef4-a4f0-3606-884c-7716e2585532 | -3.48042 | -59.50843 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 854ce1cd-38be-3ff9-a3d4-b2985359905b | -3.32692 | -57.95952 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6b062d34-5da9-3142-a2b1-f2ad5bc0b2a8 | -1.38724 | -55.41256 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4acad740-ecb1-3bf5-af74-32022e0debae | -5.09726 | -46.2099 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 49.9 |
| b4fd882a-80df-39e5-8f76-b3a3839367d8 | -2.94534 | -54.17971 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 58ad7e46-764f-3190-808d-8d3f0369b342 | -1.77329 | -55.02011 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6f37f590-fced-32b9-a25a-b5df9aae9400 | -5.4379 | -45.68643 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ace140d0-3dcf-3a01-922c-ae3480607e5c | -3.78554 | -59.37437 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 23fdc70e-6701-304d-934e-2d713b92c95c | -2.15243 | -54.47478 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 536d6184-9cfb-361c-a9f5-9afafcba0dc8 | -3.02441 | -54.05125 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 0ec97dce-25c5-3cfd-b82a-aa1130d7a88a | -2.25938 | -56.74871 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1c13a23-d512-3e77-ab65-fb0a853b984d | -6.99561 | -52.73461 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f559306b-20ee-3f76-800f-6f4446070b2d | -3.43852 | -56.93816 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2fddf932-ae35-3278-80f7-b3698d3f6e43 | -4.08839 | -44.13036 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 52.7 |
| a8ea6fe1-e374-333f-9cd0-846187d05b27 | -3.75258 | -49.04108 | 2026-10-08 16:39:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ecaf0b55-93a9-3702-a13d-78e16af33318 | -5.13589 | -44.74117 | 2026-10-08 16:39:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 61936e19-4e80-387a-b634-a24bec7f64a7 | -3.97077 | -59.33451 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f86a1557-4fe6-38ff-8957-e57e62db131e | -3.71342 | -59.64927 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8d133f12-14d5-3ec4-bc94-82712d94f39e | -6.18022 | -53.42519 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| e36fce3b-3d2f-3e32-89db-1de30248eb89 | -2.88639 | -54.18084 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3e7cccd1-8afc-3db3-997a-7cc29a130e48 | -5.5464 | -43.22461 | 2026-10-08 16:39:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 66ef1112-9320-3b6d-85a5-ffad171bbe52 | -4.67178 | -39.71189 | 2026-10-08 16:39:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 4ca1e2b9-c4a2-32ad-9b4d-fb0817bd6e8f | -1.49356 | -54.55201 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ab726846-d564-3f07-b2f7-65e762e29a67 | -3.05863 | -59.26392 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e887786b-bf92-38c6-8638-f52017b1cfc6 | -3.72042 | -59.40194 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d1bd98bd-ad90-39be-9b20-ae77c12170d6 | -2.56824 | -56.16334 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 018403b9-d088-3b7a-8a8f-8d27bb44166c | -3.59086 | -54.68105 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b826b7f9-736d-369f-8043-334004f02453 | -3.02202 | -54.04391 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| b74e5c19-0f1b-35ca-971a-847dfc25bb87 | -2.99404 | -59.0419 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 85647d7c-0ab5-32a7-b12c-196315ddf8d3 | -3.79386 | -41.65686 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d9e4264a-7be2-3d1b-a962-29c022d8959e | -6.01564 | -46.76054 | 2026-10-08 16:39:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f32f126b-5c57-3f6d-9c51-c210f1471ff3 | -3.3015 | -53.86679 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 061042fd-64a3-3a42-8e7f-486d4048361d | -3.30874 | -53.8676 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d0c45dca-c48e-363c-bef0-9410d0b30738 | -2.74347 | -54.10587 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| c1831af1-a708-38d2-938f-471df93220de | -4.66777 | -55.92589 | 2026-10-08 16:39:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0df691b5-bf72-366d-9d53-58ff054dcc13 | -4.35659 | -43.80672 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 1cc1b838-2ed8-3762-84bf-f54652c46e03 | -2.10701 | -56.62774 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 6f35cc96-20a6-359b-9dac-2a1fc996924e | -3.09502 | -58.4245 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6f685ea-8092-3e03-985a-ef1369ba64df | -1.80746 | -57.11166 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 040ff319-4614-3f01-93f4-b895dfcb985a | -1.47762 | -54.64074 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2bfbc3d8-cb63-3e41-a098-4b519b556d26 | -2.58111 | -56.17558 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 34b6141f-66e9-37e3-8005-72c5dc666a14 | -3.01822 | -54.04185 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 144d0933-deff-3b21-ab18-232bfa40153a | -2.10939 | -47.96402 | 2026-10-08 16:39:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 010d6f84-c0aa-35b9-b78d-417bbf1fef57 | -2.5847 | -56.1748 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 5fb944d8-4947-3068-880c-98446b2c30e1 | -3.20689 | -50.55336 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 6209e3af-de2e-377f-bf28-acebb117e238 | -2.40823 | -48.16428 | 2026-10-08 16:39:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d07c3712-eb1a-3bf3-b0fc-445118030fe4 | -5.50471 | -45.54705 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3a6e1e45-f350-31d1-ba52-b2e806e5dd4c | -5.82131 | -53.8258 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c463bd0e-5f06-354b-b569-b930348f7538 | -3.10643 | -57.65632 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 364c0be5-8288-360c-a9a2-39fb4eabfaa5 | -5.70693 | -53.46778 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 6ae6eb9c-e4d8-330c-a71c-cfff2cebc2fb | -3.0306 | -54.06057 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f3c4fedb-a952-3a61-8a7a-09812b5341c2 | -5.09343 | -46.20695 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 8ec1fbf4-a0c0-343c-9a80-e28b9a9c06cd | -2.52498 | -56.2587 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 987e6f71-a55d-393a-bac7-c161b781e1de | -6.09808 | -53.50104 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c2f42614-348f-341d-8a73-863b6849b1ca | -5.77258 | -45.39049 | 2026-10-08 16:39:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 76274914-9795-38ac-9987-0d33cda42813 | -3.08832 | -57.65886 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| fd15b846-aab6-3f2f-b0fe-3214822bab39 | -3.28 | -50.02066 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b88db00c-e563-3f78-a96e-924cea15e922 | -3.29369 | -42.68273 | 2026-10-08 16:39:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8bfcba10-a7a8-33b8-9d8e-c419ae456236 | -0.09193 | -49.48811 | 2026-10-08 16:39:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| ff114333-ed1d-38f7-b105-64ba645f74ac | -2.97472 | -47.33718 | 2026-10-08 16:39:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0af1c979-f71a-356e-ade1-4c6d6e6a06fe | -2.08031 | -46.56843 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.0 |
| 5d5a675f-c0bb-344c-8976-a0a0cd019c1e | -5.94735 | -45.68933 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f8f2fb7b-836b-36f8-9f14-11eda76b850b | -4.27527 | -43.93521 | 2026-10-08 16:39:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5a91d9a0-8243-3505-858d-74ee35a2a631 | -5.40105 | -45.66726 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2aba4fc7-05c2-3c02-be12-49f2f594e393 | -3.65006 | -54.2827 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 30206540-2fe8-3ebd-bcd2-7a0a4e5ef340 | -5.47125 | -45.70478 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 74766bf9-1a37-347f-8cf2-6ddce94ac66d | -4.07824 | -59.83447 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2bf253fd-afe5-399a-ba8f-88b27a7739ea | -3.28907 | -53.70655 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| e696427c-3592-3cf5-be9a-30dc4b727d10 | -3.27028 | -54.06238 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 67668ebe-3f37-368e-b760-80da068aaaec | -3.26508 | -54.02691 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 79b126f5-2bb1-3dfc-8f07-f41f621f98f4 | -5.48564 | -44.60469 | 2026-10-08 16:39:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| f44a8ecd-05b7-3180-976f-1ee58acd3f2f | -4.15971 | -43.1926 | 2026-10-08 16:39:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ade51bb0-de86-30ad-9698-bde2608220b4 | -4.75337 | -40.50735 | 2026-10-08 16:39:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 22.1 |
| 31c6860a-cbfd-3fc4-a4ac-3f976d6d1af4 | -5.38228 | -45.9426 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f4b6f56c-b10a-3879-93b4-a2d510e20b5a | -3.01746 | -43.33014 | 2026-10-08 16:39:00 | NOAA-20 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 99c187be-f9f3-30d6-b4e6-3aa05dc14be2 | -5.49747 | -42.84588 | 2026-10-08 16:39:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| a33de01d-e5ee-3ba7-b8d7-9b1183bdb2e5 | -7.23454 | -55.11715 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 09ffa491-ce7b-3eb1-9b77-6d3d9375339f | -6.18303 | -53.44543 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| e1004ea4-695f-3c65-a8e0-79a60b8b68c2 | -2.49606 | -44.17385 | 2026-10-08 16:39:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| df1cb054-a59d-3a0c-929a-686cf07cf682 | -5.30075 | -45.72198 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 8de23ccc-07fd-38a4-8b65-43696777955f | -5.81645 | -53.82653 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 29d142f5-2187-3062-81af-170361719101 | -3.39762 | -43.00587 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2c00824e-b92c-3732-b248-6b6d2cd32d6a | -1.47787 | -54.64463 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 697256b8-37c0-3fb6-ba31-bfba96fe34d8 | -0.75389 | -49.39617 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 08540cd3-44a7-3009-95f4-26b590360af3 | -5.73614 | -53.46129 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 5372c515-4a7f-3475-bbf6-5aa1f1022da5 | -5.36702 | -45.73272 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a8242326-56a6-3eb1-ba71-13b453add9e8 | -3.2636 | -54.01683 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 7732f220-1913-3e94-be86-5a59b6f348c8 | -1.8364 | -55.63717 | 2026-10-08 16:39:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2ae854a-1bf8-3df0-b7c5-bcdc1960b312 | -6.22342 | -53.27295 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e6756776-b0f9-309a-a553-4a216db6fa36 | -3.64898 | -59.1666 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 866c83bf-5fb3-35e0-941e-cc513d144a37 | -4.3308 | -55.03641 | 2026-10-08 16:39:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19bbe63b-bd31-3069-8bc8-3922eb8c4704 | -6.15287 | -51.72926 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ddd68837-2c97-31ba-ac48-ba3e0599a663 | -1.85814 | -57.04618 | 2026-10-08 16:39:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 13708d4c-5313-3fef-8f86-c2264bede378 | -1.96568 | -54.33625 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ae77cfa7-b761-3ca6-ad5a-7288db42db59 | -3.44488 | -45.08854 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 63d5bd25-32f6-369f-b7d2-106172816739 | -5.09568 | -46.19956 | 2026-10-08 16:39:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 63b44247-5208-3bad-9344-fdc1d28379e3 | -3.12075 | -54.1776 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| a5ae55e1-06aa-3b6a-a0a2-85a68b5d0356 | -5.99073 | -55.35924 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6c73b24-8df6-3167-a47e-92c823c7a8b8 | -3.00077 | -54.7699 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |


[Clique aqui para ver as próximas entradas](README365.md)
