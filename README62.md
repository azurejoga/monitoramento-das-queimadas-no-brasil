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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68302adc-4858-3c4a-b4cc-2c024181d787 | -3.55751 | -53.75573 | 2024-10-23 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| fa826c71-9458-33e4-8092-83f87339b329 | -3.54175 | -54.73503 | 2024-10-23 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 480e9680-7a7f-359a-a9ee-d709b3e1e8ff | -3.54043 | -54.72783 | 2024-10-23 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| f122bedd-2110-3c94-b25c-d67f473ed60b | -3.53848 | -54.74023 | 2024-10-23 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 641ebeeb-9deb-306b-9b91-29c36a160540 | -3.5314 | -54.73338 | 2024-10-23 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1327d935-4a67-3a88-9b68-4134cb793046 | -3.52952 | -54.74578 | 2024-10-23 05:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e84b4aba-0820-3175-a6ce-b7239c5f6546 | -3.50018 | -50.27925 | 2024-10-23 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42676690-234f-3501-9c70-a6fc5d27c1a0 | -3.48699 | -54.15131 | 2024-10-23 05:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c97ad450-8793-36bd-b7d3-564b7c6d11c5 | -3.34625 | -50.3173 | 2024-10-23 05:42:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| f1e368a0-fa6b-3a03-bd4b-35cb24ef245e | -3.30501 | -47.18586 | 2024-10-23 05:42:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5d5510ae-7673-3aa3-a3f2-c17d27bf3517 | -3.25965 | -50.15319 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f1415cdf-b798-37b2-b117-d88ea3bf6e7f | -3.24675 | -50.17872 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 72bc51cc-4139-3242-81af-b5f85a274e9c | -3.24542 | -50.18766 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 44277440-bff8-3d74-a691-015ca1cb3f33 | -3.23917 | -50.16847 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9e2e968a-2ddc-361b-a8f1-823f168f27fe | -3.23784 | -50.17742 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3abe95a7-b4a1-3a8e-a210-a1b40629bbf7 | -3.22069 | -49.10615 | 2024-10-23 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f66e74b9-b1e0-3be2-be3d-1b8b20f14a12 | -3.21927 | -49.11579 | 2024-10-23 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 977884ec-ec42-3e2d-8dde-f89c37219896 | -3.20285 | -50.29076 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a7363d52-be1b-30c0-9538-ee46d71b5bdf | -3.20153 | -50.29965 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5b18ac68-d05d-3db5-a2b3-125286aae19a | -3.16166 | -50.37794 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4fb910c-d97f-339c-9129-f982602cd971 | -3.10594 | -54.16257 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| b92b8dcb-d698-301d-81b3-7ed55e4c73b8 | -3.1042 | -54.17392 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5f6aeebe-1c67-3622-b668-21b75f478b17 | -3.09766 | -54.14981 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| eaf82a73-ac87-341e-a065-81d2c37a4796 | -3.09592 | -54.1611 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 969ffc2e-4c77-33a9-9d98-8b8ca4819e38 | -3.09417 | -54.17243 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 33d37de9-6352-33a8-bf8b-aad0d64e2107 | -3.08589 | -54.15965 | 2024-10-23 05:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| deabcb39-721a-3474-8430-521e642258cb | -3.07227 | -53.24139 | 2024-10-23 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 07eec950-093a-391f-8cc0-a34b87275abe | -3.07073 | -53.25148 | 2024-10-23 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b9acc57d-15a0-3652-8d47-8de6678894c5 | -3.06947 | -50.49426 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e320787-538b-3d80-aa86-8f649f920174 | -3.06815 | -50.50308 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3c0e9c92-c26f-3526-9edb-07753d6fe752 | -3.06279 | -53.24003 | 2024-10-23 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0920ce96-ed7b-38d1-910d-5942f035f192 | -3.06126 | -53.2501 | 2024-10-23 05:42:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e6d54a7a-4950-31ed-b126-c0f76f3c558b | -2.96099 | -48.00648 | 2024-10-23 05:42:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9969db9b-e102-3ce2-bcd0-6fbf49955f67 | -2.95631 | -50.5163 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9e99af58-47f7-3355-bed9-3472ab1a2bd4 | -2.95499 | -50.52512 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c57e154e-a09b-32c4-a3af-491f85d0b11b | -2.94745 | -50.51501 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| cfc83387-f3fa-3996-a526-cd4ee641d7c9 | -2.94613 | -50.52383 | 2024-10-23 05:42:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5365164a-57fe-3c10-bf7d-ea9bbcedbbf1 | -2.86587 | -49.45124 | 2024-10-23 05:42:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 71396021-bdff-3c19-b403-fb2e0eb84455 | -2.84226 | -49.54595 | 2024-10-23 05:42:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f4ed691-ede8-3ba0-8819-1c8be5533e32 | -2.79926 | -49.58674 | 2024-10-23 05:42:00 | AQUA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 358efcfc-2cfb-3036-9045-9fcca232eba3 | -1.37738 | -51.99546 | 2024-10-23 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fa325ebd-bede-3afb-bdb8-072d929adef0 | -1.37879 | -51.98616 | 2024-10-23 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 21683a32-8f63-33a6-8eb5-38b019b43a5c | -1.38647 | -51.99679 | 2024-10-23 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 91ac2ee9-d309-37b3-a31e-e5f67cea2e6d | -1.38788 | -51.98747 | 2024-10-23 05:42:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8634dd29-3120-36d0-9af4-7da5c2301966 | -1.75255 | -54.09544 | 2024-10-23 05:42:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9a91f6f0-6dc6-32a8-8ff8-d093ba648d6c | -2.03707 | -46.96955 | 2024-10-23 05:42:00 | AQUA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 2b17e9ab-fa8b-3b4f-b20d-1b96ea9a703e | -12.50229 | -54.43436 | 2024-10-23 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ff34814-afd0-34c0-a2b5-6ae4f04b1c10 | -12.50167 | -54.4398 | 2024-10-23 05:42:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39cb7847-6502-310d-a412-cc5924c02e8b | -10.48489 | -55.60576 | 2024-10-23 05:42:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8f8a0ee-054f-3ae9-8767-6d842d07c184 | -10.47903 | -55.60498 | 2024-10-23 05:42:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dba2ad0f-2070-3293-b84e-c9e671448e2b | -10.95114 | -55.45169 | 2024-10-23 05:42:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4daefc3-7aff-37a5-8d3b-6fae4dd40522 | -10.94464 | -55.45544 | 2024-10-23 05:42:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07d4f212-3ecf-3421-b3ba-69cb8ffeef3c | -9.5653 | -58.92393 | 2024-10-23 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85e1f1f4-93f7-398a-9c40-b4c874cf051d | -9.56067 | -58.92329 | 2024-10-23 05:42:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28b5fa76-052f-3296-915e-7ac53c61092f | -10.20712 | -59.15246 | 2024-10-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f5443c0-42b0-3ef4-82fc-8ee00f8e7ee0 | -9.94798 | -59.86179 | 2024-10-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 94eb4763-b6e6-38ab-a911-d535d223418c | -9.94362 | -59.86115 | 2024-10-23 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9595526-e4bd-3af8-a5b0-108c5d401ea8 | -9.41962 | -61.09037 | 2024-10-23 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af00fb05-a457-3a78-93e5-e25e36bfdcb9 | -12.06317 | -61.06316 | 2024-10-23 05:42:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c467223-c4d4-3802-bc01-ddcff9f42064 | -11.37477 | -61.2753 | 2024-10-23 05:42:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 796d790d-bc46-3f4a-89fa-e30ea77d1b95 | -11.03932 | -61.53621 | 2024-10-23 05:42:00 | NOAA-20 | MINISTRO ANDREAZZA | RONDÔNIA | Brasil | 1101203 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fdcb6d6-1e73-352e-be76-67a9d8ebce87 | -9.18494 | -62.03194 | 2024-10-23 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0b3a9954-b4ed-3628-b4e9-761099f9a744 | -9.18377 | -62.03363 | 2024-10-23 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6086ae2-9054-3d86-8955-a7cfd24ba1b3 | -13.04177 | -62.31752 | 2024-10-23 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc59f46f-0f4e-300b-b5fa-e37f7567cd78 | -13.04029 | -62.31994 | 2024-10-23 05:42:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50eb38ce-198a-3c63-b944-c969874e7ffe | -15.9056 | -51.74222 | 2024-10-23 05:44:00 | AQUA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7009739c-4dbd-3147-8141-c676889bfb5d | -15.9042 | -51.75233 | 2024-10-23 05:44:00 | AQUA_M-M | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f77655be-faa8-3549-b10c-b7707093d765 | -7.98019 | -50.67536 | 2024-10-23 05:44:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 433d6c02-1bc7-346b-ac23-7964f1e21d82 | -11.01824 | -48.28368 | 2024-10-23 05:44:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f78f10ee-fce2-34a1-96ec-c1d9bea97cb9 | -11.02014 | -48.26979 | 2024-10-23 05:44:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 429dd8a0-1d82-30da-8374-7f7110c44d1a | -11.81038 | -47.06335 | 2024-10-23 05:44:00 | AQUA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 8219f227-4c1f-3aa9-b6de-ec9dc47b098c | -12.18922 | -50.37048 | 2024-10-23 05:44:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6ec2e0f4-8591-35ca-a4c5-c40bfc9274aa | -12.19071 | -50.35989 | 2024-10-23 05:44:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d5e742e1-11e0-360a-8fa2-4216c44c3a78 | -14.25355 | -51.12302 | 2024-10-23 05:44:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 62a80f93-0b74-3a53-9ce6-b33011d3e8da | -14.25498 | -51.11269 | 2024-10-23 05:44:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 49434c1a-7b35-34cc-9fe8-4e5aa001abca | -19.91773 | -54.40305 | 2024-10-23 05:44:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b923d40b-85bb-3ad0-93a1-3c376cb6822b | -19.9107 | -54.40274 | 2024-10-23 05:44:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b8fb445-0a59-3d37-959f-07c992f40a64 | -18.26958 | -56.06076 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 73ae77b8-ba0f-3e9f-b884-1a28d8d19ecf | -17.02398 | -56.00174 | 2024-10-23 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| cb6cbdf0-9d46-3ee8-be7a-8f4793a7b483 | -17.0235 | -56.0067 | 2024-10-23 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d32cfe0a-60ad-3bfd-bf67-2573d9c3ac4d | -18.27005 | -56.07607 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 58fc6252-f522-364c-9061-cc0a8a7a4002 | -18.2643 | -56.07031 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 30d161ee-3713-3df2-a235-9e47c03c07fb | -18.2638 | -56.07542 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 667a865e-0089-343d-a856-70b981c906b0 | -18.30562 | -56.2131 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| ccaf05fd-6242-3b87-950a-0dea037ff9c9 | -18.26911 | -56.0659 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b444cd09-ccf7-36a2-abec-7b28edddc7dd | -18.26864 | -56.07102 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 44a8ac28-264c-311f-8c29-159fa2c21053 | -18.26333 | -56.0601 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 586805e6-b17f-3540-9db1-a23450fdcbef | -18.26286 | -56.06523 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 88d9d072-85b3-3e75-9149-1aabff4a8ff2 | -18.25855 | -56.06455 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 48a1124a-a15e-3f31-9a32-323d3e787b82 | -18.25805 | -56.06966 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4ebb1b3d-e750-3b0d-9299-0855bb5ef6c6 | -18.31182 | -56.21373 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b8fbbefd-c9f4-3bc9-ba0d-be8b883799ee | -18.26329 | -56.08051 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 71367847-e3b1-3144-9ca2-085f2f887546 | -18.26239 | -56.07036 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 49ba1c81-9def-302d-b036-c20ee6f53d04 | -18.26192 | -56.07547 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ca529bc8-3f41-3e21-8a37-aebc520412bc | -18.25755 | -56.07478 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b031a2b3-0c32-3aed-a2c8-7295816891ee | -18.25613 | -56.06969 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| db0c143c-f746-3419-b929-7a59b3a45e45 | -18.31134 | -56.21875 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| c3575d1b-e065-3174-8b1c-04aca48660be | -18.31085 | -56.22376 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 56233f28-1e78-38b8-aeaa-fb3c7634da17 | -18.30513 | -56.21812 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0c5ab68f-6bb4-39c5-96da-ab862a034e62 | -18.27157 | -56.06071 | 2024-10-23 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |


[Clique aqui para ver as próximas entradas](README63.md)
