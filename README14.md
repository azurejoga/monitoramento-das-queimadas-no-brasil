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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b852fb2-2c4b-3c1b-b336-4a996f927174 | -9.07087 | -47.05936 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 7614c48f-dead-3b65-b9b3-48019e13c107 | -9.71871 | -43.52277 | 2025-09-11 03:55:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 741b7d7e-8a62-30ef-bdb9-57243e2ddbc7 | -6.21447 | -43.49906 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1df7434d-51ba-3af6-96b4-766f1b542d8b | -5.95847 | -45.83419 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8a66c6a-3e3d-32c6-aa04-1f1b819d48d0 | -11.7311 | -50.62885 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 70ddeed7-8120-3f26-9429-fe342c0a18c6 | -12.47977 | -47.49545 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| a0b013bd-39e6-3651-a8ac-5119623882f0 | -7.9003 | -46.25497 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dbea8e59-1555-3883-b7ee-8da64dd82666 | -10.17825 | -44.76371 | 2025-09-11 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91482984-dff2-35f5-bbd0-9a5743158b22 | -8.19971 | -50.10952 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dfc51e09-91ac-3d97-8efa-f80015e751fc | -7.10889 | -50.76306 | 2025-09-11 03:55:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 475ddef9-d76c-3b40-afb3-d29eb690141e | -7.8644 | -45.50953 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a26b227-7811-3df9-9f9f-3a211e2ec3dd | -12.10104 | -51.02049 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 057fa6f5-a1ac-3028-8ac3-c23668b43880 | -8.50789 | -45.68903 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd33081d-d94e-30d2-9ca3-936cc9ca391b | -10.3159 | -48.8013 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 97a6a975-43b9-3dcc-9bf4-b37e1f196923 | -6.64033 | -38.73616 | 2025-09-11 03:55:00 | NOAA-21 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7c1dba1a-6277-3d35-8d1a-e9ba61393c37 | -11.48856 | -43.64011 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15a84006-26a9-3105-ac07-d505e4621196 | -9.07021 | -47.07878 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1fcb5e76-4672-3f9d-bf4b-30c8687455ea | -6.83114 | -45.61451 | 2025-09-11 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ba068bf-d294-38fe-93fc-323a1b6d782b | -6.39938 | -43.51237 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 676606ad-de6d-36a8-a134-fde8264fc9fc | -12.43062 | -47.79306 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38a71219-8b79-3445-8288-c91b98df9462 | -9.46221 | -46.74419 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ea9cd47b-4c3f-36ae-b9b6-771174612185 | -12.03158 | -47.54364 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de4de362-29f8-3466-a6ea-f895018f948f | -11.34737 | -46.49571 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e03115be-d142-3326-80a6-5034e9a27f36 | -8.10446 | -49.25208 | 2025-09-11 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8749e9f2-1332-34d7-8197-98cfd0ee87a0 | -6.54243 | -43.10924 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9d0e87a-4f68-31de-9dd9-c9d682a2fdd8 | -6.25349 | -43.48816 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f034b6dc-01b6-3fe3-be9b-68be6f365df1 | -11.71512 | -46.49829 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c450af04-d7f4-3eb7-a0a8-36bf42df0344 | -11.10412 | -48.41877 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd4fa77f-4751-3888-a917-e6ed1f17d83f | -8.79627 | -48.08979 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0b902bdc-ef9f-3586-8e7f-b2742b14cb9f | -12.11816 | -51.04699 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cff946b7-8116-346c-85c5-5dd743118c28 | -11.3503 | -46.52199 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b4de768d-1910-395a-a45a-e184fd58e64a | -8.1052 | -49.24804 | 2025-09-11 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce4332ac-f2ed-3e22-8a7a-ff3c913f5afe | -11.34089 | -46.49619 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b3de237-fd94-395a-be98-906ad89d7f4e | -11.77873 | -46.518 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0d06ca6e-360f-3ff2-8736-9edd1225f413 | -10.26412 | -48.82484 | 2025-09-11 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4801ef8f-ba46-3230-99dd-4f247870a493 | -12.04929 | -47.60755 | 2025-09-11 03:55:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ee95a8c-e390-3f0b-ae1e-3cedf91c245f | -11.36126 | -46.52158 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8fefefff-919d-3181-8a79-4bc46e9a04be | -8.65965 | -45.73286 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 25952e2c-5b16-3b38-9f83-c06d7c1541ce | -12.16855 | -48.48822 | 2025-09-11 03:55:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1b26cfe-b438-3b6a-9cf2-ee3aeba68b10 | -11.3632 | -46.5364 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 31c3efea-def3-3e6e-8f98-3c48533fdc63 | -11.50345 | -43.66636 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e80b9c6-442d-353b-bd65-2a18abcd1d25 | -6.54716 | -43.10494 | 2025-09-11 03:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5774664-21d4-3730-8619-1670503b5c7d | -8.48413 | -47.28735 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c192cbef-41aa-3b10-86c9-d3a910a93ef7 | -6.45004 | -44.05466 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c665f14e-5cea-3c9b-8b1a-26cf1472afc4 | -7.53446 | -44.67716 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e2608040-b345-33b6-98cd-021002bb6ec3 | -10.39662 | -50.52484 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5006ecd6-5402-3d49-8f77-9eb2904d7126 | -11.12383 | -48.39927 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b194ad20-dddc-3b4f-869c-2eb1f2fb5d3a | -6.62041 | -43.9933 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d73d85a-a116-34be-b8f2-075ee67af609 | -6.18811 | -45.65988 | 2025-09-11 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66dd5153-cbdb-338e-862a-be24c725fe27 | -9.81827 | -46.82051 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d58e1a4-e3a1-38e3-9bc9-efa3b0bb95c8 | -7.47331 | -45.28635 | 2025-09-11 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 449f3bc1-b0f9-3348-bce7-6c3b3912374a | -7.08277 | -44.84954 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87030e85-4742-30e9-8a2b-a2b1e848b571 | -9.0584 | -46.95979 | 2025-09-11 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 9f0626a4-81b9-3baa-b5b7-720d1d9c4142 | -6.10354 | -45.9337 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2ecaff77-3753-3aee-ac8d-5de898e78566 | -11.73025 | -50.63317 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 36461dab-89cf-3e48-acda-8be2c7d894d5 | -8.47913 | -47.28647 | 2025-09-11 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c1ac5ec-e115-34e9-a465-1991ab4e0b20 | -6.15425 | -45.81571 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2f7a649-9777-338c-a6b4-ec4f837ae200 | -8.02689 | -44.49702 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5c44d3d-023c-330e-a808-6eef3a19c021 | -6.67985 | -44.57282 | 2025-09-11 03:55:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4409cb3d-2581-34eb-ab1d-2e703e07c657 | -6.86149 | -41.48244 | 2025-09-11 03:55:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5647f13a-5cb2-3195-968a-aecb75ba67c6 | -5.69838 | -45.31789 | 2025-09-11 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c33fa2cc-4850-3b82-a30d-cfb94b1f5368 | -12.90435 | -43.57716 | 2025-09-11 03:55:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f95cf209-3c97-39e6-8bb4-166451719b80 | -9.84432 | -47.78421 | 2025-09-11 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50636c23-a1df-3348-97e9-fb1fe3b0ade2 | -8.19285 | -50.11295 | 2025-09-11 03:55:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 127a8b31-2e66-38e9-868e-de9db7958901 | -11.07793 | -51.33471 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 765ee8cf-e54f-31d4-bda3-7d6cd59f9a2f | -8.04366 | -49.05739 | 2025-09-11 03:55:00 | NOAA-21 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 15afcf8b-dd84-3f2a-b916-c757636094e8 | -6.39802 | -44.0486 | 2025-09-11 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 80f941b6-4b2d-34b8-a87c-215cc091b6c3 | -8.65685 | -45.72221 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 90d51f8f-0737-3ff0-b730-1caf1ac46bf4 | -8.01536 | -48.64817 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27150c39-2804-3c2a-94b4-7a11e5508a2b | -11.41058 | -43.54758 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fd988f0-4752-396d-b588-3df7d2dcfc27 | -8.20633 | -47.1395 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0112e36d-2dc5-3f80-be5d-84bc1d6e9e10 | -7.8599 | -45.50885 | 2025-09-11 03:55:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 873af0b3-2e50-3dfc-9f3c-d3675cf5f46f | -7.86868 | -47.98382 | 2025-09-11 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a4fd10a-8118-3935-b798-7866d17a9a60 | -8.02063 | -48.64894 | 2025-09-11 03:55:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 161941a4-3269-3379-b080-c6dfc50e65b4 | -12.13726 | -44.86552 | 2025-09-11 03:55:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0c249996-9d7f-3874-a6df-72956e9cf527 | -11.07778 | -51.32861 | 2025-09-11 03:55:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 291d51d9-4a68-33ce-ba1c-4080deccb68f | -7.49979 | -48.26027 | 2025-09-11 03:55:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f36031dd-cbb6-3156-9714-b0592b2d0a61 | -7.99739 | -45.79931 | 2025-09-11 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc8da867-2bd4-34a9-8d91-73793dfb9419 | -11.44853 | -43.5808 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 034b7c20-6316-3b84-90a5-721c81f88899 | -11.79367 | -50.58204 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7eccdce0-408b-39c1-b6aa-1623b28a3f31 | -11.13205 | -48.35607 | 2025-09-11 03:55:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05f4c5c2-f9c6-3b5f-892d-09ca22ef2750 | -11.16416 | -45.27601 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2507cfa7-5b98-3dc8-822a-e80c8c129530 | -11.74599 | -46.53252 | 2025-09-11 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cef7cfe6-e93e-35af-a1ff-9d7b962bfa3c | -11.44105 | -43.57952 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4d3ab945-1260-313a-ab63-f2b2eea34a2a | -11.35859 | -46.53609 | 2025-09-11 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f0d44d4f-e60f-3de7-8c94-78decfb4c2cc | -8.50737 | -45.66552 | 2025-09-11 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88562b85-c0f6-3abb-8a49-73c05ac082f7 | -9.11535 | -46.96895 | 2025-09-11 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d48761c1-a5e0-3023-96f8-68efae493756 | -11.49712 | -50.38005 | 2025-09-11 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c8ca88a-792a-31aa-9f16-107504e971af | -8.8055 | -48.09852 | 2025-09-11 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca52760e-c40b-35aa-8b54-3de0be474399 | -6.15792 | -45.81251 | 2025-09-11 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d75bc8b5-1d69-3fd3-8414-3483c37944f5 | -7.9227 | -44.87809 | 2025-09-11 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e101f821-8da2-3a64-ba1a-358372ea8103 | -11.48149 | -43.68184 | 2025-09-11 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac75283a-57c7-32b5-9a12-b3d44d389062 | -7.6597 | -49.84819 | 2025-09-11 03:55:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ef4ff8a-fae1-3332-9cf8-2f7d95428316 | -12.10469 | -51.02076 | 2025-09-11 03:55:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b56a1040-0579-33ba-9810-87bf289ccc07 | -10.14819 | -46.16673 | 2025-09-11 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e7c8529-68b3-3964-bfa1-892ea78a39bb | -12.42579 | -47.79216 | 2025-09-11 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 38f7c1ae-b39e-39c1-ab3f-7763d1c33c74 | -11.48466 | -49.25671 | 2025-09-11 03:55:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1692ed32-2ecb-35bd-9ce6-d68521230c17 | -10.37787 | -50.52586 | 2025-09-11 03:55:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5855b4d4-a5bc-3b47-85f8-66be8e434942 | -7.37369 | -47.41948 | 2025-09-11 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a5d557e-9ae4-36ba-a6d6-c6cdd9365721 | -7.83501 | -47.25582 | 2025-09-11 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README15.md)
