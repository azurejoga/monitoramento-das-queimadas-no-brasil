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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fae8d67c-3848-3803-a43a-d081bff7b545 | -7.0352 | -44.6396 | 2026-09-13 11:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| eaa6c282-9afa-3961-ac59-9373b3f7c69d | -10.6335 | -50.5651 | 2026-09-13 11:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 161.6 |
| 42010bd0-8f3d-379a-b7e6-3c21c26af165 | -7.03 | -44.67 | 2026-09-13 11:15:00 | MSG-03 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c0625fb7-3e83-3fcf-8751-9881d2cfe81a | -11.8189 | -46.386 | 2026-09-13 11:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 912cc8ed-a269-32e0-a9bc-6ab29a293c74 | -7.0166 | -44.6184 | 2026-09-13 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| bb38b4c6-97c5-3652-9467-715c82038d49 | -10.6335 | -50.5651 | 2026-09-13 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.5 |
| 6fd251f2-41a8-3df6-b9cc-6571ced7d693 | -7.0352 | -44.6396 | 2026-09-13 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| aa3a1768-4c0d-3844-a218-7547104b8a2b | -7.0164 | -44.6413 | 2026-09-13 11:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 289.2 |
| 0bd0f7ed-0c15-3a88-bd59-c91e7a381bc8 | -7.0166 | -44.6184 | 2026-09-13 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 06e28a58-57a9-394d-b035-fd15a9570283 | -7.0352 | -44.6396 | 2026-09-13 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 7b524a18-74f9-3118-b107-12aced1e43cd | -10.6829 | -54.1475 | 2026-09-13 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| ec54f6d0-bac4-3d77-9f5e-35482cf219b8 | -7.0164 | -44.6413 | 2026-09-13 11:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 344.2 |
| c3bbb306-b6eb-31ad-9622-2f5d270cbee3 | -10.6335 | -50.5651 | 2026-09-13 11:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 64d45503-5236-3996-96b2-f57ef81615f8 | -10.6827 | -54.1679 | 2026-09-13 11:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| fa046d78-01fa-3daa-a93a-fe749b17403a | -10.6829 | -54.1475 | 2026-09-13 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 0f95c648-bf97-351b-8cc7-83f481d7769d | -7.0164 | -44.6413 | 2026-09-13 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 325.0 |
| 62efb5e6-7697-343e-bbe0-efdd65790f9c | -10.6827 | -54.1679 | 2026-09-13 11:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| eb2ec92b-58ee-34de-9059-79796d44674c | -7.0352 | -44.6396 | 2026-09-13 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2ea52e40-da60-3841-aba1-6fb0fd63888e | -11.354 | -46.7874 | 2026-09-13 11:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| b8c6af2a-3094-3f17-964f-b87230af0315 | -7.0166 | -44.6184 | 2026-09-13 11:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 2b633316-e0cb-371a-b018-2a2bdab458e5 | -7.0164 | -44.6413 | 2026-09-13 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 310.6 |
| 6f15a86f-1546-3ba9-9e1b-80e637d05539 | -7.0166 | -44.6184 | 2026-09-13 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 7efb6d11-6358-314c-8837-237638c4f700 | -10.6827 | -54.1679 | 2026-09-13 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 56d4e5ac-91b8-3740-ae02-69800567333f | -10.7532 | -46.2573 | 2026-09-13 11:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 4e0768a1-0c4a-3b86-bdbc-fb3d501bc765 | -10.7535 | -46.2347 | 2026-09-13 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bfcb7288-69bb-3163-9951-bf0882851460 | -10.6829 | -54.1475 | 2026-09-13 11:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 19270554-8d01-347c-9d4b-906547d350d5 | -7.0352 | -44.6396 | 2026-09-13 11:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| e20a480e-f8f3-3e1e-81ab-891e5605f031 | -11.354 | -46.7874 | 2026-09-13 11:50:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 120.8 |
| d689b732-9eff-3d01-92bb-420b68ae2a03 | -11.0429 | -47.1856 | 2026-09-13 12:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| fa65d52d-a80c-3fb7-95df-10fec7228963 | -10.6829 | -54.1475 | 2026-09-13 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.5 |
| 880c45b0-0c9b-3735-b46f-cb24ba47e635 | -7.0166 | -44.6184 | 2026-09-13 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 71c40005-ad41-30bf-8d58-b09e05d3850c | -9.8992 | -47.5874 | 2026-09-13 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| e3a1776c-28d8-3b7c-9cca-357a2a1e7ca5 | -10.7535 | -46.2347 | 2026-09-13 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 152.0 |
| c4b94f6b-439d-3f6a-b2eb-91cfbe60632d | -11.0433 | -47.1633 | 2026-09-13 12:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 4662ae6d-6fa0-3d0a-b864-f4af3dd81ac2 | -10.7532 | -46.2573 | 2026-09-13 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 166.8 |
| a2afbfb1-0def-36fa-8fb4-5b63c3ee21da | -7.0352 | -44.6396 | 2026-09-13 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| db12f6ac-0ded-3f76-9108-69cb94fb66a3 | -7.0164 | -44.6413 | 2026-09-13 12:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 258.4 |
| 4d6b6469-d313-354f-9cd0-ec3e9746bceb | -11.354 | -46.7874 | 2026-09-13 12:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 2c763796-1268-38e1-9d02-c5d26379a28c | -10.6827 | -54.1679 | 2026-09-13 12:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 191.8 |
| c7471e98-d6d0-3454-b32f-767966f73f6a | -11.0429 | -47.1856 | 2026-09-13 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0921346a-29e4-30f6-9306-4cd9e9d6dbc5 | -10.7535 | -46.2347 | 2026-09-13 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 266.3 |
| 95f061ae-4dd7-3946-9d88-b9ba489376d5 | -11.0433 | -47.1633 | 2026-09-13 12:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| deeb708e-b00f-3564-89b6-876d0362610d | -10.7018 | -54.1458 | 2026-09-13 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 6ed81b67-9cfe-3bba-9b27-6fa63cabb6ea | -7.7636 | -46.6722 | 2026-09-13 12:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 52c1b4bb-8b80-3ac1-b478-3540e63a0958 | -11.0623 | -47.1609 | 2026-09-13 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 5bbdfe0a-1e0b-3408-847b-e854bd5c3054 | -7.0164 | -44.6413 | 2026-09-13 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 304.3 |
| 7029794d-d99f-3461-9b70-46cf27a7b6cc | -10.6829 | -54.1475 | 2026-09-13 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 195.5 |
| 98aef328-f0ad-339e-94ac-85e2cbb92fac | -10.6827 | -54.1679 | 2026-09-13 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 235.8 |
| 166df3e0-98ed-3fdc-b726-bde39d840964 | -7.0166 | -44.6184 | 2026-09-13 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| ab54f53a-ad5b-37e0-afdd-2e0c684cef5b | -10.7015 | -54.1663 | 2026-09-13 12:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| ff6fb6e0-768a-39bd-9871-5f569145b3aa | -10.7532 | -46.2573 | 2026-09-13 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 528.9 |
| 3a50a219-e088-3c02-bebb-b7747c8635b3 | -7.0352 | -44.6396 | 2026-09-13 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 2fba8230-558c-35a2-90a4-5c60503b3399 | -11.3532 | -46.8324 | 2026-09-13 12:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 1266b822-26b0-39ae-b72c-92e95f5f363a | -10.6827 | -54.1679 | 2026-09-13 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.6 |
| 8eb8e9c5-3b52-3baf-9a5d-76e16c65c88c | -10.7015 | -54.1663 | 2026-09-13 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| ef2d51ac-cd2e-3908-888a-c3e2f21ded20 | -10.7532 | -46.2573 | 2026-09-13 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 2fd033ce-426d-30ad-a7b6-74649c8b3429 | -10.6829 | -54.1475 | 2026-09-13 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 168.1 |
| 7a01c1b8-7734-32d5-ab3e-3fdf9d693235 | -10.7018 | -54.1458 | 2026-09-13 12:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 8655a607-99e5-3fba-a3c7-6ceb3cba5f49 | -7.0352 | -44.6396 | 2026-09-13 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 6d32f3ba-afe8-37a7-98a0-d3b18234f787 | -7.0166 | -44.6184 | 2026-09-13 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 28b027bc-d263-3d07-938c-2fd7c8d4238d | -7.0164 | -44.6413 | 2026-09-13 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 222.9 |
| 151153c0-cb57-31e6-9f41-ca8992b58cfc | -10.7535 | -46.2347 | 2026-09-13 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| ace92660-3320-37f5-a5d5-32dfd832dd5e | 3.82888 | -59.58424 | 2026-09-13 12:23:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| cdd5fc5f-6b62-3ff1-91e3-fa832ff78a18 | 3.95291 | -59.62193 | 2026-09-13 12:23:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 82ad12ec-b9c1-3d4d-8bba-14b6e6d99c53 | -2.67665 | -57.54947 | 2026-09-13 12:25:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d428637c-2b5b-33cc-b064-d429703c4501 | -3.39222 | -50.75144 | 2026-09-13 12:25:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 67900824-aff3-3f9e-b853-059afc322f72 | -1.4438 | -49.0204 | 2026-09-13 12:25:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| d72bb738-f846-3eef-9d93-7528d3541706 | -2.68679 | -57.54182 | 2026-09-13 12:25:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 6b2576c2-578b-30b7-8055-372617078487 | 0.14297 | -51.46594 | 2026-09-13 12:25:00 | TERRA_M-T | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 1d5c5363-3718-3b29-b690-25ff005311ff | -2.67792 | -57.5406 | 2026-09-13 12:25:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 932700a9-f92f-318d-ac43-b0c062f3340f | -3.39272 | -50.75709 | 2026-09-13 12:25:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 562dfbcd-9941-3e71-833d-90e1b36a6f6f | -2.94353 | -50.39933 | 2026-09-13 12:25:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| b97268d0-7caa-3b19-8fea-a2029939b3ae | -1.46296 | -52.96799 | 2026-09-13 12:25:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 901904f5-a9e5-3c86-8c93-eb9c80bebc0e | -3.38955 | -50.77057 | 2026-09-13 12:25:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 11721fd5-e848-36ca-901d-99202c67ac91 | -2.66273 | -57.5204 | 2026-09-13 12:25:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 8724e6e9-1e59-38c5-be82-da49ea32f293 | -2.95649 | -50.40106 | 2026-09-13 12:25:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| be2b343f-8a3a-36f6-afb0-32de6b52069c | -2.68552 | -57.5507 | 2026-09-13 12:25:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 2a1e6a61-44b3-38ac-bba6-d4cf458143dc | -1.22841 | -54.12155 | 2026-09-13 12:25:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0872fbc2-a588-3fcb-a616-6d27480f6b16 | -2.67919 | -57.53172 | 2026-09-13 12:25:00 | TERRA_M-T | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 38.4 |
| ebb9064e-d4f3-38af-a937-640ce7828574 | -9.46037 | -59.19158 | 2026-09-13 12:27:00 | TERRA_M-T | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 325e129b-41e0-3fa6-b662-5bccc798ac35 | -6.27953 | -59.92739 | 2026-09-13 12:27:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f500740d-04a6-331d-9f29-8f56e8fb24a6 | -3.16548 | -58.63997 | 2026-09-13 12:27:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f728df80-143a-397d-b6ea-0d1686119e7f | -5.13476 | -55.96188 | 2026-09-13 12:27:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 1fa017c9-04e9-3b96-9e5c-7016f393042a | -8.77442 | -61.40457 | 2026-09-13 12:27:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 95d86164-d6e6-3397-9fc8-e8b09e99daf8 | -10.94465 | -57.18129 | 2026-09-13 12:27:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4ba28f5c-ea30-32c7-a907-34593f000115 | -3.77205 | -58.84626 | 2026-09-13 12:27:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 53d47e2e-000e-3f6e-9a28-45ba2a4010c7 | -10.51944 | -57.45734 | 2026-09-13 12:27:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9e364f07-19c3-365d-8669-37fe9dc09eee | -3.44716 | -59.51134 | 2026-09-13 12:27:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 65abd46c-f417-3c34-bb3e-b8ebe53578ba | -3.60154 | -59.07654 | 2026-09-13 12:27:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e2a2caed-7829-352a-a8bf-a20c72613439 | -3.73649 | -61.75505 | 2026-09-13 12:27:00 | TERRA_M-T | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 995b94c9-2d4a-39b9-b684-d6b8cf75a837 | -8.54054 | -54.7192 | 2026-09-13 12:27:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2858d645-fd15-3859-82c8-4921ae5cd7e0 | -10.69356 | -54.17289 | 2026-09-13 12:27:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| a773c2f9-8d9e-31a4-98ae-61764bb8a247 | -3.44568 | -59.52172 | 2026-09-13 12:27:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| e343d02e-a9ec-36d1-8039-1b3340575743 | -5.1244 | -55.96994 | 2026-09-13 12:27:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| fdebbb82-b1cc-3f6b-9e0f-c1fe9a1dab66 | -5.12572 | -55.96065 | 2026-09-13 12:27:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| d9bef2f2-7f08-3e5c-8b4f-20321dac4d77 | -8.29557 | -51.22116 | 2026-09-13 12:27:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| dac8c3cc-6341-33a6-94dd-5142e4b1a545 | -4.13346 | -56.32817 | 2026-09-13 12:27:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 34b81daa-0ec8-311a-a0dd-6ed3fdf07c47 | -6.67906 | -58.71139 | 2026-09-13 12:27:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0f2d955c-42e3-3927-9c88-007b907c2f25 | -6.02935 | -52.75049 | 2026-09-13 12:27:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| b66c29b3-f4f2-3d1f-a1ea-cb692898e031 | -4.66847 | -55.99894 | 2026-09-13 12:27:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |


[Clique aqui para ver as próximas entradas](README60.md)
