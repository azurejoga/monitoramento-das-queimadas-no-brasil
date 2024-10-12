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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e079552b-5159-3dc0-b00b-746573d917a6 | -9.85512 | -60.28171 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1a551c17-8511-382e-9fcc-0a17b2bf4a18 | -9.85467 | -60.32896 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68dbc15a-812f-3e9a-b2b3-36faf315493a | -9.85457 | -60.28527 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ccadea34-1ffb-38a8-b83d-d1c58abcc57e | -9.85402 | -60.28884 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df215381-331d-395f-9506-8ca6c0b45d64 | -9.85188 | -60.32489 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5f73049-0376-3937-b46f-3787e0a7bce3 | -9.85177 | -60.28119 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be997ce5-6257-3bd1-860e-d7c32ac17d16 | -9.85122 | -60.28474 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bdca858-3dc2-3eaf-812a-6f64d5b58635 | -9.85067 | -60.2883 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47285a07-c01f-3ee7-8964-5b1a014ad003 | -9.84842 | -60.28065 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 51182979-62f6-3694-8320-eb99ad2375a3 | -9.84788 | -60.28422 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54666981-b152-35ac-8163-54b374e4bd1f | -9.84733 | -60.28778 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2702abba-f1c6-3ee5-a8e4-9661b7de4aaa | -9.84727 | -60.2659 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b2dce1fd-faba-3819-957d-9c485f5ac1b5 | -9.84508 | -60.28013 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3916c133-dcac-3147-9ade-f0f82afa6afe | -9.84453 | -60.28369 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52f43180-69af-3af0-b7c7-776348c54e0d | -9.84398 | -60.28725 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a9afa5c5-9cde-3b2a-8b75-f2f51e7cba7e | -9.84392 | -60.26537 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3eb33224-1918-3a0b-a4bd-d34cf921f99f | -9.84337 | -60.26893 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bdf11022-8a7e-3534-b5ed-84ed672bb6b6 | -9.84228 | -60.27604 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69bb6568-9d98-3948-88cb-149a55e46cef | -9.84173 | -60.2796 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f401f0b8-64f6-3af6-b389-3bec22bda2c9 | -9.84118 | -60.28316 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26f6eea2-fd20-34d5-a442-be42045e0ba5 | -9.84063 | -60.28672 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b30c6a3a-acee-34df-8587-b02c9e7abf65 | -9.81093 | -60.43462 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 14ae7978-6014-3bde-a0c2-30fc83c88bc4 | -9.80206 | -60.44771 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 244a0726-0a22-3618-b950-43499a5c0264 | -9.80151 | -60.45126 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46e8a2cb-1995-37f1-89bb-66f9bba4a465 | -9.75523 | -60.42598 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 579d8687-1382-3522-8f88-61d7a34e5b06 | -9.75468 | -60.42952 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd47c798-7c67-3335-96f1-b0f383a64dcf | -9.75189 | -60.42546 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 963c39fc-c7f3-3f44-9a0d-9efc1de1492d | -9.75134 | -60.42899 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b448e5d3-d698-3aba-8113-bcd3026a19fe | -9.75079 | -60.43253 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9fdddba-9407-3e77-aa95-54051b027c6e | -9.7491 | -60.4214 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aeb28996-cf3c-305c-8d90-fe67cc2d001d | -9.98846 | -59.86831 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a77a416-ec6b-32d0-9dbe-1baf8bc4c2b7 | -9.98791 | -59.87194 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a77ae0fd-a175-318e-a80b-c7ecf742b0c5 | -9.98453 | -59.87141 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb6bd4f5-2738-3959-9df3-669e609b12b6 | -9.94946 | -59.80321 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8c3441c-863e-30ee-a4d3-580126027aa4 | -9.94718 | -59.79545 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9063c51b-355f-3186-9746-fbce0857cd54 | -9.94662 | -59.79909 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37762c62-cd1d-3aa2-9b94-2282270663a2 | -9.94607 | -59.8027 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c144ef0-067b-31fb-b491-5c691e0e8102 | -9.94324 | -59.79855 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08420bae-b2e9-3d5e-b902-1cefb96da751 | -9.94269 | -59.80216 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9fd8d1c-deee-3508-8c2b-eda6627cf434 | -9.93986 | -59.79797 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7648c285-5282-3c2e-a6d3-3cc3348986a9 | -9.93879 | -59.82757 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e3a9eb5-dfd4-376a-a9da-9d35d31fef41 | -9.93485 | -59.83067 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee397e53-68b1-3626-a6e0-9eab850989ab | -9.93224 | -59.93776 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 82501f8d-1f1d-3a05-b8b9-afc403c1e19e | -9.92924 | -59.84472 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4553463c-4c15-3de2-8d9f-270ced06d725 | -9.92712 | -59.90367 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| edd91ea9-64a1-362f-be68-29931dadf55d | -9.92586 | -59.84418 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f08f8101-133a-3d8a-b0d8-4fffe1d6ad7d | -9.92549 | -59.93671 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50f86f10-aa28-3e38-baf0-7827e0690293 | -9.92415 | -59.83274 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06562a18-eb2c-3ec0-ba53-d3d04d168338 | -9.92359 | -59.8364 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87a16559-c735-355f-b92f-a5bc1a8dfbef | -9.92263 | -59.91037 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d728af90-aed3-318b-a195-eb9be38a4c97 | -9.91926 | -59.90984 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9bd5a64-b0d4-3f87-a6a0-7c7f8c23a582 | -9.86847 | -59.82815 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0baf299-9943-31c3-b29f-846ac0da5f5d | -9.86791 | -59.83179 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6c8c23d-1da3-3f14-8aa1-b70d876e3305 | -9.86735 | -59.83542 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17155b21-9cb0-381f-8c31-a8e400243dc3 | -9.86452 | -59.83128 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08927d08-6f93-3df7-92d6-bf128ba1acce | -9.8617 | -59.82711 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0547cd04-99c1-3440-912a-1508e6fbdba1 | -9.86114 | -59.83076 | 2024-10-12 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39861093-4925-393e-9870-19c0b613fea9 | -10.43307 | -61.00223 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ca39fb9-98ff-3469-937f-54935c7ed602 | -10.43252 | -61.00573 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc4f5164-1012-306e-88f5-edbd67c9dc13 | -10.43249 | -60.98413 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4695df5-a3d9-3b0b-ac8a-e83d2edee93c | -10.43197 | -61.00925 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5e23b31d-35b2-318e-8bfb-15b2a762b7b2 | -10.42919 | -61.00521 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17ce5c1e-5ccf-3e5b-a51f-2fecce212807 | -10.42917 | -60.9836 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6f5d0d0-8751-3523-86be-147dd77c57fb | -10.42864 | -61.00872 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 38c244de-d67a-3e7c-a816-683eb1a3e4bc | -10.42862 | -60.98711 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29ed5760-a410-3547-9663-e60e540d8a2d | -10.42587 | -61.00468 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b466787-008b-314f-a962-98ddc043360b | -10.42532 | -61.00819 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c53d3aed-a1e6-3945-bc64-26d25698d7cf | -10.42254 | -61.00415 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8381107-fc00-30fb-9ca6-56088d86fb55 | -10.42199 | -61.00765 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cfb7418-95c4-33a4-a85c-d47ad07955e3 | -10.42032 | -60.99658 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58615be5-100b-3a57-b1b5-e0f8ec5eac16 | -10.41977 | -61.0001 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b4c10be-91ab-3207-b1c7-cf48233ba8bb | -10.41809 | -60.98902 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea5d3790-a65d-39c5-ad22-0672fa48ae9e | -10.41754 | -60.99253 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 38051a84-985b-37d8-8d0f-ba2a59fb52fd | -10.41702 | -61.01765 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8753051d-b04e-31e2-a0d8-5ca411047a34 | -10.41699 | -60.99606 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b57c47ff-8b7d-32ca-bfe2-2d054f405966 | -10.38009 | -60.6908 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec9c49fc-cd1a-38b6-bf01-9182b09e74ec | -10.37734 | -60.70845 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6be97efd-23ff-3e17-914d-af1e0dd903e6 | -10.37675 | -60.69028 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 583a9bd5-4f8d-30e7-980b-bf0751f6d6fa | -10.3762 | -60.69381 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c0208fea-67ce-3864-ad38-1a7b39fdc363 | -10.37456 | -60.70438 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4257cf5d-3f59-3e16-aae4-db6c1819e462 | -10.37401 | -60.70791 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd1a4ad-1e0a-32c6-ab03-7c5983f7291c | -10.28729 | -60.95743 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23a75cbf-e7d4-3cf7-b26f-058412b64f86 | -10.1923 | -60.89583 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69051237-c7a3-3085-b219-38b9a27e5b91 | -10.19175 | -60.89935 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb4a5279-0e5c-3ba9-b483-eeda5e13294e | -10.1912 | -60.90287 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0f013f12-8621-3c87-b3b2-e96e402adbe0 | -10.18952 | -60.89178 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a08761c-b0b4-30cd-b476-e491bcdda800 | -10.18897 | -60.8953 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88583bc3-f55a-3875-b0e6-8f2e0cc2f932 | -10.18842 | -60.89883 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3d13167-b6a8-3154-8cc4-1373ab9c62a9 | -10.18787 | -60.90234 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 598d04d0-5ee9-3c8b-810c-abd2e1510df0 | -10.18619 | -60.89125 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 73bd7f74-a27b-3e2a-b97a-943965c0b35d | -10.18564 | -60.89478 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| edbbbbb6-db77-39e5-b453-35d1a3450e83 | -10.18454 | -60.90181 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d9ca38a-cb74-380f-bc20-44fb276def10 | -10.184 | -60.90532 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 036b0c35-beba-3b89-8ec8-6c5e71607d4a | -10.18287 | -60.89071 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cd64180-2b04-37be-83f8-1f9453b715ae | -10.18067 | -60.90478 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aca3c84-2dd8-3147-beda-066e87708743 | -10.17954 | -60.89017 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccabc040-602f-32d4-a383-8f55ac538b17 | -10.17899 | -60.8937 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69981c92-e7d6-3dfe-ac22-db8ec59c1429 | -10.17734 | -60.90424 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 589f3420-4c5d-3ecc-a2cd-549e47fd3dc4 | -10.17566 | -60.89317 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd415bf8-05cb-3b36-9b96-d7b7153a4cf8 | -10.17234 | -60.89262 | 2024-10-12 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README128.md)
