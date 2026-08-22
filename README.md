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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ac5093d-6783-346c-99a6-cad9786aa33d | -8.1574 | -46.7247 | 2026-08-22 00:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ae322359-e8da-38b2-99cc-4ba44d1a915c | -8.522 | -54.8209 | 2026-08-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 313.5 |
| c66e0a94-eeba-3d48-bea0-f7a462fb03f5 | -14.1807 | -53.0142 | 2026-08-22 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 0d23809c-a9bf-3379-bcda-b196e70616c6 | -10.6941 | -50.2814 | 2026-08-22 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 196.0 |
| f69d943f-c4c2-3923-b30a-b165dd274402 | -11.449 | -44.5587 | 2026-08-22 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| b22022e9-153f-3c4f-887c-5a3c8f64d052 | -6.8373 | -59.6689 | 2026-08-22 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9863c0f3-349c-3e27-a65c-f25103f9ec2c | -6.5487 | -58.522 | 2026-08-22 00:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 27947cf4-ff07-378b-afd5-5b15c747939b | -8.5218 | -54.8411 | 2026-08-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 283.6 |
| 32500eee-c4f6-3056-824b-968fb0cccb40 | -10.2587 | -50.3478 | 2026-08-22 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 169.6 |
| a1af8f4d-7dea-30da-a387-14aae2e1b1ed | -4.8966 | -45.2538 | 2026-08-22 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a3d0567b-8ed0-3d15-8c05-dd193c322e04 | -8.9042 | -60.5385 | 2026-08-22 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 113.6 |
| c4b0a435-f294-30df-a11e-516de55a1b76 | -10.2584 | -50.3692 | 2026-08-22 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 8404154b-b850-3bb3-9504-d768ca3cc31c | -10.6752 | -50.2834 | 2026-08-22 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 231bbb41-f752-38df-82ed-0e4f54458a30 | -11.4494 | -44.5353 | 2026-08-22 00:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| ce5b2f4c-2e07-3124-a9d1-1f1732720507 | -10.2776 | -50.3459 | 2026-08-22 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 2689be7c-3dce-365f-8198-a980ed971542 | -10.6944 | -50.26 | 2026-08-22 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ecf4f27b-2ab3-346b-87a8-2e2a087c7615 | -6.2712 | -62.5231 | 2026-08-22 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 113.9 |
| c5980532-2536-35c7-be95-0b572fb79907 | -2.5042 | -48.1366 | 2026-08-22 00:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 85f1ede9-e7d5-346a-858a-10b429c93bcd | -6.3862 | -54.9651 | 2026-08-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4d9959e0-2b42-306d-baa7-aba340a92cb2 | -10.2398 | -50.3497 | 2026-08-22 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| a0ec2a50-ad60-3df4-9276-8f2c3bab56d4 | -6.2528 | -62.5236 | 2026-08-22 00:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 437cb015-5d06-35bb-9b66-e3d7d1b7c3d1 | -8.9934 | -50.7427 | 2026-08-22 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| 5a19e97f-3fa9-379e-ace6-90c1b36f1e5a | -8.9936 | -50.7215 | 2026-08-22 00:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 95b2f927-1c15-312f-832b-e391a977cfe4 | -7.3625 | -55.673 | 2026-08-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ba8b96ba-905a-3aec-af50-53a61e7484e4 | -6.3678 | -54.946 | 2026-08-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| b9854770-5817-3cff-9cc0-e0f57dd53386 | -13.997 | -53.6853 | 2026-08-22 00:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 8a9bdec0-6049-3ed1-b4c0-7e843c922204 | -21.6056 | -43.9964 | 2026-08-22 00:00:00 | GOES-19 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.0 |
| 3ed188db-f907-368c-afd6-bca17f962965 | -7.344 | -55.6741 | 2026-08-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| fbd62553-55bd-3b75-8de4-3ca36dcb2f4c | -6.8188 | -59.6696 | 2026-08-22 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| e9a6750c-291f-3f9d-adc7-d3c3e5f88a9d | -6.8593 | -59.0318 | 2026-08-22 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 3ba1bc96-8d2b-3657-bf42-859bc18e307e | -14.1804 | -53.0353 | 2026-08-22 00:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6c72f05a-0376-30ea-9c6d-5336b7940733 | -8.9041 | -60.5577 | 2026-08-22 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 21ff3bf3-022a-3ee7-a82e-9816611f055d | -10.6749 | -50.3048 | 2026-08-22 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| fc18d574-56e9-3e83-aa45-5d9d90d78d0c | -4.9153 | -45.2527 | 2026-08-22 00:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 83b29e28-de21-3aec-b4a5-cb66de48ddc5 | -6.7195 | -48.1201 | 2026-08-22 00:00:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 98.7 |
| a3e4c2bd-1c28-319c-9bad-5bc3062d9b94 | -16.4971 | -47.9344 | 2026-08-22 00:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 7dc01d91-a140-309b-be29-d43ae1437411 | -8.5406 | -54.8197 | 2026-08-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 236.5 |
| 13e2bad1-734d-3d5c-a875-08b3356c1fe8 | -8.5404 | -54.8398 | 2026-08-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 199.9 |
| 886628f4-0d7e-3b11-80d9-aa6f7eb8d15c | -16.4773 | -47.9381 | 2026-08-22 00:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 960cfdab-14fe-3164-b18e-3cb5b6addee0 | -6.8008 | -59.5934 | 2026-08-22 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 3e6aecbc-c739-34cf-8245-9a03e0d312d4 | -10.2773 | -50.3673 | 2026-08-22 00:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| e3d9cf99-abb9-3403-abfc-795b98e2723f | -8.8856 | -60.5394 | 2026-08-22 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ebef981d-d2c5-395a-8037-5bb28520d76b | -6.9315 | -59.3184 | 2026-08-22 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 64160b8c-b899-3aa4-a6d0-2503fd9f0ef6 | -10.6938 | -50.3028 | 2026-08-22 00:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1ce65a71-7032-379e-935b-2b5c336d9f8b | -7.3624 | -55.693 | 2026-08-22 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 44842c22-cdb2-3a5c-a9e3-4b6c4473e162 | -6.3863 | -54.9451 | 2026-08-22 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| fbfba1bc-3008-3fa2-b57d-72a9c495da90 | -6.7195 | -48.1201 | 2026-08-22 00:10:00 | GOES-19 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 1af5ff9b-451f-334c-90f0-e109d1244656 | -4.9153 | -45.2527 | 2026-08-22 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 1c48bd27-8055-394f-930d-33b93651ce90 | -8.5404 | -54.8398 | 2026-08-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 261.3 |
| f753a923-07d3-31d8-9c5c-9fa381de8e58 | -10.2776 | -50.3459 | 2026-08-22 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| f6fdcbdd-2b0c-388a-84e5-e913a4f4a8c8 | -2.5042 | -48.1366 | 2026-08-22 00:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 99b695ac-e146-39bc-ba9c-eac304e90437 | -6.3862 | -54.9651 | 2026-08-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 1a5f8492-acd2-3c56-b1f5-48a80a43225a | -8.9041 | -60.5577 | 2026-08-22 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f470b1e7-b5e0-3397-88f9-93aa1dd555d9 | -8.522 | -54.8209 | 2026-08-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 266.9 |
| 99a25c39-d593-3ca9-b388-a8d38842828d | -10.2773 | -50.3673 | 2026-08-22 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 5c9eab8e-4e20-3043-ba7b-e13be8d0f886 | -6.5487 | -58.522 | 2026-08-22 00:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d20321f8-3bf2-3a36-80b7-806d9bdcd8bd | -7.3625 | -55.673 | 2026-08-22 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f0def9bf-8987-34e7-acb5-d0c9adb68bbc | -6.8778 | -59.031 | 2026-08-22 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 617b9f31-ce85-3d40-9704-c350eb619b3b | -10.2395 | -50.3711 | 2026-08-22 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a84d0042-9c3b-377f-992d-650ea2eba72a | -8.5406 | -54.8197 | 2026-08-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 317.8 |
| 6a7b41d7-8c3f-36cf-b665-59cc0c7f8f23 | -6.9315 | -59.3184 | 2026-08-22 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| efa3438a-791c-3654-b5fc-5f7a5db0ccdf | -8.8856 | -60.5394 | 2026-08-22 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 1dde4532-5045-31f6-837b-7fb023813d74 | -11.4494 | -44.5353 | 2026-08-22 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c139b458-07a2-346d-a39d-ce7c9d2c85b2 | -17.9613 | -42.728 | 2026-08-22 00:10:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.9 |
| f263248a-4b1d-31c4-bbbd-7dcb166b3daa | -6.2528 | -62.5236 | 2026-08-22 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| e871498f-b917-302a-ac92-90905d3400ea | -21.6056 | -43.9964 | 2026-08-22 00:10:00 | GOES-19 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| 9d26b423-6284-327f-9d71-ff1083faf384 | -4.8966 | -45.2538 | 2026-08-22 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 913813d9-140a-33cb-985b-f0db38e2ce25 | -11.449 | -44.5587 | 2026-08-22 00:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 005f3836-2526-3132-b1fe-20de694b2a3c | -8.5218 | -54.8411 | 2026-08-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 222.6 |
| a54aba65-8f66-382c-bc3b-a7e2960bd190 | -6.3863 | -54.9451 | 2026-08-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 65bd7b32-928a-33f4-989f-df17438900a4 | -10.2398 | -50.3497 | 2026-08-22 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 4ed5ebe7-7cd4-3c9e-9ef4-4c82c81a7511 | -6.2712 | -62.5231 | 2026-08-22 00:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 38460e20-98a3-3e92-ba14-94ae1e9216aa | -6.8188 | -59.6696 | 2026-08-22 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.2 |
| 586c28b9-a376-3b67-a47b-ebadf69cffa8 | -16.4965 | -47.9572 | 2026-08-22 00:10:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a785eabf-d2e5-3d0f-ab95-e1ef7fd8e230 | -8.9042 | -60.5385 | 2026-08-22 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 3afe9826-6155-3c8f-97c3-c0c51ba55f35 | -7.344 | -55.6741 | 2026-08-22 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 16704806-2ef2-3a4f-bc6d-3e9ef5e53b89 | -6.3678 | -54.946 | 2026-08-22 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a429acfe-a700-3276-89ea-cbb06d2fe479 | -8.9934 | -50.7427 | 2026-08-22 00:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 33a2f278-df5f-35ae-b52f-80632eb5beb1 | -6.8593 | -59.0318 | 2026-08-22 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 1d407158-6d25-3e43-a254-e7f2a8cca7aa | -16.4971 | -47.9344 | 2026-08-22 00:10:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| a8ecf1e7-6315-3cb7-94e0-0a918f2cdcd8 | -10.2584 | -50.3692 | 2026-08-22 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| c9b519a9-b46e-382e-a3f4-4b16708c7406 | -13.997 | -53.6853 | 2026-08-22 00:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.3 |
| bcff5ed0-fdd2-339b-a72c-813d4c38e65d | -5.7985 | -57.5402 | 2026-08-22 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 00aff815-d916-3cd7-b425-1c117763fe0f | -7.3624 | -55.693 | 2026-08-22 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| dc848363-1707-31ff-88e9-c80d4a8a4bac | -10.2587 | -50.3478 | 2026-08-22 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 165.9 |
| 8c75fbff-e2bc-35e6-afd4-550de9e51f6a | -6.78 | -59.39 | 2026-08-22 00:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d54ddaab-ef57-32f9-a2c4-4c0ad7a990f3 | -6.77 | -58.7 | 2026-08-22 00:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| be901dcb-f152-31b6-a8b7-2e6baffd2ba1 | -6.77 | -58.63 | 2026-08-22 00:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 63976e29-bbe6-3a89-99ed-b7149252b6ed | -6.78 | -59.47 | 2026-08-22 00:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cb82167b-c12a-3536-a817-6c04a1bf51e8 | -6.81 | -59.48 | 2026-08-22 00:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa0001d-47f3-33a9-9ac8-b549a981d64c | -6.74 | -58.69 | 2026-08-22 00:15:00 | MSG-03 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4104f757-ca30-3686-826d-71757c5b14ca | -6.81 | -59.4 | 2026-08-22 00:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f745841-b997-3d6d-8b2f-2b4abd524056 | -8.52 | -54.84 | 2026-08-22 00:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a66d7fe-54db-36c2-a069-b3dd9a1d2264 | -10.67 | -50.27 | 2026-08-22 00:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6c55a02c-892b-356b-b1c1-8a349bc382f0 | -2.5042 | -48.1366 | 2026-08-22 00:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f91e7a94-0cee-3539-8ab0-5593d59573a7 | -6.3862 | -54.9651 | 2026-08-22 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 396c42eb-0168-3f6b-99fc-f6c094e49fa1 | -6.9315 | -59.3184 | 2026-08-22 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 1f1efc6f-b808-369c-aa2a-39c2cb72f089 | -8.9042 | -60.5385 | 2026-08-22 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| d7f74568-5a70-33b6-bf80-082243701d8b | -16.4971 | -47.9344 | 2026-08-22 00:20:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 2257bb0b-a13b-3510-b245-f6f551922e81 | -7.3624 | -55.693 | 2026-08-22 00:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |


[Clique aqui para ver as próximas entradas](README2.md)
