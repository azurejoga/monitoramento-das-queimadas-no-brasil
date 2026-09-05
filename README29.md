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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae08606a-b3d6-3a25-bbc9-4905149c6803 | -4.19671 | -59.93444 | 2026-09-05 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f90f138e-ae0d-3dcb-972c-f40bc5188569 | -3.76421 | -61.76701 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ac5fdd02-5ccf-32c9-b844-9c20db66713d | -4.37026 | -47.77621 | 2026-09-05 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e2dbe90-7a58-3ead-b283-17e876cbfddb | -4.41607 | -59.86897 | 2026-09-05 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a4978379-da5b-3a1e-8b4b-3865978864f6 | -3.77804 | -61.76564 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d023139-18ff-3141-89a3-f96220bc0ec9 | -3.76089 | -61.76648 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3d51edf-40ed-3f33-842b-3a6f2b69ac14 | -4.24439 | -62.23741 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c3bf3281-d51f-3ff0-a46d-09cd430e6755 | -5.29319 | -55.99533 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb7ecd4e-8676-3ff8-add9-9c4f5b0c776f | -5.29257 | -55.99941 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec67ed63-e9c6-368f-8896-ee7beac2f7b9 | -3.77085 | -61.76805 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 00da690c-268b-3f70-9fd8-8c76322fcb33 | -3.77418 | -61.76857 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fa2dbd1e-d744-3569-99d5-fae15ae0edef | -3.13604 | -60.64273 | 2026-09-05 05:40:00 | NPP-375D | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2f788067-67e2-3596-9cec-765841d75a81 | -5.16678 | -56.0603 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 276f783c-5b65-3df3-a230-3f744cd09db9 | -5.33438 | -56.02477 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a27dd4fb-a511-3857-b48b-9b344dfbe61c | -5.34358 | -56.02202 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d29c0103-1d9f-3746-8ceb-644e82338096 | -5.07663 | -56.28799 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21a89f18-4de9-3ce5-8610-187668aed82e | -3.77695 | -61.77255 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76e52320-09b2-3ee0-aefa-6ad92542e817 | -3.07824 | -61.18151 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c63edab1-f931-3cc5-8e12-6b7d031536ea | -3.7714 | -61.7646 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 67b6c2b2-0968-388d-8c42-e347a35c3548 | -5.34239 | -56.03012 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3fa8d1b6-d2cd-3546-98c8-31078f077296 | -3.32977 | -58.15306 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3108f7a1-e1ef-3eca-986c-19f3f02743c2 | -5.17106 | -56.06095 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4f9a362e-3a8e-356b-aa37-224cb3ecd5e9 | -5.32887 | -56.0214 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdbeb87e-e145-37da-bbc1-cbc9f79e305a | -5.34788 | -56.02266 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13f59ed8-c34e-3ad3-9f05-da389b3f3d31 | -3.07307 | -61.08508 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e33261c2-3f52-3275-bbc6-254a4db92bc8 | -5.33497 | -56.02069 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75cd7cf4-88a2-3730-8e03-29a54ca797cc | -3.12239 | -57.69877 | 2026-09-05 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ad1386b-233a-330e-b02d-cc002e54677c | -2.81142 | -48.67442 | 2026-09-05 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d97fbe81-6412-399d-91dc-e68c018140b3 | -5.30796 | -56.01414 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ef530fc-42db-3120-810b-61c9f85f5a13 | 2.44939 | -60.76086 | 2026-09-05 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4378affc-a0f7-3c1b-8553-ddb18f9cca0a | -3.13708 | -61.21555 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2689f7f5-808e-3e0c-be54-37465c9e17af | -2.813 | -48.6745 | 2026-09-05 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 982bf253-e788-3a56-87f0-18919b50f571 | -2.91378 | -61.00306 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0a0704b-7372-32e7-9eff-fbbc082f9eca | -3.93392 | -59.34311 | 2026-09-05 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0f29f1e7-af22-3d3a-836d-13da66cdfde2 | -3.79593 | -55.87734 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3420108b-d437-33db-bb78-c9fb7acdf6ac | -4.36356 | -47.77687 | 2026-09-05 05:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1644eb0d-3ba7-38f9-8e1d-a6f9195705e7 | -3.12373 | -57.69199 | 2026-09-05 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a69566b-e68b-3819-8003-a0bb514bbdd2 | -5.21119 | -60.03051 | 2026-09-05 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 378b6f35-32f0-3f70-bca2-f4ef7955aebc | -5.33928 | -56.02134 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 25b5e0df-e6c1-3e31-bd99-e63823f22fa9 | -5.84997 | -52.0396 | 2026-09-05 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6326704-9550-3a21-85ec-5857f0a3d811 | -6.66144 | -59.95242 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1cc5b5a1-fee4-3e84-8c26-2197008cffb9 | -5.76428 | -59.18112 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f2cb5db-bfd7-3e71-af3d-06d341840683 | -6.12293 | -59.95908 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b8ffe5e-3b79-304e-8677-8e1a3c5d7bcb | -6.13425 | -59.88669 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 64622416-b997-32b0-83f3-f8d49bc9680a | -6.68626 | -59.93547 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a4a442fe-ed80-3c3b-9e38-8fd10f80b24f | -6.65277 | -59.93923 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2080aa4e-08de-3242-b574-950d84872501 | -6.59115 | -59.92189 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21bd25e3-4b48-3134-a5ba-bebb24617c99 | -9.54857 | -60.83463 | 2026-09-05 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b51fd9f8-5a40-35b7-b1c0-16b32bccfb08 | -8.86456 | -68.49078 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65c0e013-904b-3028-a442-e31bd6794b91 | -9.18952 | -68.26262 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8dfeaea-82f8-3a34-a238-e6bc370b7968 | -5.46832 | -60.05755 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74561e42-67c0-3401-808b-f340a6a5279a | -5.65026 | -60.23689 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29845945-63e6-39f7-bbd8-9a857ded1fc0 | -6.6731 | -59.94634 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6424b5b7-fc34-3916-b0a1-b0c9e7c1f4cc | -5.46215 | -60.05663 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3b5c621-0ea7-332b-859c-3a72b3f81555 | -6.03372 | -60.16891 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66b8dbc8-abfb-333f-a4d8-c74a916d2b30 | -5.46617 | -60.05343 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 849cde97-4fb3-3271-8a14-2fc5da65b154 | -6.2021 | -57.77085 | 2026-09-05 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ff091bd7-230f-3192-8be4-2496699c7662 | -7.55467 | -61.34329 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc77d25d-652a-3fe1-b0b7-75072d87569a | -6.58942 | -59.90977 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98fdace0-010f-3c6d-bb58-4b36144b6599 | -7.26104 | -61.10041 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54cbd197-bd6e-34e3-afb9-34370173d2b9 | -6.64749 | -59.95023 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edbf8b01-1a73-35ac-9880-9fbec377a7ac | -6.02626 | -60.17158 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7104f84b-7462-31f2-9eff-daeba79072de | -6.67751 | -59.96953 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bff22f3-90a3-3409-85d1-ad18f726f09a | -5.66317 | -60.24215 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86d43fd5-99ae-3fa9-93e1-98ff6c0b2430 | -8.74673 | -69.23036 | 2026-09-05 05:42:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7253424d-6449-31d3-a773-c078888d8b1d | -9.5365 | -68.63365 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 550aae08-7ac8-317c-a441-ad89795e8a2a | -6.11718 | -59.95044 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a83452e0-e79c-3a7c-8693-9d3edb125362 | -9.84439 | -68.97853 | 2026-09-05 05:42:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f70ccf6-f0ba-3c05-92a9-63ba3e083450 | -9.53299 | -68.62891 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81fc5561-40b3-3698-931a-5c8044cadc2a | -5.36704 | -60.1028 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9c358d8d-b762-3e2d-afc6-e586f5276bbb | -5.46545 | -60.05329 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ba69d96f-68df-3fda-86c9-2fd0ac4ef9fe | -9.52808 | -68.63211 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a404f842-791a-3073-8af9-fcf707af85ac | -6.52292 | -59.93978 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe1ed80b-7353-3100-bd13-29df7a0e0cf4 | -6.14909 | -59.93894 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdf36178-89c5-36ed-9a49-25ce13ec8580 | -6.12768 | -59.92869 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5799eb6-ca25-3da3-8df0-9f27b675ab91 | -6.65566 | -59.94363 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 51696747-b90e-388b-9eb8-194a371559f3 | -6.67403 | -59.94543 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce3fd97e-36d3-3efc-83b1-e6b280c7ff1f | -9.46874 | -67.42344 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5199c440-269f-3e98-8e37-56fbd011b299 | -6.67021 | -59.94196 | 2026-09-05 05:42:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4775fdd3-9cd2-3fd2-89e0-82ceefecfa58 | -9.55261 | -60.83136 | 2026-09-05 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e322d84-1f50-3f39-bd2c-e1ab6d3ee200 | -8.86877 | -68.49152 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9166694-9d65-3245-8192-cdae4aec16ea | -7.57426 | -61.32808 | 2026-09-05 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df0446fa-328d-325a-a49a-98f508e69a4c | -6.03774 | -60.16572 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 501ac3fa-dee1-3be7-85e1-399756ae1938 | -9.13343 | -67.81149 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c084a43-a342-301b-b581-34dae3532e13 | -6.14851 | -59.94276 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| df28d282-c8bc-3d8f-a802-09717f97dc9d | -6.14968 | -59.93512 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d149b779-9587-3714-b7f8-2cd54f66b14e | -8.96869 | -69.27528 | 2026-09-05 05:42:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b5ad0591-af35-35df-8d25-435e0c111766 | -6.66263 | -59.94475 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 365e3a1f-625a-329d-90dc-ff3c25433536 | -6.65217 | -59.94308 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 484a3028-b719-3d01-afa5-9dfaa73b1855 | -6.03028 | -60.16838 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2f10d4a0-f827-35a1-8e25-b76cf90b698e | -5.65347 | -60.23685 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 556e0936-251b-3fa5-965a-f2b97ac01151 | -5.45988 | -60.04865 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8e174a7-221b-3bef-b586-dbfba1816ce8 | -6.69087 | -59.9755 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdc6074f-0045-3656-9fd8-af94468bb121 | -6.37444 | -58.2883 | 2026-09-05 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 016fb83b-a3dd-30a9-98ab-2a48e9916094 | -8.5438 | -67.15977 | 2026-09-05 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8113e6b8-3e26-3fbb-9ee6-10aef4868897 | -6.13346 | -59.92485 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e725b96b-a85f-3106-8a66-76eef85d898c | -6.681 | -59.97006 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d197db3-01d9-3dcc-8e56-62805152ee73 | -6.68158 | -59.96622 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b0287b7-8344-35d4-96d7-ee37ad2f2b6a | -6.12362 | -59.93196 | 2026-09-05 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78f1d50e-17fc-3d9e-9ded-df7f734bc98d | -9.9886 | -67.57458 | 2026-09-05 05:42:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README30.md)
