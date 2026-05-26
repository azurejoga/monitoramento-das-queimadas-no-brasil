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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a3783e4-a3d0-37a8-87dc-909e2de66c47 | -5.7937 | -45.1493 | 2026-05-26 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 145.1 |
| e6ed737d-a530-3ee6-b985-45d0015c46b3 | -8.6304 | -45.0314 | 2026-05-26 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 206707d2-2f0d-393f-a615-94b9a141b009 | -7.1352 | -44.0785 | 2026-05-26 12:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 388.4 |
| a2b8a5b8-6b81-3c8a-b96f-39aa5753ec89 | -11.3584 | -52.9514 | 2026-05-26 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| d20ec41d-20b1-3289-a9d1-4dd7e2cc73b7 | -10.628 | -42.2928 | 2026-05-26 12:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 247.3 |
| 54597cf3-8122-3d4e-b09e-7f9598a5f73d | -5.7941 | -45.104 | 2026-05-26 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 211.9 |
| b8e850cc-91dc-3636-accb-728430d41cb2 | -5.7752 | -45.128 | 2026-05-26 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| a709dfe3-2d12-35e7-9f36-73574153d71a | -10.6471 | -42.29 | 2026-05-26 12:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 180.5 |
| 8fe1a004-01fa-3c2c-8f14-da1a389ff0c0 | -5.7939 | -45.1267 | 2026-05-26 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 538.8 |
| 7e1008f9-94cb-3d26-81b6-d50fb8ca9bab | -7.1541 | -44.0767 | 2026-05-26 12:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| efbab526-0c0a-3c73-98d1-4b82dbf75dbe | -8.6304 | -45.0314 | 2026-05-26 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.5 |
| cc7ff0ee-6544-37bc-9c5c-79e247f33760 | -5.7937 | -45.1493 | 2026-05-26 12:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a7fc52b5-b853-3dd2-9fc6-c4b0fb64a923 | -7.1355 | -44.0553 | 2026-05-26 12:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 295.6 |
| 88bd87a0-ee19-3027-bf9e-64e12084c658 | -7.1543 | -44.0536 | 2026-05-26 12:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |
| eef6a6a6-26a1-3b9b-b14d-4ac7984a9098 | -8.6304 | -45.0314 | 2026-05-26 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 206.9 |
| f0f9977e-dfba-38e9-af02-f29d15d33001 | -7.1543 | -44.0536 | 2026-05-26 12:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 6e98ca6b-b1af-301d-babd-1ab5c9a9e8b6 | -10.6471 | -42.29 | 2026-05-26 12:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 204.4 |
| 7ea5bc43-6acd-39f6-9518-845d0a95ed9a | -5.7937 | -45.1493 | 2026-05-26 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c5a70b46-5a6b-3676-8468-b1e166458081 | -5.7752 | -45.128 | 2026-05-26 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9c1f1679-f552-331d-8914-897f85d9e2d2 | -11.3584 | -52.9514 | 2026-05-26 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.3 |
| 221edd7b-aba1-3e74-914c-8c16273178cd | -7.1352 | -44.0785 | 2026-05-26 12:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 316.0 |
| f2bd8456-9bbf-3449-b03d-4e69c2e92b79 | -5.7941 | -45.104 | 2026-05-26 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 246.0 |
| ee9a869b-ca4a-3a03-be1c-769828eba004 | -8.6307 | -45.0085 | 2026-05-26 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| c172f33c-b49b-3eac-a51f-2aabd0784ef0 | -7.1541 | -44.0767 | 2026-05-26 12:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 43b49068-7b51-3a68-8ad3-db3c254280f9 | -7.1355 | -44.0553 | 2026-05-26 12:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 304.9 |
| 60e64544-f0d9-3a91-8d4d-277cbe1ac8dd | -5.7939 | -45.1267 | 2026-05-26 12:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 497.8 |
| 98820e97-065b-3b1e-807d-040f0044a526 | -8.52894 | -51.5719 | 2026-05-26 12:53:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 31c7b7cb-99c5-3628-b0e0-5f1319c2e399 | -11.27361 | -53.9545 | 2026-05-26 12:55:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 945f8b3e-671a-3b57-be6a-e6351ec44ce3 | -11.55227 | -56.9342 | 2026-05-26 12:55:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 624d486b-3534-3ba8-a3ec-23427d53e4a9 | -11.36381 | -52.92745 | 2026-05-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 6a421a34-7723-3b39-b0f9-77da967d952b | -11.35438 | -52.95662 | 2026-05-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 219.4 |
| 6618583e-6345-33ee-b360-49afcb9a5855 | -12.54086 | -57.2188 | 2026-05-26 12:55:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| b80881f2-89cd-351a-8593-484963a3a516 | -11.18139 | -55.91753 | 2026-05-26 12:55:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 2fcfc659-6b30-3fdd-ac80-f05f0017f182 | -10.30788 | -58.91776 | 2026-05-26 12:55:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 0ba6f368-f676-3b4f-abed-ac3cafc71c89 | -10.30547 | -58.924 | 2026-05-26 12:55:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1d99718e-aa4a-3062-a2f8-921854cf2bd0 | -10.71163 | -56.24166 | 2026-05-26 12:55:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 199cc289-5d9c-393f-9d30-b3f1d6a6bcfc | -11.56051 | -56.33953 | 2026-05-26 12:55:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 01316bd4-c29d-328d-8928-d7124c45b46b | -10.67063 | -58.95393 | 2026-05-26 12:55:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b2b51224-b9a7-3334-a9a6-f865a9047494 | -11.73791 | -54.79622 | 2026-05-26 12:55:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 2ffcda0e-6467-3e11-81fb-b65c92a34ebd | -10.30625 | -58.92985 | 2026-05-26 12:55:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| a650df9e-dbba-3095-9f2a-1419561a137d | -10.668 | -58.96002 | 2026-05-26 12:55:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fa0df379-2ff8-36c8-b8bb-f65b620113f6 | -11.35999 | -52.96433 | 2026-05-26 12:55:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 171.6 |
| 5d5a8649-78d8-3206-a76a-6964b6201144 | -11.56046 | -56.34621 | 2026-05-26 12:55:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 28.1 |
| fddd931c-8fba-3ca5-92a1-29bd6fe6ba53 | -10.31568 | -58.92529 | 2026-05-26 12:55:00 | TERRA_M-T | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bc493e46-cbae-32c4-bdfc-d1ee875a1f2c | -10.6471 | -42.29 | 2026-05-26 13:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 180.7 |
| 2bf9e23d-ff64-324f-b7bc-c9844b249393 | -10.2962 | -58.9299 | 2026-05-26 13:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 0764d324-5417-39c5-8be0-b39a6c0652ff | -5.7939 | -45.1267 | 2026-05-26 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 361.4 |
| d2fef7da-6917-38d1-b8c9-52d4a9627ca5 | -8.6304 | -45.0314 | 2026-05-26 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 96c8f360-e962-3343-b392-8452a69bc97c | -5.7937 | -45.1493 | 2026-05-26 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 82c20a54-bb38-3687-89a0-992671b15226 | -7.1352 | -44.0785 | 2026-05-26 13:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 323.9 |
| 7180b065-4319-39ab-aed0-e26a1904da21 | -5.7941 | -45.104 | 2026-05-26 13:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 180.6 |
| fa6ddef5-cac1-33df-bbec-79f33db7daa2 | -7.1355 | -44.0553 | 2026-05-26 13:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 302.0 |
| 3280f7f3-a271-3fb9-bd32-fb5aac83450a | -11.3584 | -52.9514 | 2026-05-26 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 150.7 |
| 82c5bd5f-bbbf-3fc9-ba5c-f9d7b0e33317 | -8.6307 | -45.0085 | 2026-05-26 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 0c6185fa-5bff-343c-8612-946391e013cd | -5.7941 | -45.104 | 2026-05-26 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 198.5 |
| f1b93036-123d-3db5-9b15-eef04d72af7e | -8.6304 | -45.0314 | 2026-05-26 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 102.7 |
| ae37405a-a1c2-340f-b252-8f5c4913626c | -7.1541 | -44.0767 | 2026-05-26 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 7e5f1837-f1e6-31c0-858c-0e8bc76b785a | -10.2962 | -58.9299 | 2026-05-26 13:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 568.1 |
| 3046d7c8-293c-326d-bba8-29d2e7bb6cee | -7.1543 | -44.0536 | 2026-05-26 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 10035c93-d725-35cf-a7fc-76a5cbf6f698 | -7.1352 | -44.0785 | 2026-05-26 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 260.3 |
| e1757788-81d0-32cb-bf4f-6826f5a99448 | -7.1355 | -44.0553 | 2026-05-26 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 252.5 |
| a717638c-6715-3de6-a619-742e8af59a6b | -11.3584 | -52.9514 | 2026-05-26 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| a6f9d02d-ae07-3a0b-b04d-d81b33ebf7ce | -5.7939 | -45.1267 | 2026-05-26 13:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 447.3 |
| 4c5d0fda-5e49-3e5b-b799-39e64d74dfc8 | -5.7941 | -45.104 | 2026-05-26 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 205.9 |
| d79a54ca-07ee-3192-a3b5-ac52025fbb12 | -5.7939 | -45.1267 | 2026-05-26 13:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 457.2 |
| dd453cb9-fd65-3331-b4d7-d40affaf9067 | -7.1541 | -44.0767 | 2026-05-26 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 122b2bfe-cca5-3135-9072-b3b09a5a51f4 | -7.1543 | -44.0536 | 2026-05-26 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7c2b0358-a4a8-3271-a0ef-e3524312d10f | -7.1352 | -44.0785 | 2026-05-26 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 66bfedf3-bb1c-3a22-b792-6251740f98ad | -7.1355 | -44.0553 | 2026-05-26 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 3f057ed9-59ee-3cff-9cbc-232b47bd1e9c | -10.2962 | -58.9299 | 2026-05-26 13:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 92eaf8ba-3530-3a18-9ec3-a4cb63285ea0 | -7.8194 | -42.0333 | 2026-05-26 13:30:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 78.2 |
| d89aad89-1f0f-3057-b6d2-725cf404df46 | -10.2962 | -58.9299 | 2026-05-26 13:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 3e54d458-1f76-36f5-a9a9-a205927496ec | -7.1352 | -44.0785 | 2026-05-26 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 233.0 |
| be4eba08-fa11-3049-8834-246c8d536a7d | -5.7752 | -45.128 | 2026-05-26 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 020c35d6-6acd-38a6-88ef-812a4c8de5f9 | -5.7939 | -45.1267 | 2026-05-26 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 383.1 |
| fe1a7a8f-1820-399e-8865-a79fc029029a | -7.1543 | -44.0536 | 2026-05-26 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 21ca55ef-9678-3153-ac1e-95682d98cd6f | -7.1541 | -44.0767 | 2026-05-26 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| cea5c23c-2b3b-38f7-96d7-a1a76d2fcef4 | -5.7941 | -45.104 | 2026-05-26 13:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 6f617cc8-3a20-3be4-ba16-fb249204e06f | -11.3413 | -51.4029 | 2026-05-26 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9d74f49e-1094-37b2-99df-1eb77d3c8843 | -7.1355 | -44.0553 | 2026-05-26 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 175.4 |
| 0af7976d-1301-3673-a2f9-2a7197846b46 | -5.7752 | -45.128 | 2026-05-26 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ad068b06-ddcf-353e-bcfe-74b6266874d5 | -14.0327 | -46.3423 | 2026-05-26 13:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 26752e99-072f-33de-82d5-de9874ec83d5 | -5.7939 | -45.1267 | 2026-05-26 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 281.8 |
| 56a22892-77db-317f-86d7-d918c8c3e5de | -10.2962 | -58.9299 | 2026-05-26 13:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 187.6 |
| b2075a12-208c-378e-a313-0d8a714957ee | -7.1355 | -44.0553 | 2026-05-26 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 188.3 |
| 01e9cb08-31af-380b-95c7-5455890d0739 | -5.7941 | -45.104 | 2026-05-26 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 133.6 |
| c95a6f5e-c93b-3e07-a75a-f9b366c03f50 | -7.1352 | -44.0785 | 2026-05-26 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 217.4 |
| aa6cf2b4-477e-3e70-a281-afffc9220fcc | -14.0327 | -46.3423 | 2026-05-26 13:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 18026957-4d52-3f92-bc31-966f4e481132 | -7.1543 | -44.0536 | 2026-05-26 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 71.3 |
| dba864ce-aeb2-3155-91ae-dc4faef4dbae | -7.1352 | -44.0785 | 2026-05-26 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 27372007-dc57-3a07-a133-823ef5972983 | -7.8194 | -42.0333 | 2026-05-26 13:50:00 | GOES-19 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 88.9 |
| 0dd5bd1c-03f3-39c5-8ae0-4f4525b163c4 | -7.1355 | -44.0553 | 2026-05-26 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 70d99c4b-a9d8-350f-b803-88df9ad097f2 | -5.7941 | -45.104 | 2026-05-26 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 3aeb289f-4b9b-31a5-a35f-db795d1acc67 | -5.7939 | -45.1267 | 2026-05-26 13:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 295.9 |
| d4cd6f09-a300-32fe-ae0d-e2396cb4b780 | -7.1543 | -44.0536 | 2026-05-26 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| dff475a2-009b-392f-a26d-d496bfed20e1 | -7.1541 | -44.0767 | 2026-05-26 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 37cb2eb3-73fb-33c3-a3cb-d3d8cf488029 | -7.1352 | -44.0785 | 2026-05-26 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 145.4 |
| 2c553ca5-15e3-3475-88e0-b98ec7523472 | -7.1355 | -44.0553 | 2026-05-26 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| 135e8a60-b647-3818-881d-5b50b6f05d46 | -5.7941 | -45.104 | 2026-05-26 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 36d0860e-3918-3979-8c46-12e01602c2fb | -14.0327 | -46.3423 | 2026-05-26 14:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |


[Clique aqui para ver as próximas entradas](README16.md)
