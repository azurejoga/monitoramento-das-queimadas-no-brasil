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
| 5339f934-e3fe-3ea4-aa3b-3d196ec74a8a | -9.0381 | -65.477997 | 2025-09-08 01:14:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e41665f-1b4c-314c-971b-e91dac3ffd0e | -12.1069 | -64.278397 | 2025-09-08 01:14:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35918561-f1bb-3f42-9a07-45341cbbdce4 | -9.1306 | -61.8871 | 2025-09-08 01:14:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 64c3e95f-51d2-3ecd-9013-6fb79232a7d6 | -12.3202 | -57.0457 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99112a98-00d3-3ba2-9184-3d96ac76fa38 | -7.0833 | -61.683899 | 2025-09-08 01:14:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c133fea8-34ff-33d9-8596-c96b140e8d4e | -9.164 | -60.557701 | 2025-09-08 01:14:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9665a09b-5b88-310a-b833-6cc2de2fe4c8 | -9.1289 | -61.8797 | 2025-09-08 01:14:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c4c29046-3c26-34d2-beb1-3711c26214a4 | -22.023001 | -52.3601 | 2025-09-08 01:14:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 37e3430c-9184-33cf-b7e3-3cdbcc2a6014 | -12.3136 | -57.060501 | 2025-09-08 01:14:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1723f98-913f-37ff-a2df-ccb2fb16b5e2 | -9.4624 | -60.4912 | 2025-09-08 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 7af90853-f069-3398-9b04-ae1fae72e10c | -8.8821 | -64.2238 | 2025-09-08 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| fd818897-7f87-38a2-90f7-4e088acb6e69 | -12.948 | -54.7724 | 2025-09-08 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6fc360de-208a-3f65-ac9c-1b4ed94449a4 | -14.5067 | -48.8085 | 2025-09-08 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 838875cd-e314-34b7-9853-4dcbe59f3a09 | -9.453 | -61.8338 | 2025-09-08 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.4 |
| ca6046a1-ff73-3ede-b938-ea63a6d2a474 | -12.9477 | -54.793 | 2025-09-08 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| ddbf7ca9-4366-37bc-aeb4-8caf638d972b | -7.3982 | -61.6536 | 2025-09-08 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 6b92a8f4-f96f-3172-8376-027e1f5a3928 | -11.2831 | -46.4591 | 2025-09-08 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| c0b05fb4-0e4b-3b84-8681-e337464fa650 | -12.6151 | -56.9943 | 2025-09-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f6cdf2e4-362d-365e-9e27-370b933b82c7 | -14.527 | -48.7611 | 2025-09-08 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| c7f84e64-5c30-383c-9771-c8e39566c4b6 | -14.5072 | -48.7863 | 2025-09-08 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 7d56a5de-6c45-3c85-aff5-c923b2f86fc3 | -11.2007 | -54.9992 | 2025-09-08 01:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| d08fbfa7-c690-3fbe-952a-80274968dcb8 | -14.5266 | -48.7833 | 2025-09-08 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 168954be-95c1-3399-894a-151a47301ac8 | -12.6343 | -56.9725 | 2025-09-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 217.2 |
| 7caa1c04-1d49-3799-9d56-5aa42a185dc8 | -3.316 | -48.7134 | 2025-09-08 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f7f31740-d4ba-3e4a-a645-aeef909b0e5d | -9.4531 | -61.8147 | 2025-09-08 01:20:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 94.0 |
| c4b73296-defc-3d88-936f-714f9cbc32b1 | -12.9474 | -54.8135 | 2025-09-08 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f7e08b64-85ad-3a5c-8535-b95edba2f221 | -5.211 | -43.2833 | 2025-09-08 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 5911a7f5-fbdd-3d2f-8b9c-69a77b3c671b | -12.6341 | -56.9926 | 2025-09-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| cf3b362c-9085-3fec-b57e-bb25c0b92c47 | -12.6153 | -56.9742 | 2025-09-08 01:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 191.1 |
| 86d8ac73-e656-3e11-92f5-67aec75a3764 | -14.5262 | -48.8055 | 2025-09-08 01:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 21da0a36-33f0-3df6-8bc2-0d54844b0415 | -7.4168 | -61.6339 | 2025-09-08 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| b10bcf24-6350-3a16-bc51-f012938a20cd | -7.4169 | -61.6149 | 2025-09-08 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2e8c103d-5fa0-3404-8fc4-5c9a310999da | -9.481 | -60.4902 | 2025-09-08 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 4580003e-cfc1-344e-9757-276e34725884 | -7.3984 | -61.6156 | 2025-09-08 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 155.5 |
| e830cb8e-b30f-326e-87f4-7e55fca68290 | -5.8791 | -43.9769 | 2025-09-08 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 05c28532-0942-3d43-a0a6-e763ab928c67 | -10.0495 | -59.3547 | 2025-09-08 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| f08d8b7b-9628-30fe-9204-43707c3275e2 | -7.3983 | -61.6346 | 2025-09-08 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 322.9 |
| 0a7dc1c0-dbc6-302b-8e6d-b739dc51d757 | -12.9474 | -54.8135 | 2025-09-08 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 34c1a9e0-afe7-397d-a31a-aaca49c22ac3 | -12.948 | -54.7724 | 2025-09-08 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 326759b2-cfad-3eb6-a6d3-dd099c0da4ce | -22.3609 | -51.9018 | 2025-09-08 01:30:00 | GOES-19 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.9 |
| 2849d1a1-9753-3b5d-86eb-8651fed64b65 | -9.4345 | -61.8156 | 2025-09-08 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| d526114a-f9e5-3517-8563-bd5f74978900 | -14.5262 | -48.8055 | 2025-09-08 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6e70f7fa-2463-32c7-a048-ef9e64070fb8 | -14.5072 | -48.7863 | 2025-09-08 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 60907544-fcfd-34c8-94bd-7402a8579698 | -12.6151 | -56.9943 | 2025-09-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| e505d880-f4d7-3bcb-b1c8-befd8ee00ec9 | -9.453 | -61.8338 | 2025-09-08 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 35a12d05-686c-3e17-a3d0-b93562f27e77 | -12.6153 | -56.9742 | 2025-09-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 187.5 |
| 115e7db2-81f9-3d9b-8516-d3308531a148 | -5.8791 | -43.9769 | 2025-09-08 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9fdcf78d-a821-358e-909d-605f3ba14763 | -12.6341 | -56.9926 | 2025-09-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 67badd25-a7b1-3335-af88-a32ae14c58bf | -3.316 | -48.7134 | 2025-09-08 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f1db2f20-0a13-3063-b6c1-35972a822d93 | -7.4168 | -61.6339 | 2025-09-08 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 0e9d100f-2412-35a4-8734-eabeb2cc1359 | -10.0495 | -59.3547 | 2025-09-08 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 9ff4c2cc-8b65-328c-9611-cdb5fef1cde3 | -11.2005 | -55.0195 | 2025-09-08 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d0a00818-ef3a-3470-85eb-9a9fefd879db | -12.9477 | -54.793 | 2025-09-08 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| c098ae04-5132-3910-88e5-763af0243742 | -5.211 | -43.2833 | 2025-09-08 01:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 69946665-ec59-3a93-b050-5c8ea2fabb0c | -9.481 | -60.4902 | 2025-09-08 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 31fa07d2-9315-3338-8a75-19631e62c0e9 | -5.8793 | -43.9538 | 2025-09-08 01:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 2d7c1366-2069-3bae-8a45-9b93f216aef6 | -7.3984 | -61.6156 | 2025-09-08 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 6855eb60-2c8c-3258-8266-2ccda27d860d | -14.5266 | -48.7833 | 2025-09-08 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.6 |
| ad6e9e12-d649-357b-aaf9-50b2d0cadbc1 | -9.4531 | -61.8147 | 2025-09-08 01:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 35c24503-021f-3202-8a54-0dc2cf2b47ff | -7.3982 | -61.6536 | 2025-09-08 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 83c0179b-397c-3871-a080-2b725d1edfd0 | -12.6343 | -56.9725 | 2025-09-08 01:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 138907e3-152c-37ef-b4c2-e23a7162d053 | -9.4624 | -60.4912 | 2025-09-08 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a1dfc7df-1f67-3b3b-880e-b27752ff4c7c | -7.3983 | -61.6346 | 2025-09-08 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 294.5 |
| 8f00fdba-a73c-36c9-a364-9c40e680c9b5 | -14.5067 | -48.8085 | 2025-09-08 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 184.2 |
| ac2fe629-ece1-3e30-9026-f6b5f39bd9ef | -11.2007 | -54.9992 | 2025-09-08 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f98457be-15f4-3fcb-9305-3e6373b4e951 | -14.527 | -48.7611 | 2025-09-08 01:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| da3a74c4-c7c2-3fea-b5d5-88999acdd848 | -12.6153 | -56.9742 | 2025-09-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 9f332752-181b-3ffe-a3a7-d5c97f525984 | -12.9477 | -54.793 | 2025-09-08 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.3 |
| aa7cb0bd-bc42-37bd-8779-a23c420517a7 | -12.6151 | -56.9943 | 2025-09-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ee74935b-5ced-3199-a473-3a404b5c30a5 | -12.6343 | -56.9725 | 2025-09-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 2d622df3-1c2f-3303-b23d-55d8bbefec7e | -3.316 | -48.7134 | 2025-09-08 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d5434c4c-69e3-394e-9e7c-e4ada835d0b1 | -14.5067 | -48.8085 | 2025-09-08 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 209.5 |
| fc19a76f-9fef-3d77-a302-3c8ca2a89b80 | -14.5072 | -48.7863 | 2025-09-08 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 135.6 |
| 6428d07d-6e98-3146-aa7d-0c9ac0023133 | -6.167 | -47.3078 | 2025-09-08 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| acbc1e8b-e55b-389a-91f0-5854f31bfa18 | -7.3984 | -61.6156 | 2025-09-08 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 991cc40f-14d6-34d8-9bc4-1bd3511df404 | -14.5262 | -48.8055 | 2025-09-08 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| c0d4229c-f959-39ce-abab-dec5ac008368 | -8.8821 | -64.2238 | 2025-09-08 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 26214daa-9bee-3ce4-85d0-1ce74c170890 | -6.1297 | -47.3103 | 2025-09-08 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| bbb77d5f-5316-3dc9-bf7d-3192e7f6598b | -11.2007 | -54.9992 | 2025-09-08 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 77201166-62ad-3d08-89b6-677a10596fb6 | -11.3745 | -50.3997 | 2025-09-08 01:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| f01e0c21-1010-3eed-a967-263252c551c9 | -12.6341 | -56.9926 | 2025-09-08 01:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ad9e055a-4aa9-36ce-be96-d1dc981ad324 | -7.3983 | -61.6346 | 2025-09-08 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 223.8 |
| e5f8ff6e-2a2d-390f-ad2f-80aaeebf4308 | -6.1483 | -47.3091 | 2025-09-08 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 411.4 |
| f56895d3-8a79-3996-8929-34100ad0c1f5 | -6.1485 | -47.2871 | 2025-09-08 01:40:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 950e8793-e55b-323e-82b4-3b8ff6e844d7 | -9.4531 | -61.8147 | 2025-09-08 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 1fd3359c-07be-3fff-adc1-303b154c66d2 | -12.948 | -54.7724 | 2025-09-08 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2c9ea897-36bb-3a76-bc20-2d1aae7a8ee0 | -17.1564 | -44.4266 | 2025-09-08 01:40:00 | GOES-19 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| c97f543b-5e82-3e31-8998-f5f24050bda0 | -7.4168 | -61.6339 | 2025-09-08 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 85fa8a3b-d7d7-3f55-8f5b-3a64761055f7 | -9.4345 | -61.8156 | 2025-09-08 01:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 360ec9e1-6095-300b-9f0a-c4703f147312 | -5.8791 | -43.9769 | 2025-09-08 01:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9e9afbe0-0d50-3358-bb0e-3a24c7fe1f82 | -7.3982 | -61.6536 | 2025-09-08 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| f6df9ee7-6b41-3465-ac0b-58885abf8191 | -9.481 | -60.4902 | 2025-09-08 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 7b29c96a-2604-3e53-ac58-24973f63e9f6 | -14.5266 | -48.7833 | 2025-09-08 01:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.0 |
| f1f2c246-a274-3675-b0f0-5214260c9f1f | -12.6341 | -56.9926 | 2025-09-08 01:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e1c21804-8bba-3662-a650-5ccc746dc26e | -3.316 | -48.7134 | 2025-09-08 01:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 44c0ef5a-b9e9-3525-b1ba-3304fa43f89a | -7.4169 | -61.6149 | 2025-09-08 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5d9685fe-6c66-3235-8423-e15073adbcf1 | -11.3742 | -50.4212 | 2025-09-08 01:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0a8f2779-0776-3c3c-b9b5-2190c4f6b9de | -12.9477 | -54.793 | 2025-09-08 01:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 09832432-3745-3c70-973c-2710d144ecd6 | -22.3401 | -51.9062 | 2025-09-08 01:50:00 | GOES-19 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| a9260cc1-00c5-38af-83fa-849ca7725cd1 | -7.3983 | -61.6346 | 2025-09-08 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 169.6 |


[Clique aqui para ver as próximas entradas](README16.md)
