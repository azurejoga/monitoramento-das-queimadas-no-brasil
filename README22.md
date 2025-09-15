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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f41566f4-0b33-3001-8a80-659e9567bebb | -6.69849 | -44.12785 | 2025-09-15 04:19:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa6bb8ee-c8b9-3887-88a7-86d127abe540 | -6.17109 | -41.17642 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b929ed1d-2eb1-340e-87cf-64285a8369f4 | -9.23395 | -45.67108 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5404ccc-6fa9-326d-bda2-8eac0cbb0ff5 | -6.17058 | -41.20147 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f17700a6-238c-3d2e-b2a4-f178c0bc0484 | -9.21148 | -45.74942 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1927b378-7653-3700-bb5f-11b075f8a5e6 | -5.74664 | -43.92574 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b23aa64c-46f3-326b-93e4-4868dad3fe11 | -7.05754 | -44.13726 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cad3ab79-c525-3b22-aed2-26c68d7fe998 | -5.6997 | -49.20223 | 2025-09-15 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 80217118-6fcb-382b-820f-0b752b67843c | -5.18758 | -45.17391 | 2025-09-15 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f946c0bb-ffaf-345d-90c5-dc5550e2bafc | -7.89021 | -43.58147 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 19d53b5c-0d55-3230-99bd-c95b62dd7677 | -7.51381 | -44.7044 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2eb350bb-d99a-3051-972d-6d9d6c95e242 | -5.86339 | -43.72242 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 603468e7-b5c0-3187-94a8-3d2f77d9b13f | -6.09476 | -43.72206 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5b7b2fbb-06ff-3ec3-9212-d24df470b197 | -7.8014 | -46.12097 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d12539c-a31c-3a76-80fc-346ef97af484 | -8.77646 | -46.06841 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2ef8ba2-7a71-33a5-8975-dc2de03e89a3 | -5.08012 | -41.15911 | 2025-09-15 04:19:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7862430d-b592-3282-814b-0aa9df19918a | -8.08648 | -44.49923 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5a6577e-e525-312b-a539-47edd6bb9817 | -6.91844 | -46.1755 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f4b71e52-b9c5-3d25-b388-b847b106b2e3 | -7.05854 | -43.88924 | 2025-09-15 04:19:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f47ca04-76f8-3b0b-be4f-c01ccb85e7eb | -8.97442 | -45.82874 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 82252eaa-cc51-3fbb-ab48-d0cb89e0a28c | -7.48579 | -46.13572 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72de8e6b-659e-36ba-a626-04413723d149 | -3.44416 | -39.03939 | 2025-09-15 04:19:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 61e756f3-3d98-39a4-a2bb-b617e17733dc | -6.16901 | -44.53457 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76ffaea6-2bff-3d3b-8474-0a5f9ca1cc58 | -6.80478 | -34.94619 | 2025-09-15 04:19:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 36ae20d9-34a8-350d-8637-4e5f84ec74f2 | -5.99233 | -43.72428 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fc6506d-186a-3f32-abd2-bc0104765040 | -7.49883 | -44.67012 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 266e808a-b2d6-3b31-b91a-127cbdc7b446 | -7.88291 | -43.58406 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 06a18c0c-2a26-397a-8ab7-401d955463fa | -8.64533 | -46.35781 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3157a14-8c2b-3cad-96c7-fd1230fe29f2 | -7.51562 | -44.36316 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7efc517-625e-3ca8-bf73-191937f9fec6 | -7.35674 | -44.29145 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d77e51d7-e7e0-34b1-a1af-be1de43261e3 | -6.66024 | -44.63668 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 43b8fb72-a51f-31af-8a9d-c258df0b538f | -9.21424 | -45.75342 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97648bb0-324f-3d28-affd-456ca23bb765 | -8.91289 | -45.50578 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e93f3c1-59c5-32ae-b15e-6b5749746f15 | -7.68829 | -48.86576 | 2025-09-15 04:19:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a13e930c-de0b-34e0-a986-9abbdd5ab6a3 | -6.14809 | -43.35604 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c86df030-a668-3c64-80bc-5c98442d085f | -7.86995 | -43.57833 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 9ac16861-ebf6-3544-955a-6f2d8ef0e19a | -8.12946 | -43.66543 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7325d7e0-f465-322a-8bf5-09b782179f2a | -5.53902 | -46.41629 | 2025-09-15 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 029e8e5e-3e34-38e2-9218-1368eb0c7ae3 | -7.98647 | -45.66294 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5088cc95-ec34-3424-af7c-d32bc9f0b233 | -6.99268 | -45.61804 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 050091a9-94c9-33b6-9053-1a19c5807082 | -7.87552 | -43.56433 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa3601ee-a7a6-36a3-bdcb-122431fd18e7 | -8.61833 | -45.73235 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 974f546d-7894-38f3-930a-a1ef336a0ac2 | -9.07839 | -44.81297 | 2025-09-15 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71526728-9c11-39c2-92f5-4c0c6f2da3b9 | -7.29899 | -46.57822 | 2025-09-15 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5935b52-a19e-3daf-b3e2-db2ce88411ba | -8.92104 | -45.47515 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 01d6d4f5-9de9-3e53-ab2a-9f2828725238 | -5.14795 | -46.00513 | 2025-09-15 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9f62f580-1c92-3af5-acde-4ae63173a3f5 | -8.90085 | -46.18596 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1597d7d6-5478-3f88-98d0-ce761da7ac5a | -8.91694 | -46.12747 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59ea9be5-ff52-3494-ac0b-5f3c20ad0dc5 | -7.988 | -44.84667 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fee7ae25-dc1f-301b-b6b4-f27a9e7bcd41 | -7.51177 | -44.36613 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 974ec6ed-a79d-36a1-8b2e-7f4543c67c55 | -8.99422 | -45.78908 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c8507cc-f7d1-3bc4-9c30-07f678dcc984 | -5.91319 | -45.72927 | 2025-09-15 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c4c9f60-8f99-3be7-a35a-917c26280a63 | -8.95955 | -45.79424 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c7f7df7-8a44-3b1a-9745-08cf44e5fa4d | -8.96292 | -44.4382 | 2025-09-15 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06dc5ff5-1f0c-301a-b286-07b5eb36843d | -6.08475 | -43.15106 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4f05db5f-ffaf-328f-95fa-013361affde7 | -7.87333 | -43.57885 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e3bfd794-c30b-3bc1-962a-9a2d4ab2d786 | -7.63931 | -49.72675 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e960ccf1-2be3-35ee-bf61-d38c92708108 | -6.17617 | -41.189 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 80a6c425-55c0-3b1b-b2f2-06946727941f | -5.65055 | -42.60062 | 2025-09-15 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| db02a885-b79c-35ff-9a72-8f1ce00981df | -5.76396 | -43.92531 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c7dd7e9-169f-3dea-935f-195df631c30f | -7.15381 | -44.32784 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a5907a0-873a-34d6-a47d-9845aa1744af | -7.46237 | -44.44405 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faaa22e5-9c61-3b55-ae83-7ba4f63a52f8 | -6.20559 | -55.63456 | 2025-09-15 04:19:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c88d4d96-73b4-3074-9302-edc6e04322e9 | -6.05482 | -43.56055 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00b27f4f-7bab-37c6-a647-8a154f863557 | -3.41972 | -50.11274 | 2025-09-15 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dff17051-711a-3b37-892f-2b98b35a5da2 | -7.37131 | -44.35091 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02ae6f07-c19e-388a-aeef-05077def61a8 | -6.40732 | -46.94104 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0ff6bbd-7f96-380a-a885-11e9ee1fd987 | -5.77498 | -43.91989 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 140316ea-d170-39ff-b98c-b9319332bcee | -2.29493 | -48.57495 | 2025-09-15 04:19:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48c90899-580a-3ed7-bdf8-20ffe115b98d | -5.76449 | -43.92183 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a239f32-c64f-3589-b9a1-f0df296196f5 | -8.08209 | -44.50571 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ce38783-56af-36a0-b694-24b091f5cb1b | -5.57773 | -51.97157 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ce886e4b-91a7-306b-9c8e-736ba8dc18ec | -8.40529 | -45.81213 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6234ace-ec24-32fa-9855-2a0a4691d59c | -8.99531 | -45.76069 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 096781f8-5164-3a55-b761-49fd2718d354 | -2.79519 | -48.64308 | 2025-09-15 04:19:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3347faf9-a886-3de3-9be9-506f338ca0b6 | -7.86789 | -43.58149 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68b0d7f3-3eb1-3160-99e1-36a326f68abb | -3.59681 | -47.51424 | 2025-09-15 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5d85038-71b9-3b77-b893-0d82ea76b7e6 | -6.10197 | -43.71955 | 2025-09-15 04:19:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe216198-b9c5-35c1-88aa-baaa03dbf340 | -5.14558 | -44.70433 | 2025-09-15 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59dcd9e9-a01b-382a-860b-90f3511bc9eb | -6.42391 | -44.3833 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc7a0fd9-7516-34c8-a924-6c0d4ccdb122 | -8.27534 | -45.62039 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5836fe27-6a9f-3afe-a60a-09e65ece1997 | -8.77039 | -46.06384 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3bd04780-324b-349c-8d2b-7d46815ccc48 | -5.73955 | -43.20569 | 2025-09-15 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 553e17ed-2eb7-336d-9f18-21f6007afc6b | -8.62655 | -45.70158 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d677c4d6-ac31-3f1a-a922-65a7f4cb3cc7 | -7.67717 | -44.48457 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 45b9119c-05b3-36d6-8905-3099706c5789 | -8.19949 | -43.76157 | 2025-09-15 04:19:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bb9274d-5500-314e-8d3d-408522d89328 | -5.97132 | -43.21509 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 02cd274c-6a03-3faa-9feb-28b09e82eba9 | -6.81295 | -46.93149 | 2025-09-15 04:19:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00850643-f8f7-3151-b993-c1eeaa95c40c | -6.25853 | -43.47187 | 2025-09-15 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40c03048-ae83-39b5-883b-48227c2dcd07 | -6.66636 | -45.55133 | 2025-09-15 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 644c1b36-fc60-387d-bf28-67d2ac2ea0bb | -7.02147 | -44.89582 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8f5fe85e-24a9-318e-b158-8b9a3f06e5f2 | -7.63687 | -49.73954 | 2025-09-15 04:19:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4a7e4027-87c6-311f-b3ab-db6a151fd18f | -8.2088 | -45.54515 | 2025-09-15 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8ee6c5d1-5e48-3a5a-970c-dc7bea044bea | -6.8916 | -45.63349 | 2025-09-15 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bec3bf39-5038-3ab2-9447-4623b2027ae4 | -6.16627 | -41.20524 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 657c72aa-c83f-33db-8642-790dd2a72d16 | -7.45112 | -44.38527 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8b48216-9c0d-3334-902c-5dc6c95533f9 | -6.1669 | -41.20091 | 2025-09-15 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ada583d2-34a8-3149-a759-f5a7720fbb40 | -8.64809 | -46.36185 | 2025-09-15 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00f9c468-9c52-3ab6-9784-5f21610fa01f | -4.18752 | -50.42735 | 2025-09-15 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 423cb4cd-d181-369a-be86-9ad17b0f8eeb | -7.49338 | -44.68349 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README23.md)
