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
| 9b146a31-75dd-35fc-bb6e-96d8fe0c2c9d | -6.04871 | -45.83507 | 2025-11-24 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae265bfe-a0a6-3ad7-b81a-a402a988d03a | -5.71552 | -42.74836 | 2025-11-24 04:08:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ef81f530-35a3-380d-a3e4-45b2970e06ab | -7.50698 | -40.86973 | 2025-11-24 04:08:00 | NOAA-21 | SIMÕES | PIAUÍ | Brasil | 2210706 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7e26d6c0-fa5d-3a90-999e-0c15a014100f | -6.315 | -43.81615 | 2025-11-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aefdf545-9dbf-3458-98ed-f033a13b8ced | -6.55207 | -43.21198 | 2025-11-24 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6ce2220d-e02c-3a90-aa11-bdea40912219 | -11.78927 | -49.31654 | 2025-11-24 04:08:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d6599231-3107-3d43-98c5-5947179937bc | -8.12531 | -39.43851 | 2025-11-24 04:08:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ecbcdcf6-5205-3e1f-bcbd-b26d52114a7b | -6.31756 | -43.81268 | 2025-11-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c50f932-efb7-3dd2-9819-76aedad90e8d | -8.72746 | -48.02759 | 2025-11-24 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2e2d78b0-7d7b-3098-8121-4019b68ea43c | -11.79291 | -49.3218 | 2025-11-24 04:08:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 555fd19b-6bea-32fe-ade7-8c932beb050c | -9.57989 | -36.11561 | 2025-11-24 04:08:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 140.1 |
| 65e1b0bf-5e09-3a2a-a48f-2ceaa6d73d65 | -6.08654 | -41.68927 | 2025-11-24 04:08:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0b4761ba-d5e1-3e77-94e8-5ea5ca42ad7c | -7.69355 | -35.11084 | 2025-11-24 04:08:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 6581dfef-ec2d-38f6-91a5-80aeb93129a0 | -11.5206 | -49.68359 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b9a44085-b503-3587-a5e7-b54442f3ba18 | -6.3156 | -43.81234 | 2025-11-24 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 13b96485-dedd-3959-aadc-a41969622f96 | -7.84907 | -41.31666 | 2025-11-24 04:08:00 | NOAA-21 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d86cb8f8-98b4-3f2b-a98c-664baa1f89e8 | -11.52664 | -49.67756 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 01ddcd60-ab37-34c4-b8e5-1a2d37e99d60 | -7.09158 | -39.67093 | 2025-11-24 04:08:00 | NOAA-21 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1f1ef25a-8a2b-3485-a5eb-dfef90ae1293 | -6.11803 | -41.8361 | 2025-11-24 04:08:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 425e3bac-03d7-352f-987a-f7f4affbe09b | -11.52145 | -49.67881 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| df73f158-ea2f-3883-b746-2f9d234a8271 | -6.08323 | -41.68875 | 2025-11-24 04:08:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e04c0e3e-d211-356c-9a8b-3d0cfab93c12 | -11.52576 | -49.68235 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b03b0ad4-e1c1-38c0-a5c7-d67e0d2c761a | -5.73942 | -42.38026 | 2025-11-24 04:08:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 106909a7-a00a-37e9-8503-b4c160f1453a | -7.30273 | -45.43959 | 2025-11-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02354769-fec1-39e7-b3b7-c7a963563dc9 | -7.29975 | -45.43451 | 2025-11-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6e43975-18ef-324b-b9c5-38e00063a8f7 | -6.55547 | -43.21251 | 2025-11-24 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8781a729-1dff-3d18-86be-8916f40f98cc | -12.00059 | -49.27398 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 666d03cf-939d-3e42-a32b-b5f24e5e5aaa | -9.58418 | -36.11633 | 2025-11-24 04:08:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 09855fea-d875-3405-b6a7-10d1c573e8ce | -6.11387 | -42.05596 | 2025-11-24 04:08:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 01bee280-7ccb-3324-a287-15cd02ce4311 | -7.35663 | -35.20515 | 2025-11-24 04:08:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f413b5bd-2832-34ff-b59b-a45689ab692a | -5.57115 | -44.97505 | 2025-11-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 00c9d90e-ce4e-3fbe-ab31-9d2976bbef1c | -5.74337 | -43.78729 | 2025-11-24 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02aee75d-85b0-3b78-b762-8c494f80bd85 | -5.07291 | -49.99847 | 2025-11-24 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ade7d6d-6a00-301c-be1c-94ba02aea059 | -11.5212 | -49.68151 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1c1c02b8-ebf9-34a2-968c-d95e3b652b6a | -9.29645 | -40.36534 | 2025-11-24 04:08:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 18cdaf90-5d55-34c6-8889-29f885c3c772 | -7.35724 | -35.20081 | 2025-11-24 04:08:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 1cb4b33d-304f-3ee9-bd8f-ed0ff87e836a | -6.23546 | -46.40384 | 2025-11-24 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80780af7-7c17-3a94-a824-4a941cdec867 | -11.99618 | -49.27319 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 64d63b1f-4eb9-3709-b2dc-f68c673e4ca6 | -12.00939 | -49.27561 | 2025-11-24 04:08:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 880ecb27-2d95-3e84-bf1e-4673fec21533 | -9.81958 | -47.24682 | 2025-11-24 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf1baeff-3e1e-33ad-9fe1-8c337fa7c37f | -7.29901 | -45.43899 | 2025-11-24 04:08:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be3878c4-3099-35b5-8d5d-49d3f6f2e270 | -8.22454 | -37.39013 | 2025-11-24 04:08:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| be1205b6-5224-3fc2-9ee5-d2fb84fc12ac | -11.78847 | -49.32106 | 2025-11-24 04:08:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e771a99a-ada6-3835-9927-b4e623050b2b | -6.4265 | -40.40234 | 2025-11-24 04:08:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fbbfc935-62c3-3d56-94fe-763108f57d6c | -11.78403 | -49.32029 | 2025-11-24 04:08:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 922ff1a7-d733-32ac-810d-21d1b716c156 | -5.99573 | -45.40052 | 2025-11-24 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24f450cd-61d8-38f8-9e4c-9ce11d33d53a | -6.53098 | -47.01257 | 2025-11-24 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8530766-e585-3d50-ae49-3ee35272de1d | -5.87599 | -45.2798 | 2025-11-24 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 99b43db9-624d-3bf0-80be-576108ad954c | -11.52602 | -49.67963 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e9d8d7ba-d8c6-3318-9e9c-817afc7d2c93 | -7.4717 | -39.96318 | 2025-11-24 04:08:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1bdc1f0d-b0a5-3c82-a0c2-7e01a3efc209 | -9.58475 | -36.11218 | 2025-11-24 04:08:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8572b1e2-42b5-3368-8c25-850cf3745103 | -9.82758 | -47.2482 | 2025-11-24 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b0baf45d-fa83-392b-96bc-796fbe0d43f0 | -9.82358 | -47.2475 | 2025-11-24 04:08:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d6f267d-4e8a-34f5-8edb-46eb173476f9 | -11.52208 | -49.67676 | 2025-11-24 04:08:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a252b6f6-ecc2-338d-923f-d62d04fad6a6 | -5.0113 | -46.85494 | 2025-11-24 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8cc02e2-a2c2-324d-a3e5-9deea275c49d | -5.07361 | -49.99943 | 2025-11-24 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72805ecd-4363-34c4-9281-c4eef88028e7 | -12.00576 | -49.27045 | 2025-11-24 04:08:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aac0f226-b198-3162-89e1-3c53a0f88ed9 | -5.93516 | -45.57748 | 2025-11-24 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 22eda851-5654-33c8-a0f9-92d0855425f4 | -12.00137 | -49.26962 | 2025-11-24 04:08:00 | NOAA-21 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 969d74c0-bca7-3652-89a7-20e19bb6c577 | -6.08269 | -41.69222 | 2025-11-24 04:08:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dc1a749f-743b-3acc-a318-aab241dc0775 | -6.36844 | -39.65363 | 2025-11-24 04:08:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 059cfcf7-c927-3833-b92f-788f03be1ee8 | -16.7628 | -51.35199 | 2025-11-24 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 19104188-e8a8-36e4-b34a-4ba23510a77b | -17.05725 | -52.75076 | 2025-11-24 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6e874c0-c10f-3831-a824-a339eebb5146 | -17.54173 | -54.03681 | 2025-11-24 04:10:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7dbc7497-d1bd-30c7-814d-50c7e0adda2d | -16.76011 | -51.34935 | 2025-11-24 04:10:00 | NOAA-21 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 45be3af1-ba17-3a30-a9bb-5363ed8730a1 | -18.62791 | -50.86864 | 2025-11-24 04:10:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ebd0449c-b337-35a3-bf64-5dfa31258fdc | -17.55334 | -54.03545 | 2025-11-24 04:10:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cc1d266-d6d9-30ca-9867-79d992df2463 | -17.54634 | -54.04172 | 2025-11-24 04:10:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 971ac2fb-28d8-3cba-b847-6ac33dfa4e5f | -17.05221 | -52.7497 | 2025-11-24 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ab6229ca-3804-3a3d-85f0-75e6c820cb5c | -17.05157 | -52.75285 | 2025-11-24 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eda88de-9ce5-33d4-860b-8a1747e9c4aa | -18.48458 | -50.43377 | 2025-11-24 04:10:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e01ac4e9-4ed3-3fb4-8b5b-bf0226b3d799 | -17.05285 | -52.74655 | 2025-11-24 04:10:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d141514-5b80-3631-a016-a223e9c34b2f | -17.55873 | -54.03673 | 2025-11-24 04:10:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 468accbc-fe99-36b2-b842-ef5a29ad6f33 | -17.54714 | -54.03798 | 2025-11-24 04:10:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1730328f-e7a4-3b89-adb4-7a55915eadeb | -19.18528 | -57.33445 | 2025-11-24 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 525fe579-0a25-3106-824d-0b1feda1e36a | -19.22047 | -57.33323 | 2025-11-24 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cfc312a0-271f-3302-9889-f3016f7e7fdd | -19.22176 | -57.32772 | 2025-11-24 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1586193e-bb1d-37e3-a2b5-9af66ee5d319 | -19.18113 | -57.32912 | 2025-11-24 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 16baf2db-41b8-38b7-b456-16a95d6500fe | -22.89764 | -43.65612 | 2025-11-24 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ddeb7c5e-cd38-3770-b886-f374dc80ea95 | -19.18747 | -57.33072 | 2025-11-24 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 42f70292-7dcc-3a62-afb8-c075a962ebfa | -19.18655 | -57.32891 | 2025-11-24 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 02f5f921-ea09-304e-9297-0a96f86bf7ae | -29.90855 | -51.69214 | 2025-11-24 04:14:00 | NOAA-21 | TRIUNFO | RIO GRANDE DO SUL | Brasil | 4322004 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f9ceb75e-35a0-3f1e-9059-666ca68fb891 | -1.48583 | -45.87145 | 2025-11-24 04:33:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 005d2369-d5fb-3265-9a1d-58a06cd73140 | -0.98422 | -48.63815 | 2025-11-24 04:33:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8222ce55-73ac-3375-b8af-c9b122e06658 | 2.22876 | -50.88325 | 2025-11-24 04:33:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c2ac6281-5117-36e3-bd5f-16d39d92e64b | -0.26676 | -48.79624 | 2025-11-24 04:33:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37e70ece-580f-3a41-8dc9-c05f28e9c15f | -0.95162 | -46.87796 | 2025-11-24 04:33:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9721d3f5-16b7-39c0-b5b0-f389093c6826 | -1.48249 | -45.87093 | 2025-11-24 04:33:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c2c8135d-c9c5-3e75-b634-1f0211982e32 | -1.48917 | -45.87197 | 2025-11-24 04:33:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2c3fa2d4-702d-39d7-8c58-324f8f77cfbc | -1.48528 | -45.87495 | 2025-11-24 04:33:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a415faca-e24b-3c4e-9e3c-fb263f359e54 | -0.26267 | -48.79952 | 2025-11-24 04:33:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c8acea9-3ed0-34f6-9ccd-b6b73eabd040 | -1.48194 | -45.87443 | 2025-11-24 04:33:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bbf46f7-fc7e-3fda-b2f6-dc2288369d9e | 2.21959 | -50.87749 | 2025-11-24 04:33:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91cc60a9-2fa1-33a4-aced-b7563f9d0ee8 | -0.95494 | -46.87848 | 2025-11-24 04:33:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 23777048-9e17-3e78-aeaa-cf6e35c1612f | -0.25918 | -48.79898 | 2025-11-24 04:33:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 099dc1fd-58d2-3109-b44f-e0931433df81 | -0.26041 | -48.79133 | 2025-11-24 04:33:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ecef8092-b9b9-3f88-a695-e774d2d781e3 | -1.21978 | -46.40142 | 2025-11-24 04:33:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5643597-a115-3606-a5aa-9d021e6dad4c | 0.16827 | -51.08297 | 2025-11-24 04:33:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17fb4a6d-cb1c-36aa-bfe1-69bfd1e55fc8 | -0.26738 | -48.79242 | 2025-11-24 04:33:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d422cdb9-6b20-35be-a7fa-db9b918caa16 | -0.18822 | -50.10084 | 2025-11-24 04:33:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README7.md)
