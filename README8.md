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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ee1c028-33a8-3ec3-b0dd-3dd1bcb6df00 | -5.97029 | -44.52111 | 2025-06-25 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f954d5-5f40-314d-99e0-8fbec9414605 | -7.33273 | -43.18957 | 2025-06-25 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 35aeed24-58e7-3210-bfd1-5b3cb631cb1c | -7.02778 | -44.56919 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 42a3a2f6-c88f-3515-816e-5d1c5ec4487b | -4.22583 | -43.63962 | 2025-06-25 04:06:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4d9f8927-393f-3b25-95be-78eaebdb3363 | -7.09289 | -49.17727 | 2025-06-25 04:06:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d0b4ada-4e0c-3d92-aaaf-ae926a86af5c | -3.70488 | -42.19431 | 2025-06-25 04:06:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 613dc804-13c3-3e4d-8904-f4d84bf19c11 | -5.82841 | -46.36178 | 2025-06-25 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efd9423e-35de-33e8-8091-a2d0f9665803 | -7.01488 | -44.55896 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b875211c-1b08-31fb-bee7-59cb249f1ec1 | -8.24365 | -44.95343 | 2025-06-25 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5468903b-d8a4-3ead-9626-17cc87ee503f | -5.35613 | -45.11709 | 2025-06-25 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34e9e8d8-68d5-331a-a0aa-2c0259eb1786 | -8.06224 | -43.10798 | 2025-06-25 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e15934bf-8f4c-3664-b235-4f987aec2709 | -6.22615 | -43.35789 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4bcd7e0-7487-3ca9-ace5-284614e9b270 | -8.42804 | -48.30438 | 2025-06-25 04:06:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cac6f189-d3ba-3b04-9f78-435bffd8af9f | -8.42368 | -48.30362 | 2025-06-25 04:06:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b61bf532-cfc6-3245-8759-aa99f7b9d279 | -6.22175 | -43.36106 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82298de4-cc43-3c70-8ead-113a71aa5170 | -6.95645 | -42.7997 | 2025-06-25 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 23cba58d-2575-370e-9de5-d8d8ffef3e4b | -5.97516 | -43.75842 | 2025-06-25 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b490cf04-290a-31c1-8f8b-515fbb8487c4 | -7.5602 | -44.9508 | 2025-06-25 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5153f4e2-4b33-3f72-bd05-6e86c51a344d | -7.3091 | -45.76975 | 2025-06-25 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6759f7f5-9216-388f-acab-81d571814872 | -6.29533 | -44.23936 | 2025-06-25 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5c9673e-27b8-32dd-aa6b-a0b2e032a261 | -9.54924 | -40.34946 | 2025-06-25 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 35.5 |
| be4ea475-494c-327a-981f-8da2ecb473ee | -8.34017 | -48.52464 | 2025-06-25 04:06:00 | NOAA-20 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a38da7f6-0b59-317c-8803-8d80a4ff0c95 | -6.22435 | -43.36896 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7a50d3a-f401-3bcb-8adf-94249805faa7 | -9.54583 | -40.34894 | 2025-06-25 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3bac8f80-16d8-3711-a492-4f31a9a3ba52 | -4.73916 | -43.26703 | 2025-06-25 04:06:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 956c016b-95f7-3c17-a162-c57584343264 | -4.95199 | -37.43888 | 2025-06-25 04:06:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aecd7fc5-cb13-35eb-ab53-4006db9f0c1c | -6.00514 | -44.33017 | 2025-06-25 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c3804ed-5ddc-32e3-a5e4-515b95b4e490 | -4.37223 | -48.06992 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6c3ba323-5b22-3f0e-bf6c-a862167ee3c8 | -3.61525 | -47.53081 | 2025-06-25 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c0a2ba88-8cf1-3413-b3d8-69c8feeda030 | -4.53322 | -48.00578 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5acd4d63-5abd-3bb2-85ba-8675345bb798 | -5.75638 | -43.39866 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0387fa60-ae4f-368c-b8fb-640f9aa114a7 | -8.40207 | -47.12629 | 2025-06-25 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 984b0fe6-d5b0-3ab8-af52-64d67532f9b4 | -7.09901 | -49.17474 | 2025-06-25 04:06:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cedaa832-b818-35d7-96ed-d27d3e2cd4eb | -7.35676 | -43.4807 | 2025-06-25 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2c1abcd-87d4-3f48-8bfe-5a09771eb837 | -7.66944 | -45.93551 | 2025-06-25 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b40c035-2f74-3ed4-a5c8-1ddfc4ecaf5c | -6.172 | -39.94582 | 2025-06-25 04:06:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| eb4b713f-daaf-340a-8681-d38aa0d550cb | -4.22933 | -43.64019 | 2025-06-25 04:06:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94e82966-300f-362b-82c6-c4b9f708ece5 | -8.24479 | -44.95495 | 2025-06-25 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b536220-553c-3923-befc-28b248f45c04 | -7.20116 | -43.09544 | 2025-06-25 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 97281953-b6c2-39cb-a837-5a16022ed8bc | -7.03132 | -44.56987 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54861f89-5126-3799-912c-82f90a2b744e | -4.37685 | -48.06861 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06e00382-9be3-3b76-a65c-b035f5cce330 | -6.36693 | -43.65911 | 2025-06-25 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 668e4769-8fdd-370a-9dd5-89c9ba668376 | -5.76443 | -43.39229 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f02a649b-e8a3-312e-9757-e533bdeb5f2e | -9.55266 | -40.34999 | 2025-06-25 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 35.5 |
| 8ec56440-87a1-3b45-ad4e-38f9a80de650 | -6.22495 | -43.36526 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9a09b2a-c488-3f43-9919-40b996efac0d | -5.47753 | -43.03759 | 2025-06-25 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41ba1d99-4592-3acf-af0f-9d0b4b655b70 | -7.86313 | -50.66649 | 2025-06-25 04:06:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d65c9cd1-c026-3e90-b4fb-477c9186e539 | -5.9183 | -43.48146 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a89d817e-a0fe-3a89-b529-0952921d8f1f | -6.92465 | -46.41039 | 2025-06-25 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e67d8348-1bd6-3aa3-9ff1-513208a6d918 | -7.8822 | -47.88566 | 2025-06-25 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cfdb9a8-5df9-3f1b-9fdd-64e5d0866c8d | -2.44898 | -47.4985 | 2025-06-25 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02c5e085-7f87-36c1-9639-111723877ae3 | -6.22896 | -43.36213 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5a4d8d00-9fbd-3e17-8c18-70a9d9bb9fe8 | -6.1829 | -48.07285 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 700df874-a8ae-35d6-be11-ad47bf9b544e | -6.09216 | -43.51186 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5eb58ca-682e-33bf-820e-b21309514322 | -6.18213 | -48.07745 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b19fef85-0496-396e-93d5-13e711b7569c | -6.17845 | -48.07206 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 47ab73ea-b3f0-351a-ad63-6cd5f0ab82fe | -8.06281 | -43.10442 | 2025-06-25 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5f6ceb3c-86f9-3545-a24a-eb7b6b9da07f | -7.00891 | -44.55581 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc27c19f-8cf6-3490-88d9-01ee58b7dbc9 | -5.97052 | -43.80888 | 2025-06-25 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51821dfb-bb61-325e-ad60-a75bff5fe843 | -3.6145 | -47.53528 | 2025-06-25 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1d6c9089-e757-34d6-8be7-91adff053741 | -7.43725 | -45.53687 | 2025-06-25 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12b0d74b-9385-3226-8ab5-61f8dbc07a0c | -2.45277 | -47.50391 | 2025-06-25 04:06:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e68300b7-a39b-3d7d-8718-060a60df4734 | -7.01843 | -44.55952 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 733a482e-7dec-3bae-803c-041b357ebf84 | -6.29562 | -44.23875 | 2025-06-25 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64161343-0bb0-3dca-baf4-a0f9db692f86 | -3.61376 | -47.53973 | 2025-06-25 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e535f5c-0476-3aae-a93b-977a877052d8 | -7.01777 | -44.56351 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08ea3127-c931-3b5d-ad3c-0dfb8e5ce22c | -7.00534 | -44.55538 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6deeb517-9c98-3290-aae5-cb7b76e59839 | -7.96666 | -46.4365 | 2025-06-25 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd9230dd-def4-3c16-b327-d7590a700367 | -7.0985 | -49.17292 | 2025-06-25 04:06:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 975b0f2e-b017-37a1-a3fc-35345f44bb59 | -5.47811 | -43.03395 | 2025-06-25 04:06:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5559217-2001-3bd3-8e7d-f98725826ac8 | -5.43717 | -46.28572 | 2025-06-25 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 32d3361f-a514-3d61-a5cd-4672d5d425b0 | -5.54696 | -43.93808 | 2025-06-25 04:06:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b3d0655-61b5-3442-a15c-03a524fa09e7 | -6.17691 | -48.05393 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c4176d2e-d778-3cc2-9618-01f33b3de10e | -7.8829 | -47.88161 | 2025-06-25 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 10577383-f0e2-3448-b538-1ae48599f045 | -8.4023 | -44.60868 | 2025-06-25 04:06:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b5e0ec1-353d-324b-aead-a714a4e49fc3 | -6.22057 | -43.36845 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 401ed85f-3f11-31dc-a30a-201a3080165f | -8.06779 | -43.11619 | 2025-06-25 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| df354d96-4316-34b6-b42b-c7888f7c1132 | -6.36349 | -43.65855 | 2025-06-25 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 96fc7c5c-06c2-383f-8e8e-e22f90fbead1 | -7.09427 | -49.17391 | 2025-06-25 04:06:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dcc98c2-f77e-39e6-96d2-0a7d96425c97 | -7.02907 | -44.56136 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2df3f209-c88b-361d-b8e1-deddb3d976ea | -4.52786 | -48.0098 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 872c6b55-0f55-3016-b81e-dee5f23fdc9c | -6.8129 | -42.868 | 2025-06-25 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d90e850-e861-3d34-8c03-90f675f5366b | -7.02712 | -44.57322 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2c56bf6-d269-3197-8c6a-fc782515c02c | -7.00956 | -44.55179 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0abbfe3f-8e24-3be9-bd34-2f88ee9fc1ae | -4.32713 | -40.17124 | 2025-06-25 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc58c844-95b4-39cd-bd86-06efebd930b6 | -7.03066 | -44.57389 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3c9aadb-03db-37c9-becc-1d47a7e52f45 | -6.29628 | -44.23475 | 2025-06-25 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44948ffa-7e14-3ed0-9ffb-50393af487de | -8.24321 | -44.94211 | 2025-06-25 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 92d2b508-445f-3267-a351-45846ed51afe | -7.55661 | -44.95013 | 2025-06-25 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a9b10298-222f-3daa-837a-d9c5200eeeb4 | -7.01557 | -43.87427 | 2025-06-25 04:06:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b2052cd-0ee4-30ca-87b2-c6e7242ef94f | -7.33719 | -43.1941 | 2025-06-25 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ecd22570-f5e7-38d6-8f32-99b9cca91848 | -7.43353 | -45.53626 | 2025-06-25 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f679242a-2a64-34ee-bc8e-585db868dbea | -5.75698 | -43.39493 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 866576d3-1690-38d0-8342-a44213456bdc | -7.01554 | -44.55494 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a3d30a81-941f-3b5a-ab42-00d60f019084 | -6.22675 | -43.35421 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e8aa1cb-52d3-33ac-8613-cc8936f27804 | -5.0693 | -43.72881 | 2025-06-25 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f9be47c-9640-39f0-b723-82a3d0e7c210 | -7.00908 | -44.54992 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 627e4408-a404-36a0-8632-aae4386f6c93 | -5.91891 | -43.4777 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0d5610fb-b30b-3ff9-bcf3-cbcbc8b99282 | -8.53551 | -46.32973 | 2025-06-25 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccfa6f61-4713-3dd7-8194-6acd61cd9731 | -5.7604 | -43.39547 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README9.md)
