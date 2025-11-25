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
| eb90ff5c-447f-3b1f-a850-a823cee1b421 | -4.67695 | -45.00938 | 2025-11-25 04:16:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8dc955d6-6176-3864-8034-587ca6a8c89e | -5.4262 | -38.80001 | 2025-11-25 04:16:00 | NPP-375D | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c405bdf1-5b8f-3791-951c-bab6cf3ffa2b | -3.7804 | -44.0481 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a52c7d09-0a2c-3139-846a-abccf32f2150 | -4.04489 | -42.514 | 2025-11-25 04:16:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8845a01-03da-3dee-aebf-e46ea5cb718c | -1.93215 | -46.5153 | 2025-11-25 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f10b1e24-8f9b-30bd-aa14-23f89e82dae3 | -2.93417 | -48.22952 | 2025-11-25 04:16:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 88a7025a-f1f6-3db0-a842-0858ef9f7817 | -3.819 | -48.87212 | 2025-11-25 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0c28ff00-c8c7-3649-b51d-2b16262adef3 | -3.10143 | -44.49523 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4d5de50-f6af-372c-a3ad-4b03a6072f27 | -3.19463 | -44.41321 | 2025-11-25 04:16:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65556b70-8b28-34ff-b102-4e6646af811b | -3.76625 | -44.04957 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 984356b8-4970-340f-9f21-c86a715b643a | -3.59775 | -40.98477 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5d1adaa2-7bb6-367f-aaf4-f9b3bb02306b | -3.53029 | -43.95043 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5df290b-9eb8-3d1e-8b19-fd233b853d13 | -5.34442 | -40.59821 | 2025-11-25 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5a09e555-3964-35d9-bd3e-86e1fcfcd271 | -1.67743 | -52.09115 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17a55152-7e50-3978-b838-56ce814753c6 | -3.10648 | -51.50356 | 2025-11-25 04:16:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00e9a77d-47fd-3aed-a0ec-e688bc9391e8 | -4.81462 | -43.82985 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4ebeaecb-edbf-39cb-a26a-34cd08dfe44f | -3.21472 | -46.83022 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| da3922f1-6f04-37ed-87ae-fe15f0595168 | -4.67286 | -45.01258 | 2025-11-25 04:16:00 | NPP-375D | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc7d44db-2e20-3db8-8438-7fdcdd8ef501 | -1.29941 | -53.14936 | 2025-11-25 04:16:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 936ca9c3-3919-34f8-8c80-e1d13ce0f94f | -1.93225 | -46.5174 | 2025-11-25 04:16:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1833eb9a-dc39-394e-85e6-7ae89a984874 | -4.09224 | -48.81969 | 2025-11-25 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f28365c7-62c4-3140-ae95-bd89049ed2f1 | -3.70684 | -44.9357 | 2025-11-25 04:16:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72e5030c-45b3-3e2b-8157-c7fa7565df4b | -3.3932 | -47.18565 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33c7ff24-bead-3f24-8ecb-09aafc17c165 | -1.64663 | -52.05314 | 2025-11-25 04:16:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7dec670b-feb0-340c-abbb-c46932956cba | -4.94493 | -41.16397 | 2025-11-25 04:16:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1401ea9c-3357-34d2-b3d1-8ed4c1e2ca88 | -4.35394 | -44.32819 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e4a079b-e4ec-37ab-afc3-f4e743e9801f | -4.83252 | -43.82542 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 80bbe98e-7c46-3c3b-be3e-7210f0a8383f | -2.88592 | -44.37708 | 2025-11-25 04:16:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 078017df-e81f-318a-810f-2a331bb2374d | -3.82342 | -48.87286 | 2025-11-25 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d2575a8-fc87-376c-8c1f-74f911fee6ac | -4.1815 | -43.83197 | 2025-11-25 04:16:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e82a56d2-544b-3a1c-89e7-a23d2b86538c | -3.65783 | -42.77877 | 2025-11-25 04:16:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3af6d963-ed6e-370c-943c-e93327b17b19 | -5.31224 | -40.87206 | 2025-11-25 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0f8afb4d-38ce-33d5-941d-2687ec46dcf7 | -5.11858 | -40.80803 | 2025-11-25 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 391f2213-29e2-3982-b6cd-5003f2b7b0c3 | -4.82637 | -43.82082 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f084978e-c6fa-3d68-bf91-ea9ea69a9387 | -3.50672 | -45.72393 | 2025-11-25 04:16:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9964dde-2c3d-3196-a3f7-8b68437da70e | -3.28151 | -42.18231 | 2025-11-25 04:16:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f9ec02c-3dff-3c3a-9448-694200104017 | -4.08782 | -47.0999 | 2025-11-25 04:16:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84d3cf72-47ce-30ed-8526-ae7027ed0d6b | -3.10083 | -44.49901 | 2025-11-25 04:16:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5f24424-cf23-3ffe-a31d-8dfb8b102d85 | -4.8286 | -43.82843 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9fc85d6-a5f0-3396-93e8-896c9178a393 | -3.3884 | -47.19008 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6924ba87-4b97-3ee0-8038-0fecf1d1744f | -3.20772 | -46.8241 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f101041e-4307-3d4d-9aea-c4d020f8f9bc | -1.96335 | -54.70675 | 2025-11-25 04:16:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7fa117f-e049-3b83-b27c-52f316a80222 | -4.04766 | -42.51797 | 2025-11-25 04:16:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 27f9ef78-8085-363d-ba43-fe5cae04fbcd | -3.56538 | -41.6079 | 2025-11-25 04:16:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b520361-0e9c-3070-8c51-7b9be37df9a0 | -4.8191 | -43.8233 | 2025-11-25 04:16:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| dc8548ca-fd78-330a-8485-0bd213e7c13e | -3.59492 | -40.98064 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbe8ac41-e282-340d-9950-c56a68f2cc5f | -3.76684 | -44.04593 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c9b108f-c99f-3010-bd56-8b6b58d10c27 | -4.09154 | -48.8239 | 2025-11-25 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c96c1d77-6e19-342e-9f2b-5aa5a1810bd5 | -4.02788 | -47.77454 | 2025-11-25 04:16:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79d19cf7-d5f4-330e-927b-eb9a45d73d59 | -3.19808 | -44.41375 | 2025-11-25 04:16:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2191550-cd8b-3945-8b5a-dd44ab48ae56 | -3.9907 | -43.43263 | 2025-11-25 04:16:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 018271df-532a-3c84-8562-aedef1ffea4a | -3.21392 | -46.83509 | 2025-11-25 04:16:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1709644-7120-3e65-a33a-7296a70fec84 | -3.26952 | -46.01591 | 2025-11-25 04:16:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f45c19f7-5414-3d2d-8193-4abdab8ea795 | -4.32847 | -45.76529 | 2025-11-25 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83c15395-13fd-3872-82a8-8d537417c746 | -4.72815 | -44.73823 | 2025-11-25 04:16:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fa058bc-2c92-38d7-ad3d-7b770259cc73 | -5.05637 | -37.92295 | 2025-11-25 04:16:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4cfa962a-39b9-3da4-9d98-5ff27439e784 | -4.59324 | -44.05443 | 2025-11-25 04:16:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21c92536-cf4c-32d2-b1e0-2e76c2038fbc | -4.93983 | -41.15207 | 2025-11-25 04:16:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fde73429-27c8-32a5-930e-b664e55b3eb9 | -4.16829 | -41.62217 | 2025-11-25 04:16:00 | NPP-375D | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 514d86ab-06f9-3add-ae7a-f8ce9a73d8a9 | -3.41983 | -44.22782 | 2025-11-25 04:16:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79649d24-8103-3206-8741-9e5182146ed2 | -4.60095 | -44.87706 | 2025-11-25 04:16:00 | NPP-375D | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba31d040-1e8e-39c3-9c8b-dbc8659b5030 | -3.41142 | -39.19591 | 2025-11-25 04:16:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f662ba1c-4a82-3228-b86d-ce65261941e5 | -3.02941 | -51.03214 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f95fcfd3-e9c5-3b63-b77d-3b3f8d1d4fb0 | -5.63531 | -35.47991 | 2025-11-25 04:16:00 | NPP-375D | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 604d4a56-ffb3-33e5-9e36-c52f0d59b117 | -4.33807 | -45.63537 | 2025-11-25 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ceb5c2aa-2cb3-3ba5-af79-be75e82ecbeb | -3.42065 | -45.4516 | 2025-11-25 04:16:00 | NPP-375D | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1db4777c-f6c5-3841-83c0-588d03f3a05a | -2.96086 | -41.55352 | 2025-11-25 04:16:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ac3e31e-949c-32e4-b152-c4c68d041be4 | -3.57361 | -43.81333 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84035961-4259-33fa-99c2-99cc3b89a88c | -3.83084 | -43.99318 | 2025-11-25 04:16:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ea6333a-8e72-3361-81d9-c4c8ba6aea4e | -3.60449 | -40.98601 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8be46427-7faf-317c-a171-fc79a953b280 | -4.33448 | -45.63479 | 2025-11-25 04:16:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96d9361c-5d01-3af7-83ae-91de5c997919 | -3.60112 | -40.98539 | 2025-11-25 04:16:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 40321cff-0f2a-34a7-96a4-a795f9e67427 | -3.77419 | -44.04342 | 2025-11-25 04:16:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a4b7cf1-bb18-3645-8d30-8a44e3f85ada | -4.74995 | -44.45369 | 2025-11-25 04:16:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6387f0b-d26a-38b7-b349-fb246270091b | -3.71702 | -49.07582 | 2025-11-25 04:16:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 736b7524-7df1-3c3d-b86b-c0f9c41e50a4 | -4.44943 | -44.29853 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2df8fe29-4964-3f1c-b847-6fe1955a2a4c | -5.34381 | -40.88816 | 2025-11-25 04:16:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| df6fc990-31c0-3dca-95b8-489137a32a22 | -3.02452 | -51.03135 | 2025-11-25 04:16:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da192b2a-7616-32cc-88dc-7628e1d378f6 | -4.33705 | -44.32535 | 2025-11-25 04:16:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1f980c5-0d2b-37ad-838e-99b2c9afbd3d | -3.94636 | -50.61315 | 2025-11-25 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a972c169-7211-3798-90ce-01b90d985c15 | -6.27956 | -39.68226 | 2025-11-25 04:18:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5e3debd6-8f79-32b0-9e3e-02c68b6d2dc0 | -5.78131 | -44.0517 | 2025-11-25 04:18:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffc4ad99-da97-378d-ad2b-501897f748a6 | -8.06333 | -43.12757 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 67f17a6b-35c4-3d0a-8a94-f93831fb84ed | -6.3856 | -43.86637 | 2025-11-25 04:18:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb7290f5-a447-3cf4-acfd-89750dd6be22 | -8.04508 | -43.1354 | 2025-11-25 04:18:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 55494756-cd43-37c8-aba0-4f74f73cd8b1 | -4.48006 | -48.15074 | 2025-11-25 04:18:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cec26c75-e370-3b2f-b9c4-c90a1df94bb1 | -6.85062 | -46.28282 | 2025-11-25 04:18:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7bdf10b-2bd8-31d1-a37e-aa7ce65ac07c | -7.34183 | -35.22983 | 2025-11-25 04:18:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bb70d787-9ae7-3e16-8f78-7a256019c22e | -6.12191 | -42.94839 | 2025-11-25 04:18:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f3d2a4de-4cac-3c2b-b22b-93b8f3e7ae8a | -6.24267 | -43.68201 | 2025-11-25 04:18:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fafdb210-23ec-3f6e-98de-d28df5138483 | -3.95069 | -50.61889 | 2025-11-25 04:18:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81e5f2ed-f49e-3618-95a1-509ea74462e7 | -6.24469 | -40.30069 | 2025-11-25 04:18:00 | NPP-375D | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0c89358c-146f-3498-b4ae-10b36a118d19 | -5.12857 | -43.02533 | 2025-11-25 04:18:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39584501-f735-3e2c-b117-fa71a1abd2f2 | -5.90348 | -44.00938 | 2025-11-25 04:18:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbd51152-9b63-331d-b7df-a54ee8d868eb | -5.05541 | -44.20411 | 2025-11-25 04:18:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed279d9f-0e2a-3115-b483-c6369e9bcd77 | -7.56636 | -45.86742 | 2025-11-25 04:18:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 789d8db5-e98a-337d-980c-9ee510a3e2c5 | -6.68548 | -43.93914 | 2025-11-25 04:18:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 50c68a2f-37ab-30f5-a740-ce683e59811b | -8.58127 | -44.10991 | 2025-11-25 04:18:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c8ffb613-a5ec-3642-8e8d-ba294d566ffc | -8.58515 | -44.10695 | 2025-11-25 04:18:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4bdfeebb-d035-3d95-9174-26ffedd65ba5 | -5.41422 | -43.65771 | 2025-11-25 04:18:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README8.md)
