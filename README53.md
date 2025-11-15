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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fcdcee3-4448-33b7-a04d-3d0a11ed4795 | -2.69782 | -49.85902 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5833268-884b-3f08-9028-2c715bb92062 | -3.1729 | -48.6115 | 2025-11-15 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e069583c-b302-347d-900a-16ec025a7caa | -3.69873 | -50.95367 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4208b02b-8c25-37b8-87d7-e5a2d6b92d46 | -6.16722 | -48.03903 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7f2335f9-cae5-35b5-abff-ad8bc7c02602 | -8.74619 | -48.31975 | 2025-11-15 05:16:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8fa94c7-128f-3de7-a2e3-65ca86e1761e | -3.61028 | -54.71173 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eb171f2-78be-3438-9547-8bdfd092d4c7 | -3.70531 | -47.63159 | 2025-11-15 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f6c0392-94e8-30a3-aee3-b43c1553db95 | -9.4868 | -47.28352 | 2025-11-15 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96de3cf2-57b5-3c45-b361-635522a7a5fa | -4.86399 | -47.38193 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 970e8d94-911a-35bc-9cc4-f403e710c829 | -2.80545 | -52.96876 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fafb2341-4fd5-331f-a195-2224cfe2e8f4 | -3.46419 | -50.11716 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0476b982-e39c-3cd8-aa41-0fae78aab9b7 | -1.41659 | -55.43583 | 2025-11-15 05:16:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1350bc0c-eb44-3b47-a9aa-765b0a08a11b | -4.35854 | -50.78985 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b741bde-02a2-3464-aa49-be4bfbafd93e | -7.53277 | -47.19731 | 2025-11-15 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 190f0252-1dd5-3434-9ef9-e3ba66d1e0c2 | -3.77815 | -50.14307 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b2f27dd3-9b1b-3856-9c82-c8d0a51438a4 | -3.69551 | -54.62272 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4a17cab-b966-3970-b45c-083fd54aa498 | -3.35891 | -52.14214 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cf7004c-b5ba-3f10-a078-0a9667a8eafc | -4.1072 | -48.01353 | 2025-11-15 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 33af2f86-088a-3ce4-b62c-62ef0fa25af9 | -7.89044 | -48.39877 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c39cfb26-80e4-3dc1-bff9-357296c21fc3 | -2.69283 | -49.85826 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22f79767-3040-3562-acf3-e6a17560bfdb | -4.26952 | -50.5307 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d769a7c3-b658-3bda-9378-5357a31bf685 | -7.52004 | -47.19552 | 2025-11-15 05:16:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 59591a32-bdb8-3c13-bab1-f15ef71bbf08 | -5.38347 | -45.3726 | 2025-11-15 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ae2f1754-48fe-3ca6-8941-63e95118849b | -4.82349 | -47.09348 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7a96e73b-a475-300a-b0d9-ccdc91fe4d1b | -7.26385 | -48.02964 | 2025-11-15 05:16:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90bb8126-0773-3556-9ca3-33526976e78f | -3.14599 | -52.26428 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d160a67a-fb78-3b88-bff6-897d55d85c99 | -5.09469 | -47.7074 | 2025-11-15 05:16:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0bc307d2-f2c5-3ca9-ab9b-6f4210eb2002 | -3.16711 | -45.21601 | 2025-11-15 05:16:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 7f81b65c-1c79-3225-873a-973728ac8910 | -3.41832 | -53.53352 | 2025-11-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c939cf8-f173-30b1-8457-8f37159e647e | -2.79688 | -52.97083 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f748932b-9002-37dd-8e28-b9dd0a66c62e | -7.88449 | -48.39808 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a64d03bb-e0c8-39b3-bc62-4fbc63897a79 | -2.80194 | -52.96466 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6fdcf360-8d25-3cf8-9991-9b80e3d0f7cd | -2.88413 | -51.42706 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11c75803-5585-3368-8bc8-e76c469e7d6c | -1.82708 | -53.76761 | 2025-11-15 05:16:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1bc7528a-e7e3-36ce-87df-20a27b94eb87 | -3.70201 | -51.62885 | 2025-11-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6e39d38-28ee-33e8-a685-8356c4127289 | -4.01859 | -48.80928 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67298fba-7d19-3c5d-945a-10735f45d20b | -7.95575 | -54.84362 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2848bef2-b503-3d8b-bdfc-9212e8f5948c | -4.73333 | -47.15768 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 835e9f53-b178-3ce2-8641-dc17ab71c269 | -4.86561 | -47.3801 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1d0850a4-9336-30a9-9081-23c6bdf58afd | -3.84587 | -50.20848 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30af0942-e16a-3217-b4a3-b95228dc602b | -6.81488 | -48.82598 | 2025-11-15 05:16:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5280052a-bae6-36d5-ad0f-8e3941fbd3fd | -6.81441 | -48.78581 | 2025-11-15 05:16:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4edd63cf-6571-3e46-89e7-7ca2c0a7075b | -7.88392 | -48.40242 | 2025-11-15 05:16:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fbee3f1a-cb74-3a31-94cb-dc3640727f32 | -8.62824 | -54.9431 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cf502938-6943-3aca-afea-7d40f85978c4 | -4.46921 | -50.53565 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a8b1ec0-757b-3766-b82b-5babad7572ee | -7.26985 | -48.03065 | 2025-11-15 05:16:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 84de334b-8312-310f-a277-4220b5bc52ba | -9.49331 | -47.28427 | 2025-11-15 05:16:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7aab7a69-6c26-39e5-9164-b5b850c7d2b8 | -3.86428 | -49.12455 | 2025-11-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 594a7d85-d00a-3727-8bfd-83abbf4e78e6 | -6.15094 | -48.04228 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 68da9f07-c94e-3d19-987c-adfe4551ce20 | -2.92231 | -52.51784 | 2025-11-15 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eab63387-67b2-3fac-bae8-7a34e99c4790 | -3.44273 | -52.94304 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 584ffcaa-232a-35ab-b74f-481b01c62e67 | -6.14887 | -48.04068 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ed71298e-fedc-3239-a994-2f41d47b8776 | -3.41866 | -53.53204 | 2025-11-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b92f5ed-d77c-33c2-9e16-f6ba81d78a12 | -4.38754 | -50.42579 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df8121f0-b3aa-3fa3-93e6-fdb1a6461110 | -4.86499 | -47.38457 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ec3f5414-e9df-3c0b-afe3-ea828dd93453 | -3.76475 | -51.95613 | 2025-11-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91212a52-20aa-3d9e-b418-c0dbed8c650e | -9.12971 | -47.12105 | 2025-11-15 05:16:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b502c82e-3c2c-346f-8ca6-92f346097494 | -2.94216 | -49.35986 | 2025-11-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 09d87cea-eb7a-3b90-b057-53ffba445b18 | -3.26194 | -50.09671 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d0dfbb8-9f57-38bf-bf8d-2d8b58d24b7a | -9.21294 | -48.5924 | 2025-11-15 05:16:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44c11dc4-9cac-33d2-89ae-1c0fa1c4c4f5 | -2.69235 | -59.42527 | 2025-11-15 05:16:00 | NOAA-21 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 052cb56c-c5ff-3e3b-a246-754ef106c5c3 | -7.43439 | -45.2274 | 2025-11-15 05:16:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c86fc8b7-5322-342f-a55d-a9c418a21d22 | -4.4272 | -47.59995 | 2025-11-15 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4038ab6a-0a24-3cc5-a882-fba9d08d89ed | -3.28703 | -53.82261 | 2025-11-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7af2ee2a-6ab5-3b4f-abd4-a16fab1dd420 | -3.47939 | -45.65155 | 2025-11-15 05:16:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd1d45bd-9023-3f4a-8b5d-95f54a79733d | -7.7078 | -49.38332 | 2025-11-15 05:16:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e4629a5-a123-33bd-94ed-f971cd88c5b9 | -2.04301 | -52.63723 | 2025-11-15 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e29cd10-31ca-34cf-ab04-bca87724b57c | -6.97497 | -52.87088 | 2025-11-15 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b5fde86-3132-3b5b-a73d-8c9e7d1821ca | -2.04314 | -52.63806 | 2025-11-15 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5d92bd8e-741c-3d56-9a50-22e36242bfcb | -4.73068 | -48.56459 | 2025-11-15 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb66805b-01a9-31b9-b6c5-6f2f64bb3bf9 | -3.23923 | -50.8035 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1049c491-23e2-3885-ad1d-5cc72acc2053 | -3.41594 | -49.99495 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e36f748-6d05-3faf-85aa-e3bb6c323f6a | -6.59893 | -50.06734 | 2025-11-15 05:16:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48d4d1d1-85d9-3a81-9b43-b26575eaad35 | -2.79792 | -52.96399 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17d8ac1f-7d72-3807-8724-82cd84249705 | -2.88861 | -51.42779 | 2025-11-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fe9d69a-120a-3274-bf84-86546e03d03a | -2.85391 | -51.27699 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1d9fd58-6b8f-3b04-b3b0-09e49c74174c | -3.15183 | -45.38477 | 2025-11-15 05:16:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 767f43e4-552f-314f-8a3c-af7e303a802d | -3.24337 | -50.37499 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a8ab318-9a2d-363f-96aa-0d66f5a27841 | -3.46335 | -50.12281 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 002e7674-2efd-347a-a9e9-e22fa02a088b | -3.71126 | -47.63196 | 2025-11-15 05:16:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 600fab4c-e55d-3fd4-bbcc-f7a004221eeb | -2.8956 | -52.86861 | 2025-11-15 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6af0643c-1751-37a5-beb5-9eca82f17434 | -5.6678 | -49.22642 | 2025-11-15 05:16:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d7704dd-7d4e-341f-9903-9f07a7777ce2 | -3.28391 | -53.81707 | 2025-11-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a461a49-fe81-37c6-b301-e4bba8ac8a45 | -4.19157 | -51.02522 | 2025-11-15 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4192086-8ec9-3ff8-90df-7bde9320473c | -2.11412 | -52.27456 | 2025-11-15 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8116542-1083-3e1d-bf96-30ea8a8f1c43 | -4.38672 | -50.43139 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e7db08d-fe6b-307b-ae02-81d1fb8b5f89 | -3.60083 | -54.67475 | 2025-11-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6d097536-0d29-36c4-8f78-d436298e579d | -4.2712 | -46.83903 | 2025-11-15 05:16:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 958b55f0-9225-34b8-8ca5-f6809e1057df | -4.10661 | -48.01758 | 2025-11-15 05:16:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a71ddb23-1715-37e4-9914-a63210da463e | -3.17429 | -48.60981 | 2025-11-15 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fa7ffd0-b327-3ae6-9858-9d6a1bde2aef | -4.41277 | -50.82138 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddbf45e1-0ec0-3eaa-a1c6-e0f4c584a6b6 | -7.95261 | -54.83818 | 2025-11-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ac248bd-4acd-39ad-aa2b-0ed436110264 | -4.98492 | -47.23928 | 2025-11-15 05:16:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5acb2dfc-9dd1-3d04-8563-ca1edde850e2 | -6.14826 | -48.04529 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| b713b48d-c03f-397c-b244-36cdfebc2b78 | -4.10868 | -50.05701 | 2025-11-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71b9f162-7f73-3981-80dc-b55a4902e144 | -2.68743 | -49.86035 | 2025-11-15 05:16:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2af71b94-929e-3f89-bd7b-9da363bd6c59 | -6.16658 | -48.0438 | 2025-11-15 05:16:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| de4bfca0-1629-3a12-9e7f-9a7b4039c122 | -3.17379 | -48.61335 | 2025-11-15 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd91ead5-923e-3be9-8555-61c319159a33 | -2.79285 | -52.97014 | 2025-11-15 05:16:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 570a9dd3-6ecd-3d59-b6d1-ffa417ec32fb | -3.15642 | -50.26682 | 2025-11-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README54.md)
