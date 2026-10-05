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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13b966c7-5013-3849-a846-da91f00c89a2 | -8.62607 | -69.49816 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60ee6940-f982-3e77-b5ba-2feada2fe19f | -7.65949 | -67.16051 | 2026-10-05 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c25fefb5-b4ae-3c4a-9026-7f43e11ac861 | -7.4413 | -63.56796 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 369908cc-28ca-36c5-9ede-ce32da0e0257 | -8.87742 | -66.64968 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cec7af78-ffe8-35b6-9b4a-c96aca29faad | -9.16144 | -68.24574 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98e10a85-5ae0-3603-b926-a1bbdb1016e8 | -8.34849 | -62.82949 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2edcc63c-2765-3da1-952c-19a7416f93fc | -12.1578 | -60.74817 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d14335c8-687b-328f-98f0-0fa1ab2d0bfc | -9.10625 | -67.82395 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6db3f0a1-f004-3bcf-8bf2-1c0bb43a762b | -8.65763 | -54.55319 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7ccb58c-08b1-36a5-866f-268df7c1235e | -8.35208 | -62.83004 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea59e993-f43a-34b4-beda-0ad311deb5df | -10.8816 | -57.09182 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2acf157b-b116-3674-b40e-da619d96ccb9 | -10.11651 | -68.07826 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a00ddde2-aa8d-39db-9566-fc3639ba2878 | -8.04955 | -72.43339 | 2026-10-05 05:44:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eaa31197-2a0a-353b-b417-0f6b2d25b6bb | -9.16864 | -68.26633 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62b6d12e-4fd1-38b2-9564-aab96b9d2296 | -9.11127 | -67.83605 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf8f2261-a97d-3fcc-bd92-b095ec9ea51f | -7.43786 | -63.56742 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58841a8f-de04-37ba-ac63-f79dc088026b | -9.22954 | -67.89305 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f42c8adf-6efb-3de6-94ca-d2acd0d6bf9e | -7.44991 | -63.55764 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7bc63a18-a7a1-3443-b754-911bc20b6b7d | -9.06167 | -67.73402 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56a20d39-6011-35c3-b585-85d62a210aa2 | -7.43555 | -63.55931 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c1976c5-f6a3-3d38-aece-78acabbef38d | -7.68079 | -69.93402 | 2026-10-05 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b704137-e7cb-3b9b-97cc-9a0ccdeb9055 | -7.43097 | -63.56637 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b02054c7-a597-3120-80e5-529409d1505e | -9.03684 | -67.55491 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17cc646b-8b76-3774-a175-bceb01383f11 | -9.14154 | -67.9359 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdcbac25-77a1-3904-bcf6-aade4cb52ca2 | -10.62208 | -67.9236 | 2026-10-05 05:44:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 299d7d50-ca2c-3e7e-97d5-33a5b32f8a39 | -7.65892 | -67.1641 | 2026-10-05 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6031b768-9a5e-307a-966c-a9eb089bd5a3 | -8.57003 | -66.9996 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32ed32cf-7dc7-3039-b9c2-a8e928088059 | -12.87877 | -61.72118 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d8100bd-91c2-36c1-ad42-7dcff49620ef | -9.3395 | -64.71882 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3effaca-a3c7-30bb-9a0b-b436d30b46fb | -10.88115 | -57.0953 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c413d276-0306-3b3d-9f72-5207c50bd92c | -9.44869 | -68.57387 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f273d89b-e55e-3cb5-b906-dd4c07de8c56 | -8.3449 | -62.82896 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03443573-37bc-3b23-8149-b4ee6207f98c | -12.88382 | -61.71441 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ea589e5-7cd9-3059-ae6b-2c9b1369d8f8 | -9.15426 | -65.39621 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6e5db54-6f5f-384f-9b99-b646da405019 | -8.52746 | -54.59781 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9ea2b92d-58e8-3482-acb4-daef94af188d | -9.02954 | -67.55744 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2db65f0c-176b-31ec-be33-52989d7b064b | -7.41715 | -64.66483 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 284536e1-d4ba-395b-8cf3-106c0bc6549f | -8.35816 | -62.81397 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b1f09a66-308a-3daf-8869-33b2baf0024c | -7.43498 | -63.56311 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a00ddfd8-ee68-3b87-981e-c9d76870bb49 | -9.55002 | -68.64179 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25f972e3-7feb-3e2b-8809-56c7cbbc75e8 | -7.43843 | -63.56363 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 30150964-f3ee-3102-bf3d-5e04c60ef3ff | -9.11339 | -65.397 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60cfc75f-37d9-39a2-9996-33dca50b07b2 | -10.85497 | -68.22855 | 2026-10-05 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2484b609-7ab2-39de-9ee1-ad64e288db0c | -8.84348 | -63.75439 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08b1aa15-ae68-3108-b5b3-c5f1b1efe8b3 | -8.35864 | -62.83527 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66e00881-7f86-37ba-87d5-354885639eff | -10.86453 | -68.68781 | 2026-10-05 05:44:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 23888966-75a0-3794-a2cd-3e018f437679 | -9.18573 | -68.91178 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0a65a6c-e561-3e66-bc22-85b1853c7ba7 | -9.12477 | -68.21309 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ca087c2-9db5-3f49-9adf-b146d7e5a3ba | -9.13509 | -67.8252 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7bb21418-8cdc-3c31-9e6b-885c27de13d8 | -9.10673 | -67.95686 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a1b58d5-b29c-3a0c-8d68-529e0e28ad59 | -9.08381 | -72.24192 | 2026-10-05 05:44:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58b27abc-54ea-3461-a5dc-77a7fb503b0e | -9.25908 | -67.64674 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10192be7-7387-389e-ae1b-0ec6e9f587e1 | -9.21954 | -68.17005 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f66697f-df50-30db-9bbc-e20812b093e2 | -8.44418 | -62.7182 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eb1005af-de2b-35a2-aea2-53a12bb33560 | -8.62862 | -64.11192 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c56721a5-171e-3074-bb90-75b89ecf4e10 | -7.44589 | -63.5609 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1097e42b-3981-3812-ab59-9d1e53f0f893 | -10.89999 | -57.09654 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2c94132e-70d2-3f2a-900e-fea46d96b546 | -9.48096 | -67.15744 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c006b37-a0fa-37f1-8f65-cfcb48731721 | -12.8752 | -61.71691 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f939d3e0-8601-393f-b76e-de1cf24d3767 | -9.44066 | -68.06387 | 2026-10-05 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee4d670c-1bbf-3744-af87-b52eaf4b9d21 | -9.16363 | -68.25385 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39f77ac5-404f-3852-aab9-160b39aa4d64 | -8.65171 | -62.52803 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17461a6c-7bbd-371a-8a76-ba3d4717efcf | -8.44954 | -62.73193 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4d767719-28d0-394c-979e-46cdd5b5b233 | -8.57557 | -67.00774 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f402c845-5004-3b07-992b-3221057b4925 | -9.39989 | -65.89612 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1784e85d-500a-3352-a25a-9d821f3f015a | -13.50334 | -61.13454 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 34cf7b93-d679-3153-94a8-25da5f707779 | -9.89593 | -67.33053 | 2026-10-05 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e06d9490-356a-30fd-863d-fba559c0d55c | -12.87471 | -61.72058 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec5f4a11-c29f-3a5a-8de4-d350e5c1ff1f | -9.07799 | -65.38428 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8026e884-0191-3040-a8fd-8394a8643d70 | -8.66883 | -54.56433 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 513a1ff5-da84-3b6d-a58e-fcd665cb5f67 | -9.15976 | -63.16427 | 2026-10-05 05:44:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a97c6b1-9659-3423-b543-899af776ef69 | -9.12133 | -68.21254 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bb5471e-4a30-37e1-882a-b3034c373105 | -9.48658 | -63.95441 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b828b1d-b441-3fe7-9d82-b39c8e913ad8 | -7.44532 | -63.56469 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36b85446-f45d-32b7-9d72-787582a8750b | -7.43154 | -63.56258 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f52f3e9-190b-371b-b94e-ae9229a29ba3 | -8.57795 | -66.82034 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97c2e03d-6d3d-3c89-ba96-2732fdb2d950 | -9.10552 | -65.35983 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fb510cf-6d69-396d-92e2-f15a337da393 | -9.40373 | -65.89317 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae292216-2c96-3786-b7b7-7452fe7ed30c | -9.47497 | -67.10939 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8254e3c2-91cf-3a87-b134-8f71496ce109 | -8.34787 | -62.83365 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f3702bd-321d-3472-871b-cce4a9acc69e | -10.90042 | -57.09302 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1eb24d0f-c9a1-3155-bf90-90f1550caafa | -9.15989 | -68.25758 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be92d7da-717a-3b2a-932f-e68699c628c4 | -9.15681 | -63.15963 | 2026-10-05 05:44:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e59d7c58-3842-33a0-bb43-1b44a678af85 | -9.10938 | -65.35685 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6789ada7-0e4e-36ba-83eb-6074bfdf211e | -8.55938 | -67.06686 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c1ad15b-f890-3f01-bd24-8c458e03d226 | -7.44646 | -63.55711 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7f172386-c414-38ea-b617-8608a0798c4d | -9.13873 | -67.93165 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16691f3d-896b-36d2-83ad-f19a7a52e6d7 | -9.15463 | -68.26843 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5835426b-4471-3e78-b82c-5646984bbc2b | -8.62141 | -69.50349 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df24ced1-521d-37c0-87f9-cf81284f3676 | -8.56594 | -67.13342 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f18bc77f-a154-3b12-a492-993e5ccaed00 | -8.35802 | -62.83942 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f403f6b-441c-32ea-a39a-2313f9d6d0c0 | -8.65999 | -63.48172 | 2026-10-05 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 76a9719f-3f17-3995-ba2c-ad75bee82284 | -8.66635 | -70.03976 | 2026-10-05 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b8ed616-6854-34c1-a019-fa55f53f2de9 | -9.13306 | -65.90763 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f910cfa-d8e5-342f-adff-cc13e82e8344 | -9.12175 | -67.86454 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc9532d5-ef1e-3503-ad62-edf9f6e89284 | -7.43441 | -63.5669 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97b5e13c-b7c1-3a06-91fd-300080c99e2d | -8.66934 | -70.04501 | 2026-10-05 05:44:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0aa9973-ed78-34a7-9ca9-1b23c192b6ab | -8.62534 | -69.50247 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af9e855a-2bb9-3561-8521-2edf086e44c0 | -9.12591 | -65.91001 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 80e11d1f-1083-34bf-b435-50781cb4c14d | -8.34725 | -62.83779 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README58.md)
