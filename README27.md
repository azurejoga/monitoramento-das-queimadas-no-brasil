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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27dee76b-47e0-3b80-816a-87113a5b7cec | -12.23967 | -50.73375 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84a8d3af-596b-35b9-aae5-dd51a9580820 | -12.20708 | -50.74651 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63423010-2009-35bb-95d7-9bbd67ee4dad | -10.90163 | -53.94831 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb02e4ea-5251-3777-aba9-e237366f8593 | -12.23303 | -50.75434 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 285c7f93-4acb-3626-93cd-fb028749246e | -9.02334 | -49.63635 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff7afb5a-8a67-3cbf-bb9e-34b85a9d092b | -10.90743 | -53.9362 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 137463d4-1522-3c8e-b816-1c80c029d6ef | -11.18542 | -46.04215 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1a8e834a-2e8d-3495-84a6-b813c85c3a6e | -6.65126 | -55.0761 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e392ae73-583b-3e7a-bc6b-6e8e6010ba79 | -10.28127 | -49.95074 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38184ede-ba0c-386b-be6b-48ede1069ab9 | -6.06856 | -44.87486 | 2026-09-25 04:46:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 339d0676-4d31-3c48-bc95-e420250b2a36 | -10.61505 | -53.99936 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d5c65cd-0a1f-3fcf-a40c-2ba8d763f269 | -12.2076 | -50.78632 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| beabf708-c042-374b-ac97-023bf4d97015 | -10.89874 | -53.94345 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 55018bb3-3f8d-3ed4-8209-af392ac4e518 | -9.2118 | -60.45952 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ae53d06-11b1-38d5-9412-1d1f281c6624 | -6.68498 | -55.05122 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee135c90-0596-32db-9e37-7f69a2b2cb7a | -6.51148 | -55.36633 | 2026-09-25 04:46:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1be577fd-1693-3b46-92c3-2662d6d1c958 | -12.20927 | -50.77576 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 27f5d790-ba40-358b-8904-454659e62886 | -10.85669 | -54.03412 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46b6f703-4014-3004-a668-eba253edac7d | -12.19824 | -50.75952 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44122a41-c384-3864-9dfe-74198ffb3e6a | -12.22309 | -50.75273 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| a84e9ba7-6b82-3b34-a84b-d5f02581df3a | -9.02998 | -49.63741 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 902173ed-1754-3562-9f64-3d039c99230f | -10.62014 | -53.99138 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 099d6752-a003-3522-b38d-78ebff89c05c | -11.28479 | -51.2923 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7f723645-fe3a-3857-ba3a-5a15164a1d3c | -9.14869 | -59.47169 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 263efbf3-cb3f-328f-be77-c00b12b4e9ad | -8.77322 | -45.59552 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5194e61-a0c3-3ba0-96d5-30a9681539ac | -12.23083 | -50.74676 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 75d3bac2-b7a9-39fc-936f-24518cc3744c | -12.21425 | -50.76574 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 60c8dc3b-6f74-3f8b-b135-478f6ee7a7bb | -9.0183 | -60.56015 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 458d8d0d-9759-3605-adcf-8d1960f35089 | -12.23299 | -50.79767 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34a67703-5a6c-3da6-b575-e650e4569e76 | -9.15035 | -59.47201 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| de3db661-1db4-3598-813d-8ff9a70de478 | -12.2181 | -50.78442 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bac71457-18ee-33ff-b78a-c7caf2c3590e | -5.83371 | -47.75346 | 2026-09-25 04:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86472d32-0616-300f-a6d0-421a2f2f085c | -12.21147 | -50.78334 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c410cf45-8d47-3a8e-a4a6-618c1bd44f5b | -12.23856 | -50.74079 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ec4be84-893e-37f8-9a0f-c51e96d53127 | -12.23301 | -50.77602 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d05bbeec-6e24-3e98-ab90-e47cbd8b950a | -9.03356 | -45.02946 | 2026-09-25 04:46:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 678a5a0b-0e70-3173-950f-a989107bf760 | -10.61869 | -53.99999 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2236642d-1ab6-3d4f-8907-8b9fb23a81e0 | -9.62735 | -49.02125 | 2026-09-25 04:46:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e7e58e5-d72f-3691-ac42-235a272d6d6f | -12.22915 | -50.779 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d556ab1-ff19-3ee6-bcf5-0d152560c778 | -9.20081 | -60.86424 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de71ade2-bce6-3280-ad1d-8475f663aee7 | -10.42313 | -53.78097 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63528d89-8889-3b27-90b5-99d80facd023 | -11.27039 | -51.29718 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45894d8f-cd72-3f55-8b02-bc064b4a6a01 | -12.23079 | -50.7901 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25d7b406-f5cd-3ac3-a8a3-af60b477cd55 | -6.45124 | -57.77717 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e41117f3-53dd-3dee-8d11-572798b2fddf | -11.72434 | -50.55665 | 2026-09-25 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ff70ad6c-cb9e-3575-a8ed-0b9a3413bf06 | -8.94257 | -45.88985 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14af52db-db18-3d7e-b999-0942a0b5b61d | -8.30236 | -54.76917 | 2026-09-25 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e88b5175-b94b-3ac7-b484-fdb67e222c8f | -12.21095 | -50.74352 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d22b6b89-eb2c-3987-b77e-2bb0e89ca4d5 | -11.2754 | -51.28715 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a5547570-4c1e-307f-a058-0e12f601feb9 | -9.36029 | -60.36859 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03669fb5-a45a-38ad-a45a-79e59c6620ad | -11.27816 | -51.29121 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9a96726-5143-375d-989a-8c547d5aa297 | -11.97193 | -50.70871 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 738347d7-e737-3219-943e-0a6713a6c7f7 | -9.15866 | -59.41884 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc0e4682-a7b3-384b-9cf3-8b773fa11988 | -12.21922 | -50.75571 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 86617402-bc6b-323b-b20e-02647e966336 | -12.20762 | -50.76466 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9978e7b1-bf78-3df4-a20d-680faf2551fb | -12.22032 | -50.77034 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 25395de1-4415-3898-9b47-925c73ae3f89 | -10.75096 | -50.82711 | 2026-09-25 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b4de94c-8124-318e-801a-354e6111e698 | -9.73664 | -54.80718 | 2026-09-25 04:46:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f361a7cf-32bf-333b-83a1-6d623f1b7f3a | -12.2264 | -50.75327 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| fd9e5ad9-1937-3d22-89ea-df30c516adaa | -12.22916 | -50.75733 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9b25a19d-d608-323e-a31c-9285fed9f6df | -9.02569 | -60.52058 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c090714e-c100-316c-a1f2-8d8d8f4d5841 | -12.24406 | -50.77059 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 60a24b4b-08e4-3bd7-953c-78854ffa75b8 | -12.21203 | -50.77982 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5028fc4a-9e57-342b-993a-25342fbcd496 | -12.22529 | -50.76031 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| e5a46d0b-ee4d-3b68-b6bf-675076835991 | -7.70128 | -46.66367 | 2026-09-25 04:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dccd7b1b-fd5d-3aba-8246-f4b99237e660 | -12.22089 | -50.74514 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4a35f183-6e97-3cb4-bb37-1535e07eeaa0 | -10.64034 | -51.34937 | 2026-09-25 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d239774f-6958-35fc-a6eb-350362404ece | -8.32831 | -55.27827 | 2026-09-25 04:46:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8009ea37-cb5f-3864-a4e6-3e2afe16fa73 | -10.89945 | -53.96107 | 2026-09-25 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6babda59-ac2f-3ad8-8ef3-126ecebdf884 | -9.02666 | -49.63688 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77075d1b-9547-3356-8a40-68bdaecda181 | -12.22196 | -50.78144 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 80503acc-69de-3812-9447-9ca9fda0274a | -6.31091 | -57.75728 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a2e0de6a-fb0d-3144-b2a6-96c39d1baf1c | -12.21369 | -50.76926 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b3156987-4395-3f4f-9851-1946d6238115 | -12.18774 | -50.76142 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e7e948c6-9dd6-3684-94ed-cb2666686ea1 | -11.28091 | -51.29528 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 17da8138-2b5a-3d2c-8f72-c0dfd00084a7 | -11.17915 | -51.38006 | 2026-09-25 04:46:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e86f0346-cb2c-3ceb-8785-b33c1c0e9470 | -11.2759 | -51.30532 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7705341-4efa-30bd-b78c-c018c6914cb3 | -9.04546 | -61.02275 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f494d0a-17fe-3d44-8b2d-a87daf565b17 | -6.31689 | -57.75245 | 2026-09-25 04:46:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 364c4157-6df3-3d0a-99ab-ea2037c04d17 | -13.40222 | -40.96663 | 2026-09-25 04:46:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13185d4b-9e02-3c61-9a56-f5eb931911ae | -8.77714 | -45.59607 | 2026-09-25 04:46:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 898a03ad-bfee-3a1b-a7ed-858e0c37ecb0 | -12.20153 | -50.78172 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80546737-be99-31bc-ba3c-5e7f6d479ebc | -9.02002 | -49.63583 | 2026-09-25 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1df0dc2b-6ebe-3f5c-a01c-70208b8b26f2 | -9.35467 | -60.36766 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 663e6162-c335-3cb1-b931-d9a8ad586ab8 | -12.22306 | -50.79605 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14a977bf-e22f-3dcf-9c1d-4031a6e11b14 | -8.33291 | -44.1569 | 2026-09-25 04:46:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c6513403-f537-3b35-bcf6-da28942255be | -12.21534 | -50.78036 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 61adfe85-23f9-3ec4-a67e-fdb6897db1c1 | -6.83199 | -43.56548 | 2026-09-25 04:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5bec188f-7f71-3c55-a54d-66d5c830b6ca | -9.15399 | -59.47268 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f91e4ad1-8103-3bc0-b140-08d72bdf3879 | -12.20155 | -50.76006 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 41a73c96-1619-39ac-b4e8-a1876e6d88ed | -10.27795 | -49.95021 | 2026-09-25 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98243562-9227-3ed4-adc9-573220e6d3e5 | -12.23136 | -50.76491 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f1da4e0-01d6-3655-a7bb-e0f761b759a0 | -9.15462 | -59.46933 | 2026-09-25 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da75f35f-284d-3a55-81a3-6444269ef191 | -11.2831 | -51.30288 | 2026-09-25 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18492801-e691-387d-89d5-818f947a2787 | -9.588 | -60.52214 | 2026-09-25 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fa4036e-a5f2-384e-be4e-0a46c0a4db8c | -12.21811 | -50.76276 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6cd708b6-67ad-34cf-8894-221b7b0566b6 | -10.41092 | -53.80925 | 2026-09-25 04:46:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2d36f65-56be-3bf9-aff5-0f94c221c0ec | -10.67372 | -52.50879 | 2026-09-25 04:46:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c6e224d-10af-3806-ac33-e8dcc55911f8 | -12.20101 | -50.74191 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc8e61f0-242f-3834-84a4-cbfbf00aea84 | -12.18609 | -50.75032 | 2026-09-25 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README28.md)
