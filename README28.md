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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0aebbcde-aadc-37d8-a9b6-cb70e8d2c684 | -14.29172 | -51.95281 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 213fcf1c-0208-329f-8e7d-2c84b87782e9 | -14.3122 | -51.95254 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6a62741-3650-3e32-9815-b77ca801e902 | -13.46087 | -57.06358 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3208da7c-f6e8-3fd9-90c7-b9dd4cd84388 | -15.06409 | -47.03562 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b7cb63d-86f1-3ed9-b5ba-9f0f5c660e01 | -14.3902 | -51.91045 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95cac1bb-880e-3853-84cd-d562b8e58566 | -15.05437 | -47.01969 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 558a2e80-32bf-37a6-a31e-07f2d02070c5 | -15.17201 | -50.07116 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d9f88613-bbec-36ea-8dd7-50cae8e6b8df | -13.53546 | -46.24656 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2dc06fb5-7a53-33b2-93f1-2aec3ab91d91 | -12.68649 | -48.462 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a4c70780-016a-3f32-98d0-55030c41b26b | -15.1608 | -50.07686 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a05d1b9-d673-383f-b2bc-a8a93595714e | -16.13118 | -48.80531 | 2026-08-16 04:42:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6cc50c57-0085-3c46-8818-ae5409281817 | -15.15026 | -48.62219 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 233bc9ec-56b4-3d7d-b4cd-bac80e5f7e98 | -13.43625 | -57.05555 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a275d24-e206-3850-acb7-a740c72e4366 | -13.80645 | -53.77994 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a241c3a9-98d6-3e44-8610-87f914ecf2fb | -14.41362 | -51.84846 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91c62b96-b39a-3cd9-80a6-6ed3ea1358de | -13.69393 | -46.25125 | 2026-08-16 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90522394-6c75-3b2f-8179-155309d604e2 | -14.22861 | -51.81387 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 576a0dff-d625-396c-8645-ad82b100f838 | -13.81104 | -53.78003 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e86e81ce-373c-3a55-9503-e6d580b25bcf | -14.48533 | -45.68688 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 970b36f9-ce38-39e4-85d4-99d8c885414f | -13.70391 | -46.26748 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02bce074-ce1c-325b-8d8d-0fbcc6d43557 | -14.48863 | -54.02515 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97dd32ab-74ef-31a1-bc26-bbe23cb12327 | -12.68944 | -48.44961 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 19b24c44-10dc-39fb-86f6-aeef7dfcf58c | -14.90381 | -46.64569 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9f2d085d-cd05-389b-a2cd-0b05b75f0be8 | -13.42924 | -57.04601 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4440aaf7-33e2-3999-817d-bb5d12e84a9d | -16.12941 | -48.81793 | 2026-08-16 04:42:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20f7f6c0-4b9b-36c5-acf1-fdb3457965a6 | -14.39084 | -51.88493 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0af748e-3a38-3d76-969a-510382972c3d | -14.40135 | -51.88301 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a438871-6dc4-3302-9740-3d2b4ae6b36b | -15.04426 | -47.02613 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d83fe33-c9aa-3efe-a5a4-b72a9ad4904f | -13.44046 | -57.05638 | 2026-08-16 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ff765e5-8a3e-3269-994c-4bb750cc159f | -15.06211 | -47.02094 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 324f60ac-9341-38ff-8210-724924155f44 | -14.41919 | -51.83475 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7462d90-7ad0-38ec-8bf0-2ab1317b844b | -14.47648 | -45.68958 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76766d54-92ce-38b0-9f3d-aab1462d2df3 | -14.04381 | -53.66087 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4a97a07-8bc7-3272-ab4e-dbedaf9812e8 | -12.6696 | -48.45538 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95a6b466-4ed5-368a-b8a1-87bd9fe5c7d0 | -14.44718 | -53.29979 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfcf83dc-da98-322e-b4ea-146b2cdb1757 | -15.07053 | -47.017 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33102b27-a7bc-337f-824f-c7400385baa0 | -13.49764 | -48.22947 | 2026-08-16 04:42:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 91e90fb2-f353-314b-87d4-05e340453b45 | -12.6941 | -48.4421 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f525ae93-b47a-35b8-b27e-98f199799458 | -12.67251 | -48.45984 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3cc04c31-0cca-3464-9200-59c41bc03aeb | -17.99358 | -48.03189 | 2026-08-16 04:42:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e39d6623-d0ce-3830-93a3-d2402d92a9e9 | -15.06534 | -47.02627 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c7fd4430-a452-3d81-9e56-084940605392 | -13.26364 | -51.67947 | 2026-08-16 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5d7929b-806e-3275-af16-4a79029a413b | -13.79334 | -53.79403 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a4c0519-5f95-30c5-9c5c-6565d52faa09 | -17.19849 | -54.21931 | 2026-08-16 04:42:00 | NOAA-21 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d008a47e-25de-3723-974c-d9b44bc102be | -13.80232 | -53.7832 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1ce469b1-0e00-3ab7-bf3a-01701fcf46ac | -16.92638 | -54.1403 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fbb6f8b1-c0d9-3377-a15e-41576faa2284 | -14.3842 | -51.88383 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2caa95bc-8cb7-3dfc-beba-7735ab02df0f | -13.26752 | -51.67648 | 2026-08-16 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bdd5092-bba9-39ec-a780-165c0ca802b5 | -14.38809 | -51.88081 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f17aba4-6754-3324-8d25-74ca2b39606f | -14.30775 | -51.95913 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 357bea2e-6377-3801-a4dc-796e8c0ca92a | -18.3123 | -44.51181 | 2026-08-16 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 615724f1-de46-3e5d-a010-1985b5b1b963 | -12.71454 | -48.47379 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2ebbd636-bba6-3ce3-884b-01736ac7d42a | -15.17255 | -50.0675 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d4a7270e-07a5-3fc6-828d-9f6adef222bc | -13.80995 | -53.78055 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ac8a812-f892-38f1-b123-20aa5119c2e1 | -18.59569 | -47.13294 | 2026-08-16 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ab22f308-3e18-3781-83b9-0f384864aa4a | -14.06358 | -58.74977 | 2026-08-16 04:42:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 878f6591-d50d-30f1-896e-46441f61b21c | -18.9569 | -45.3838 | 2026-08-16 04:42:00 | NOAA-21 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9864c1fc-f98b-35f8-b389-5fa571e227aa | -12.20251 | -52.86762 | 2026-08-16 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 420c85eb-eaf2-3727-93f4-5d6c9808d820 | -13.81373 | -53.76415 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a60aeb4-0221-3968-b97e-7e90031766d0 | -13.79854 | -53.82803 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 351432f6-a9a4-3c0e-ba81-5ec0c2e935fa | -13.25425 | -51.67429 | 2026-08-16 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 13bbf608-0406-3842-9375-31b2ab5b1f26 | -12.68943 | -48.44226 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2bc7880-ec9e-3d3d-8bb6-d9b89d609e9e | -13.70161 | -51.87648 | 2026-08-16 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6125a28f-92c7-35c7-836f-1fc97fae0969 | -14.98094 | -46.58243 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 15f6938d-27c4-39b2-b133-2926febdcc21 | -12.707 | -48.47654 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b272fa56-e480-3d07-a566-6bea158b04da | -15.06666 | -47.01632 | 2026-08-16 04:42:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a022192-b087-3e69-b254-261f006f5d8f | -14.38138 | -51.90166 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f492f83-32d9-32bd-a207-3afc0088c3a6 | -14.92375 | -46.61691 | 2026-08-16 04:42:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0bfdb9d-9a4f-3e6e-a824-df5afcce8aae | -13.24555 | -54.18198 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54c6bc45-54a2-3914-a2c1-19997e89646a | -14.41279 | -51.93984 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa6a2587-e7dc-3d8c-946b-10170a209f1c | -13.2642 | -51.67592 | 2026-08-16 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f0b7130-f5d0-3760-abb0-18ab5370404b | -13.90954 | -53.94935 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b850daf-4865-3805-a216-f9812b69a20e | -12.75229 | -48.43571 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7483c7b-5f43-3134-bbe3-f9137b0a4629 | -14.32649 | -53.307 | 2026-08-16 04:42:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9dab93f4-e74e-3e35-b3a8-900c05666993 | -14.49852 | -52.08604 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86bedbc1-67a5-312a-83e6-660d9756e1ac | -13.77951 | -53.81239 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64752564-8faf-33b9-9861-dcaf2e83adca | -16.89721 | -54.17167 | 2026-08-16 04:42:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c949b74a-ecec-3a59-bd2d-62d39fb30389 | -13.78917 | -53.79749 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a7cc8ca-c9b8-351e-b723-9a2be5709d44 | -12.71975 | -48.46255 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80c431db-3483-3f6c-a66c-9f30fce202ca | -13.75788 | -53.43321 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4e42769-2fbf-33fa-a271-fbdbc3a91525 | -14.42638 | -51.83229 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f159a773-debe-3c24-94c1-528b0abc28cf | -14.80906 | -48.30185 | 2026-08-16 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 860240ac-844c-38d3-818e-4706f27aa18c | -14.48583 | -45.68295 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f306278-a730-355b-be1c-dd40d9e7171a | -13.75506 | -53.42871 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34a1b06a-381f-3025-aaba-e5f22c4ff2a5 | -12.70881 | -48.48865 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c7a67519-db81-356b-ad79-d0fff71d7c06 | -18.42351 | -48.57139 | 2026-08-16 04:42:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1b4a5f40-c5bf-37ee-8854-0daffa5ece2a | -13.27731 | -48.7001 | 2026-08-16 04:42:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a473159f-85ff-3436-9b28-412b728707a5 | -15.10402 | -48.7164 | 2026-08-16 04:42:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1eed2b5-f12f-3794-820c-c23924883d45 | -14.48951 | -45.68747 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0eba6ac0-edac-3d95-81dd-dc7af91a6b5e | -15.10887 | -48.18403 | 2026-08-16 04:42:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d8bbcc1-7d09-326f-a5ba-d3a32e2ddbea | -13.54746 | -46.2478 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e69705b7-d641-3b4b-a51b-99ba56de1720 | -13.79835 | -53.80732 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 590fed28-29b6-3dbb-a5ab-e380a96acc02 | -14.07116 | -53.72181 | 2026-08-16 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b5b6d22-97db-3cf6-af07-22b8bc5193e5 | -14.47971 | -45.68674 | 2026-08-16 04:42:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ed330beb-f37e-3667-9901-c55bf9ba887a | -15.70199 | -47.62781 | 2026-08-16 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 77f1e3bf-7b38-3e4b-91f9-0abf126d039f | -13.65213 | -46.24327 | 2026-08-16 04:42:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e150a787-3690-3d0b-9d93-d0c29f985a7f | -12.68473 | -48.44981 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3fa3eb3-31c5-37ec-b8b5-c56aed101d31 | -12.70238 | -48.48368 | 2026-08-16 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2420397e-99dd-3f8d-8e3f-3d470a008d89 | -14.2884 | -51.95226 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e18611d1-048f-3841-a506-77d5fc003abb | -14.22585 | -51.80976 | 2026-08-16 04:42:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
