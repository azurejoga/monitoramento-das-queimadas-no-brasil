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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a1082ee-ffe4-387d-aed8-f06f23bff71c | -4.22377 | -47.21855 | 2025-08-13 05:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b50b52e9-f87c-38aa-ad1a-6ab621379f65 | -2.90422 | -48.25555 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| bc001d20-78f1-30d9-8b97-69c3993a3d68 | -3.70851 | -49.0767 | 2025-08-13 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48f37846-7633-3518-8e19-01d1c37350e9 | -3.07368 | -52.28367 | 2025-08-13 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea8cbbbb-0dd2-3007-bd95-2f2bd9033aa4 | -3.58246 | -47.52621 | 2025-08-13 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ff75e61-7352-3b22-8aab-4e8cde706530 | -3.5817 | -47.53129 | 2025-08-13 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e00c89f5-3a12-33be-80b9-8cc061aab6f4 | -4.22542 | -47.21535 | 2025-08-13 05:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ee5c6b4-bce4-34a8-9373-f6df08029b7e | -2.90814 | -48.25395 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| cc415920-2e3f-3899-aa5b-3d58368c93fd | -3.83716 | -47.74683 | 2025-08-13 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 600462db-9533-3fe6-a9b5-14c6a88f17db | -3.43186 | -49.04557 | 2025-08-13 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40556f7c-a6c1-3a61-bc30-9f75a15b1c36 | -4.22461 | -47.21292 | 2025-08-13 05:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fef361d-e673-3151-851a-9bf2d0a1d9d1 | -4.06579 | -47.97781 | 2025-08-13 05:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5068163-2458-3b34-80bd-f87bd8113879 | -2.58496 | -51.9234 | 2025-08-13 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a2ebc71-52b9-397d-af60-23a2bfb3af43 | -3.43618 | -49.0462 | 2025-08-13 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8b0a5d1-ed61-3dee-9011-90e1dda67d94 | -3.83242 | -47.74606 | 2025-08-13 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c365f3b2-9865-30ab-bb52-e0a95dc428b6 | 2.89644 | -60.29216 | 2025-08-13 05:04:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2be1aec7-4d68-394d-bfe0-425a15336992 | -2.91006 | -48.24731 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f29bb370-7ca7-310e-8dad-5f717d295f2e | -2.58853 | -51.92396 | 2025-08-13 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 142c63e4-fe55-3328-885f-3abdf6afff05 | -2.90555 | -48.2466 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 4c720195-95b1-357a-b6f4-96e3f6126a1b | -2.90954 | -48.245 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 59bf2f8e-6ef6-3dc9-b46f-23ceb71bc618 | -3.08371 | -48.8528 | 2025-08-13 05:04:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef733478-1cbb-319f-8b99-469687c221d8 | -3.70913 | -49.07262 | 2025-08-13 05:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3ebda1f-4a65-3fa4-9fad-759ffd8c002d | -2.9094 | -48.25181 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4cf5dce4-9c72-3a4b-b7d1-36432860a0e8 | -3.83706 | -47.74577 | 2025-08-13 05:04:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 050b2d34-4831-3139-ab05-5d55507de7dd | -2.89982 | -48.24806 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e7523ee-b23c-31b1-8bf6-fa35876d0308 | -2.90433 | -48.24878 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 3450402e-9125-3101-b2e8-90512f1bf381 | -3.43247 | -49.04144 | 2025-08-13 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d829fc14-a7a4-3bd4-8b82-b7b8c5b44d6b | -3.43678 | -49.0421 | 2025-08-13 05:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b0160168-5847-3748-99a3-56c0ae00d3c7 | -2.89913 | -48.25253 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffccff84-4a00-3620-8dc8-173602c71b03 | -2.90363 | -48.25323 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 788f17ce-5ab4-3595-ad48-344a671a0066 | -2.90038 | -48.25037 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| bbe837f4-5f19-37c7-ab8e-4b55014504d9 | -2.90884 | -48.24949 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 1e7a2346-92aa-3a37-bc29-97ccce1ae03f | -2.90489 | -48.25109 | 2025-08-13 05:04:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 4546a836-ada9-3e2b-b1a4-6150a351b9cd | -8.11128 | -55.57272 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b40d6fe9-1959-3766-ad87-267626bea17b | -8.31682 | -55.10684 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bda8b33f-83c4-3744-8e32-5b9891153da2 | -6.88267 | -59.13335 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e5b32ba2-082b-35f7-9b8f-f0099943ebd3 | -6.2797 | -53.64102 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3689a663-9bf2-39d6-a3c0-168de168db46 | -7.45459 | -60.6347 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 68bec61a-f3a2-3fd7-b360-ceacb73f24da | -7.07742 | -59.19709 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc39d2b4-edee-31b4-a985-cb6f9e3a93ac | -10.34424 | -50.82784 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9d76d4e-1ea3-361c-b6d6-5fc1323d375b | -7.1311 | -60.12881 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| c7daa45f-6567-33a4-b3a3-531844ab9b1f | -6.88493 | -59.14251 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ca1f8a61-9afc-35b1-a8e6-44caea9132b8 | -5.66541 | -51.36499 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 279fabca-09be-3e57-b532-ebdf094dac8f | -6.87185 | -59.15346 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 3e36ceea-e380-3060-b226-c1cbc29f79bf | -8.11516 | -55.56975 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e789177-6c60-3500-8df5-85740273dd1b | -8.11238 | -55.56572 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d14a9887-2ee8-3007-9723-53bc41a261be | -6.91263 | -59.13391 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 49f24b14-e688-314a-b3fe-76b2587aaf72 | -5.73607 | -51.67035 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ff38dec-52b1-3996-bc55-79d1690ffbc5 | -7.27196 | -60.6259 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f7352a00-1540-35b1-b76c-4f4a27d96ddc | -6.89069 | -59.13026 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b3010222-5241-3923-8ea8-f579d40cc824 | -6.90532 | -59.13271 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |
| d9568720-6684-3fba-a5f2-d167c17dbf43 | -6.88423 | -59.14677 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 4d49685e-9668-3bc0-a8ee-fe10608af211 | -6.91333 | -59.12962 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 48fe2a67-7f1e-380a-8499-20f823fd33e8 | -6.89505 | -59.12656 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e7f56fe1-ed08-3efc-a76e-52c287840919 | -7.13657 | -60.11983 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3482eb3a-862e-38c5-b943-8a36d3e31dc2 | -8.56967 | -54.69401 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6488a4fd-1009-31d1-918a-2fd2a623910e | -7.09647 | -60.02962 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d830b85e-f70a-3720-9b08-4563093290d2 | -6.97028 | -59.283 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6cfa409-8b6e-3a3c-b630-3516c6d93f6c | -7.2594 | -57.63646 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ea8c78a-01f5-33a3-ac83-52b3f34c8b7c | -8.11293 | -55.56223 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e621ea84-18d2-3089-aa78-50bb578f4a7b | -9.36579 | -47.62909 | 2025-08-13 05:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3247afe5-6a65-3bd5-b3eb-6d27337360ce | -7.25397 | -59.99551 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a41bc388-ac5a-3b15-9f80-0a2d51804392 | -9.71323 | -49.4802 | 2025-08-13 05:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a2de55a6-89d4-3614-8a98-d4e22f7ed8f4 | -5.84365 | -59.92075 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3172c186-d3eb-3e59-ac66-46cb9a8a1f4b | -7.12885 | -60.1186 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80bb423c-6ea0-3fc9-a2a9-d8daf997d3f3 | -5.44449 | -45.1021 | 2025-08-13 05:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c1d2d19-b3cb-3113-80c7-1bcdda305fd9 | -5.73337 | -51.68853 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8ea40208-502c-3bfa-be63-25296d704ab8 | -8.56344 | -54.6669 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 122aae4a-162d-3d07-a3f9-c9e9fd5196b5 | -5.84284 | -59.92559 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a8d73b7-ed07-39e2-a815-31b919b99364 | -8.56683 | -54.66743 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a9a679d-4a8f-372b-b9d9-457c96975799 | -9.71387 | -49.47548 | 2025-08-13 05:06:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b40f34b4-e0ba-3c83-9cfe-d1121a9863f5 | -4.95401 | -47.60033 | 2025-08-13 05:06:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 88529341-74df-32c8-85b3-9e32e14e89af | -6.10799 | -59.91915 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 629c17e6-edde-3449-a645-0e8c98afa42a | -7.08859 | -60.02071 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0afbee6b-4473-37e7-b6b1-2c22e9b814e4 | -7.08475 | -60.02011 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eeb62e7c-96e6-377a-843a-66ed6f325527 | -10.34112 | -50.81934 | 2025-08-13 05:06:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c3c079e-8c0a-3821-a4dc-4d5068d47214 | -7.14348 | -60.12594 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 02df343a-cb18-3267-87b5-772b8e4d52ce | -6.09398 | -59.93182 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 76be3764-9458-3b06-9535-744c955ca725 | -7.81911 | -61.32877 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27937076-de63-3294-8af5-60ad88577c36 | -6.97099 | -59.27869 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5118b2e5-b5ac-3d54-90c5-aa9b26f5231f | -6.88633 | -59.13396 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ba91a29b-7d04-3448-a5ca-3c507d3e9b3c | -7.48357 | -43.93284 | 2025-08-13 05:06:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81bfc911-c975-384b-888c-8cccc89e292c | -7.48501 | -48.38111 | 2025-08-13 05:06:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2af782f0-f261-3258-a639-7f4adb37c1af | -5.8506 | -59.92688 | 2025-08-13 05:06:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebd92177-9112-3c19-865d-f24c45756e80 | -6.92563 | -59.14314 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 917e50d3-6c5b-3568-b411-68d733ccc9c3 | -6.87326 | -59.1449 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e04339a-bc06-35db-972a-a5c49cf0996a | -8.57251 | -54.72052 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b6c3cbe-d96f-3a8c-a475-8e9cde8b94b9 | -8.10741 | -55.57568 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d6a9c94a-fcb6-374a-ad06-8b40f10a9f59 | -7.09567 | -60.03431 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7c75307-87be-32c4-843a-2da3b0b91717 | -5.88953 | -57.74384 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e1bc7d65-d898-36c7-b43a-78574f5fc913 | -8.57646 | -54.71741 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1cad56d-8bca-30e0-94a4-2891afcf3ca3 | -8.56626 | -54.67108 | 2025-08-13 05:06:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67d4b552-fc46-36d4-899f-50073996661b | -7.45785 | -59.88822 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9285e95f-7d23-32cf-86e5-8f5c443f9fbe | -6.61362 | -43.88266 | 2025-08-13 05:06:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2298af59-5a01-33fd-9f9a-922dfa316c57 | -6.5508 | -56.1985 | 2025-08-13 05:06:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 55f03fad-8962-3106-acee-69d86f1d0167 | -7.2753 | -57.6466 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e18536b-e95a-3005-ad42-287a80132598 | -8.11849 | -55.57027 | 2025-08-13 05:06:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c63c797-85f1-3fa0-ad73-3f440ea44026 | -7.27872 | -57.64715 | 2025-08-13 05:06:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b449daa9-2083-37dc-ae2f-8cb9d47ece3a | -6.01862 | -52.17179 | 2025-08-13 05:06:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60df8b2c-1e15-3c52-9a41-85f3d02c23df | -6.92519 | -59.14916 | 2025-08-13 05:06:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |


[Clique aqui para ver as próximas entradas](README24.md)
