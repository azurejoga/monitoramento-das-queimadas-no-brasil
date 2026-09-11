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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bbcb2b60-1e6f-3861-aef5-ae5df0d1af69 | -13.249 | -61.5983 | 2026-09-11 02:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| dfc25c8b-82c7-3837-8a1b-bf009b903c17 | -9.043 | -65.4175 | 2026-09-11 02:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a38f0cac-c100-3e4d-80bf-3ebedcb183bb | -13.2488 | -61.6177 | 2026-09-11 02:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 103.8 |
| c73124d9-b132-3990-b36e-1a495f98ff9b | -13.3053 | -61.6721 | 2026-09-11 02:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 5e784c06-4f0e-3c37-9cec-bf17bfdb11ad | -4.2953 | -49.1021 | 2026-09-11 02:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 05468f9d-16d7-3e02-8445-bff8b43712aa | -9.1799 | -68.2194 | 2026-09-11 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| dad8c674-784a-3d72-9a7e-8513f8578079 | -9.1984 | -68.2189 | 2026-09-11 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ea9d370d-a15b-3aa6-af70-d0e43f3432af | -9.0866 | -61.0287 | 2026-09-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 12966fb3-10ba-3eef-9f13-79bb4839df27 | -13.3243 | -61.6709 | 2026-09-11 02:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 4f25f348-da30-3bc4-9ad6-f6b5cfa3ebcc | -13.2488 | -61.6177 | 2026-09-11 02:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 0cc02247-a51b-307c-b9a3-bfd97ddb870b | -5.2115 | -45.5498 | 2026-09-11 02:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6cee3563-767a-3308-9b0b-007cd18b0b5c | -13.3433 | -61.6696 | 2026-09-11 02:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 89.1 |
| a16a2800-b3ca-3594-b3c1-7e44b930c775 | -4.2953 | -49.1021 | 2026-09-11 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| add5e15b-f26b-376f-a5f1-f21004c25575 | -9.068 | -61.0296 | 2026-09-11 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| c2831a18-eae9-32bf-9f09-0f56a174f8cb | -9.18 | -68.2009 | 2026-09-11 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 0355c1ca-67f0-33c2-b8b5-990561a4259c | -9.1985 | -68.2004 | 2026-09-11 02:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 7dba2226-75e9-3995-90ab-26446b1d7eca | -13.2678 | -61.6164 | 2026-09-11 02:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b44e4959-d9c0-3dbc-bc29-86ef3522dda5 | -9.0866 | -61.0287 | 2026-09-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1b3c62da-af42-3820-9f53-ff38227a4a1d | -13.2678 | -61.6164 | 2026-09-11 02:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| cd938a06-97b4-3673-8c0a-29aae589112c | -13.2488 | -61.6177 | 2026-09-11 02:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 115.8 |
| c64e21d0-6ecc-3008-b79a-fddb4a583d84 | -13.3243 | -61.6709 | 2026-09-11 02:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 5a06a6e5-f74f-371e-a147-31c672af6c9e | -13.249 | -61.5983 | 2026-09-11 02:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b11f0566-004a-3537-a198-f2e11ce71c08 | -9.1799 | -68.2194 | 2026-09-11 02:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 636e9efb-1944-335f-8a24-e1c23e4e84a1 | -13.3433 | -61.6696 | 2026-09-11 02:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| f1a17d5c-fd66-3372-ab26-d71b5c87abb9 | 2.7454 | -60.2012 | 2026-09-11 02:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| cd25c549-5026-3c63-a8b3-43c7044692e8 | -4.2953 | -49.1021 | 2026-09-11 02:30:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ec255b4b-57c1-320e-af54-8abdbeb27d5d | -9.18 | -68.2009 | 2026-09-11 02:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| de328b53-7a7e-389f-bf8c-2168fc60fbdf | -9.068 | -61.0296 | 2026-09-11 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4cc6ffc4-0558-3b67-b711-d854557206e1 | -9.1984 | -68.2189 | 2026-09-11 02:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f053cb52-2d5b-3b68-8f1f-1e1c3883a401 | -5.2115 | -45.5498 | 2026-09-11 02:30:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| cacbc419-326e-30eb-9bc4-3b4e88712bc3 | -4.9335 | -42.8813 | 2026-09-11 02:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 44f8c9bf-5b2c-369d-aa07-881e8d0290b2 | -13.2488 | -61.6177 | 2026-09-11 02:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 117.7 |
| a2cc7b6a-a90e-3121-be8b-7768762ad794 | -9.18 | -68.2009 | 2026-09-11 02:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7af6d7a9-cf47-3f2d-a2e3-f80e4b508147 | -4.3138 | -49.1012 | 2026-09-11 02:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 0dbbfe82-130a-3a75-a1b9-18faf21ff461 | -13.249 | -61.5983 | 2026-09-11 02:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 6dc71c84-ec0f-3ff7-a8ce-352d0be87ebb | -13.3243 | -61.6709 | 2026-09-11 02:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 06c92e58-fd26-3080-82d8-5e252a96f6c3 | -5.1928 | -45.551 | 2026-09-11 02:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| ff5bf745-238b-397c-a6b6-0543166c1e28 | -9.1799 | -68.2194 | 2026-09-11 02:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| dcdfd29b-e022-3fbb-a05f-8cd435ebe162 | -13.3433 | -61.6696 | 2026-09-11 02:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 110.2 |
| a665cc77-d20c-3f1d-ad56-b5044cf8a35e | -9.0866 | -61.0287 | 2026-09-11 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| d9994a38-d388-3737-9123-97817ff25a14 | -4.2953 | -49.1021 | 2026-09-11 02:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 375a0fd2-1bb2-3663-8e34-7a6fcfe32867 | -9.1799 | -68.2194 | 2026-09-11 02:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 2c2da2e2-ee37-37db-8da4-2c80cf466a85 | -9.18 | -68.2009 | 2026-09-11 02:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 49f709c1-f0bd-360f-b804-e3246cc1ed41 | -4.2953 | -49.1021 | 2026-09-11 02:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 7b2fae6d-61f6-31c0-8986-651a329f5af1 | -9.068 | -61.0296 | 2026-09-11 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| cdb51b52-d9cd-30e8-bb42-1e9c04a44821 | -13.2678 | -61.6164 | 2026-09-11 02:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| dc87ee7f-67ed-340d-90e0-a5fb60f03748 | -13.3433 | -61.6696 | 2026-09-11 02:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 7fdc1a22-05ce-3f71-a644-52380067fe32 | -13.3243 | -61.6709 | 2026-09-11 02:50:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| f9334a60-3b9b-3dd9-809d-0a5e82863c06 | -13.2488 | -61.6177 | 2026-09-11 02:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 68fdaaa0-b905-3f45-9748-1e47048092f0 | -12.1501 | -64.1414 | 2026-09-11 02:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 24c18f7a-6dcb-3490-b05f-202c7b145b4d | -8.8361 | -62.489 | 2026-09-11 02:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 92c335a7-ef06-3902-9c63-93851238ad44 | -4.2953 | -49.1021 | 2026-09-11 03:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| a24caf0c-d0ec-3278-a56f-f96a671af1bb | -9.18 | -68.2009 | 2026-09-11 03:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 0dccecf0-aa6e-34b9-ae25-f8bda303f601 | -9.1799 | -68.2194 | 2026-09-11 03:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a8071bcf-dd2b-336b-9d0d-8df1ebdf71a7 | -13.2678 | -61.6164 | 2026-09-11 03:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b628a381-00c1-3e15-8cf2-16a2a3a07278 | -13.3243 | -61.6709 | 2026-09-11 03:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 6dd4784d-6a17-3194-8fb3-fe999b74c83d | -13.3433 | -61.6696 | 2026-09-11 03:00:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 68.2 |
| c5f6de94-0da4-357f-9b3e-3278ac2e0792 | -13.2488 | -61.6177 | 2026-09-11 03:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 82.6 |
| d1194cef-5f7d-3923-ad41-11852644bcf6 | -4.2953 | -49.1021 | 2026-09-11 03:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 6dcb9e04-f188-3f27-b058-1b285358a75a | -9.068 | -61.0296 | 2026-09-11 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 29ce677f-8003-31f4-8ee4-7c6e00b74e38 | -13.3433 | -61.6696 | 2026-09-11 03:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f7ff275a-2b1f-3819-95dd-264928e8340f | -9.1799 | -68.2194 | 2026-09-11 03:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| b1e7c286-3e18-3a2b-b2ed-3d04e85a776f | -13.2488 | -61.6177 | 2026-09-11 03:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| b16beb41-5d23-3a93-bd64-aeee7566db18 | -13.3243 | -61.6709 | 2026-09-11 03:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 51a6c19a-56ff-3ade-88ab-d2cec63966ac | -9.18 | -68.2009 | 2026-09-11 03:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 50a262a8-b714-33f0-9ec9-2598046ab066 | -10.15655 | -36.31501 | 2026-09-11 03:13:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1ee920c3-a0c0-3d29-a615-add0a310b7a4 | -8.91278 | -37.36231 | 2026-09-11 03:13:00 | NOAA-21 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 835e2555-fc4b-35ae-b9bf-f808dd5f2900 | -8.07565 | -38.22306 | 2026-09-11 03:13:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9a261b82-2c26-354f-9b55-25c7b5adcff8 | -7.02836 | -34.88056 | 2026-09-11 03:13:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8cf45db0-e1e3-35ba-80f3-9d0791926776 | -14.89395 | -41.70228 | 2026-09-11 03:15:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9422a3c6-a8b9-3566-b3a6-1e65db2bf387 | -8.8361 | -62.489 | 2026-09-11 03:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 20dd5ed2-2413-3ea7-b53b-9326fd9c46fa | -9.068 | -61.0296 | 2026-09-11 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1adebdc1-e18a-31b3-ab85-0b7f19f661b9 | -9.18 | -68.2009 | 2026-09-11 03:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 1703001f-9335-3fa4-a3c2-ae524bb669f1 | -13.3433 | -61.6696 | 2026-09-11 03:20:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 87af2b4a-896f-391c-987f-f3c409474f12 | -13.2488 | -61.6177 | 2026-09-11 03:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 74.8 |
| d2b126c8-00c7-3f31-b330-0931c309e18b | -9.0866 | -61.0287 | 2026-09-11 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 84031fd8-408a-39e8-8805-87929679aa63 | -9.1799 | -68.2194 | 2026-09-11 03:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2e7f48ca-a6c2-371d-918a-f55f4d70db42 | -4.2953 | -49.1021 | 2026-09-11 03:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 814697ca-3780-33c8-addc-0eed4214ea02 | -13.249 | -61.5983 | 2026-09-11 03:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 039f2da8-7107-30a1-9b13-a4bdbb6e2105 | -13.2488 | -61.6177 | 2026-09-11 03:30:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 61e1866a-6b71-3be1-b58a-2c52f0113aff | -8.8361 | -62.489 | 2026-09-11 03:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 91014109-e8ec-339a-a6cd-741df7728cbd | -13.3433 | -61.6696 | 2026-09-11 03:30:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 2ea1bedc-e766-3615-9461-71c2d8280b4e | -9.1799 | -68.2194 | 2026-09-11 03:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 7f68afd6-76f9-3f0c-9618-02a73e76ef5b | -9.18 | -68.2009 | 2026-09-11 03:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| baa8600b-2a9b-3dd5-bd21-a6b848d03124 | -9.1799 | -68.2194 | 2026-09-11 03:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 47728161-bf14-3908-9f7e-4c834fcd57f4 | -13.3433 | -61.6696 | 2026-09-11 03:40:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 99.1 |
| aec84413-2f0f-3cb1-85f5-b45cdc559f6a | -13.2488 | -61.6177 | 2026-09-11 03:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 1b14a1e9-27c8-3b4b-bab1-98e2108418f6 | -8.8361 | -62.489 | 2026-09-11 03:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 19dba5c1-4559-36a9-a9ac-3b98bd1efd25 | -8.49053 | -44.75279 | 2026-09-11 03:47:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f0a1304d-cc01-3652-b65e-f30073401811 | -6.12497 | -43.7458 | 2026-09-11 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ff379d95-20b8-3276-aee8-3384ca689f1a | -7.8058 | -42.77794 | 2026-09-11 03:47:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 351acbe9-b5d0-3326-819e-677baa0f26e9 | -3.51617 | -43.25888 | 2026-09-11 03:47:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f86efb2-9424-3efe-a5eb-e89999dbcbce | -9.3132 | -44.36357 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3520be92-2b59-32f7-8b46-e7bde0bdf8e3 | -9.31681 | -44.35928 | 2026-09-11 03:47:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a96585d3-ba94-366b-b676-0337bf3b03dc | -8.7809 | -44.18271 | 2026-09-11 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7d04fcb-3ead-3643-98b3-ac8baa50da92 | -3.55947 | -41.11713 | 2026-09-11 03:47:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 643e63ae-d76d-3e64-b498-abf44b68957e | -8.03234 | -43.85126 | 2026-09-11 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 06ac2254-7cbc-3aff-815e-dc27d5643a07 | -8.9094 | -43.88313 | 2026-09-11 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12de03bf-ddb3-3c63-8896-2df49dc16571 | -6.13071 | -43.74664 | 2026-09-11 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2535e86d-dc01-3004-976b-0c2d554611b0 | -8.93613 | -44.40789 | 2026-09-11 03:47:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README8.md)
