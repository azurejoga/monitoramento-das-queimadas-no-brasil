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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74ff899f-d657-3afb-a329-4e223dcac751 | -20.33271 | -57.8371 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.8 |
| 2f5f656f-5035-390b-a3b0-de8252bbcf66 | -19.64681 | -57.27222 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.5 |
| 07bd3624-8d76-32a4-a757-531b40a618b8 | -19.64265 | -57.28012 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.3 |
| d1700a60-b1bd-313d-9290-f24e8b5ebe75 | -19.62612 | -57.28401 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 39.9 |
| e3eb5bc8-980e-37fd-994b-b228abd5e455 | -19.61836 | -57.24518 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.1 |
| 633644c3-67ca-3610-84d9-d14104a19627 | -19.63495 | -57.24128 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 190.5 |
| 8ed3f941-5e51-3fb3-b512-96f060329726 | -19.63886 | -57.23342 | 2026-01-25 01:45:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| 1ff7a020-4beb-3c4c-a7ce-3b8a77d0e2a8 | -18.8111 | -57.6493 | 2026-01-25 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.0 |
| 5b331b02-4243-3686-842a-30c9665e21ab | -18.7912 | -57.6519 | 2026-01-25 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.3 |
| 8afa0a8f-d517-3ccb-9312-d9a4d35aee78 | -19.6364 | -57.2499 | 2026-01-25 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.4 |
| 8d388c11-2c86-33a4-92fa-bd06202c790a | -19.6163 | -57.2526 | 2026-01-25 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.0 |
| 375e329b-d1c4-3faa-ad3e-22d62c771bb8 | -18.7912 | -57.6519 | 2026-01-25 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 185.5 |
| bd3884a4-500b-3f8c-912a-fb87f4b68977 | -19.6364 | -57.2499 | 2026-01-25 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 42cf6d1a-7ce0-310f-9545-171bc7e54878 | -19.6163 | -57.2526 | 2026-01-25 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.7 |
| e24325ff-7931-31ac-88d3-0d1b601a9225 | -18.7908 | -57.6726 | 2026-01-25 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.6 |
| 436411ed-f46d-3e57-9b46-5799778e5f2b | -19.6368 | -57.229 | 2026-01-25 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.5 |
| edae17a0-90c3-3709-a8cc-58bd932afda1 | -18.8111 | -57.6493 | 2026-01-25 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.1 |
| 1520a9dc-e693-301d-ba0c-cbcbdea908c4 | -19.6368 | -57.229 | 2026-01-25 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| bdec9454-84dd-3414-aead-c064aeaa731a | -18.7912 | -57.6519 | 2026-01-25 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.2 |
| 76c25def-faf4-3596-bf35-b4e093815f03 | -18.8111 | -57.6493 | 2026-01-25 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 611d9d23-c107-3f5d-970b-2d6a9b1c7011 | -3.0791 | -40.1063 | 2026-01-25 02:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 79.0 |
| 25430a72-cb4a-3ad1-9132-93404ff3c298 | -19.6364 | -57.2499 | 2026-01-25 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 175.0 |
| a80920db-6601-373a-a663-fdd32da6a6d9 | -19.616 | -57.2735 | 2026-01-25 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 811d3c5b-0c37-3719-adcc-20e37550b76c | -19.6163 | -57.2526 | 2026-01-25 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.1 |
| 91838d13-0c47-3ea2-b344-6b4a33ee45bb | -19.636 | -57.2708 | 2026-01-25 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.6 |
| 9691c3e1-992d-3311-b72a-ae27a8302dfe | -19.6364 | -57.2499 | 2026-01-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 246.4 |
| 2f427ac2-b8e5-3718-bfc9-d3c6f1ceac7d | -3.0791 | -40.1063 | 2026-01-25 02:20:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 3d3c3828-a67e-39ef-9496-9281075efac0 | -19.6368 | -57.229 | 2026-01-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 45.5 |
| 04fa0292-7ef0-39f3-80b2-52ae638abbd8 | -19.616 | -57.2735 | 2026-01-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| beac2d82-b379-360d-9a38-24cddf7a1d57 | -18.7912 | -57.6519 | 2026-01-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.3 |
| 638c4202-bedd-339b-a9da-0ca30190c70c | -19.6163 | -57.2526 | 2026-01-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 171.6 |
| 7f5b3c37-7f2e-3842-bc78-df978df19936 | -19.636 | -57.2708 | 2026-01-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.0 |
| 5cbb276e-dd52-39f4-95ae-6c470912b23d | -19.6167 | -57.2317 | 2026-01-25 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.9 |
| 9349d5e5-49c9-363a-8929-022d688dec90 | -19.6163 | -57.2526 | 2026-01-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 141.6 |
| f6db871a-45df-3242-83fe-b79e5f618614 | -19.636 | -57.2708 | 2026-01-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.1 |
| ca5def9b-effb-3a7f-9916-068dbdde59cd | -18.7912 | -57.6519 | 2026-01-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.6 |
| d3217454-2eae-3001-a27c-07c5fdb9b04c | -19.6364 | -57.2499 | 2026-01-25 02:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 130.1 |
| 904c5ab3-c288-34d6-89fb-e9d81a9c9768 | -19.6561 | -57.2681 | 2026-01-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.7 |
| e949d55c-4e60-389a-a619-32aed550b4b9 | -3.0791 | -40.1063 | 2026-01-25 02:40:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 335f38a5-5d66-3af9-9ae8-c95c59004499 | -19.6565 | -57.2472 | 2026-01-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.3 |
| 8c7c7e26-559f-3535-96ad-f0634fa4652c | -19.6163 | -57.2526 | 2026-01-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 57df3a16-c8db-3237-b350-d7ed769375be | -19.6364 | -57.2499 | 2026-01-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 227.8 |
| 87483111-45bc-3026-a6a2-7d8046f190f1 | -19.616 | -57.2735 | 2026-01-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.7 |
| c5aa7e1c-6391-3327-ba10-9a04ad440aaf | -19.636 | -57.2708 | 2026-01-25 02:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.7 |
| 407004fa-94e0-3bc1-9d28-99279f874077 | -3.0791 | -40.1063 | 2026-01-25 02:50:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 1da2b3fa-9209-30f6-b8a0-141402f9d3de | -19.616 | -57.2735 | 2026-01-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 133.0 |
| 3a0ecda0-6304-3730-9f0b-1f6cae87205f | -19.6561 | -57.2681 | 2026-01-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| eee858d6-823e-3a4c-b55b-870f7ad47145 | -19.636 | -57.2708 | 2026-01-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 224.6 |
| ada42fed-8a2b-3750-a74b-f2c82d127a9b | -19.6565 | -57.2472 | 2026-01-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.6 |
| 008eae63-af78-32a8-abf7-cd72e51b6c35 | -19.6163 | -57.2526 | 2026-01-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.4 |
| 282f47ad-f182-37d6-8dc1-4498d94f188c | -19.6364 | -57.2499 | 2026-01-25 03:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 233.0 |
| 2780d7cd-8778-34cc-9392-17ac9f494e36 | -4.65698 | -37.92768 | 2026-01-25 03:04:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2360577b-ade4-32d3-93a7-936ead90a59b | -9.60936 | -35.9082 | 2026-01-25 03:06:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83e122cd-f130-3cdf-8cc4-2b9d6047183b | -9.61006 | -35.90446 | 2026-01-25 03:06:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b3d28fb0-ad8f-3b07-a1f6-521f813a3b02 | -6.1999 | -39.28838 | 2026-01-25 03:06:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 49b43622-bbb6-3f92-827a-a58da69916c0 | -6.2012 | -39.28142 | 2026-01-25 03:06:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 074e458d-fd7b-3999-90b8-ec3eb8ecb272 | -5.56909 | -39.11927 | 2026-01-25 03:06:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| abf72792-3357-3e95-898d-91d0f3bec424 | -19.636 | -57.2708 | 2026-01-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.4 |
| 1102e930-b51f-3d5f-a6c5-38bc9eb96213 | -3.0603 | -40.1072 | 2026-01-25 03:10:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 104e89d5-0204-3d77-9e13-ca12265b5322 | -19.6565 | -57.2472 | 2026-01-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 521c27aa-682a-3edd-a4a8-03a8b3f491c3 | -19.6364 | -57.2499 | 2026-01-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.7 |
| 95df1064-d751-3e41-834f-3516f1544123 | -19.6163 | -57.2526 | 2026-01-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 2dccf03e-d78b-3ecd-8535-ff63f2b350d3 | -19.616 | -57.2735 | 2026-01-25 03:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.2 |
| 6bb140c5-1911-3f88-b3c3-d2df6c638961 | -19.6565 | -57.2472 | 2026-01-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| 88cbb310-bda7-39f6-b4ac-525c1f82be5f | -19.616 | -57.2735 | 2026-01-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 211.5 |
| e229bfcc-4b5d-3c4b-8f89-76f59ce84e1c | -19.636 | -57.2708 | 2026-01-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 347.5 |
| 75671375-a8ed-3225-8a49-8cc49ec00864 | -19.6163 | -57.2526 | 2026-01-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 171.2 |
| 279d4b11-13b2-37b0-9c9a-7579b236013d | -19.6561 | -57.2681 | 2026-01-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.5 |
| c1339220-391c-3457-bcc0-437e6d7e6cf7 | -19.6364 | -57.2499 | 2026-01-25 03:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 235.8 |
| 71fbbb84-86e2-386b-8a35-8ab27ebfdf2f | -19.6364 | -57.2499 | 2026-01-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 217.4 |
| 577c8408-0549-3a1e-8d10-82888f7c8217 | -19.616 | -57.2735 | 2026-01-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 197.3 |
| 42e245d2-12ab-3a38-b9f1-ae5bb132b18b | -19.6163 | -57.2526 | 2026-01-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 135.4 |
| 3cc3dc02-708a-3aa5-ad61-e16171094131 | -3.0791 | -40.1063 | 2026-01-25 03:30:00 | GOES-19 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 72.8 |
| 3dfeb2c6-656d-3e2d-b9ce-90d3ef8af9bc | -19.6565 | -57.2472 | 2026-01-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.7 |
| c2d1b84c-da76-32e5-b13e-7394c7defdc6 | -19.636 | -57.2708 | 2026-01-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 356.2 |
| bb1ef816-cd7f-3c4e-ac9c-19a2b8ea9f34 | -19.6561 | -57.2681 | 2026-01-25 03:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| e1c0e1e9-e61e-36bd-a2c4-8d0567a7d6a1 | -5.54068 | -37.68817 | 2026-01-25 03:34:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| ffbf0d25-9208-3cc4-b6c3-5a6ab717de53 | -5.48007 | -37.66688 | 2026-01-25 03:34:00 | NPP-375D | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d39501d2-3bb1-3fb8-94de-35184be58c09 | -3.06888 | -40.11544 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3d531f13-98c8-3264-9454-2243e5e3d677 | -3.06472 | -40.10814 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c9baef6b-9c55-3c65-a901-35318ba2af91 | -6.2254 | -35.52496 | 2026-01-25 03:34:00 | NPP-375D | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c1bdf14b-5341-3a66-8e72-5f44548e386f | -3.07514 | -40.10994 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7979ed5a-3b2a-3b93-ad42-4cc2811394ec | -3.06368 | -40.11447 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| e36d502f-b6a4-35b1-91b4-cac6becea009 | -3.07045 | -40.10587 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 1454697c-58fe-3b35-ad8f-369966fbd65b | -5.35321 | -40.60217 | 2026-01-25 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 706a7960-b69c-34de-8cd9-c41c9a04b1dc | -5.35841 | -40.60307 | 2026-01-25 03:34:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c5af1ea-8059-3824-bd5a-0c342f6ea56a | -3.06941 | -40.11219 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c1c49672-a79c-399a-a8d1-ced3449a44bc | -5.5706 | -39.11989 | 2026-01-25 03:34:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| a1bebebd-36f6-30fb-8bdf-6116137a99dd | -5.55663 | -39.54945 | 2026-01-25 03:34:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c5fb00d-0216-373d-ad39-0931eaec7887 | -6.22625 | -35.52682 | 2026-01-25 03:34:00 | NPP-375D | SERRINHA | RIO GRANDE DO NORTE | Brasil | 2413508 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a7ada2b-4aba-3f26-b761-2c033c36df8c | -4.69108 | -38.16279 | 2026-01-25 03:34:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 625666a9-4266-31fc-a51a-2ce50158e793 | -5.56593 | -39.1191 | 2026-01-25 03:34:00 | NPP-375D | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| e2560f46-2677-338f-b4e1-79231df80661 | -3.0642 | -40.11127 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| ae35da83-f48f-362c-a46f-83689a3e43cb | -3.06993 | -40.10902 | 2026-01-25 03:34:00 | NPP-375D | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 9845a06d-0fd5-3778-a62e-cf6fdf6f3647 | -5.66434 | -37.85556 | 2026-01-25 03:34:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 674c6d14-669f-3048-a6ad-b3203c0ccd6e | -6.20361 | -39.28216 | 2026-01-25 03:36:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 70381239-8034-3c44-b7a5-75b197973e6a | -7.58484 | -37.63416 | 2026-01-25 03:36:00 | NPP-375D | SOLIDÃO | PERNAMBUCO | Brasil | 2614402 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f0349c02-cecc-376d-b83c-84cc65c1ebcd | -11.55553 | -37.97609 | 2026-01-25 03:36:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3b5c6348-1ad2-3d56-af49-2bca611d5ea6 | -10.11362 | -36.9968 | 2026-01-25 03:36:00 | NPP-375D | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 306bdf4d-572a-3eb3-a287-90960d4efac3 | -6.20275 | -39.2872 | 2026-01-25 03:36:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |


[Clique aqui para ver as próximas entradas](README3.md)
