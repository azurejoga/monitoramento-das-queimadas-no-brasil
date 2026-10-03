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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c011592d-d205-3b2a-b54e-93f8c57be4ff | -5.9437 | -43.669399 | 2026-10-03 00:52:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 374380d2-f1e5-36b5-836f-16790ccdeba3 | -3.1175 | -53.738899 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9f27576-f485-3c92-8242-5223dfd09dc8 | -6.8438 | -59.277901 | 2026-10-03 00:52:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73929b69-038e-398f-9273-a03b8e77269d | -3.1371 | -53.734501 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5605c5cb-5912-30a6-bcd9-dfc3794e3746 | -6.8374 | -59.2953 | 2026-10-03 00:52:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39299833-873b-3332-bc5d-f9d948d6a092 | -3.7083 | -50.659901 | 2026-10-03 00:52:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb47ecf7-661a-3c56-8d3f-d976f7b94c7b | -3.1207 | -53.7528 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f33348c3-5c79-396a-b7ba-871f862d506e | -5.9394 | -43.651901 | 2026-10-03 00:52:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d7490a6-b4d5-3f40-b837-7f270fb67255 | -11.454 | -43.404499 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 914e1ca4-ed8f-3a33-bfcc-d7dca0242caa | -4.265 | -50.747398 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57b25e26-6d96-32a0-b64c-aa325c783cc2 | -4.7817 | -55.719898 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7a2c24c-5b12-397c-8019-1efcbf51542d | -2.9692 | -53.271 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2885105d-4dd2-37a0-b7d5-a12cc78db97e | -11.4793 | -43.382 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 76a2ec6c-04f3-33ca-9a10-b163ff713db3 | -3.3238 | -51.6735 | 2026-10-03 00:52:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21a38bef-68a5-323e-a3a8-2957956f344d | -6.7401 | -44.1371 | 2026-10-03 01:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 5c2c3686-8005-37ec-871e-cdf4fb1f15f0 | -6.8579 | -59.2829 | 2026-10-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 5ec7fe35-f1a5-30c9-a2f6-2f56e1f6eb22 | -5.7376 | -45.1533 | 2026-10-03 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| fe7fc2cd-001c-3d1c-894f-8cdf4e5c85af | -4.4507 | -47.9112 | 2026-10-03 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 471ad7e3-f1a0-3cb5-9429-3ca7d73cfef4 | -3.2952 | -53.8194 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a9d6d019-fca4-32f2-814b-ae7377bf8bac | -6.8578 | -59.3022 | 2026-10-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| fbee7dc4-b9b9-3b41-8740-f9dbe9aa4f90 | -3.2768 | -53.8199 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 27443bf1-b816-3294-831c-34124f892613 | -4.5706 | -46.5907 | 2026-10-03 01:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| f4c9740c-1359-35f3-ab0d-f2849a27ae48 | -5.9384 | -43.6482 | 2026-10-03 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 2d8e9312-df7c-398b-9aac-6ffad51c67fa | -11.7187 | -43.4148 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| c60959b7-9a4c-3aaf-ba57-1316dbac3ea0 | -2.8855 | -45.4175 | 2026-10-03 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 5867a90c-ef78-3a5b-a62b-ba0a0e53e4e6 | -11.8127 | -43.5184 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| b3b667d5-2056-35d1-9a41-e94ca75a359a | 1.8037 | -55.5854 | 2026-10-03 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 049853eb-efe2-36f4-932d-201d6f267252 | -3.1116 | -53.7436 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| b6914469-f0f3-3cd1-b3fd-3f49dbf817de | 1.7854 | -55.6054 | 2026-10-03 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 9aa45f54-703f-3485-893a-d43d459614f6 | -3.1299 | -53.7431 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 03d517b4-059b-3e43-b9f3-be4878b3fe7b | -11.4507 | -43.3854 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.3 |
| d0e85725-bf9b-3930-bcee-9b6ee5f2fff0 | -5.7357 | -43.2682 | 2026-10-03 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 9973506c-a988-3719-a56c-0406076f5994 | -3.13 | -53.7229 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 3918eda4-b81c-3b7c-ba52-cd382e5fdc12 | -4.3657 | -43.8242 | 2026-10-03 01:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a49e0930-5f18-3c85-8752-b41fcc40d089 | -10.9879 | -59.1393 | 2026-10-03 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 898b50b8-4872-3c0b-b4dd-f62a821759b4 | -10.9881 | -59.1197 | 2026-10-03 01:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 4a0f88f3-0ffb-32ba-b866-db33d5f74d04 | -5.9571 | -43.6467 | 2026-10-03 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 08b0293a-d5d2-34e0-96e7-dbdc8eb22234 | -6.8395 | -59.2643 | 2026-10-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f1b190a1-6669-3fc4-aedd-d438a0385f53 | -5.7355 | -43.2916 | 2026-10-03 01:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ba1599dd-6d9a-37b6-a8b4-ea605638b7db | -2.8897 | -54.1313 | 2026-10-03 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 19c108eb-1721-30ae-bed6-270dab0f8a75 | -4.7434 | -43.2679 | 2026-10-03 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 79e9eb4a-7d4b-3ac3-b312-a4ad2b953725 | -12.9592 | -41.1904 | 2026-10-03 01:00:00 | GOES-19 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 74.3 |
| 508ef997-e82b-3b74-89a6-6588a289ffca | -12.8676 | -44.6878 | 2026-10-03 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1e618826-bb1f-3356-ac22-542861136873 | -3.2951 | -53.8395 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 604be8b0-852f-303a-9336-43dd6e80be1a | -6.8394 | -59.2836 | 2026-10-03 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 94c7440b-8568-3cd4-9512-3ab40a14c9d0 | 1.7854 | -55.5856 | 2026-10-03 01:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 768ea583-f879-3c7d-b26a-53504840f81b | -2.9041 | -45.4168 | 2026-10-03 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 6664e4ba-e045-3d3d-b81f-72ba6bdd23fb | -11.7169 | -43.5098 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| b13e132f-054f-3dfb-82f3-75157bcae613 | -3.1299 | -53.7633 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3bd5fda8-c23b-3d3a-949c-50f93aab2d24 | -11.7935 | -43.5215 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e5267319-813e-3338-91be-1374e8c23ab3 | -11.4315 | -43.3884 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| c8230edd-c993-31fa-b60a-430f221e1803 | -2.9042 | -45.3944 | 2026-10-03 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 53.8 |
| db91ca04-de6c-3c96-956a-4a3ee8125fb2 | -5.6321 | -44.3862 | 2026-10-03 01:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 6cf4fe88-c378-3df2-92b6-4e70f919eacd | -5.9381 | -43.6714 | 2026-10-03 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 9cee54d3-af01-3eff-b6cf-2b989ceb6216 | -4.4691 | -47.932 | 2026-10-03 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 521d6fc5-cb80-32f0-9e60-1bb31af23eb9 | -3.2767 | -53.84 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 3366637f-e3a1-3d43-9e9a-f4442579b2a4 | -5.9569 | -43.67 | 2026-10-03 01:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 1c1d2a6c-9b6b-3f1d-9a61-4681ca78e6d0 | -2.8856 | -45.395 | 2026-10-03 01:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 66c8b6cc-cfd7-3f56-9443-c06c693e8339 | -4.4693 | -47.9103 | 2026-10-03 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| e9c16b09-a2b7-3090-bf7f-a90aa1be5884 | -3.1483 | -53.7426 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 539311c8-a08d-3d48-bce9-513f1320e385 | -11.8123 | -43.5422 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 3218f6d0-400c-3318-8f96-7ff30041721e | -3.1116 | -53.7234 | 2026-10-03 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 10415447-a685-3335-b98f-c0beb5ef2261 | -4.5708 | -46.5686 | 2026-10-03 01:00:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 1696a1b5-8150-30ce-9ce0-93960a95aece | -5.6134 | -44.3876 | 2026-10-03 01:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 62.1 |
| eed818b4-a6f9-3620-b41b-0c63e1a1378a | -4.4506 | -47.9329 | 2026-10-03 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 7efa5fc3-871a-34d4-94d6-b705292f6793 | -11.7174 | -43.4861 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 5ac9036e-00e0-3b8a-ae35-107a716e01f6 | -11.793 | -43.5452 | 2026-10-03 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| a1dde7e1-c870-39a1-93df-17931c58be4b | -5.7376 | -45.1533 | 2026-10-03 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 6019006a-f84b-38f0-ac28-11529cfee6cb | -10.9881 | -59.1197 | 2026-10-03 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 40783ac7-83a5-363b-b5ff-54b4fcd4e29a | -5.7355 | -43.2916 | 2026-10-03 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 2b31477d-aa09-3f7e-a1d3-ea14796b7b10 | -11.4315 | -43.3884 | 2026-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9dde4d3f-28bb-35d3-8892-0163f016b3b7 | -8.8519 | -66.8012 | 2026-10-03 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| e305dd4d-79cf-3bad-a06c-16b07b25cb6f | -11.7169 | -43.5098 | 2026-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 3be77330-e2ee-30e8-ae92-57fe1eaf7e69 | -3.2952 | -53.8194 | 2026-10-03 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 54ea2114-340e-39ba-b826-36cea313d204 | -11.793 | -43.5452 | 2026-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 9a124490-7b2d-320d-b4e2-23ce730dcc20 | -4.5708 | -46.5686 | 2026-10-03 01:10:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ba19d682-bcaa-332e-8961-b12b7075f785 | -3.2767 | -53.84 | 2026-10-03 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 05998edb-d808-3d36-869b-6068f8c7ba41 | -4.7434 | -43.2679 | 2026-10-03 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 3f3a00ba-c46d-35d3-8585-9bffd4c9b538 | -5.9384 | -43.6482 | 2026-10-03 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 2b4709a9-0649-3963-b5a9-a0d9461ba18c | -5.9571 | -43.6467 | 2026-10-03 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 9f51e409-56cb-3423-b37b-fd508f0d579e | -11.7935 | -43.5215 | 2026-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 17fb6c0d-4d72-3023-b4f0-d5e4db16c1d7 | -3.2951 | -53.8395 | 2026-10-03 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 15455075-d29e-37dc-9b46-2c9d0365d44f | -2.8856 | -45.395 | 2026-10-03 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 33c7bd19-09e1-3738-83d5-44b96ee0ff9b | -11.7174 | -43.4861 | 2026-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 3b856975-ecd3-32c9-b633-95cd6f1b1bab | -11.8123 | -43.5422 | 2026-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| c058fcee-6854-3e10-9ddc-ecee863df688 | -3.1839 | -54.0839 | 2026-10-03 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 94bb7fab-4c2e-3fc6-b0c1-cd2c7cf953b5 | -3.1838 | -54.104 | 2026-10-03 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d24b20d9-f3d8-35de-a623-7e6428681ef9 | -3.2768 | -53.8199 | 2026-10-03 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f81245c6-9d7d-38f6-93ae-04634bdc0aa1 | -5.6134 | -44.3876 | 2026-10-03 01:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| d79c7173-c140-3e15-9efb-dff308961882 | -8.852 | -66.7827 | 2026-10-03 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0f292e02-b3b0-3a71-8d83-1e7c53a4d642 | -6.0508 | -62.5294 | 2026-10-03 01:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| a065ca64-0993-3230-8c9e-1f71d952f87f | -11.8127 | -43.5184 | 2026-10-03 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 2ac1c081-67a1-3e1c-b025-9c88b5e9e9db | 1.8037 | -55.5854 | 2026-10-03 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 386089f9-190d-375c-8ba4-b24e212b8af6 | -2.8855 | -45.4175 | 2026-10-03 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.4 |
| eabaeec3-869a-3c91-b4d2-1e04ddd99f05 | -10.9879 | -59.1393 | 2026-10-03 01:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 869147f2-80f0-3f18-b087-7c98134baf78 | -6.8394 | -59.2836 | 2026-10-03 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 0a8c3499-c074-34f5-b1d6-a92fcf280282 | -6.0507 | -62.5482 | 2026-10-03 01:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 3c30c418-4f64-3b82-ad0c-21ff848c154e | -5.9569 | -43.67 | 2026-10-03 01:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 81a7128e-5bf4-3ad6-ab09-2d157d411c7b | -5.9381 | -43.6714 | 2026-10-03 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b3fef20d-f6c4-3ffa-905c-01a6d3c77c38 | -8.8705 | -66.7822 | 2026-10-03 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |


[Clique aqui para ver as próximas entradas](README12.md)
