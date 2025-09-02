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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dafd874f-c986-345b-a1fe-6854f02f28a8 | -11.6647 | -57.3533 | 2025-09-02 00:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 2f8035cb-f2b5-3943-b8a7-88234b64fcdc | -10.2596 | -47.5245 | 2025-09-02 00:50:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 92f672d1-da43-3295-807b-88e077b1f7ee | -12.9385 | -56.9655 | 2025-09-02 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 144237c7-e1e2-37b2-8524-3bf0b0e18b02 | -3.2305 | -47.135 | 2025-09-02 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 56883c64-1187-31bd-b718-f0f35f66b5e4 | -7.5477 | -61.3247 | 2025-09-02 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 58d43874-d6d7-3ce3-aef1-aedc673b86a3 | -6.8281 | -52.8143 | 2025-09-02 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 28fa532b-e815-3dec-83de-3f94f3e05117 | -14.2687 | -45.2636 | 2025-09-02 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 64eb2397-7cde-33bc-a921-dcfff3210d3d | -12.9382 | -56.9856 | 2025-09-02 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 27d41bd6-f7fc-3b7f-bd69-bf5f3273e992 | -5.6079 | -45.0265 | 2025-09-02 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| a2ae6787-3bf9-306a-b7e8-a9e258e9778e | -14.2692 | -45.2403 | 2025-09-02 00:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a82e2137-a3fc-3a98-a6ee-68cc75ed5166 | -10.0623 | -48.0978 | 2025-09-02 00:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 4270dafa-ae66-3f86-9fdf-626395cfd859 | -7.6783 | -61.0908 | 2025-09-02 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ba3fa71a-c7f7-332e-be75-8709c064378b | -9.1207 | -61.4864 | 2025-09-02 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 55175a3c-8f3c-35ae-9a09-8aef7e5cb178 | -12.9197 | -56.9471 | 2025-09-02 00:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 9af45465-2158-3f16-a956-b1a4454aa64f | -7.5292 | -61.3254 | 2025-09-02 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| d2d1013e-f5d6-3333-8336-42299309a733 | -17.9016 | -47.1569 | 2025-09-02 00:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 01779e6e-fbd5-3cd7-be13-c892a72af3a5 | -6.8093 | -52.8359 | 2025-09-02 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| a960dd3e-f78a-37d3-a724-6f2a9b11b749 | -17.8815 | -47.161 | 2025-09-02 00:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 838768fb-1ab5-321c-839f-53e4ebe1cad1 | -6.2224 | -43.3693 | 2025-09-02 00:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| a9ca12b6-e8e0-3e3b-9019-d7d403ac46d6 | -10.0617 | -48.1417 | 2025-09-02 00:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| bfdd08e4-bb6e-369b-a631-b5d0d0fd1caa | -6.8095 | -52.8154 | 2025-09-02 00:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 9871ea85-be61-344e-a0a3-220397bcc4d4 | -7.5476 | -61.3437 | 2025-09-02 00:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 207.4 |
| afc0db3e-9c95-3b58-a741-e1769bb70a3e | -11.1033 | -44.6548 | 2025-09-02 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 4c9a003c-7d6c-39cf-a14a-178723fed51b | -8.6487 | -62.8376 | 2025-09-02 00:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 72.8 |
| aa6ca451-b11e-36e6-9aff-f15152229b98 | -10.2786 | -47.5223 | 2025-09-02 00:50:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| fd19a7c0-f659-323c-bbcd-2745f8e0f078 | -10.45 | -54.7785 | 2025-09-02 00:50:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| f6568676-1db1-3a39-b3f4-7a95850d8978 | -10.062 | -48.1197 | 2025-09-02 00:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| dd1713b9-a56a-3cbb-bb9f-2f9a6aeb7f8f | -6.403 | -58.1979 | 2025-09-02 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 0cb5d033-1647-34d5-a0b1-2060087bac88 | -7.5291 | -61.3444 | 2025-09-02 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 09987866-05d2-31ae-9310-ac00f84df784 | -7.5476 | -61.3437 | 2025-09-02 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 198.9 |
| d4d97ed4-c77e-327e-bf91-f19d8bba7395 | -10.0617 | -48.1417 | 2025-09-02 01:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 1af31012-57c4-3814-856f-9a5ca2c6327c | -9.843 | -65.0528 | 2025-09-02 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| cbac1fdc-912b-3e5e-bc0b-1d20740c179e | -17.9016 | -47.1569 | 2025-09-02 01:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 91a1f866-c401-38d8-a705-af1b9776e1c6 | -10.062 | -48.1197 | 2025-09-02 01:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 69bd47d9-3604-3647-8daf-84d1b15cc888 | -12.9382 | -56.9856 | 2025-09-02 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 953ff070-12fc-3dd1-9193-f5f218da89a7 | -7.4778 | -45.3739 | 2025-09-02 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 18676b3b-8900-3fca-93b8-7212ec53680d | -11.6458 | -57.3548 | 2025-09-02 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 94dead7c-763c-30af-baf6-d0c8c86eaeb2 | -5.6081 | -45.0038 | 2025-09-02 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9d2d8705-3687-3d29-ad55-83d2ff196702 | -7.5292 | -61.3254 | 2025-09-02 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| acf542f5-93cd-366a-a76e-2aec958788a0 | -7.478 | -45.3512 | 2025-09-02 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| ddaf0ae1-3840-3ca6-826e-a5bc23424c32 | -22.5307 | -46.8109 | 2025-09-02 01:00:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| b00ad23e-34b6-377c-9305-3a9b9c6349ef | -21.456 | -47.4211 | 2025-09-02 01:00:00 | GOES-19 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 86d2365d-c026-3548-aa46-36ed72cb0f57 | -12.9385 | -56.9655 | 2025-09-02 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d662cd42-27d4-38c3-b51e-28a0d83ff724 | -17.8815 | -47.161 | 2025-09-02 01:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 72020672-9f67-3257-bb70-32f5f6a600db | -11.1037 | -44.6315 | 2025-09-02 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 68138f62-c348-3542-b46b-b4c17566a34c | -17.7096 | -46.873 | 2025-09-02 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0c1a548d-541e-3549-abbe-2ab2628d6054 | -7.4969 | -45.3495 | 2025-09-02 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 91ebe0a7-9342-3c4c-bb4b-9d61b6a1910b | -3.2305 | -47.135 | 2025-09-02 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| a2189041-25bd-3ab6-ad94-ee187ea8b6d1 | -10.2596 | -47.5245 | 2025-09-02 01:00:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 05541a34-5bd4-3a8e-998a-6c57cf35ba52 | -9.1207 | -61.4864 | 2025-09-02 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 84130ff2-2e8f-39db-8a0d-860a4e0326ca | -7.5477 | -61.3247 | 2025-09-02 01:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 196.6 |
| 8486f075-07b1-37c3-b74f-18188ff89cbd | -11.6647 | -57.3533 | 2025-09-02 01:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5b226d68-d526-3642-9ea6-b3518a1e6f3e | -9.8616 | -65.0522 | 2025-09-02 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 5be687be-3979-3a5d-b843-6be3429ad7fb | -8.6487 | -62.8376 | 2025-09-02 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 96706631-f02e-3c7c-9a8d-56a4313c98ea | -6.2674 | -44.5213 | 2025-09-02 01:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| a4f24ddd-8937-3f31-983c-4ac9011912d7 | -10.45 | -54.7785 | 2025-09-02 01:00:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 843ffe4d-fe81-39e2-8087-a20943785036 | -11.1033 | -44.6548 | 2025-09-02 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e72ad6f1-abce-34ff-a5eb-9ddf009e6264 | -7.4966 | -45.3722 | 2025-09-02 01:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1b2d1078-a194-3719-a43e-fc51b7eaf33b | -5.6079 | -45.0265 | 2025-09-02 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 456bf408-058c-3db8-ba3f-a1dd2b86bc22 | -7.6783 | -61.0908 | 2025-09-02 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 2dbaba5a-4ec1-33ae-b56a-303f7b6ef7a5 | -6.4029 | -58.2173 | 2025-09-02 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| ab0b42da-99c3-3c8a-975e-6929c98998aa | -17.7091 | -46.8962 | 2025-09-02 01:00:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 2ce4cdac-2ef0-3511-9746-154bae5d41b7 | -12.9192 | -56.9873 | 2025-09-02 01:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 7d105aea-68e6-35c2-95e9-a3eab4c6061b | -6.403 | -58.1979 | 2025-09-02 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| d6379624-9917-30c3-bc4b-50f080b239c1 | -8.6673 | -62.8369 | 2025-09-02 01:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 29505d91-51b0-3072-8fd9-45a867414826 | -15.5666 | -48.3469 | 2025-09-02 01:00:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| d835c62d-562d-3620-b435-0b1517bb763a | -9.8617 | -65.0334 | 2025-09-02 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 83f50223-2e12-36c3-9f7c-0d57475c38bb | -8.9664 | -65.961 | 2025-09-02 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 55fd9ec6-e619-3c4c-aa6c-fdadf54e578e | -5.6266 | -45.0252 | 2025-09-02 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| facd2db1-58f7-3bbc-8815-a943b3e861ac | -9.8617 | -65.0334 | 2025-09-02 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| a5ff0ca5-e6dd-3701-9eb5-b66b30935155 | -6.1859 | -47.2845 | 2025-09-02 01:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| d7017660-e8fc-38da-bb8f-ac277a683422 | -12.9197 | -56.9471 | 2025-09-02 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| b1005c7e-064c-3cda-9f82-d754c2dc2cb5 | -9.8616 | -65.0522 | 2025-09-02 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 425ac561-62ed-32ef-bd61-8378c1eb14eb | -11.0526 | -45.399 | 2025-09-02 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 5bec4b24-52ca-366a-af51-317800fc8eb1 | -10.2786 | -47.5223 | 2025-09-02 01:10:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 07569e36-429e-303c-b410-c2ffef2f0c58 | -10.0617 | -48.1417 | 2025-09-02 01:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 0d497aaa-6626-317b-9332-23dcfebd77ac | -11.1033 | -44.6548 | 2025-09-02 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 289e7c00-e7ec-3c1b-b1f6-04a3eb6c9846 | -17.8815 | -47.161 | 2025-09-02 01:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 593ccc76-40fd-3ea7-86d0-8f2195c204cd | -17.7096 | -46.873 | 2025-09-02 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 33e02bdb-c033-3b88-8545-2c1e6851529a | -10.45 | -54.7785 | 2025-09-02 01:10:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3a663d36-677c-319f-9ab3-bbd7e6b16b29 | -8.9664 | -65.9796 | 2025-09-02 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 3034fe86-bf0d-3479-b62c-62bb32e698a1 | -12.938 | -57.0057 | 2025-09-02 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 980fa9eb-3000-3f98-9c6a-7542305d1592 | -12.9192 | -56.9873 | 2025-09-02 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a3bd5d04-389c-3f5b-ac52-12d1cfa09503 | -5.6268 | -45.0025 | 2025-09-02 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 81b8a5cc-ae71-386e-b0a8-96e1b79882c6 | -6.403 | -58.1979 | 2025-09-02 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 58891c67-8803-3a8f-a1c3-28cff2db8c16 | -6.1672 | -47.2858 | 2025-09-02 01:10:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 484a6301-ae3f-3b63-83d3-eddeb6b58d20 | -6.4029 | -58.2173 | 2025-09-02 01:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 5a1791f3-342f-34a0-a68a-069e6c3d88b9 | -7.5477 | -61.3247 | 2025-09-02 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 182.3 |
| be36074f-c250-3589-95d0-cd5a04cb68c3 | -3.2305 | -47.135 | 2025-09-02 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8220637d-e97b-3d1f-8858-f77ee9ebc2e2 | -17.7091 | -46.8962 | 2025-09-02 01:10:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| adb8c831-a590-3a9b-bf08-95dcad8247c7 | -6.2674 | -44.5213 | 2025-09-02 01:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 46d9ca2b-9b97-3581-83ac-668762accfe3 | -12.9194 | -56.9672 | 2025-09-02 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 3ed03d29-0da7-3d2e-8d05-b796a1d51270 | -8.6673 | -62.8369 | 2025-09-02 01:10:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 48dfc0b2-d51c-3aee-90ad-a1e249916450 | -7.4778 | -45.3739 | 2025-09-02 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| a5ddcf40-ec15-31fc-a4ae-de53b943d8c4 | -9.843 | -65.0528 | 2025-09-02 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| b9fab65a-01c8-3cbe-a8fe-0b4177ac449a | -12.9382 | -56.9856 | 2025-09-02 01:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e2d4132f-9448-3531-8548-47f3904f6b34 | -9.1207 | -61.4864 | 2025-09-02 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 01e3bc6c-e4c6-3ed6-a023-bfe961fb8a3b | -17.9016 | -47.1569 | 2025-09-02 01:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 76504953-1aee-38cc-8055-25235aa8dbe3 | -7.6783 | -61.0908 | 2025-09-02 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 79e58b27-136f-3ec6-8b9d-582cff86939e | -15.5666 | -48.3469 | 2025-09-02 01:10:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 78.8 |


[Clique aqui para ver as próximas entradas](README8.md)
