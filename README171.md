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

## Dados Diários - Página 171

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7c2b83a-1c82-3a5d-8458-50f0505bf345 | -19.98626 | -55.50305 | 2024-09-26 05:50:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db857aee-55b9-39af-a141-5ebb5018b32f | -19.98584 | -55.50878 | 2024-09-26 05:50:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 876a41d0-ed4b-378d-b31d-e62cb99da2b6 | -17.10683 | -56.16989 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 34ffd642-5f37-378e-ae3a-ac3a1ce14030 | -17.1063 | -56.06802 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 70e9eaa0-ae6c-33a3-a9a6-d1620a6fbf54 | -17.10572 | -56.07412 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 879d6fa3-f65b-3a8c-a793-298c7f89bee0 | -17.10515 | -56.08021 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 40f4a0fa-75bc-3da4-9785-633f76a5fc7f | -17.10493 | -56.1539 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| ebf4adbe-d030-323b-b8a6-358ba4462056 | -17.10435 | -56.15995 | 2024-09-26 05:50:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f6a9f35c-b460-3b15-ae3e-e39f940b8ddc | -9.4322 | -65.4607 | 2024-09-26 05:56:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 1e2b866a-28d3-3bb8-891b-7d098337eb83 | -9.4323 | -65.442 | 2024-09-26 05:56:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| d4f26bfb-2e72-3157-8791-bc69b27af959 | -11.2599 | -65.299 | 2024-09-26 05:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 489f887d-cbfb-38b7-8fe0-4de79f6d79de | -11.26 | -65.2801 | 2024-09-26 05:56:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 67abb896-977c-3329-a0c6-387397867da0 | -13.4997 | -61.2308 | 2024-09-26 05:56:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 585b2953-6b00-3210-818f-8b83bbe77a5a | -12.95 | -45.33 | 2024-09-26 06:04:10 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 704b6887-93a3-37e6-b4a2-436744973d5c | -12.86 | -51.27 | 2024-09-26 06:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3a323037-4187-3edd-8178-9389bcbc2a8b | -12.89 | -51.28 | 2024-09-26 06:04:13 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b209ff43-da33-3e52-a360-0fdf98ed9154 | -10.04 | -53.48 | 2024-09-26 06:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b154eccc-f061-3bdb-a693-75d5fe3802ee | -10.01 | -53.48 | 2024-09-26 06:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdadc1e8-ebdd-3b7a-87b0-9840aec54b7f | -9.4323 | -65.442 | 2024-09-26 06:06:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 529b0d51-75c5-3f50-bb02-0c5e8c38640e | -9.4322 | -65.4607 | 2024-09-26 06:06:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| ad1c8f92-fde0-327f-9592-294dc008d3d9 | -11.26 | -65.2801 | 2024-09-26 06:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 850bd1c9-cdf0-3706-994f-848e7bab20eb | -11.2599 | -65.299 | 2024-09-26 06:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.1 |
| bb3d4321-4fc1-3fc6-87c1-96f62cf2dc21 | -11.955 | -60.363 | 2024-09-26 06:06:15 | GOES-16 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 68811184-aca8-30d0-8390-130a1fe0ade3 | -12.8411 | -62.6874 | 2024-09-26 06:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 175af808-484e-3f61-b9ec-2e18928b39a6 | -12.822 | -62.7078 | 2024-09-26 06:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 0af6a226-aea9-39b8-a320-b03eca97c206 | -12.8222 | -62.6886 | 2024-09-26 06:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 291fb283-f1f1-309e-9476-571db18982a6 | -12.841 | -62.7067 | 2024-09-26 06:06:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 05414e34-546d-364a-99f2-9bb97242dc1e | -15.3371 | -58.1651 | 2024-09-26 06:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 204.4 |
| 304bf288-25d4-3d3e-8a9f-a67249969e93 | -15.3368 | -58.1852 | 2024-09-26 06:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| c140d372-79b6-3069-a3f6-773161b8029b | -15.3562 | -58.1833 | 2024-09-26 06:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 124.7 |
| a26952af-7d01-37f9-ac91-3b8e6c9d2095 | -15.3564 | -58.1632 | 2024-09-26 06:06:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| a79466b7-07e0-39bf-b448-41081ca64354 | -9.1219 | -61.3143 | 2024-09-26 06:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| e6565d4d-4d8c-3747-9cbd-e70ed726fdac | -9.1217 | -61.3334 | 2024-09-26 06:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| aaf52467-351b-3be0-a819-63e0853a4fff | -9.1216 | -61.3526 | 2024-09-26 06:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 2ed997cd-c9af-3697-9545-51275149de6c | -9.1033 | -61.3152 | 2024-09-26 06:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 1f341044-3c39-3ab2-a8e7-29c482bdbf3a | -9.1032 | -61.3343 | 2024-09-26 06:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 723a1974-02a1-3cb1-b2e0-14115db68fbc | -9.103 | -61.3534 | 2024-09-26 06:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 6ab1c6d8-6653-3324-baf9-8ac59f192f45 | -9.4322 | -65.4607 | 2024-09-26 06:16:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| fffb3d28-4fc7-304d-90a6-bde1148a7995 | -11.26 | -65.2801 | 2024-09-26 06:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.7 |
| c9cb0249-f2a5-3be4-9bd3-52af69d10363 | -11.2599 | -65.299 | 2024-09-26 06:16:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 4285dd43-9842-39a7-b27c-ee29c4d90bb2 | -11.616 | -60.3463 | 2024-09-26 06:16:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 36.5 |
| cc9997c3-1985-3097-8cf6-6d22f8c762ea | -11.5972 | -60.3475 | 2024-09-26 06:16:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d6071cfc-c2d0-3afc-954a-720d890bc929 | -11.597 | -60.367 | 2024-09-26 06:16:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| dedd4e79-5684-3463-9e29-771d40887c1d | -12.8411 | -62.6874 | 2024-09-26 06:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 4d29aa25-4f25-336f-b5a9-8366995e2558 | -12.8222 | -62.6886 | 2024-09-26 06:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a984998e-5dc3-305a-bbbd-feb4307ec8f5 | -12.822 | -62.7078 | 2024-09-26 06:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 8d254ede-f35d-3623-a141-8bb02207bbae | -15.3564 | -58.1632 | 2024-09-26 06:16:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 118.8 |
| 457af160-80bc-33a6-abc3-4fd74351fb88 | -15.3562 | -58.1833 | 2024-09-26 06:16:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0d542c27-a007-3f29-a5a7-20ab025db02c | -15.3371 | -58.1651 | 2024-09-26 06:16:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 212f7587-640a-320c-b351-184c0b1c42e2 | -15.3368 | -58.1852 | 2024-09-26 06:16:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7b849c0a-6833-3c75-91b5-f01116742871 | -8.8293 | -63.699 | 2024-09-26 06:25:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 3aec0ca7-fda2-37b8-ac9e-b72250358bf8 | -8.8292 | -63.7179 | 2024-09-26 06:25:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 34.3 |
| ce3eb82b-7be5-3a10-82e3-69c92998c0bc | -9.1217 | -61.3334 | 2024-09-26 06:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2ca8c62f-9ef0-3901-836a-7feae538b41a | -9.1216 | -61.3526 | 2024-09-26 06:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.6 |
| f1d6463c-b2e5-3350-bf17-7bf3e27d5e58 | -9.1046 | -61.1237 | 2024-09-26 06:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 6c01afba-b944-34e0-b93a-fa375f8b233c | -9.1032 | -61.3343 | 2024-09-26 06:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 82661ed4-bed6-3fdd-8286-de7d5479894c | -9.086 | -61.1245 | 2024-09-26 06:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 801a3a38-c4e5-346a-ae3d-755eb638b6b3 | -9.4322 | -65.4607 | 2024-09-26 06:26:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| b5f7fef5-5f11-3124-a7f1-d0865d11651d | -11.2788 | -65.2793 | 2024-09-26 06:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.0 |
| eef5d711-185f-3632-9318-2553870f2837 | -11.26 | -65.2801 | 2024-09-26 06:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3ffe3c6e-069b-3e77-82de-e9443a19be10 | -11.2599 | -65.299 | 2024-09-26 06:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bc502522-620e-30b5-ac99-e371b8ac6d84 | -11.616 | -60.3463 | 2024-09-26 06:26:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c329fa4f-cd37-306f-a088-fdb48e8c22c5 | -11.5972 | -60.3475 | 2024-09-26 06:26:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 751b1de1-a261-3c31-bf65-8c9087d02d66 | -11.597 | -60.367 | 2024-09-26 06:26:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 11644205-b3e4-3144-9a3f-c3c17d65d93c | -15.3564 | -58.1632 | 2024-09-26 06:26:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 81692d72-072c-3534-892e-963108504328 | -15.3562 | -58.1833 | 2024-09-26 06:26:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| ef1a0e7c-585e-3853-867d-34fdc2729060 | -15.3371 | -58.1651 | 2024-09-26 06:26:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| eee6e6df-d35a-3d62-b368-b3d217894ba4 | -15.3368 | -58.1852 | 2024-09-26 06:26:33 | GOES-16 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 4238db82-b3d5-3e86-b516-72654ccbed47 | -16.8591 | -57.6993 | 2024-09-26 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| a80665c4-a75c-3275-85a9-9ab2b199a837 | -16.8588 | -57.7197 | 2024-09-26 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 9c6da344-4c15-3916-82c6-a39842099b15 | -16.8396 | -57.7015 | 2024-09-26 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| c9e5dd86-18a3-33de-bd12-d1968b4864e3 | -16.8231 | -57.4994 | 2024-09-26 06:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| a5a91326-db33-3e0c-89a0-9fc6caf168d4 | -16.8787 | -57.6971 | 2024-09-26 06:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| 5906fe55-b9a0-355c-8281-025a93e015ab | -16.8784 | -57.7175 | 2024-09-26 06:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.4 |
| a39842fb-66b2-3554-b31f-60d2e6abe80b | -20.6279 | -51.5169 | 2024-09-26 06:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.6 |
| af6a8bfa-d97c-3d30-9116-c00d495862c2 | -20.608 | -51.4986 | 2024-09-26 06:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.4 |
| 2890b17e-408a-3d43-b959-bc20a4794074 | -20.6074 | -51.5209 | 2024-09-26 06:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 168.4 |
| d20c30b8-a77d-3f34-9495-e2444a9e49d9 | -20.587 | -51.5249 | 2024-09-26 06:27:01 | GOES-16 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| 156c45e9-6e69-3aac-9021-563e3d8aac0f | -21.9381 | -48.5453 | 2024-09-26 06:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 11ca9d4e-5c40-38a6-80d3-579a64d2e11e | -21.9374 | -48.5688 | 2024-09-26 06:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 88c34e96-2bb9-3865-9ed9-69218f7e4b90 | -9.1219 | -61.3143 | 2024-09-26 06:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.9 |
| accd2e9c-421b-3ef5-b9f2-787d32f1ced3 | -9.1217 | -61.3334 | 2024-09-26 06:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1c04ebfc-ddaf-3ce8-a0b0-9cea4d85b11f | -9.1216 | -61.3526 | 2024-09-26 06:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 624a6b33-bfcb-34a8-8a51-9153a5656e49 | -9.1032 | -61.3343 | 2024-09-26 06:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| bbbeabac-7824-39e6-a7f4-fe83fdb6bfa5 | -9.086 | -61.1245 | 2024-09-26 06:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 59d9a484-4128-3c78-a9f9-cd056ea34650 | -11.26 | -65.2801 | 2024-09-26 06:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 4119a4c6-358a-3f6d-856e-7e1777e12b76 | -11.2599 | -65.299 | 2024-09-26 06:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| a631259a-e8d4-3a70-9901-719108b2a38c | -11.5972 | -60.3475 | 2024-09-26 06:36:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 498bf195-5504-34a7-ab37-bbacc4a51a12 | -11.597 | -60.367 | 2024-09-26 06:36:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 9bd5533a-56c4-3193-91a2-cd33a23b59f6 | -16.118 | -51.9867 | 2024-09-26 06:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 39.5 |
| b3406be0-f1b5-342b-8bc8-141ad211354a | -16.7992 | -57.7876 | 2024-09-26 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.2 |
| 98c974ca-11de-3038-9830-bcacbdd386c1 | -16.8039 | -57.4811 | 2024-09-26 06:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| 60c8ab09-1d41-3658-b398-863c807a2fd9 | -3.76363 | -69.47053 | 2024-09-26 06:37:00 | NOAA-21 | TABATINGA | AMAZONAS | Brasil | 1304062 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ed4cc9-210b-3b19-881e-53a16c71887e | -3.70144 | -69.39919 | 2024-09-26 06:37:00 | NOAA-21 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 97230877-8799-3bc1-8227-f3a57e921c77 | -3.70061 | -69.39712 | 2024-09-26 06:37:00 | NOAA-21 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cae8f49f-fcef-31a2-8e2d-38b67cfe0795 | -20.6284 | -51.4945 | 2024-09-26 06:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 43.3 |
| 6428804e-4d0b-3861-a6a4-3a5465e72822 | -20.6279 | -51.5169 | 2024-09-26 06:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 2df06000-e38f-390e-878c-e98ad7f0299c | -20.608 | -51.4986 | 2024-09-26 06:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 114.6 |
| 279c1269-2a74-3879-a60b-9be3ea6bebfc | -20.6074 | -51.5209 | 2024-09-26 06:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 208.6 |
| 379e4a25-87b2-3359-9567-5b08d87acbae | -21.9381 | -48.5453 | 2024-09-26 06:37:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 62.7 |


[Clique aqui para ver as próximas entradas](README172.md)
