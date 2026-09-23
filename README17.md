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
| 9efd0011-625e-35bb-9bd8-d5348e8cc371 | -1.2206 | -54.548801 | 2026-09-23 00:36:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7707d73-b5f7-3de9-af39-91cceee05489 | -10.6892 | -48.700199 | 2026-09-23 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cc9ca44-5f2b-3c01-ab99-5a3eda3a2beb | -7.8738 | -61.170601 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 520badf4-4d1d-349d-b9d1-6106050c7029 | -5.9299 | -59.911701 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f45091b5-d616-35d3-86cb-bff4204565eb | -12.1032 | -57.181999 | 2026-09-23 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e5a9825-e0c5-3534-94cf-a5db2e6e7285 | -10.3826 | -54.397999 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62fddbe0-bcd8-3ba1-8004-ce0cac4901c4 | -3.6939 | -58.918999 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa643642-e0a9-381e-a4b2-3b91ff6ffcac | -6.1621 | -57.709702 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80f471dd-ef13-38bf-85bc-2661230914df | -6.604 | -59.9422 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 70164804-bbea-3fa5-b476-fbba5e47bb5f | -4.0874 | -62.078999 | 2026-09-23 00:36:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8155032d-775d-3e9d-af18-61f593dcac89 | -6.2872 | -57.7631 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0b9a80a-23dd-3f12-ae99-61482bb1bf6b | -8.8233 | -50.480999 | 2026-09-23 00:36:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51972424-60cb-3b3c-9051-ab15dc564bc2 | -3.764 | -59.462399 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52579d3f-6922-3838-85a6-e7a1ea780ca4 | -8.826 | -50.492401 | 2026-09-23 00:36:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 559a5f5c-102e-3abc-a09e-07d9e8d68339 | -6.0698 | -57.803902 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3685ac25-0cdd-3535-a3a8-69223393ef99 | -4.4386 | -55.057301 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23772d55-200d-3fd6-82a3-e04b8ed009ac | -4.0658 | -56.226601 | 2026-09-23 00:36:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9abf0b6c-6c60-3f50-88f4-d59749fed2c7 | -12.3976 | -46.959801 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 172ad6de-5998-3f88-a543-a2d53b791e99 | -10.5987 | -53.989899 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 475633af-0527-3dea-8d05-10f29784cce5 | -8.9384 | -50.9174 | 2026-09-23 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96bdf081-7ade-3aa3-992d-3e51eb550327 | -10.255 | -50.212799 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 513b9204-0613-31d9-8c62-36c2d80028de | -2.4568 | -57.906898 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6d2a342d-2671-39b3-805d-b4972488f887 | -9.8554 | -48.293598 | 2026-09-23 00:36:00 | METOP-B | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab4cd11b-731b-360e-971f-72ed34e65dd5 | -4.3368 | -55.6502 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea522fb4-60c7-3979-846d-477774813d7e | -10.6183 | -53.985401 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37fce3be-8268-3340-9208-6bab17a2a1cb | -13.9121 | -47.829201 | 2026-09-23 00:36:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c40eecd-0d74-378f-a216-7c18e0f5f4c1 | -9.5153 | -45.337601 | 2026-09-23 00:36:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54faf271-f7d6-3118-a862-44ee3531e764 | -8.2328 | -62.821098 | 2026-09-23 00:36:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e2a9f7de-e905-396e-a202-525e7956ccb1 | -8.4935 | -57.5961 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8ab64ef-d416-3e42-983a-be8aa11501d9 | -3.6327 | -60.534698 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee4c9129-912a-3816-b19d-fbff35ad7abe | -6.0369 | -53.2677 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48253e55-5f08-317a-9cc8-67e712fac16f | -7.0289 | -59.491299 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1679487b-c8d4-3449-bcb7-92977306d98a | -10.4515 | -51.287102 | 2026-09-23 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 722aa18e-cbf6-3767-b47f-85465f82a569 | -3.3335 | -59.838299 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf339fc-5fa0-33d3-989f-475a6afb372d | -4.8667 | -55.849201 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 445572c4-ff87-36bd-b685-a6f18b516646 | -2.6213 | -59.369499 | 2026-09-23 00:36:00 | METOP-B | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20e1c6ae-cf1e-375e-8396-30702a3b92d5 | 2.872 | -60.681099 | 2026-09-23 00:36:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 16fe702c-8b57-3f47-9891-ac254fd68d63 | -11.465 | -47.3512 | 2026-09-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7a01c66d-b923-3e2e-96c2-7034421abe57 | -3.7089 | -60.553501 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e98fe7c2-0a88-303b-b364-869c80df5bf7 | -8.9064 | -61.461201 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa32031e-698c-3b7c-b8ac-71d182fa3a64 | -3.6052 | -60.5495 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b1cf7b92-a6d9-3222-bbdd-b67b7976674d | -8.4536 | -51.480099 | 2026-09-23 00:36:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55172008-c4e0-381e-b6cc-f1239ac5b43b | -3.4616 | -59.5368 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d83f3e6-9722-32cd-aa32-c08be4a261c0 | -5.8727 | -52.122898 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59430e39-8b32-3e36-b4a5-fe0cd794e11a | -9.1295 | -58.907398 | 2026-09-23 00:36:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2345e3a-ed34-32a6-8151-74ad1892c3d1 | -7.6119 | -50.418201 | 2026-09-23 00:36:00 | METOP-B | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 589e5f74-04fd-36c7-af21-cf110dad6151 | -3.2508 | -53.968201 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a411baac-ceb9-3488-bc2a-c14c2f3575fd | -3.1068 | -60.711601 | 2026-09-23 00:36:00 | METOP-B | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cbc5175a-0c65-390a-affc-2ac4101b373e | -6.1636 | -57.716702 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420d4945-576a-3934-a90e-f9c09dc14073 | -5.4256 | -60.233299 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e7be6c42-cb9c-3e81-82b6-19ab080a2085 | -6.6996 | -59.957298 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00cd80be-da7a-3cf9-a22a-e078a2a70e06 | -10.6035 | -53.965801 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e8ec1542-7977-33d6-9fbf-b8e6616d35b8 | -12.808 | -50.858299 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e768c2c2-a62e-329c-8d43-e7c1a701b620 | -9.9294 | -48.466599 | 2026-09-23 00:36:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27c8e444-520b-35ed-9a7c-18a936e3ce12 | 1.5684 | -55.872299 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ddb5cb-38dd-3e98-85c7-f30806a41bb6 | -3.2893 | -57.851799 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf48ab7-eb9b-3e70-8397-76aea088c680 | -7.085 | -61.0718 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00907980-1b54-3a42-8de8-044a560edaf5 | -6.3081 | -59.997398 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7eac5c46-44f9-364d-b319-ba9438115458 | -6.6413 | -59.925201 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48c3055d-1a22-3605-bb47-103aeb6ba0a4 | -2.8612 | -57.7813 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 052ad818-f79a-383b-89ba-d6691b7336c2 | 2.932 | -60.417801 | 2026-09-23 00:36:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| adc36c24-0c4c-3eb1-94da-14c4d9827486 | -3.2842 | -59.433701 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6afbd6a-b440-3b0f-ba8e-dd4735f55cce | -7.2824 | -56.4585 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43de73cc-8e57-365c-bff0-3fd9142acd1b | -5.8493 | -52.023499 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3618b631-07c9-3084-910b-209f8139da95 | -13.4415 | -46.2416 | 2026-09-23 00:36:00 | METOP-B | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fb5c0c8b-facc-39d3-a3fc-f7ee4f53dfc0 | -3.8148 | -58.999199 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14b7942b-ecfb-3566-96ab-2ac582717160 | -3.3957 | -61.039799 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b2344c3-953f-3d64-887f-1febc7aaa209 | -8.4466 | -48.681 | 2026-09-23 00:36:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 62ce2df7-ab8b-36ef-9c67-3060d3e3cc10 | -16.6336 | -42.3116 | 2026-09-23 00:36:00 | METOP-B | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0f7f595d-c329-3a39-aa5c-b6cbffac3319 | -3.1594 | -57.686501 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f86169e8-72d1-3240-a01c-0982eb6ce547 | -3.391 | -57.937401 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 023a0db4-c1d5-31a1-b8d4-64060b47f382 | -6.7787 | -59.614498 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c7fc3732-1d33-347a-bbf0-8eff04bd8436 | -8.454 | -48.711102 | 2026-09-23 00:36:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a499b703-0a6a-3272-bfa4-f10c7038463c | -4.0897 | -62.089401 | 2026-09-23 00:36:00 | METOP-B | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 12711ed8-6ff1-3bb5-a1b5-6ded51ac8576 | -6.1819 | -52.783699 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 53ee29db-56b6-3557-9b2a-e5a6cdf1cebe | -3.7702 | -60.7374 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 325825ec-139b-3593-b400-198a733ed535 | -9.6163 | -55.1096 | 2026-09-23 00:36:00 | METOP-B | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fa0d5619-ff7f-3274-8198-cf60dd18bf9b | -4.0438 | -58.918201 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 565c9327-1d5e-3d0a-8b29-1680ea31ad76 | -6.7155 | -44.1716 | 2026-09-23 00:36:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b88f0f7f-52d3-3667-b861-a2cd815f7f41 | -10.2606 | -49.980999 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d632a23b-e491-3b1c-b9a1-968eef2ffe37 | -9.6953 | -51.972599 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f84da8f4-803f-34e6-a7db-53b1b69eedbe | -3.9532 | -59.341801 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce2f4de1-1672-3aca-8512-e37d5041fb62 | -10.8418 | -56.2108 | 2026-09-23 00:36:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54eeac92-bec6-32ae-8c23-99bdcf0a8aa1 | -12.7758 | -50.8965 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 799c5a98-3688-3f32-84ec-0033825b8f24 | -1.2108 | -54.550999 | 2026-09-23 00:36:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 757c568c-bfa8-3a2d-85ca-c39f29141984 | -4.9838 | -56.958 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 114c6ea6-f1b0-3401-88d7-d742d60d366a | -8.4563 | -48.6786 | 2026-09-23 00:36:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| c953b9af-e5f0-38bb-943c-ffd1be816177 | -6.707 | -44.138599 | 2026-09-23 00:36:00 | METOP-B | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f7cfb90-d641-30ac-8214-8895cf80a1cd | -6.7558 | -63.115101 | 2026-09-23 00:36:00 | METOP-B | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f531c812-0371-3e9a-8db8-84aae38d7a47 | -3.9786 | -59.778702 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46343c1c-876c-3c6b-8952-526c3bfe0d06 | -12.7862 | -50.8536 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d01890ff-4c83-3026-a9c2-09b49ef5ca3e | -10.6069 | -53.9804 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fba2ae33-a24a-3c88-b930-090e1790b3c9 | -6.3008 | -56.036701 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fb52402-4071-336a-8b8a-74c30d746dea | -6.1036 | -57.6786 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0eea8810-d4a6-33c8-951f-788694f59543 | -6.0297 | -55.3424 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1b3addb-2b27-3521-8270-51547c2a39f7 | -3.6772 | -60.595901 | 2026-09-23 00:36:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 21ddef0b-1d91-3972-8b5e-439db50b9c93 | -3.158 | -60.065701 | 2026-09-23 00:36:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b48b371d-df3e-3f0c-a38c-bb094891bbb1 | -9.0923 | -61.422199 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f154b918-8b69-3129-be23-db307c79651a | -6.685 | -55.0513 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdd5efe2-ce9d-3fa6-932e-932640473c54 | -11.3054 | -51.359299 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README18.md)
