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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48d0e8dd-abb6-30b5-a319-d97f48b81b83 | -5.96649 | -43.49987 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 73c51384-0a36-3785-8eb5-83cee90bac69 | -6.18774 | -43.26116 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 109e86b7-a43e-39df-a28f-11d54900769c | -4.61257 | -43.14634 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aefc31ff-2f9f-33fe-9256-8dd38eda3434 | -7.65531 | -45.46836 | 2025-10-04 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 496db03b-6b68-3fbb-89b6-f1d689ec4c42 | -7.31085 | -47.30162 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12c7f26f-044c-3c58-873f-670f2ccb003d | -7.72803 | -42.60236 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2c15b90c-afd3-3021-9871-4f561b572c2a | -6.87708 | -47.23073 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2299b635-400d-33fb-9515-95782081c780 | -5.48556 | -44.10964 | 2025-10-04 04:12:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d402b79d-bcca-3983-8055-2a7b44c08325 | -6.998 | -44.50387 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b557ff9-334a-39ce-adff-f9cacec99371 | -7.76932 | -42.51196 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5916b3cd-55f5-37ed-8a03-b372a62cb0a4 | -5.65958 | -42.73521 | 2025-10-04 04:12:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d9bbecce-852c-3388-83a1-cd776f375108 | -5.70949 | -42.63347 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 55b599a1-b295-3c5e-bba6-bcbdc591e54b | -6.28356 | -44.04944 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2feb718-250c-369b-8386-b801f35a3e9d | -6.23228 | -45.35066 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3744c4c1-d26c-3cd1-9922-0b065a67189e | -3.84476 | -41.57449 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ef680040-39e3-37b7-879c-356312872b2e | -5.77155 | -43.61516 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f8d8bf6-8630-3581-b7dc-a83807cafc88 | -5.95498 | -43.48698 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 348101a4-e38f-30cf-ac45-4455a5ec43c2 | -6.69347 | -41.94426 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e4a4452f-a205-3864-9c4e-64371851f75b | -5.73689 | -42.02605 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6d0f3c36-7db7-363d-918f-d26d8643e8b6 | -5.78527 | -45.78298 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60c9c526-ab76-3373-9dd5-fa491a9aec3c | -7.37262 | -39.18912 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 901bd6d4-233a-3c14-9598-b92484f47e63 | -5.74273 | -42.91807 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b7eeca0a-53b3-367a-9622-1fb6e99fc77b | -7.31291 | -42.89008 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8e004072-3e7d-34fc-8058-f5d56278dd3d | -5.3308 | -43.35245 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2318c24-068a-3d5b-a58d-334a1f5390aa | -5.31676 | -43.09773 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72e9d152-c964-3382-a195-cf7c808fd888 | -7.3638 | -39.17124 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6915d7c2-5cea-306e-b520-51521e97a8bb | -6.36877 | -43.89687 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 627f48de-a772-3a98-9921-85aa186bb58b | -7.31237 | -42.89354 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0665145b-be55-364c-9023-19ca8c635d2f | -7.06568 | -43.2303 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fd3033fa-46c6-3f7e-9bb0-77f81b2e48fe | -4.42759 | -40.76733 | 2025-10-04 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c87e8f90-168e-345f-9f06-36a5ace7b106 | -5.34338 | -43.70178 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e44e1366-7415-3a58-8ad8-353bc0eb1ae9 | -7.71115 | -42.58183 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5c622fb5-0720-3fbe-8565-2351a30d2fa8 | -6.78371 | -46.12295 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a997a99-cb14-36d9-afe6-774fa7497227 | -4.43152 | -43.23845 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46fd51a2-cc6a-3ed9-b502-e816085c7d08 | -6.4653 | -44.58587 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| df8a903d-d7db-346a-a53f-10a37e1ea33e | -4.87661 | -44.88597 | 2025-10-04 04:12:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cb97abc-9ec6-3de7-9012-95e111adcacd | -5.33522 | -43.34602 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5af4e381-ce5f-31a9-9cf7-530329b744ee | -5.72638 | -49.29882 | 2025-10-04 04:12:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 017ab821-f4cb-3e98-8d54-3c1d8f33bf7f | -5.9148 | -49.3042 | 2025-10-04 04:12:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c410d834-c7a1-3163-9536-6b57831111f8 | -7.77508 | -42.60617 | 2025-10-04 04:12:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 5f5e8a33-f517-3317-9ad4-9f460fe1fd34 | -5.31162 | -45.30541 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfef3c97-704c-3fd7-b19e-1ecf00224cac | -6.60087 | -44.3121 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1932e3a-c529-3214-a3eb-cbe6c5532516 | -6.06033 | -42.51832 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 62c01666-6c6c-38f0-af88-568f48631590 | -5.92872 | -44.18718 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 266b85fb-a790-3771-82b9-1b33555ceff4 | -5.46969 | -42.77564 | 2025-10-04 04:12:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6304047d-e83d-3dbd-9f68-da8741f37a43 | -5.30225 | -45.56328 | 2025-10-04 04:12:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4c2f3f9d-3376-32a6-8a67-69bf672023b2 | -5.83725 | -42.8797 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3c423462-f8ec-35a1-84ff-490fc9c02978 | -5.46986 | -43.16124 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4b81d67-ec7e-3383-8fdd-db928e47aec7 | -5.98022 | -44.09262 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9da6eefc-dbcb-34a0-9c6f-8fb654b61c99 | -4.44149 | -43.24002 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5eff27a-a4df-3ffa-92f5-c49ad1a17625 | -6.33933 | -43.46251 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89e5817c-2049-3a25-88f3-c7f9473d0146 | -6.67286 | -44.20635 | 2025-10-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd714904-ef0b-32e1-ad90-bf2581ec3ebb | -6.05534 | -42.50691 | 2025-10-04 04:12:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 25155a4f-949e-3ac4-a490-ee10f4edaf4f | -7.77413 | -44.16149 | 2025-10-04 04:12:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fe37d6b-8a15-3b95-8b9a-ab8d5ed40c1a | -6.09625 | -43.43132 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6646cc4f-dc86-3dae-806b-eb59abcc7fde | -5.47317 | -43.16176 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 164893bc-1189-33ec-a30e-bb35c1242f82 | -3.84367 | -41.58146 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3656f15b-f46f-30d6-a659-b28b24c367e3 | -4.27192 | -48.87605 | 2025-10-04 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 651e9c31-ef21-3bbd-9d8e-dcfc3d3f5211 | -5.466 | -43.16418 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c511a0de-6711-3f2f-a364-6c4b9fb8315d | -7.78536 | -42.49649 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e087238b-54c0-37a3-8891-74cff490e3b5 | -5.85409 | -42.20907 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f73a31d0-b921-3980-8614-41dd125f9aee | -6.27987 | -42.43949 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d0890267-bd1f-363f-9ce5-08c3e9f9ad16 | -5.98143 | -43.49153 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 216c93a5-49b0-31da-85a1-987b0ccfbcc1 | -6.99464 | -44.50331 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2b91ed6-b7f5-3cbc-bbb0-98e17eb21322 | -7.05108 | -42.78456 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c9e4e0e7-73ed-359f-b868-a3e636022c5b | -7.0071 | -42.30696 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e4300af8-d3fd-3b57-bae4-70c56c8bf053 | -5.01732 | -43.65745 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e80e1cc5-bc7e-3eb6-8d37-ae11cb54cbc9 | -6.23702 | -45.34353 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcde84ab-5656-39da-a083-ec65cd1d4e9b | -6.06696 | -42.51936 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 334647a3-c92a-33b4-aeb5-d91c816f9b87 | -5.46211 | -43.16708 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f4b4d37f-1e81-30f3-92ec-83f07fa45222 | -6.67228 | -42.81711 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 24b721e3-3fd5-3909-8c1e-cca80f305def | -6.30509 | -44.44532 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37af3931-372a-30b9-9682-6e5ecdb535f1 | -5.08476 | -44.09074 | 2025-10-04 04:12:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 865818a8-c82d-35f8-9615-7463e79641c3 | -4.42688 | -40.76723 | 2025-10-04 04:12:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b32c6c42-5291-38fd-93f7-4389bb3e8909 | -4.0526 | -49.32018 | 2025-10-04 04:12:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97caad36-784b-39a1-bd47-285d73f2aac2 | -7.71057 | -42.5638 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3b4ceaf2-2bec-3d6f-a023-9f5794263f4a | -3.84644 | -41.58546 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29045a8a-1261-3886-9f86-614cff23fe8c | -6.24178 | -44.24708 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4b0ee105-400b-333a-8ebf-8229aa6f82eb | -7.52229 | -37.99977 | 2025-10-04 04:12:00 | NOAA-20 | NOVA OLINDA | PARAÍBA | Brasil | 2510204 | 25 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cc913d8f-1571-3c50-917a-ae97d86f2ade | -6.63062 | -42.41239 | 2025-10-04 04:12:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d1d8acc2-f2c4-3b05-bb45-0ab749cbb97e | -7.24033 | -42.9851 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b0276f78-9cbb-3390-9740-159e3cadffca | -6.36265 | -42.88538 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8e5fadfe-9d1a-3a90-b572-49157346f0ef | -4.43264 | -43.25288 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14c3fb84-5262-3d89-809b-ab7eae71dc52 | -3.39209 | -50.27412 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74fce277-4d41-3eda-8876-0f14379df834 | -4.61146 | -43.15327 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| a1473d72-d1ae-3321-b901-51f8ddf45f08 | -6.43245 | -44.45814 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54af41ea-c373-3a97-8ca5-d62325ce797c | -6.05757 | -42.51434 | 2025-10-04 04:12:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ed109b71-00f6-3c9a-ba76-373d7d8497cf | -5.77032 | -42.93656 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2889bafd-0158-3b5e-b6c9-57139cf397ea | -6.35478 | -43.45074 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5221af96-b42d-3c0f-bd79-17702c1c8d9f | -7.04638 | -43.22369 | 2025-10-04 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 969d1c5e-19dd-3155-97ee-4300c35468aa | -8.65466 | -39.43084 | 2025-10-04 04:12:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4dddf174-e426-3654-b7d6-b14d1fe7a3b1 | -5.72228 | -42.6814 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b95571ce-a897-3d09-ac8f-ff749b89ba3f | -6.37959 | -44.65822 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24a65bd6-6123-32e5-8297-fa15d5100d82 | -5.41212 | -41.34651 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f66d63f4-2691-30ec-8f44-d19f5f58c375 | -7.04532 | -44.33881 | 2025-10-04 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7daadfc7-895b-31a1-bcc9-303ef303513d | -7.71889 | -42.57588 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7e4bc79b-25cf-360e-818b-54db67ab191d | -6.12238 | -43.1161 | 2025-10-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1b3a0c81-3471-328d-b1c6-b34ac7b19eb4 | -5.67612 | -43.03839 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7818eaab-7072-3626-9755-8de9ac5db400 | -6.17877 | -43.9177 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b457ed4d-087b-39ca-b586-5b89b6367e08 | -6.72548 | -45.97154 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README61.md)
