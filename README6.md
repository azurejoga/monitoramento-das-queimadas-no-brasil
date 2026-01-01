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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 470c3d17-208b-3e18-958c-90fcfe50f7ac | -5.71174 | -49.10203 | 2026-01-01 04:46:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1e0fd5a-ffff-3d7d-83ca-77b8b62151ad | -3.02261 | -50.51241 | 2026-01-01 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4738b166-e40d-30ff-aeb7-dd0197e0ce87 | -9.57181 | -44.59803 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 7f074a16-949d-306c-a42e-e3f1071d6af8 | -2.41452 | -48.27699 | 2026-01-01 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8855785e-0535-30ce-ac51-98facb3b0473 | -9.57115 | -44.60291 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fd7f7c0b-2ce8-3789-98e8-cd1cbbefa38e | -2.44724 | -54.72144 | 2026-01-01 04:46:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 600691e5-a412-38da-861f-a0bfec142533 | -3.18322 | -50.40003 | 2026-01-01 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5fbf4839-da8a-38a2-b9c7-f65e10167f98 | -9.57649 | -44.59875 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c40db7be-0d54-3536-a9c5-1bbef1b88372 | -9.5693 | -44.60009 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 52ef8e6f-336b-3971-aa72-bbc6c7f7ab2f | -6.29455 | -46.99959 | 2026-01-01 04:46:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6166170b-9e81-3e52-ba90-6351893a4c78 | -5.72216 | -45.03488 | 2026-01-01 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d9897f29-1204-3d83-8ab6-43b592cbad6a | -2.55086 | -48.93119 | 2026-01-01 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4aeab28-d84f-3364-88ec-e3332600dc80 | -2.91227 | -49.3783 | 2026-01-01 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b78168b6-59d8-3662-b022-b6090464f6b5 | -5.72584 | -45.0396 | 2026-01-01 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 69788c93-919f-34e2-a4af-5a85e44bae15 | -8.11887 | -47.99176 | 2026-01-01 04:46:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fd4ec3d1-4d9a-342f-a2ef-f379ae9cfaf5 | -9.57467 | -44.59591 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d62caa27-5435-3f6c-a61a-5c8d363455de | -4.21417 | -47.76508 | 2026-01-01 04:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4807e453-701c-342f-bf9d-b6fa75180bce | -9.56582 | -44.60706 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 268be1d8-adc2-33ef-a387-b6dc609e43fb | -9.57584 | -44.60363 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 00908abb-c4ea-302d-bf4c-e57f14281802 | -9.57398 | -44.6008 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 2c461c96-5ac8-3964-b78f-9e5bc324e7f9 | -9.5733 | -44.60566 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a9e906a4-a005-33a2-8be4-153da859e90a | -3.02591 | -50.51293 | 2026-01-01 04:46:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71116c7b-cead-3e0e-8f53-7e3ed678f972 | -9.56647 | -44.60219 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c83e161c-1429-35a1-85a9-5b86c1a49c24 | -5.08823 | -50.01435 | 2026-01-01 04:46:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3314a587-d5ae-3b67-b321-4da1cf046fd2 | -3.86989 | -54.23262 | 2026-01-01 04:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| a7fd1754-2d3c-3acc-a1d4-32ff77c59bfd | -5.72646 | -45.03552 | 2026-01-01 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bef81773-1427-3587-bd07-44a05bf297ae | -2.55141 | -48.92762 | 2026-01-01 04:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18540072-1737-3869-bb67-48f50305333d | -5.92998 | -43.40429 | 2026-01-01 04:46:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b23d939-f217-3354-9b09-cec5a7f67792 | -5.14933 | -47.25402 | 2026-01-01 04:46:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23c5cc09-a234-32ff-ad79-f4ea3e60263c | -9.58119 | -44.59942 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d5134069-10ba-3134-8d69-db01d8ee10e4 | -4.93847 | -47.36277 | 2026-01-01 04:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51b3e7a9-a012-3b7a-930f-7fe3e4cd7b2f | -3.41905 | -49.48558 | 2026-01-01 04:46:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06e36bff-5046-3d55-be0e-a0f080b44d6b | -9.56999 | -44.5952 | 2026-01-01 04:46:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 03b1b248-003f-3586-8eb1-14b53170961e | -5.72155 | -45.03895 | 2026-01-01 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7556784f-0ee1-38c4-ab6a-df3170b52c0f | -7.57097 | -49.39813 | 2026-01-01 04:46:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efda6915-bafd-30c1-8fde-c96caa27667c | -2.41393 | -48.28071 | 2026-01-01 04:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06070afa-3265-3c95-9dc9-4414f1533966 | -3.86788 | -54.23486 | 2026-01-01 04:46:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 85570908-0eb9-3825-9ac8-15322bc53df9 | -5.72522 | -45.04371 | 2026-01-01 04:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 474741bf-ee1d-3b89-82c1-3ebb1664456b | -7.14179 | -45.2612 | 2026-01-01 04:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68ba27c0-f780-3241-8832-8372b0944dd0 | -5.93074 | -43.39904 | 2026-01-01 04:46:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48427310-a046-3c5c-a6a2-84a246a43770 | -12.96196 | -48.68261 | 2026-01-01 04:48:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54009cd8-21d9-3fe5-9ab7-5b1501ecbfdc | -14.6422 | -55.82472 | 2026-01-01 04:48:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57dfe031-3cf6-324b-8f65-d3916637c610 | -9.70391 | -57.93459 | 2026-01-01 04:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52e2f336-33e7-3635-b08d-d31040eff3a2 | -13.62762 | -44.32604 | 2026-01-01 04:48:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d761c0eb-db6e-3def-bc87-c6f11cada39b | -10.31927 | -54.15648 | 2026-01-01 04:48:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53eea3d3-ee2c-3d34-a847-eae74d340baa | -11.40447 | -54.99774 | 2026-01-01 04:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 24f19164-41a1-3881-86b6-ff74dd43c2a3 | -14.63515 | -55.82347 | 2026-01-01 04:48:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5e2e7ce-bcca-3d5a-886d-0a1c07d1958c | -14.82273 | -52.86807 | 2026-01-01 04:48:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ff5c81b-83d9-3d7a-a198-2ea4becb96ec | -12.3216 | -47.90076 | 2026-01-01 04:48:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 225e8a7a-117a-38ce-b31f-1364f7039baf | -14.50656 | -52.54555 | 2026-01-01 04:48:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d9f9c48-2188-3bb1-9930-1391d817b4e1 | -14.50988 | -52.54609 | 2026-01-01 04:48:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd7d1e0f-bdff-37a6-9fec-09e734e7f04f | -11.06622 | -49.57496 | 2026-01-01 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c8a7a9b-6a5e-3de3-b001-3b68e9b3cb93 | -11.40514 | -54.99376 | 2026-01-01 04:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91380854-3bd0-304d-a3fc-7b2a34602233 | -10.93604 | -49.42842 | 2026-01-01 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73afa153-a240-33bb-b0ca-51c4f7ae60c3 | -10.93959 | -49.42894 | 2026-01-01 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f176ebf-6fa0-3dab-aa31-623fb3f9ecec | -13.62258 | -44.3252 | 2026-01-01 04:48:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a12157e-2f3e-3c2a-afb8-9f35682fb746 | -12.66234 | -46.7647 | 2026-01-01 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7442e5bc-52ae-32c1-9ef7-f6df6529c362 | -14.64151 | -55.8288 | 2026-01-01 04:48:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5828ea74-c8ed-39b6-b086-aae9e60921ed | -14.82329 | -52.86451 | 2026-01-01 04:48:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c5a01cef-fa9f-33f6-88cb-f97a127997aa | -13.76211 | -54.64474 | 2026-01-01 04:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54e103d5-1518-3c70-81bf-64439ccd780a | -9.70818 | -57.93534 | 2026-01-01 04:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e64c4f6-80ed-3c6f-937b-540dd2d12f98 | -15.20384 | -52.90491 | 2026-01-01 04:48:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 837a5d31-0150-3d7e-92e8-df35ba9c8681 | -12.65865 | -46.76006 | 2026-01-01 04:48:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9e81fd9-8956-3f4c-9e23-c3cea2e96f56 | -15.13781 | -45.27895 | 2026-01-01 04:48:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a28c7d8-8508-3252-b1f6-b732893cc568 | -14.19534 | -41.68382 | 2026-01-01 04:48:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29fcede7-3293-3c9f-aa8f-19dfaa890e64 | -14.6429 | -55.82065 | 2026-01-01 04:48:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d06ea5f2-a8e2-3096-9697-c9ceb3c43dde | -11.40162 | -54.99313 | 2026-01-01 04:48:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b85f0a3-8d3b-3af0-8564-1ea02064bc44 | -14.63162 | -55.82286 | 2026-01-01 04:48:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76a04a1b-530d-32cd-8309-2682a5d6ca64 | -11.0112 | -49.03873 | 2026-01-01 04:48:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a8b45e7c-97e0-33fa-8865-b8a7e84b5e00 | -15.12998 | -52.94412 | 2026-01-01 04:48:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| adfe2a87-f0d7-3575-b9a2-a34aa2e4d903 | -16.12703 | -52.33732 | 2026-01-01 04:50:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a03b11dd-4451-3b63-b778-267e9f63747d | -17.70609 | -53.27057 | 2026-01-01 04:50:00 | NOAA-20 | ALTO TAQUARI | MATO GROSSO | Brasil | 5100607 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eea6bfb1-d1ea-3cbb-aba2-e562cfba995b | -17.28164 | -51.94936 | 2026-01-01 04:50:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2c2b82c1-a0a8-3491-8ad5-3303a4d5e48c | -17.28505 | -51.9499 | 2026-01-01 04:50:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5e10db3e-2f42-3406-93b5-bfa5e53145d2 | -18.77354 | -43.72395 | 2026-01-01 04:50:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f8ab7d2-251c-3cc2-816c-43bc6db5edf6 | -15.66637 | -53.67474 | 2026-01-01 04:50:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 620fdcf0-8743-3e47-a2c4-7144e6030dc0 | -19.37048 | -54.59906 | 2026-01-01 04:50:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 047f3aa3-b1c8-3b20-a83c-10cca78fb80b | -19.21368 | -53.43904 | 2026-01-01 04:50:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74d17297-f9d3-3d13-879d-28cfd607e6b0 | -15.84408 | -53.26024 | 2026-01-01 04:50:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac2f4f3e-70cb-35e7-9128-eadfb5f425dd | -19.21311 | -53.44271 | 2026-01-01 04:50:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58c30588-19b7-3448-8db9-eb826d3d2129 | -16.12759 | -52.33366 | 2026-01-01 04:50:00 | NOAA-20 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cdc199b6-fea5-38ed-9350-4a202fec60da | -17.31068 | -44.92855 | 2026-01-01 04:50:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10718cb4-cc73-330b-b7ca-0d0613d6f6b6 | -15.96472 | -54.88905 | 2026-01-01 04:50:00 | NOAA-20 | SÃO PEDRO DA CIPA | MATO GROSSO | Brasil | 5107404 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42b81812-5865-327b-9f23-c5d3defdd510 | -17.7143 | -50.87789 | 2026-01-01 04:50:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a2b9e7e-a5dd-32f3-97d2-86977fe57c95 | -18.49917 | -47.60295 | 2026-01-01 04:50:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4d54e4d-d382-37ab-841e-0ea8bc28b1f4 | -15.91049 | -53.01048 | 2026-01-01 04:50:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 189a050f-ae53-343a-ad7f-f03219659ceb | -15.41597 | -43.32344 | 2026-01-01 05:22:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 417ea527-7c4b-3176-a1b1-80c2dd96dc47 | 0.72304 | -60.04575 | 2026-01-01 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54663a90-74a6-3e26-ba16-0bac0e725f26 | 3.538 | -60.86002 | 2026-01-01 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bca725b7-a8c7-3c01-a939-336c9c706718 | 3.12435 | -60.718 | 2026-01-01 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f199875-61d3-3c1a-ba42-1bd85963f37d | 0.61269 | -60.55462 | 2026-01-01 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6b54cc7c-6afd-3726-a201-3df381e25abc | 3.53855 | -60.86348 | 2026-01-01 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67d6c929-cfc2-3900-8323-34937c27dcd8 | -3.87009 | -54.2332 | 2026-01-01 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| a49123c4-176a-3971-8b64-3e99124266d1 | -3.87057 | -54.22993 | 2026-01-01 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 43329ed9-7665-30ab-ad24-731acfa9cecc | -3.02468 | -50.51202 | 2026-01-01 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 542e81c6-7ca8-3686-b17f-04d92b4f2623 | -14.64303 | -55.82329 | 2026-01-01 05:37:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caca9b14-09ff-309b-8787-11161a71b8c8 | -14.64345 | -55.81955 | 2026-01-01 05:37:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 851fc12e-08b0-35b7-b85e-b8cab4bf6061 | -11.40495 | -54.99477 | 2026-01-01 05:37:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4512687e-6d21-342f-b2ee-d31d4655e0c3 | -14.64262 | -55.82704 | 2026-01-01 05:37:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afb32e77-2700-32de-b8fa-3d8a07a41c03 | -10.03316 | -63.08939 | 2026-01-01 05:37:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
