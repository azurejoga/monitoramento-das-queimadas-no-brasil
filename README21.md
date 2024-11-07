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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a34508e-43b5-3b08-8f10-baf2fbf6ec0b | -5.0342 | -46.83 | 2024-11-07 03:00:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 23e4ad3e-498b-3d7c-8f04-ddd4ab45bd19 | -2.8352 | -48.6648 | 2024-11-07 03:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| fc9f5586-4856-30b6-b3bd-c73b9ff53db9 | -1.1466 | -53.7177 | 2024-11-07 03:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 06d56472-f29a-34b4-9fe4-6fa31f10a928 | -3.1617 | -50.2038 | 2024-11-07 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 1a5425b5-f48a-331e-8c75-b62f6c32d2fb | -3.5864 | -50.2317 | 2024-11-07 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 7da5058f-c151-37fb-b496-e260bfa75bc9 | -2.6228 | -51.3038 | 2024-11-07 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 31025ba8-0700-38dd-89bc-22ae310b0954 | -4.5218 | -42.8843 | 2024-11-07 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 4ca72a9c-8a17-300f-912c-9cbac2d58cdb | -2.82 | -52.9409 | 2024-11-07 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 9c7e61d4-088f-3041-a3dd-dc054e897c0e | -3.7033 | -48.9986 | 2024-11-07 03:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| d3197e62-abe3-3f4e-94f6-d10e53386398 | -5.9975 | -45.3607 | 2024-11-07 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 7850e9ba-dbdb-3d6c-8b94-4cb7e9ffaa13 | -2.8536 | -48.6856 | 2024-11-07 03:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 98256d4e-d8a5-3173-a95c-19486ce57ce6 | -3.6602 | -50.2501 | 2024-11-07 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7a203f1a-aa99-31d6-98e1-78a28951f1d9 | -5.9788 | -45.3621 | 2024-11-07 03:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 155.9 |
| f828c0c7-804b-33dd-aae5-17d242d44f90 | -4.5033 | -42.862 | 2024-11-07 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| e5da8883-7ced-3b7a-aa0e-f43ed0d5c950 | -4.522 | -42.8608 | 2024-11-07 03:00:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 905d899d-7cd0-3f26-90af-cb146c80f6ca | -3.0396 | -53.2805 | 2024-11-07 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 391c4f6d-cfeb-3d22-8cb9-a75534ca255c | -3.9669 | -48.1716 | 2024-11-07 03:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| feb187ff-dd8f-3c15-a877-cd35c1b1f353 | -1.1831 | -53.8985 | 2024-11-07 03:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 05f61f64-79b9-3230-aa4f-f3a894564ed3 | -3.0207 | -53.443 | 2024-11-07 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| b3155422-9250-36fe-8f83-80f475073030 | -2.6228 | -51.3038 | 2024-11-07 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 4d2ec061-9717-3af3-8c2c-a5dca7eea7ba | -2.8351 | -48.6862 | 2024-11-07 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 88621fae-1896-3db4-9cbb-1cb25a331fcd | -2.82 | -52.9613 | 2024-11-07 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| a9b78ac0-e5a6-3075-80f5-e725855194ed | -3.5864 | -50.2317 | 2024-11-07 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| b645037a-a1b6-3254-8aaf-5edd583de9c2 | -2.8352 | -48.6648 | 2024-11-07 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 592107e3-cf14-3c6c-bcc4-b509b4b37a12 | -2.8537 | -48.6642 | 2024-11-07 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| f7a8ef87-b8c4-3e27-80ce-731b104f498d | -2.8536 | -48.6856 | 2024-11-07 03:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 59c796b1-9d99-3a0c-b5ce-977e94bdd1a5 | -1.1466 | -53.7177 | 2024-11-07 03:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 976c9380-0fcb-3d4a-82e3-970aa3c8c6a3 | -3.7218 | -48.9979 | 2024-11-07 03:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 4e6dba22-b876-3ee4-843b-fd6f9f933662 | -5.9975 | -45.3607 | 2024-11-07 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| d65bf0ec-938c-38f7-8a6f-9ba285747535 | -3.0396 | -53.2805 | 2024-11-07 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 39897908-b921-3b9e-99a5-0254a583e6f7 | -3.6602 | -50.2501 | 2024-11-07 03:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 4a974e80-a15f-34ac-ad86-13de23252e71 | -3.7033 | -48.9986 | 2024-11-07 03:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| d62d9096-df17-3734-9eab-f57f9b52abc9 | -3.1617 | -50.2038 | 2024-11-07 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| a77fc20c-60da-31c2-b3ee-010ff892e94e | -3.0397 | -53.2603 | 2024-11-07 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| d91bb8c5-767a-3699-96c9-8fd897c514d3 | -5.9788 | -45.3621 | 2024-11-07 03:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 171.3 |
| ed12e186-c2a0-3c2e-ad4b-c621bdbd6ce9 | -2.82 | -52.9409 | 2024-11-07 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| ab3d222b-17e1-3c43-b432-05ddd3c5d7ee | -2.82 | -52.9613 | 2024-11-07 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 2bfdfc2d-b5d9-3459-a088-a8ea029e9a8d | -5.0342 | -46.83 | 2024-11-07 03:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 1c9d0d87-c203-37ce-9e57-23e8560cbd6f | -2.82 | -52.9409 | 2024-11-07 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9be0380c-f2ac-38f5-ac8b-8ec1dadafe98 | -5.034 | -46.8521 | 2024-11-07 03:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 3c05ea78-e6c7-3398-83c0-a45fdde7ea69 | -3.0396 | -53.2805 | 2024-11-07 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| bafc647b-1eda-37cb-b0a7-72a189bfbff1 | -3.7218 | -48.9979 | 2024-11-07 03:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 656d13f6-15bb-33cb-9f49-b1c0fac25c0c | -2.8351 | -48.6862 | 2024-11-07 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| f680b8e9-a1c0-31f6-b49d-0264550601f9 | -2.8536 | -48.6856 | 2024-11-07 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 82900090-96d6-3a6e-918c-9015baef02a6 | -3.5864 | -50.2317 | 2024-11-07 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 6725f8ce-a264-3dae-86ac-1d50be029889 | -3.0397 | -53.2603 | 2024-11-07 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 78c967b7-d639-37a9-9a70-92eed0d1bbe5 | -3.1617 | -50.2038 | 2024-11-07 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 9c471b30-0f58-3b85-b3f7-36fa886c3d37 | -5.9788 | -45.3621 | 2024-11-07 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| e64127a7-a9b3-35cc-b524-e1d3109d6e65 | -5.9786 | -45.3847 | 2024-11-07 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 28bbf1b8-e4fb-3531-bb11-4c5a1045eddd | -2.8537 | -48.6642 | 2024-11-07 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 119a00fa-bfd5-3958-bdd2-d71447d96007 | -3.6602 | -50.2501 | 2024-11-07 03:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 0f8aa982-92a8-3f54-a69a-13ad95c66aa7 | -2.8352 | -48.6648 | 2024-11-07 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| facddd7c-bfea-381b-b104-ad2101e17cf5 | -2.6228 | -51.3038 | 2024-11-07 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| a7b9b49c-9007-3fa8-b73a-8893fdb50462 | -5.9975 | -45.3607 | 2024-11-07 03:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| f50bf7e2-18ac-379f-a89d-bd9401f11106 | -3.7033 | -48.9986 | 2024-11-07 03:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| bcf3a5f9-43fc-3a32-ae4b-636ebbc30148 | -3.0207 | -53.443 | 2024-11-07 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| a398f5c5-1c88-3b98-9ac0-afea3c59168c | -6.11121 | -43.97018 | 2024-11-07 03:29:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 46218b02-efb9-3d40-8814-137fe53d2e75 | -4.51529 | -42.87366 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 87d107e2-3b0b-35e1-b094-5838669887c1 | -5.1962 | -38.02381 | 2024-11-07 03:29:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e293968f-1f9a-3f5e-a0d5-9d46633d8aa5 | -5.2289 | -44.91849 | 2024-11-07 03:29:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 315335cf-cc62-3cae-94f3-73fb754beca8 | -5.58895 | -45.20945 | 2024-11-07 03:29:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| fde4bcdb-31ca-349c-96a3-fbe6ee8292c9 | -5.44563 | -43.58464 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| e5c8842f-bf26-3091-80a6-7bae3aaff9df | -5.62439 | -43.95093 | 2024-11-07 03:29:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 585bbca8-2f44-39e4-803e-f88586e15341 | -5.44954 | -43.58506 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 3cc1d18a-99de-35cf-aa46-5e04dd460a5a | -4.50841 | -42.87724 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3fad64a-6c80-3978-8365-0e6afb4b367f | -5.93234 | -43.77522 | 2024-11-07 03:29:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0548100-fca4-32e7-9d2b-7ebdda0fba0e | -5.55569 | -43.69908 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bec107b-df35-3bf9-9dd2-34f8aecca762 | -6.89477 | -40.03805 | 2024-11-07 03:29:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 382b7cb1-b982-3fa6-87e8-7edb0ebef380 | -4.51608 | -42.86917 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ecdbe08-09af-394f-b1fa-3165b677a2d9 | -5.58868 | -45.20915 | 2024-11-07 03:29:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2da7906a-8358-3b14-8ed1-d37eca849747 | -4.51079 | -42.86363 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 01404927-5309-3a84-b216-16d0fc8c93ff | -5.19548 | -38.02058 | 2024-11-07 03:29:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 70efc965-d7ea-3245-8b2f-0ee02bd5efed | -6.10485 | -43.96921 | 2024-11-07 03:29:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e9ee9b6a-a410-3c20-a09d-0d7dbdd30e4f | -5.93556 | -43.7737 | 2024-11-07 03:29:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d33c150f-4930-39e9-8a02-e1b0d8c4f4cc | -6.85334 | -38.89301 | 2024-11-07 03:29:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| bf5b89c8-0fb2-3aef-bf80-8e27d500818d | -5.11261 | -43.9651 | 2024-11-07 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18c29987-f51a-36c1-ba80-a721c81a6fad | -4.86048 | -42.95562 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5d8d9158-b134-3f57-b14c-61c468fb3edf | -4.85968 | -42.96025 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae2342b2-bdf3-3709-9ddf-1ec751f4e47d | -6.43994 | -37.70444 | 2024-11-07 03:29:00 | NOAA-21 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f615906-fcb7-3f10-a0ec-6198e68798f5 | -6.69508 | -37.47161 | 2024-11-07 03:29:00 | NOAA-21 | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 949cf835-198b-308c-a24e-6b64b48eaa4b | -6.56991 | -35.14603 | 2024-11-07 03:29:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 467fd812-69c7-30d8-ac9d-e8f452448a8a | -6.44193 | -37.70148 | 2024-11-07 03:29:00 | NOAA-21 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 20545726-f336-38bd-98b1-18e7302e2b37 | -5.61799 | -43.9499 | 2024-11-07 03:29:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 909d3c1f-3507-359f-a52a-dea9c66185e7 | -6.32706 | -35.10571 | 2024-11-07 03:29:00 | NOAA-21 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2b395e2c-e6b3-3e09-a4e9-a6671f46ef92 | -5.19691 | -38.01962 | 2024-11-07 03:29:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f71005cc-71ad-39be-a856-ce0c5df03cae | -5.56107 | -43.70528 | 2024-11-07 03:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e202b164-5616-323c-a143-6f4979b77c53 | -6.44129 | -37.70527 | 2024-11-07 03:29:00 | NOAA-21 | RIACHO DOS CAVALOS | PARAÍBA | Brasil | 2512804 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f925317b-d1be-31ae-b645-2bd6139c9d9a | -5.93956 | -43.77119 | 2024-11-07 03:29:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbc773da-1047-3446-b3ca-5ed4e504fa52 | -6.32948 | -35.10504 | 2024-11-07 03:29:00 | NOAA-21 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 2145b892-ea9f-350a-84d0-c8a4af3f6715 | -5.27214 | -44.88304 | 2024-11-07 03:29:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d0f7c8d-6cae-341b-8a76-f060ad9d072a | -5.11356 | -43.95974 | 2024-11-07 03:29:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a88629a2-3a48-38a4-b80f-4121c7cba68e | -4.50999 | -42.86818 | 2024-11-07 03:29:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2bf8a3e6-e7d8-3421-88f6-7b7e252cef74 | -5.27881 | -44.88482 | 2024-11-07 03:29:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bd830e6e-aef6-3a96-af64-452d60ad1d6f | -5.94188 | -43.7746 | 2024-11-07 03:29:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 384ba894-15af-300a-9a0b-5574dec11c9e | -7.04544 | -35.21492 | 2024-11-07 03:29:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4aac5cec-3e7a-3ae8-ac42-5ace6278894e | -5.61706 | -43.95505 | 2024-11-07 03:29:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 9026df4a-75bc-32f9-bcb5-d087a5d609ef | -7.47596 | -34.84372 | 2024-11-07 03:29:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 19274757-cdda-3f01-9c93-6a215e74d835 | -6.33015 | -35.10095 | 2024-11-07 03:29:00 | NOAA-21 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f0fe5961-a52c-3ba8-ace7-ae29c76194f6 | -6.32881 | -35.10912 | 2024-11-07 03:29:00 | NOAA-21 | VILA FLOR | RIO GRANDE DO NORTE | Brasil | 2415008 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 33c3259c-26ac-3897-b1b7-ab968462702b | -7.47917 | -35.20245 | 2024-11-07 03:29:00 | NOAA-21 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |


[Clique aqui para ver as próximas entradas](README22.md)
