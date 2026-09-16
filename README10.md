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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10605b5e-96b6-362f-82d4-8b1b94c7988d | -7.6378 | -67.170799 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e8dce599-682c-3863-8aa0-4d890f9a15e8 | -8.6484 | -66.581902 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ca50ef7-1886-31b4-8fba-b6ffd4c493ff | -9.1321 | -65.8442 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 099fd0e2-a9af-3062-af60-4ca202e75087 | -9.5059 | -64.711899 | 2026-09-16 01:43:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0c280f0c-d00d-3e64-8540-4568c3aa1f41 | -8.6047 | -64.103897 | 2026-09-16 01:43:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b68cd46e-e56d-34fa-84f0-16bf9647d58d | -7.6141 | -67.248901 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e615d2c-33f7-38e8-af37-c015f5e71999 | -9.1419 | -65.842003 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23a278ee-ec1c-3d1f-bada-8a88594ccca9 | -7.6361 | -67.163101 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb37733-bcff-3b9e-9d69-afebc83b1c8a | -7.6158 | -67.256699 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 67fe9456-c27c-31a4-8f63-c022a22b0895 | -7.554 | -62.329601 | 2026-09-16 01:43:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4e3b5be-6a94-3c02-844f-971db3556947 | -8.6864 | -61.393101 | 2026-09-16 01:43:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06dc7916-43f2-3721-a77d-7ea099fd6505 | -9.1009 | -65.934303 | 2026-09-16 01:43:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc635c3-8178-3611-b5f3-105bbc6675f7 | -8.2971 | -61.4063 | 2026-09-16 01:43:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4fc3b932-2092-32d8-a592-72a68f71a9a2 | -9.3906 | -60.316299 | 2026-09-16 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c77ddf42-230b-31bc-9821-f250eb00ac21 | -8.7155 | -62.839001 | 2026-09-16 01:43:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ac8b7e52-62a1-37e3-897f-36ba6414c50a | -1.2821 | -55.719501 | 2026-09-16 01:43:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4959cdb-97cd-3120-b983-bedbc32c5475 | -9.7813 | -60.480701 | 2026-09-16 01:43:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74a197be-6a4b-30cf-b93b-52e09dc5b6b5 | -11.8118 | -60.458099 | 2026-09-16 01:43:00 | METOP-C | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3a382935-3e25-3c96-bdad-7b7e84d7a1ea | -2.6959 | -57.620899 | 2026-09-16 01:43:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52f32526-ef63-3971-a0a1-8e5424f33a2d | -8.6982 | -61.399101 | 2026-09-16 01:43:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe57bf65-fefa-3bdb-b5dc-5422c6fa5fd9 | -10.699 | -54.174702 | 2026-09-16 01:43:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aaec2c6f-6bb3-3242-bbb0-b76f4f3b1c2d | -7.6557 | -67.158798 | 2026-09-16 01:43:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 404513c2-b950-3700-8cc3-85f68925781f | -5.1217 | -47.5928 | 2026-09-16 01:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a4408422-82a6-3785-9634-9c2083c34d18 | -9.3893 | -60.3022 | 2026-09-16 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 8c51f660-9d7a-30a5-998c-a62d19250ce2 | -3.1174 | -57.6779 | 2026-09-16 01:50:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| c7c81d0e-51cb-37e7-a4f5-960c157ca7ee | -11.9033 | -43.8112 | 2026-09-16 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 548a50ff-e0bc-33a7-8aae-cead4a775531 | -5.144 | -55.9345 | 2026-09-16 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 101.5 |
| e8104874-458a-3860-986f-ee36102ac3a9 | -5.1215 | -47.6146 | 2026-09-16 01:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 123.3 |
| ee4cc910-99b1-3517-a5fd-8f207c927b29 | -9.4102 | -62.7113 | 2026-09-16 01:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 2b0f1c5a-abf9-3ac1-aae9-cc3ea2e9183b | -9.7322 | -64.9067 | 2026-09-16 01:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| e355f768-4292-3556-b815-7bcbb7ad7e99 | -7.6511 | -67.164 | 2026-09-16 01:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b9e661f3-c10c-3b03-8b02-f61e892af2da | -11.1401 | -40.4748 | 2026-09-16 01:50:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 3dc5fd50-6a0d-354c-904f-ed7225867a06 | -5.1029 | -47.6157 | 2026-09-16 01:50:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 85c3d3b6-9c1f-3f0c-b3c7-ccce09f74508 | -5.1624 | -55.9338 | 2026-09-16 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 3df96465-6ddb-39bb-b3b1-cc44774f8aee | -11.884 | -43.8142 | 2026-09-16 01:50:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 61f3e4af-01fd-36ee-97c7-8b6eeee90f16 | -9.1123 | -45.7067 | 2026-09-16 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 33.3 |
| e01aaecb-c5ce-361a-882e-92bfa7321e45 | -9.4102 | -62.7113 | 2026-09-16 02:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 0cfecb3f-cd34-3ab0-afac-a4ee033ae556 | -11.2117 | -42.8275 | 2026-09-16 02:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 55b2e6bb-7467-3d08-8fa3-6c6724325f5e | -9.131 | -45.7273 | 2026-09-16 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 8d4c262e-4329-3ac9-8692-0522d6b55929 | -12.6625 | -50.8478 | 2026-09-16 02:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 195b229b-d4a2-3713-9107-6fbd47499380 | -9.7322 | -64.9067 | 2026-09-16 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.7 |
| e316cc63-3308-3bce-9a19-d1480f172968 | -5.1029 | -47.6157 | 2026-09-16 02:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 7ec36bc6-c1fa-38e6-9db4-a338fd0b0ebe | -11.1401 | -40.4748 | 2026-09-16 02:00:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 06bb4bab-e669-3a0b-81b0-8c46aff873a7 | -9.0931 | -45.7314 | 2026-09-16 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 70420217-4ff2-38ae-a484-5436bc671f1d | -5.1217 | -47.5928 | 2026-09-16 02:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 5a9e45ef-f336-3e87-adc6-4affef326488 | -9.7136 | -64.9074 | 2026-09-16 02:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 50912cec-cec9-350d-af24-777dd68ff0e6 | -11.9033 | -43.8112 | 2026-09-16 02:00:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| da32c39d-413d-3a38-bb17-71f9388edfcf | -11.1925 | -42.8305 | 2026-09-16 02:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 81.7 |
| 295e7982-e09e-3878-a446-4bdfc3857b46 | -9.3893 | -60.3022 | 2026-09-16 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 0020596e-7763-3a8e-9926-06cdb08262f0 | -9.112 | -45.7294 | 2026-09-16 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 87cd762a-01c4-388f-8ff8-32eba24199fe | -5.1624 | -55.9338 | 2026-09-16 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 62a19666-02e3-3c52-a7ce-4cabec18d19a | -5.1215 | -47.6146 | 2026-09-16 02:00:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 75b390da-7e3b-326d-b931-4f9ff6d6ac9c | -9.1117 | -45.752 | 2026-09-16 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |
| e04e0a6b-0ac7-362d-9165-34c84c611bdf | -5.144 | -55.9345 | 2026-09-16 02:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 8f9996ad-340d-3311-8bbc-bf552c105b64 | -7.6511 | -67.164 | 2026-09-16 02:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 4caba02d-b6e1-39f6-bc6b-1b1086d52c3e | -9.3893 | -60.3022 | 2026-09-16 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ed396c21-e3b0-31e6-8bf0-39e7646379a0 | -7.6511 | -67.164 | 2026-09-16 02:10:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e1229268-1f92-3ce6-a695-ad35118c60e8 | -5.1217 | -47.5928 | 2026-09-16 02:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 6e731e6d-cb05-36f5-81c6-34c38664f093 | -9.4102 | -62.7113 | 2026-09-16 02:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| b76c1d48-edc2-35e4-a7a2-eb04f7d51502 | -5.1215 | -47.6146 | 2026-09-16 02:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| a7f4b119-dff2-3446-81ea-074347bf12ee | -9.112 | -45.7294 | 2026-09-16 02:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 5f73bc73-7a51-3203-9d7c-1ce3d9d05e8a | -5.1401 | -47.6135 | 2026-09-16 02:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| f4a89f3e-b3e4-3f53-a8f6-7fb0231aa6fc | -11.2117 | -42.8275 | 2026-09-16 02:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 115.4 |
| 97cc733c-563e-39b1-9f59-50ae9158541a | -11.1401 | -40.4748 | 2026-09-16 02:10:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 71.8 |
| 335e2608-edd6-3245-b11f-501f4362c291 | -5.1624 | -55.9338 | 2026-09-16 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| cd5fc1dd-042c-33d3-8ea4-c8e08c5ffe90 | -11.9033 | -43.8112 | 2026-09-16 02:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| e5432fe5-4007-3acb-b7e2-0ef116bd958c | -5.144 | -55.9345 | 2026-09-16 02:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| d1905ab3-681f-3684-9bd7-c08650e7ca72 | -11.1925 | -42.8305 | 2026-09-16 02:10:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 85.1 |
| 598378b5-ff8b-329e-8948-c8006b324ebb | -5.1029 | -47.6157 | 2026-09-16 02:10:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 43.3 |
| d061aae4-2d26-36b4-8c3d-1303145240ed | -9.3893 | -60.3022 | 2026-09-16 02:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a1b21d8e-6b96-32cd-8e87-a93ebc774ab1 | -5.1215 | -47.6146 | 2026-09-16 02:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 0180c0a3-0c6a-3f10-a1ae-a0e5e1b3aecb | -5.1401 | -47.6135 | 2026-09-16 02:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 11cf3470-6fd8-34d8-9242-bca7a36c8c63 | -5.144 | -55.9345 | 2026-09-16 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 88d6ba79-0697-38b2-8fbe-a39a23f7e787 | -10.7729 | -46.2096 | 2026-09-16 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 612e9a94-a092-391c-89b8-8f16fd164d76 | -9.4102 | -62.7113 | 2026-09-16 02:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 0b380d4d-fc9e-3e5f-bf84-8518907e29d2 | -5.1624 | -55.9338 | 2026-09-16 02:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 09415705-84ee-38a7-9e66-851fe9b22586 | -5.1217 | -47.5928 | 2026-09-16 02:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 39.6 |
| fe785540-e88c-3798-a5df-13e1875f67f9 | -7.6511 | -67.164 | 2026-09-16 02:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1974b2a3-2df1-31c6-abc6-782b475facff | -11.9033 | -43.8112 | 2026-09-16 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b813b684-7f58-3dc4-b78b-0963a84ad5fa | -9.112 | -45.7294 | 2026-09-16 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 363cb5e2-37d6-3e5d-ac54-c1e5c0da686a | -5.1029 | -47.6157 | 2026-09-16 02:20:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 0aaa19c2-9377-3fc6-9554-aeda68d168b7 | -11.884 | -43.8142 | 2026-09-16 02:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 790b25d1-778b-3b9b-8755-10c6b6342b37 | -5.144 | -55.9345 | 2026-09-16 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 55f3dd2b-02e9-3627-865d-4941087e1d50 | -10.8114 | -46.182 | 2026-09-16 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 2c13c44d-3fe3-300e-934d-fec26b165a8f | -10.7923 | -46.1845 | 2026-09-16 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 540af924-0f9c-311f-9d15-8a7c2790fe04 | -9.4102 | -62.7113 | 2026-09-16 02:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 6e661c72-adc0-3f97-96c7-b4b2c3a99cd1 | -10.792 | -46.2071 | 2026-09-16 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 6de129f9-a21d-3860-b183-6c1501930d8e | -11.884 | -43.8142 | 2026-09-16 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 3ccabb17-082e-3b6a-8f45-87b194ae5838 | -2.1051 | -52.0575 | 2026-09-16 02:30:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 5fd40664-5deb-39ab-977c-9c8dadd1fb6e | -5.1029 | -47.6157 | 2026-09-16 02:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 2a65e82d-a32b-369c-a42f-99fec5fe04fc | -9.112 | -45.7294 | 2026-09-16 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 411f9989-ef7c-33e2-a557-e8e01a670184 | -5.1217 | -47.5928 | 2026-09-16 02:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 35.1 |
| c55645aa-5340-349a-b410-face4254a892 | -7.6511 | -67.164 | 2026-09-16 02:30:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 99ea7261-ff98-37d4-8ea8-dba87488e16b | -9.3893 | -60.3022 | 2026-09-16 02:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e59dade9-7318-3872-9734-c061791d8925 | -5.1215 | -47.6146 | 2026-09-16 02:30:00 | GOES-19 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f251e2bd-d1de-3318-b880-de63641683c1 | -5.1624 | -55.9338 | 2026-09-16 02:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9a66c905-40a0-3923-aadf-9d25e9395510 | -10.7729 | -46.2096 | 2026-09-16 02:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 3dbd4976-381b-3d0b-a58f-819d0e83928c | -11.1401 | -40.4748 | 2026-09-16 02:30:00 | GOES-19 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 7c2e4c6d-5cb0-3ae0-a363-2b106b6ec1bd | -11.9033 | -43.8112 | 2026-09-16 02:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 94e26a9d-f2bf-347a-8f87-e351bf1658aa | -10.7923 | -46.1845 | 2026-09-16 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 55.1 |


[Clique aqui para ver as próximas entradas](README11.md)
