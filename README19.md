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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a84cdc17-e9fb-3835-894f-3cfb46d9dcda | -5.8894 | -57.7708 | 2026-08-30 01:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| fb51b688-93ab-3394-aabc-b8a2a84703d6 | -9.0615 | -65.4169 | 2026-08-30 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 826f0900-e1d5-3ce7-9585-772b44f8988e | -4.9603 | -55.8622 | 2026-08-30 01:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 1bfe2e6b-4174-338e-8f5b-1283f8e716ab | -3.6215 | -60.566 | 2026-08-30 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 09a14d59-1b9b-3919-906d-fc7bac2f2dc1 | -3.6398 | -60.5656 | 2026-08-30 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 183f1808-6a16-3e20-b85c-576e42a78a30 | -10.8253 | -45.3152 | 2026-08-30 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| c7bc3454-69a6-3f4c-b0b1-42044546d314 | -9.9114 | -60.2741 | 2026-08-30 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 8309a9fd-431d-3dd7-a6dc-2bbb7cc3d4c5 | -3.6399 | -60.5466 | 2026-08-30 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| ccc873a7-1d10-3cb1-9602-307a915ec946 | -6.9361 | -55.7157 | 2026-08-30 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 07e4e88e-ce9e-3546-ab44-a00a93cf781a | -10.9593 | -43.0326 | 2026-08-30 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a69fd7ae-c924-3813-988d-28d73694b989 | -10.8058 | -45.3407 | 2026-08-30 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 57e0c82c-7c6a-3d0b-9079-1a77c96cc6e9 | -7.5661 | -61.3239 | 2026-08-30 01:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f8206499-3c86-391d-a044-1bb722f139a2 | -6.9363 | -55.6958 | 2026-08-30 01:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c75b30cc-3090-3964-8dfa-a8b802d3845f | -11.3068 | -54.0299 | 2026-08-30 01:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 34435934-c9a0-3939-9c97-884cc7b760dc | -10.7407 | -54.0401 | 2026-08-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 19f1b7a1-53f4-3988-b460-805a61be80d2 | -9.8927 | -60.2752 | 2026-08-30 01:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 334f0a57-0e4e-3e45-b725-d2807cde2f91 | -5.4876 | -57.1416 | 2026-08-30 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 0c8d1c12-cf62-3319-8499-5cfd6e2bce36 | -5.871 | -57.7715 | 2026-08-30 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 2d531ec4-408b-3697-9112-aee6d10c54ae | -6.861 | -41.6772 | 2026-08-30 01:30:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 729477ef-15c8-3551-8af7-5f40463022f6 | -3.6216 | -60.547 | 2026-08-30 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 81ec4e51-8af4-3344-9086-923967feb46c | -9.9468 | -60.5232 | 2026-08-30 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 689b1f47-f072-3fe8-a4b8-ee84b2758d72 | -5.8894 | -57.7708 | 2026-08-30 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 5dd03b1e-970e-3040-be3c-650abca89e1e | -6.9546 | -55.7147 | 2026-08-30 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 2d331091-747a-3107-9ea5-cc7d8f3506c3 | -11.2879 | -54.0317 | 2026-08-30 01:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8e54bcae-936d-395a-8028-67201e51be66 | -10.7407 | -54.0401 | 2026-08-30 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5416aaec-884c-3b11-82f4-21c525c59916 | -5.4876 | -57.1416 | 2026-08-30 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e147fb0a-536c-3a81-98a2-533d1f62f2ef | -4.942 | -55.8431 | 2026-08-30 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| e1ef6850-ed10-39b9-9881-6680d87d4b92 | -9.0615 | -65.4169 | 2026-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| c3bf28b5-8aa8-3d71-8579-7f42d2a39261 | -9.8927 | -60.2752 | 2026-08-30 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 38ab138e-514d-326b-afea-ba7ea3d1fc3f | -6.9361 | -55.7157 | 2026-08-30 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 29d0a80c-8c71-3821-b02f-7d40b07afa92 | -5.4875 | -57.1611 | 2026-08-30 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 04870a52-3e53-3630-a162-7e2c4eea4a7d | -4.9603 | -55.8622 | 2026-08-30 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 71e94b32-c342-3ac7-8690-6334cd9bede9 | -3.6399 | -60.5466 | 2026-08-30 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a72b6478-0d14-39e2-a1e0-dda7e7718567 | -3.6215 | -60.566 | 2026-08-30 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 73490cdb-599e-3324-8927-f366d7845a5f | -4.9788 | -55.8417 | 2026-08-30 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 61c4d44d-64b6-389a-8eec-102f55610921 | -7.3117 | -60.6089 | 2026-08-30 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| cb65b2b3-ff49-3fb9-8b5a-c8312eae45d7 | -4.9604 | -55.8424 | 2026-08-30 01:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 135.0 |
| 77b62f01-70e4-3ac7-85e0-6cf177c3978f | -10.9401 | -43.0355 | 2026-08-30 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 23b5a585-42ad-3e41-9e75-c73d570e30c2 | -3.6398 | -60.5656 | 2026-08-30 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 1e77fb7b-bc2d-333b-8366-da234cb6497b | -9.043 | -65.4175 | 2026-08-30 01:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 224adf0d-f026-3fe3-add0-4b488c7b282b | -6.9363 | -55.6958 | 2026-08-30 01:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0f449db4-054f-3973-bb07-8da26e5b5551 | -7.5661 | -61.3239 | 2026-08-30 01:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| f54aa635-a0a3-3b5e-a022-70162dbd8b3b | -6.9546 | -55.7147 | 2026-08-30 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 62cc1ef3-750b-3f4e-acc9-89c1ca309976 | -10.8062 | -45.3178 | 2026-08-30 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 8ce58df5-78b2-30ba-81a1-770b7f11b8cc | -9.043 | -65.4175 | 2026-08-30 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| e3057a3d-4dc1-338a-8f2a-0ac4d56b2ba7 | -3.6215 | -60.566 | 2026-08-30 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| dbfa8fca-aa47-3f68-bb24-ca09fb2312d8 | -14.4287 | -58.4526 | 2026-08-30 01:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| cc0d783c-a679-35f0-896b-0c52dabb65b9 | -3.6216 | -60.547 | 2026-08-30 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 83110a05-59dc-3a5f-a805-c0be3d4125a5 | -4.9603 | -55.8622 | 2026-08-30 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 57e7666b-95a4-3a7f-9108-2a121e823fe5 | -9.8927 | -60.2752 | 2026-08-30 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 089b1c66-007e-3d59-9851-cfcfdbab2182 | -3.6398 | -60.5656 | 2026-08-30 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 6c786f16-5496-3979-8fe7-e8060a38569c | -4.9788 | -55.8417 | 2026-08-30 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ca7eff13-791c-32af-870d-50fe80faf3b3 | -6.8799 | -41.6754 | 2026-08-30 01:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 80.5 |
| ef52cb42-1c9f-3163-8fa2-0e91b848ea7e | -7.5661 | -61.3239 | 2026-08-30 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 914e3abe-4cde-361b-a8e9-544262df3815 | -5.4876 | -57.1416 | 2026-08-30 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 5a421d7b-4a3c-39ac-b0e9-f2b628d4a602 | -10.7407 | -54.0401 | 2026-08-30 01:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7d49b19f-de95-3a58-85df-b161779d4ad7 | -6.861 | -41.6772 | 2026-08-30 01:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 144.8 |
| 7ba32069-9b21-3b38-82cd-57c86d66c873 | -4.9604 | -55.8424 | 2026-08-30 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 187.8 |
| 6f8111c1-55d7-3052-9001-1bc3ab229677 | -7.3117 | -60.6089 | 2026-08-30 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| da95d2d9-b9e4-32e5-96b7-b7aa82f5e4f5 | -3.6399 | -60.5466 | 2026-08-30 01:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| c26a7c6f-c022-37eb-be72-e47d06b32be1 | -5.4875 | -57.1611 | 2026-08-30 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 017b2ef6-b2a9-38b8-a915-226f9a1e30c3 | -5.8894 | -57.7708 | 2026-08-30 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| b435fd72-113f-3d56-8a78-6ecad1547324 | -4.9605 | -55.8226 | 2026-08-30 01:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| eaa730e7-0b8d-3092-b104-47156dfb56bb | -6.8613 | -41.6532 | 2026-08-30 01:40:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 7b6452c0-62ae-3f70-a3d0-e82b12a034c9 | -5.871 | -57.7715 | 2026-08-30 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 50622ed9-e0a2-34e6-bceb-8fca7fb66d4d | -9.0615 | -65.4169 | 2026-08-30 01:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 63f28e97-0380-3804-a007-abef4b735e1a | -6.9363 | -55.6958 | 2026-08-30 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 840a92bd-6f22-3b49-97a1-858fddec3381 | -6.9361 | -55.7157 | 2026-08-30 01:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 16208f27-8e1e-3169-99a1-08cd913f3d37 | -10.7407 | -54.0401 | 2026-08-30 01:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ce5067ba-28d4-3866-81f9-53f617acc0f8 | -6.8799 | -41.6754 | 2026-08-30 01:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| d88315e7-5caa-3118-819a-29397e057769 | -11.2879 | -54.0317 | 2026-08-30 01:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| fa62758f-e5e2-3911-9d79-925b14768722 | -3.6399 | -60.5466 | 2026-08-30 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 790047cc-4f1c-389a-942a-c92309233763 | -4.3772 | -47.7844 | 2026-08-30 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b4ab574f-e096-3104-91bf-179afd267378 | -3.6216 | -60.547 | 2026-08-30 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e436289c-7c83-3840-815c-2dadc1e235fb | -4.9604 | -55.8424 | 2026-08-30 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 196.9 |
| 0d882838-4021-3d84-8411-3e17f84bf98d | -9.0615 | -65.4169 | 2026-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3bceae4b-6532-351d-8593-ad677b9e4fac | -9.043 | -65.4175 | 2026-08-30 01:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 7ccf341d-9370-3f9f-9044-aa393125ba7b | -9.8927 | -60.2752 | 2026-08-30 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| db2a7472-bb87-31a2-a386-540f047690ff | -4.9603 | -55.8622 | 2026-08-30 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 85f7a4d4-ce0a-3f92-bf8a-052517426a75 | -5.4876 | -57.1416 | 2026-08-30 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 06288904-ee55-3fce-9edf-5aa1d1eeabae | -4.3774 | -47.7627 | 2026-08-30 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a1d184c7-65eb-32fc-929f-2c22cd943301 | -5.8894 | -57.7708 | 2026-08-30 01:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| fa1c31f8-963d-38d8-bd76-9ca702b0ffc5 | -6.9546 | -55.7147 | 2026-08-30 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2e29e9ea-f07e-3fa6-8505-4288e5764973 | -7.5661 | -61.3239 | 2026-08-30 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 38.3 |
| e9bd7abf-2c4d-3ff6-9937-35617d1b54f0 | -6.9361 | -55.7157 | 2026-08-30 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 1da26f83-181a-3a8b-ad28-44e82ad1d861 | -3.6215 | -60.566 | 2026-08-30 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7727a71b-f7fe-3346-983a-086a0843453a | -4.9605 | -55.8226 | 2026-08-30 01:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 297be501-e53d-3e6d-abe0-d1c72bc2d129 | -6.9363 | -55.6958 | 2026-08-30 01:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 6af7ff44-2c76-3b3e-a6ca-590773255325 | -16.3531 | -50.9775 | 2026-08-30 01:50:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| b822551c-d558-3b74-8ba2-9306e5a5ab7e | -3.6398 | -60.5656 | 2026-08-30 01:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 93a8d5a4-6f7a-3c7b-97ab-8ebdc48f5bbf | -6.861 | -41.6772 | 2026-08-30 01:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 1324172c-57e9-320a-bbec-5f5767863be3 | -10.8062 | -45.3178 | 2026-08-30 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 4b03dfc8-0237-31a0-b0fb-4d53254cc977 | -7.2377 | -60.6309 | 2026-08-30 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 215c17b6-0f7e-3f11-ad7e-2575b40b59f8 | -4.3588 | -47.7636 | 2026-08-30 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 314d094e-8d37-3ce2-b1e0-5b7f5bc8529f | -6.8613 | -41.6532 | 2026-08-30 02:00:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 9213628b-af59-316d-a7de-c65483772692 | -6.9363 | -55.6958 | 2026-08-30 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 169287a6-8217-3f88-8b68-346dc332263d | -9.0615 | -65.4169 | 2026-08-30 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| d6695093-e8c4-3c42-a7d0-7a1c3956724f | -5.8894 | -57.7708 | 2026-08-30 02:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 33cf486b-f586-3abc-94cf-0eb4a0691a39 | -11.3431 | -45.1521 | 2026-08-30 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| f4833787-07c8-31cc-8818-4f6c7c1ce881 | -4.3587 | -47.7853 | 2026-08-30 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |


[Clique aqui para ver as próximas entradas](README20.md)
