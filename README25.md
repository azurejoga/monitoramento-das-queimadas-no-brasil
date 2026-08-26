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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1521ec6-c60b-30eb-8f68-bc65f191a5c9 | -13.65472 | -51.84994 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f2e15da2-78f1-3e71-9e99-b160b36b49aa | -13.18034 | -51.34613 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8f2d6c9a-be9d-37c0-9144-76aba10aa46c | -14.29108 | -51.14146 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3b0f6dfa-6528-3d07-8ba9-b3767bfb73f5 | -15.69456 | -43.79097 | 2026-08-26 04:10:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 53dc8b76-50f2-3228-a6fe-32bea1390cb3 | -13.23713 | -51.51424 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3240f40d-f06d-3c4f-9cb9-331c87ce87a0 | -13.23594 | -51.49147 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c28add0-9c89-30cc-ad74-37fbf8ae5988 | -15.77032 | -48.39635 | 2026-08-26 04:10:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2478b01b-b551-328a-8804-c5a90a206478 | -17.69253 | -40.17798 | 2026-08-26 04:10:00 | NOAA-20 | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3d1ae06d-5e25-34a3-aab5-4228c9a88f55 | -13.60828 | -49.0077 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e418da49-ccd9-3bec-acba-8350e0821b19 | -13.23072 | -51.37512 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| cf1829d1-3e62-3e91-aaa2-d3518879369c | -15.87993 | -48.34594 | 2026-08-26 04:10:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60372d2a-c2bb-33b1-91c2-867baf195ca7 | -13.61568 | -48.99354 | 2026-08-26 04:10:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c2b66359-93f1-31f6-a00e-0501544b8954 | -13.2448 | -51.38919 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7f02f04d-7606-3924-9fd7-4f094e332f25 | -16.09882 | -45.13795 | 2026-08-26 04:10:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bfd8d8a3-4d08-3845-bd19-4ba604256367 | -16.61967 | -43.41624 | 2026-08-26 04:10:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 28ca7ef3-d442-3038-9d01-e3d06b12215e | -13.25819 | -51.52249 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e0c81dc-c60c-3fae-ac8c-38a1d7c8a4c6 | -15.76953 | -48.40061 | 2026-08-26 04:10:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c89cbb4f-8880-3120-9656-6a70d06ffceb | -13.28804 | -51.46211 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 719589f8-8288-3136-a464-e7434d91b425 | -18.7821 | -47.62503 | 2026-08-26 04:10:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b532b954-3f05-3174-aa84-a8e09f3298eb | -14.93326 | -52.62892 | 2026-08-26 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3aad65cf-afb3-37d5-9727-514cfc53871c | -13.65611 | -51.84309 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e4faf81-b025-35fd-a15a-d353dc3ff945 | -13.8698 | -54.06231 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e031cd1c-9da9-36bb-a0f6-e013b2b4e37f | -14.62227 | -42.52894 | 2026-08-26 04:10:00 | NOAA-20 | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 09f7a431-e90c-3907-ae30-2f0b88988848 | -14.7873 | -48.79997 | 2026-08-26 04:10:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 403bf94c-5697-339e-a32c-9b193d83d01d | -13.25275 | -51.5213 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 327e63ed-35d4-3aab-8253-5bd97087f9e2 | -14.29622 | -51.11525 | 2026-08-26 04:10:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1e35f39-3cc9-3eb6-b007-2c382c564682 | -13.1897 | -51.35543 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 5adcf642-5517-3e52-9612-5bc0f5740a88 | -18.54386 | -42.57775 | 2026-08-26 04:10:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f096b82b-c954-3042-a2f6-06d85dd398ab | -13.2455 | -51.38564 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c09eaf6a-fbaf-3bf6-93c1-6b269b40ef99 | -13.22603 | -51.37044 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd8599b0-5eca-398f-a7fa-6baf6ce27080 | -13.23098 | -51.51669 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 225cd9e4-b3dc-3de0-bc32-1a7c08cf0dda | -15.05929 | -45.32109 | 2026-08-26 04:10:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b451814-b92f-3c45-9209-3053b1b75d29 | -18.77826 | -47.6242 | 2026-08-26 04:10:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98a33a23-b81f-37d3-8c22-ac47797fdf3e | -14.55172 | -52.31942 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d4d4140-a97f-30fc-b9b7-33dd6185d93c | -13.18449 | -51.34549 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 066057de-cda1-3f7d-88a3-30d493a856b8 | -14.31666 | -51.73183 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e92bc1d-c351-3019-9472-dd23c4fa5212 | -13.18782 | -51.35725 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 54b53515-6121-3e8f-bc56-e07155fac8c6 | -13.1791 | -51.34436 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a0cb38e-fd52-33e4-8078-6b84c7095347 | -16.86279 | -43.23774 | 2026-08-26 04:10:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 124e22e8-afd3-359d-beb5-7d5bcefb5e10 | -13.86174 | -54.03833 | 2026-08-26 04:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eb21310-2e5d-3bed-8ed3-9fb14ac4c359 | -15.60033 | -53.12687 | 2026-08-26 04:10:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| caa7e1cc-f9ea-34f0-9525-0a52f60b0674 | -13.66634 | -51.8494 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7609abc3-1862-37c1-81e3-2ca8d6bf6b0c | -20.52098 | -44.7308 | 2026-08-26 04:10:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 24bf95d4-0441-3e63-ad00-01a58d2f0e75 | -19.32036 | -40.14376 | 2026-08-26 04:10:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 2ea860d5-1efb-3c26-8235-140b8d3c12ea | -14.58247 | -52.02916 | 2026-08-26 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cadefaf-7bd7-36ae-bf76-b495e1c9e173 | -13.27551 | -51.4625 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cf14b9f3-07fc-3f26-9e2f-0fedea634eef | -16.6347 | -43.61887 | 2026-08-26 04:10:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 455bad4e-2417-3a4c-b9fa-829de5f574a5 | -13.66708 | -51.84573 | 2026-08-26 04:10:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1ba5a117-91bf-39ca-9f3c-3f63d4e15b88 | -16.56158 | -40.90056 | 2026-08-26 04:10:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dfc23485-977f-30d2-9cff-756dc15957ca | -13.17841 | -51.34789 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9d0a45e-df6d-32a3-b58f-dd774d38fe77 | -13.2345 | -51.41288 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 032490d9-d5bd-30e0-87df-3ff6128d058c | -13.2542 | -51.39858 | 2026-08-26 04:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 2e9c67dd-3e5b-3408-aad7-bc8342f805b3 | -17.17795 | -44.43322 | 2026-08-26 04:10:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a307caf9-06f2-36d5-bb2a-1d90997086ab | -15.06288 | -45.32175 | 2026-08-26 04:10:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c9332a5-691f-336f-a2e1-3f507b506ef8 | -27.34134 | -50.72396 | 2026-08-26 04:14:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 05af872a-3a48-3be7-a5cb-619555acab72 | 1.4734 | -55.9642 | 2026-08-26 04:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 5593ed9b-d5f7-3dbb-8fa3-c2d9d06283ad | -6.641 | -58.4987 | 2026-08-26 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 8bde41a9-ea89-3168-a24c-5f291c2bbb42 | -10.7784 | -54.0368 | 2026-08-26 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 270ea56b-b830-32e0-bb1f-8f558ad2edb8 | -6.6226 | -58.4995 | 2026-08-26 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 3eedfdb2-3afc-3af3-9dcf-da6a01519305 | -10.7598 | -54.0179 | 2026-08-26 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 23ddb65d-5a63-3d0f-8307-3bd7a35e34db | -13.19 | -51.3593 | 2026-08-26 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| d2098a4b-97b2-3d7e-a495-59bbe1d0c3d4 | -6.2677 | -53.3565 | 2026-08-26 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 8f11f5ef-7c96-35db-a189-c25b7cf3c5e9 | -13.2472 | -51.3735 | 2026-08-26 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 75169bd6-2f31-3650-baff-bbe87d2d4e47 | -7.529 | -61.3635 | 2026-08-26 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4d1b1b8d-34f0-3948-94ce-60523a63661a | -10.7596 | -54.0384 | 2026-08-26 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 96.7 |
| ebc39992-bc5b-3a4f-8580-0fdd894176b5 | -12.6836 | -48.4116 | 2026-08-26 04:20:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 49579e46-e134-3557-9da1-b98d5c42fe90 | -6.2676 | -53.3768 | 2026-08-26 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fcffc17f-020b-34c3-ae95-f0e42dd2b466 | -7.5104 | -61.3832 | 2026-08-26 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| ef0326e6-7346-3001-b756-03756628d10b | -7.5105 | -61.3642 | 2026-08-26 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| c9da933f-8509-3cd0-b0c9-bec404a33112 | -13.2469 | -51.3949 | 2026-08-26 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.1 |
| ff995711-11a7-3bb5-9bd6-a78e7b62cc61 | -7.0797 | -59.2157 | 2026-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.6 |
| a09feeb9-ca0d-30bd-a111-ccf7ba781f51 | -6.6595 | -58.498 | 2026-08-26 04:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 3940721a-1420-3225-89de-64de93fa9f77 | -8.1484 | -47.4998 | 2026-08-26 04:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 121.3 |
| a7e2ce3a-1ec1-36eb-8c17-13ccbfc7c686 | -13.1903 | -51.338 | 2026-08-26 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| ee151221-ea60-3ec9-b50e-20d53223f954 | -8.1299 | -47.4795 | 2026-08-26 04:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0ab0a21a-3dfc-3b0e-8579-2707795c3b1c | -7.5289 | -61.3825 | 2026-08-26 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 147.2 |
| b4613dbe-8143-3938-b7c1-0d03b799307d | -13.228 | -51.3759 | 2026-08-26 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 137.7 |
| 57b1e0bf-4a17-3432-a07e-1f9a35b0207a | -8.1296 | -47.5015 | 2026-08-26 04:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 527d89e7-d97c-3fb3-aed2-87173c61a0b2 | -13.2284 | -51.3545 | 2026-08-26 04:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7c04ccff-1783-3d58-ba12-8c80719fc764 | -10.3727 | -45.0537 | 2026-08-26 04:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 58d1c878-269a-37f1-a2bf-0184aba4ddb1 | 1.4917 | -55.964 | 2026-08-26 04:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 9ff7236a-513e-34a9-b810-4e0610d413ec | -9.6024 | -55.1078 | 2026-08-26 04:20:00 | GOES-19 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| bd01b31f-c34d-3340-838f-06f570fc293e | -8.1301 | -47.4575 | 2026-08-26 04:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ee91e94a-7c47-309d-9fd9-b463dd25ea80 | -7.0613 | -59.2165 | 2026-08-26 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| f67dc275-6db9-3129-8e87-0fa171a815de | -13.3034 | -51.4517 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 132.5 |
| 73ed1393-51d8-37e2-83cf-df15feb52b7a | -13.2469 | -51.3949 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 07c30500-5e31-3df1-8f67-1580478d0d57 | -7.0613 | -59.2165 | 2026-08-26 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b5cccaea-ba03-347f-9d06-0dc52801b473 | -10.3727 | -45.0537 | 2026-08-26 04:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 600ab052-7b94-3cf8-b25f-f02a6fab134a | -8.1296 | -47.5015 | 2026-08-26 04:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 223804fb-296f-3792-a8b3-895e4e27f49b | -13.2842 | -51.4541 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.7 |
| fd715cb9-c04c-3d0a-9aea-676f63e37502 | -6.6595 | -58.498 | 2026-08-26 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 208833ad-a8ea-31c8-b765-5a03dfdd6f22 | -13.2448 | -51.5229 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 14e933c2-3637-316d-8c3e-7c5872e16b67 | -13.228 | -51.3759 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.9 |
| 54541bfc-d9ca-3cd4-a800-333d27c88d22 | -6.2676 | -53.3768 | 2026-08-26 04:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| ee999738-c8aa-3742-ba76-58095f996f95 | -10.7598 | -54.0179 | 2026-08-26 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 6ffc178c-5a95-3894-8514-d6027155cbf3 | -8.1484 | -47.4998 | 2026-08-26 04:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 157.3 |
| b442a461-8624-3952-a29d-968fc61cd073 | -10.7596 | -54.0384 | 2026-08-26 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| ef2aefa6-8f81-3944-a995-97d5a7f6b428 | -7.529 | -61.3635 | 2026-08-26 04:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 3fe9159a-7825-3c32-b5fa-c958dfa4f079 | -12.0362 | -45.9917 | 2026-08-26 04:30:00 | GOES-19 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 82a24e31-bcac-31b8-9123-3f47d07fb3a8 | -13.2664 | -51.3711 | 2026-08-26 04:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |


[Clique aqui para ver as próximas entradas](README26.md)
