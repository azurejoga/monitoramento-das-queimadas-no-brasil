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

## Dados Diários - Página 158

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39af999c-1601-373b-a6ec-c03b25247eb7 | -6.7614 | -60.0559 | 2024-10-09 04:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 7d252b6a-621b-33e5-b703-b1237c49ae70 | -10.4287 | -60.9979 | 2024-10-09 04:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 10ff45eb-8bfa-30b5-ad56-5f7b5c0d0e68 | -10.3843 | -64.8255 | 2024-10-09 04:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b254e5dd-7f36-322f-8875-c10b0fd72cb6 | -10.3656 | -64.8262 | 2024-10-09 04:46:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 8346b315-e6e6-3193-9703-6bf8c462d4ff | -10.6258 | -55.8953 | 2024-10-09 04:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1c3e2fd2-2130-3e33-8c98-0401b0ed9ce5 | -10.6256 | -55.9154 | 2024-10-09 04:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| db29cb01-8990-33a7-ad6d-85a8c096ac4c | -10.8755 | -63.8979 | 2024-10-09 04:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| dc17774c-7dd9-3b58-bf5e-e17d5952d167 | -10.8754 | -63.9169 | 2024-10-09 04:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2a3f615a-9fa7-3fff-b439-304d6f2fcbbe | -11.2583 | -60.3885 | 2024-10-09 04:46:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 4fea4e33-0522-3e9b-a589-c043b34aeede | -11.2771 | -60.3873 | 2024-10-09 04:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d47e8587-2d85-35f3-92e0-305910f8c7b2 | -11.5233 | -65.137 | 2024-10-09 04:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 9d5f22ad-752b-3e76-9c6e-4466fe32a90b | -11.693 | -65.0163 | 2024-10-09 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 8a69cbbc-d53e-3eac-aa61-b4b66e29fe1d | -11.6806 | -64.0312 | 2024-10-09 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 0825ab15-2b8a-363c-acdb-477cf980151f | -11.7119 | -64.9966 | 2024-10-09 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 248fc486-9550-309a-8316-af8e6a325150 | -11.7117 | -65.0155 | 2024-10-09 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 146.8 |
| 0638b634-cbe4-3577-ba74-f40f8642bcab | -11.6931 | -64.9974 | 2024-10-09 04:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| f32c9473-9c24-3991-81c0-5f3d1094a55a | -13.417 | -61.9169 | 2024-10-09 04:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 11e2da74-903c-3935-9304-5f372a9f78c6 | -13.398 | -61.9182 | 2024-10-09 04:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 991a7633-1586-39e7-80ff-7ca2d9c3ba50 | -13.3978 | -61.9376 | 2024-10-09 04:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 41.1 |
| b08fc3d2-8383-3aa1-beb7-376d27822502 | -15.7076 | -59.3726 | 2024-10-09 04:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 03e3b7f8-b465-3c89-b3c7-25fec9e1589f | -15.688 | -59.3945 | 2024-10-09 04:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 27.4 |
| dbd25fff-753f-3b93-b988-6bf688c2c924 | -1.11 | -53.6173 | 2024-10-09 04:55:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ee058c8b-01df-3a67-a67c-588e82cdc6fa | -6.7799 | -60.036 | 2024-10-09 04:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 9d8e980d-0b8e-33cf-a921-5f20dc4db80d | -6.7798 | -60.0552 | 2024-10-09 04:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 107.1 |
| cd33d2de-4707-3669-8342-b1fc734e78e9 | -6.7615 | -60.0367 | 2024-10-09 04:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0a8ee107-3a8e-3dd0-b105-72ff35ea13b1 | -6.7614 | -60.0559 | 2024-10-09 04:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 2af811e9-6a51-3ed4-a012-77a0409d5ef9 | -10.4287 | -60.9979 | 2024-10-09 04:56:05 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 492ddf54-da8b-382c-ad5f-96504d5c9650 | -1.60435 | -47.38352 | 2024-10-09 04:59:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da554c8d-cd9e-3c48-97f6-d7059bb7ac9e | -1.37891 | -47.49326 | 2024-10-09 04:59:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f89e9f3-4974-36d6-8f5a-3eda9b3214ca | -1.3769 | -47.49511 | 2024-10-09 04:59:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef75fb5a-18f6-3141-bc30-0feb200aef3e | -1.24077 | -47.89797 | 2024-10-09 04:59:00 | NOAA-20 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38bf522e-38e1-3f82-823b-937b79d93193 | -1.19261 | -47.47663 | 2024-10-09 04:59:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 955721a0-7f96-34a9-a7a3-81da158b298b | -1.18797 | -47.47594 | 2024-10-09 04:59:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f3f7ce26-5ffd-37ea-9d9a-7dcce5fc05f1 | -0.83805 | -48.6343 | 2024-10-09 04:59:00 | NOAA-20 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28ee52c6-dafd-33d6-a05c-da313aeeb669 | 0.82158 | -51.84863 | 2024-10-09 04:59:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b56eecb7-a479-334a-af03-0dd4d900f205 | -0.56986 | -52.11796 | 2024-10-09 04:59:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fcc9e63-75d1-3ac6-9c9e-6c3698d4708d | 1.11763 | -60.51627 | 2024-10-09 04:59:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 776cdf8a-6ee6-396f-88e9-c3c79b6781e9 | -3.82076 | -41.60379 | 2024-10-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 686f6b65-0799-3571-94c2-35739ec93d29 | -3.81979 | -41.61049 | 2024-10-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b9728b33-2648-33d1-b618-9a1e72f733f1 | -3.8137 | -41.60288 | 2024-10-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 4c9ee3ac-f7b1-3794-9f91-6b623792cffc | -3.81273 | -41.60958 | 2024-10-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| dbc478ca-f4ad-3f51-961b-7f2713e76158 | -3.80566 | -41.60868 | 2024-10-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d19a895b-1eb3-3a1b-8b12-aeeee1e8b7a1 | -3.79762 | -41.61458 | 2024-10-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c5c78b72-c954-3553-a671-ec71d78ef641 | -3.79665 | -41.62133 | 2024-10-09 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 188df24f-ffd1-301e-b78e-aea87d837edf | -4.17572 | -42.99512 | 2024-10-09 05:01:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bb631af-7e04-3dd3-9409-126aa8fb1fdd | -4.17484 | -42.99629 | 2024-10-09 05:01:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0dd168d7-f6e0-383c-8337-819d2513bd29 | -4.1692 | -42.99416 | 2024-10-09 05:01:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74fa7e69-0047-390d-844c-8284cbfc2ce1 | -4.16832 | -42.99528 | 2024-10-09 05:01:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a38dd20c-0795-31d5-be47-ca527564a922 | -4.16268 | -42.99316 | 2024-10-09 05:01:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54bddbfc-be91-3383-b6ef-c01d82cc19f5 | -4.16181 | -42.99424 | 2024-10-09 05:01:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f84b485d-623c-3877-abdd-adf2e2acc3f4 | -3.61886 | -42.76141 | 2024-10-09 05:01:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 003a4d24-297f-31f9-a940-3bf1dd752c22 | -6.18516 | -42.61277 | 2024-10-09 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3fed5c51-b79c-3be8-9ea2-1c8366bcf0c5 | -6.17837 | -42.61135 | 2024-10-09 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc08b622-7f6c-3891-917d-2967b455165b | -5.97202 | -43.36293 | 2024-10-09 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7163b194-ab10-334b-b376-4170b02968e1 | -5.96469 | -43.36791 | 2024-10-09 05:01:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 71714cf5-304c-3aaa-bbee-94bb73a63e03 | -6.31397 | -43.37875 | 2024-10-09 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f7a9d564-928e-3f15-920e-6388f1c5fb7a | -6.31322 | -43.38429 | 2024-10-09 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d36ed57b-163e-3f54-b7bb-6eb2d7f73ce1 | -5.58333 | -43.25372 | 2024-10-09 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e46af471-2694-397d-90c1-4a9c1274e024 | -5.58253 | -43.2595 | 2024-10-09 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 902a0726-35ef-394c-ace8-65397c613014 | -5.57601 | -43.2584 | 2024-10-09 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f88c366-a8a3-3f1e-99a0-14c73903d47f | -7.79002 | -43.08967 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ad2ecb08-b3ba-30ec-abd1-5061c4b4a6fe | -7.78928 | -43.09554 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3aaae738-a76d-3df2-9042-843abe02f81a | -7.7725 | -43.10546 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7c41c2af-e94d-3d9b-be6a-d4be18569d2b | -7.77178 | -43.11094 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6cbb537d-1435-3502-a27b-57b52cb0ada0 | -7.76809 | -43.09925 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bb32617e-e372-3ca9-9105-4a561b45428a | -7.76737 | -43.10501 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4fbf891b-41d2-3e05-b510-10e12f29d2ce | -7.76666 | -43.11071 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 172b5fbe-2aa8-38f5-a7f5-7c5f7eac4a00 | -7.76653 | -43.09837 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 570d1954-b0c8-3a12-ad98-6656dc0f4a5e | -7.76577 | -43.10416 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1241afef-8210-33d7-9ff3-eb0803ecb3be | -7.73197 | -43.04506 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a7dcf66a-c0fb-39d0-8386-5488a05cfc8d | -7.73042 | -43.05708 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1efb93d6-a63a-36c6-8218-5e93d05f303f | -7.72439 | -43.05018 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a41c059b-2817-39c2-982b-77fea7353c36 | -7.72362 | -43.05613 | 2024-10-09 05:01:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 39c5df1b-6a00-3f03-a184-353bd8931253 | -7.69059 | -42.9889 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8dc105a8-fa5c-32ee-9d2a-a4524f2ac374 | -7.68985 | -42.99477 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4ea4c693-a09e-3735-8d40-90fe66681182 | -7.68937 | -42.98702 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0400dc4a-e410-3f4e-bc91-2772a50e26fb | -7.68858 | -42.99295 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3ef4b51c-da5d-336f-8f7a-fc82d8fb6a5c | -7.68376 | -42.98794 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1ff52d58-12ff-358c-95f1-b4bbacf723b9 | -7.68304 | -42.99372 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| cc29fa9b-e780-3620-b763-0afe0146f9fe | -7.68254 | -42.98606 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b7953aca-f43c-3131-97ea-77586e6ace71 | -7.68177 | -42.99191 | 2024-10-09 05:01:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d8eec17c-585f-3aa5-95a6-dde83b7f4eb4 | -7.65828 | -42.51963 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8c3ec56d-2404-3557-8caa-b182f15cc1f2 | -7.65746 | -42.5261 | 2024-10-09 05:01:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 48657b54-2513-39e8-9818-493f9db43d21 | -7.23664 | -42.29962 | 2024-10-09 05:01:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8e4fbe31-089b-3d31-b391-eba3b84a02e8 | -7.23234 | -42.29929 | 2024-10-09 05:01:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fdadcf0a-6e92-37ab-9f7d-284a43ef2f0c | -7.22956 | -42.29872 | 2024-10-09 05:01:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0bbb53f6-5e9a-3e5d-8cef-d54aa7b82e24 | -7.22527 | -42.2984 | 2024-10-09 05:01:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9fbd81ff-e280-3533-a3a0-3b504254c1a7 | -7.13642 | -42.65125 | 2024-10-09 05:01:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b0cbb440-9def-3cc2-a4c8-25233ac03afb | -7.12953 | -42.65012 | 2024-10-09 05:01:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bd8b5073-6bc6-3573-84ef-61419845baf8 | -6.83207 | -42.82348 | 2024-10-09 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 51e13d14-437f-30ac-9ed9-77998725c2e4 | -4.64549 | -44.37397 | 2024-10-09 05:01:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab9cdd1a-77a2-3744-a6bf-9939e2cfef74 | -4.64489 | -44.37831 | 2024-10-09 05:01:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c5ef68d-5c38-3471-8fce-e62d33a1becc | -4.64341 | -44.37603 | 2024-10-09 05:01:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5d7bb1f9-703d-3a47-a977-1ea92a40fd87 | -4.63945 | -44.3732 | 2024-10-09 05:01:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e0f37b7-8046-32a4-8d84-e848b6abbec2 | -4.63882 | -44.37772 | 2024-10-09 05:01:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 27517e0d-6d07-3e38-a3b3-0f754f8d533a | -4.28331 | -44.39808 | 2024-10-09 05:01:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8719921-100d-3ce4-a335-c891588d0b5a | -4.27668 | -44.40158 | 2024-10-09 05:01:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b2adbd8-9bb2-31d7-863f-0ed3a308a144 | -4.22783 | -44.27181 | 2024-10-09 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfef966d-f7e9-3abc-a8ad-6e569a07fc61 | -4.22653 | -44.2693 | 2024-10-09 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f1ded1b-ccdd-3845-b466-e696d5800fe3 | -4.22586 | -44.27377 | 2024-10-09 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README159.md)
