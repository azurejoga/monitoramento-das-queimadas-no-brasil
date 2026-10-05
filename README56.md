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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bdabebd-bded-3327-b1f9-dada7dad6b25 | -9.02675 | -67.55328 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1194a108-8417-3112-9b84-1574d307832f | -9.12141 | -65.87379 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d84302df-db16-3bf6-82a3-c0fdc9882324 | -8.62577 | -69.49978 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af1b46d5-27bb-3555-bc56-f7cf3f645709 | -8.77758 | -69.53519 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abfdbae9-9f90-393b-b6b2-e5b59eb08f7e | -10.66094 | -69.13049 | 2026-10-05 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faa4221a-cf11-304b-bcb7-16178638f412 | -10.08503 | -68.46853 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa657dca-26d5-3873-a62a-73344e36fbff | -9.15201 | -68.24077 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c183d3a-9b7e-3bf1-961a-2b7d23059563 | -9.48152 | -67.1539 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4d58bdc-a126-30f1-baea-f10df2cf64df | -9.13349 | -65.4647 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 594bbd2f-17ff-359c-945e-374fe900d5cc | -9.15262 | -68.23699 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2ac50111-b8ec-39a5-9b31-90f1e4f43f55 | -8.52116 | -67.00632 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c99b103-f1b8-38b4-a0de-8b73aa70ad84 | -9.55216 | -66.79411 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e55db72-1a6f-361c-99d3-47572d04d3b7 | -9.1518 | -68.26408 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea9acc79-bbaf-3023-858d-26deedf03855 | -8.04877 | -72.43782 | 2026-10-05 05:44:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 879b816d-e2cf-3943-876e-b081d5273679 | -8.5276 | -54.59371 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 066141c0-2bf5-3e70-87ba-931224cc58d5 | -9.52132 | -62.97248 | 2026-10-05 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39dbf7bb-6377-3ab2-9221-4011dc1ce6d3 | -9.40773 | -68.65982 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32c44348-09e7-3dc3-a3ec-dc963481a23e | -7.44475 | -63.56848 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83cf5d86-b47c-3c28-ad12-0e1815892ceb | -9.15895 | -68.26088 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da322b4a-bce0-36e8-8f95-1ad364a217e7 | -8.66444 | -54.54899 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4ed63a5-6256-37a0-a833-34ab5050b1ea | -8.59676 | -66.80894 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 098dc77b-6438-3877-895e-68fb81299b71 | -7.36238 | -72.60937 | 2026-10-05 05:44:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 40ba00c8-aeb0-3c06-9518-c01bcc665f20 | -10.26721 | -68.83284 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cd2d532-01ea-3e49-89dd-052080f5d7e0 | -9.11721 | -65.94421 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba060f87-824e-3eb3-ab73-db7e31473e04 | -10.44777 | -69.49631 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5133be2-c7a7-354e-a86a-a327dee269f1 | -10.60937 | -68.68198 | 2026-10-05 05:44:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12fb3240-d44a-3461-864d-afce2b6ff65f | -8.58957 | -66.81139 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8dcda66-e3cb-3e1d-816b-5583ed9e127e | -9.49897 | -67.68187 | 2026-10-05 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 417225d2-c0e5-3958-bdc5-16032c7ac57d | -9.13251 | -65.91105 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc68c593-6759-3ebf-933f-718e692c1df3 | -9.44235 | -67.10067 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce37fd3a-f72c-3772-8c21-6d96dcd08283 | -9.25671 | -67.65023 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6c4ecee-3fae-304d-b0df-fd9dee2190e0 | -8.36176 | -62.81451 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2e81214-48d8-37e7-8097-6e7a0c86738c | -7.44876 | -63.56522 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bc8b03f-ccb9-3da2-9f58-21309327a4cf | -7.439 | -63.55984 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15b98675-7675-3a2c-812b-32298efdaa56 | -9.15833 | -68.26467 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65bd6500-0856-3358-aa75-837cca2326ce | -8.74626 | -64.19086 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1dac5c48-6129-3b3c-9a16-231c23866d92 | -9.16114 | -68.26902 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 563b135d-b696-3308-87d6-b83fdea3cd9b | -9.39454 | -67.84779 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a737ef2-cfc3-30f7-a169-01a39f63bfc3 | -8.6756 | -54.56045 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 634d1d46-bac5-35a8-8737-b7683b7b0f44 | -10.13535 | -64.86573 | 2026-10-05 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8b829ee-16f8-3107-a5fa-3f61e48cb51c | -9.7106 | -67.5714 | 2026-10-05 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4648b0b9-a5a8-3337-892f-cd486dcfdc42 | -11.97265 | -63.61004 | 2026-10-05 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82980bf0-774d-3ef9-b4cf-56c764c7ff3a | -8.67124 | -54.54497 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81094966-17c8-3a69-b3cd-d11704d867c0 | -8.88073 | -66.65021 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8216a235-a3f5-3cf6-b239-4bb9af6c97f1 | -8.53375 | -54.59462 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4df845e2-d00e-3ad9-92dd-ed9aa53443ce | -9.40427 | -65.88968 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bca0dec6-e1d8-3983-98f1-b2ba52bc7508 | -9.40757 | -65.89021 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f6b34b4-6a48-3d29-996c-3dfb4e388727 | -7.43957 | -63.55606 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 660752df-4005-3f5c-b542-22dc5fcc95f6 | -8.35879 | -62.80982 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a1df8a-694c-3535-86bc-9369885dbbd2 | -8.3413 | -62.82842 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b4b249c-2be7-335e-a2d3-ceaed4c6fa6f | -7.44073 | -63.57174 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6f310d6-1fc9-3380-b497-30e171c8b590 | -11.97625 | -63.61059 | 2026-10-05 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d7c1a3e-8f82-32b7-b931-8b51c01d60f9 | -8.87797 | -66.64619 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da8fe834-db6d-3669-a0d3-f4bc0c26d727 | -9.11306 | -64.35931 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a594f10d-32b5-3fea-a221-abcea7abc60c | -10.14246 | -68.39589 | 2026-10-05 05:44:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 433dc09e-748e-3f87-b6f2-f515a04b1fef | -8.51783 | -67.00578 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 537a874e-df2b-3bbd-acf3-26d867ac837f | -7.66367 | -67.06944 | 2026-10-05 05:44:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f16a5b6-109c-33da-aed1-85fa973dedb6 | -8.52701 | -54.59848 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a92cbc39-82e9-3dbe-bf91-418792e81838 | -8.67184 | -54.5401 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5a1d2ca6-1b4b-3825-92e4-994c669fb8c9 | -9.08733 | -67.32349 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 033ef3da-6463-3517-8d90-a9d9491dcafd | -8.74257 | -69.45112 | 2026-10-05 05:44:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9aee9848-61d1-368d-b4a4-5f50ebf1b409 | -9.40319 | -65.89664 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d076a69b-16af-3937-8ed8-86554d6bdb81 | -8.35084 | -62.83834 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c2e619b-6475-3096-8d6c-4c521b7fadac | -9.66927 | -66.82772 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ca3689a-85ee-3a02-8650-089de6341ae0 | -10.25566 | -63.16768 | 2026-10-05 05:44:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 819821f9-abd0-3a7d-9665-a7cb9ebb0eea | -10.90173 | -57.08234 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| b9f5c695-6918-3300-839d-96ea0cf19764 | -8.87411 | -66.64915 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 600112cc-85c2-311a-a009-298c59f776a8 | -7.4304 | -63.57015 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdee099b-ce05-31c2-9261-50945ac41036 | -7.44244 | -63.56038 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7177c308-4bb4-3479-a996-0f042c796b7d | -9.43786 | -68.0596 | 2026-10-05 05:44:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b689b74-b266-3b01-ac3b-1f04ca3a6f58 | -9.06564 | -67.73092 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 524f3e66-85f4-369f-bbe5-26182e32d75a | -14.30118 | -57.47001 | 2026-10-05 05:44:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ea324e5-a9c2-3235-9e5b-d671d9379a0d | -9.67257 | -66.82825 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62b2b5b2-5462-3ea6-ad9b-b1efc498b2a2 | -9.50233 | -67.68242 | 2026-10-05 05:44:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 457bf44e-9b0a-32b8-b8de-42126df6a7a4 | -7.45278 | -63.56195 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee0de848-9f36-31fe-8310-eb47b143cb29 | -7.41769 | -64.66129 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ac935dc-260d-35c0-abb3-b9f552161552 | -10.895 | -57.09237 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ecc6aa3-9f62-3d5e-8148-f63e87317525 | -9.15929 | -68.26138 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aff7de3a-43bd-322f-8aa7-da27fd14969e | -9.1562 | -63.16373 | 2026-10-05 05:44:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9442530-e5f4-3786-bdd0-c6ff727febdf | -9.13645 | -68.24992 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd5992fb-7b41-35f1-9bdb-e5281254e7a7 | -10.13589 | -64.86208 | 2026-10-05 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7a24b8a7-7868-3349-b156-893ff14a59f3 | -8.28435 | -71.07587 | 2026-10-05 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc61c651-63de-36e0-9bb8-6dd8f6b6ce9c | -9.4149 | -68.54921 | 2026-10-05 05:44:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79f67990-f41d-370c-8f26-5ff50fe180ca | -7.68459 | -69.93466 | 2026-10-05 05:44:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09eaee17-fbcb-3c08-a8ec-2cf07be13f0f | -8.33932 | -62.86624 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f098ecff-5daa-3f94-8a88-35454edd1360 | -9.1179 | -68.21198 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9931050-4e5c-35d6-8360-8b18052dece0 | -12.1621 | -60.74868 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f236b081-b12e-38ef-892d-c6b3df0820c8 | -10.90217 | -57.07871 | 2026-10-05 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b169e74-9349-34d9-83bc-19f2b340ff8e | -8.93258 | -62.37288 | 2026-10-05 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14f52607-841a-39fd-92fa-6d28602e4a77 | -9.1652 | -68.26577 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e919af62-be9f-3573-932b-8a8f9acb4d98 | -8.74285 | -64.19035 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e050e6f-083e-3434-9440-694f3da602f9 | -9.22296 | -68.17062 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8fad4ee-8fe2-3d71-aac2-0c9273d7e939 | -9.16177 | -68.26523 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb874d81-3f08-3aea-bf58-89fd81cfa966 | -9.39935 | -65.8996 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45fc6f37-5aca-33a5-b8d6-665d696845f8 | -9.40703 | -65.89368 | 2026-10-05 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 508ca88a-6593-39e5-90f8-05f0a6842976 | -9.25849 | -67.65037 | 2026-10-05 05:44:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 68da63db-eca7-330c-83ae-421917367856 | -8.66505 | -54.54407 | 2026-10-05 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b445215-3de3-3667-a5f5-5928a189b9f0 | -12.88333 | -61.71809 | 2026-10-05 05:44:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74317332-35da-3e47-916c-41250a148083 | -7.44934 | -63.56143 | 2026-10-05 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0a17695-4b28-3b5e-a8bf-e53c9ef48a2f | -8.4448 | -62.71399 | 2026-10-05 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README57.md)
