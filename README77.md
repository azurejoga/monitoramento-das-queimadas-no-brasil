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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b53b327-d9d1-379c-9a02-e4ef709e717a | -2.05297 | -48.22156 | 2026-10-05 15:56:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 458f0ec7-f25d-3ae1-8503-c2df93114615 | -3.30806 | -43.94751 | 2026-10-05 15:56:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d3dd6558-c410-3218-b2ca-611b6e487b88 | -6.13006 | -43.16984 | 2026-10-05 15:56:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7d595644-b454-3d9c-98e1-295240c57e15 | -3.49191 | -43.34527 | 2026-10-05 15:56:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 97cd7f13-5258-38ac-b4e7-239830f270a2 | -2.03954 | -48.34664 | 2026-10-05 15:56:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3d985606-5d37-38e3-b7ac-f17f58d0a573 | -4.8438 | -41.81545 | 2026-10-05 15:56:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 89d06e80-7d30-321c-bd21-bed6be982a87 | -5.30313 | -43.21241 | 2026-10-05 15:56:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e8bf36cd-cb9b-35ec-b63e-827c0e68f2c6 | -3.77261 | -39.85278 | 2026-10-05 15:56:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 42.7 |
| 1166772a-f1af-3d32-bdee-bb65cab9f921 | -3.34421 | -44.58888 | 2026-10-05 15:56:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7769ba12-65de-3302-98a8-4d43b6f019e9 | -4.71491 | -40.90967 | 2026-10-05 15:56:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9d577c81-4d50-3522-a7f5-5c84a7ab879b | -1.62574 | -47.67479 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e56e6743-1ed4-3ae4-86b5-ed3df1156438 | -5.11507 | -42.6342 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 43d7631c-31a9-36a1-8fdc-2ea63f47b636 | -4.53073 | -43.53177 | 2026-10-05 15:56:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3fd92e9f-06e6-3a7d-9c7d-cf12a32705b4 | -4.7802 | -39.9735 | 2026-10-05 15:56:00 | NOAA-20 | MONSENHOR TABOSA | CEARÁ | Brasil | 2308609 | 23 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 9b4fe6b9-4d0e-3169-994a-58b8ad3115d3 | -4.34117 | -44.37394 | 2026-10-05 15:56:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 460a4ac9-6d88-3a3f-ac69-6b84cf2aa005 | -3.653 | -39.43729 | 2026-10-05 15:56:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 23d716db-c1eb-3bb4-9692-bf2ec5703ecd | -3.28266 | -42.25746 | 2026-10-05 15:56:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cd33b34c-7d23-3082-b860-6ec9d49157ed | -5.03455 | -37.03492 | 2026-10-05 15:56:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b2fbaa64-8bba-3e64-adfc-84262aa66937 | -4.34649 | -44.37322 | 2026-10-05 15:56:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| afe4e1cb-10dc-3805-92f6-ad608766fbef | -5.84822 | -45.01576 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b2addf2f-4bd6-3b90-abff-154d252515b2 | -1.80623 | -45.27607 | 2026-10-05 15:56:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2b114db7-8844-3806-a158-358068b95971 | -1.40542 | -47.21872 | 2026-10-05 15:56:00 | NOAA-20 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3c1aa4d9-cc00-310d-9c83-641440e726ea | -3.10662 | -41.82992 | 2026-10-05 15:56:00 | NOAA-20 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8b26747a-3fa6-3614-80d2-963f119bb38a | -3.31734 | -43.93999 | 2026-10-05 15:56:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 072a2035-9cfc-3fe3-9a27-791d2b2bb766 | -3.61867 | -40.43979 | 2026-10-05 15:56:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ce02a413-ee01-38a2-b128-d8665d51d885 | -3.79145 | -42.94807 | 2026-10-05 15:56:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a351508d-69d4-3ed8-893e-79264d2c977a | -4.22252 | -41.68695 | 2026-10-05 15:56:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ebfed5ee-dded-30c0-8313-38f1292d9d13 | -4.9725 | -43.07739 | 2026-10-05 15:56:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04ddc69e-6dfe-3282-8ed4-67195389b17c | -3.36258 | -43.38413 | 2026-10-05 15:56:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 483ad4c5-0008-3a58-9643-8ff6b8706370 | -3.85878 | -38.51954 | 2026-10-05 15:56:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 6ec9c8f7-b084-3aab-b89d-f3ca60126ac4 | -3.71291 | -40.3446 | 2026-10-05 15:56:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5e47f0ea-2968-3121-9152-9fd4ab71f03b | -5.34684 | -45.16663 | 2026-10-05 15:56:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a5099d33-3c45-3736-a0a3-47b5640ed3a0 | -3.43477 | -44.44282 | 2026-10-05 15:56:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 05f513bb-3015-343f-b6e9-88ae03230845 | -3.93939 | -40.72499 | 2026-10-05 15:56:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 300b1b23-44d5-3ac1-b400-3ab77010df35 | -4.34861 | -43.83023 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 103b6694-68d4-3c02-af59-79bf1f88180f | -3.58007 | -41.23971 | 2026-10-05 15:56:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 62.5 |
| 7691d240-29a0-3f48-8111-5883b9644691 | -3.85938 | -38.52367 | 2026-10-05 15:56:00 | NOAA-20 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c77350f1-9337-3800-8288-a16d266926e1 | -5.83351 | -45.01275 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b9fb3454-8ff2-31ae-a319-7de44f59f591 | -4.85249 | -42.19693 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 43bf33fb-2a4f-3bac-8b66-dbbcac9c3a79 | -4.80799 | -42.14751 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 217.5 |
| f608de6a-3e08-3c2d-be1f-c6da5459710c | -4.49287 | -39.36369 | 2026-10-05 15:56:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 84ad0a0c-2ae5-315b-a308-69d6d75b5598 | -3.25227 | -41.24327 | 2026-10-05 15:56:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 81f03b4a-f6ff-3d0c-b653-fb3250cd7cde | -3.77443 | -42.60257 | 2026-10-05 15:56:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80cea97a-28d1-383d-90d8-a23175b34a66 | -3.74218 | -39.80746 | 2026-10-05 15:56:00 | NOAA-20 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 49cd385d-0c2b-3a7e-8c53-b2e0054d162e | -4.0014 | -38.35591 | 2026-10-05 15:56:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| a67a12ea-0a6f-3f75-bb33-a96467dfeaca | -4.36265 | -43.92816 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 16a1d2e2-b8ad-37d1-a49a-2a3b087e8a63 | -3.93994 | -40.72867 | 2026-10-05 15:56:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 599fc372-d6e9-323b-a98b-c2297d3a5177 | -3.91285 | -38.66034 | 2026-10-05 15:56:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f90fbf2f-7c76-32c5-8889-d059f994f66f | -2.47539 | -49.40747 | 2026-10-05 15:56:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d3e9f76d-158b-3d65-a30c-0a6a81595bbb | -4.84672 | -40.39648 | 2026-10-05 15:56:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 0be1d64c-206b-3261-8136-79b08c947170 | -6.15065 | -45.46481 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c8f57a2-d1e3-3961-aa44-c6b5a3ab5895 | -3.17123 | -41.39468 | 2026-10-05 15:56:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 5f7fd425-0c93-311f-b514-dec6d254830c | -4.89439 | -43.4626 | 2026-10-05 15:56:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d0f4b88c-96e5-35b1-a944-36bb6fd7dc1e | -4.84372 | -40.40439 | 2026-10-05 15:56:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 17.5 |
| b022d1d1-659e-31c2-9225-acf241edb4fa | -4.35842 | -43.82564 | 2026-10-05 15:56:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5b8b1bf-56ad-3e51-b24f-85f2388c9a3a | -4.2483 | -41.77206 | 2026-10-05 15:56:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fa3b3422-9f8f-30ec-a9bd-7205c445dde4 | -4.4384 | -43.42314 | 2026-10-05 15:56:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6cca927b-760d-370c-a0ef-a54afbfc1553 | -3.3837 | -42.59353 | 2026-10-05 15:56:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a8c31dad-bdc8-3931-9de1-c4cb392a9675 | -4.34164 | -44.37722 | 2026-10-05 15:56:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| c1a733c7-da34-3db1-8ba8-317044c9ced4 | -3.21216 | -42.44422 | 2026-10-05 15:56:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| a7420d64-e467-36c3-850b-28473e1a5a7f | -5.83972 | -45.01577 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 7ed41ca8-cf78-3715-93d8-63bce4daf0e3 | -1.73175 | -45.63874 | 2026-10-05 15:56:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b59907f1-cbd1-3bae-a12b-cd40a35a2420 | -3.28717 | -42.25675 | 2026-10-05 15:56:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 7f66c6cb-1412-3150-a4ae-c93cdcc234ba | -2.05874 | -48.21494 | 2026-10-05 15:56:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 79e7e7d6-b381-3ba5-a0b4-cc7e33a45b0a | -4.94039 | -42.71171 | 2026-10-05 15:56:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 1904a73b-a806-3331-9471-e32e0b95e6c9 | -5.85218 | -45.02203 | 2026-10-05 15:56:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 1324ad18-4cfb-3357-84e9-010f5b6ca529 | -3.30274 | -39.76224 | 2026-10-05 15:56:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b7a3d4b1-6137-3c3e-b322-06b677926aa7 | -5.95539 | -41.33875 | 2026-10-05 15:56:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 3410f368-a1fd-3e1b-bba9-30abfe499096 | -9.1148 | -65.9192 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 12628634-901d-393d-98b4-98cb1230c364 | -9.1408 | -64.3836 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ed505a2f-5163-3398-afa0-3c134c454cf6 | 1.8399 | -55.8218 | 2026-10-05 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ef7d30a8-009a-37bc-8e69-e8a0a7b35413 | -9.0584 | -66.1073 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 911b6ead-0814-3259-8c85-f2a2eae26912 | -9.1349 | -65.564 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 00e696c9-e21e-35a3-ac7c-7bb57bedd5fb | -9.1243 | -68.2206 | 2026-10-05 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 95.2 |
| acbb4f0b-031f-3480-8208-0226e6d059f7 | -9.4565 | -64.3344 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d21adead-0c92-3c81-8600-d9880b1fbb42 | -9.4819 | -66.7836 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| e523b61a-3725-3957-9dae-64b38ef7e8c2 | -8.871 | -66.6521 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 3f8c853e-b812-33a8-994d-fff5140f26cb | -9.1535 | -65.5634 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 00093673-31ec-30d9-aac4-813ecf346cf3 | -9.4751 | -64.3336 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 05ee6dd9-7dda-3ace-b98c-eccff300d401 | -9.3431 | -64.7143 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.4 |
| e0ba7d3f-35b5-3def-b075-8ce36d321a2b | -9.4958 | -63.9562 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 07bd22e0-0b7e-32ef-bdc0-f0285905bc6f | -9.1149 | -65.9006 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0e4983fd-008a-3083-9449-9652020dafd2 | -9.1613 | -68.2383 | 2026-10-05 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| f7d1f82c-1e7b-3a2f-aae2-4e94dc8d8bd9 | -2.5353 | -65.8819 | 2026-10-05 16:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| bd98cb55-12a0-327f-86e3-bc5d92cb8587 | -9.0585 | -66.0887 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 57047811-4d23-336d-9092-f63c28b8b005 | -2.5353 | -65.8635 | 2026-10-05 16:00:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| c132bf26-836e-3d67-8733-b1cec9b46d67 | -9.7126 | -65.0951 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| bb99708d-1ba5-31f4-8c1c-3b822cf38d75 | -9.1335 | -65.8813 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 657a8d4c-dbb5-377f-b8fc-7d7cda2c5e76 | -8.6214 | -69.5026 | 2026-10-05 16:00:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 61.0 |
| df6ad464-c8a4-3a41-a21b-9584a64f3e7d | -9.1076 | -67.703 | 2026-10-05 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 731ab18a-fa27-37e0-82b6-ebf3766f2bc2 | -9.1244 | -68.2021 | 2026-10-05 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 7302637e-fd42-3f30-affd-0d5968c3302c | -7.7127 | -73.1158 | 2026-10-05 16:00:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 74.5 |
| e3fe0ee5-86e2-3b7a-a52a-7628c78590f6 | -8.5929 | -66.8266 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 1aa7e063-02e5-343d-bf9e-408282dc1e7e | -9.2365 | -67.9035 | 2026-10-05 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 50a780ab-6cec-3758-a6ff-ab739cd0cba4 | -9.077 | -66.0881 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| beefb086-40c8-3b25-bdfd-9c6f1adfe0ee | -9.1407 | -64.4024 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 49ced258-c24a-32e7-8aff-22ade475f5f3 | -8.593 | -66.8081 | 2026-10-05 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 0a33debc-a25f-3fcd-adec-7fbac1f36bab | -9.1445 | -67.7577 | 2026-10-05 16:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 166.9 |
| 68b268cb-57e2-3576-8ded-8b6f1492968d | -11.8814 | -64.9323 | 2026-10-05 16:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 3e1f5123-4bf7-3763-a401-b5092dcf5810 | -9.7499 | -65.075 | 2026-10-05 16:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.0 |


[Clique aqui para ver as próximas entradas](README78.md)
