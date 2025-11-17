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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1ece0c96-2b7e-3cbb-8b97-cf8608cf23a5 | -4.95039 | -37.40482 | 2025-11-17 03:49:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 005c736b-61e2-33c8-81f1-ef391f125a26 | -11.83669 | -49.21618 | 2025-11-17 03:49:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dcad100a-d34c-3b8b-9d4f-157540ba0d27 | -4.41007 | -43.02951 | 2025-11-17 03:49:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12e93005-9ff8-3869-aef1-d362efc1f1cc | -6.6875 | -42.0296 | 2025-11-17 03:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 8611296c-e189-3a27-9ae2-7b5d462d76c9 | -3.2344 | -50.4952 | 2025-11-17 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 85f6e4d0-c649-32d4-9cb8-ba0d1ca1cc2d | -10.8597 | -46.739 | 2025-11-17 03:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 06fc3d82-0b2d-39dd-a581-8a1db4d67129 | -2.5053 | -47.812 | 2025-11-17 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 1a44a146-c922-3d00-9060-e505311dd06b | -2.5238 | -47.8115 | 2025-11-17 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 82bb8135-e993-393d-ba77-610d99836a1c | -5.0401 | -43.5973 | 2025-11-17 03:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 41482acb-5e09-36ae-a53b-387f3b4b315b | -22.10887 | -48.26903 | 2025-11-17 03:51:00 | NOAA-20 | DOURADO | SÃO PAULO | Brasil | 3514304 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f45692c-a55f-3080-a2dd-d29498c9ba0a | -19.70283 | -47.01603 | 2025-11-17 03:51:00 | NOAA-20 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d56199aa-b24f-3397-85f8-36b9b25a5dec | -17.28522 | -47.1389 | 2025-11-17 03:51:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee439df5-ed6b-3df9-b049-cdac64a955a5 | -17.66387 | -46.68065 | 2025-11-17 03:51:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fd16d2b-9ebb-3c0d-aeeb-25bc7377da03 | -17.32907 | -46.55243 | 2025-11-17 03:51:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77d2001b-47f6-37b1-9969-18f7a81c16df | -3.2344 | -50.4952 | 2025-11-17 04:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| e161bde2-6b8b-3d27-a4a2-72a95d3fae53 | -6.6875 | -42.0296 | 2025-11-17 04:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 90.2 |
| adde24a8-6414-300e-9049-02c2328386c2 | -2.5053 | -47.812 | 2025-11-17 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b5085e61-c438-37c4-8007-c4db77da03fa | -6.6875 | -42.0296 | 2025-11-17 04:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 738992c9-fbef-39c1-8271-bbe21a8ea5b2 | -3.2344 | -50.4952 | 2025-11-17 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| dc53e95f-f748-3aa1-85e1-519e598cda65 | -10.8407 | -46.7414 | 2025-11-17 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 62421f19-df7c-38a4-8961-9afdde3e83fb | -10.8597 | -46.739 | 2025-11-17 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| df3e5897-27fa-34a2-9e5d-ca349966db63 | -6.6875 | -42.0296 | 2025-11-17 04:20:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 1b396650-e6bb-344e-9432-7941702fc3d3 | -6.6875 | -42.0296 | 2025-11-17 04:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 74.1 |
| 9932f7d9-bd91-3d99-880f-ffd879725e38 | -3.2344 | -50.4952 | 2025-11-17 04:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| ee182d85-9f4d-33bd-b148-288d2fe3e6ce | -11.8184 | -45.3138 | 2025-11-17 04:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 7b9b7db7-df51-3d9e-9189-6124ea035f83 | -11.8188 | -45.2907 | 2025-11-17 04:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| d7cd59e1-ec9d-3f4e-94c0-a47b5a48f293 | 0.14596 | -49.82473 | 2025-11-17 04:36:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3ca24d5-60b6-3013-8a9c-30d2a0c4308d | 3.78048 | -51.81218 | 2025-11-17 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46e15b32-5957-3ab7-a776-ae6681e060d4 | 3.77652 | -51.81274 | 2025-11-17 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdd63871-a971-367c-b7c9-fe9c626bf2a3 | 0.73518 | -52.05749 | 2025-11-17 04:36:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edd86c48-253c-3955-9f2d-408b2e15f308 | 1.64324 | -55.96811 | 2025-11-17 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cf694d7-adbb-3ccb-9151-c0239e8e1cd8 | 0.56153 | -50.92737 | 2025-11-17 04:36:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 48d3c294-fa6e-3aa4-8515-2a7b05ebb4a3 | 1.72615 | -51.06554 | 2025-11-17 04:36:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fd3f2ff-1a53-3fd4-8255-1bd7636db1c2 | 1.64976 | -55.94273 | 2025-11-17 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 655ebd60-c128-3030-89c4-fa8feb4fe36e | 3.77986 | -51.81436 | 2025-11-17 04:36:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aac321f3-933b-36f7-96bc-51529399a5fb | 0.24169 | -51.01563 | 2025-11-17 04:36:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bf5c284-f7a7-355b-b5b7-055e3d8cfdc9 | 0.23809 | -51.01618 | 2025-11-17 04:36:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce5f8d6c-b11f-331d-a210-23b3fd27c352 | 1.64279 | -55.96511 | 2025-11-17 04:36:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 51152e9d-0738-35f3-b5f9-9f569cb10dce | 0.72856 | -50.72276 | 2025-11-17 04:36:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 19505785-8e38-3a11-a1b1-903a58d1c677 | 0.23448 | -51.01674 | 2025-11-17 04:36:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8390e033-e2e3-3c92-bbd6-a3c12b944972 | -6.02652 | -49.84216 | 2025-11-17 04:38:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0f2e106-f3a9-3b3c-9899-aa9639722f94 | -5.00109 | -44.36041 | 2025-11-17 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a6fba61d-ceed-3091-9a76-d444d0557c37 | -7.16282 | -41.76361 | 2025-11-17 04:38:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ea5b3e15-8c04-3bcc-b231-0a8ce8fe2265 | -3.58235 | -50.71946 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ee97c12-f8f4-3f5e-8c61-c1850eea9b55 | -4.66025 | -46.74406 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 0e2d7c94-d8cf-3cec-8cf0-6a1cd1fb28f1 | -5.3609 | -44.8624 | 2025-11-17 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5faf7308-fe72-324e-8b16-8705125f9bac | -6.04628 | -49.13078 | 2025-11-17 04:38:00 | NOAA-21 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79bb4b55-6ab0-37bc-ab44-8e415eb55c37 | -2.91148 | -54.16187 | 2025-11-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3065c8a4-6730-3020-954f-507e99f9a8d4 | -3.38534 | -50.16838 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf79ae2c-f879-37bd-9f19-5bdbed9e8e20 | -3.12424 | -50.1797 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a596bf1-d09e-30c5-892a-6293b9f1751b | -5.92055 | -44.01816 | 2025-11-17 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68a53ded-2a57-36a4-bbf6-825b7f2cca3b | -3.99017 | -51.09052 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c3a8f62-8798-3bb2-b227-ea987ed502c7 | -6.48232 | -47.19127 | 2025-11-17 04:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 44848378-ace9-3477-ab72-ce0ee8b0572f | -6.67823 | -42.04404 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| d10fe94f-1452-369e-8643-0ed60404c441 | -5.4057 | -44.06649 | 2025-11-17 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b48d27a-0073-30de-8ecb-2fda48c6e85f | -5.40476 | -47.26404 | 2025-11-17 04:38:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06ad3e5f-a01e-370c-964e-cbc871a36c36 | -3.34708 | -44.43026 | 2025-11-17 04:38:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 43298134-db5f-3b31-8dd4-7a33f5f2dd08 | -3.55292 | -46.16553 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ed3110a-4d19-3654-8a74-f01513223585 | -3.18183 | -50.65407 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8472222a-5992-380b-8630-e906f06d6d05 | -6.40044 | -42.28449 | 2025-11-17 04:38:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 3f8db013-5e84-3c5d-b9cc-8f291e92dcd3 | -3.23331 | -50.50646 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83f19a16-c497-34bd-ad47-e4989de1b653 | -5.8412 | -48.8331 | 2025-11-17 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cf2271bb-3070-3bd0-bdc9-e4106d5a8bfb | -2.46632 | -48.26752 | 2025-11-17 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab7dd658-2ca0-3ba0-9a88-ebad7a0b9983 | -4.66141 | -46.73646 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d473fa4-e5aa-3111-978a-56163fe58245 | -7.0578 | -42.23748 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 91492d66-fd84-339f-8069-53c1bd9d6893 | -3.13122 | -50.28833 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e94e736-a5ce-3bcd-b112-10b2bafd3ee8 | -3.24013 | -50.50754 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68440812-cbe5-302d-8a6e-bf7490db58c4 | -5.47906 | -40.96229 | 2025-11-17 04:38:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3bcc687f-c0e2-3f11-ae6c-1a8c26f841dd | -8.32563 | -45.4111 | 2025-11-17 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b0c74b1-621e-3ffd-8c5e-7dc69914bf88 | -4.21484 | -49.13709 | 2025-11-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2e7a16e-8cdc-3cd3-ac60-5d3737479ab3 | -7.70443 | -42.94485 | 2025-11-17 04:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 565bbae0-6c58-3034-a3c6-bdf0e0697cad | -4.5787 | -50.28244 | 2025-11-17 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12a8a4f9-cc31-37ab-80d8-7e0e0b0a1e1d | -3.77423 | -49.96983 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 883aabf4-67b5-3525-af86-9a8e106d67c7 | -2.4337 | -52.11836 | 2025-11-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0566b71b-9a2f-300b-a9fe-94670e96921f | -4.69834 | -46.30358 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7751064d-dab5-3126-a536-6371da3f424b | -4.74496 | -46.39893 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e42164e-1f29-381b-a3fa-c453f56c8b93 | -8.11712 | -43.52724 | 2025-11-17 04:38:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ca81b9e8-9ff7-38e8-92ea-c7b29bf75a3b | -4.75649 | -46.57918 | 2025-11-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1802c8f8-3968-36a3-8a6d-4ca21790ceeb | -8.2834 | -41.43014 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7e1d4e2e-5eba-3079-af74-827ef74057b1 | -6.90038 | -52.19485 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2cc88e84-9d54-3837-9f5a-0431d9c1f85a | -2.24404 | -53.62328 | 2025-11-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6e8f5570-7c35-35c1-bfe6-631cafb73e1b | -3.23164 | -50.49491 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfa6e07b-9500-390f-b228-5f2a90f95894 | -1.9926 | -56.58054 | 2025-11-17 04:38:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7e93fa3-ab58-332f-8696-6dae32579b06 | -8.46526 | -45.13496 | 2025-11-17 04:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f212afb8-4677-3cd0-8613-1503d1d885b0 | -3.23273 | -50.51014 | 2025-11-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10cda82d-dffb-30b9-bacc-9ce04b6ec783 | -2.52347 | -47.81453 | 2025-11-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ff8c6d3-ee6a-3af3-a27d-4bb69d12704f | -2.46849 | -48.55582 | 2025-11-17 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 108c7974-a7e4-3b26-8669-9ed782c2e2e9 | -4.81936 | -49.94332 | 2025-11-17 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 968709e0-ba7e-3693-8d29-675c110c90d2 | -5.78536 | -48.57972 | 2025-11-17 04:38:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00111141-c08d-3c5e-a0f3-5a351b2ac169 | -3.80856 | -51.34311 | 2025-11-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e655ee6-9761-3fae-9b06-e2edb2cb2342 | -6.62209 | -41.46593 | 2025-11-17 04:38:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b3a5871a-86aa-35fa-9592-17897fc1d066 | -3.42284 | -50.3555 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ace7f8-0208-3002-9921-8b60b6c7ed67 | -3.35405 | -46.20802 | 2025-11-17 04:38:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6916aba5-0628-3fce-bb70-9d5c34d86f58 | -4.72628 | -46.38027 | 2025-11-17 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 94f628e9-6383-3a00-8540-4e271c6f4e85 | -3.83662 | -49.80974 | 2025-11-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f7cd0a76-2691-35cd-80ea-f8cdb3bc5e61 | -3.55266 | -41.71826 | 2025-11-17 04:38:00 | NOAA-21 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dfbc8884-72f5-3949-b1c0-05af0444e1c8 | -6.68223 | -42.04979 | 2025-11-17 04:38:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 377ce3fc-a74f-384b-9132-c8fb50a482e4 | -3.43539 | -50.11366 | 2025-11-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58851f8d-f44f-3207-9290-26ad16e967c3 | -2.82867 | -46.72528 | 2025-11-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36ec3cd4-74d6-3bd2-8339-4403986a1221 | -5.64203 | -51.32718 | 2025-11-17 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README24.md)
