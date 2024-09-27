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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90ee3d82-1cd9-3dfc-80f6-7eb42cdce1d6 | -7.7885 | -61.2008 | 2024-09-27 02:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| eb2066b7-5526-3fd7-977d-a1d61d00387b | -7.7886 | -61.1817 | 2024-09-27 02:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 20808272-2eb4-366f-9f7c-82f2331bbea6 | -7.9174 | -61.2909 | 2024-09-27 02:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 20ba9159-b46b-354d-8b16-c73a73a9dade | -7.9175 | -61.2718 | 2024-09-27 02:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| bff1f78b-760e-36f4-9472-f9e41e43ec54 | -7.9359 | -61.2901 | 2024-09-27 02:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 4895c383-6b86-396c-a043-f2e59ef3c002 | -7.936 | -61.271 | 2024-09-27 02:35:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6aadcccf-7612-3c51-8d80-c81615b4978d | -8.1394 | -61.2817 | 2024-09-27 02:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 59617e47-51db-341d-92ec-f66a660238fe | -8.1579 | -61.2809 | 2024-09-27 02:35:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8548c3b8-b720-36fa-b0fd-cd580755a596 | -8.556 | -49.6112 | 2024-09-27 02:35:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ca409723-9879-3515-a11f-d5416c5a0d7b | -8.6101 | -63.1226 | 2024-09-27 02:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 3338df95-e102-33f5-ad4b-552a896caf53 | -8.6285 | -63.1408 | 2024-09-27 02:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 65b21895-60d8-3750-8e16-d7468f7fb577 | -8.6286 | -63.1219 | 2024-09-27 02:35:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 7abe7515-1d54-342b-b248-8fe7a49815b6 | -8.7032 | -66.9907 | 2024-09-27 02:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7ceeb8f9-fc9b-3c85-8009-d075772c3464 | -8.7033 | -66.9721 | 2024-09-27 02:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 9c1fa0cb-a02f-3aae-bc8a-977a597c2d58 | -8.7218 | -66.9716 | 2024-09-27 02:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 34e4e14e-cb31-371d-93d0-b21eb3ed0300 | -8.7219 | -66.9531 | 2024-09-27 02:35:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 0f1d5e1a-bf87-3e39-87d7-1a715ea1b367 | -8.8116 | -67.6917 | 2024-09-27 02:35:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 7f4f63c9-a8b1-3d31-a531-f226bf6f5afd | -8.8117 | -67.6732 | 2024-09-27 02:35:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 023c7e0c-ea57-30e0-b4a6-c8ba1ff54ab8 | -8.9977 | -67.3909 | 2024-09-27 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 44ee11f3-63c0-30e1-90b6-22ab52717315 | -8.9978 | -67.3724 | 2024-09-27 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 290.2 |
| a83aecde-08d8-3b28-8216-52b5880239ac | -8.9978 | -67.3538 | 2024-09-27 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 213.2 |
| c09ae052-a48c-37ae-ab3c-7627c53f1c13 | -9.0163 | -67.3719 | 2024-09-27 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| b36c7b90-bc2a-3972-8f0e-7d2b403902ab | -9.0163 | -67.3534 | 2024-09-27 02:35:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| b3a29f50-02cc-3cbc-95aa-6d88e1b3d7f0 | -9.0656 | -61.3934 | 2024-09-27 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f9aa595e-f7e3-3cdc-9914-387a312f8e3c | -9.0657 | -61.3743 | 2024-09-27 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 116ee92a-1193-3b08-aa50-afdd9424d376 | -9.086 | -61.1245 | 2024-09-27 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| f16c6aa4-eb79-3298-967e-7b9b9df3989f | -9.1029 | -61.3726 | 2024-09-27 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 2958d470-be20-3fc9-bad9-d99c9f05e599 | -9.103 | -61.3534 | 2024-09-27 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| cdb3944a-90e6-3af0-a578-b06ecf5a6fc1 | -9.1032 | -61.3343 | 2024-09-27 02:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f3f55a0e-5994-3829-9fce-ef8c497d9d1e | -9.1215 | -61.3717 | 2024-09-27 02:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 5e2e008b-7d8a-3eee-b4ae-150d828b96d6 | -9.1216 | -61.3526 | 2024-09-27 02:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 39efaad7-dfce-3d0e-bec9-3cce31945016 | -9.1217 | -61.3334 | 2024-09-27 02:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e9df7c7c-03dd-39c4-b6a0-312d591966af | -9.417 | -51.4426 | 2024-09-27 02:36:00 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5a8db6dd-c16a-3d7f-b35e-8ebaf04ecb5c | -9.5829 | -50.137 | 2024-09-27 02:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 277.7 |
| 06a8a706-7ac7-3f09-b3ef-1f1369e0f14d | -9.5832 | -50.1157 | 2024-09-27 02:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| ef0b2eae-5b85-32cf-993d-ae6b77491ae2 | -9.6015 | -50.1566 | 2024-09-27 02:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 3e6dbe56-5170-3ee0-8da9-fad2e9676ab0 | -9.6018 | -50.1352 | 2024-09-27 02:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 374.6 |
| 086e73d0-75ae-312c-98dc-96317520da65 | -9.602 | -50.1139 | 2024-09-27 02:36:01 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a391f6ac-92e2-33f8-b7f0-f7386eb84f77 | -9.6206 | -50.1334 | 2024-09-27 02:36:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 7e155533-a0e8-3d35-9d67-0b9a5c2a6ebe | -10.3672 | -53.7858 | 2024-09-27 02:36:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 947ed669-5de4-3c18-9a9f-f3630e3327a4 | -10.6449 | -45.8862 | 2024-09-27 02:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 930bb2ef-b4cb-3f29-8a6a-ed661ae598c8 | -10.6452 | -45.8635 | 2024-09-27 02:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 64856cb0-63dd-3742-9792-4a329742efcb | -10.6639 | -45.8838 | 2024-09-27 02:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 25e34dbc-79d7-3e55-88ee-4c77e69e8043 | -10.6643 | -45.861 | 2024-09-27 02:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1d79f80d-105a-3dcb-911d-1b1b1924b1aa | -10.6846 | -50.9847 | 2024-09-27 02:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 4b42a867-7570-3c74-b007-f0914ae2f769 | -10.7036 | -50.9828 | 2024-09-27 02:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 235cbbf6-fbcf-3b04-8426-c6f76e5fefb2 | -10.7211 | -51.0869 | 2024-09-27 02:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 964d76a2-67ab-3325-a30e-98aa2cea64b7 | -10.7214 | -51.0657 | 2024-09-27 02:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| a03ae981-fcf3-34f3-83ce-2355cbd886da | -10.9264 | -54.2692 | 2024-09-27 02:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 78dd2b85-0d2b-3b82-9191-209d8da51bc6 | -10.9267 | -54.2488 | 2024-09-27 02:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 4f08e5f4-24f6-3331-a706-13aec52dad9e | -10.9453 | -54.2676 | 2024-09-27 02:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| bdc2f487-927a-3384-86bd-284350a752e3 | -10.9456 | -54.2471 | 2024-09-27 02:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 425b5a6d-dd0e-30d6-b453-9a745b48309b | -11.2034 | -54.7752 | 2024-09-27 02:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8e035486-5742-35fc-8231-e6f403a386dd | -11.2223 | -54.7735 | 2024-09-27 02:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 1e2ae34a-a1fc-3fa9-b8c6-e42d4ef568bd | -12.1668 | -50.8218 | 2024-09-27 02:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 894c332d-fa29-3613-97a5-a74c674344ce | -12.1672 | -50.8004 | 2024-09-27 02:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 61eab6c1-930f-341f-8fb5-ad2d2f1759e8 | -12.5464 | -53.5147 | 2024-09-27 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| fe238a35-60e7-30ac-80b4-a9bacf8f92c4 | -12.6639 | -54.6577 | 2024-09-27 02:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d4e5628c-905a-36d3-ba34-c1c4319bfb50 | -12.6824 | -54.6968 | 2024-09-27 02:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| e6e3797a-8a86-3857-96bf-18758a2c71f8 | -12.6826 | -54.6763 | 2024-09-27 02:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| bffe8276-fbcd-3667-8a67-2042a844bbaa | -12.6636 | -54.6782 | 2024-09-27 02:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| fd0f34db-9ac4-3022-893c-d45d340bdaa3 | -12.844 | -54.0215 | 2024-09-27 02:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 32febf14-5db8-3bf9-9da8-e7f8f3e7e934 | -12.8628 | -54.0402 | 2024-09-27 02:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d1143626-6f83-332e-be69-db8ffba45678 | -12.8631 | -54.0195 | 2024-09-27 02:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 954eee99-5988-3a3f-9aae-a33875e4dcbc | -14.9414 | -51.448 | 2024-09-27 02:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.8 |
| d771a543-2fde-336a-8c48-84b569706456 | -14.941 | -51.4695 | 2024-09-27 02:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 34b99cd3-50b1-33c5-a427-07bc0d3716e1 | -14.922 | -51.4507 | 2024-09-27 02:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 64dbeb99-3f59-373e-984c-fea4c66300a4 | -14.9216 | -51.4722 | 2024-09-27 02:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 145.5 |
| eccf24e3-5ed2-30f3-aa04-8fd66062b816 | -16.7325 | -55.8445 | 2024-09-27 02:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 70.4 |
| d894979f-0260-3446-a563-3b097c43e2d9 | -16.8933 | -58.0213 | 2024-09-27 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 79da9316-66f2-3b45-973d-91a9c54bb8b5 | -16.893 | -58.0417 | 2024-09-27 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.2 |
| 99bb8740-fdcf-3f8a-9880-d671adb64cf4 | -19.6136 | -42.8159 | 2024-09-27 02:36:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.2 |
| e70e83e1-7ca9-3539-81e2-3cd94a6c892e | -19.5476 | -47.8675 | 2024-09-27 02:36:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ad4590b6-64f6-3ba2-b102-04d848375155 | -21.0658 | -48.8428 | 2024-09-27 02:37:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 103.0 |
| 99d08811-0526-34d1-a209-74d9848df784 | -21.0665 | -48.8196 | 2024-09-27 02:37:02 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| 74476fb0-c160-31f7-94c3-2b33ffacfa27 | -21.0865 | -48.8381 | 2024-09-27 02:37:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.2 |
| 374c3995-73f7-345f-90b1-ed1d01653633 | -21.0871 | -48.8149 | 2024-09-27 02:37:03 | GOES-16 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 83.6 |
| b9c3ae1c-deec-323c-8941-a039e7f2f29d | -22.7442 | -44.7785 | 2024-09-27 02:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 99.8 |
| 5c3af74c-5501-3030-9c3c-6e8962eb21a2 | -22.7433 | -44.8035 | 2024-09-27 02:37:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.0 |
| 99290c3f-37f8-39c2-b88f-b1d40475f6d1 | -2.3579 | -47.6206 | 2024-09-27 02:45:20 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 1e67411d-80c6-34d0-aa08-45cd03cde6c3 | -2.358 | -47.5989 | 2024-09-27 02:45:20 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 137.8 |
| cb7b33e5-688c-3cd7-a4e3-34ef307f2ba8 | -2.6783 | -57.6087 | 2024-09-27 02:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2818de43-341f-3334-b6ac-ff421f6d46db | -2.6783 | -57.5893 | 2024-09-27 02:45:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 013ba797-81d1-37f0-9199-9fb47f73c253 | -2.8795 | -51.6695 | 2024-09-27 02:45:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 8605338a-3cb6-3d98-867b-ce9d96a24ada | -2.9339 | -57.8562 | 2024-09-27 02:45:23 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| c9967169-606d-3bf8-8559-46da9b5bd8e0 | -3.0107 | -51.0652 | 2024-09-27 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| c9970f28-d42b-3301-ac29-7df6f7f1048e | -3.0292 | -51.0647 | 2024-09-27 02:45:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0c567ae2-1680-3092-bcfb-3290a56a0c87 | -3.2135 | -46.8063 | 2024-09-27 02:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| c9a071e5-187f-3499-b1eb-04857a465b2d | -3.2136 | -46.7843 | 2024-09-27 02:45:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 073222d8-7f1b-34dc-8c0b-f1fea481ef11 | -5.397 | -43.4332 | 2024-09-27 02:45:37 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 69c6b8cc-d352-3586-a125-5554bc612c5f | -6.253 | -62.4671 | 2024-09-27 02:45:42 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| f3afb702-b4d2-3970-a8f4-b56a1a3c63ec | -6.2714 | -62.4665 | 2024-09-27 02:45:42 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 881184bb-c37e-3510-ac81-0bf0d9998b12 | -7.2906 | -61.0869 | 2024-09-27 02:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 089bc822-2348-3144-9a09-3f41e34ae991 | -7.309 | -61.0862 | 2024-09-27 02:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| e83991c9-8023-3a63-8a12-2e2cc3cbd934 | -7.327 | -61.1808 | 2024-09-27 02:45:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| f29e2349-0e28-3750-ad49-6bf7cf37ab7f | -7.7701 | -61.1825 | 2024-09-27 02:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 6dc13288-cd51-3159-8966-8e55bd28292c | -7.8156 | -54.7252 | 2024-09-27 02:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| e9513687-effa-3d1c-b6f1-c8ff9a167e72 | -7.7885 | -61.2008 | 2024-09-27 02:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1e61afd8-8f49-31ea-adea-ccfa3656a852 | -7.7886 | -61.1817 | 2024-09-27 02:45:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 21f51198-c613-3634-a767-0ececdfb0879 | -7.9174 | -61.2909 | 2024-09-27 02:45:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |


[Clique aqui para ver as próximas entradas](README44.md)
