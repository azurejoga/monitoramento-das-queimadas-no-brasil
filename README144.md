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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80322403-ff20-3e53-b278-7d6355f8a967 | -9.8991 | -43.7237 | 2025-10-03 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| da016f9d-ae1d-3e91-ac61-270a1d15d4c2 | -11.9155 | -46.3272 | 2025-10-03 12:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| a5be5623-8476-3640-992a-7a72a6e13070 | -13.3414 | -48.1411 | 2025-10-03 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 672e1814-6b33-329b-ace2-411c3edc04a4 | -7.7682 | -46.2703 | 2025-10-03 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 39b51412-061d-3959-9b9d-6075c23ad015 | -9.9959 | -50.2462 | 2025-10-03 12:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2ceba820-5b90-3fc9-9adc-e3f92b80f3a7 | -10.9483 | -51.0634 | 2025-10-03 12:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 263.2 |
| b40f3afd-e857-32ba-9b9d-d97b410c3b1a | -16.0387 | -51.0484 | 2025-10-03 12:20:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| ceb67803-64c6-387a-b955-a77c30030273 | -13.1973 | -50.9095 | 2025-10-03 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8525e262-d0a3-36c5-9291-f99ea65cbee3 | -12.5305 | -47.2988 | 2025-10-03 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 389185fc-d265-319a-aca6-e5e0470fdccd | -13.3422 | -48.0965 | 2025-10-03 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 9862e544-09cf-3f38-ba15-fc1944773360 | -14.1244 | -45.66 | 2025-10-03 12:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 61bc167b-7053-3484-ad97-079bc83599c2 | -7.7496 | -46.2496 | 2025-10-03 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e2c12f76-2a30-3145-a4d9-55cfecdc477a | -12.5301 | -47.3213 | 2025-10-03 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 6e5347f6-1806-3478-a2f5-a46c5338bacb | -14.607 | -46.7249 | 2025-10-03 12:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 26622677-bfe9-385e-a90f-785b96e631e9 | -13.7666 | -48.0777 | 2025-10-03 12:20:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 49967f92-cab6-33c6-843f-619500ce7e1a | -7.8165 | -46.9781 | 2025-10-03 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 63a1aac3-0383-3baf-bc42-e31df1620da7 | -13.1534 | -47.9015 | 2025-10-03 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| c93b3096-9a0d-3046-a420-4c9eacf752bd | -9.9965 | -50.2034 | 2025-10-03 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.5 |
| e7a65829-79a4-3f2c-a40b-01ce5eae6802 | -8.5959 | -44.7833 | 2025-10-03 12:30:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 98.3 |
| d633e8a8-be72-3cdf-9a74-6c6224397973 | -7.7494 | -46.272 | 2025-10-03 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| bea06d41-b9fd-3193-a0bc-49078145012a | -13.9843 | -44.941 | 2025-10-03 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| cec77638-3db6-3bbd-b704-544adafabb9e | -7.2911 | -45.2775 | 2025-10-03 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 251.4 |
| 0ff81d7c-9316-3d5a-8140-feab3693cf58 | -8.8343 | -46.7694 | 2025-10-03 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| a7792791-d173-37d0-950d-983e5c119d8b | -13.7472 | -48.0806 | 2025-10-03 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 87d71ca0-f1cc-33c1-a14d-00828640f598 | -14.6497 | -44.7499 | 2025-10-03 12:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 121.1 |
| d5946bd6-8d86-39c4-bb9a-a0259fd29d1b | -7.2913 | -45.2548 | 2025-10-03 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| a92e5a72-6a4e-3b8f-9f69-83b3ace31220 | -9.9959 | -50.2462 | 2025-10-03 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 290ea5b5-55cc-3d8e-a277-5344aad5abd0 | -12.6127 | -46.9951 | 2025-10-03 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2406a8fd-da84-307c-89d1-04e826473a7c | -7.3101 | -45.2531 | 2025-10-03 12:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| f24c4449-06ed-3fb7-ac2e-5e19017d65b3 | -11.9167 | -46.259 | 2025-10-03 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| ce05b9d7-fe75-3589-b862-5f4d7cec2089 | -7.7682 | -46.2703 | 2025-10-03 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8355be87-7910-3c76-bb27-63acfc098477 | -12.6131 | -46.9725 | 2025-10-03 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 7d65fdeb-c6c2-354c-b39a-bbcdfd6a82a9 | -8.6531 | -47.7163 | 2025-10-03 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 39c40230-d900-3a89-8dc1-f3e055f503c0 | -8.6908 | -47.7126 | 2025-10-03 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5953f641-de61-3d84-b0f1-b502b710837f | -12.5305 | -47.2988 | 2025-10-03 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 0d6c7a9d-ea7d-32a2-ac4b-98a3c59094cb | -14.6503 | -44.7263 | 2025-10-03 12:30:00 | GOES-19 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 27220c69-22ef-38d6-91f7-9b79b99ec073 | -11.1275 | -47.8634 | 2025-10-03 12:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 2294b6c7-aa0b-30df-80ee-bca0be061e6e | -13.1534 | -47.9015 | 2025-10-03 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 49025fdc-0954-3a95-935f-ff64eeb95773 | -7.7496 | -46.2496 | 2025-10-03 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 089561cf-8f3e-3d82-9d89-3d4267ad2043 | -9.9182 | -43.7212 | 2025-10-03 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 158.5 |
| a77b7abb-cd42-3790-a35b-b34c05aa0986 | -11.9155 | -46.3272 | 2025-10-03 12:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 679f0485-afc6-37b0-bc28-f3c47ad271a4 | -9.062 | -46.6565 | 2025-10-03 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| bb940ea9-0d54-3549-b879-cf58c6374822 | -12.6319 | -46.9923 | 2025-10-03 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 62d9cdb1-cd73-32b5-9127-e28dcfb7b18b | -16.0583 | -51.0454 | 2025-10-03 12:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 3ae8fb8b-b401-30e9-9f0d-6e2cab07490b | -12.9314 | -46.3818 | 2025-10-03 12:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| ea931a3a-1ccd-319c-b0da-6918fd5dd77d | -12.7627 | -50.5567 | 2025-10-03 12:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f1b0b0fa-068a-3e4c-b2d9-4071101d2d01 | -13.3418 | -48.1188 | 2025-10-03 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 0280cf14-1b9e-337f-bca5-698009e9be09 | -9.9186 | -43.6978 | 2025-10-03 12:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 6b0343e7-27cb-311a-a063-5d2dc5130975 | -11.5462 | -46.6943 | 2025-10-03 12:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| c3c2f3cd-b4e5-3776-bf48-be144fc76a91 | -9.3357 | -45.9532 | 2025-10-03 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 8744dc24-91b9-30b7-948a-0279a335c422 | -10.9483 | -51.0634 | 2025-10-03 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 219.7 |
| e8ac3a9d-0795-3416-9d68-1d42adb89e1a | -13.1973 | -50.9095 | 2025-10-03 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 8741917a-80ff-3b31-a3e9-fb287e5f28ce | -7.7758 | -42.4914 | 2025-10-03 12:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| b9444741-8606-3cf7-84cb-75b690a09195 | -14.8063 | -51.424 | 2025-10-03 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| b84e0f0d-a87b-33b5-949c-e2320c4efbc3 | -13.5828 | -47.5916 | 2025-10-03 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7191d1c4-eb13-3932-ad32-15599ad7b08d | -14.607 | -46.7249 | 2025-10-03 12:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 97.5 |
| e3f02455-2e0f-30ff-bb63-d2ce85b3ac82 | -13.1727 | -47.8987 | 2025-10-03 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 89e51fc1-b937-3df5-8e45-931197441128 | -9.3547 | -45.951 | 2025-10-03 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| cb463905-0b79-377a-b00e-a3295fad85fc | -9.8772 | -47.8103 | 2025-10-03 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 28fd96c2-4011-350f-842b-6c0f45b7a16a | -13.3414 | -48.1411 | 2025-10-03 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| e52ae1b3-044f-30c9-ab3c-02dea841a982 | -14.0037 | -44.9376 | 2025-10-03 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| c082e39c-b5bb-3a0a-890a-b9d805774c68 | -12.5301 | -47.3213 | 2025-10-03 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 1a786a47-adea-3f9a-b8f6-86ab086c2bb2 | -13.3422 | -48.0965 | 2025-10-03 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 7358f42b-4a90-38ef-8c4a-2707f3977039 | -9.9962 | -50.2248 | 2025-10-03 12:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 69cddb66-1e38-3971-82e3-67ad8c6cc8e4 | -14.2316 | -46.1024 | 2025-10-03 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 9c610842-67a5-3a2e-af4c-7caa48009d1c | -8.1699 | -44.1608 | 2025-10-03 12:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| cd0a7a8a-c841-3f4d-90c8-e0e9c1a521d5 | -10.948 | -51.0846 | 2025-10-03 12:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 740da8f0-6949-38fe-8de2-d069f521c64d | -14.0042 | -44.9142 | 2025-10-03 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| b3c4c81e-ecc3-3bed-9a41-30b5fdd35131 | -8.6911 | -47.6906 | 2025-10-03 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 46538cb8-2826-3339-bffc-ce13fb01d812 | -9.8991 | -43.7237 | 2025-10-03 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 4a92417b-5afb-35cb-a1ab-6ec429dacefc | -9.8772 | -47.8103 | 2025-10-03 12:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| b7c3ff4f-9599-3dc7-a162-a05e9543e06c | -11.9159 | -46.3044 | 2025-10-03 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 080b1006-eecc-3510-86db-866172276c5c | -11.8626 | -44.9844 | 2025-10-03 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 500831ac-eac7-3237-9963-4aa7ebad2676 | -9.3395 | -45.6812 | 2025-10-03 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 135.6 |
| c33e3da8-a656-33cc-8ce8-69df42595b01 | -9.062 | -46.6565 | 2025-10-03 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| b0279b98-c7e6-36ff-871c-e57d2e560979 | -11.9151 | -46.3499 | 2025-10-03 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 1d14991f-4ff9-35f6-9bc6-e472b9085002 | -7.2913 | -45.2548 | 2025-10-03 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 175.8 |
| 7884cc3f-349f-38ee-882f-452357de987e | -9.9959 | -50.2462 | 2025-10-03 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| dc2d7ac3-23a4-39c7-a4f7-13113ebb20c6 | -8.8343 | -46.7694 | 2025-10-03 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| d1795784-fc9c-3b7b-9c62-1e5b5048d642 | -10.9673 | -51.0614 | 2025-10-03 12:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 24804fcf-cae6-39cd-8574-32f712d2992b | -11.5462 | -46.6943 | 2025-10-03 12:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| d66f104e-474b-359b-b61a-71839a563dec | -13.3418 | -48.1188 | 2025-10-03 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 533fa539-f6d5-31c8-ae85-ad4917284d0c | -9.4548 | -45.5545 | 2025-10-03 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 2a686c57-dab1-30fc-9551-242213e3ad3c | -12.5301 | -47.3213 | 2025-10-03 12:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.3 |
| ed7f7efd-0592-35cd-9748-b5b7067b5592 | -10.2773 | -50.3673 | 2025-10-03 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 03dfe974-0c7e-3c9f-a8c9-14718be98d4f | -13.7858 | -51.3047 | 2025-10-03 12:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 5a58a8a2-9737-3f63-8aeb-fdab6d6dd57a | -14.607 | -46.7249 | 2025-10-03 12:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 1cd52693-4c38-3127-b13c-609892b75cf0 | -8.1699 | -44.1608 | 2025-10-03 12:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 2c065bd9-7b13-36f0-aafd-f4c07430e958 | -9.9962 | -50.2248 | 2025-10-03 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 21d286dc-7bb0-3012-84b1-5ba78b49d228 | -16.0583 | -51.0454 | 2025-10-03 12:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c151d5bc-7d1e-3e3d-852e-586eefe47639 | -9.9965 | -50.2034 | 2025-10-03 12:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 4ae8d524-e864-327a-aa5f-e00825883cca | -11.1275 | -47.8634 | 2025-10-03 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| edcc9c5f-37dc-344f-bffd-9cad56fada85 | -14.2172 | -44.9463 | 2025-10-03 12:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 28ce9573-3702-3230-82e7-2c9f072fd6af | -7.3101 | -45.2531 | 2025-10-03 12:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 495d6757-7352-318a-bb20-4aa31a180b9f | -13.9843 | -44.941 | 2025-10-03 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 6c0a2df5-ce3e-34dc-867b-4d6bf81d835a | -9.9186 | -43.6978 | 2025-10-03 12:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 42beb34f-ce84-3cf3-bcb3-5a8c13e9bcb2 | -7.7682 | -46.2703 | 2025-10-03 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| fb3ae8c6-4318-323d-8e20-6d9fed0a3696 | -7.7494 | -46.272 | 2025-10-03 12:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 2707b692-3b63-381a-98bd-865a48707a10 | -8.5959 | -44.7833 | 2025-10-03 12:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6077dc35-c062-3daa-ad0f-5f43ba1b6cf1 | -11.9155 | -46.3272 | 2025-10-03 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 293.3 |


[Clique aqui para ver as próximas entradas](README145.md)
