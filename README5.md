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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3a5dbe2-66da-37eb-8581-382066c8f11f | -3.1833 | -49.4429 | 2025-07-24 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 7b65d21b-c861-32a8-aeb6-371e7a91bb56 | -7.2594 | -43.0881 | 2025-07-24 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| 4833cce6-89b4-3d51-90d2-a0f1e1677482 | -3.1648 | -49.4648 | 2025-07-24 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 7d41164a-5045-3be1-911e-020c44fbb0d8 | -3.1832 | -49.4642 | 2025-07-24 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.8 |
| 5c8dab32-f83b-33c8-a790-42a568ed3b91 | -15.5749 | -49.8323 | 2025-07-24 03:00:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 20faca7c-87b8-3014-a709-b08390b1c132 | -7.2597 | -43.0645 | 2025-07-24 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 193.5 |
| 857e1360-954e-32db-9a87-ff4f8739bbf7 | -7.2408 | -43.0664 | 2025-07-24 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 3ae57f01-296e-35a2-91a3-9aba11c66bee | -4.0569 | -42.5118 | 2025-07-24 03:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 61.5 |
| b0f032c5-a54f-3627-a4ba-2579210f5497 | -18.83094 | -41.98769 | 2025-07-24 03:04:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4d95d795-cda3-3f95-9566-1a9544f76f4d | -7.2597 | -43.0645 | 2025-07-24 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 171.2 |
| 86d06f5f-9889-3d98-a4c3-aade172fc75e | -3.1648 | -49.4648 | 2025-07-24 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| fb695745-027e-38b2-84ff-dabc43e5b2d8 | -3.1649 | -49.4435 | 2025-07-24 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 58cc537d-ebe5-3e6e-aa9c-b74699c20058 | -4.0569 | -42.5118 | 2025-07-24 03:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| b26f26ad-19f0-3606-b691-2d6b12cb3d89 | -3.1832 | -49.4642 | 2025-07-24 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 117.9 |
| ebe0900f-2eb8-3c7f-a7a6-d69a759454d4 | -7.2594 | -43.0881 | 2025-07-24 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| b8b718ee-fc28-3408-9730-844a1efc400f | -7.2408 | -43.0664 | 2025-07-24 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 1f89fd36-0eab-3df5-ae16-782a6aaf05c3 | -3.1833 | -49.4429 | 2025-07-24 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 115.9 |
| 5b8dcf31-07c7-389e-9ab3-f45057248e79 | -3.1649 | -49.4435 | 2025-07-24 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 0d987506-3a5f-36bb-8267-d6acdd5f0b87 | -4.0569 | -42.5118 | 2025-07-24 03:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| a8b5e265-fb8f-3a38-b9ef-963ea588cf32 | -3.1648 | -49.4648 | 2025-07-24 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 0f3d61dc-87fd-339f-b836-8a8294791717 | -3.1833 | -49.4429 | 2025-07-24 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| c62166ed-6f24-3a53-ab73-04fe63ffb3c2 | -7.2594 | -43.0881 | 2025-07-24 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| ee785602-e046-3998-9a66-d7e9bd669ba6 | -7.2597 | -43.0645 | 2025-07-24 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 188.9 |
| bf3f5a18-98f9-3879-8818-140cd1122d7c | -7.2408 | -43.0664 | 2025-07-24 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 64fe061e-9937-3070-a087-46bb068ba283 | -3.1832 | -49.4642 | 2025-07-24 03:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| c430ba91-b2e1-36cd-aef0-90bd37fab12c | -4.17005 | -42.02756 | 2025-07-24 03:21:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 044a26ee-1e34-3ddc-a983-ab15f5d7d8a7 | -3.93801 | -41.49829 | 2025-07-24 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7dd24387-bba8-3e1d-bd90-d762419fd812 | -3.94484 | -41.48603 | 2025-07-24 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 981bc1db-da3c-33b5-ab30-3727ceb547cb | -3.79539 | -41.00214 | 2025-07-24 03:21:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b19ebf3f-6607-3496-ae43-96e53a871f54 | -3.93691 | -41.49469 | 2025-07-24 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 484f3505-2e74-3fd9-9079-021aafbc4bcd | -4.58454 | -43.31856 | 2025-07-24 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e767df16-73ef-3377-85fe-52bc1b2a8280 | -7.25419 | -43.08819 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 08393918-6f2d-37c7-9949-f342efde3f86 | -7.25523 | -43.08262 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 54100c4a-14b1-32e0-bb67-baed4d1f3345 | -7.40374 | -37.5177 | 2025-07-24 03:21:00 | NOAA-20 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 88e03940-357f-3cf5-9d50-1558baa462ee | -4.05629 | -42.52232 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| af6b88c5-8736-38cf-8678-6363fb295033 | -4.80158 | -43.21555 | 2025-07-24 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 61295a99-f2a8-34a9-bae9-c562e9700907 | -7.25625 | -43.07714 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 75af3099-ff89-37a5-a4cf-91c9ec28dbd5 | -7.24873 | -43.08147 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 930e185f-4cc4-37fe-9621-73b0c2e36482 | -4.04311 | -42.51999 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 710191d2-836f-38fc-9913-8b0bbcefb59c | -5.48436 | -42.15357 | 2025-07-24 03:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75117df9-deb7-3cf0-bb1b-c53201d5f0fd | -6.81273 | -44.0007 | 2025-07-24 03:21:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4907729d-cff4-3817-a4d0-b2cd7db2fda9 | -5.47808 | -42.15229 | 2025-07-24 03:21:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60952fdb-3489-3df6-9969-e246bc345b03 | -4.17645 | -42.02859 | 2025-07-24 03:21:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 848cf694-5843-3754-868e-16259cad5114 | -7.24328 | -43.07477 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| a68694b4-5b34-3939-a4fb-79a5fb558887 | -7.26272 | -43.07838 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 407e8595-145d-3905-8405-aac4e842d2d6 | -6.13418 | -42.96213 | 2025-07-24 03:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3cbc2903-1130-35e2-b472-19a8d228f5dd | -4.05826 | -42.51095 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 978253ff-c3fe-3390-b47c-d636dc195d88 | -4.58343 | -43.32493 | 2025-07-24 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd20684d-3778-3aab-bca7-b2e47a90c20a | -4.04411 | -42.51422 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 61d0794a-b350-3a8c-9f40-e6676df5a873 | -3.79461 | -41.00676 | 2025-07-24 03:21:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 28542ae8-b914-3315-832a-bc90857d0ad4 | -7.2443 | -43.06934 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 21734de9-4aa2-3383-9678-4165f8feb5c7 | -7.24119 | -43.08591 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 8d8ad259-19e5-3801-96d2-7991d4c05dbc | -3.93264 | -41.49227 | 2025-07-24 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a76c8fc2-e326-303b-aa03-ebc4dd82ce9b | -7.24224 | -43.08031 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 57a45451-4b95-3c65-83d9-ff7ac4b1ef1f | -4.0421 | -42.52579 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 393eb6cb-eaec-3bef-9d63-28a5ec90ee79 | -7.25724 | -43.07182 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| d6461e03-bbc6-3624-82f7-d059a3858857 | -7.25077 | -43.07056 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| c9e47bd9-3293-3b43-9203-2c2d1b01316a | -7.24769 | -43.08706 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 57ae56e2-cb55-3339-b3db-a71105e54323 | -3.47242 | -42.85887 | 2025-07-24 03:21:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9a89c9d9-0c6d-357a-9f97-140f886dc18a | -4.05528 | -42.52812 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 30d3f56d-fc80-3904-a113-679d0223200a | -6.46261 | -44.58343 | 2025-07-24 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39254d75-3bd0-3673-b6a3-a8b57e3fd12b | -6.139 | -42.96587 | 2025-07-24 03:21:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6bea0198-2bb7-36cc-981e-2662e6534a13 | -6.13249 | -42.96444 | 2025-07-24 03:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 643fc2c2-4a0d-379a-821a-c8d1e5f74ee6 | -4.04869 | -42.52694 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 197d9bf1-c829-3d41-94d3-2deb732e3eb8 | -4.0497 | -42.52112 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 03e50756-2839-3076-a621-9f25ed3354b8 | -4.58428 | -43.32359 | 2025-07-24 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e184bd8-4eae-3d1d-bf26-5d8d9a4b2c99 | -3.93072 | -41.49357 | 2025-07-24 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 66b52141-45ce-3846-9362-96f90926eac2 | -3.93181 | -41.49714 | 2025-07-24 03:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c481c264-7ba6-392e-811b-b3a7d4f133b9 | -4.58545 | -43.31718 | 2025-07-24 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ec42ef6-c9c7-318a-8c8b-53542bf6cc3e | -7.24976 | -43.07597 | 2025-07-24 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 1b958fff-277b-3127-96e2-25d53fd629e8 | -7.40826 | -37.51838 | 2025-07-24 03:21:00 | NOAA-20 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b5293671-cd61-3d9d-8ae7-e0bedfae5d37 | -4.0507 | -42.5154 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6542fdb7-aecf-3c19-841f-8fc58fc64a5a | -6.13313 | -42.96793 | 2025-07-24 03:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7409372d-667c-3738-a70c-6d80ace69be2 | -4.80945 | -43.21064 | 2025-07-24 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4165e048-1db7-3814-a691-3085c083c14f | -4.05727 | -42.51663 | 2025-07-24 03:21:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1d798eca-0d93-3ccb-bfcb-79f709a3cae9 | -9.65573 | -40.59162 | 2025-07-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7bb067e9-0b01-34eb-975d-ffc5732e2d30 | -10.62296 | -45.24477 | 2025-07-24 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5bc72aba-ef07-3aa7-8272-49efe26a8be2 | -9.31868 | -44.85651 | 2025-07-24 03:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d60206b-c9eb-3bf8-974b-45574e3906e8 | -10.62576 | -45.23137 | 2025-07-24 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c0334e61-dada-3410-a163-a4b8df6bf343 | -9.76183 | -41.88202 | 2025-07-24 03:23:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b3058c0d-0851-3ba0-9354-6d29c92387c5 | -12.25208 | -44.7805 | 2025-07-24 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f98772dc-d6dc-3710-9d52-efbcca0e3dcc | -12.4205 | -45.3761 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b294e370-e52c-3802-a8d3-51498d0882f5 | -12.25084 | -44.78642 | 2025-07-24 03:23:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 82ce9cb1-6cc9-3d55-b56c-857630d00fa7 | -10.6273 | -45.22993 | 2025-07-24 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 01e52cad-f1e9-3657-975c-22b9053c1426 | -9.6551 | -40.59504 | 2025-07-24 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 72ea23cf-bd3c-397f-abc4-0e69c6106209 | -12.41832 | -45.38214 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63dd155a-c0b2-386a-b684-33a919526dcf | -9.6997 | -36.73381 | 2025-07-24 03:23:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cc1472fe-f6fb-3148-b0b5-eeee1047fa86 | -10.62438 | -45.23797 | 2025-07-24 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a77e18f2-54e3-3abf-90c0-f706828a2116 | -9.32561 | -44.858 | 2025-07-24 03:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 489ee6d2-e1bc-3a9e-969a-3b915b8ff24b | -9.31734 | -44.85594 | 2025-07-24 03:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 56ae7a2c-1a59-3fa9-a292-023a1236fcbb | -12.4251 | -45.38365 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 28ef40e8-75ab-30ac-b074-2f8cb28c59ec | -12.4264 | -45.37738 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 671f8773-3f7b-3be4-a3e1-e2bd6b791800 | -12.42728 | -45.37757 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af07eb95-5628-33bf-a5e7-1ff95e447ec1 | -10.62461 | -45.24323 | 2025-07-24 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3ab27216-3fb7-30eb-86d2-4efac454fb35 | -12.4238 | -45.38993 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 54e21436-35b8-376c-b362-d34a78987613 | -10.62597 | -45.23648 | 2025-07-24 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3109a73a-7c8b-331f-b396-e2f1155ac854 | -10.61906 | -45.23489 | 2025-07-24 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2b47b61-e157-3265-bf28-31e94b59e6aa | -12.42594 | -45.38384 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1bdc1a47-43a5-3290-a93a-4af52ee700e4 | -9.31869 | -44.8493 | 2025-07-24 03:23:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf8795a0-4e44-30f7-86d1-a914cc8a987a | -12.41916 | -45.38234 | 2025-07-24 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README6.md)
