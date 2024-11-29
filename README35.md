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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16066515-2150-338d-804d-d4ea2a8629a1 | -1.67943 | -45.79916 | 2024-11-29 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 139d80a3-2322-3d37-b439-8de9ad2caedb | -3.34242 | -50.23649 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daf46c1d-65d7-3332-9976-6248f66d377e | -1.08228 | -53.3904 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fb203c16-4386-3aed-b36d-602f69e00bf0 | -1.94359 | -52.97899 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a8187d96-cfee-3998-a88e-7725673904d2 | -3.96556 | -50.19204 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c64512c-b3be-3605-945b-272c00239879 | -4.85395 | -41.25582 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7f631063-209c-3eba-82da-f0f4983536ec | -2.84598 | -46.86216 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68d9e975-e4ec-361e-a269-33e85e73f906 | -1.71066 | -52.4966 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9b79ad6-f970-326f-94b0-fa961644d165 | -4.36056 | -47.25351 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3d802db6-10e5-3b5d-acd5-569f671343b0 | -3.97953 | -46.99412 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acc33160-ebbb-38df-a873-13784db7494c | -1.89529 | -46.69093 | 2024-11-29 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f41244d3-235d-3e5b-bae4-e112f74c3c58 | -4.22993 | -45.77974 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 235609b2-b8fe-3298-927d-e25f8e44fc59 | -3.61059 | -49.85902 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a12fb70-06f1-394e-81ab-24012532e30f | -3.34494 | -45.41164 | 2024-11-29 04:04:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f57773d4-12b0-31d2-83df-3e8cb13b1f19 | -4.91023 | -44.02607 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 93f5fef2-af52-3b6a-b74e-bc196a9e84eb | 0.94167 | -50.74401 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 63502616-a08b-353c-ad26-c904b1584936 | -1.62312 | -52.37992 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d8c7c522-226a-33a9-b004-3dc46277ea44 | -1.44196 | -47.11813 | 2024-11-29 04:04:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e96302ba-8077-3f54-a483-c09f2aa89277 | -1.72308 | -46.22429 | 2024-11-29 04:04:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab1f2e37-4638-3535-ac69-5be3d519a7c9 | -1.53122 | -52.6937 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 966eb65c-fb1c-3011-bf14-66337cce9bc1 | -3.1004 | -50.36258 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 314e295d-ea62-3efb-8b6a-bef4fbdc5db7 | -5.28144 | -45.12723 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73476ca4-be65-3e5b-9d39-c06794a64dc9 | -1.14245 | -48.34297 | 2024-11-29 04:04:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2233e0e3-b699-3c54-8ee6-917d3e22c677 | -3.46684 | -50.53575 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 608a5421-ab25-3e65-8022-dde8ed3920ed | -3.67833 | -44.70771 | 2024-11-29 04:04:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6e53f0a-c95b-323d-80d1-759d6f9fe489 | -3.69288 | -42.04343 | 2024-11-29 04:04:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 51ef738f-29e4-3009-a0b2-20acb271b121 | -4.31193 | -48.21071 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97b20b43-2c59-309a-97f3-9f1df2bc417e | -3.46064 | -50.53854 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07da3624-b234-3932-aa36-f293fe04aaf8 | -4.64113 | -45.96982 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 483d20d2-60cf-33d7-8e1f-40293abed0b3 | -3.38784 | -54.29393 | 2024-11-29 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4397c44d-e759-3c83-a7cb-660aa71e0acf | -2.65087 | -48.7879 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7fc13221-bae2-30d3-8ccb-cf55120a0c97 | -3.38467 | -50.11813 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8cfd82e0-6f6c-325e-934a-f14c9e98044f | -3.96302 | -48.08402 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a08d6c74-3c67-3079-827f-36e1bd53a659 | -3.93411 | -46.51231 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5799394e-e2a2-32e2-bf3a-3f53c3ed6810 | -4.92534 | -44.53218 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c75813e6-2ceb-3c6c-a8cf-149a1741b117 | -1.6753 | -52.43005 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b74340e7-644e-30d6-9e18-f7f425713763 | -5.75154 | -43.40002 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 09f4f51e-d3f9-3f9a-bb69-17d16916eabb | -3.82045 | -44.0449 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1244b81-31be-3b75-b383-6f99c1b3fed2 | -1.69951 | -52.64587 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| defbc6f5-cfd1-3920-8706-6cbdab801e71 | -4.07382 | -47.02558 | 2024-11-29 04:04:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a95dbc4b-62eb-300f-a299-f4ba539a72f3 | -7.26593 | -35.14942 | 2024-11-29 04:04:00 | NOAA-20 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d8cda885-7eb2-3950-8492-3ad36de98b48 | -5.62791 | -46.96535 | 2024-11-29 04:04:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 352cf45f-75c9-340d-8acf-b261fcf52b60 | -2.86143 | -46.87758 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7294957-1428-3bff-bdac-1c14e4c170c5 | -2.5301 | -47.33334 | 2024-11-29 04:04:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08b88969-259d-3de8-a6fc-97268fbbddea | -5.01489 | -43.98402 | 2024-11-29 04:04:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8026504-d7e0-347b-9e01-c845ec0609a0 | -3.61113 | -49.85583 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ff2f549-8c9d-3f2f-86f1-4599a51ace68 | -3.96586 | -47.23887 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2056f914-57ed-3bd4-8a4a-d666b7c4c6c4 | -6.14766 | -42.16411 | 2024-11-29 04:04:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b4c3e46c-adf9-35e5-bc75-d031ca6f9ec1 | -5.36912 | -44.84719 | 2024-11-29 04:04:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 564e6947-90ce-30a6-8425-13684494024c | -2.41534 | -47.60609 | 2024-11-29 04:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ce728af-d00d-3e63-9f36-4bb2816651c4 | -3.75953 | -49.90477 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92628c94-2749-30bb-97ef-7969a941117e | -7.02246 | -39.36747 | 2024-11-29 04:06:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e5da203a-3fd2-3327-b2d2-ba7d06513e29 | -8.37329 | -44.47734 | 2024-11-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a47b7f00-5177-3bc4-ba6e-4dd1fabe14fe | -7.69323 | -42.97457 | 2024-11-29 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b165248f-892c-30db-9c02-1151a909bc3c | -6.82053 | -46.77054 | 2024-11-29 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d011d32-3844-3f72-81a9-efa7fcf6706d | -10.19793 | -42.4794 | 2024-11-29 04:06:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a7473d8-e977-332d-8fcc-3a988f625c5c | -5.8766 | -47.31549 | 2024-11-29 04:06:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1296d10-f0e9-3789-9be8-05f9539bdc8e | -6.51903 | -46.85221 | 2024-11-29 04:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb62eefc-8825-3a57-a377-7e1f738ee5ac | -7.44433 | -39.84041 | 2024-11-29 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c1e1dfc8-874c-3fe9-af16-b3ec56e28906 | -10.51822 | -42.40917 | 2024-11-29 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4958edff-bec7-388f-904b-b6cace9da924 | -11.39835 | -45.0859 | 2024-11-29 04:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24352815-e4eb-3e7a-93c6-2a48008e5d42 | -8.71839 | -48.29112 | 2024-11-29 04:06:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb357533-158f-3618-9090-1a5562c4a3fd | -9.4467 | -35.91024 | 2024-11-29 04:06:00 | NOAA-20 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| ace6ca96-c56f-326e-8730-3d9edbe06850 | -10.19848 | -42.47591 | 2024-11-29 04:06:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 57ada6db-5be9-39bf-b3d2-98c94fe4ecbc | -6.92743 | -43.50373 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a55ce5e3-f452-325a-a1bc-a2a2caf202c5 | -8.12815 | -47.98811 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e860dbee-d580-3d8c-bcd0-d0a3aab18ed2 | -11.40185 | -45.08649 | 2024-11-29 04:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 82b357c2-7414-3f4a-94ca-df63170e3822 | -6.11798 | -44.91673 | 2024-11-29 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| efbbaebe-5038-3672-8f46-6a5c2b7ab9fc | -10.69525 | -37.05088 | 2024-11-29 04:06:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3bac56d7-37d0-38be-af90-3ff80fc100b9 | -6.48566 | -44.68201 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| aa4487d6-a281-3c5c-a501-e7b4e4cc5d12 | -10.09417 | -44.35214 | 2024-11-29 04:06:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fcd082fa-e911-3992-942e-e79e98a1ab6d | -8.37744 | -44.47397 | 2024-11-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32ccf708-73d1-39bc-b566-1b1a4684be4a | -6.15928 | -44.70752 | 2024-11-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c29c1dd9-84b9-34cd-821a-5b2d4d92b19b | -6.75349 | -46.5275 | 2024-11-29 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9e10030-e53f-31a9-929e-71ec3133ed67 | -8.13339 | -47.99171 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e9a4c407-8ea4-3dc4-a0e4-a8535ddc2ccb | -6.90412 | -41.87062 | 2024-11-29 04:06:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 680ac88e-fc6e-3314-9925-f3fed16db968 | -6.74948 | -46.5268 | 2024-11-29 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0422853d-92b8-312b-beeb-f205596c6cf7 | -6.90467 | -41.86716 | 2024-11-29 04:06:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 19d067c6-af1c-342d-a601-ee2a2e0d66e3 | -10.09356 | -44.35593 | 2024-11-29 04:06:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1a02c565-20de-3b70-bd8a-ebde34a4e4bc | -7.0628 | -38.97341 | 2024-11-29 04:06:00 | NOAA-20 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da9d0c24-03d3-3390-81cf-62ae79fd339c | -11.37625 | -39.30139 | 2024-11-29 04:06:00 | NOAA-20 | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b2a1fc2-0b30-3120-ae83-7e00bec7d999 | -7.68931 | -42.9776 | 2024-11-29 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b57bc253-e85c-32e9-9e45-d54b3ed5845e | -7.83594 | -48.19434 | 2024-11-29 04:06:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c182e3f5-2cdf-3884-8bc5-beed4e807eda | -6.93085 | -43.50429 | 2024-11-29 04:06:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cddaaee6-0735-3330-8bec-3d02dee42e84 | -9.12455 | -47.71167 | 2024-11-29 04:06:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb09c4d9-1521-3ad0-ac1e-e13dde9f2d33 | -8.28003 | -48.02933 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efa11ee8-9d2d-38cf-afc1-a8f017236dd4 | -11.4012 | -45.09044 | 2024-11-29 04:06:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8ec84863-ce29-3e88-8de2-b675b809864e | -6.00252 | -45.75838 | 2024-11-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0077ffc3-ffd0-3d6b-9bcc-6ef68914f9ee | -6.11727 | -44.92109 | 2024-11-29 04:06:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 432f4800-1717-3e35-a344-27c005590944 | -9.91232 | -48.10436 | 2024-11-29 04:06:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e73372cb-6c75-3151-8189-e8ca6c5ddb26 | -8.27858 | -48.03775 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4948da48-70ba-3670-91ca-d3ca2a519294 | -7.98395 | -38.27386 | 2024-11-29 04:06:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d2dd572-36df-3e8d-a2b8-868bdc52967b | -6.8199 | -46.77423 | 2024-11-29 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0fc252d-e8ad-36f4-81f3-5ae66881f9f1 | -9.30114 | -46.22542 | 2024-11-29 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bf92145f-52a9-325d-bd0f-796035012213 | -8.12744 | -47.9923 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f8b14bca-fbc6-31b9-aac7-9282cd5d8d2f | -7.91384 | -38.41927 | 2024-11-29 04:06:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 03ca8531-c3a0-3fa1-b6b2-695300024d23 | -8.13413 | -47.98753 | 2024-11-29 04:06:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 64249165-06f4-3577-9f0e-434f5b43d223 | -9.31332 | -46.2227 | 2024-11-29 04:06:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eecc4f0c-bf34-373d-ada0-c2f1baae8fb0 | -8.13023 | -44.47982 | 2024-11-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f27d4ef-5708-3953-ae5d-a396465bfe2a | -10.52153 | -42.4097 | 2024-11-29 04:06:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README36.md)
