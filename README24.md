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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccd9fccf-f1e0-3336-8198-15b959e5e7a5 | -9.415 | -57.03128 | 2025-09-20 04:55:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac94c7cd-58fd-3433-a436-aee14d9e55b8 | -13.07767 | -42.14413 | 2025-09-20 04:55:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbf8de7a-c128-343a-82ed-ece0ea659e52 | -15.28677 | -56.81694 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e277114-4170-37c3-a260-c423d10b5e5d | -12.89861 | -46.79104 | 2025-09-20 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d374d80c-1b1f-3980-8123-98190e296e0f | -15.27723 | -56.83136 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e20b7237-add7-39f0-b97a-7d4c7b4af61c | -9.39849 | -54.69277 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18d01e55-8c1c-34e3-bab0-2ec12a79e938 | -10.32825 | -45.23962 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| db366d71-b653-34fd-874e-59f6a444c9ee | -13.22646 | -57.12922 | 2025-09-20 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 625fcb95-f680-3ba3-a837-90b0302f2d0d | -9.39452 | -54.69583 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74370a5a-54ee-383b-9ae5-208e3265a6c2 | -12.08705 | -44.8479 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 24c481cb-5351-387f-99d8-f46d9058e3e1 | -9.5302 | -63.57882 | 2025-09-20 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d2c482fc-4533-34ab-94d4-9e1e4d917136 | -12.39768 | -43.8191 | 2025-09-20 04:55:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17502aeb-b98d-386e-be56-1752ae3b48ad | -12.07681 | -44.84353 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5428196-f627-3ca7-9b6f-291f989e4ade | -9.9025 | -59.60232 | 2025-09-20 04:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 577b528b-1ded-3054-badb-e382594fbf6f | -9.01319 | -48.01825 | 2025-09-20 04:55:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbe7dd1a-6fc9-3b3c-99d3-d73b4b88d726 | -9.74906 | -53.91861 | 2025-09-20 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b127c962-07ae-3b7a-8377-cbde28137bd7 | -12.36419 | -60.77827 | 2025-09-20 04:55:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aceb3c4-9f40-32a4-b7b4-2c3cb4cedab0 | -12.85409 | -52.99853 | 2025-09-20 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b4079132-b329-3658-bd32-ee287e595d6a | -10.88093 | -53.75127 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a212ab1c-0c3b-33e1-af36-07d354e969af | -10.23236 | -45.00425 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9909d3e4-a348-3849-9da9-9fe77ebd551d | -15.27243 | -56.83865 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b71b092c-2314-3a32-9098-8a5dd30455b0 | -15.29108 | -56.83375 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46aa5313-922e-3fc0-b725-9078a9dc0402 | -15.27525 | -56.84312 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9501a7e1-e562-34fb-96eb-151b540d3cd9 | -9.73799 | -53.88073 | 2025-09-20 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea4afc05-456a-3c0a-8996-d5588ef0aed2 | -10.11524 | -44.75558 | 2025-09-20 04:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b03abb60-449b-3bac-aaa9-da9ebf1f534c | -10.33406 | -45.23449 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 897d1829-3a66-3dba-9a87-9a9421f9a744 | -15.31854 | -56.8187 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b059497-acfb-3aaf-985a-a694e6511ece | -9.39907 | -54.68914 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee3b0d42-aebe-3a29-b9c5-af282031fd45 | -15.31228 | -56.81353 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 690b8c16-5ad1-3efe-92d4-19b127c1f95e | -9.39569 | -54.68859 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd7ba44f-be06-348a-b4f7-7a307247e5a8 | -8.17048 | -55.17507 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c52542b-81c9-3372-9415-631390fffbbc | -9.35941 | -54.52675 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d89e6fa2-8cb7-3f23-b8a4-e906d13faafd | -9.40981 | -54.68716 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 851c9ef3-c168-3512-b7a0-abd236e2bf49 | -9.40246 | -54.6897 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 04cb0d34-5484-338c-b2a2-61c738f42f7a | -14.58633 | -56.92179 | 2025-09-20 04:55:00 | NPP-375D | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7915dae2-e610-36f3-9989-a46c57c90a8f | -12.07964 | -44.82098 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e39aef8-b65a-3f0f-abd2-1a30ea041ab4 | -10.23438 | -48.05456 | 2025-09-20 04:55:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cecf8201-982d-3003-9381-cdb3d6e7b8fa | -10.32529 | -45.26188 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f652d4d-69a0-3144-bd8e-ebf538ce37f4 | -12.12475 | -59.882 | 2025-09-20 04:55:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9c9915c-7f8a-30eb-ab7a-4a1a03f4f90e | -12.08664 | -44.8511 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fe51a47c-9904-3034-9d8b-07ca21fe856a | -12.07765 | -44.83686 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0ddc414-3e1a-3c5d-88a0-96189a9ea137 | -11.28223 | -47.41254 | 2025-09-20 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68383074-b87c-38d8-9f02-c3fceef95222 | -8.92493 | -54.44918 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e142000-2225-35b4-b688-93db83ecfec2 | -9.40643 | -54.68661 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df300a4b-24fd-3431-ac38-ab4a8a613a25 | -9.41039 | -54.68353 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 278e18cf-a999-3994-8869-495316acabc9 | -9.41245 | -63.69766 | 2025-09-20 04:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05670dcc-ff6d-37bf-a34c-036a988ae996 | -12.07358 | -44.82624 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b7588a98-e2df-3fb6-9be0-55127d88df76 | -12.07397 | -44.82314 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 87897b6e-c8b3-3894-81e4-1ebd45d6db86 | -12.85801 | -52.99545 | 2025-09-20 04:55:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0af81263-08b3-38d0-a9ff-e5d7df14102e | -8.92155 | -54.44862 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72bbffe4-b521-366d-9a33-071cd28e2777 | -9.40584 | -54.69025 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1d70f8a-fccd-351d-8e53-017d603b8ee8 | -11.28662 | -47.41324 | 2025-09-20 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b51f25e6-211f-35b6-ab13-bac09130e6ed | -10.88205 | -53.74423 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46d3c550-8634-3be8-9ce3-b2beccaace42 | -11.64277 | -52.86432 | 2025-09-20 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6a6e078-5558-330b-8408-b3ed310453d6 | -10.88149 | -53.74775 | 2025-09-20 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f05420c2-5091-3ae6-9eff-0f973ffbdc84 | -12.08211 | -44.84428 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8576ef7b-e48e-3dd8-998c-0ca84f4f1385 | -9.40701 | -54.68299 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd8f083a-5dc9-34a9-9d95-87d289072a94 | -9.39394 | -54.69946 | 2025-09-20 04:55:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c46afdba-37e1-3580-9f87-e2651925cdf5 | -10.34203 | -45.25163 | 2025-09-20 04:55:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2082913f-0129-3b3e-9bb1-4b8f4717915c | -12.89058 | -62.12804 | 2025-09-20 04:55:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5471d175-cde9-31e2-96f6-cf3cf83feb57 | -10.87591 | -45.43316 | 2025-09-20 04:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b04ed4e5-7b2a-3c52-88ac-178a23f8b71f | -9.46958 | -54.45226 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba27baa-bb94-3e96-9a48-de2356b9668c | -9.41319 | -63.69375 | 2025-09-20 04:55:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe05c7c7-efcc-3999-8742-2510ba0464c9 | -8.93727 | -54.45852 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 251026a9-aa87-3221-a0ed-c5792c235773 | -9.18408 | -62.61634 | 2025-09-20 04:55:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc5fe231-0ea4-32bf-92b3-fda4246231e3 | -10.03044 | -59.35421 | 2025-09-20 04:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf9ce5da-0966-3ac5-92a2-8685c4044af0 | -14.43679 | -46.51501 | 2025-09-20 04:55:00 | NPP-375D | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba4ee6ef-dfd9-3c1d-aa51-e63973f5c334 | -12.08538 | -44.81826 | 2025-09-20 04:55:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 737f4a58-f34e-358a-9e27-516c3b8dd6f3 | -10.02974 | -59.35826 | 2025-09-20 04:55:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45d9607f-af3d-3fbe-b27a-155589e86b1d | -9.48256 | -54.43602 | 2025-09-20 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 525773bf-e41a-3365-b223-edc78b02056c | -13.22716 | -57.12505 | 2025-09-20 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3cbab52-fc9f-34b0-987f-50c9f6f30fcc | -15.2774 | -56.85156 | 2025-09-20 04:55:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cd7def2f-357d-3b9a-8dac-6b826a98ba1b | -10.11571 | -44.75544 | 2025-09-20 04:55:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99f59533-8665-31c7-974f-9c121f796713 | -19.54734 | -48.0431 | 2025-09-20 04:57:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e227469-29e7-3942-b6b6-1544e0f20e17 | -21.28902 | -55.91481 | 2025-09-20 04:57:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef43ee4c-48eb-39ca-84d5-a5964d716b0f | -19.61474 | -57.74182 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| bd871011-df4c-3925-9df7-f7664544fd10 | -18.32933 | -55.04819 | 2025-09-20 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 37a93e66-2fb2-31c4-939d-750ccf818062 | -20.33119 | -49.20336 | 2025-09-20 04:57:00 | NPP-375D | ICÉM | SÃO PAULO | Brasil | 3519808 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bb7bdd8-e7a5-3ffc-a14b-d7b1546f1cd2 | -23.27747 | -46.40079 | 2025-09-20 04:57:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c13edcc2-d4a5-369c-afbc-48a712e4868f | -18.3299 | -55.04453 | 2025-09-20 04:57:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 17aacf77-96da-3ac1-aaf7-89652cfc939c | -22.63898 | -44.52226 | 2025-09-20 04:57:00 | NPP-375D | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| eb830746-45d2-3862-800e-e72b97e3d12e | -20.50041 | -56.86957 | 2025-09-20 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de91dfe4-1be8-32d8-9d3c-240a150e2554 | -22.18269 | -55.99428 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 304c7dc6-d967-3eb0-89b2-ccd30d4c94a4 | -23.48188 | -52.18723 | 2025-09-20 04:57:00 | NPP-375D | PAIÇANDU | PARANÁ | Brasil | 4117503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f95b695a-35e5-3942-accb-3d1e6ddddde8 | -23.81634 | -47.58097 | 2025-09-20 04:57:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 60fd9033-556b-3df8-a3d3-716054ebd107 | -22.61824 | -54.94691 | 2025-09-20 04:57:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da9acefb-e231-3a1b-955b-50fe5d15fc4b | -23.74428 | -47.82157 | 2025-09-20 04:57:00 | NPP-375D | SARAPUÍ | SÃO PAULO | Brasil | 3551108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c3b5f66b-6642-32d4-963f-3e7e37796aa6 | -19.61408 | -57.74577 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 41092cf2-8501-355c-8710-018c309a7028 | -19.07917 | -48.14889 | 2025-09-20 04:57:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63f93617-a168-31a2-923a-d95628d0c24a | -15.92135 | -59.45291 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 58706bd0-8187-39cd-a224-90c24b4dfee5 | -20.35153 | -48.78214 | 2025-09-20 04:57:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 548f37c5-850e-30f8-a14b-d7463b1bf8fc | -18.03814 | -50.94566 | 2025-09-20 04:57:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a07acdd-fca2-347e-ba4f-e04586cb0445 | -22.61767 | -54.95081 | 2025-09-20 04:57:00 | NPP-375D | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d12af036-06eb-39b0-911c-b129df248af4 | -22.19399 | -49.64905 | 2025-09-20 04:57:00 | NPP-375D | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc25a5e7-ab9e-3272-be5c-e4b73bd2eec8 | -21.29258 | -54.79787 | 2025-09-20 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f216c1e9-5a0f-3a6e-9790-6cc9cdc3be17 | -15.34318 | -59.40469 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6218ce00-d4db-323d-b79e-9e82a59e840b | -19.61064 | -57.74512 | 2025-09-20 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 3fc7591e-630c-32a0-a67a-833e285d7578 | -20.6046 | -56.72636 | 2025-09-20 04:57:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35fe6068-e66c-3246-8294-0471d31cbcbd | -22.21437 | -56.19932 | 2025-09-20 04:57:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5184eb64-f383-3130-a3c9-f13fffa155b0 | -15.91746 | -59.45213 | 2025-09-20 04:57:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README25.md)
