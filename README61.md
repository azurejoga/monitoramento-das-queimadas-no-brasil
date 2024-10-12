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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2bfb9a6e-a3e5-3047-9eb6-cddef45d86ee | -7.87654 | -54.71548 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| cda50544-7d8e-39f3-8c0e-fda9c4f830b3 | -7.876 | -54.71894 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83184153-97ea-3726-b28c-afc717da9f76 | -7.87545 | -54.7224 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3ee5994a-96a5-3548-b3e7-0944955cc487 | -7.87487 | -54.70459 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e4eeea7e-aa87-3a38-bfdc-f9693e330a43 | -7.87433 | -54.70805 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7ad6e67-89b3-30bb-a60f-e9fb308d0cb9 | -7.87379 | -54.71151 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| c9d2d8e0-890c-32b2-a60b-80f8691c97cd | -7.87324 | -54.71496 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| af93e5b5-cbab-3f25-bbe3-3a95c614dced | -7.87321 | -54.69371 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 366e145d-892a-3739-9e22-6651810f3f39 | -7.8727 | -54.71842 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ccb639f8-a338-3bf0-9123-96fbaaa0610e | -7.87266 | -54.69716 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 41733862-8ce3-38bf-925f-4c444b55884a | -7.87212 | -54.70062 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 49e3eaa4-47c9-3271-9d7d-dc62d5488345 | -7.87157 | -54.70407 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 52fdd5e9-7e0d-3dc3-ae27-58798146a650 | -7.87123 | -54.89918 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b882a0ed-b97f-3f4c-a806-bf06cf66dcd4 | -7.87103 | -54.70753 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4fc4627-351d-3795-97dc-a22d2fbfc402 | -7.87049 | -54.71098 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| afc4aa59-d554-3929-a0c0-19855a479f15 | -7.87045 | -54.68973 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1be0309a-baee-34d2-8ce9-008f93adf406 | -7.86994 | -54.71444 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 36e211a3-eb9a-37c6-aa85-0b0eb58cd617 | -7.86991 | -54.69318 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80f3b39f-bed0-3337-b2e5-ae529905f786 | -7.8694 | -54.7179 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c6c4b8-1ae0-326c-8e26-ed72f0fee528 | -7.86936 | -54.69664 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e6273745-e248-317c-b98c-9db71ace59ff | -7.86882 | -54.7001 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aa6febcb-e893-3128-a7dd-ef2396a1290a | -7.86828 | -54.70355 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3b4eb569-e7a0-3b8b-b6e3-f351ffd790f6 | -7.86773 | -54.70701 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 49982ed6-5f35-3a8e-952b-c1ccda742c48 | -7.86719 | -54.71046 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3e02deb5-0633-30f2-9f97-dcf7d2a4556a | -7.86664 | -54.71392 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 99c0411d-5bc4-3790-be06-3045e1384688 | -7.86639 | -54.68911 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| edc3c94b-8b81-3707-a687-ad91e13263e3 | -7.86584 | -54.69257 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 79947562-85d9-39e8-844d-5e95089623fa | -7.8653 | -54.69602 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e6606604-c130-3e25-a7d7-f8a87fef6d78 | -7.86476 | -54.69947 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 29f95948-2ab3-3d4b-b9f2-59aa3180beb4 | -7.86421 | -54.70293 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d2468c4-ed46-398d-92f4-b60880d1c87b | -7.86367 | -54.70638 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1837a988-853d-3f74-bdf2-7436520a85f4 | -7.86309 | -54.68859 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 687a1b5b-1768-3439-a8c4-5d03b1a9f676 | -7.86254 | -54.69205 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 320a33ab-08b3-3fda-9aec-e571aca7904f | -7.862 | -54.69551 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8814b58-def9-3506-856d-159b77c7dba8 | -7.86146 | -54.69896 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4ac6be7c-56ea-3af3-84d6-d84bc1036449 | -7.86091 | -54.7024 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 720cc28b-7524-3825-9127-c0b7930815c8 | -7.86037 | -54.70586 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f592b951-688d-3f20-8ef4-23c39b5a091d | -7.85925 | -54.69152 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3c25425d-0436-364f-a3c0-fe509d201eb5 | -7.8587 | -54.69498 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 48a26ce4-6ed7-3c2f-8ee5-4531460520b1 | -7.85857 | -54.89362 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28d6a5f7-1169-3789-88eb-8ea8b05c1380 | -7.85816 | -54.69844 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cc2cdc93-4103-3842-af9f-95f6ceaef502 | -7.85582 | -54.88963 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3df3d87f-aa39-357d-b776-e42fa39d17b6 | -7.85527 | -54.8931 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96abf5a1-6dba-3e3c-9a8f-ddc50cee78d2 | -7.85142 | -54.89605 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6992eaa-01c4-36d8-86f7-8672f6f81812 | -7.84811 | -54.89552 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78bf2845-d514-3eee-ac51-2b4fa8982505 | -7.84481 | -54.895 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfa34712-4cb6-3cf6-9f4f-b42275b4bd9a | -7.84151 | -54.89448 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a08137ce-a2c8-307f-810c-6a9494fd19fe | -7.84096 | -54.89795 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2dbe1f62-e1a0-332b-8931-d6cab5030109 | -7.84041 | -54.90141 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06406876-da93-39bf-8d04-3990d7448f5a | -7.83986 | -54.90488 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a39a918-cbc7-3bcb-b4ed-362845fbaba2 | -7.83072 | -54.72243 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e1c4ac32-8f1f-3558-bb6d-95d7252cf6bb | -7.83017 | -54.72589 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb4df2a4-7f68-3c62-a64a-ac16f4de7d32 | -7.82963 | -54.72935 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f46622c-71e3-3da3-8f3f-0afef24357b1 | -7.82742 | -54.7219 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 169b5e5d-1756-3fbb-9609-f510579a1967 | -7.82688 | -54.72536 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a304279f-1876-3154-aabe-2f061b287db3 | -7.82633 | -54.72883 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8585932b-0b93-39d0-be24-ff904fc23e16 | -7.82303 | -54.7283 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c143249e-fb22-39a1-93f5-7cff180e1540 | -7.81093 | -54.71928 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 21534b8b-be8b-3efa-a805-4e8c34e56304 | -7.80709 | -54.72222 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 02b747ad-7829-3764-b744-2462a28ec2de | -7.73674 | -54.77846 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d4afe6d-9a1e-32a8-a04c-4be1e3c49f95 | -7.6263 | -54.96343 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 860293da-d992-326f-880e-63300cf13075 | -7.59168 | -54.96452 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e863a42d-8158-361b-939f-c956c58da61c | -7.34272 | -54.81842 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c1e69579-be44-36f1-b1c2-a4db6d8b8c64 | -7.33942 | -54.8179 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc94eab1-87f0-3b0f-97a0-94bc57e6b8ad | -6.88878 | -55.14825 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1a9dd182-275e-31b0-a5de-6513ac7dec8b | -8.23049 | -55.23174 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bac945aa-c7c6-3ea9-8d78-ec42e364c986 | -8.14026 | -55.17767 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f541e52d-d710-315c-bc2c-820eef6961f8 | -8.13971 | -55.18114 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56afc175-bcef-372d-9d3e-ed12d625f1c2 | -8.1364 | -55.18062 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71f2d054-7aba-3839-a208-5b9e6828a457 | -8.11344 | -55.08778 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7be0fc40-e12a-38c9-9e1f-2c6753eea216 | -8.11069 | -55.08378 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ff84a05-9fa1-3c0b-81a7-2ffd120f222b | -8.11014 | -55.08726 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19adc281-1a93-325e-bb8e-efc1f46b213e | -8.09068 | -54.84592 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 852ef736-488c-35f8-9c17-e7c3ddfe07a1 | -8.09014 | -54.84938 | 2024-10-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee648132-0f15-3bad-b8ed-73378e4ffefe | -1.76586 | -55.15454 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a6e4202-a4d6-3328-8cdc-d7641a26f8ef | -1.75545 | -55.3327 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6366daf-45d7-3d78-be77-6d68e8c37010 | -1.7551 | -55.13387 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f2545b5-ffde-38ea-a128-013b55065637 | -1.71913 | -55.13969 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81b4ab64-6720-38ff-920c-251b8ac2a8a3 | -1.67031 | -55.1363 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f33451bd-1c80-3676-b372-6a3122385771 | -1.66973 | -55.14 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 730fc281-7710-37b4-80d1-5a317e8466a8 | -1.66689 | -55.13578 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 650341b7-ad42-3577-914f-1d4365bdba07 | -1.66631 | -55.13948 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6eb9eb43-1628-3dad-878a-eda4a1cbbded | -1.6619 | -55.45405 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1c699de-3122-3188-bd39-39f949475f46 | -1.65126 | -55.1905 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8d72cab-1a9f-313a-90a3-8cfec7a33a37 | -1.63325 | -55.12677 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e74553df-969b-3615-8902-26721396f812 | -1.62902 | -55.1756 | 2024-10-12 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66450d99-3168-3736-a734-c7f2ae48784e | -1.53955 | -55.41195 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54210455-e4be-3749-a96d-b406a2685d37 | -1.53896 | -55.41576 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd482540-a5bf-3e74-93a1-4268e0a33d65 | -1.53143 | -55.41852 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d3e53350-13d7-31ac-9145-368887ab6ae7 | -1.53084 | -55.42233 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3289b9ce-8428-3193-81e2-acdc2d5af8b2 | -1.52797 | -55.41799 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdd0cf80-bcc6-3b87-9b26-84af99e8138b | -1.50823 | -55.86903 | 2024-10-12 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37347fd8-b7c1-3101-bc9e-0aa03d460e96 | -1.50469 | -55.8685 | 2024-10-12 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e59cb6d7-22c5-39bb-a978-205d546e16bc | -1.20843 | -55.86132 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 736d87f8-1a8c-377d-be78-d31b7cf198c1 | -1.2049 | -55.86069 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c38300a2-e64f-3ebb-9563-f14b1b53bb35 | -1.20136 | -55.8601 | 2024-10-12 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3daa7b52-7fda-307d-a59b-fcc09c7ed5b5 | -3.60387 | -55.45766 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7cc3cd59-3cf4-337c-8ef2-316310b54c0c | -3.60046 | -55.45711 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 201d7f95-256b-3840-bf07-2f01a9d337e4 | -3.59988 | -55.46079 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 55d8a18c-f869-3c96-a85f-2b87d5f6d4fc | -3.59706 | -55.45657 | 2024-10-12 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README62.md)
