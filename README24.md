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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1936898a-bce9-33ff-920d-9a26a72b08d2 | -10.72247 | -68.5481 | 2025-10-21 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 319c45d0-54cd-3d48-abe2-a7c01d4e0617 | -8.99683 | -65.92155 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 5d303b4f-6040-3ab1-9823-f627d7426f9c | -10.30299 | -68.86288 | 2025-10-21 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6aa114fa-5888-370b-a948-be7e8c48dd9a | -9.11997 | -65.36373 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a4a78da-6205-3040-946f-084fa845fead | -10.36454 | -67.98038 | 2025-10-21 05:36:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 624f2259-d76f-31f9-a050-941c919b8bd8 | -9.53891 | -64.57481 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2c5f451-3e46-328c-bf70-836caff22237 | -9.88711 | -64.24159 | 2025-10-21 05:36:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6f64a59e-349f-35f7-b40f-a1c063c44c60 | -9.01044 | -65.9238 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ade0f41d-f625-326f-9374-69e538638286 | -7.57008 | -64.54109 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e65a5c77-46fc-3cbe-b3bb-6b323972428c | -8.99003 | -65.92045 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6be2946d-ca7c-3011-b4f5-7341e59cf419 | -9.74644 | -64.20838 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e6dee5f-b1b8-317c-b0c0-92e83bc00dd3 | -8.75946 | -66.58104 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 393c7c21-726c-3319-806d-484813d79ecf | -9.37582 | -62.63667 | 2025-10-21 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 329ede14-6158-3a04-87eb-ca30b6648639 | -9.48519 | -57.92615 | 2025-10-21 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 950891b5-3dc1-3b1a-a57a-6102c5e97363 | -9.71986 | -67.48463 | 2025-10-21 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5e61d86-aaf0-30c6-b77c-dfb6f7071b17 | -9.01325 | -65.92805 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f3a0a59-a23e-3aa5-9954-45b88c3ef72a | -9.89753 | -64.17535 | 2025-10-21 05:36:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a6b7deb-1409-3612-a5fb-7851c761aa47 | -8.53932 | -67.05574 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c24daeaf-371a-3224-97c1-e8073f5b20c4 | -9.01205 | -65.93546 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60434bd2-a57c-3d9d-bddf-1c177b609ed4 | -11.75547 | -62.87156 | 2025-10-21 05:36:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50609c05-4438-3994-96e6-44abcf3d33a9 | -9.18889 | -61.38676 | 2025-10-21 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f81f7553-76b0-3fbf-ae44-c3b75ca2c72f | -9.79273 | -64.75205 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cc43ec7-500b-3b9b-8e59-97127548becb | -12.15422 | -63.05795 | 2025-10-21 05:36:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3df34d87-4bc6-39b0-b51f-c9474c03602d | -9.68231 | -63.17886 | 2025-10-21 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c52c529f-40a0-3740-b42a-e389115695e4 | -8.99784 | -65.93692 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98ce1f4d-4ad6-3a9e-803b-12f652953ebf | -9.56145 | -63.25824 | 2025-10-21 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80ace3b6-ee96-3bf6-aae1-a2908731c5eb | -9.47713 | -67.06644 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fc8d723-8f1d-3881-be8b-5b42714fb45b | -8.36373 | -64.07925 | 2025-10-21 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8be36ee-899f-3338-bb27-c1f4240195c5 | -10.87876 | -68.42704 | 2025-10-21 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdc301fe-243d-3246-8a78-d5ba51cf5d7e | -9.55886 | -63.25859 | 2025-10-21 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3db9f388-ff44-3ec3-8c62-66232453451f | -10.30214 | -68.86778 | 2025-10-21 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb89840d-f58d-3814-bf0c-aca49eba371f | -9.80344 | -64.96223 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e0023974-f92c-3ae8-8fcc-15620fe1024a | -9.04991 | -65.70033 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba0a8ec4-7ca5-3c2e-bf2f-a4c6c8c01739 | -9.55289 | -57.35711 | 2025-10-21 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ded4158-7768-3f42-8015-a2b2d5e1660f | -9.64161 | -67.68524 | 2025-10-21 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50901c82-5755-3f99-8b15-d197164d6743 | -9.799 | -64.9687 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6dbb5ea7-0214-3bdd-b42f-dff2175dae2d | -10.29957 | -67.35549 | 2025-10-21 05:36:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4dc84470-5da1-393a-9621-976177d4d791 | -9.79956 | -64.9652 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a4f9642-c9c9-3a52-b2e3-a895f28bb35b | -9.77712 | -62.76129 | 2025-10-21 05:36:00 | NOAA-20 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e0cf2c86-2daa-3ef5-bf83-6e32e1fe3d07 | -9.22699 | -65.73602 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3ea49f4-dce6-3c95-b4b0-8c1a7aecc435 | -8.99403 | -65.9173 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2534903c-3231-318c-ad49-587f730810dc | -9.01146 | -65.93917 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a659a980-ee87-3983-aaae-813f9faff25e | -9.78442 | -63.81352 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef83221-851b-380f-9fb7-01ab55a26752 | -9.50572 | -66.71623 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 36d98277-93be-3f6e-8b3f-e3728b3c5ef3 | -9.72276 | -67.48946 | 2025-10-21 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2a6d0fc-2dd0-3e74-8b2c-1ffa7f83f908 | -9.67991 | -63.17833 | 2025-10-21 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 819cafbc-7feb-357c-9e05-44a7eeca6036 | -9.64735 | -65.25917 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e588380-0bc2-3bd8-bd9a-6bccb3d07d8b | -10.88249 | -68.42772 | 2025-10-21 05:36:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f443d0c-a73b-35ca-8089-69b1d488d68d | -9.00805 | -65.93861 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb582d57-4b9e-3e30-b94f-644a81456c4a | -8.6677 | -66.58635 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9224be5-80b2-3303-b83d-b220ca7331e3 | -9.73578 | -65.02332 | 2025-10-21 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bb67b71-693a-30b0-804f-acf743e7bc73 | -8.92288 | -66.88766 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91680d55-d9cf-39ae-aa38-bd754ff3bde5 | -8.99844 | -65.93322 | 2025-10-21 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42f59a81-3428-3f67-9ff3-0d41883efd11 | -17.4307 | -55.04463 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3054fec1-01cd-3696-b0f1-336742d50a14 | -17.68412 | -52.25429 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d4b7567e-c92b-3fbe-80bd-ce6482eb27fa | -18.16288 | -52.9846 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7f065037-14a0-3710-9474-142f3d407101 | -17.6815 | -52.26831 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a897dae-5aa1-3617-887a-6a1216ada7df | -17.41974 | -55.05363 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 08981d77-0c33-3df0-bc7b-e22896737b1f | -17.40481 | -55.06413 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4ed79e04-4051-375e-84a8-c2b4437ca39c | -17.41926 | -55.05811 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 9b85a94f-4070-366f-88fe-8444fb125156 | -17.68319 | -52.24853 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0102f062-c2d5-3621-86fa-55386eda10dd | -16.5325 | -53.7234 | 2025-10-21 05:38:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ee65c5c8-2bd4-3cea-ae05-948e8ba9be3f | -17.42655 | -55.02618 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9f733962-fb5e-3ba2-93e5-e2b18e14e3a5 | -17.40743 | -55.05674 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 6fadcba3-7b17-3364-9f60-2afb05e17f7a | -17.40696 | -55.06117 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0300aa7b-0f47-345f-bc6f-74b85a68c5a3 | -17.41204 | -55.0515 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2e9979d2-4283-3019-9326-3f26a2bf6095 | -18.19102 | -52.97475 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e395655-ee2d-3fe3-8b95-d04b446dd42c | -17.68476 | -52.24739 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| afed9b1d-5eba-3e55-abe0-af51c5debc79 | -19.09227 | -57.5382 | 2025-10-21 05:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e3f56c28-11ca-3155-80ee-d536d972373a | -19.09262 | -57.53498 | 2025-10-21 05:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9ac6205d-6f92-31cb-bd80-7750db3f2878 | -17.41249 | -55.04706 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0c49e222-153a-3c64-976a-72ae84869d69 | -17.41161 | -55.05593 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0e28f7d0-f85a-3da4-8861-ab92e99a21ad | -17.68261 | -52.25537 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e931842e-a585-3cd0-97cb-bc066074ebff | -15.8968 | -59.61009 | 2025-10-21 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a1b03154-6d09-3c8d-bb39-5c402ea55ed1 | -18.16065 | -52.98415 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3695ec26-3257-36c7-8d23-7d949f8532ad | -17.43026 | -55.04906 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| a6a386b5-6754-3347-8880-3e80dcec7ed3 | -20.48172 | -54.68456 | 2025-10-21 05:38:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 373d626b-3bdd-3375-a08f-a71c3c8b8907 | -17.42258 | -55.02699 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7a962242-2693-33dd-b473-0b6dc2af67e1 | -17.68353 | -52.26081 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e169b41-f638-3fe8-823a-f0f4d6ef5bb8 | -19.09673 | -57.54527 | 2025-10-21 05:38:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9d982cbd-6d3b-3401-991a-5c40d931ce5a | -18.17018 | -52.97905 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6b554f58-5f9a-3a2d-88ab-62804b3d7731 | -17.443 | -55.04151 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bcb8e020-68d6-35fe-bb09-1be5b14fb764 | -17.40525 | -55.0597 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 44cc2548-79fb-3e5d-bf99-e4e8a95fadd2 | -17.4079 | -55.05231 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5aeeff34-6197-38d6-b441-22a4c133070d | -17.41429 | -55.04853 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 14512b8d-69d6-34c3-96b7-c5a15aebd5a9 | -17.42614 | -55.04983 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 02c4e206-5754-33a6-8d94-98fb36afa991 | -17.68375 | -52.24191 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb9ceb5b-2743-3aed-89e8-f02500ca117f | -18.16342 | -52.97839 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9f6ceb0-e7b7-327b-b9fd-aff29d921162 | -17.43663 | -55.04529 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 3fbc7008-f3b2-3b8a-80fa-82c9615171c9 | -17.43618 | -55.04973 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| c2c6d84c-dc0c-3682-a58f-98e209dcb8bb | -17.41382 | -55.05296 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 48175c72-ac8d-3e70-9b41-0e81bc5837c2 | -17.42389 | -55.05285 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8e0164ac-4faf-30cb-88e3-34610d816d2b | -17.41288 | -55.06184 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 737b15e9-69be-32fd-8102-1d081a02cb5a | -17.42851 | -55.02764 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 014834c0-d9cd-3677-9571-0b434f277643 | -18.17749 | -52.97356 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 57ddf001-8be7-317a-bfdc-1ea4146880fc | -16.52564 | -53.72777 | 2025-10-21 05:38:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72eb5888-e518-3125-9d49-cc4d8cb5aa27 | -17.41879 | -55.06258 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e0518eb1-18ab-3c61-985a-cd0583bf9770 | -20.48215 | -54.67934 | 2025-10-21 05:38:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4afbacc4-6822-3b71-8c2a-d59669a61274 | -17.41708 | -55.06112 | 2025-10-21 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2fa6b2a3-d219-3769-9d90-a034da71bc20 | -17.6765 | -52.26032 | 2025-10-21 05:38:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README25.md)
