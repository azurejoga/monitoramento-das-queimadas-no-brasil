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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25219f16-192c-3f4c-9068-4f8bb4f87ee1 | -4.96696 | -43.63627 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4bb1af5e-8340-3d5a-85d9-9a4baab92282 | -5.5869 | -42.91749 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 04877d20-bb84-319a-a84c-94c1076b2d2c | -8.0663 | -48.65561 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f30ed698-6fac-3b54-b5bd-e7e4c2205a59 | -8.48425 | -47.30247 | 2025-09-10 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27b22313-08af-3601-99da-e4dbc3d48571 | -8.52036 | -45.72113 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c53f26c-e8f8-3b6a-b8a4-455c835797f8 | -5.42028 | -42.80682 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73ab2eb4-a423-3012-9c32-d3f9784f6dac | -6.17549 | -41.05074 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9013ec4-2a53-3de5-ad7b-cc9e261e71a4 | -8.06785 | -50.1839 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d0300055-f744-3ede-8234-6b03253bdd10 | -3.98964 | -43.25043 | 2025-09-10 04:14:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f5055f71-05f6-3b27-b957-2e825ff48841 | -6.1743 | -45.80736 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 502aa8a9-c5f8-3833-8afb-1c3db9bcd279 | -8.98339 | -45.72603 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| acf5ac98-1b76-3108-a47b-c479679539b2 | -5.99587 | -43.32473 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4f130df-a3a1-3d92-80e5-997c5f000329 | -4.08464 | -48.04035 | 2025-09-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c99d856b-3b95-38b1-9de3-db9ea19714e2 | -5.41867 | -42.81715 | 2025-09-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 663f24f1-4280-31f9-b2de-3a391be68845 | -5.22489 | -43.70513 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99243ab6-f0fe-396c-97b4-855759f6e4d4 | -6.3099 | -43.81731 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 776915af-0b69-3fce-a546-213c409512ae | -6.36945 | -43.13312 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2c0610fe-5b8f-3113-ba1a-c7b5789017a7 | -6.43068 | -44.04325 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00966464-4dce-3210-bfd6-48d33469f87c | -7.25652 | -44.45947 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c124f578-68f2-3285-b118-a8eeb47ce4f2 | -5.92909 | -46.177 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 84bd44e1-0a30-3f8c-81d7-753f1a09e97e | -9.05177 | -45.75988 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6be172dc-a73e-379f-80e9-6109b9d1ae10 | -7.78074 | -46.06191 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 25bb8976-0c18-3a3c-a2a6-356195e48862 | -6.65326 | -44.54848 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6b1a7a6-e16a-3adb-ae83-6d2f40108c1c | -7.85324 | -46.02171 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82a35cc9-38b4-3ebe-94af-c4d433a6f2e3 | -7.54453 | -48.21385 | 2025-09-10 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83a1ea98-f7e9-3916-8170-0059e8ec8b10 | -9.07581 | -46.97776 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8e50b8a-5e09-30c2-be4d-5241d4282b52 | -8.0482 | -48.68926 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 640e03a9-1350-3b3d-b8d7-e52493b8b13f | -7.57995 | -44.65278 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38d3c649-0a80-349e-ba7f-b732e844a215 | -2.3873 | -47.71779 | 2025-09-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a860f1a-1558-308b-9299-58c1a0c65d80 | -7.61428 | -42.5415 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f7a02cca-4da4-336c-a025-a5865c635040 | -5.67194 | -43.35096 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 690602c7-3b4d-3372-9e10-42c2694cb335 | -8.06507 | -48.66285 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92bca542-da60-333c-b0fa-1f6c22924c25 | -5.64246 | -42.626 | 2025-09-10 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4ea441eb-3823-301d-9357-46dea6112a6a | -8.85096 | -47.2656 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e53b6ed3-f9be-3bba-913b-deddbe04b6c4 | -5.22707 | -43.69122 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 040c0692-7d50-3925-a302-0009febb691c | -4.83808 | -45.3582 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d90e411a-f3fe-3a3e-a1c9-40e9cc30866d | -8.04397 | -48.66557 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8aa32752-1f98-3049-8188-1c26d17f22bb | -7.23818 | -44.46739 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e7d58ca-bdf1-37e9-813d-fb2e67be566a | -8.07234 | -50.1844 | 2025-09-10 04:14:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52b897f0-236f-3c4c-956e-6d16be6e3743 | -6.56485 | -43.14613 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 852613cc-0cbf-3c9d-aa96-970138f49d57 | -8.52212 | -51.38592 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eacf50ea-beef-3715-a2bc-b1c569ff5877 | -8.4307 | -49.12128 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5699a4ef-a391-3f65-ac5b-e06c54b5ec82 | -7.68585 | -44.71015 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff7b3935-6c07-3af8-8107-3aca8e89f699 | -8.71058 | -45.30521 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41d83d37-56dc-3596-a03e-f4183f256089 | -5.4224 | -43.44559 | 2025-09-10 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 502adc2b-2477-38e6-981b-d4042778d36f | -6.41073 | -45.2942 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd68da5c-e50a-3c66-b76c-3bc4556be632 | -6.19719 | -45.02461 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ced3401-ca58-330d-8426-2f0a87ad84f3 | -5.66099 | -45.32451 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85c5e37e-7ca9-3b6a-84d1-65d3fee1a279 | -5.22653 | -43.69468 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6635d873-dd6e-39e3-b95a-842effe62536 | -9.06262 | -45.75779 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4c9cdc0-a63f-3e01-80ed-9b419e4079c8 | -8.21148 | -47.15902 | 2025-09-10 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2866c11-e6f4-3621-9b28-a1279dcdd7b2 | -9.31822 | -46.72204 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b66f72ec-b105-3766-a646-ef10180cea05 | -8.48935 | -44.64649 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 36717f38-6be5-34ad-bc86-e7b389c3160c | -5.75344 | -43.93568 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2f10133-2f1d-3a84-9c98-3785192fb248 | -5.68071 | -43.33819 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc780ce3-9bc4-394d-b6f5-97de53da6296 | -6.68411 | -51.40906 | 2025-09-10 04:14:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b26518df-3d9a-34af-935d-0873a76d147f | -6.52147 | -44.8436 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 905f5f6e-5a43-3492-ada1-6eda4a2e79fa | -7.88173 | -44.81051 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c09d81d4-5984-3a62-a05b-b88b3d5e4ee1 | -9.09717 | -46.98232 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 11836b34-cac6-3b51-ac4c-33129988cab3 | -9.0614 | -45.76523 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37fd4c30-e925-3eaa-abe2-f9c020006ce8 | -8.38489 | -45.02722 | 2025-09-10 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f3effb2-cc25-3bd4-9049-cdb9bed405e3 | -3.04745 | -48.96166 | 2025-09-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4ad264f-248d-3232-b607-6e58654c2d92 | -6.18216 | -41.05097 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9fc7f0c9-179d-385e-a74f-696e70b72766 | -7.74793 | -50.73278 | 2025-09-10 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdfe3a54-09d7-3657-a964-12420394e8c4 | -9.75716 | -45.40001 | 2025-09-10 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| db099c61-fe1d-34f0-9afc-b86e02de49da | -6.30624 | -43.32101 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72d91863-1ffb-3bbf-9639-65e0658d8a2e | -7.07394 | -43.91407 | 2025-09-10 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0980ab99-60b7-3a39-9591-ecf84e089ed0 | -6.3113 | -43.56913 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0af31652-f880-3e90-ad98-d787f13cce9d | -9.08008 | -46.97428 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 369f29d4-4596-3515-9261-a25629f795ac | -6.65197 | -44.08587 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ec79c8a7-84a3-367a-8b22-f44c9e9e3f1b | -5.81139 | -45.67522 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ad75dff-3f8a-3ec8-8ab3-5c0acf6b66c0 | -7.7122 | -45.14915 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bab9659-b848-33f1-bee3-74489ca759f7 | -6.17206 | -41.05022 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc02bc3d-a01d-3af2-811d-2e2f776cf5cc | -5.87565 | -43.98042 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04ff8d8e-e749-34d5-82fd-4721a735a897 | -8.41331 | -49.09938 | 2025-09-10 04:14:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2865e4d6-5487-34b5-b6aa-f695d3c7015b | -5.91099 | -44.97219 | 2025-09-10 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48978320-e4b0-3354-8339-53a5281859fc | -5.12038 | -44.66443 | 2025-09-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a73e9958-8993-3ccd-b88f-30a438144f2c | -5.72796 | -45.40867 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 847a6155-8ff1-3636-845f-d2af8e050cc3 | -7.72189 | -35.13322 | 2025-09-10 04:14:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5afbb81f-5c76-3949-9a99-301977a64f37 | -6.84752 | -47.92392 | 2025-09-10 04:14:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dec4b93f-04bb-3641-8a96-2e8ad84f9b9b | -7.78247 | -46.11819 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a4d295ba-b87f-327c-80c2-08c1e126c067 | -9.35187 | -46.49854 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| beaca759-c83a-31ba-afc1-cd2f39eb4bfc | -5.42614 | -45.8806 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b81e97a3-ca03-34e9-af0f-daec241ab94f | -5.77412 | -43.13424 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 31c28544-1ec1-3b4b-9692-dd5cdd79f10b | -7.78759 | -46.09478 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c4172d1-c273-3a15-9b25-c2d832f6ae56 | -6.44232 | -47.02377 | 2025-09-10 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| be21c9c1-3d71-3a91-8d97-9a1470d2ebeb | -7.54486 | -44.65812 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3fb13cae-ae65-3539-bd44-122b656cf2c5 | -6.20114 | -43.31813 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6522f6f3-68c3-334e-b7ef-6f744595e018 | -7.76075 | -46.07482 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 49ee8563-3f60-359b-bb22-376960fbef6d | -6.67727 | -44.54857 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c88870e5-2518-3a23-a80a-75b9e0a3843e | -5.94059 | -45.68329 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e414fa4-0650-3342-8f74-bcd235ee69e0 | -7.84589 | -45.41444 | 2025-09-10 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8ee65bc-4c85-3569-8354-6f31af919951 | -6.73956 | -45.12548 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc788268-38f0-3c8e-8f9a-300cb9f798b4 | -8.05405 | -48.67913 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6563d96a-289c-3106-a988-f0743a8fca8a | -5.67578 | -43.34802 | 2025-09-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd177dc8-2469-3168-9478-1078a0af5899 | -5.20776 | -43.70602 | 2025-09-10 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57929e60-dc70-3ad0-909f-8d2d7450570d | -6.29282 | -44.22604 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3629a6d3-dc83-3827-9d8a-d45c18b5c31c | -6.25812 | -43.41234 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| a7ef395e-3c3e-3809-86c9-4044c81bb5fa | -7.57807 | -44.70339 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57185587-d9bd-3452-a0a2-d781f4ccead2 | -6.35597 | -43.04625 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README27.md)
