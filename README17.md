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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e1f4848-bd27-3b2e-9a0d-e153bb74a7be | -3.1282 | -54.2459 | 2024-11-02 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 680eeb5e-6bc6-3c1b-87c4-5a7dec788448 | -3.2249 | -44.431 | 2024-11-02 01:35:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 83efe8e6-3021-3a4d-a6cc-3540597afd8e | -3.1098 | -54.2665 | 2024-11-02 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d892e777-fd0e-3b93-ace2-cae979a79370 | -3.1281 | -54.266 | 2024-11-02 01:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 66044d44-1b6c-3df3-9beb-e05fc3f26c30 | -3.7701 | -43.5554 | 2024-11-02 01:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| 375581f0-fcfa-3014-8869-6da3d6ace7ad | -3.7703 | -43.5323 | 2024-11-02 01:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4983e061-63eb-3b8e-b295-4b1e80bf5935 | -3.7888 | -43.5545 | 2024-11-02 01:35:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e993fa4d-d511-3caa-961c-be9f61d805b7 | -3.8144 | -48.9729 | 2024-11-02 01:35:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ed76761f-554c-3ee2-8e68-1ad879e981a1 | -3.9289 | -48.3458 | 2024-11-02 01:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 24ed6f78-1330-3d9b-8329-3dd6d1c0d857 | -3.9474 | -48.3451 | 2024-11-02 01:35:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| dfb59f77-9c1b-3df2-8023-d802fe639a7a | -4.4054 | -43.4746 | 2024-11-02 01:35:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 2d8012e6-e8c8-334e-91b7-dd4691d21089 | -4.3537 | -48.6068 | 2024-11-02 01:35:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 76ff098f-6136-3dec-b12e-119ea112964b | -4.5577 | -43.0928 | 2024-11-02 01:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| daad7b2f-ec47-3d62-8ec8-4fb8402610ae | -4.5764 | -43.0916 | 2024-11-02 01:35:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 1309ef06-8a6b-31cf-92de-7d66dc5e09fd | -4.8067 | -44.8061 | 2024-11-02 01:35:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2ccd0612-f955-39a5-a9ab-6c829e34e4d3 | -4.8068 | -44.7834 | 2024-11-02 01:35:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1459c8a8-0fc7-3b9e-b7af-d35d29e93641 | -4.9252 | -49.1573 | 2024-11-02 01:35:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| cd556563-3ab6-30fe-b890-5f18494d0323 | -4.9438 | -49.1564 | 2024-11-02 01:35:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 4e1c2db7-ea33-3670-84df-3d2e71d95c79 | -4.9439 | -49.135 | 2024-11-02 01:35:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| d37fb5cf-6b1e-315f-a4b2-f1a622063517 | -5.3252 | -43.065 | 2024-11-02 01:35:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| f722d555-6d9e-39fa-9831-ff96bc02e243 | -7.1294 | -46.3711 | 2024-11-02 01:35:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 5759c743-3ab9-3728-987d-fe4ac747271f | -10.9811 | -45.1104 | 2024-11-02 01:36:08 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.3 |
| ae9662bd-1908-33f5-b57e-734d107e2298 | -1.5715 | -52.1894 | 2024-11-02 01:45:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 428fb1b7-eb11-37e1-9220-1ea25218ef76 | -2.195 | -46.4634 | 2024-11-02 01:45:18 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 38f02d1d-9b6a-388a-889d-cb887634f325 | -2.2568 | -50.4376 | 2024-11-02 01:45:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| aee17ea1-60b9-3cec-b128-5e8369e79823 | -2.2663 | -53.7422 | 2024-11-02 01:45:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| d54b6a00-5ecc-3291-a017-db0c563ba5f7 | -2.8386 | -52.8794 | 2024-11-02 01:45:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 8fc10206-aa83-3eab-85de-767b1dd9c2e8 | -2.8509 | -49.3895 | 2024-11-02 01:45:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| a581cf47-d304-3198-b542-2040eb10a7dd | -3.0734 | -54.167 | 2024-11-02 01:45:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 87374f73-5b4e-3113-bf53-736bcd567cd2 | -3.1097 | -54.2865 | 2024-11-02 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 9d834cf1-2e39-3410-a10d-05c4a098c74b | -3.1098 | -54.2665 | 2024-11-02 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 342d8401-8180-3aac-a0a4-647aade48b28 | -3.1281 | -54.266 | 2024-11-02 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 5d2ecf36-674a-39ef-93f9-fa63dcd87900 | -3.1282 | -54.2459 | 2024-11-02 01:45:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a6c03845-8ce4-37b3-9c4e-f921de8cfa0a | -3.1767 | -51.0812 | 2024-11-02 01:45:24 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| a9e86a9f-f14e-3120-b9f5-87feadd7523a | -3.2249 | -44.431 | 2024-11-02 01:45:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 13650318-f0ce-3686-80a7-9d7cfbba5431 | -3.225 | -44.4081 | 2024-11-02 01:45:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 81.5 |
| a2e81280-c809-3122-9817-2cdbbe63d900 | -3.2601 | -53.3557 | 2024-11-02 01:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0591521a-8186-325c-85e7-926c41153fb1 | -3.7701 | -43.5554 | 2024-11-02 01:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 119.0 |
| bdc461c7-961d-38a1-89d5-a638cf2ec9d4 | -3.7703 | -43.5323 | 2024-11-02 01:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| a4db93b9-4eb6-305b-b946-09153c450ac6 | -3.7888 | -43.5545 | 2024-11-02 01:45:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d1d5c298-9ae5-3085-b1a0-dd399fa52bc1 | -3.9289 | -48.3458 | 2024-11-02 01:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 9833e45b-59fe-38c3-8285-82c4d19dbb19 | -3.9474 | -48.3451 | 2024-11-02 01:45:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| f3d05449-a978-3477-bcc7-1a12a0862282 | -4.4054 | -43.4746 | 2024-11-02 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| ca74ff67-b078-32a4-94ee-38e3a2075972 | -4.3537 | -48.6068 | 2024-11-02 01:45:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 64edf95d-7ef2-3b3c-9419-5dd918806298 | -4.5575 | -43.1162 | 2024-11-02 01:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8ce19768-9d39-3ca1-a8ee-ce0b59b755a2 | -4.5577 | -43.0928 | 2024-11-02 01:45:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 43ec2f5c-9ebb-335b-a2e9-998df752ceb1 | -4.8067 | -44.8061 | 2024-11-02 01:45:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 495f3c3f-8349-3370-9642-4cdcf6fb030c | -4.8068 | -44.7834 | 2024-11-02 01:45:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 8ee1959b-7d77-302a-b43d-963261e54713 | -4.8255 | -44.7822 | 2024-11-02 01:45:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 96e4b9d1-7aaf-38b1-924a-c5b0587dbfaa | -4.9252 | -49.1573 | 2024-11-02 01:45:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 3df56dbd-e1e8-32c3-8213-7573ac2a36e6 | -4.9438 | -49.1564 | 2024-11-02 01:45:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| d0c6677e-87de-3ba8-b5b2-93f60176b7fd | -7.1294 | -46.3711 | 2024-11-02 01:45:46 | GOES-16 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 8d147ed4-77bf-3af9-9b31-b4f6ef5567f4 | -1.5715 | -52.1894 | 2024-11-02 01:55:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c5a0ef5a-806d-35b9-bae4-025c24aec77b | -2.2663 | -53.7422 | 2024-11-02 01:55:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.1 |
| d3554fcc-aeb4-30d0-b190-2fccbd283145 | -2.8509 | -49.3895 | 2024-11-02 01:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| f1950924-1272-3749-bab7-46262f3001b2 | -2.8386 | -52.8794 | 2024-11-02 01:55:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| c296b3a0-a8b5-38fc-a964-3ab3ac42b5ac | -3.0734 | -54.167 | 2024-11-02 01:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 69788fb5-b76d-380d-a001-d196e228bde7 | -3.1097 | -54.2865 | 2024-11-02 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 6fb74c65-81ef-3f04-b2a9-03682e640934 | -3.1098 | -54.2665 | 2024-11-02 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d8b94965-6eb2-31ae-b918-dff14bc33ddf | -3.1281 | -54.266 | 2024-11-02 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 75138572-abb5-3677-b41f-89e015b700a0 | -3.1282 | -54.2459 | 2024-11-02 01:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 78c24850-28ad-31a5-b967-415261bc3a18 | -3.2249 | -44.431 | 2024-11-02 01:55:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 35db5874-1126-30a6-bbdb-a8a257a0f826 | -3.225 | -44.4081 | 2024-11-02 01:55:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 9358533d-59b4-3584-8e80-2ea675ece28a | -3.2601 | -53.3557 | 2024-11-02 01:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 11ae971e-44b9-328d-84b5-dc5ecb85621c | -3.2602 | -53.3354 | 2024-11-02 01:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| aafd6b05-8f44-3c62-9095-d6f4b29ac583 | -3.7701 | -43.5554 | 2024-11-02 01:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| fea616da-541c-39dc-bc31-f9c54282523c | -3.7703 | -43.5323 | 2024-11-02 01:55:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 6b4f4a84-230a-326f-b1d2-aaea4cb99337 | -3.9474 | -48.3451 | 2024-11-02 01:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 1ffd493b-14c7-315a-bace-c9db2a26b8e1 | -3.8144 | -48.9729 | 2024-11-02 01:55:28 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| efa83f65-2e31-34e5-9be2-3741091df0a2 | -3.9289 | -48.3458 | 2024-11-02 01:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 999f9dda-bf5e-31fc-80e3-05ad7d872511 | -4.3537 | -48.6068 | 2024-11-02 01:55:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 053ed671-fc78-3f3e-958a-6c12f33ff8a3 | -4.4054 | -43.4746 | 2024-11-02 01:55:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| db9247c3-0630-3267-8f5d-46d68c4ac0c9 | -4.5575 | -43.1162 | 2024-11-02 01:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 894a7f00-f644-35cc-8e7d-c0f340956b4d | -4.5577 | -43.0928 | 2024-11-02 01:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 5c4924d3-c291-350e-a984-7470744f9982 | -4.5764 | -43.0916 | 2024-11-02 01:55:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 8d658601-6c83-35b3-ac46-25d1b030724f | -4.8067 | -44.8061 | 2024-11-02 01:55:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| c12d7edf-1c53-318f-9cd9-d2e649edb867 | -4.8068 | -44.7834 | 2024-11-02 01:55:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| edc4d428-5374-3f79-9aca-b86097bdb852 | -4.8253 | -44.805 | 2024-11-02 01:55:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| acd431b0-1d1b-358f-84e3-faad4874ad88 | -4.8255 | -44.7822 | 2024-11-02 01:55:33 | GOES-16 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| dc8a3ef0-ca8b-318f-98a0-92afe1390c21 | -4.9252 | -49.1573 | 2024-11-02 01:55:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| fefec425-174a-3082-b0b4-4bfb73b6d71c | -4.9438 | -49.1564 | 2024-11-02 01:55:34 | GOES-16 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 81767951-7d92-3a3d-a615-a2cad9f40c1c | -5.3252 | -43.065 | 2024-11-02 01:55:36 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| dbde6971-d73d-3c30-bb64-3d15a34798bb | -1.5531 | -52.1896 | 2024-11-02 02:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f67a7d0a-17e3-3b4d-853e-966b51777cc7 | -1.5715 | -52.1894 | 2024-11-02 02:05:15 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 98488128-a80b-3425-a501-453be5fc8183 | -2.2568 | -50.4376 | 2024-11-02 02:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7b669004-afb6-3752-950b-d60c643b07e9 | -2.2663 | -53.7422 | 2024-11-02 02:05:19 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 5988d1ce-48a2-3edd-a18e-64dba15bfc56 | -3.0734 | -54.167 | 2024-11-02 02:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 39bbc951-c39e-3b97-9fbc-73c5862b07c4 | -3.1098 | -54.2665 | 2024-11-02 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| cbccbd8f-601a-35a0-b96c-316a40b6099b | -3.1097 | -54.2865 | 2024-11-02 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c46419ed-40c4-3fb5-b475-55faa3d805bf | -3.1281 | -54.266 | 2024-11-02 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 32d246c0-97f5-3fcb-ba7b-b5a0b06e5ea2 | -3.1282 | -54.2459 | 2024-11-02 02:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8bc80a9b-bdbe-33ed-8fa9-f3796919f005 | -3.2249 | -44.431 | 2024-11-02 02:05:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 96d5ac6a-5b16-3357-a131-25406e5c780a | -3.225 | -44.4081 | 2024-11-02 02:05:24 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 60.9 |
| fb58638b-9737-3b31-8231-e6b1650d79a8 | -3.2417 | -53.3562 | 2024-11-02 02:05:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| d4cd71f2-80e8-3adb-9516-f67293ab907d | -3.2601 | -53.3557 | 2024-11-02 02:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 4d629735-f61a-3ac6-9aa6-5586fb94e471 | -3.2602 | -53.3354 | 2024-11-02 02:05:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 6763dc6a-9eb2-32cd-a726-aef96944f558 | -3.7701 | -43.5554 | 2024-11-02 02:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 91bfa5dc-b462-3478-83ce-9e24d50c0dcd | -3.7703 | -43.5323 | 2024-11-02 02:05:27 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1ea01069-3c0f-3cea-8567-a93eab291c47 | -3.9473 | -48.3666 | 2024-11-02 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 1695f3f0-7bea-31d3-b485-bbbb2a579307 | -3.9474 | -48.3451 | 2024-11-02 02:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |


[Clique aqui para ver as próximas entradas](README18.md)
