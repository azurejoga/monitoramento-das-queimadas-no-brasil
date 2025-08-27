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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 947a9090-5e5c-305d-86af-8d036b03e86a | -10.08613 | -62.89989 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7732d7d8-1f58-33ae-a33b-fec076be09e6 | -9.60315 | -64.44527 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04731179-9e33-3717-a592-d6457fa3a382 | -9.03934 | -65.73064 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9af72d4b-c091-3749-90ed-69cc5631cb4a | -9.02937 | -65.72905 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3824a54-47c8-3afa-9906-f59146838569 | -10.04252 | -64.89482 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abc07246-86b8-3580-bb53-c48673e5f852 | -8.9851 | -65.4321 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68f0f046-8df7-3d87-9e39-7af24c8be359 | -9.07165 | -66.06161 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d95f118d-267c-3fef-9e3c-42b30ad52444 | -9.79431 | -64.24475 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 17e1729d-268d-3e25-8c51-3ec25303a7bb | -9.64852 | -64.99067 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb16babf-34d0-3db4-b66b-56e7b5e23ddc | -10.2877 | -64.50449 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6272d16a-9e39-3775-8eef-27fcb5b96b2d | -10.77547 | -60.78674 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81f0a0a2-e8ae-3fdb-a39f-7f74aaece7c8 | -9.08591 | -65.7344 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6fadfe2f-c952-33bf-8887-8c6821615597 | -9.81083 | -64.29655 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4eeadd2-3ee8-3a63-b8b9-b037013dd3d3 | -9.08495 | -66.06374 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c461700-103d-3c03-8b06-04949cec59a0 | -9.08646 | -65.7309 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3771b3c8-d0a7-3745-a8cf-495ef08d9bdf | -8.92187 | -65.9197 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0aa0fdc-4675-3c8c-9695-baf0af452b93 | -9.06777 | -66.06457 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14f3e330-39a5-357b-8c06-c1c18419bc35 | -8.92132 | -65.92319 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7529c621-8e5e-3940-95f6-3f0012751cec | -9.8057 | -64.26169 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bc2c9af-deff-3209-a360-33e60fb24e54 | -8.99726 | -65.39815 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e25e71-0dc8-30af-b286-9ca4e73428d5 | -15.62537 | -52.72639 | 2025-08-27 05:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a53f067-79a8-346f-9b32-7b393def825f | -8.93809 | -65.93999 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e39721ba-8588-39ce-add6-23346046cdc6 | -11.30634 | -55.11485 | 2025-08-27 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13507e22-f46a-3403-aca4-0c20ae74041f | -8.10848 | -71.25281 | 2025-08-27 05:46:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86346f4d-6ca2-3948-9e44-687d71c5f641 | -8.95915 | -65.9577 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| aa10b8bf-d161-3eae-900d-8f98d56dc229 | -8.93074 | -65.92828 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56fd86a9-329b-35ae-811f-e952ebd7fbd3 | -9.09033 | -65.72794 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b40490a4-db8f-309e-b802-ba80a7082a52 | -9.67553 | -67.50089 | 2025-08-27 05:46:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe783b19-d5f7-3628-9243-c1edeb3920a7 | -10.08854 | -62.90863 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01fbe9f7-0426-3ce5-b3c7-19b481122678 | -8.96248 | -65.97972 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d916e52b-ba65-38ca-ad2f-96e52b298992 | -10.2843 | -64.50396 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5941e232-fe82-337d-95be-eb8a7a2adcdf | -9.0266 | -65.72503 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bdb9196d-c25a-31a2-a669-e70739a075bb | -10.08915 | -62.90452 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9e42a429-d89e-36fe-a3b6-1f30cc4cc402 | -9.80399 | -64.25005 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc0e3305-4dfc-3fff-a517-e6d14fcf54da | -8.91799 | -65.92265 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80b84937-181d-351f-8f3a-415f294e06d1 | -9.60938 | -64.44998 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c8be8f9a-5e41-3d2b-8391-71cf0fac9af4 | -10.27806 | -64.49922 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 349df43e-e61c-33ae-a3e4-579656f6f02f | -9.04267 | -65.73117 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1123ac22-fccf-3149-b967-a5048d381399 | -10.77186 | -60.78239 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2904ba8-7d5d-330d-a370-8b4537a6a397 | -10.08553 | -62.90396 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 13687fc7-2728-37e4-8762-cb837fdd2249 | -11.69496 | -60.16949 | 2025-08-27 05:46:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 246ca5fd-5408-338e-bfbb-d04d531551df | -8.94252 | -65.95503 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 5166b3a2-169f-3c5c-9a1a-0bca49fb5598 | -10.09699 | -62.90149 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04748eee-c8db-3b41-a731-f7c0917c599f | -8.95749 | -65.96817 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| aeb4f8a2-baec-3e9c-bd32-0aa03e64ae75 | -9.64742 | -64.9978 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a40fe78-8f44-3ccb-88f0-7e94a53a8356 | -10.08312 | -62.89523 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b23c0da6-96f9-3e28-93ef-e7adc75ff0a5 | -10.27182 | -64.49448 | 2025-08-27 05:46:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 90334b24-3d18-379c-a9e3-1efaa21b10a2 | -10.10062 | -62.90197 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59fa2c79-f53e-3022-a0ab-f8de4b2d64f4 | -9.80058 | -64.24952 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e811cb4-c79a-3f5d-99cf-f0b89ece98bd | -10.5194 | -57.9857 | 2025-08-27 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c139fab-b526-3005-953a-a06d37564e3f | -9.64797 | -64.99423 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cc14e397-e4c9-3b81-8d95-f02e1d7b4d62 | -9.80799 | -64.29233 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91a806d8-b035-326e-a8ef-1d76b2b15883 | -9.61784 | -62.26427 | 2025-08-27 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f45f307f-6c69-3cac-80e8-841c5d3f1cbb | -9.05319 | -65.72927 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c2d79e4-2972-3d03-a5b9-356d302a9c46 | -8.95638 | -65.97516 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b4a5b81-9d4e-3d6f-899b-966f1073389c | -9.08701 | -65.72741 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4e15127-b3da-381b-aa76-7340cecdf4ef | -14.30504 | -60.35923 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03cf5e70-afab-3136-a969-5e23fd180b49 | -9.00116 | -65.41671 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 129db1b4-7ebe-3ba7-b6b0-fb7e8d3d9fc7 | -9.1209 | -67.70821 | 2025-08-27 05:46:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51b06319-97bc-3112-a2ad-abacd29f837f | -8.92797 | -65.92426 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb42a610-8d8f-3e79-94da-0f5fa2efef39 | -8.10006 | -71.2514 | 2025-08-27 05:46:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97ddd54a-73be-3c33-b381-e2b9f009a914 | -10.17677 | -69.00591 | 2025-08-27 05:46:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4795a41b-6696-3a8c-bea2-1251dd9b358d | -8.50311 | -69.79968 | 2025-08-27 05:46:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a41c07d-0651-3a82-b989-bbcae577d4b0 | -12.07947 | -63.15131 | 2025-08-27 05:46:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f383f59-a855-30c9-bae2-7cdb95ce7bc0 | -9.79148 | -64.26328 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f79e6ad-0470-325d-bcc5-a3ff9dd68164 | -9.80798 | -64.24688 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7b13e14-6734-3cfe-aea4-84d60d8ebaa1 | -8.93019 | -65.93178 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ad7a01a-2410-3b10-9b40-13518d678e8a | -11.69438 | -60.1737 | 2025-08-27 05:46:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a30541c5-e955-3422-909b-5f2d6c32cea3 | -10.7766 | -60.78968 | 2025-08-27 05:46:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d5ec256-7f6e-334a-bfc5-38289c1904d2 | -8.96358 | -65.95124 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c588b033-ab76-3804-8b9f-0bc2fd539bcc | -9.13749 | -65.28 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1486078-1f11-3b6a-8878-c3b000e7aaa9 | -9.13804 | -65.27648 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6baedfc7-a42b-321d-abfe-6f3541e4b5af | -8.96081 | -65.9687 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| de03ba43-9724-3eae-ae9e-3f171521f0d6 | -8.94751 | -65.94508 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61da1d15-0604-351c-ae5b-2c5b42d75914 | -9.71347 | -62.39833 | 2025-08-27 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18688bf2-b1eb-3c33-8197-749b949697e1 | -9.07498 | -66.06213 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d115ebe4-752b-3f63-8d2f-4065c1c4d5e3 | -8.94585 | -65.95557 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| c4e77728-e5e4-383a-a6f3-98edcdb7cf64 | -9.75753 | -67.53332 | 2025-08-27 05:46:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1db83e36-8f2b-3955-8480-ff706fe3fd56 | -8.93587 | -65.93248 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6369daea-8aae-3d6e-869f-16d2d4e3dc16 | -14.76894 | -59.72687 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9f3c40a-ff77-3ca1-8d35-e8a06fb759d8 | -9.69445 | -65.71648 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 667da014-cd46-317c-97aa-4d630cace6e7 | -10.10001 | -62.90614 | 2025-08-27 05:46:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0021b3d8-ed84-3d98-a7a6-427fd30911ee | -8.95361 | -65.94965 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd22bccf-8323-3409-b239-7e65addffb96 | -8.10915 | -71.2489 | 2025-08-27 05:46:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea96d22e-6897-36c1-8753-9a1806ab6e97 | -8.10982 | -71.245 | 2025-08-27 05:46:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77093e19-df16-3b1b-81ef-d9897c3f86d5 | -9.65692 | -65.00294 | 2025-08-27 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1852574f-aae0-37b2-aafa-4aa4fca36dda | -14.77146 | -59.70609 | 2025-08-27 05:46:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 88d3cd6c-4999-3514-9771-080c68956bf8 | -9.70225 | -61.28695 | 2025-08-27 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e912e76-e202-3f60-9e2c-43f978486113 | -8.95305 | -65.95314 | 2025-08-27 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d5e63082-67a2-34b7-a6a7-fd24d7b44b1a | -10.0977 | -62.9085 | 2025-08-27 05:50:00 | GOES-19 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5c550e36-cecb-39d0-b1d5-3d55f59df12d | -14.4105 | -51.9482 | 2025-08-27 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| aa28c999-9789-3859-8d49-b531d4921e76 | -9.4064 | -60.5133 | 2025-08-27 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| f7447f3b-bff0-351c-9058-76fee346afc6 | -6.8412 | -58.9746 | 2025-08-27 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d9092632-e048-3ff9-95ca-5b3c628ea22c | -14.4109 | -51.9269 | 2025-08-27 05:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 658a902a-a85e-3337-8f1c-6692305ef572 | -9.4062 | -60.5326 | 2025-08-27 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| f5c88186-ac1e-3d17-98c2-bc62d6531344 | -13.3838 | -46.9017 | 2025-08-27 06:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 1c01e7e5-efa4-3dc3-a84c-304743f55e93 | -9.4064 | -60.5133 | 2025-08-27 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 55fdaa90-df3a-3479-ab80-042ae2ae0f12 | -6.8412 | -58.9746 | 2025-08-27 06:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| bea85b10-6cce-3da0-a58e-25b1b34b990d | -9.4062 | -60.5326 | 2025-08-27 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 8c419c99-b6d6-39f1-8099-1b5ba6128972 | -12.7843 | -48.1321 | 2025-08-27 06:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |


[Clique aqui para ver as próximas entradas](README81.md)
