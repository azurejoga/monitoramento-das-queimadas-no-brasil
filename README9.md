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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 73c6f860-9981-33ba-bf9d-fd2863b98a92 | -2.5238 | -47.8115 | 2025-11-15 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 6c2a4761-16ea-3e56-8e64-27a132d1445b | -11.8299 | -49.2024 | 2025-11-15 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 0f87f263-0088-3037-b660-fae966bf7ac4 | -11.8677 | -49.2195 | 2025-11-15 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f1a86119-0489-373b-a5c6-384a520e5435 | -12.7532 | -43.6487 | 2025-11-15 00:40:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| bc69139b-5dc2-3b8b-b913-ca6955a073d6 | -4.538 | -43.2341 | 2025-11-15 00:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 454.4 |
| f861704f-968c-3733-8288-16da97aad990 | -5.2396 | -44.3677 | 2025-11-15 00:40:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 2c43a8c8-7529-350b-95a1-bae9720ebf13 | -2.5053 | -47.812 | 2025-11-15 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 145.3 |
| b744ee13-d849-3603-a277-01a3b702ed56 | -8.5984 | -46.0549 | 2025-11-15 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| a562990f-8a47-384f-8db1-e54d756022d0 | -2.7374 | -45.2877 | 2025-11-15 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 1c9912e5-940c-3c39-b456-fcbf504482af | -8.5981 | -46.0774 | 2025-11-15 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 199.3 |
| f9e60793-4ff0-39bb-a9a4-0ba8312a2d58 | -13.8927 | -42.8932 | 2025-11-15 00:40:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 53382f14-f300-343f-8d6e-07b643e30f67 | -12.4622 | -43.7447 | 2025-11-15 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5fcd2867-8449-3f51-b23d-826c384d5694 | -5.2397 | -44.3448 | 2025-11-15 00:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 179.3 |
| d83959e7-2983-30b6-b830-9cb1e56d1c2a | -11.8681 | -49.1976 | 2025-11-15 00:40:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7c44d92a-2d07-3b0b-9b24-a94be847c026 | -5.221 | -44.346 | 2025-11-15 00:40:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 29224459-1f61-370c-899a-54e0ab211462 | -2.7374 | -45.3102 | 2025-11-15 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 8d0133fa-73f6-34a6-a544-dcc0968b4a27 | -7.8947 | -48.3963 | 2025-11-15 00:40:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 0afdb322-7a30-3c4a-b3ce-f08bafb47fed | -4.5381 | -43.2107 | 2025-11-15 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 562.8 |
| 397b7234-f9ae-3e67-ac2a-dc5681b44d4f | -8.5792 | -46.0794 | 2025-11-15 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 301.9 |
| ba758646-7394-341f-9d42-40558588ff71 | -8.5795 | -46.0568 | 2025-11-15 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 136.9 |
| 057256b2-91c1-39c1-9077-af42d0daff41 | -11.8677 | -49.2195 | 2025-11-15 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 15f63ef3-5375-3daa-bd7a-b92738e72bfb | -13.8927 | -42.8932 | 2025-11-15 00:50:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 68.8 |
| a32514f9-98ba-37f5-868e-31dbd6db009f | -2.7374 | -45.2877 | 2025-11-15 00:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9a5b6e9b-2ad5-37f0-b1b5-7d9f25ded28c | -11.8295 | -49.2242 | 2025-11-15 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 0a0b5d5b-c401-3830-8f72-571a7233c44f | -5.221 | -44.346 | 2025-11-15 00:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| fee2ee2b-8057-3353-ae5d-b8f59bf7c33a | -7.8759 | -48.3979 | 2025-11-15 00:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 978973bd-870f-324c-98a9-a12305dfd487 | -4.2242 | -45.4942 | 2025-11-15 00:50:00 | GOES-19 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 138d4868-4bb6-34b9-9e9d-f1b838b44c78 | -8.5984 | -46.0549 | 2025-11-15 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 178.5 |
| 5ca416ee-f85c-3477-86f0-048a1bf69546 | -12.6745 | -46.7605 | 2025-11-15 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 75628a60-1d62-3d73-b64d-c469f951b82c | -2.5238 | -47.8115 | 2025-11-15 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 53b94248-1306-34e4-bcee-76c6ebedce2a | -5.2397 | -44.3448 | 2025-11-15 00:50:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 194.5 |
| dfea7572-4f67-3276-a692-42a3b3b6e00b | -12.4622 | -43.7447 | 2025-11-15 00:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 4dc280a8-b9e1-35b2-85d2-7c4c9ef00181 | -4.5568 | -43.2096 | 2025-11-15 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 282.9 |
| 06cef208-0d6f-37fa-807e-5d8484264b73 | -2.7374 | -45.3102 | 2025-11-15 00:50:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6ab5e9ff-c5e0-344f-a097-54b59dbbebd2 | -8.5981 | -46.0774 | 2025-11-15 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 455.2 |
| 75786384-c441-3322-b07f-deb8d67855db | -12.7532 | -43.6487 | 2025-11-15 00:50:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 4d60f020-6058-3ca2-adcd-8bce4a3acad1 | -4.538 | -43.2341 | 2025-11-15 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 322.9 |
| e10840ec-145e-3a48-92d6-839fc455600b | -11.8486 | -49.2218 | 2025-11-15 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 73d0b39c-ed84-3199-8b15-ef3fe0139df6 | -4.5567 | -43.2329 | 2025-11-15 00:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.0 |
| a2a0376b-6b67-3845-9cba-f90908dd8688 | -11.849 | -49.2 | 2025-11-15 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 178.9 |
| 18041262-47c3-3a6b-b736-e01515766a45 | -2.5053 | -47.812 | 2025-11-15 00:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 168.3 |
| e8804622-36f8-3923-85db-23b309056194 | -11.8299 | -49.2024 | 2025-11-15 00:50:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| d9f24f48-c851-3f9f-a443-22f12f22947f | -5.2396 | -44.3677 | 2025-11-15 00:50:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 23dd4b04-066a-33d8-beff-1a5cd55b6a42 | -6.1606 | -48.0507 | 2025-11-15 00:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 5bb096fe-0833-31e4-b383-17f141ae9ecb | -10.7048 | -44.5248 | 2025-11-15 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 2da69af5-aef7-31cd-8f28-e380d96677eb | -2.5238 | -47.8332 | 2025-11-15 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| a8b0f215-9137-37cb-9caf-6a23f1b72ed2 | -4.5567 | -43.2329 | 2025-11-15 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 143.5 |
| b544b5b4-ccb7-3ef2-a9bc-05eec1d84bc3 | -5.2397 | -44.3448 | 2025-11-15 01:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 242.7 |
| 25f1bf8b-f27b-3f8a-b4ea-9b3cbbbe7f00 | -4.5381 | -43.2107 | 2025-11-15 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 406.3 |
| 6173aa87-f91f-32dd-bced-4664a14c42f3 | -12.7532 | -43.6487 | 2025-11-15 01:00:00 | GOES-19 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| b9a562c0-a90c-3964-94fa-f1274750946a | -4.5568 | -43.2096 | 2025-11-15 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 285.2 |
| ab6f5eff-c399-3675-8bb6-a893a68b3676 | -11.8486 | -49.2218 | 2025-11-15 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 246.2 |
| 39c7615e-2474-3b81-be08-64778abc5446 | -5.2396 | -44.3677 | 2025-11-15 01:00:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 4872c514-ea43-3428-9513-7b342fb9dd7f | -6.1606 | -48.0507 | 2025-11-15 01:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9b1d7534-a690-3494-a3cc-4bc90ee3b5c2 | -5.221 | -44.346 | 2025-11-15 01:00:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 4c6ced35-05d9-337b-b6a6-681fc2f2eb81 | -4.5194 | -43.2119 | 2025-11-15 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 75410ac4-8532-3cc2-bd22-6d804adad189 | -13.8927 | -42.8932 | 2025-11-15 01:00:00 | GOES-19 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 72.5 |
| 1d6b1928-ca05-3c27-bd34-1e9e2a278b04 | -8.5984 | -46.0549 | 2025-11-15 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 57de1309-a811-324f-8874-05de3083caf6 | -8.5795 | -46.0568 | 2025-11-15 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 114be269-dbc3-3b28-8893-683995390713 | -11.8295 | -49.2242 | 2025-11-15 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 8fb51449-328d-3f79-9ba3-ed5017fb32d4 | -4.538 | -43.2341 | 2025-11-15 01:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 192.8 |
| 33343e74-407a-32fa-b7ab-afba5c0ba727 | -11.849 | -49.2 | 2025-11-15 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 1fac6214-dc50-350a-8002-d6fc14211ca6 | -8.5792 | -46.0794 | 2025-11-15 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| dcbb3b4a-a266-3fdf-8a0d-bfff4c851579 | -2.5238 | -47.8115 | 2025-11-15 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| b6697ac0-4225-3a0b-bbe3-65c3bc88d812 | -12.6745 | -46.7605 | 2025-11-15 01:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 46.5 |
| b7e40987-3770-3e9f-92b6-d95cbc1336b3 | -2.5053 | -47.812 | 2025-11-15 01:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| 795234f6-d099-3d9c-a1a1-549a41663e36 | -17.2639 | -42.6527 | 2025-11-15 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 5cbe749a-7edc-3cd1-9ca7-39d59025e2ff | -8.5981 | -46.0774 | 2025-11-15 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 219.1 |
| 8bc48e1e-221e-3a6a-a7fa-26371ac8a765 | -10.7052 | -44.5015 | 2025-11-15 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 3dc40993-7f6b-31f2-a8ec-f3137233cc41 | -7.8759 | -48.3979 | 2025-11-15 01:00:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| face4d86-1e78-3e1a-95e0-84ca3707982a | -17.58393 | -46.68607 | 2025-11-15 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 9e28c523-e30f-3022-9820-55ede703506b | -17.58396 | -46.67887 | 2025-11-15 01:09:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 69.9 |
| d2c532e8-61d6-3b52-a81d-efa0acf3ef9a | -11.8486 | -49.2218 | 2025-11-15 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 253.5 |
| a4627f2d-5130-3f20-9acd-9423f31e4d5c | -11.849 | -49.2 | 2025-11-15 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 5bfc98d3-c1c3-3100-93d8-7cd65cfccf5f | -4.5568 | -43.2096 | 2025-11-15 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 174.6 |
| 01776106-be07-3939-a3b7-737fbcc6e70a | -4.538 | -43.2341 | 2025-11-15 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 239.0 |
| 8cd4a57e-2f1d-3951-8b6b-27f725b8602c | -2.5238 | -47.8115 | 2025-11-15 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 187.4 |
| f6cb3457-59e6-3db2-b8ec-8a56faa03dae | -10.7052 | -44.5015 | 2025-11-15 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| bb1b22f7-3a3f-3ceb-aa5a-257e2a5dbf42 | -5.2209 | -44.369 | 2025-11-15 01:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 59e834bc-d8a7-3fdb-8ca0-6b42df2f414e | -5.2397 | -44.3448 | 2025-11-15 01:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 64c35ea0-3677-3c7c-aaae-c4c8d2ab48c5 | -12.6745 | -46.7605 | 2025-11-15 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ca5408d0-fa3e-38f5-8f94-840e1870f041 | -2.5053 | -47.812 | 2025-11-15 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 1e92d4fe-d995-39a3-b475-9e9dbda51353 | -4.5381 | -43.2107 | 2025-11-15 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 416.4 |
| 3ff44b89-8d44-30c9-a686-7d36760a270e | -5.221 | -44.346 | 2025-11-15 01:10:00 | GOES-19 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 6f4c6f68-4b6d-3fdd-90b8-4e3b84c1e8e9 | -5.2396 | -44.3677 | 2025-11-15 01:10:00 | GOES-19 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a46080b7-4dd6-3c14-a8f4-9224ed6787a3 | -4.5567 | -43.2329 | 2025-11-15 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| bd99b859-db2f-3e27-b09d-15a77e29d687 | -7.8947 | -48.3963 | 2025-11-15 01:10:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 20bf83e7-4c84-3bbf-9204-43fe5757adc3 | -11.84926 | -49.20768 | 2025-11-15 01:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 383.9 |
| 383cccdd-e7f2-379b-8fc5-1ca99b5cc53a | -11.83901 | -49.20265 | 2025-11-15 01:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 290.7 |
| a4c93cb3-a4dd-3d2a-b37a-869589665730 | -11.86165 | -49.23468 | 2025-11-15 01:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a780b2c7-6fa5-3c95-94d1-3b1ac5c1b5ca | -11.85535 | -49.24278 | 2025-11-15 01:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 50900c50-0acb-33f4-bd2e-ff886828b039 | -10.35444 | -48.92544 | 2025-11-15 01:11:00 | TERRA_M-M | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| cdaf72cf-2436-3487-a4fb-7e694256280f | -11.83292 | -49.21066 | 2025-11-15 01:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| e8e3e523-9bfb-3acb-b5f6-f9dbcd44ef0c | -6.56958 | -51.1298 | 2025-11-15 01:11:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 3c5e9a25-d4da-3639-872d-1fc9e316a8ef | -12.24018 | -49.38987 | 2025-11-15 01:11:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 79ca78c7-9891-36c0-b901-6a8f359b92fe | -11.8553 | -49.19938 | 2025-11-15 01:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 02e2a5f9-9940-3094-a26b-d98f9558b8a5 | -6.57926 | -51.12143 | 2025-11-15 01:11:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 673b946c-14ee-3f18-b3cf-61e95eca2bca | -11.84536 | -49.23766 | 2025-11-15 01:11:00 | TERRA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 181.5 |
| 7aed9410-ef08-31e9-8277-f5492b64ef74 | -1.83322 | -53.79685 | 2025-11-15 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 732680ed-8db1-325b-92b5-69a5a7e71044 | -5.1238 | -55.97339 | 2025-11-15 01:13:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |


[Clique aqui para ver as próximas entradas](README10.md)
