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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7556652d-dda9-3441-8b59-900d5788a62a | -7.2795 | -49.82799 | 2026-08-31 06:50:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a28666ec-b31e-367c-b926-2e1b2b701480 | -5.24333 | -55.88018 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 3448b719-f937-30f1-9817-b9e8bd8f914c | -7.52383 | -55.32924 | 2026-08-31 06:50:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 6d558b95-df97-37f8-a893-9e5e61c7566f | -4.84832 | -55.83069 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 58010ea1-0b60-319a-99d9-f9d9de323ba0 | -6.60683 | -58.59413 | 2026-08-31 06:50:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 222.5 |
| 1034103e-fc75-398c-a246-5f0739a2f7eb | -9.41798 | -45.65407 | 2026-08-31 06:50:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| da1b7ef1-c2b3-3123-8cdb-20cfe838ea48 | -7.93224 | -44.24159 | 2026-08-31 06:50:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2fe534dc-b67d-3479-b460-981332685027 | -7.27815 | -49.83685 | 2026-08-31 06:50:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c689d9ba-fe70-34fb-a534-2c003558813e | -7.97348 | -44.27014 | 2026-08-31 06:50:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 3cc2aa07-7846-3bb2-af04-f3d664923b20 | -9.579 | -47.61344 | 2026-08-31 06:50:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4e01222d-ef10-3153-92aa-9024763603d1 | -9.43015 | -45.64263 | 2026-08-31 06:50:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 73a1fff2-5e2e-3362-87a0-320f051a4b7a | -7.92092 | -44.23985 | 2026-08-31 06:50:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 780f991c-38aa-38a6-b01b-29f9cb385a35 | -5.25133 | -55.87384 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 83ecc584-89ac-392f-90fb-a1f2333d78ee | -5.24398 | -55.91969 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 483a5b82-d8d3-3038-9eb7-55acb2440c4c | -5.25314 | -55.90515 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 2be31af3-ae98-32ad-a7e0-bda415f1d56c | -6.93286 | -55.63864 | 2026-08-31 06:50:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 50588e0b-514a-361b-81a4-ed8bd66b9c49 | -5.25695 | -55.88239 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| af598726-60a4-3256-be3e-71bff946def2 | -5.24769 | -55.89655 | 2026-08-31 06:50:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 3f668b9f-35ab-33b7-a3c0-5ac83c0e17e3 | -6.61124 | -58.60294 | 2026-08-31 06:50:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 570890f4-1cbd-384c-a184-882185164e43 | -14.26752 | -52.87904 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 04cdc65d-4eb7-3415-b3d6-d472cc66aa30 | -15.06568 | -48.00792 | 2026-08-31 06:52:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 22aafda5-da0d-34fb-9e64-d192589909d8 | -11.21321 | -45.10173 | 2026-08-31 06:52:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 892adb96-817f-3eb7-be1b-ea81fe9457b9 | -14.43882 | -52.51262 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6e2b16b1-ca05-33ff-813c-a9e454a3fe1b | -10.73589 | -54.04416 | 2026-08-31 06:52:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e0803bda-1dae-337f-89c7-850cab1f943a | -11.32824 | -45.19064 | 2026-08-31 06:52:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 02b9a714-4088-3baa-8b6e-fa587055c271 | -11.68357 | -47.60701 | 2026-08-31 06:52:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 335d234d-466c-397e-9f36-ec80eca4961e | -14.20045 | -46.56258 | 2026-08-31 06:52:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b212136a-e763-3a42-b7c5-fea0c4515f76 | -9.18683 | -51.55076 | 2026-08-31 06:52:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3a131966-2e4e-3801-b9b3-d016974c8351 | -14.15479 | -52.78471 | 2026-08-31 06:52:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7e681ccf-74e1-3eb8-abc7-574dba90c629 | -14.58875 | -54.11228 | 2026-08-31 06:52:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 851c7a8a-9090-307d-99ba-f9fa5be47020 | -11.20667 | -43.37468 | 2026-08-31 06:52:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 19.0 |
| a60e8628-1372-31f7-ba0b-d037d4dba3c6 | -10.73803 | -54.03092 | 2026-08-31 06:52:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| ef7b14d9-2d26-3a18-9298-be50f04c260d | -11.87867 | -45.8133 | 2026-08-31 06:52:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9a715247-8a58-3729-8937-d0d0fb49fa54 | -10.80454 | -50.65624 | 2026-08-31 06:52:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9082b298-21fe-3241-a576-51a1e189cd2a | -14.39903 | -52.53052 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5a12692c-f9d8-3fe3-84a9-054bbb554a0c | -10.04215 | -48.6752 | 2026-08-31 06:52:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 139560a2-2a01-31d3-83dd-d97f763d9a3f | -10.74145 | -54.03827 | 2026-08-31 06:52:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| f01bb2f1-830f-380b-b572-af96af294979 | -14.38366 | -52.5684 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 97249201-4455-3583-9f30-ee8c8c740a66 | -14.43724 | -52.52244 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 87ebcc44-059c-3eed-ac36-52c6abbc27fd | -14.40826 | -52.52769 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 01e78923-1c07-3203-acea-dc7f68faa08a | -15.40745 | -52.702 | 2026-08-31 06:52:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ffb4ff9b-4a9e-3ff3-92d7-173733fa3845 | -14.40058 | -52.52068 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 1beca1bf-561b-32c0-9fa5-5e188941113a | -15.06717 | -47.99728 | 2026-08-31 06:52:00 | AQUA_M-M | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| f55a01e1-227a-3b76-ac4e-03265c3ecb27 | -13.46348 | -51.41024 | 2026-08-31 06:52:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2bfbc63-5e6c-328d-9de5-9a2accd45de3 | -14.60261 | -54.09016 | 2026-08-31 06:52:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a1b3a97a-7c5f-30d1-bce0-a99a91e0538c | -14.22897 | -52.84437 | 2026-08-31 06:52:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 54427a6d-2030-3f47-aa79-89d090086acb | -15.4272 | -52.69553 | 2026-08-31 06:52:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1a79fe36-b96e-3feb-81ea-d732195d90b7 | -10.80592 | -50.64722 | 2026-08-31 06:52:00 | AQUA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 1ef0d3be-ca02-3b4c-8eca-4ab8dc2bc63c | -13.63873 | -51.83709 | 2026-08-31 06:52:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8af8174e-edd3-3605-914e-03a198aeb99d | -13.62976 | -51.83571 | 2026-08-31 06:52:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 9648ece9-5782-32cf-9bca-f2fc162b0842 | -14.2273 | -52.85482 | 2026-08-31 06:52:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4eb1ac7a-b9ca-325a-86b7-9022f48ce05f | -14.60068 | -54.10197 | 2026-08-31 06:52:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3db2ea2c-1cb0-3607-81f7-4b7f56ef498e | -12.13121 | -47.25893 | 2026-08-31 06:52:00 | AQUA_M-M | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a2f6f4c7-d92d-3acb-927b-a2f8245049be | -10.74368 | -54.02496 | 2026-08-31 06:52:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 88b45425-10d7-381e-b847-e506b547f37b | -11.67416 | -47.60545 | 2026-08-31 06:52:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| c810e9d3-9926-3d1b-8a1a-dc442c64390c | -11.04477 | -47.11986 | 2026-08-31 06:52:00 | AQUA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| f9a2d3cb-84ce-335f-8d2d-3a2327be2893 | -15.63264 | -50.09673 | 2026-08-31 06:52:00 | AQUA_M-M | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ded48546-1bb3-32a5-b6ff-49394f2476f9 | -17.27532 | -45.99204 | 2026-08-31 06:52:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 30ef068f-d742-3d59-a093-baebe7579019 | -14.59074 | -54.10015 | 2026-08-31 06:52:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7cd7458a-6a4a-34fe-8bfe-5aab2528f7eb | -14.59875 | -54.11382 | 2026-08-31 06:52:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 871220da-0d7c-3048-bc2d-5d18ed455005 | -15.41496 | -52.71352 | 2026-08-31 06:52:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c8c36c5f-4e3b-316a-8912-ac123180a339 | -14.38519 | -52.55871 | 2026-08-31 06:52:00 | AQUA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c4e2bcec-c861-3025-8252-772ac7213dbf | -14.12368 | -52.80045 | 2026-08-31 06:52:00 | AQUA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6f3470cc-8c9e-3e73-aa42-9e605756e366 | -15.42562 | -52.70541 | 2026-08-31 06:52:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 24f4b728-6213-3e2c-9374-63c14c6df4fb | -13.6283 | -51.84497 | 2026-08-31 06:52:00 | AQUA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a4a740b2-f99b-38e1-98da-21f989a31494 | -10.0435 | -48.6661 | 2026-08-31 06:52:00 | AQUA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2a54498d-9aa2-3133-9438-fe8b6a6969fc | -17.61588 | -46.66062 | 2026-08-31 06:52:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 6561fe57-b886-3c7b-b68d-49732aca85f1 | -17.27663 | -46.00197 | 2026-08-31 06:52:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 60c6c6dd-330c-3c95-871d-e1341b10d20c | -19.15211 | -57.39279 | 2026-08-31 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 3a5b5cf1-e7b1-3c2e-b68f-97ebe763632a | -19.11467 | -57.41492 | 2026-08-31 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 62a96edf-aadf-3b4e-9f2f-2b44e727148a | -22.03901 | -56.08421 | 2026-08-31 06:54:00 | AQUA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| c1e9b142-a377-3602-bf4e-7f46e2d23cc6 | -19.16372 | -57.39514 | 2026-08-31 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| bcbe9a96-7bf2-3cec-92e5-ca628135c8b3 | -19.14402 | -57.38562 | 2026-08-31 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.9 |
| d9e55edf-b1b6-3bbf-b498-53dd832f26c1 | -19.14099 | -57.40262 | 2026-08-31 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 5333c257-4739-3125-b855-228e456dd3c5 | -19.1405 | -57.39045 | 2026-08-31 06:54:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.7 |
| 30ad4d79-6dcb-33a4-a083-83e0182f753d | -19.154 | -57.3978 | 2026-08-31 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.9 |
| 611733de-6690-3e65-bae0-7ec039cd2755 | -6.622 | -58.5965 | 2026-08-31 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 567498aa-81ca-3ea9-b07e-ed39f43edf9d | -5.2547 | -55.9105 | 2026-08-31 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 38b1ab2e-337b-3139-9101-8fcbfda07107 | -5.2548 | -55.8907 | 2026-08-31 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 938a0b53-b9ae-3a2d-9af7-6ef842cdf3b9 | -6.6036 | -58.5972 | 2026-08-31 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 134.6 |
| 1a1e8048-5583-30ad-b2b9-66d2132be480 | -5.2362 | -55.9112 | 2026-08-31 07:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 04c731a3-cbcc-3deb-989a-dfa25e5ee92e | -6.1294 | -57.6833 | 2026-08-31 07:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 0426a520-9766-39e9-94a4-f7f3a217ce86 | -6.6035 | -58.6166 | 2026-08-31 07:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 208c6bc1-7388-393c-85c5-0b46e9ea3cae | -6.1294 | -57.6833 | 2026-08-31 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 14bce65a-5eb4-37e9-9ffd-c8b6024524bf | -5.2548 | -55.8907 | 2026-08-31 07:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3dabf7e6-95ad-3c08-a55a-da8cf6334cb9 | -6.622 | -58.5965 | 2026-08-31 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 41c52b7d-468f-37fe-9c18-d7c00e8996a3 | -6.6036 | -58.5972 | 2026-08-31 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 50b15db6-9525-3421-9f2d-19b37c89925b | -6.6035 | -58.6166 | 2026-08-31 07:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 32f0fa00-c523-32cf-8e1e-c73ce0161b4d | -5.2547 | -55.9105 | 2026-08-31 07:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 9439033f-7c0a-3dbb-8a39-f284d5659e47 | -19.1136 | -57.4239 | 2026-08-31 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 9a532333-f34f-3f1f-9098-9815ef6d9285 | -6.1109 | -57.684 | 2026-08-31 07:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| cfc92a0a-27b4-3609-b2d6-5219fed0dde2 | -6.6035 | -58.6166 | 2026-08-31 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 07a9fb0f-3098-360b-a17a-cadb02f0d38a | -6.1295 | -57.6637 | 2026-08-31 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 234b7a3c-f114-3350-a0bc-594839ea5e68 | -5.2362 | -55.9112 | 2026-08-31 07:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 51ce57ee-a95c-311a-b2d1-5fc4dca6c30d | -6.1294 | -57.6833 | 2026-08-31 07:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| c1f6a3e5-bbc3-3254-8daa-43a7228b867b | -5.2547 | -55.9105 | 2026-08-31 07:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 67e5f5e3-665b-3204-a081-5de1909e511e | -5.2548 | -55.8907 | 2026-08-31 07:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c4f6ad81-6a02-393b-b374-24cea3b951fc | -6.6036 | -58.5972 | 2026-08-31 07:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 2dbde168-84b6-37a3-8f50-5e168d635397 | -6.1111 | -57.6645 | 2026-08-31 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 74eeefe7-32f1-370c-830b-6ad388046e88 | -6.1294 | -57.6833 | 2026-08-31 07:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |


[Clique aqui para ver as próximas entradas](README80.md)
