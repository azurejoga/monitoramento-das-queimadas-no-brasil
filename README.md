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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5efaa76c-1502-351e-b9bd-6a6aec611f55 | -12.5682 | -57.7579 | 2025-01-27 00:00:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| b6b7ba06-3733-3aeb-87e0-3f885b437540 | -8.1206 | -43.124901 | 2025-01-27 00:04:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a0dde061-7c19-381b-b1ff-170ab5684be9 | -8.1108 | -43.127102 | 2025-01-27 00:04:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a6fc3593-6346-3137-a6b7-469723b028a0 | -11.2677 | -37.284901 | 2025-01-27 00:04:00 | METOP-B | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f7b55e21-8a2d-35a9-a53a-056bb6ebc50c | -6.57 | -51.069302 | 2025-01-27 00:04:00 | METOP-B | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5834d533-f861-3abc-bed6-f24411504019 | -17.7939 | -40.168201 | 2025-01-27 00:04:00 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ea57f413-4460-3559-b9f3-4b57df90ee4d | -17.7971 | -40.182598 | 2025-01-27 00:04:00 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6ddc21a-2a86-3acf-8b1b-16155ccfdfbe | -5.2811 | -45.7687 | 2025-01-27 00:04:00 | METOP-B | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c56bc8dd-f571-3a1c-b94c-08d543f18674 | -17.7955 | -40.1754 | 2025-01-27 00:04:00 | METOP-B | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 103ba46c-a599-32a9-b1a5-2655197a077c | -8.1222 | -43.131802 | 2025-01-27 00:04:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ad648898-6568-3b79-b028-86080e59f633 | -30.4578 | -54.1683 | 2025-01-27 00:30:00 | GOES-16 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 85.3 |
| 1dc67d82-6a13-3da7-89de-fca8bef77f17 | -12.11717 | -43.64123 | 2025-01-27 00:39:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8e3d2c0d-cecf-31c3-9e9b-c02198de2c0d | -5.27587 | -45.77406 | 2025-01-27 00:41:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a462b37c-5420-3e02-9bbb-3b235df01fd2 | -8.11326 | -43.1259 | 2025-01-27 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| bfa1232c-e3f6-3a6c-8cd8-40e737829c08 | -8.11489 | -43.13698 | 2025-01-27 00:41:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 6e053079-3055-39a9-8008-330ee329c546 | -9.23424 | -44.5584 | 2025-01-27 00:41:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 810807f7-bf8c-33bc-8883-6bdc869330b4 | -19.195499 | -52.314602 | 2025-01-27 00:58:00 | METOP-C | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| fc8da862-d9ca-3de8-a229-8c505a22dbbf | 4.2415 | -60.9049 | 2025-01-27 00:58:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 64fde4c6-57ea-3cea-b6d2-c9b865ad1cea | -12.5614 | -57.753899 | 2025-01-27 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35b301b3-5a78-3e9d-b12c-b8b7e8e1aa0f | -13.4808 | -52.9398 | 2025-01-27 00:58:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a2c14716-062d-3dc5-b7e9-2be43ccb533f | -19.197201 | -52.322601 | 2025-01-27 00:58:00 | METOP-C | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3d21a857-d915-30a3-bcf4-af3c055aa666 | -12.5588 | -57.7411 | 2025-01-27 00:58:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 257b03e3-2176-34dd-888a-98e520e56a1d | -2.8298 | -52.1278 | 2025-01-27 00:58:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21a49bec-f8d9-3e8d-9212-50b48cee5fc1 | -12.36974 | -38.45539 | 2025-01-27 03:12:00 | NOAA-21 | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f87d1d8-feb4-3608-9f25-ff087859db17 | -20.43196 | -40.8539 | 2025-01-27 03:14:00 | NOAA-21 | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 7f3c01d0-1c90-3c73-ba90-eecac4acf47e | -5.5192 | -37.48354 | 2025-01-27 03:36:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ab333acb-ac91-3868-9e39-14f00735df78 | -5.52298 | -37.48417 | 2025-01-27 03:36:00 | NPP-375D | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6a35e552-36bd-3391-aa98-f4b66df31296 | -8.11845 | -43.13057 | 2025-01-27 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 22ad0535-e8ba-37de-9296-01170c49412f | -8.11787 | -43.1338 | 2025-01-27 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| db6db00d-bdfa-3b53-ac5e-16bf76833812 | -12.11235 | -43.63956 | 2025-01-27 03:38:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52bfd9c8-757a-3e26-8de1-fbfba76f6460 | -9.22762 | -44.55307 | 2025-01-27 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f424cc77-2b41-3d9a-b238-582c09e23fbc | -10.22056 | -36.65635 | 2025-01-27 03:38:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a94ab06f-83e0-3da8-95eb-4fa8afb494ac | -14.11856 | -41.67644 | 2025-01-27 03:38:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bd718dad-b834-3919-8ed0-3643a66f6430 | -8.11262 | -43.13281 | 2025-01-27 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0de1ba01-2537-38fd-859f-c8ddff96a5b1 | -10.13032 | -36.19984 | 2025-01-27 03:38:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52faa87f-ebe6-30e7-9404-ce356a355942 | -9.22826 | -44.54967 | 2025-01-27 03:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd936f06-4032-38e8-9a69-8cc50453ec8f | -8.1173 | -43.13702 | 2025-01-27 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f1f8ec18-4cf4-3477-a134-5944f1743ead | -12.36705 | -38.45342 | 2025-01-27 03:38:00 | NPP-375D | CATU | BAHIA | Brasil | 2907509 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18c010e2-faf0-3d3d-9a91-4a78790de9a4 | -8.11319 | -43.12957 | 2025-01-27 03:38:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 22acb918-61fb-3cd3-bdc3-0a4a727c176b | -9.6153 | -41.65457 | 2025-01-27 03:38:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 170f8d2a-06a5-36b5-b169-45e4b406d9fa | -10.21711 | -36.65577 | 2025-01-27 03:38:00 | NPP-375D | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5f0a19a3-9fe0-33e7-8b63-6483d60b4d40 | -19.71847 | -40.35382 | 2025-01-27 03:40:00 | NPP-375D | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c99a3eb4-8947-31e1-97af-68d4d7b89c69 | -20.43572 | -40.85073 | 2025-01-27 03:40:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad3acdb8-7f81-3abc-b09e-70c8bba8a354 | -20.43201 | -40.85002 | 2025-01-27 03:40:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 15135573-654f-33d2-926e-f924e207ded3 | -20.4349 | -40.85533 | 2025-01-27 03:40:00 | NPP-375D | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5a538cd1-d249-3de0-a61d-58bed98fab4e | -8.11752 | -43.13788 | 2025-01-27 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b2cba9ea-6af6-321c-bd70-26bdd778fd36 | -9.22777 | -44.55409 | 2025-01-27 03:59:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 320ac59c-3389-3068-bfb1-67ab70298332 | -9.61434 | -41.65426 | 2025-01-27 03:59:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b74ce20e-2c19-361e-9599-770744c72f88 | -8.49907 | -43.28905 | 2025-01-27 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 67da2cb5-fcda-3fd5-af02-0a3059efdde0 | -8.11465 | -43.13328 | 2025-01-27 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| aa4756fa-5ce2-3502-af5e-8ec344df0eaf | -11.10308 | -43.34101 | 2025-01-27 03:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 32c2ace4-bf18-32e4-a414-5012e631919d | -11.10105 | -43.34315 | 2025-01-27 03:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50901580-27e0-33d0-9126-6f3cd68ab5a9 | -10.70149 | -41.86354 | 2025-01-27 03:59:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f53c3971-9328-34ce-b999-c441ce3b34b9 | -10.77283 | -44.55196 | 2025-01-27 03:59:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59be2bcb-3233-3849-a2ac-6da073d067a3 | -8.49859 | -43.2878 | 2025-01-27 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b2cd8410-e67f-3528-a3ed-4de35bd9e03f | -11.10169 | -43.33929 | 2025-01-27 03:59:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9dac74a6-4545-3d1e-bd9c-beef836afcf8 | -8.11686 | -43.14189 | 2025-01-27 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5019afd5-4c3a-3820-90bb-2d1da7d7c792 | -10.13013 | -36.20156 | 2025-01-27 03:59:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 21541d54-6553-3bc2-b0ff-9b320d9d7e40 | -8.11531 | -43.12928 | 2025-01-27 03:59:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| 07065bfe-af5e-33c5-af6b-a98927b8fe21 | -18.03847 | -39.92541 | 2025-01-27 04:01:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 71cad1aa-7382-3e6c-9a3e-507a472e8018 | -17.29253 | -53.77567 | 2025-01-27 04:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 59b09177-70db-36d2-8992-21823082edd1 | -17.29353 | -53.77111 | 2025-01-27 04:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9923fd8-87e2-3db7-ada9-ff517046f74a | -17.29432 | -53.77707 | 2025-01-27 04:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 236f63b4-8421-3ee6-b600-79a327eb135d | -12.11346 | -43.63761 | 2025-01-27 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58e405b8-b797-3a7e-8d99-b314071c8564 | -12.11282 | -43.64151 | 2025-01-27 04:01:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8193c0b8-4e98-35ec-b261-9255d8d08f9b | -18.03817 | -39.9271 | 2025-01-27 04:01:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 154cf247-ca91-3853-80c1-d98d4cbf2b0a | -17.29626 | -53.76794 | 2025-01-27 04:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b234881d-a132-322d-bca4-af3d0c88de46 | -17.29455 | -53.76648 | 2025-01-27 04:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d3f5797-6028-3f12-95f2-38e8f4b056aa | -16.6815 | -43.8823 | 2025-01-27 04:01:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b59f5e9-10ba-387a-b69b-761945d12c49 | -17.28843 | -53.77581 | 2025-01-27 04:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 267f52ef-b558-3f28-ad19-adfda5b43e93 | -13.30134 | -44.30193 | 2025-01-27 04:01:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 444f2c9f-81cc-3190-9168-45d4444b35ee | -17.29527 | -53.77257 | 2025-01-27 04:01:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 857984d4-9754-3f95-b4ff-0ec838db7bab | -16.68089 | -43.88599 | 2025-01-27 04:01:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 865323ff-3b83-3299-9528-a576c737866f | -19.83714 | -40.0831 | 2025-01-27 04:01:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7f1c5c47-eeab-38b3-b57f-b8c06300200f | -20.34943 | -40.35965 | 2025-01-27 04:04:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d99c8606-122f-3a49-9e6d-a47071c1352b | -20.43451 | -40.8526 | 2025-01-27 04:04:00 | NOAA-20 | MARECHAL FLORIANO | ESPÍRITO SANTO | Brasil | 3203346 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8ed39865-9caf-3569-8ff7-15c2cfa46d4f | -23.98487 | -48.91957 | 2025-01-27 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd98806f-a76f-34d5-afe3-80e05d86281c | -29.29824 | -51.32787 | 2025-01-27 04:06:00 | NOAA-20 | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f9d21fa-0ba2-35d8-9d08-d80839778bcf | 4.28673 | -60.88343 | 2025-01-27 04:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9087d070-e3b5-3523-afbf-2f8e05ab1720 | -2.52868 | -53.98237 | 2025-01-27 04:50:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ab58e8d7-e318-3966-9a32-9823bc689745 | -3.45898 | -52.86114 | 2025-01-27 04:50:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d2e049c-c1fe-360e-990f-808be614706d | -2.94781 | -52.32267 | 2025-01-27 04:50:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d2873c0-2486-3a32-a5c3-78971726c3dc | -0.82777 | -47.45212 | 2025-01-27 04:50:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9664407-d5cd-33f1-9b2b-712accb6fe82 | -2.90911 | -54.28809 | 2025-01-27 04:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab0595bb-4551-3f1b-85bd-00a687977db8 | -3.45843 | -52.86465 | 2025-01-27 04:50:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9894254-ca66-362c-9f12-4c37859573af | -0.82587 | -47.45407 | 2025-01-27 04:50:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b3c4f2bb-41e2-3c49-8874-424f66781a5b | -3.38646 | -53.23673 | 2025-01-27 04:50:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8e29509-60df-3829-b349-0bc4094b1f84 | -2.74383 | -54.14784 | 2025-01-27 04:50:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 315b8dd1-7483-3009-8ad0-235444b1b8a3 | -2.67819 | -52.17428 | 2025-01-27 04:50:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bac90314-04a0-3036-a00d-7e57a0551037 | 0.00208 | -50.50753 | 2025-01-27 04:50:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05bce308-9892-3149-a529-b66cd2087a7d | -17.30064 | -53.76843 | 2025-01-27 04:53:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 744fa0b7-fd76-3b09-82f8-cd0e09d1acd0 | -15.25103 | -60.22003 | 2025-01-27 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d46bda97-3988-3965-aa3b-708c956dee4f | -15.24206 | -60.22233 | 2025-01-27 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57c83012-3baa-3987-a271-46ab0a6ccc3e | -9.25974 | -60.31627 | 2025-01-27 04:53:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 61866d74-9bec-3528-974c-188eeeafac34 | -15.25172 | -60.21624 | 2025-01-27 04:53:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 259229c0-9b8f-36ee-ba38-27488dff8900 | -10.80475 | -45.17382 | 2025-01-27 04:53:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2986a653-4c5f-37fe-a056-2e630f99d4f2 | -5.23603 | -56.06235 | 2025-01-27 04:53:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b5f5020-4200-38bf-a467-efa810c4251e | -16.68326 | -43.88354 | 2025-01-27 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5a0aa544-4bdd-3b44-9d69-615fa6624fd2 | -9.22267 | -50.20133 | 2025-01-27 04:53:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 399e120b-89b1-321e-9c74-a8b75eba3314 | -11.1031 | -43.34145 | 2025-01-27 04:53:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
