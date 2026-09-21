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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 121ad012-6cb4-37b0-a7b3-82d46f391bd7 | -7.59249 | -57.66738 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f5802bac-7bca-3ec2-91c2-ea5b78aa1158 | -6.44977 | -59.96902 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| dec765d3-ae5e-377c-8a2f-6abf25dd8d22 | -6.15496 | -57.71169 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f3d7464-a3d8-32a3-b1fd-cbbc0cacb1ff | -7.57157 | -57.6837 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 765cdebe-50bd-3c73-9ab6-7a95c80c4b4f | -6.7549 | -59.06398 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 960a768a-3152-3ed5-96f9-619a1a86c93b | -6.69064 | -60.0133 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 026d1e51-a517-36ca-a15d-199d6924c60e | -7.59734 | -57.67768 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3ad1acff-8bc0-39d1-bf77-fcf06baabffb | -6.30479 | -60.00999 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a69186e4-c284-394c-8767-f01a935665d4 | -6.30423 | -59.94016 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6ed00b0-073f-3d6c-b37e-76e2e5e3e2a4 | -9.22333 | -71.8677 | 2026-09-21 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f292852-950e-3c10-b0dd-048f7d4b9ae8 | -6.13846 | -59.94463 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ff34da9-e0de-3ab0-86c0-8e4d8a47ff74 | -9.54896 | -66.02013 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9bef6490-db48-3ee7-8698-83d7c4a1fc0e | -8.7957 | -60.79802 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04f0cbdd-eeb6-3ff0-b326-e05158489483 | -7.80847 | -61.80679 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b432f41b-8300-34e1-a42e-d226e618dd2f | -9.5511 | -66.0554 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68600d6c-a2a0-3d02-83d3-d5eb197e4355 | -8.86002 | -68.51235 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 630137c9-a3ad-3525-8bbe-a4112a40c781 | -6.46548 | -59.97812 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ec9d31a-0f8f-332b-94a9-0364f957abd1 | -6.74559 | -59.41847 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7e8b89f9-3a4d-3e99-804f-d93e297d5e6e | -9.64343 | -67.49105 | 2026-09-21 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9fdaa31c-c051-3c67-86bd-1ca33f364e36 | -6.09547 | -57.68353 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fce0b6b7-95dc-359f-b3bb-d61bd4645d77 | -8.65562 | -62.48656 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9af9cadc-3086-3ca2-a81d-d88300d5b96e | -7.12712 | -59.65376 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cec86f5-d60c-3101-9055-f9963668ac15 | -6.10326 | -57.62805 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bf77a76b-17d3-3c11-a348-9a594fe2467b | -7.4847 | -64.70624 | 2026-09-21 06:01:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e9bbb12-d3c9-376c-8b16-9df69f4e3b50 | -9.55533 | -66.05473 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee9f9d3b-b8f4-322f-aa86-93126ffc13b3 | -6.45421 | -59.98315 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55d4ac8b-dbb1-3d16-a9c2-a4c6e6d18d06 | -9.42642 | -68.75674 | 2026-09-21 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c68248c2-f228-38ce-9689-10a01e2f1c5a | -10.46063 | -61.31489 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 032cd43e-762c-3043-b663-b541cd097727 | -6.74936 | -59.06317 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d52ae80-3093-39a1-82c6-415adb8d38f7 | -7.33765 | -55.61604 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 014c83bc-e124-37f9-b6ee-d054d4354482 | -9.56333 | -66.04846 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 892c1b52-57c0-31a7-9d91-969a47e936c6 | -9.55474 | -66.05595 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 15697344-3afd-30e2-80cc-71d3d2d74d53 | -6.45033 | -59.97291 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dc72aedc-cd4f-3819-b287-c0481dfb1acd | -6.46028 | -59.97747 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af03dc50-2733-31ad-abb1-c14d4099f36e | -6.30663 | -57.7395 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ca62a51-3211-3f01-9821-6a477cd236e3 | -6.72446 | -63.12568 | 2026-09-21 06:01:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9a5d5fc3-2d22-3548-8e82-7cde4c75cfb6 | -9.55756 | -66.01262 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 713acab9-6c0d-3e43-bdec-47979303c499 | -9.03163 | -61.66078 | 2026-09-21 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45acba55-ff88-3c66-9fa6-be490349ec81 | -6.64871 | -59.96592 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7bce88d-f7b8-33c2-bee2-24bbecd15f8f | -7.57769 | -57.68455 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 42341f83-e919-38f3-ac3b-d8075c31e8e3 | -9.22268 | -71.87164 | 2026-09-21 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7f6363e-3936-314c-a177-ee52dc818e69 | -10.20885 | -68.74651 | 2026-09-21 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 218a4776-6f46-30b8-8832-8688f2a1d03c | -9.56626 | -66.05634 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5edeb46-a1bf-331a-9478-b631cfa9c631 | -9.5523 | -65.69436 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a42e915-4197-3c20-a63c-fe74a2b07ba0 | -10.45561 | -61.31415 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c9f73bf-bd4b-3d2e-b66f-881af895e6af | -7.32605 | -55.21376 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 950a4303-a3a2-3267-af5d-17fa9917e1ef | -6.2814 | -57.74497 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7cfe01dc-b3c5-30f9-b3ea-c5da9d5959b6 | -10.89292 | -69.34293 | 2026-09-21 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 064f511c-9417-369f-a3b5-e6464e2b9fb7 | -6.73247 | -55.09173 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 084f3e69-0dac-324a-ab88-b10aaab0f64b | -6.44887 | -59.97517 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 001d6251-32e9-3272-b738-d5f81c6de673 | -6.45509 | -59.97677 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dbe39ef9-1dcc-377e-addd-861726e63fef | -6.96463 | -71.7599 | 2026-09-21 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3196d995-01da-39a7-837f-aa5e27c421f3 | -6.4443 | -59.97828 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 847f9932-ef85-3f9f-8ed2-333c2c2d850a | -10.61981 | -67.92779 | 2026-09-21 06:01:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8767572b-9e61-389a-90bf-2b0657953dc8 | -6.3323 | -60.0153 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b10bc3c-fa9b-3282-b5d7-98a00744eed3 | -6.13803 | -59.94771 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 572a53f7-35ce-3d06-a645-a89402e4df84 | -6.13652 | -59.94609 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc51fbbd-9846-37fb-96bc-83ae424d632a | -10.70851 | -69.43515 | 2026-09-21 06:01:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f0031ad-c290-3f90-bda3-d8d39e21d0e9 | -7.24811 | -55.60149 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b95a54dd-8f65-3b1c-a7f1-7b6bfac50566 | -6.73728 | -59.42433 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eee39a1a-c6fe-3300-99c3-912da10844f3 | -9.55004 | -66.03773 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aee92223-104d-3c74-a62f-4af630fe709a | -6.14363 | -59.94546 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 235e12f8-20ae-3683-b203-0e1e12ff507c | -9.56262 | -66.05579 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b400fe57-827d-3c9c-8c44-0a2474a63664 | -7.32815 | -55.22147 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b36e5996-892f-3236-a31b-872e156ef505 | -9.55456 | -66.00776 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eccc1cb3-29a2-3c9a-a105-ee1db4575931 | -6.82852 | -55.53651 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| f1dfa2c9-3adc-35bf-b066-5caacba0464e | -6.45406 | -59.97593 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 82bb2ced-9ec9-39e7-86d9-ac1feb28cf74 | -7.54633 | -61.32104 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4ee8c2d-1c8c-3274-b2ba-48e6d4d0af1a | -9.28005 | -68.36863 | 2026-09-21 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83ad6234-c69f-3709-9dbe-f664045b5501 | -6.82816 | -55.5366 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| d1aeb6c0-0c22-3bde-a955-fb6098a21a91 | -7.24684 | -55.61479 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b81f84aa-0f80-3be9-b9d6-a534b6d7bfd4 | -8.31055 | -70.56291 | 2026-09-21 06:01:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ddf74eb-1aa4-3294-aee0-0b18b1bffdf1 | -6.13134 | -59.94539 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76541775-9921-3ad3-a18b-5494072da8ca | -6.13889 | -59.94156 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79da70c2-a092-32c4-a77a-54714bfcedbd | -9.56689 | -66.05207 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a4a2b0aa-517e-391d-b899-a9a4c16a976e | -7.54716 | -61.31951 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa4f1560-2da4-313e-989e-2f7ebe563ae5 | -8.01678 | -71.14127 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b435254-664d-3030-8a0f-d36d1d3a8ac2 | -8.0162 | -71.23076 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88b3a389-eaad-3114-b512-360fea5d40b8 | -9.54725 | -66.00666 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef095f0a-bc94-335b-b7c6-01a31614ba1e | -9.1712 | -60.85479 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9be000db-da40-31cc-8839-c45609e74bbe | -6.75924 | -59.11325 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 593bdd41-7ff6-370c-ab2c-de0d8f60dfb1 | -9.27697 | -60.6313 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 209066fa-d05d-370c-a7cf-afcdcaf64cba | -6.33272 | -60.01221 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ff38093-d258-300d-9add-e5c9fbe0c0d9 | -6.45313 | -59.98225 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d414e7e-2aaa-344e-b404-60a5843e7ca4 | -7.58382 | -57.68538 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a0fbb471-f2c9-3e85-9f07-d2b1d3921f33 | -7.57707 | -57.68921 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c92e7038-f9de-3803-b81e-5dce349a4044 | -9.66901 | -64.5952 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7575bf68-18fc-3cf7-b67f-979eb5467160 | -8.04851 | -61.32834 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4bd01b2-7323-35a0-9e6d-fe5952293a77 | -6.7532 | -59.11618 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25e54517-e141-3211-a2e1-59d6417bac87 | -7.33145 | -55.60933 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7e2c9fc-f734-3a33-b7bd-4f6fae0663e6 | -7.5512 | -61.32543 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f5927eb-1681-3d2e-8590-c3f2071cb8fa | -6.13371 | -59.94083 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2362103c-ba6f-31ef-aac4-96cbd4011b55 | -6.14278 | -59.95155 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0163ddcb-5bb7-3ba3-b61c-20e451a37070 | -6.75822 | -59.12047 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9ffaf5f-fe20-3ed7-bbdb-75fd800f2bd8 | -8.86389 | -68.50936 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eaaa7eeb-18c4-3020-b4ca-e9ecca32b819 | -8.2411 | -62.84027 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ea2cc48a-22d3-38c7-893e-9fa653321051 | -6.13089 | -59.94844 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89660510-fa3e-3e22-9084-5c846f13ba24 | -9.55133 | -66.02918 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72a1f7ae-2600-3e9f-a0fb-045e1f44cb43 | -11.03689 | -68.50009 | 2026-09-21 06:01:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48e0ea55-721c-300f-b0f5-facd5079cb10 | -9.2869 | -60.63585 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README109.md)
