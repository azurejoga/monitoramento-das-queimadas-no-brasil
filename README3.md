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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99545868-a2f5-30d4-af0e-0130f6843437 | -1.6463 | -45.868698 | 2024-12-27 00:41:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d082ca21-6277-3e67-baf2-80a4b4353649 | -4.3972 | -47.762001 | 2024-12-27 00:41:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7a61127-3dcf-33fb-b2d4-f22bc84de661 | 1.6195 | -60.319901 | 2024-12-27 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5e022a4c-c81f-368d-a4bc-721c46175e78 | -5.9041 | -43.4618 | 2024-12-27 00:41:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 561da35d-7df7-3f09-aae5-397461833d6a | -1.4542 | -53.6675 | 2024-12-27 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f472b6bf-a32f-3c68-99a7-c8b4affcc8e7 | -3.9467 | -46.9804 | 2024-12-27 00:41:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bd1b847b-056f-391d-86df-86d47397b664 | -1.5705 | -53.498501 | 2024-12-27 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6aac0ed-5f2e-32f3-a375-24cdb76d1791 | -4.4368 | -46.574402 | 2024-12-27 00:41:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4fb0502-248e-305f-b0d8-93c9dd4efbd7 | 2.9238 | -60.279099 | 2024-12-27 00:41:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e3e29708-9396-3312-aca2-c9325a870fd9 | -4.464 | -44.321201 | 2024-12-27 00:41:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 39ba72ce-8d42-3681-a491-d4c4acb8d6bc | -4.1896 | -47.974098 | 2024-12-27 00:41:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9434d0ab-5cd1-3828-a179-fa64a23cb9f8 | -5.1234 | -43.242001 | 2024-12-27 00:41:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 06436afc-4f07-3965-a9b6-897a50abd0ec | 2.9264 | -60.268002 | 2024-12-27 00:41:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| baec0328-c72c-3dfd-ac30-b217e6dfffb8 | -5.9143 | -43.503502 | 2024-12-27 00:41:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8196fae8-7af9-361b-9913-88609b60b3cf | -4.4239 | -46.563202 | 2024-12-27 00:41:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 42e41ce6-455b-36d1-931f-b7611be3e8a9 | -4.4336 | -46.560902 | 2024-12-27 00:41:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 522d53ea-e87d-3085-b2e5-2561ecb29a2b | -4.4686 | -44.340401 | 2024-12-27 00:41:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9303895-0a19-3e15-862c-51a1b3f0b685 | -4.4304 | -46.547401 | 2024-12-27 00:41:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a1983358-6ff3-33af-bf09-6a151ad2be76 | -1.4813 | -46.571098 | 2024-12-27 00:41:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 532d2ce8-2944-3088-ae71-71eea327dec8 | -5.6402 | -43.722801 | 2024-12-27 00:41:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4839c57-a944-3322-83ea-c9ea5cae8461 | -3.4118 | -44.888199 | 2024-12-27 00:41:00 | METOP-B | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9bd388cc-99c2-3648-bed3-9b53503e7336 | -5.6449 | -43.7001 | 2024-12-27 00:41:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1577d89-738f-3a03-b147-ed4d0b65d7e0 | -1.1794 | -53.728401 | 2024-12-27 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 427127de-9894-3f0d-b3bd-43130360fedf | -1.7575 | -52.593102 | 2024-12-27 00:41:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e577d97-e685-35e9-b17f-096b2957aedc | -1.569 | -53.4916 | 2024-12-27 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eeff4c4-8929-31ab-a978-b4417fa64266 | -2.6565 | -54.660702 | 2024-12-27 00:41:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9881c580-f3ea-3d05-b6eb-b9db0aa4e368 | -5.6499 | -43.720402 | 2024-12-27 00:41:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7d2a8e7-5b9c-3713-8b4d-5a75fb57a946 | -4.4828 | -44.357101 | 2024-12-27 00:41:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 71e79632-73b3-3cc4-ba50-8ec2436e999d | -3.5891 | -51.040699 | 2024-12-27 00:41:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37e7aa60-90ae-37c0-b1b2-edd95090b224 | -2.2752 | -45.581699 | 2024-12-27 00:41:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5fce3b80-c045-38a6-8931-7486d82dfa28 | -1.5592 | -53.493801 | 2024-12-27 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60a0b9e1-15e6-331d-8878-236d1fa5f649 | -2.2809 | -45.562302 | 2024-12-27 00:41:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 412cc8b7-e91f-3e84-a07b-543b8263e6ce | -5.6546 | -43.6978 | 2024-12-27 00:41:00 | METOP-B | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af62e0bf-89b7-3cb5-bd69-9ca27bcb4718 | -4.3998 | -47.773201 | 2024-12-27 00:41:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c0bf721-2b16-37dd-abf5-1fe2ac8e3fe6 | -4.4782 | -44.338001 | 2024-12-27 00:41:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f2bafe57-8f40-313b-bc38-154e25ef3961 | -4.4207 | -46.549702 | 2024-12-27 00:41:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a76c6b83-f30f-34c9-bbf6-11db426f0fc8 | -1.5052 | -52.388901 | 2024-12-27 00:41:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61f88af0-be1b-3289-8031-e7f38f8d1b65 | -4.2613 | -47.576698 | 2024-12-27 00:41:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1840c34c-e4eb-32e7-a45c-82cdc22a5760 | 1.6221 | -60.3083 | 2024-12-27 00:41:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 92eec87d-d2dd-3163-a5cc-0eb9e930404e | -4.4833 | -44.316502 | 2024-12-27 00:41:00 | METOP-B | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70b8ee09-cc0b-313a-ba2d-287516ecb4e4 | -4.0325 | -46.167099 | 2024-12-27 00:41:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4a703900-3dc8-36ac-beca-fc072399779c | -1.4557 | -53.6744 | 2024-12-27 00:41:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eecdfc04-3045-369e-8943-29c3f032a326 | -4.42 | -46.55 | 2024-12-27 01:00:00 | MSG-03 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3763389b-9924-3625-a020-5e2788cc5e52 | -4.45 | -46.55 | 2024-12-27 01:00:00 | MSG-03 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| feb92237-507c-30f7-ae58-2a038ca56183 | -4.42 | -46.6 | 2024-12-27 01:00:00 | MSG-03 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef23b7bf-7d30-319c-acd8-314e939f5e4c | -15.23687 | -59.92125 | 2024-12-27 01:24:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 907927c4-8449-3a3d-9cd3-b9febd0f5450 | -2.15458 | -53.7289 | 2024-12-27 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fb13ac7b-cea2-3046-9ead-4be4b7652868 | -2.15649 | -53.74216 | 2024-12-27 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7164a168-a2d3-3ec4-9cae-48dbce2cc478 | -2.64802 | -54.67012 | 2024-12-27 01:26:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 1a18c142-0f0c-393a-aa32-5b50937eec96 | -1.55886 | -53.50254 | 2024-12-27 01:26:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 87eae75c-d2dd-3eae-bea8-41e3cb41f7f0 | -3.13735 | -54.66065 | 2024-12-27 01:26:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9b3aab47-41d0-3987-9906-fe84f7c952ca | -1.71347 | -52.4188 | 2024-12-27 01:26:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| db1ac518-ca84-36b3-a001-651bbf4205ba | 3.30915 | -60.0746 | 2024-12-27 01:28:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b8027774-21c4-38cb-af74-e68ffe3a067c | 2.93596 | -60.30494 | 2024-12-27 01:28:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| dec04c18-c62e-37f2-8a29-8cecf39ce21e | 1.63224 | -60.33961 | 2024-12-27 01:28:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.6 |
| db7b9152-0561-3c4a-a67d-088d2fed0b3f | 1.62309 | -60.33835 | 2024-12-27 01:28:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a9598d6d-9fd2-3e4a-b58c-f5fbede448f1 | 3.67648 | -60.67419 | 2024-12-27 01:28:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 48b795fb-cab2-3d2a-a5c9-88d57d47a212 | 2.92692 | -60.30367 | 2024-12-27 01:28:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 3bf9c54c-81c3-377b-b281-8e90c3237fea | 2.93724 | -60.29571 | 2024-12-27 01:28:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 0d0f6ff7-c677-3e01-bc8e-0d1c1155238c | 3.02785 | -60.1089 | 2024-12-27 01:28:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6e3d50b6-34ec-3941-bdd4-26c44883ebe9 | 2.9282 | -60.29443 | 2024-12-27 01:28:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 87c6e17d-5852-3e69-9bf3-7550bbc99d14 | 4.38357 | -60.49561 | 2024-12-27 01:28:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2ce41819-ab48-3da7-bc1e-6df2cee2d9d4 | -28.048599 | -55.197899 | 2024-12-27 01:37:00 | METOP-C | PIRAPÓ | RIO GRANDE DO SUL | Brasil | 4314555 | 43 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9618972a-870d-330c-8a30-6e0855cdcfbc | 2.9243 | -60.2915 | 2024-12-27 01:39:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e8ba4aba-cc1c-3be0-9977-c808dac7854b | -15.2393 | -59.917801 | 2024-12-27 01:39:00 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21e49cd9-0551-3cfb-9010-b1e2e844039a | 1.6211 | -60.3326 | 2024-12-27 01:39:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 54c4a92b-994c-34ea-bb96-b517602da0e2 | 2.9219 | -60.3022 | 2024-12-27 01:39:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 89a40812-48a4-3457-bab2-0bd0dddbe9f1 | 4.3687 | -60.483299 | 2024-12-27 01:39:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8b85ba7d-f663-37af-83c2-744827666943 | 1.6188 | -60.3428 | 2024-12-27 01:39:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6316801f-714e-374b-acbc-814315a5c1ef | -9.04335 | -36.00399 | 2024-12-27 02:53:00 | NOAA-21 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e8df9908-855f-381a-84e0-ef4f3db305af | -9.60761 | -35.90571 | 2024-12-27 02:53:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8f483c39-cbb5-33f5-b239-06ac9e821a28 | -9.04447 | -36.00945 | 2024-12-27 02:53:00 | NOAA-21 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1df99722-7d82-3085-9e8b-0941cc30a61b | -9.60675 | -35.90721 | 2024-12-27 02:53:00 | NOAA-21 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 3659d03c-e3c8-3e8f-9c1c-9de0402df51d | -9.0378 | -36.00855 | 2024-12-27 02:53:00 | NOAA-21 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6ab6ba23-411b-3540-9241-12522835b887 | -9.0421 | -36.0103 | 2024-12-27 02:53:00 | NOAA-21 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b73a5ded-6b35-33c8-beab-2d084fff6b1b | -9.04567 | -36.00315 | 2024-12-27 02:53:00 | NOAA-21 | UNIÃO DOS PALMARES | ALAGOAS | Brasil | 2709301 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 2539272f-b679-3ebf-8862-b8fabd47569a | -4.52875 | -42.06668 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b875f165-3283-3c9d-897d-2ca1bf63cd19 | -10.00786 | -38.40958 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f28fd201-e945-338a-9535-39a6931bab40 | -4.52049 | -42.07217 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bc887670-8787-38e8-8a6b-aa0a9a2fe94d | -10.00896 | -38.40374 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 819c2960-046e-3cee-b003-f84f59f165c5 | -10.01354 | -38.40757 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2367de73-cc8f-3d8e-8763-0fb3b635282b | -4.51533 | -42.07473 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| abb8e248-f966-372f-812a-e1f8e765619e | -4.52295 | -42.05874 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fdc5d60b-7936-37f0-9880-7a3ce896705b | -4.70234 | -38.16755 | 2024-12-27 03:17:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4db607ad-2a38-3268-ab74-9834c0758f8e | -4.52235 | -42.07605 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 49e2a843-a1d8-354e-a285-0fcf93b090af | -4.52353 | -42.06931 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 166b5231-e6c9-3203-9eee-3e7eab3f4709 | -10.00841 | -38.40667 | 2024-12-27 03:17:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 57aed0c2-1dfa-3dad-9130-0d5681ff01a3 | -5.39294 | -40.67422 | 2024-12-27 03:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a4492dbc-7936-3978-b0af-3983891f1ae5 | -3.06104 | -40.08429 | 2024-12-27 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3f9a3bca-a38d-391a-80c4-37fdcdb493bd | -5.35843 | -39.34324 | 2024-12-27 03:17:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 61771846-c19c-381c-b5c2-19a19c88b74a | -12.18817 | -41.35267 | 2024-12-27 03:17:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c71d6ed8-3877-3991-9ebd-94c34c8d9c49 | -9.81392 | -35.93501 | 2024-12-27 03:17:00 | NPP-375D | BARRA DE SÃO MIGUEL | ALAGOAS | Brasil | 2700607 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 40fccafa-4cd7-304c-b9cd-f94d8cd96987 | -10.52787 | -36.95345 | 2024-12-27 03:17:00 | NPP-375D | JAPARATUBA | SERGIPE | Brasil | 2803302 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 38891508-c328-39fc-b397-1ab62a065bd5 | -9.61183 | -35.90598 | 2024-12-27 03:17:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 23b63450-4404-30b7-967d-783cc4f0ae11 | -3.0348 | -40.12291 | 2024-12-27 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 92f41374-08a6-329e-a600-41d0cb892876 | -3.0685 | -40.0836 | 2024-12-27 03:17:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 13c444aa-8d3b-3b3f-a771-496c5cc97f1e | -4.51414 | -42.08144 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| afb2409a-de05-3365-8a2e-460210a8e589 | -11.24139 | -41.88964 | 2024-12-27 03:17:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 04e45a8d-30b1-394a-8908-ad4c9193ae6e | -4.52118 | -42.08269 | 2024-12-27 03:17:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 604246b9-118f-3c5f-af8d-2ff5c459c282 | -10.47323 | -37.01758 | 2024-12-27 03:17:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README4.md)
