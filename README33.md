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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b8a0c1b-7d07-3150-8c0c-953a87fd6870 | -5.74996 | -40.44429 | 2025-08-24 04:32:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1933aff3-ab01-382f-b049-da20c9512cf6 | -6.68534 | -43.17559 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a4e6ea5-7e79-3e5e-92d2-eb0e07ea5930 | -4.82425 | -43.55074 | 2025-08-24 04:32:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 27a65cc8-0e05-39be-98db-9b4e7b8dce66 | -5.26902 | -44.27338 | 2025-08-24 04:32:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8158c84c-1053-34a9-a61a-7864a0d13a29 | -4.95718 | -55.81693 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 25be0a06-2295-34ff-9d26-59d382d459e2 | -4.56179 | -55.96507 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb8067cc-d140-3cbc-b01b-b6ea6fd340e4 | -3.60081 | -47.5252 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 7523db06-bf4d-3565-a4ed-a2eeaebec05b | -3.45061 | -44.14038 | 2025-08-24 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bfe0266-2eee-39df-bd4a-74861f89b7f1 | -2.71156 | -48.20833 | 2025-08-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e50fbbf-879a-3503-833f-228d9eadcd70 | -5.49482 | -41.40479 | 2025-08-24 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ece136b1-ffda-31ce-91f9-4a79b154531d | -3.66342 | -54.757 | 2025-08-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f4afe3ed-3c4e-3401-bc9d-67241c8ecd80 | -5.6404 | -51.72239 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69f84ed9-bbf1-3719-b66a-99c959445765 | -4.27852 | -48.64891 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ca9e888-e6c8-328f-90e6-d84003bb44b5 | -3.25182 | -46.90732 | 2025-08-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bd572ee-f119-3967-ba05-efd70ff73b36 | -5.48977 | -41.40841 | 2025-08-24 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 95690e50-160e-3be8-b6ab-c38cef99a3e6 | -6.76276 | -44.31499 | 2025-08-24 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b0a93e9-9cec-3451-9629-5e011e69d3a0 | -6.10049 | -44.69485 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2c7f09f-8bf2-3a96-b35f-679bc0f0efe3 | -5.66405 | -45.15065 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a91d4089-c6b0-3884-8a40-f31a5b1b2ec2 | -5.62 | -45.1073 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7e46582-2994-3aee-87e2-de8edbf9484a | -3.51488 | -47.2058 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3db64e17-cc72-383e-86e4-e40bde0ea4c0 | -5.48913 | -41.41271 | 2025-08-24 04:32:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 36bf113f-65c7-3686-9f7e-020cba7f8878 | -6.20099 | -42.98235 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 1861f340-8dbc-33d1-ae07-b6ec183b3df1 | -5.50242 | -47.504 | 2025-08-24 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6195a3a-2352-3eae-a41b-93852d1ffab8 | -6.70729 | -42.96558 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c4bfb597-f9ec-324c-bb34-cc69257a35ff | -3.39917 | -52.83444 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24139285-5fcb-37c1-aa06-3c7ec9fc537e | -3.44061 | -49.04504 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d1a715b1-aa31-3a65-b317-eb8ae409be54 | -5.31893 | -45.25385 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31211991-1a13-32ef-8fb9-173955581069 | -6.37167 | -45.52267 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b3a9409-f906-3717-9c6c-f6983815ec73 | -2.91421 | -48.30433 | 2025-08-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30fb5adb-df84-365f-a08e-0a710e239b90 | -5.41335 | -44.98873 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b5511c78-263a-3a23-8b67-4bd1cd93c6b4 | -6.59184 | -44.55744 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25c515ec-5845-3384-a88f-44f3b4309bf9 | -4.96154 | -55.82694 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| fde7a44c-e94f-3a6a-ba1b-1ba9897f9121 | -2.26399 | -47.85194 | 2025-08-24 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b719096d-03b2-3243-9480-1bace778be12 | -3.38706 | -47.61176 | 2025-08-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d13e5380-6a50-3e25-903b-ef37bc2f99da | -3.7907 | -47.57306 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4319b82e-1ad2-3124-88fd-31c16b10bd18 | -4.31095 | -48.09649 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 474cc8ce-8cac-3df5-a298-84d9cdff99cd | -3.5975 | -47.52469 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| f6dba95a-5ec5-398d-86af-2556229dcb0e | -6.77442 | -43.27916 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 736b6e90-46ba-3cff-a3f4-c27076f61121 | -3.52746 | -42.69864 | 2025-08-24 04:32:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5871f252-abe3-3e7a-b16d-0d598ed24eee | -4.63828 | -41.41805 | 2025-08-24 04:32:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d4ebd22a-e6cc-3058-ba69-4351b74a55c1 | -2.93145 | -53.70322 | 2025-08-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d79e427e-bf8b-3267-94ff-ab1ed2195112 | -3.5909 | -47.52367 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 05fdac21-d9c4-3359-b3cd-1745db45df17 | -6.4336 | -44.54108 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7a300a3-d40f-336f-bccb-878ae32ef27f | -5.66113 | -45.14613 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 419a645a-5676-3c38-9b53-fd32512ce79a | -4.78569 | -45.32685 | 2025-08-24 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f0099884-6dcc-3508-92dd-ba1f7490b248 | -5.64902 | -51.8395 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c20a9d19-ef4c-394e-b970-379a572ffc08 | -3.32925 | -48.71061 | 2025-08-24 04:32:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7de8d905-389d-31f3-8055-911bb74c32fa | -6.91866 | -43.7791 | 2025-08-24 04:32:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dbc4a64d-d565-3f98-b3f1-6b809da64244 | -6.21882 | -44.12019 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cf17f1c-f5a4-35ab-bdbd-66951755a50f | -3.73592 | -48.9355 | 2025-08-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2550f6ac-fad6-35e1-97cc-747824e4837b | -4.95623 | -55.82263 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a3d67e6c-c709-37e9-b10f-b7df903e7d6d | -5.81112 | -45.40088 | 2025-08-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60aabac0-00e1-3d00-ad44-a67200cf6355 | -6.26577 | -44.34089 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf8e90a4-4b04-3169-8c17-d28803723869 | -6.43791 | -44.53741 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11eeded6-3b88-3af8-a4e8-ef4c9bbaa118 | -7.05486 | -41.9094 | 2025-08-24 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bec6a39f-b60a-34e4-9938-c4282c308594 | -3.44004 | -49.04868 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 466e2f36-daeb-3576-a0c2-3a3ecc3af9e4 | -4.3071 | -48.09943 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 40d7dae4-04cb-3d9c-9c5d-682cab00a98c | -3.6587 | -54.75632 | 2025-08-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d387571-7b69-3e86-9228-3ff1d35fb757 | -3.7874 | -47.57255 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7a0590e6-8175-3424-a244-a277868d7f35 | -6.25902 | -44.33546 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 138ceab4-ed19-3728-8b1d-082cd9fde786 | -6.1861 | -45.43185 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f315260-bb60-3dc4-b9db-89914420b424 | -3.44634 | -44.14402 | 2025-08-24 04:32:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bb5ae37f-a049-31bc-a6b7-898c71b210c3 | -2.79207 | -41.88409 | 2025-08-24 04:32:00 | NOAA-21 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b0481cb-d43f-3a9c-a53e-dba397ff169e | -4.5603 | -43.2228 | 2025-08-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38192499-461a-31e8-ac28-96b2e8ea0e52 | -3.90078 | -54.6901 | 2025-08-24 04:32:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6f4e1fbc-9abd-31b4-9e26-496f1d2cc158 | -6.43229 | -44.5498 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbb9409a-c930-390b-9ea7-95bab2bd97f0 | -4.09938 | -48.74712 | 2025-08-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 240626ab-ef41-3160-8066-2fd9ce486066 | -6.10111 | -44.69064 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 382bd2e7-890a-380f-ac59-0bed6186b85e | -4.30764 | -48.09597 | 2025-08-24 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a7615d5-d171-31d5-bf36-5abd4054a527 | -5.57992 | -43.25129 | 2025-08-24 04:32:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33be2966-3079-39cf-a450-e45a4dfe6ed0 | -6.79885 | -44.9971 | 2025-08-24 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8170cd71-4988-3cef-8410-d2204deb169c | -3.59366 | -47.52761 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 90949d50-8fc1-3da4-ba7d-5cfc46763136 | -3.78794 | -47.56911 | 2025-08-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a40ff94b-c069-3af8-b49f-70e1315da776 | -6.7136 | -43.86122 | 2025-08-24 04:32:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c616275f-3608-3343-8d6b-8dabaada625f | -6.02706 | -42.80555 | 2025-08-24 04:32:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8d6b661a-7a58-3d11-a78a-bd742c465666 | -4.4832 | -47.67149 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 258e5b06-a59d-3404-876e-4d4078f6bdbf | -3.73312 | -48.93137 | 2025-08-24 04:32:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5794e3b1-1a93-3092-b782-ba2ebf4f0ad5 | -6.20007 | -44.11749 | 2025-08-24 04:32:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc31c9ae-62b0-3c6a-9b36-bf758ecdf463 | -6.09646 | -44.69083 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b7501ac-cdc2-3171-9c45-941a2a963c72 | -6.36817 | -45.52213 | 2025-08-24 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f0fe7a7-225b-34aa-a906-3368c361bcb0 | -2.869 | -41.75414 | 2025-08-24 04:32:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cfa2570f-b9c7-330d-8e7c-772df4810b4d | -4.70604 | -55.93475 | 2025-08-24 04:32:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45abf2d7-bf8a-38f4-87ee-4bf92af234ee | -3.43665 | -49.04815 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c3e79d07-f438-3af8-b93f-bfa4b50c984c | -3.13284 | -58.03931 | 2025-08-24 04:32:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e91090a4-9934-342a-af92-9d7f983b8160 | -4.69858 | -43.26033 | 2025-08-24 04:32:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bcf2b0d-3dc0-315a-ad1d-4af2cb667eb2 | -5.64525 | -51.83885 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0502da10-11ef-3733-a568-495642932d87 | -6.19788 | -47.84307 | 2025-08-24 04:32:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f10eda2a-7f93-345d-8283-32648ed445af | -5.5815 | -45.80735 | 2025-08-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 417c09a0-2faf-336c-b5e1-c50c0c36c7dd | -2.5869 | -51.91961 | 2025-08-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7589d514-2883-3d93-be2d-5ddddef0a770 | -6.50092 | -42.95409 | 2025-08-24 04:32:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a0a7e3a-d2a7-325b-a73b-18a48e2919e4 | -6.11604 | -44.41383 | 2025-08-24 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22334ef9-1041-3cdd-bca1-3cb4194b1766 | -4.29268 | -48.06178 | 2025-08-24 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04382a7a-83c2-3f6b-8476-e4dd9d2d2937 | -2.71489 | -48.20884 | 2025-08-24 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b8193d5-9360-3378-aaa9-c3151ff71910 | -2.26344 | -47.85541 | 2025-08-24 04:32:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed0ef251-090b-327e-b497-4628988fa8b9 | -6.20048 | -42.98579 | 2025-08-24 04:32:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 99bce56f-c4af-3fac-a1cd-fd719a5de0df | -3.84242 | -55.96495 | 2025-08-24 04:32:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e87b87d4-c195-3b5d-88cf-7545379af03b | -6.82301 | -42.8237 | 2025-08-24 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| eb7c1e31-dcdf-3f17-acc3-e754bbbc8a68 | -4.01705 | -49.50773 | 2025-08-24 04:32:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03cec6dc-f16a-3502-a89b-b6fafbc7c953 | -5.36865 | -41.21848 | 2025-08-24 04:32:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0f31d4eb-61bc-3269-934c-385add93cfb0 | -6.47595 | -43.45805 | 2025-08-24 04:32:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README34.md)
