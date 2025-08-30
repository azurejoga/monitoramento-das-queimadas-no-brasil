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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e46801bf-3a31-389a-b138-a8e059a2b91e | -9.17459 | -59.57772 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35628e50-a634-3ea3-89ed-df44d03c3054 | -8.1789 | -61.37034 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aacd2699-7358-3207-b7c8-ce10a57c5cea | -8.90589 | -62.10723 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7db5fcf5-adb8-39d9-b299-227f8791a1a7 | -8.59417 | -60.58141 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53814e55-7b28-3419-b83f-3fbee836938d | -9.15167 | -59.55938 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b4330e1-ff45-3997-9ad5-5aee8d79cfb0 | -9.44224 | -62.36055 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 031c03b5-2627-32a8-a0a5-186937344692 | -8.83476 | -70.66988 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35b33a53-2b79-31a5-ac4c-be4680da1fe3 | -9.80844 | -61.19989 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c99471aa-a0d3-35f6-8a61-7b6c11d9acc0 | -9.44068 | -62.37269 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fe90778-338b-3e00-bd82-b5b9842eb468 | -9.17655 | -65.79634 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68aaaf0f-7492-3edb-8af4-79770c03b5a0 | -9.46465 | -62.34825 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0aaef05f-7239-336c-a1fa-27852480050a | -9.44852 | -62.3522 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 86c11785-f384-3baa-9afc-7a6176e7fca8 | -10.15741 | -68.80532 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b5ce4d-5f50-3a95-a406-d34dafabd22b | -9.13728 | -65.81226 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f07b95df-f4ef-355a-9f49-89e5c93ae2c2 | -9.44103 | -62.32926 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 51e87301-f92c-3b27-9d4b-b42b67b26d77 | -8.70192 | -64.21035 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 634f1799-a41f-3608-b1a9-7b2fb9ee13de | -8.67188 | -62.43944 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03a77763-525c-386b-ab8c-174ac516ef5d | -9.11864 | -65.74056 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9251f7db-e06e-35ad-b6b1-cb820b4c188c | -9.43839 | -60.55025 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7da778d6-8191-3b34-805c-845c04166029 | -9.77274 | -64.25768 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18c7acba-fc4e-3b2d-adab-8ed39cbc0e90 | -9.4494 | -60.55616 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9545707d-1cbb-3241-b0dd-32675b613b87 | -9.06907 | -65.44292 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 65d4b7d2-2e61-3907-b4b6-a6e8c1b4227f | -10.24003 | -68.09505 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 595a5cb1-a645-3953-acd6-3c3b889949c9 | -8.81492 | -69.29841 | 2025-08-30 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74785a56-5b69-3cea-81ac-ea2a29764f07 | -9.24388 | -59.77856 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4446e59f-31d3-3174-8df4-6df624222460 | -8.6264 | -67.24679 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| acadc93a-98c2-37a6-9142-2ff2d165a5af | -9.12521 | -65.81052 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bce0be02-a102-3b80-a566-09b41f8a8963 | -6.98766 | -63.0136 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aa768ec4-3d8e-3abe-902a-a3107d0c565d | -9.13626 | -65.81938 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0f92bd29-a612-3143-8dba-5362772eba7e | -10.48649 | -57.95427 | 2025-08-30 06:01:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dd0a00f9-877d-3a23-9723-71cfccc3a467 | -9.45597 | -62.33472 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 68a5996e-a66c-3fe8-bb35-32019ad889d2 | -9.45718 | -62.32531 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 11.8 |
| d4a1ada4-b0d0-3d84-addd-af833c132568 | -9.45206 | -62.36511 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be3796cc-b5df-308a-9992-0a704f8e6ebd | -9.03344 | -68.32931 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d38cc78f-702d-32d8-a361-437888b279ec | -10.37548 | -57.82459 | 2025-08-30 06:01:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f6ba354-d3d1-3bd0-bfbe-b04933ab4ccc | -9.1141 | -65.74351 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3f6bb54-0284-3d3e-9e6e-0f31405202c7 | -9.44432 | -60.54352 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8c2f8d0f-31dc-3758-938a-22bda7b925e7 | -9.17731 | -65.56052 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ef3ecb7-9632-35bb-b705-79eeae108fdd | -9.44969 | -62.34307 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 94565afb-79e4-34f3-abd2-96cb55b76a24 | -9.44146 | -62.36662 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de66abfe-251f-323a-a8ef-a2a8259c62ef | -7.35526 | -70.126 | 2025-08-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af06a469-18fe-3262-b72f-a5f4f3f53a1c | -9.41504 | -68.55231 | 2025-08-30 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0114aed-5320-3461-b85c-a33c449316a9 | -9.44617 | -62.3704 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 68fe4153-55ed-34dc-985a-1e3abb053a33 | -7.57665 | -63.04124 | 2025-08-30 06:01:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15a3bed7-54d8-3332-9f77-1f91cefde426 | -9.46146 | -60.55341 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e0753ed-bfc8-332c-92d7-f7b589320a90 | -9.43887 | -62.36325 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3daccf72-87ad-39d9-8111-6d1cafebcda9 | -10.36996 | -59.20258 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f7375b5-31f5-3d3e-9a27-d21e888ca783 | -9.44796 | -60.56062 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f2664e67-4d1a-3cfd-a8cd-46042c5335bb | -9.44901 | -60.55257 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bccfa580-f68c-3291-9df5-61a80b0ece2a | -9.43831 | -62.32895 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 099f2f7a-4af0-3cfc-9eb4-8452107ba6fc | -9.44414 | -60.55122 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ad49b064-d05b-3f1f-9c14-2f8f7e317fa8 | -6.56919 | -69.95253 | 2025-08-30 06:01:00 | NOAA-21 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a68be6f-1c8e-3c38-be4b-dfe00408b49b | -9.44053 | -62.35102 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b9ef10d-575d-323f-bfc5-aa3b20d496e2 | -8.17802 | -61.37715 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53d1e46d-e235-3820-ab30-248552c913e2 | -9.11918 | -65.76597 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| e1c94723-cd65-3c30-ba31-571ec26f77ec | -8.88022 | -60.73363 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce030e9e-24d2-31d0-839c-deea32983c06 | -9.44364 | -60.5553 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cb13e617-c92f-397a-b1c6-42f5e2416a15 | -9.67696 | -65.01911 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 40dce9f9-30df-3e21-bfdd-84d9b6bbebde | -9.44496 | -62.33934 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7a1ca080-2c0c-3891-b486-dc1d70e77238 | -9.43792 | -62.35363 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 82bed741-51fa-3a76-bcab-9f15ca8bb65a | -9.24715 | -60.93031 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d17784c-2a69-3c81-bd6e-7ea973043f32 | -9.44107 | -62.36966 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cfa5da48-a91b-35f1-b014-68861bb3e4b6 | -10.70505 | -69.05865 | 2025-08-30 06:01:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac07a682-0257-36b4-b54a-8b5199a86712 | -9.11565 | -65.79099 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efb44f52-8a7b-389b-b7c2-c65c8a659ae3 | -9.13677 | -65.81581 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1437c472-b011-3bce-9b9a-786e8927eb7c | -9.17459 | -65.78154 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70f8967a-4d26-376e-a6b3-f1d5e91210a2 | -9.21121 | -71.77888 | 2025-08-30 06:01:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bca11078-650e-3bbc-b218-783c37aebd99 | -10.36295 | -59.20706 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f54c203e-06d8-31c4-b7df-41d56b23d18d | -9.43594 | -60.56295 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 46bf60fb-5938-31c3-ad95-71de9591e0b2 | -9.44182 | -62.32311 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4795307-1fe5-32ac-a522-cee0419d8ff4 | -8.29022 | -61.41982 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad89343b-d7cb-3bc5-8001-f59f51c8b639 | -9.18175 | -65.79662 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 149dea29-2ca7-3949-97dc-bea70576dd19 | -8.93067 | -71.27332 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef3a3d3-ecd8-38b5-b60d-f89bd074f8ef | -9.44168 | -60.56382 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 84b6e8fa-84cd-3275-919f-2ab7f7c8a73b | -9.16846 | -59.57708 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f6a545e-52fb-353e-91fd-647032ef9e7e | -9.1519 | -59.55988 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4e538004-dc15-32f4-a433-07c3a0d86496 | -8.59731 | -60.58379 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 11552926-6007-3376-8990-06c255a0790b | -8.66741 | -62.4358 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44807569-d700-3fc5-87c2-06a8add5896d | -8.85474 | -64.1482 | 2025-08-30 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a80cdbbd-7fb3-3a2a-9784-73a838214069 | -8.71855 | -68.68386 | 2025-08-30 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96bb3b1e-22fd-3484-b0d4-8fbf1f4741dc | -8.84841 | -70.62578 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7160bf6-5de8-388f-bba6-dfbe6d654714 | -9.43713 | -62.3598 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81e2c416-5f5a-3b70-bc9c-944cb30eee21 | -8.79309 | -71.02254 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80e732c1-eace-3f3d-860d-b20583c2a612 | -9.07372 | -65.43979 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 89cad634-c9ed-3a42-b2f8-86210da5c789 | -9.71038 | -61.30601 | 2025-08-30 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bc4ba83-b64e-377c-900b-4a470a92c368 | -9.44574 | -62.33321 | 2025-08-30 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2e2f17be-6931-3eea-a3e0-a977b94d7269 | -8.59395 | -69.65733 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f923beae-48c4-3a81-aa28-25bb2a7610f1 | -9.43751 | -60.55075 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 19116e1c-1528-3d2e-9fb4-0061036d9d14 | -8.04278 | -70.09929 | 2025-08-30 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0cb9f3a3-b906-326e-ac01-5cfb64b59d69 | -7.3525 | -70.12202 | 2025-08-30 06:01:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59624a9c-5c34-30cc-a613-a0231b5d71f8 | -9.55643 | -63.2121 | 2025-08-30 06:01:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c7b18723-5b71-3520-bb38-0040371a14ce | -9.59649 | -68.53023 | 2025-08-30 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3cc8095-a04f-30ca-bfab-136c4c150aa4 | -8.53224 | -64.01203 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 010d17cd-7929-3b32-9b38-25e795927690 | -8.17757 | -61.38059 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29a33f96-d764-3181-b1b0-2a5128ad8a48 | -8.28433 | -61.39943 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94bdf4b9-563b-3f32-8db1-e1337be13e77 | -9.4504 | -60.54793 | 2025-08-30 06:01:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4e5a53a3-2dbb-303c-a401-e2a11804ecc6 | -7.54433 | -63.84454 | 2025-08-30 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0941432e-7ffc-3281-af97-9fe145bb41ba | -10.25558 | -64.49924 | 2025-08-30 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c589bf23-3c8a-383e-87ca-91d9dd33f09e | -9.0696 | -65.43918 | 2025-08-30 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 9ce40ce6-507c-3115-a160-d4c7b3442018 | -8.28703 | -61.40236 | 2025-08-30 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README84.md)
