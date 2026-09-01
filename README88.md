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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e90e7955-f2e0-3b03-9546-3e1720f93a28 | -8.71764 | -67.11297 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1cdb15e6-a8d1-36c6-a229-3b0f0f86c3e4 | -7.86649 | -69.94527 | 2026-09-01 06:22:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46d02a92-5b03-359c-8d9e-b9d2a16927a9 | -10.10164 | -68.40479 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bd916669-9252-3772-bc22-5f4f6147a7b2 | -9.02718 | -65.45334 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8f1bd998-fb9f-3240-8dd6-52c9398e550c | -8.89351 | -68.90227 | 2026-09-01 06:22:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 416b4868-13f3-313c-b533-8af34f136925 | -10.1023 | -68.3997 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21876c56-2533-329d-8af3-b42a2a22f356 | -8.54234 | -67.16241 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbed9e41-ecc4-322c-8c90-0990e53b1c6a | -9.45857 | -67.45589 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2a10287b-03ee-35da-ba59-2335f18f6cc0 | -9.03422 | -65.39863 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d69e5ee-285a-395e-8228-2ee53fcb6807 | -7.35305 | -72.9537 | 2026-09-01 06:22:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6564c51a-c1b3-342c-917b-6ae6d5b09cd5 | -10.13533 | -68.58254 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16578174-a1fa-313c-87fb-6b253b11da8c | -10.43893 | -67.84279 | 2026-09-01 06:22:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0dbcbc88-de39-3839-b274-3367dcb2136a | -9.05308 | -71.26322 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0be2882f-39e9-39bc-a7cc-94c548fe525e | -9.62295 | -68.60177 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fcd70553-65f1-3288-b161-55d4ecd1b29b | -8.75281 | -70.80882 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 977825a4-035b-3c20-813e-198a2dbe18f6 | -8.77518 | -69.33979 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 4fb4c7ac-9bb9-306e-997d-5131c6197013 | -8.79029 | -62.49193 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f670d37c-c60c-3a54-b7cd-9d6acd6bf87e | -10.41488 | -64.45971 | 2026-09-01 06:22:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d73ec5c5-d81e-3750-ba95-a5323c2640d3 | -8.58788 | -66.97297 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97052d2a-8c68-3b71-ad90-837b850fb6a9 | -8.80265 | -71.04667 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc293acd-11fa-3f21-8f35-4b0307feb842 | -8.86971 | -66.77959 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5266d533-10ba-3c81-8e93-23df078c7725 | -8.78607 | -62.48354 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acd7f8d7-cb0c-3f81-bf47-337337d34a5e | -8.87532 | -66.89408 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5db0f267-1f5c-312f-85f7-132768c58d50 | -9.06066 | -65.48337 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 43f53b8c-51e2-359e-a542-a91401917fb5 | -8.60918 | -70.21879 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93d272dd-d0fc-393b-a15d-8c336983d16c | -8.87803 | -66.89104 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b54024f-3c89-39b5-8915-054ffa5faba7 | -8.79107 | -62.48572 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f09467b6-18b0-3daf-9891-63daad403faf | -10.0855 | -68.29755 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b064f54-47df-3dac-b9b8-2a4414a8d683 | -10.61219 | -69.6287 | 2026-09-01 06:22:00 | NOAA-21 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95aee5c4-e5aa-32f5-908c-81ca5fc4718f | -8.58708 | -66.97903 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| afec4343-6a20-3e68-82a8-0b9a172ce8b3 | -10.25325 | -68.21344 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24a186f3-2351-3512-b641-8f6c96148b3e | -8.51042 | -67.13441 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3caf7c14-77a0-3e72-bcf8-59b345edc3f6 | -9.06583 | -65.48809 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58021526-a75f-3e0f-ad71-eedf9a7a5115 | -8.97279 | -71.25928 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7b1b9497-7ba1-393c-93b7-b3cfcdd522f0 | -8.77952 | -69.34043 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f209629-7654-3819-b9fe-c9c01fdac6c3 | -8.80388 | -62.49381 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b2c223eb-3762-3e30-ae91-06b3ee57711f | -8.93366 | -62.36197 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ded55c5d-8c73-3218-9568-90c9d2fa1eae | -8.60614 | -70.21092 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c6194bd-b58f-33fa-a70f-2738816b97a9 | -8.86495 | -66.77571 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 915aae30-7c88-3ed8-859e-61425fc5e219 | -8.51545 | -67.13515 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 591370a9-aed5-3459-8258-07b3d4b24f6f | -8.59257 | -66.97667 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fd5ad16-fb55-3e66-972a-741ecf8d22e1 | -8.75674 | -70.8094 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2fac7277-edcd-3ef5-9ca9-5f4c7b09d0ad | -9.4532 | -67.45484 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fb3a4e14-78f3-3158-9dc8-a55c03a21c71 | -8.72949 | -71.02388 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5aaffeef-1dcf-3e40-9fc5-acdcb310de52 | -8.88317 | -66.89178 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01845a85-b963-34c3-9abe-5b0252b510a2 | -10.18209 | -68.9959 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 101eb9a9-6a85-3a84-98e0-35268a6be04a | -8.96896 | -71.25872 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9eddfe67-71d4-3ae0-a824-56ddcb7d7b65 | -8.8658 | -66.76938 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b6c049f-7cd6-362f-8516-8650235a9b0c | -7.65565 | -73.03704 | 2026-09-01 06:22:00 | NOAA-21 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| db47237a-f2f0-3b4b-bdd6-03f9c601bb51 | -8.87964 | -70.81606 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c83e4c17-90aa-3463-8ccc-ec32bfe5a5b4 | -8.97348 | -71.25454 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8f473688-95b7-3e24-971a-887b25565e49 | -8.89071 | -66.83295 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a4e3a80-de79-3c60-b813-ead327f11e8c | -9.45358 | -67.45519 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bbcc3006-65a2-378a-9727-d14e5aaac585 | -8.79477 | -62.51142 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 638b1f93-a297-3b75-965c-450d056c2fbf | -8.60154 | -70.214 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9274ab03-c4a9-3e50-b539-5c000fbcb029 | -9.03335 | -65.45024 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 463f1c3b-7762-3bcf-8359-b2363dbe0710 | -8.93975 | -62.3694 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1ee46e7-3f88-363e-9337-99f1e35a8d9d | -8.87055 | -66.7733 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67ffcd48-d842-37a8-9df5-9dceefa54fd5 | -8.79214 | -62.49064 | 2026-09-01 06:22:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7bf7c07b-0de9-332e-ba96-a4de042b1177 | -8.12646 | -71.38838 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2a8d20c-3a6a-3c11-916a-65cbca7279a0 | -8.59746 | -70.21342 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4b5fad6-d672-33ad-afe6-f1f1288bebfa | -9.06328 | -65.48611 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f28dd98-55ea-3f07-8f11-c950385995e0 | -8.37417 | -70.84982 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d1777af-2a21-39f5-890a-6033ff58af3d | -10.21924 | -69.04036 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac52bef9-712c-3f01-ad02-8a66d57d26a7 | -8.7007 | -69.41869 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ddaac90-63c3-3bad-b806-6e971efcd470 | -8.60666 | -70.20727 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97ba0a7c-0a52-389e-abfe-d6c150378868 | -8.80226 | -70.79713 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 854e41b9-84fa-36b8-9111-92fa15435aae | -9.06277 | -65.48997 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6477a0be-1e23-3f08-a799-49efd01d2e8a | -9.02903 | -65.39391 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5116533b-0049-3e5c-a0d9-b4f9fc0a5e19 | -8.81062 | -71.28909 | 2026-09-01 06:22:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2717a90-1651-32f4-a17d-be203f698ee5 | -8.92727 | -72.83817 | 2026-09-01 06:22:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59344e7d-d3c4-305c-aefa-e9b1a03571e1 | -9.00462 | -67.8007 | 2026-09-01 06:22:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3f92519f-52fa-314e-8c5c-ea84007e7ac5 | -9.03991 | -65.39939 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5523482b-3e9d-3def-a497-e64394a95177 | -10.14255 | -68.77151 | 2026-09-01 06:22:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dceebc49-eb6c-3963-92d2-0c0923c4ca52 | -9.02817 | -65.44563 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b08d0f6e-a678-3968-af4c-4b500e8f740e | -8.77409 | -69.33627 | 2026-09-01 06:22:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 61c23fb0-5aac-3d49-a442-560108ae51ab | -8.88278 | -66.89481 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87de711d-907c-3192-b101-8066bca1ba2f | -8.65776 | -70.68953 | 2026-09-01 06:22:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4db5b8fc-20a1-360d-a718-ba7a1241f9b9 | -8.87764 | -66.89406 | 2026-09-01 06:22:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f10c3bf2-866c-3cd7-85fe-fe214a1d6dfc | -7.571 | -60.4643 | 2026-09-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| b618a1c6-8fbc-3c66-9742-0dd07a6bb159 | -7.5709 | -60.4835 | 2026-09-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 9562b51b-f332-35bf-8440-b15e3bf1b719 | -7.3487 | -60.5883 | 2026-09-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 571f71e4-63d9-3c8e-8ba9-1afb5c14d8f4 | -7.5894 | -60.4827 | 2026-09-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| bd775dc6-4ae2-3545-80fd-097a57371b95 | -7.5895 | -60.4636 | 2026-09-01 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 20ca3a60-8943-33fc-9299-1281400ceff6 | -14.4011 | -52.5014 | 2026-09-01 06:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| fc4e3e3e-1daf-3d16-92b5-61259eff43a6 | -16.0547 | -54.3908 | 2026-09-01 06:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 84a24955-5927-3d23-a27c-a9ef7c78af87 | -14.4011 | -52.5014 | 2026-09-01 06:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 73313f67-4ab9-35d5-a999-8d1cf73df68e | -14.4204 | -52.4989 | 2026-09-01 06:40:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 4c63f615-e645-3ef3-bb37-b1ff98c56111 | -14.4011 | -52.5014 | 2026-09-01 06:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |
| e8a39bca-dbfd-3776-938e-ccd940e8c84e | -8.1112 | -54.9483 | 2026-09-01 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| e465ea5d-c916-39df-aa95-4ad96eaf9bea | -8.1296 | -54.9672 | 2026-09-01 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| a8611f96-0acd-337b-bfbb-6f14c451bb63 | -8.111 | -54.9684 | 2026-09-01 06:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| b5526032-ab9b-3f0f-ab73-8ead1f0a03c6 | -8.77356 | -69.33856 | 2026-09-01 06:59:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 546bb7c7-fc9a-3f56-b9f3-0464c73f1469 | -9.62311 | -68.60171 | 2026-09-01 06:59:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88f74faf-0f23-38f9-a513-b4eacf4b3fdf | -8.80041 | -70.7992 | 2026-09-01 06:59:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29bc22b7-be9b-3565-8453-fc10ae6a0b47 | -8.801 | -70.79475 | 2026-09-01 06:59:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bc8c5d3-3087-36fc-9960-1e6eea98ab45 | -8.97407 | -71.25645 | 2026-09-01 06:59:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9222476e-a73e-357c-81a2-1225cc78f175 | -8.60942 | -70.21001 | 2026-09-01 06:59:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36c07695-d5e6-3956-8e35-902b810761f9 | -8.60315 | -70.20926 | 2026-09-01 06:59:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edb58bf9-9081-35ad-b439-e51c8ffd451f | -8.77145 | -69.33891 | 2026-09-01 06:59:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README89.md)
