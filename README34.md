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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4c4b359-e6fb-3141-97fb-84127be97cb6 | -1.7048 | -45.82632 | 2024-11-29 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28eb8d4f-832f-3d2c-b520-ce9e510bcb1f | -1.21344 | -53.75796 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e5ad2721-8268-3418-a275-38f3280381bd | -3.81636 | -46.59349 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 542e89ee-785f-3a59-8d17-403698324bc4 | -3.97905 | -46.74035 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8d91e4-f46a-3ea2-93b0-1b68dd085478 | -2.66449 | -48.79904 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56bac71d-4075-390b-8a92-d3b49f8dd20e | -2.58438 | -51.9231 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96b80cd8-eff7-3488-9749-f89a851a690d | -4.22282 | -45.77327 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a06b449-2bbe-3b79-baf9-eeb0db153090 | -5.02233 | -40.91884 | 2024-11-29 04:04:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| da220359-655d-31b2-b35a-84625dd8d394 | -2.66588 | -48.79041 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c17a7450-8dcb-3647-b835-aab74aca6e1e | 0.03752 | -51.11212 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 24f32939-d8d8-3ff6-9fab-aac3e891ffd8 | -2.54352 | -46.24076 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38cf1e78-c938-37b4-a6a1-4fe8c714171e | -4.79192 | -44.43093 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2870bd85-ea10-309b-b1d7-ba34a8a83517 | -3.14805 | -46.59605 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3388b98-04ea-3c6a-8697-1edfc3170f4a | -3.30578 | -50.28306 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8884ac5-d5d7-34c6-be8b-0e8c07060fa1 | -3.33433 | -53.21473 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6b4a567-c385-319b-b7b0-d639018ada82 | -4.17054 | -44.26556 | 2024-11-29 04:04:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 896b4128-5359-3399-a3ec-f29850ec857f | -2.69854 | -48.65128 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d1785c2-806c-3ab0-926b-a47909b50dc4 | -3.43958 | -40.83245 | 2024-11-29 04:04:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| feee0f77-954a-3e04-801b-b39db9f66dfa | -5.75843 | -43.40111 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6be95d2-0b2b-32ac-9e92-e5eaa9bd1ed8 | -3.18146 | -50.28368 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49b87961-8522-33a1-aedf-63babb50840d | -4.87106 | -41.27615 | 2024-11-29 04:04:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 5aafac4f-796e-37f2-a0d9-548f5a0edb55 | -1.68418 | -45.79604 | 2024-11-29 04:04:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f903670-e3ec-3bb6-9690-3510df164b6f | -4.17361 | -48.62219 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53a14dba-c491-35bb-9f8a-359831b6275a | -5.76309 | -43.39413 | 2024-11-29 04:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98dd1562-a2cf-3d4b-9814-a9066880151b | -2.75448 | -51.66146 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bb8ea17-a223-3069-a297-9b064c073951 | 0.94099 | -50.75069 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a856e45-77fb-3b7f-b03c-20c33d202d49 | -3.99707 | -46.31317 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 189ebde9-34c8-3a33-8ad9-7f4022d0c1e4 | -4.72593 | -46.86222 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8024935-8e94-3b73-8d67-314b8d320d17 | -3.71471 | -47.14791 | 2024-11-29 04:04:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcc99998-5a8c-3ccf-96e7-063ee3ac4985 | -4.66577 | -42.38204 | 2024-11-29 04:04:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfb54011-6fc6-316a-8913-e263a653bfaa | -1.68462 | -52.45355 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23a3451f-4644-3ce9-9ba1-5ac6049d5d71 | -4.17843 | -48.62302 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 543ffa6e-00a3-3224-acf6-45297fbf774f | -5.01623 | -47.5161 | 2024-11-29 04:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f465ce20-cd08-355f-ae87-8f452178a6c0 | -2.69142 | -51.99986 | 2024-11-29 04:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e71ae0f3-88f2-34ef-b2a4-77052e2fbe27 | -3.17023 | -46.30318 | 2024-11-29 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c65fb6d6-2a6f-398c-b882-e27d22a9c21c | -4.66385 | -45.95624 | 2024-11-29 04:04:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b98a91e-7211-3085-b1de-6aad10039d79 | -3.99537 | -47.9156 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1a2815dd-81ba-31e1-ae69-db3482ee033c | -2.29063 | -51.98348 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 185631f1-ec6d-3313-8246-6b97968180dc | -3.196 | -46.57089 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bbe2f21f-80d3-3a0a-812e-0237fddecb35 | -4.04774 | -48.07985 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af568c5f-a26b-31d5-b896-514d37a692da | -1.68215 | -52.5083 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd32035e-6bc6-30e7-b3e1-047acc9a543a | -2.85578 | -46.82925 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d732c4ae-4cad-3a7c-9648-9236a8241253 | -5.56984 | -43.30975 | 2024-11-29 04:04:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e874e6e5-916e-3762-b06f-2f4902bd8707 | -3.61562 | -40.49065 | 2024-11-29 04:04:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2b1abfb4-1908-3d34-bf5d-83af73ea48b4 | -3.30042 | -50.75979 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ac296225-3d71-39b8-aaf0-2c5ebc2e08a1 | -3.16961 | -46.30701 | 2024-11-29 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bb51de46-e931-36b8-893f-29d86da1677f | -3.83092 | -46.53203 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cb2e357-3956-36e1-b4a0-3fe748e6f714 | -2.67453 | -46.15083 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b44259cf-b76e-3506-8ee0-da14498b9c5f | -1.19449 | -53.87491 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5742846-fd36-3565-8967-a690e441a17b | -2.79558 | -48.68683 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3350fc89-a83e-395a-80b6-81a8116582a7 | -3.80464 | -44.05092 | 2024-11-29 04:04:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d440dd7-94da-3bf6-b8a2-eb9e7618080e | -1.98594 | -50.6748 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f58cffc3-6ec5-3cb9-b680-3ead15b20b8f | -3.479 | -46.19237 | 2024-11-29 04:04:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3abca349-be6b-3bf5-a70e-3400e2113e28 | -4.10387 | -50.98691 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 350cfd4a-ad08-35ff-9c61-d9b0c91b7bef | -2.85955 | -45.53753 | 2024-11-29 04:04:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b187a67a-cd38-3c0d-aabf-d67f363a84e8 | -4.43438 | -46.57705 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 15184632-a730-38a8-974a-66fbc73194ea | -5.61292 | -43.96063 | 2024-11-29 04:04:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2133d76-2e7a-3f9f-9cee-3bfd527a20b9 | -2.56704 | -51.8372 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a9778519-b877-33a2-8b1b-600fc0bf63a8 | -3.62708 | -51.43509 | 2024-11-29 04:04:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74be1709-a905-3987-bc22-19db54e0b634 | -1.70041 | -52.64036 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c33da4aa-3919-3d2f-bdd2-b15f31d87fe4 | -1.58757 | -52.27665 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fe221b36-cb4c-38c5-985b-1fe9adb71683 | -1.70696 | -52.63695 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f63c1167-3fe5-3391-bac6-4d7e1602d6af | -6.9183 | -37.83833 | 2024-11-29 04:04:00 | NOAA-20 | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6de7ffbe-75a6-36bb-99e7-f4477c36f2bf | -3.68896 | -42.04642 | 2024-11-29 04:04:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 566ca056-01ed-37a0-ad73-614a12aa84e5 | -4.92168 | -44.53162 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7bfe2f7-418e-3e25-a8aa-d3391dceb3bc | -1.06864 | -53.64431 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4b0d5813-bcbd-310c-a3a5-2b6abecc3b85 | -3.24418 | -53.63702 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 93f64aad-e414-3595-8abc-bd3e56c84f8c | -3.78375 | -46.68995 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e143224-789e-386b-af4a-5ac5392c6180 | -0.05184 | -50.82803 | 2024-11-29 04:04:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4ff394c-508e-3f93-bfb9-02894c4296d3 | -4.69298 | -46.66778 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d993e508-f0c1-3b81-ab2b-117422653574 | -3.5683 | -53.02422 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bad436ac-d416-392b-8376-3ccbc378eb2f | -3.54284 | -50.19188 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95868cf3-3a20-35db-b1f9-f748d8c7de83 | -3.78233 | -46.69275 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ebd7f71-0200-3ef9-a640-c98f0477ef49 | -3.46784 | -50.53551 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d50a17d-e8ca-3386-b661-0865ca4585cd | -2.64589 | -48.78696 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99dbb1ab-7e21-38ad-9459-513ef04dbbd9 | -3.66396 | -42.75096 | 2024-11-29 04:04:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ae1514d-af49-3ed5-843e-e591cf1b1f35 | -3.27281 | -50.61409 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ef28fce-475f-3018-83b6-e09f029e1919 | -3.72692 | -49.87189 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c99e0f72-0ad4-3ed3-be3e-d527438f063e | -1.21239 | -53.76444 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4175ef62-1d9b-31d3-8e2e-5fca737d85ee | -3.96222 | -48.08894 | 2024-11-29 04:04:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 533935f0-179f-34f9-9dba-bb03d65b4b76 | -4.43376 | -46.58085 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 68668465-cc01-3e5f-91a8-94e188e5256e | -3.25945 | -49.89427 | 2024-11-29 04:04:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 701afec7-d617-3168-b5cc-699deb441926 | -3.2474 | -50.59426 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86b27a31-f743-352c-b5a2-55508b61a14c | -2.96777 | -53.30205 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| ad806413-7531-3cd3-b1dd-510f1d156f09 | -3.68092 | -42.95247 | 2024-11-29 04:04:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b43cd0ac-a790-385c-b679-778ef0f38ccc | -2.97441 | -53.30326 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| cda43567-470d-3d5e-b1cc-3e4bbe5cd1d6 | -3.07902 | -50.2553 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7426ca8-6af0-301c-bda0-0a7f877eb5eb | -3.49795 | -53.81422 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b3be796-1775-30c4-b4e7-04db212421ec | -1.68929 | -52.46535 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 809e3f65-0c0c-321d-8f84-0eec696810ef | -1.7144 | -52.63258 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d436795-df93-306a-8e7e-5bbcadd2a160 | -2.40991 | -48.53817 | 2024-11-29 04:04:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b21f2219-3fb4-35e1-bdbf-47cedd37710b | -4.26219 | -42.60678 | 2024-11-29 04:04:00 | NOAA-20 | MIGUEL ALVES | PIAUÍ | Brasil | 2206209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c57e225b-77a7-3a30-a1a5-e2185136b898 | -2.03389 | -53.50249 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2823a798-a502-32ec-8e52-8c57cbe58462 | -5.3993 | -41.54714 | 2024-11-29 04:04:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9fb74b80-4c4e-3220-bada-86f825444db3 | -1.62398 | -52.37463 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcb201e5-8b85-3bb1-bcc8-29b6633daf63 | -2.64206 | -47.12503 | 2024-11-29 04:04:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3d753292-0b7a-351e-98fc-490876f89aee | -3.80826 | -46.61604 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b0317c8-80e0-3aaa-abcb-7157e07ec8af | -4.5223 | -45.73385 | 2024-11-29 04:04:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08bef128-7cac-303d-b98b-b9575c04954e | -5.65313 | -45.20077 | 2024-11-29 04:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c1d6d82-146d-3099-8296-fe5cb2ef2e22 | -3.37422 | -50.18058 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README35.md)
