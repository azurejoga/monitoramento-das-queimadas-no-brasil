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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b1b39f8-d07e-37e0-95e7-544f27758547 | -9.41046 | -60.43911 | 2026-08-22 00:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| cc6df0ea-83bf-34a0-adff-de8d29e78921 | -7.01742 | -59.55749 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fa987a70-f727-38d0-851a-507beb830f15 | -8.59604 | -54.71895 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e57cfc35-85fe-35df-9612-5a803c116a0c | -6.37959 | -54.95481 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| ae3cc15b-ab45-375c-b10b-c8196e79befc | -6.74818 | -58.67719 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| ac5dba73-9012-3379-9617-7d5b10f63f9e | -9.21347 | -59.76493 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 81ecc04e-aac0-386a-9569-5c006459a8b3 | -6.55289 | -58.52032 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 3beca508-0a0f-3c66-a75c-6b004c0d5f7d | -6.82895 | -59.6842 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 75e12905-080a-3a1f-a6bd-3d8c9163de97 | -6.02488 | -57.68356 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| c228c1b7-55b6-3c55-8137-071d7d14fd9e | -8.55935 | -54.71512 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1a3ce645-2454-3b26-aa20-e767955f71c4 | -10.75609 | -50.25185 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 80c9e0ef-7f57-3c86-b891-4a06e2e2323a | -8.5136 | -55.32403 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| efd8e8a1-bebc-3893-9913-85f145f99580 | -6.84992 | -59.44226 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 170d8d26-5239-37c6-bf74-51d9841e7d11 | -8.20835 | -55.05132 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 93c51053-00a0-35ff-a9ff-036db2faaccf | -9.17349 | -59.44053 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| bc7eeb53-bd42-3e1a-95f8-01644800a90e | -9.17511 | -59.45368 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 137.5 |
| abf4d385-e625-3c52-85a9-0719eb6053cc | -7.55065 | -55.56422 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fd7de7ee-7bc2-3412-9029-99e89887be3c | -9.16675 | -57.00888 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 11f070eb-3c43-32bc-8b53-a509088e4ecb | -9.15055 | -59.55707 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 57d1dc65-6ba4-3f38-8669-eabe453950d2 | -10.24184 | -50.35674 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 92c41946-c74e-36e9-8be1-7b73b6e71c85 | -6.78706 | -59.43852 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b387b99d-6826-33fd-a896-9b35b36d5c86 | -6.78517 | -58.63287 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 5d1f9855-fe48-3f83-9bbe-4d6f14e9eea0 | -8.16285 | -55.38945 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a41b19a-1385-3e24-b903-fc636b29f08a | -8.53119 | -55.32151 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 6557090f-2c94-3a3a-8204-59ec4c7cfe57 | -8.15278 | -46.70854 | 2026-08-22 00:28:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 79c59b41-6e39-3dad-8180-f95f56043c38 | -8.52028 | -54.83641 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 08c62515-bca9-3c0a-b5d6-68a8f454cdd8 | -7.05361 | -59.83748 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 56f296b8-8b1b-3418-b8b8-085eb32e0d6d | -8.53547 | -54.81594 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 7356bb02-6d11-3f04-b87a-526a74fd180f | -6.937 | -59.32662 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| b6018450-c110-394d-aeba-20035194c1f1 | -6.78658 | -58.64367 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 9d93787d-fb57-3db2-8a62-4e272db42096 | -6.76756 | -58.67453 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 144.0 |
| 5050a2bb-4389-3855-9c05-6063801c418e | -8.18967 | -54.98161 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 4c1a7370-a848-3d6f-bc0f-217cfb4533bc | -6.09563 | -59.91347 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| ce1e9018-bf12-3b82-901f-b9b2163921e4 | -6.74674 | -58.66637 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a8270b17-6df3-37c3-b78b-adb63efad875 | -6.96229 | -59.05573 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 23.4 |
| e594d022-24eb-3082-8e02-e233108e1dca | -6.78948 | -59.44399 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 42fead91-3d68-31e9-8572-0b9d478973ba | -6.09775 | -57.87834 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bc5e99af-fc2e-39e6-80dd-db5aba27c00c | -11.20558 | -55.05313 | 2026-08-22 00:28:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cf4082b6-77cf-3a40-93bc-90352f5841ad | -10.69831 | -50.32779 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| bd871c79-413e-3dc9-893d-2b534e473a6c | -8.58078 | -54.80356 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9b69bf17-16a7-3b08-a948-71910a0b3001 | -6.81679 | -59.88663 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a28b3cdd-7a50-3619-a655-70f492293356 | -7.10495 | -59.77184 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 4037a879-ff42-3d72-9c5f-a1135405ce6c | -9.44544 | -51.64893 | 2026-08-22 00:28:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 968d1dea-8f41-3d90-acbe-95a3a0380053 | -6.87921 | -56.63673 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 9c0e6f58-c2a6-3930-a75e-92910ac4b79e | -6.53514 | -58.53338 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 95866883-ee26-32f5-b716-daad15643cac | -6.69239 | -58.94805 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8c53c2fb-f670-3c80-85c6-f8ecd3504dba | -6.00425 | -57.7989 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 936a9a62-049a-35cb-9e36-aabb0c1b261a | -8.52117 | -55.31392 | 2026-08-22 00:28:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 10ca62be-1a2c-3058-91a8-aaff556a312d | -6.00556 | -57.80848 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 2a15fa63-9d2a-3df7-8b05-2b72ec84b6bb | -6.38086 | -54.96385 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 286acb61-23a9-3589-b02f-fd461fd02023 | -10.255 | -50.2939 | 2026-08-22 00:28:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| c2f7f5f8-3373-3a52-9cf9-88996bbc3712 | -9.11323 | -60.34365 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 97d0aeb2-a719-3e10-99e9-1f0a1293e20c | -6.10014 | -57.69591 | 2026-08-22 00:28:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 57bf0755-81c3-315c-b89b-eec1c6283d4a | -7.01192 | -59.59646 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 75b22dff-6269-3a04-add9-007b51199051 | -6.78866 | -59.59392 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 48775425-adb0-31e9-8400-34d54d623e31 | -7.09956 | -59.77893 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 49897e63-e1b3-32a9-9974-b60df2095e70 | -6.88794 | -56.43553 | 2026-08-22 00:28:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bf85a970-6960-3c1d-9aea-703e6d635941 | -9.18572 | -59.45226 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| f7bb0484-bc05-3611-9e6c-7db5eb2612d3 | -10.90284 | -50.23746 | 2026-08-22 00:28:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f6526049-35ff-3ed1-8159-8b551f3c8fc5 | -6.8413 | -59.45583 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| e0d6a826-592e-344b-bb0a-01d5edc1ec50 | -6.75932 | -58.68666 | 2026-08-22 00:28:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| f533ebf9-8a43-396a-9a56-55ea7d0bbc10 | -6.85314 | -59.46658 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d729ad54-9b04-3e73-9fb2-4afe06601610 | -6.95386 | -59.30638 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 95d89b5a-8417-3d29-8673-6b163e9c1677 | -6.70831 | -58.99198 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a04b9b45-198e-31aa-a099-a0639631ca6f | -6.81298 | -59.3982 | 2026-08-22 00:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.5 |
| df0fee29-23d3-3f12-8964-cb4be4efe300 | -7.26083 | -49.90293 | 2026-08-22 00:28:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| b53b1db4-ae37-3aff-a4ef-1195c02ad2df | -6.37068 | -54.9561 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a799f8cf-75b4-3fda-a554-be3440fd8973 | -6.38976 | -54.96257 | 2026-08-22 00:28:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f346405b-1b7f-304a-b3a2-a353faf8f6bd | -9.18281 | -59.47167 | 2026-08-22 00:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 19de7295-1a8a-3f38-9850-bbb3cbeca41e | -8.522 | -54.8209 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 300.7 |
| 8aa5ef3a-3eb9-3825-86e9-e89528659cb4 | -8.5406 | -54.8197 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 289.8 |
| cc1d0925-00b2-3589-aff0-40377c33273c | -6.8778 | -59.031 | 2026-08-22 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 74adb9ee-ddf7-33a2-9f0f-ac222886a89b | -8.5404 | -54.8398 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 225.2 |
| 473a0525-8738-3108-9e21-b2a686b198e3 | -11.449 | -44.5587 | 2026-08-22 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 35dc8dd2-a83e-3f2e-a862-abcfdb7a65f2 | -11.4298 | -44.5615 | 2026-08-22 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d4feb996-06d6-347f-8b4e-0a48f9aa0223 | -13.997 | -53.6853 | 2026-08-22 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 45f32165-3c84-3bb4-93ec-919f8e382fac | -6.8593 | -59.0318 | 2026-08-22 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 904a4873-6a9d-3432-8699-a86d5cf86eb1 | -10.2776 | -50.3459 | 2026-08-22 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 193ecca3-0f89-3133-96ef-6c2c18e91a26 | -6.9315 | -59.3184 | 2026-08-22 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 35d40e91-ace9-3b17-b3af-775b5fdca882 | -4.9153 | -45.2527 | 2026-08-22 00:30:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 4dbae734-c7c4-3854-a9dd-a462f449b216 | -8.5402 | -54.86 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| beea804c-7177-3d35-a8a6-5d40fe919835 | -10.2398 | -50.3497 | 2026-08-22 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 180.4 |
| 7b94b037-2cb0-37a5-94b1-7817718ceb3c | -10.2395 | -50.3711 | 2026-08-22 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 13c3515b-f2b3-39f5-ad8f-06f4cb008915 | -6.3678 | -54.946 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 25fdf4d5-3575-3ebd-985d-d59205a48528 | -6.3863 | -54.9451 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 28be851e-fa58-3631-bb0b-8a74d429afff | -8.9042 | -60.5385 | 2026-08-22 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6ef448f5-2eb9-308b-bdbb-d0ad4b062086 | -8.5218 | -54.8411 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 223.4 |
| da55ab46-603f-32fe-8c09-ea923774a540 | -5.7985 | -57.5402 | 2026-08-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 155feeff-0665-390a-a260-0fe783098f30 | -5.9997 | -57.8054 | 2026-08-22 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8f81e5c8-c72c-3a0f-b29b-fe6ba8353153 | -16.4971 | -47.9344 | 2026-08-22 00:30:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 231ba3fb-bf39-3875-b10d-688e0986e577 | -6.8188 | -59.6696 | 2026-08-22 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.1 |
| e17492f6-0bcf-38bb-8ca1-3e0b4f26dbac | -8.8856 | -60.5394 | 2026-08-22 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 0ac98f34-ddbe-3b91-908f-cddabf6f4aee | -7.344 | -55.6741 | 2026-08-22 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a7c0446e-d2b2-3108-a374-18b9eb5b9e2d | -2.5042 | -48.1366 | 2026-08-22 00:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c8a45556-7b9d-3c71-b1fb-ed514df7d9d6 | -6.2712 | -62.5231 | 2026-08-22 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 3f06d48c-d388-3e1d-8eec-cb4eaca9b3a2 | -6.2528 | -62.5236 | 2026-08-22 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| ca129b87-20c2-397c-bf91-ff7883ade485 | -10.2584 | -50.3692 | 2026-08-22 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 261d02bd-e7fa-3cd5-a1ee-0db360e8d27c | -8.9934 | -50.7427 | 2026-08-22 00:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| cf61ff84-d304-31f0-a686-960b1d0266ae | -10.2587 | -50.3478 | 2026-08-22 00:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 217.4 |
| c7b01a60-06fd-3e00-a74b-a80f668918a4 | -6.3862 | -54.9651 | 2026-08-22 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |


[Clique aqui para ver as próximas entradas](README7.md)
