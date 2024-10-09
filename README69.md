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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fc71f63b-eb36-3391-8bf1-fbd0efbe72b4 | -13.417 | -61.9169 | 2024-10-09 04:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 1a10c406-c1c3-34a0-b078-0037e24dec70 | -13.8764 | -44.5386 | 2024-10-09 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 02162383-b50d-3eab-bf2f-f6c2271c1f79 | -13.8963 | -44.5116 | 2024-10-09 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| db8be1a1-2f8d-313f-b9ae-f8d88bb72b8b | -13.9153 | -44.5317 | 2024-10-09 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 618fef9b-5944-3dfc-bd6f-72d87d4cea8e | -13.9158 | -44.5081 | 2024-10-09 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 50ac678b-e77e-30c0-9d06-2e98bdccc2b9 | -13.9343 | -44.5518 | 2024-10-09 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 57.5 |
| b2f8433c-3a84-3942-8b14-93278a2db6a9 | -13.9348 | -44.5282 | 2024-10-09 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 8a821ecb-1c66-365c-9270-1b9c45cd9d6e | -16.4184 | -55.9455 | 2024-10-09 04:06:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| 53f4d2ff-c50a-36ed-9d4e-9736f561a09b | -16.8241 | -57.438 | 2024-10-09 04:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.5 |
| b64177b9-6d26-3777-9ff9-f1ce63974cd4 | -16.8898 | -55.8039 | 2024-10-09 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 143.1 |
| f5c3a02c-d2bd-3493-8ef8-fd70141471de | -16.8901 | -55.7831 | 2024-10-09 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 1d1d2105-9f85-339f-a8e1-0221b9538b64 | -16.9091 | -55.8222 | 2024-10-09 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 86.3 |
| d2024131-277e-36dc-9e82-943ad54e18d4 | -16.9094 | -55.8014 | 2024-10-09 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 267.8 |
| a8d4284a-81a4-3ba7-a104-42fb3c5fd2f9 | -16.9098 | -55.7806 | 2024-10-09 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 169.9 |
| a755fe58-79b8-3e31-8d9c-68ba42157dcd | -16.929 | -55.7989 | 2024-10-09 04:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 108.7 |
| 168f25f4-344c-3168-90b7-e8ca579817e3 | -17.1467 | -56.8463 | 2024-10-09 04:06:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 64.5 |
| d3b3849c-0753-3b50-9f57-6c6a1ba85029 | -18.1193 | -56.3921 | 2024-10-09 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| e1e71c13-d6a8-3c3f-bbf6-aa857eccf7e1 | -18.1391 | -56.3895 | 2024-10-09 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.4 |
| fc1632b7-c70e-3679-a343-b8f3297cba53 | -18.1394 | -56.3686 | 2024-10-09 04:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.3 |
| 50a32d2b-20b5-354f-91d1-c4b583289837 | -18.5993 | -57.2629 | 2024-10-09 04:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 17435df9-72b5-3a1c-b8ca-b3ed60b8f6ca | -18.5996 | -57.2422 | 2024-10-09 04:06:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.6 |
| 52201866-1f5e-373c-bef2-965d78cbeec3 | -19.8131 | -45.6202 | 2024-10-09 04:06:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 53a74592-a05e-315c-b56e-7da7f54f4b94 | -20.103 | -55.9647 | 2024-10-09 04:06:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| 654b3315-8aff-3c86-b20f-544d2da39efb | -20.1035 | -55.9434 | 2024-10-09 04:06:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| 806c9a79-3622-3d61-bdcf-104af19af462 | -20.3551 | -48.7262 | 2024-10-09 04:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 237.8 |
| b8c1f2a0-0171-3bd4-9064-97595b988cf2 | -20.3346 | -48.7307 | 2024-10-09 04:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 192.1 |
| 0e2a1396-a67f-311a-9b8f-211fea196cb9 | -20.3352 | -48.7076 | 2024-10-09 04:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 108.4 |
| eb39b531-736a-3950-9103-50789610c0cb | -20.3557 | -48.7031 | 2024-10-09 04:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5132784f-3493-3c21-a961-9908e13c6938 | -21.1126 | -47.2229 | 2024-10-09 04:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f6862e73-9230-3638-8911-6d6730696abb | -21.2721 | -51.0513 | 2024-10-09 04:07:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.6 |
| 6cbcd9ef-1ac8-317a-95af-a0f0a87c014d | -21.2927 | -51.047 | 2024-10-09 04:07:04 | GOES-16 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 96.8 |
| 1f5ea9e9-1262-32a1-a2ff-e0465fd72a57 | -21.572 | -46.9898 | 2024-10-09 04:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 79c7e194-efb4-37f2-bc7e-cb7cf8a910e5 | -22.1369 | -48.1224 | 2024-10-09 04:07:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5ccd85f8-6455-313c-9e83-78dfb0b9bb92 | -22.8137 | -48.4225 | 2024-10-09 04:07:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 32ba9821-168a-3d24-b47f-d9d4b537b8df | -1.07965 | -46.57636 | 2024-10-09 04:12:00 | NOAA-21 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f92c668-67ee-3a83-a21e-847f3d89d8af | -0.71004 | -48.03858 | 2024-10-09 04:12:00 | NOAA-21 | SÃO CAETANO DE ODIVELAS | PARÁ | Brasil | 1507102 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98b57101-ffd1-3fbd-a187-d390c948498e | -9.3664 | -38.0427 | 2024-10-09 04:14:00 | NOAA-21 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 662ed79c-58a5-3490-baa6-be71d62ec644 | -10.12811 | -36.41247 | 2024-10-09 04:14:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 9.3 |
| f7e53dd7-c225-3a09-bb72-a7900511be75 | -7.30872 | -37.44259 | 2024-10-09 04:14:00 | NOAA-21 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9003d202-904a-37d8-9af6-a501d4292bb0 | -7.30815 | -37.44647 | 2024-10-09 04:14:00 | NOAA-21 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1ead6258-6af7-375b-8ea4-87f0412f4d01 | -7.30813 | -37.4448 | 2024-10-09 04:14:00 | NOAA-21 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7a0c94aa-c490-3765-af6d-7effa14e8b8a | -8.42578 | -36.97031 | 2024-10-09 04:14:00 | NOAA-21 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6a053275-9ef8-3c6d-af7c-f45d7942ca0d | -4.03968 | -38.25556 | 2024-10-09 04:14:00 | NOAA-21 | PINDORETAMA | CEARÁ | Brasil | 2310852 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2d10b37e-209b-304d-bcfa-350e2aea3edb | -4.72137 | -38.45741 | 2024-10-09 04:14:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 7db45000-9b90-395b-937e-bb9c86214825 | -5.84021 | -38.03001 | 2024-10-09 04:14:00 | NOAA-21 | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 432d78ed-646f-3c0e-992c-5bb4616aaa56 | -5.16532 | -38.09159 | 2024-10-09 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| a1697ce5-ac8a-361f-a71d-6d79b2a3c970 | -5.16632 | -38.08926 | 2024-10-09 04:14:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| dd8da928-6d02-3a4a-8cb6-1696fc361a34 | -4.85196 | -38.67192 | 2024-10-09 04:14:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1b685ba-efdf-3068-b770-898f34f9e8fc | -4.85538 | -38.67442 | 2024-10-09 04:14:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 144cf34e-a36a-37c0-a8c1-6373f22ab1bb | -3.43438 | -39.04569 | 2024-10-09 04:14:00 | NOAA-21 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc51f16f-6fc3-3728-ae1f-f59b625b7007 | -4.85575 | -38.67248 | 2024-10-09 04:14:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff1d189c-2881-36ea-935e-eb72f8aff9b5 | -4.85159 | -38.67385 | 2024-10-09 04:14:00 | NOAA-21 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe74c9f6-0e2d-3671-9f1d-00feaa14fff6 | -6.08457 | -39.21629 | 2024-10-09 04:14:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| afc996db-4328-3381-a4f3-58b8c837fd3d | -5.22967 | -39.93228 | 2024-10-09 04:14:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d15c3bbb-7b6d-3111-8970-0c27e2016f93 | -5.22612 | -39.93172 | 2024-10-09 04:14:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a4a89d20-1c13-31ed-8adf-a4d713c3f373 | -7.67082 | -39.62165 | 2024-10-09 04:14:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8816a7f5-586c-3ff3-a521-8003cf9d4a28 | -7.24341 | -39.18118 | 2024-10-09 04:14:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 510d3ab1-c39c-35ef-aa34-24f7ba273d56 | -7.22595 | -40.16874 | 2024-10-09 04:14:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2a41d4cb-bb98-3776-baab-1554dd6d6a87 | -9.16673 | -40.10831 | 2024-10-09 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6d74b625-4b31-3da4-b2a5-06e0b7316627 | -7.89574 | -40.71759 | 2024-10-09 04:14:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 41c67f92-c2d3-36fe-88e0-299f873a9062 | -8.10517 | -41.08745 | 2024-10-09 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 59fd73b4-f5c6-3e18-b53f-80504446fc34 | -8.10227 | -41.08307 | 2024-10-09 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d0bf80d3-3082-3961-a128-2e009bbfa4f3 | -8.09879 | -41.08256 | 2024-10-09 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 01fe50b4-bdfa-306b-a197-16e51b071956 | -4.0401 | -40.4031 | 2024-10-09 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ae8dc27-f83c-3583-9172-b14048df35b0 | -4.03783 | -40.39507 | 2024-10-09 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 362f4f27-c1ab-3685-9c74-63fc2bbf74ef | -4.03724 | -40.39882 | 2024-10-09 04:14:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17ad73b8-be28-37f0-abda-8fe56c66f7e3 | -6.29814 | -41.84595 | 2024-10-09 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 56470668-847d-3305-8406-946eabe2dbb9 | -6.30094 | -41.85 | 2024-10-09 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| bfadce31-4adf-30a1-854a-49d061a0908e | -6.2948 | -41.84543 | 2024-10-09 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| faf6b75d-e51c-3610-8798-d8ec968f56c3 | -6.2976 | -41.84948 | 2024-10-09 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f7fc63b9-f60e-300f-8498-e203384ad2de | -6.26428 | -41.88783 | 2024-10-09 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d747e020-d42f-3a57-975d-e511d29afdcf | -6.25923 | -41.87617 | 2024-10-09 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 23c7ff99-ddbf-35ee-8793-51c5c2c4473c | -5.18695 | -41.29121 | 2024-10-09 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 96eed345-30ad-348f-a69c-08acf9fdf453 | -7.35816 | -41.93945 | 2024-10-09 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8cc97458-97b3-377b-84a2-26a501965642 | -6.48475 | -41.95796 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 20ad7673-c18c-3991-9cfa-803b8f28127e | -6.48196 | -41.9539 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4dc90cd6-e15b-36e2-a5ce-6223e1840e84 | -6.48142 | -41.95742 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3374ae16-8b85-3ae5-b723-940023e875da | -6.47754 | -41.9604 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7089d385-b813-32a8-a666-4442dd125028 | -6.48421 | -41.96148 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d73b5e09-a75c-38d5-8c76-f0f6c9f19ba2 | -7.35971 | -42.19504 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6b283b9b-f192-399b-b684-352b8389a81b | -6.99844 | -42.11004 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 36a53b08-1def-3acd-8054-c406e11d1b56 | -6.48087 | -41.96095 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4879e522-b0f1-3076-8954-24bee1b72421 | -6.47808 | -41.95689 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9c8069a9-eb98-38d6-b096-04b1b5e6a1a0 | -7.36026 | -42.1915 | 2024-10-09 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e89bccec-7dae-3a30-beb9-7a0399e93742 | -6.69508 | -41.60254 | 2024-10-09 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 41273004-3b0f-3410-918a-4be0b56df8d8 | -6.47863 | -41.95335 | 2024-10-09 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 89c4788a-b278-3449-939f-f63bb5a5999b | -9.32491 | -42.20758 | 2024-10-09 04:14:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| becb4f0a-e8b8-304f-be3a-01b741aff5c5 | -8.42684 | -41.95132 | 2024-10-09 04:14:00 | NOAA-21 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1ab7215e-f153-3eca-9390-381ad34eb6b3 | -8.10169 | -41.08693 | 2024-10-09 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5f82f4ca-8bcb-35bb-9a2b-113796d4f58f | -9.32829 | -42.2081 | 2024-10-09 04:14:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6cdfccba-d81d-3487-a7d0-2b95032c92e3 | -8.23043 | -41.56008 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5a880124-4e42-36cd-8a90-5cc94504c15b | -8.09822 | -41.08641 | 2024-10-09 04:14:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1a2a2e80-a71d-30b7-827f-f3a7f1c0fd68 | -8.23099 | -41.55634 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 09f480b9-f802-36cf-8c04-59f4c5b7c7fd | -3.79713 | -41.60905 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6547bcc0-c763-386b-9b29-b37e4fed4a4e | -3.32842 | -42.86134 | 2024-10-09 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fdaf9da7-c114-3f15-95f5-4eab8ec79776 | -3.32788 | -42.86478 | 2024-10-09 04:14:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a22c59ec-a84b-3002-bed2-a00922cbbe40 | -4.24715 | -41.93227 | 2024-10-09 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cd9da80b-5ad4-3e07-8d69-83294d1ad95d | -4.73995 | -42.6306 | 2024-10-09 04:14:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 085df263-8f31-30c1-b807-1540b6bad13a | -3.81869 | -41.60166 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6ff62667-f0ce-31b8-a25a-2aaf5d920de9 | -3.81537 | -41.60115 | 2024-10-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |


[Clique aqui para ver as próximas entradas](README70.md)
