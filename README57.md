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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7906b7bb-5aab-3d6c-9ce4-932e6daff8cd | -5.68476 | -41.7417 | 2024-11-01 12:36:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| de5cfdd5-171a-3426-89ae-03bdcfeaf942 | -5.6252 | -43.42447 | 2024-11-01 12:36:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0a48445e-333d-3da0-82f7-e80d3030347f | -5.5802 | -42.87795 | 2024-11-01 12:36:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 90415bd6-94a4-309a-bbae-f9c1e11f0c10 | -5.57541 | -42.88152 | 2024-11-01 12:36:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 39.4 |
| 1751f80a-2534-30bf-976e-a0ce47712530 | -5.57393 | -42.89194 | 2024-11-01 12:36:00 | TERRA_M-T | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| d495ccee-07cf-36b0-be33-f054b30a637c | -5.51261 | -43.05113 | 2024-11-01 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6a4399cf-53de-311e-bae5-68f05f738e11 | -5.49455 | -43.31408 | 2024-11-01 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 185cd84b-1a9f-3e8e-888a-a412e4202c1e | -5.46732 | -43.16864 | 2024-11-01 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 2373544a-9973-37f6-98e3-6f2481022cf6 | -5.46593 | -43.17862 | 2024-11-01 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 814e501c-172c-37a3-8913-875deef71dd3 | -5.45342 | -43.2682 | 2024-11-01 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 4e82488e-8e6d-3d85-a2af-4a598770de8b | -5.34555 | -43.20043 | 2024-11-01 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| c6f8b58b-d7e4-3113-aa3a-1fa0213854bd | -5.32477 | -43.7273 | 2024-11-01 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b8beb642-b7dc-38d8-9520-0e1e215a3b14 | -5.29296 | -43.02949 | 2024-11-01 12:36:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| fc3f596c-e553-34fd-b7a2-9f710fc532b9 | -5.27931 | -43.05854 | 2024-11-01 12:36:00 | TERRA_M-T | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 07cf1af8-5a83-3067-96c2-05e8956ecbfe | -5.02526 | -43.56077 | 2024-11-01 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e9e16faf-917b-3e3d-8d1c-bbd95a26475b | -4.93532 | -43.6777 | 2024-11-01 12:36:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c6383690-0ed2-3a83-9cad-9ef45c3fa26d | -4.80641 | -43.03808 | 2024-11-01 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 77b51533-4869-3010-a930-652a7510ec4a | -4.73823 | -42.97773 | 2024-11-01 12:36:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 9d58ca4c-b52f-30cc-882d-602b0ed15fec | -4.65742 | -43.75409 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| a59bafb0-0378-3c32-a114-1198b370096d | -4.64834 | -43.75282 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2ae822d1-ecef-337c-bfd2-2734eb799e73 | -4.40246 | -43.47025 | 2024-11-01 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ebbeebf7-ed0c-3d26-ba82-e6ee45127fca | -4.40112 | -43.47972 | 2024-11-01 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 9471fd9e-0ab1-31c2-b4ac-df7450e50622 | -4.39463 | -43.45945 | 2024-11-01 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 4e2a21cd-a587-3afe-a8b1-41e34d99ee24 | -4.39329 | -43.46898 | 2024-11-01 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 7dda5787-dcbb-3bc1-ab7a-42610bbd0d3b | -4.39196 | -43.47848 | 2024-11-01 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 177.3 |
| af4add40-a219-3192-9711-3df3d80529ef | -4.38638 | -43.46172 | 2024-11-01 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| ce3b19e7-7395-35ed-815b-32241d4895fa | -4.38501 | -43.47125 | 2024-11-01 12:36:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.1 |
| bec25212-c5fb-31a0-a1d3-72f7e7ce0933 | -4.35584 | -43.54433 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| e685a410-0ef9-3c7e-bd3a-391626b34db2 | -4.3545 | -43.55371 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 515d97bd-8338-328d-bed3-3e603694c36d | -4.34972 | -43.77835 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 2801b455-bf6e-3808-85e4-e0cfd5ffc9af | -4.34048 | -43.78012 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 4eebf414-ce51-3c70-be6e-c39cff6f9fcb | -4.33516 | -43.49329 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| cbb5acc3-430a-3fd4-81c8-6038fdc672c8 | -4.28104 | -43.74363 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 09d80118-412d-3663-aee3-06afd1784476 | -4.27201 | -43.42044 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 3b1b394b-22bc-309a-b015-10c97d363e33 | -4.27065 | -43.42998 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c9127586-62c8-3941-9044-da8e1fba5465 | -4.26012 | -43.43823 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| e5eb6071-3fee-3015-bdd4-ef87c5645fe7 | -4.25877 | -43.44772 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 261fb9e1-78fe-308e-8eee-9e59c20ca15f | -4.16471 | -42.23274 | 2024-11-01 12:36:00 | TERRA_M-T | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| 4935d10d-7cd6-33fd-b77a-fd8c27c37635 | -3.87355 | -43.9521 | 2024-11-01 12:36:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 7f6c927f-b8c0-34f7-bf52-571dac4dfa75 | -3.76759 | -43.53078 | 2024-11-01 12:36:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 51de476c-ed6a-3538-a041-94c402b38a0a | -3.76625 | -43.54016 | 2024-11-01 12:36:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e2cba0bd-1853-3d54-b3b2-393aa8b41923 | -3.65656 | -42.36116 | 2024-11-01 12:36:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 21efe42f-4065-3d55-a32a-a614f19159d4 | -10.98783 | -45.11276 | 2024-11-01 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d6481623-454c-381b-915d-21d3ec75e9dd | -10.98652 | -45.12219 | 2024-11-01 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 583a83fc-1a9a-3760-84bf-1ef48560b802 | -6.71202 | -47.64408 | 2024-11-01 12:36:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4de54451-57b9-3218-91fa-433fe0d8f8dd | -6.70415 | -47.63286 | 2024-11-01 12:36:00 | TERRA_M-T | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| e7828902-885e-3d6f-90d0-075b59f14d1c | -6.70269 | -47.64272 | 2024-11-01 12:36:00 | TERRA_M-T | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a55ee11c-4127-37de-b7bc-f6a3c47f4d2e | -6.26084 | -45.43326 | 2024-11-01 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 706bcc36-9493-35c6-831d-7602ceb70400 | -6.20744 | -44.32598 | 2024-11-01 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 18a8b4d0-c050-37e3-9906-5af1a1c55acf | -6.19566 | -44.53857 | 2024-11-01 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| eef47690-bc9a-36c4-901a-b0a0b025e96d | -6.15868 | -46.82689 | 2024-11-01 12:36:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7d4d5d0d-0695-346d-9af2-3e74e906d004 | -6.05962 | -45.79837 | 2024-11-01 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| f28a296b-7575-3beb-b04a-2c4b571f8026 | -6.05076 | -45.79712 | 2024-11-01 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ac2be81f-120e-306a-a7fb-d18386faab91 | -6.04948 | -45.80598 | 2024-11-01 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 296b1870-7d01-3abb-984c-3826dbfbe933 | -5.97687 | -44.78004 | 2024-11-01 12:36:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3671cff3-c47f-3dbd-8215-b0d9362b7cfd | -5.8402 | -46.23442 | 2024-11-01 12:36:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 16e8aefc-711f-3573-a3d6-edbfa9e4eb96 | -5.785 | -46.54427 | 2024-11-01 12:36:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 198260da-ee11-3557-82d0-23e0ff2c0ccd | -5.78367 | -46.55344 | 2024-11-01 12:36:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 42c6dd5f-9906-30c9-895a-8e83af33001a | -5.59299 | -45.19928 | 2024-11-01 12:36:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 739be9dd-511c-3589-ab2f-4766b4984ca6 | -5.59172 | -45.20811 | 2024-11-01 12:36:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8b252b73-d1ea-337d-a2b6-b04a7125f1c7 | -5.31366 | -45.48066 | 2024-11-01 12:36:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50bbbe6f-dff8-3d3d-a78f-1beb7cf98b23 | -5.2598 | -47.91277 | 2024-11-01 12:36:00 | TERRA_M-T | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b242dc34-4059-30ce-a8af-72f6636bedee | -5.23103 | -46.73581 | 2024-11-01 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 65e314c5-e27b-3cef-bbfe-719d46e05e96 | -5.22964 | -46.74517 | 2024-11-01 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 0dd99693-948c-3f08-b92b-5174c20a39c0 | -5.22056 | -46.74384 | 2024-11-01 12:36:00 | TERRA_M-T | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ea0a9f9c-196d-340f-b179-1731e42c7d8b | -5.11373 | -45.13702 | 2024-11-01 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d1374e0c-c9a4-3e6c-9101-8c618b2035b9 | -5.11246 | -45.14584 | 2024-11-01 12:36:00 | TERRA_M-T | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| eb0163ba-49da-3db5-887d-3310dc9864eb | -5.05626 | -45.53397 | 2024-11-01 12:36:00 | TERRA_M-T | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d1b4639a-d1a5-35dd-973a-570bb8708ad6 | -5.01244 | -45.83537 | 2024-11-01 12:36:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1b90dc09-747e-3496-ad92-1d17ce2cb3e4 | -4.93984 | -45.70084 | 2024-11-01 12:36:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ed051f60-6f28-312c-8c9e-5176d5a98fde | -4.90814 | -48.06527 | 2024-11-01 12:36:00 | TERRA_M-T | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7abea972-13f9-39f3-a481-72a0ed95f44f | -4.82829 | -45.83307 | 2024-11-01 12:36:00 | TERRA_M-T | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 39daab83-e891-32f6-8786-5ba34be75ed0 | -4.82133 | -48.24453 | 2024-11-01 12:36:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 508cca85-0f3a-39eb-86f1-45e8b69fe02c | -4.81607 | -45.66822 | 2024-11-01 12:36:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.6 |
| db2b3e32-33ef-361d-ae4e-091f372261a6 | -4.74855 | -44.08327 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 11dfa0af-9883-3629-8844-c9a614ac1c91 | -4.74483 | -46.65731 | 2024-11-01 12:36:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 350032a9-e41e-3761-a214-89e4ddd7e454 | -4.73956 | -44.082 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| c87b3940-e1ad-33ed-85ca-0431928f67bd | -4.73925 | -45.68708 | 2024-11-01 12:36:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 827796ce-c366-3a03-abae-9e0cdecd1f3b | -4.73825 | -44.09109 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9b54d801-4920-39d3-80e4-d1d9ff3c3f33 | -4.73018 | -45.74931 | 2024-11-01 12:36:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 92244a3b-a540-3918-980a-b0e49643858a | -4.70484 | -46.61355 | 2024-11-01 12:36:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f68a43ac-7404-3aea-b6fb-dbbba6bb0cdb | -4.66114 | -44.18232 | 2024-11-01 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f6ae5b6e-9828-3a29-8ff2-5b7e62b23625 | -4.65616 | -46.31757 | 2024-11-01 12:36:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 15eeb6a1-a3fb-3079-97eb-6b565161059b | -4.64818 | -45.35513 | 2024-11-01 12:36:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 40f59294-9b34-3ecb-8f6e-7662d5336f5f | -4.6469 | -45.36395 | 2024-11-01 12:36:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| dc7da677-f584-357c-b2a3-54fea212a4d9 | -4.59721 | -44.63037 | 2024-11-01 12:36:00 | TERRA_M-T | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c9b9b00d-b466-3f15-b9e0-94af8d0c4c8b | -4.55492 | -44.40895 | 2024-11-01 12:36:00 | TERRA_M-T | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d0442e9a-02b2-3980-b1e6-dd8e2533c658 | -4.55364 | -44.4179 | 2024-11-01 12:36:00 | TERRA_M-T | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 75e99940-48a1-318f-b0ff-0c8429828bd2 | -4.54231 | -45.71037 | 2024-11-01 12:36:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 5857191e-8794-3352-8e0c-aca3abb6e4c0 | -4.54101 | -45.71926 | 2024-11-01 12:36:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| bc036d5d-a1b7-36c1-92ab-06e82f30f4bf | -4.50803 | -45.31145 | 2024-11-01 12:36:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 94424704-e6eb-3a57-bc86-5829f4ad13df | -4.50675 | -45.32027 | 2024-11-01 12:36:00 | TERRA_M-T | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 4e6bd8eb-ae91-3865-b35f-4e5b8bf48b63 | -4.49083 | -45.67888 | 2024-11-01 12:36:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d4cc8d13-de22-398f-9726-e3059df79c32 | -4.4816 | -45.80479 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 8ead9678-0e62-31eb-945e-c6ac1964d715 | -4.46861 | -45.89409 | 2024-11-01 12:36:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6ac79676-a7da-31ec-bf31-829abf071240 | -4.44726 | -46.86664 | 2024-11-01 12:36:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 8a9629b0-0278-3a06-8eb9-d7c0b027c6b5 | -4.44587 | -46.87618 | 2024-11-01 12:36:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ea246160-faec-32e8-9277-aabbfc6d07f8 | -4.43806 | -46.86533 | 2024-11-01 12:36:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6daf3480-3cd9-382f-8a41-e3e460845881 | -4.43666 | -46.87492 | 2024-11-01 12:36:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 46.6 |
| a933561c-b05a-3ac2-baee-1bb6750f6884 | -4.41144 | -45.71568 | 2024-11-01 12:36:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README58.md)
