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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c37cedd-4c6c-3f68-b408-30e6024bc6cc | -6.39538 | -44.25508 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69b0604c-2495-369d-89cf-66b131057cdc | -7.63562 | -45.27505 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a9ff559-202d-39ed-9caf-25db6f8009d3 | -4.48232 | -43.90142 | 2025-08-20 04:08:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ed4bf44-9fbe-3d93-94db-ed8accf632a2 | -5.25334 | -44.45457 | 2025-08-20 04:08:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 41cb8585-8582-38c1-82bd-6790fd8c1053 | -7.44928 | -50.27456 | 2025-08-20 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f69d7fe-7d77-3ff4-a10f-e1a7f24b5a08 | -6.09104 | -44.40742 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33adbab2-c2b0-3450-8988-4efa9af99884 | -6.05294 | -44.14659 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ccfca01-59a2-358e-8b25-3af21852219f | -5.63507 | -43.37389 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0419788-635d-3240-b663-4fbf98e9dc88 | -5.98516 | -44.14373 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c8682cf9-6377-3f62-ba10-a1e746257923 | -6.49271 | -42.97832 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4cfa5f02-2370-34d4-9acc-6efeaa598fb5 | -3.99037 | -42.52118 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bb0b30bf-3aa6-397c-898b-7b177245acdf | -2.77074 | -48.59435 | 2025-08-20 04:08:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df28d4c1-d97a-3b69-81dd-929d98d3778e | -6.62964 | -43.8974 | 2025-08-20 04:08:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8673dc1-2392-3b93-9aab-e6cccdd8c463 | -7.64653 | -45.27672 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 517dac86-7fe0-330e-a153-88352bca687b | -4.91522 | -42.09278 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 86797f0b-70cc-3637-b3bb-9585a6dfa525 | -6.86427 | -43.59427 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4391003f-6b75-335f-8895-21a39eb2e5fc | -7.65449 | -45.27363 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3f7ec895-111f-3d18-9920-83b283794108 | -8.16975 | -47.35559 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3164b71c-9b96-3b9d-b987-a456053c9639 | -5.65691 | -43.50243 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee8775ae-af60-3255-98d0-6c0704457a9b | -4.02107 | -48.06306 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b18197d5-3c57-3cf2-8069-4fd7babcfc46 | -6.63563 | -48.68422 | 2025-08-20 04:08:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d136d5d-adaf-3d7c-87fe-a66ba060731e | -8.79118 | -45.47923 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cffe6101-2e2f-3ae2-bf05-d94b27ccb7e5 | -9.67111 | -40.58752 | 2025-08-20 04:08:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 4ae5255f-bf43-3df2-aa54-7e2743ea1f6d | -6.48993 | -42.97422 | 2025-08-20 04:08:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd7c283a-7f56-3676-bdcc-10baf7f0d7e3 | -9.02917 | -45.10667 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8f42eb4-f6f7-3c9f-98a3-f6b6c927c34c | -8.80674 | -45.43814 | 2025-08-20 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89923ef8-3fa8-3a02-950c-4b806c764c72 | -5.61579 | -43.47352 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c305229a-1f15-3f04-8b71-c911f8ab7330 | -7.39423 | -44.27164 | 2025-08-20 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cef712d6-47bc-3a1c-afaf-c1a47c0408f4 | -6.13919 | -45.1513 | 2025-08-20 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0eafb69-1825-327e-9d0a-c39bc1fb515e | -6.03805 | -44.35394 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ec51b6e1-2ee5-36bf-b909-1af2ec334147 | -6.06844 | -44.11677 | 2025-08-20 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60876829-fee6-3057-adfa-5cc36605d16e | -5.86033 | -43.4393 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7af1249a-b7f9-38f1-bf51-4de8b1e3ea14 | -7.65658 | -45.261 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d22980f-002b-37ff-9b2a-7fd7eed547fd | -8.02771 | -47.673 | 2025-08-20 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 429096fa-5b3c-378e-996e-03ac6d3642b3 | -6.3989 | -44.25555 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cdfc74d-787e-3842-885a-253b696ed18b | -7.63785 | -45.28403 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8d2f5d9-9b3d-3bb8-afb7-2705f0cd7371 | -6.16152 | -42.7106 | 2025-08-20 04:08:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e921771c-f504-35f3-bd67-6339110d67e1 | -2.83453 | -49.14245 | 2025-08-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aac86e21-201f-32f6-92c7-ddf2a9fff01b | -8.80413 | -45.33121 | 2025-08-20 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ed659f8-213d-307b-9fa8-5c5732322e52 | -4.72474 | -38.39724 | 2025-08-20 04:08:00 | NOAA-21 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 2da73f13-9992-3167-8e41-3da74474f264 | -7.12236 | -44.64814 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f67a16c-2388-3911-ab2e-0f236c5cb968 | -3.27112 | -49.14445 | 2025-08-20 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a737a635-5437-3389-b4ed-d9e471d40419 | -3.40033 | -46.90478 | 2025-08-20 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d031375-5928-3e6d-8d30-380fa39d79d9 | -6.92617 | -46.99505 | 2025-08-20 04:08:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5a8576b-eade-3542-8233-9a46ea87423e | -6.51469 | -45.46673 | 2025-08-20 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| da392b77-721d-32ef-952c-bb43d389e13f | -6.2346 | -46.24615 | 2025-08-20 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c7dc6d-3fae-3af4-99b6-ac7ef28c8edb | -6.35317 | -44.10893 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86fd9605-5936-39d1-b556-88889a30fb87 | -10.24884 | -48.33487 | 2025-08-20 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 639af1b7-aa3d-3185-abf2-a482e36cac39 | -5.99329 | -42.84757 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 687e8f48-f933-3486-9ee1-40ee413510d4 | -9.86989 | -45.97512 | 2025-08-20 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d02b3f22-a060-3dcb-8ed0-a214edd8afc7 | -6.85909 | -43.60477 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d30b0dc-b6b8-3918-bc74-d0efd0ef7e57 | -9.14923 | -44.3904 | 2025-08-20 04:08:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 779bcbbc-e8ba-39d6-b7b1-e6286c135305 | -6.45886 | -53.38052 | 2025-08-20 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dab166a9-31fd-3e86-8b49-ae0fed8f4be7 | -6.39671 | -44.24695 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec03d497-5b87-3103-a76d-29217a2f3faa | -6.67739 | -43.68598 | 2025-08-20 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7ef9575-7da6-34e6-8263-ea217e5dc314 | -3.82068 | -41.56853 | 2025-08-20 04:08:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e5063072-c3c5-381a-8614-47c5c47c01f7 | -6.82102 | -39.89534 | 2025-08-20 04:08:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4575f0d0-7215-3509-8f70-fae4845fd213 | -7.96794 | -55.30278 | 2025-08-20 04:08:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdf025ff-3628-3dc5-85b5-7bef9c71f46b | -8.83503 | -52.04321 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8d60f04e-f736-3088-aad2-7baf70143fdd | -5.35874 | -41.21807 | 2025-08-20 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fe82f762-5266-3f5d-8330-0c499ae67b82 | -5.54556 | -45.37421 | 2025-08-20 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b58534a1-e8f9-325a-802b-9402d2b5a392 | -3.23504 | -46.80162 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2dbace26-2374-3be3-a9e8-ce735e92e514 | -10.31155 | -46.68256 | 2025-08-20 04:08:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5d9da432-5aa7-3a6b-8c72-5803e1ba1c24 | -5.48501 | -42.16875 | 2025-08-20 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 387d2c34-2a3f-3847-807a-ccb71d6de614 | -6.8665 | -43.60215 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a042074e-d28a-3623-a2cb-ebc7fc5623d1 | -7.63173 | -45.27147 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d15a4f5-ccee-363e-8852-2852e60a2274 | -6.95864 | -42.87399 | 2025-08-20 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 210ba179-2155-34e6-bd85-5a539f4a91a8 | -7.07171 | -46.87628 | 2025-08-20 04:08:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7998e8e7-3a0a-3bf4-b287-bed897d5bfda | -8.82046 | -52.03059 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43d6a7bf-ff33-3147-8934-bd4a73afaeb1 | -4.42615 | -47.75528 | 2025-08-20 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fc69afc-4c1d-39ae-b32c-28042cdddbdf | -6.56033 | -43.49643 | 2025-08-20 04:08:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f8ce2c9-4140-32ca-9ca2-450738d6f50a | -5.42454 | -43.1749 | 2025-08-20 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c475b7b0-5ab3-3b4a-91ac-091cbf710cde | -3.35953 | -43.36065 | 2025-08-20 04:08:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1006fcf-26c6-398b-a840-1cfaf96be6d8 | -5.79119 | -43.88747 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cbaefdf8-dac8-3bd3-87b4-46b2f7c93b34 | -5.78435 | -43.89494 | 2025-08-20 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cc6d0d1-444a-3ded-8c84-4e9e2f164be7 | -7.58498 | -45.42177 | 2025-08-20 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b79dfd5-7f19-325a-a8dd-b946b54f6b61 | -7.79093 | -45.15255 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a346fe45-5ea4-3c59-97d5-f1000da12a06 | -5.97672 | -43.60999 | 2025-08-20 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b0d56875-efa0-32fd-83fa-830fa8f88f26 | -5.48556 | -42.16527 | 2025-08-20 04:08:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1654a9e3-c611-3706-9560-b06bb1461bcd | -7.21518 | -46.25838 | 2025-08-20 04:08:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 27482b48-21de-328c-87c2-fdf31275cbf4 | -6.40609 | -42.49733 | 2025-08-20 04:08:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 000d91e0-c396-320e-b237-cc4a577fb2a7 | -6.86591 | -43.60583 | 2025-08-20 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a61cfdaa-c63b-38e8-a235-071afde25ac4 | -3.99093 | -42.51761 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bba32252-1f09-3a91-ad8d-88d2362c0b66 | -5.98886 | -42.83221 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| be6ef8f0-4f77-32eb-940c-81d1409e285e | -2.90441 | -48.29341 | 2025-08-20 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 67b12b96-b53d-3366-b351-19dbd3e9085f | -9.92436 | -49.28617 | 2025-08-20 04:08:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e0332829-0d21-399f-8f42-a1051a66e707 | -7.65086 | -45.27307 | 2025-08-20 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4e4d7d0-2724-35fc-8c62-5660239962c0 | -7.58936 | -44.38892 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e68967fb-921b-37ff-a231-63f4a6395ffd | -7.14565 | -44.59417 | 2025-08-20 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0add9f3f-1397-3650-b122-de7435614227 | -3.65219 | -48.32445 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3f6a657-a58a-3205-9b03-48f21c707547 | -7.58461 | -44.39612 | 2025-08-20 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3d92990c-e39a-3e43-a0aa-03a1a551d7a4 | -3.65477 | -48.45288 | 2025-08-20 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db255bc2-5c72-3311-bf33-41530a26ad26 | -7.22923 | -44.70544 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36039f31-7d89-3da3-97f8-4d3755e96227 | -4.9095 | -43.23417 | 2025-08-20 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed7b0547-8ee7-3f51-b59b-0219311d77ce | -4.90671 | -45.67703 | 2025-08-20 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e53ebd6-371f-3add-871d-d1608b451e08 | -3.98198 | -42.5089 | 2025-08-20 04:08:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 6ceaba7a-33f0-3e73-9b44-ddf551a5bc23 | -8.82969 | -52.04242 | 2025-08-20 04:08:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20232b90-00b3-37da-ab2f-3e1045ada2a3 | -5.99942 | -42.85221 | 2025-08-20 04:08:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fddf85e0-95d6-30f6-8b3a-a896145b83cb | -5.64755 | -43.38337 | 2025-08-20 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f38bdcfe-fb1f-3393-9155-e45e931459db | -7.19881 | -43.95945 | 2025-08-20 04:08:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README16.md)
