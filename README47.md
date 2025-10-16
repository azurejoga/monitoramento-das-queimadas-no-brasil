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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94196118-592d-3d51-9be2-bca1da82c99f | -6.22491 | -42.50455 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0f971420-6401-355c-8b9b-4019e2578e5c | -6.45478 | -44.57733 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bd31e74-07a7-380f-9456-1e7819befc01 | -3.27733 | -50.04711 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 652a000b-bbf9-3617-9e65-6972b1e3157f | -7.35585 | -44.06845 | 2025-10-16 04:38:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 377b25eb-2702-3923-8202-1a63d3fadc27 | -6.197 | -44.1088 | 2025-10-16 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a79cccec-0758-33da-a31b-63992e1632c9 | -6.26249 | -44.34108 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e732797-c1aa-376a-aa5f-056b8b2485fe | -7.95223 | -44.13538 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 33bc8368-e6b8-3db6-873a-5d9137cc616c | -2.87588 | -50.74204 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 548a8267-d32a-3677-b575-0b1abdc235c2 | -6.21827 | -44.41791 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c17315a-5aa6-3631-b9b9-303f1f75442e | -5.90185 | -42.82386 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| af778917-6788-31e8-8669-d5d763fac1ef | -5.50785 | -47.29937 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94e0ed73-f4a0-3011-a94c-b93ac3813110 | -4.10135 | -48.02555 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58b41d08-45b4-3ed3-8235-ff40ad88b35d | -8.25006 | -44.14016 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 271a3ec3-1309-34d9-ab94-122b07e68868 | -5.3824 | -48.91278 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8bfd223-762b-3791-9f1c-3c9db289980b | -5.4089 | -40.89777 | 2025-10-16 04:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e334fe2b-dcf7-3ebb-9960-d6eb368db93c | -2.47565 | -47.23117 | 2025-10-16 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bb1798de-9ec0-3426-a613-cc884c2887e5 | -7.18224 | -42.1957 | 2025-10-16 04:38:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 841e93e5-0e91-3e5a-9426-5487631310b6 | -7.48467 | -42.74503 | 2025-10-16 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e6d7ae8f-9b03-39f1-894c-a17fb149c00b | -4.84373 | -42.79468 | 2025-10-16 04:38:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 288bb39f-f468-3c5b-aa8d-adeaf094b404 | -2.72571 | -48.31225 | 2025-10-16 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2179fd93-83c8-3922-b5f2-3ae0e688bd90 | -6.96237 | -41.49814 | 2025-10-16 04:38:00 | NOAA-21 | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 234a427f-e514-3b40-a56f-cc3f4d30cd22 | -7.15224 | -44.38268 | 2025-10-16 04:38:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bf64f51e-e61c-3bf5-a9ea-5a4f3e77f3da | -5.5107 | -47.30359 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0422f855-e80f-3fea-bd78-4f44b131027e | -7.9413 | -44.12196 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 763bbb64-d1eb-314e-856a-f48c1827090d | -7.85554 | -45.40934 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96bc3df5-1a79-3136-acfb-24b4e887c38d | -1.38798 | -48.98748 | 2025-10-16 04:38:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cbf015e-789c-327f-8b89-5a2d81e3da13 | -5.65514 | -45.96026 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60436249-2747-3cbb-8165-66746714d08d | -4.67092 | -44.08772 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db3c4c76-271f-3678-9053-89ba87b69810 | -3.09122 | -42.49633 | 2025-10-16 04:38:00 | NOAA-21 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ed32ed9-507a-38f6-aa1a-06cadf4332a2 | -5.88093 | -43.88247 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 690ee6af-9d27-3b40-ad60-3a52e1447fe0 | -4.67146 | -44.0842 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31cf33ef-34ee-35b1-ad77-337126d1200b | -6.22034 | -42.50399 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3eafd253-7262-3624-8f1e-20e5e5f608f3 | -6.41038 | -42.55389 | 2025-10-16 04:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| bdeb0fcc-25ec-3a0e-8865-2ebbc38d1189 | -5.30644 | -49.57024 | 2025-10-16 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb0948b4-496d-3957-9650-220a360fe955 | -3.81978 | -49.21901 | 2025-10-16 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a041191-483f-3388-87e6-fa7246a44fe8 | -3.01121 | -45.3882 | 2025-10-16 04:38:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bb406ba-e43b-3f99-8848-d06b1a3d20d2 | -6.54214 | -46.2418 | 2025-10-16 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30b381fc-3189-3f55-90d0-ea1ba69ee8d0 | -4.93861 | -48.63526 | 2025-10-16 04:38:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6338b359-86c8-39bd-9f5e-2dcc814f8f44 | -6.37658 | -44.73143 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb8298b0-4bb1-34b8-99ac-c3fe2dc77cbf | -6.45593 | -41.82906 | 2025-10-16 04:38:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ac4b4c5-45dd-37ba-a02f-4ae986c8d0f3 | -8.07297 | -45.43111 | 2025-10-16 04:38:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0c0ba080-483a-3eba-abee-54741a485649 | -5.20995 | -43.80016 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2d3342e-9ed4-3d7d-a58c-898a3794c573 | -5.35047 | -43.75341 | 2025-10-16 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99c52664-a1a3-3268-be6e-fe9d0f4caee9 | -6.52794 | -44.74032 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2ee7844c-d13a-366e-8244-e310a6df7e8f | -5.86082 | -43.87589 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b53fe4bc-3f40-348b-b27d-e561afc2ab89 | -4.87775 | -45.9509 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 640c63f7-6f35-3fd3-8c66-9b599fc0edb9 | -3.1247 | -51.14604 | 2025-10-16 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b405b1f8-3cd8-3127-abbb-5fea45302797 | -5.64599 | -45.97184 | 2025-10-16 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae2766f1-7e8d-3606-9f0e-3f0e495938d3 | -5.87565 | -43.88968 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52c6aa56-eef3-3ffc-9e05-54fedae87a63 | -5.86219 | -42.87969 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df8e98cd-87ef-3e76-8c01-d71ebe24643e | -3.88223 | -52.23943 | 2025-10-16 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90b19e90-6781-3d13-bfd1-b98701ce5cc7 | -5.90248 | -42.8195 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bcae4bf9-93cc-32b7-89ef-610c75315f74 | -5.53878 | -41.32217 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 840c29f5-57cf-36e8-aa64-503293340438 | -8.24091 | -43.42005 | 2025-10-16 04:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c71728ff-1846-3b4d-b2a9-fbb81525dec6 | -6.03674 | -44.31901 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 963727ac-b99d-3cff-8f89-96452452f012 | -7.96644 | -44.12542 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55f28db4-d9bc-38ad-b8c5-6e09fc7d5508 | -3.12871 | -50.21089 | 2025-10-16 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a215b50a-5ead-3e77-8ab8-e21db3aebb1a | -3.84379 | -49.93007 | 2025-10-16 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a4f4a410-6572-3ab6-a2f9-d140cc7cb9a1 | -5.45087 | -41.03247 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df272d37-3458-3928-a773-105b6b6e39de | -4.17556 | -48.14022 | 2025-10-16 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5c66df7-bcbd-3a9f-b8f9-f14325b9ca26 | -4.72625 | -46.16292 | 2025-10-16 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8102f03b-1e1e-3d5e-8266-627a0e9a0121 | -5.8567 | -43.87525 | 2025-10-16 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6074f5ab-2665-36f4-84c6-206c816d5f11 | -2.9017 | -49.77475 | 2025-10-16 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35548fb2-f197-3dc9-a040-98480f716e82 | -6.16424 | -40.91244 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| c989273b-33f8-3116-b238-6f2cd4e6620e | -4.87836 | -45.94687 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b18b906e-9944-3f61-9a15-ef913275f48b | -8.2071 | -43.98179 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e3f31a13-0c0d-3ca4-b8e3-df1f02eb2a5d | -7.11131 | -44.7259 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05cccac5-dd8b-3616-b56d-7d215ca7befc | -5.63507 | -48.09369 | 2025-10-16 04:38:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 056570c3-05bb-3a60-b467-e00791696ed7 | -5.47484 | -42.943 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 23bec104-7d88-38b6-813d-ad27faa67cda | -7.64329 | -44.08857 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 4c96ed9a-783f-3cc3-9ab0-f1aa156efc3a | -5.47294 | -42.92554 | 2025-10-16 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f26b9f1c-1e07-3c67-ae41-c2211035a5c2 | -6.06804 | -44.31253 | 2025-10-16 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fc0d684-be81-3f72-842b-9e0b4274d09c | -3.89561 | -45.08523 | 2025-10-16 04:38:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c7cfed0-8837-39c7-9ed9-3c791046b6b0 | -5.21421 | -46.19532 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2842d24d-c9b7-3f53-8f80-2820026626ba | -7.9475 | -44.13868 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f91d5a8-d711-3e95-b88f-efb6898ad00d | -3.35146 | -49.25407 | 2025-10-16 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e392169-90d5-3615-9db0-36df0469095d | -5.86636 | -42.81867 | 2025-10-16 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c00f663-1f48-3bc0-9808-ce097e1c4391 | -7.67467 | -42.55884 | 2025-10-16 04:38:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d9effcdf-a258-3210-a5fb-25728d894cc3 | -6.15874 | -40.91471 | 2025-10-16 04:38:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 17a40534-3764-3aed-8d32-d429a3e842e5 | -8.2569 | -44.08605 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81b423d5-164e-3669-9bfc-362c86e95f12 | -5.72551 | -44.5192 | 2025-10-16 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 618dd272-8ed3-3850-8159-b1c03561402d | -5.45893 | -41.016 | 2025-10-16 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 4772bf51-b6cf-3f01-83f5-c1bb096dd544 | -6.04346 | -41.93954 | 2025-10-16 04:38:00 | NOAA-21 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b9035a9b-1517-38e1-9dc0-bec3d1c5851a | -7.47998 | -42.13374 | 2025-10-16 04:38:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b87b6f8c-c024-32e8-9839-9953f61c1709 | -6.80128 | -45.47535 | 2025-10-16 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 511899ac-42c4-3000-95ab-0f6c762c0ab5 | -4.39923 | -43.39733 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 231a4859-9c8b-3072-98a7-ce9901252c1d | -5.4307 | -44.22891 | 2025-10-16 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0e7f8c62-e782-37f6-b9eb-fa5ca27ab1e9 | -6.73832 | -42.15242 | 2025-10-16 04:38:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 41b7633e-edd0-3111-8b37-794780288eeb | -4.66777 | -44.10848 | 2025-10-16 04:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d89dbc7-a04a-3e1c-b39b-39dfc9609408 | -7.11179 | -44.72254 | 2025-10-16 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9f226fd-2c7a-3f38-8848-1f2270565565 | -4.91417 | -45.97719 | 2025-10-16 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 655f76ea-3911-3666-a202-70362180168c | -4.357 | -43.3947 | 2025-10-16 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| dcde0a0b-d7f4-3d43-8bdd-d5f4050bc095 | -8.21501 | -43.98706 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe414302-03e6-30ac-937c-1e5b27f235ce | -5.1811 | -43.14036 | 2025-10-16 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2787407-8705-3597-a97f-9032cb641156 | -4.7227 | -46.1624 | 2025-10-16 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 451c3a9c-5d15-367a-b99d-d089b1801946 | -6.14063 | -41.77407 | 2025-10-16 04:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d2301427-4fa7-358f-8a30-d8b397d35530 | -5.68776 | -45.09629 | 2025-10-16 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| a19c21df-0f20-32da-80a8-0ec2d1547dfe | -7.27088 | -47.90985 | 2025-10-16 04:38:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 233d7bc1-6942-36c0-9735-1167bd7c7169 | -7.95477 | -44.14767 | 2025-10-16 04:38:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4fe04007-92c4-30b6-a540-a7cafa131a3d | -8.25498 | -44.06968 | 2025-10-16 04:38:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README48.md)
