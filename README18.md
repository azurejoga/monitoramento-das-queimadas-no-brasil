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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35c1a467-d3e6-39bd-8d8f-7af187874665 | -17.293 | -57.5062 | 2024-11-10 02:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| e3d56940-4d12-36d5-a9c7-b6c3b6cc1cb1 | -3.9624 | -49.0096 | 2024-11-10 02:00:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6e7cc34e-ec08-318a-b7e1-9854e5fae879 | -3.23 | -50.26 | 2024-11-10 02:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78b419ff-5de7-3612-a6bd-715127002cf9 | -3.23 | -50.32 | 2024-11-10 02:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7dd491c-316b-3038-ac06-a2a67c3ed987 | -3.14 | -50.42 | 2024-11-10 02:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c51a5898-9099-3b88-b004-a20589efe584 | -2.2095 | -47.733 | 2024-11-10 02:10:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 8d4f5d52-81fe-3d85-b76f-ad7d4b9a72c8 | -3.9671 | -48.1283 | 2024-11-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| d6578830-6b76-355a-b9d0-2dc4e06736a4 | -2.7587 | -49.3497 | 2024-11-10 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e9f704d4-679c-3bd3-a785-720873112649 | -2.7586 | -49.371 | 2024-11-10 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 3bb26930-499e-392d-8d39-dd2c457e7a6f | -3.6003 | -47.3614 | 2024-11-10 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3f2675a3-815e-3661-94fd-9b8fa317fc6c | -1.4926 | -55.431 | 2024-11-10 02:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| e0befd16-0316-3f42-9f78-272b76d54f34 | -17.6066 | -57.551 | 2024-11-10 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 7e434524-b732-325a-82de-94baec8b887b | -3.9625 | -48.9883 | 2024-11-10 02:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 5b0d5adc-7029-36b6-a320-3bcba95e8b0b | -3.1423 | -50.4352 | 2024-11-10 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 256.2 |
| 8d4bffe2-6b97-37ce-9887-cc3a960c72e9 | -3.6004 | -47.3395 | 2024-11-10 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 2ac44792-74f1-3872-b5f6-5d9054ff1904 | -3.1422 | -50.4562 | 2024-11-10 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| e6351e7a-1224-3a22-a3f0-7a7425a75271 | -1.5347 | -52.1899 | 2024-11-10 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| abd5daa4-3aba-36bd-8021-092061d5734a | -3.9668 | -48.1932 | 2024-11-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| a3fcdc0a-22ce-367e-85ad-936ccabe59c3 | -2.9355 | -51.482 | 2024-11-10 02:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9fb614c3-ee36-3326-a951-bef025846d47 | -17.6073 | -57.5099 | 2024-11-10 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 347.6 |
| 3aec6770-5e76-31aa-a78f-d484125d626f | -3.9485 | -48.1508 | 2024-11-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 35d11d89-cabe-380a-a9f4-1ca76ba26add | -3.4198 | -50.3005 | 2024-11-10 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6579e5fa-98a2-33f3-8bfc-ef882978ba7d | -3.5064 | -44.0294 | 2024-11-10 02:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 61f9ec31-eb90-3790-b824-af4b770defc9 | -17.293 | -57.5062 | 2024-11-10 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| 5bb5eb74-c3f1-3018-83c5-98a83cef50a9 | -17.2933 | -57.4857 | 2024-11-10 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 141.5 |
| ff40cbf8-de6f-31a6-bf79-216b3144b619 | -2.0953 | -48.8338 | 2024-11-10 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| bd49cbab-90d0-38f0-8d14-0a05064f9993 | -17.6266 | -57.5281 | 2024-11-10 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 373.1 |
| 7be95bf4-a3c0-374b-8ba9-acb4e1c3e512 | -2.9171 | -51.4825 | 2024-11-10 02:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| c2083781-b23f-3608-85af-3ea155b20491 | -2.7772 | -49.3492 | 2024-11-10 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 88b7560e-8c9e-371b-a22d-7164a19aea47 | -3.9624 | -49.0096 | 2024-11-10 02:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 884167da-b354-306d-8487-124b2512872b | -3.4383 | -50.2999 | 2024-11-10 02:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 2b925d01-4899-321d-8b4a-c14905f2828e | -17.6273 | -57.487 | 2024-11-10 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.7 |
| dd49324d-2001-3d68-8080-a6fe4678a490 | -17.6069 | -57.5304 | 2024-11-10 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 469.2 |
| c01f14f9-7a4d-3cac-9fe5-ecafcab69226 | -3.1238 | -50.4568 | 2024-11-10 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.6 |
| 272ca3e0-fda1-3028-853c-ab173ab2bf45 | -3.9483 | -48.1724 | 2024-11-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 4960a2e2-cc46-33fe-b31c-7c5c872908ad | -3.9669 | -48.1716 | 2024-11-10 02:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.3 |
| aaed69db-5920-31e0-b02e-26febb9aabbf | -3.1095 | -49.4241 | 2024-11-10 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 09bad0c6-2b9e-353b-8157-376d54cadae3 | -3.525 | -44.0286 | 2024-11-10 02:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 09afee9a-3536-3f77-a9fb-70cf92752a25 | -8.3778 | -44.1386 | 2024-11-10 02:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 047d35d5-7fd7-3af8-a336-b9db7ec9e8f1 | -8.3964 | -44.1597 | 2024-11-10 02:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 04f96781-87a9-3ec7-9f05-4625eb005e9d | -8.3967 | -44.1365 | 2024-11-10 02:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 8e287ffa-654b-3995-918c-4a952e86b5c5 | -3.5818 | -47.3621 | 2024-11-10 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| b981b543-f232-38e4-ab0b-3f9758a6e5b8 | -2.8857 | -45.3726 | 2024-11-10 02:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 54d2d8c2-2ab4-3fcf-9369-560a9634ad29 | -17.627 | -57.5075 | 2024-11-10 02:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 372.8 |
| e548989a-9bc2-36b5-ac68-8dcd7e13a742 | -8.4156 | -44.1344 | 2024-11-10 02:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 7d57dcda-5dc6-3f14-920f-653bea62c89c | -3.1239 | -50.4358 | 2024-11-10 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 231.2 |
| 81389c77-7d7e-3799-a4eb-734e1dab5c76 | -1.5347 | -52.2104 | 2024-11-10 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 56bef183-4edc-39d7-ac83-e3b569701eba | -1.5163 | -52.2106 | 2024-11-10 02:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| dd9429af-473a-3436-be6f-267bb8fd3800 | -2.0954 | -48.8125 | 2024-11-10 02:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ebbab1df-e99a-3d5a-8f39-49c7a6d76a70 | -17.313 | -57.4834 | 2024-11-10 02:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.3 |
| 6709f639-cf89-3b4f-91a5-df8e55533cff | -3.5819 | -47.3403 | 2024-11-10 02:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| e786cf54-32f4-3bd8-9ace-7f2ed73dfce3 | -3.9668 | -48.1932 | 2024-11-10 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d4f62b61-d958-3602-98e5-92b722c8bb21 | -3.1422 | -50.4562 | 2024-11-10 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 244.4 |
| d68e96c5-94ac-3b1a-bd65-e7e4d7fffe37 | -8.3964 | -44.1597 | 2024-11-10 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 5c928536-2f86-357d-b79e-7791d9a5437a | -1.5347 | -52.2104 | 2024-11-10 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 9f4bb41e-6f22-3904-b060-08c363ae968c | -2.7772 | -49.3492 | 2024-11-10 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 4b9a46f3-adc2-35b1-a5eb-03161566d8e2 | -2.931 | -52.7753 | 2024-11-10 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 7d6e70e4-af72-3d03-9c12-d88c81108209 | -3.6003 | -47.3614 | 2024-11-10 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 4cd00d19-8f1d-3dd9-b79b-7754e83a3e4f | -2.9355 | -51.482 | 2024-11-10 02:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 00723278-00b4-374d-bc13-caabd99c1182 | -3.967 | -48.15 | 2024-11-10 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 556d276d-71c4-3518-9a67-28338684a354 | -3.5819 | -47.3403 | 2024-11-10 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| cd8475ce-1045-3e56-b08f-dab9ec3aa1cb | -2.9171 | -51.4825 | 2024-11-10 02:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 61445fa2-6ff9-35c1-8815-5d0af7d2349e | -2.2095 | -47.733 | 2024-11-10 02:20:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f2dbfdc1-241a-310a-b45f-3eb9a29fd7a6 | -2.8857 | -45.3726 | 2024-11-10 02:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 43439b9c-b9ca-354c-bff3-1bd55ae669e4 | -3.2427 | -53.0722 | 2024-11-10 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 50135728-657c-3ab2-ae3c-1ffc6d1365f6 | -3.9483 | -48.1724 | 2024-11-10 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| da8e5b90-c341-34a3-a4f8-9e5144f7b33d | -3.525 | -44.0286 | 2024-11-10 02:20:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| c8f7c885-d51d-3565-8646-7ac328f3e4e1 | -3.9669 | -48.1716 | 2024-11-10 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 43c78422-2e30-375e-a76c-68f33db20dc4 | -1.4925 | -55.4508 | 2024-11-10 02:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| bf0ec968-84d3-33ac-b885-11fdb0e903cc | -3.1238 | -50.4568 | 2024-11-10 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 1d4b5382-6a3b-3fd7-8d17-2b940abb92eb | -3.2244 | -53.0524 | 2024-11-10 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 588c231a-ccee-35d8-bd6e-8186aebb177b | -3.2428 | -53.0519 | 2024-11-10 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e514f266-a625-3e93-8652-aa5f5ec5a840 | -3.9485 | -48.1508 | 2024-11-10 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| bbcc230c-8c08-39a7-af81-739561d7cab9 | -5.5795 | -43.9761 | 2024-11-10 02:20:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 7207aa36-e849-314b-bd25-af05d1a2bdbc | -2.9494 | -52.7748 | 2024-11-10 02:20:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 75bdec4f-b453-3925-989e-adee7a2e5a24 | -2.8802 | -51.4835 | 2024-11-10 02:20:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| d60f4ff2-b536-3da0-92f4-9257d785b421 | -2.4183 | -51.9484 | 2024-11-10 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 064af500-ebe1-32e6-ba7e-88cbce6b232a | -2.0953 | -48.8338 | 2024-11-10 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| f231a21c-dcd4-3fc4-b19e-17448dc56886 | 2.8552 | -60.0853 | 2024-11-10 02:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 28.7 |
| ac61e0a8-4ba2-320e-8081-e79eaf9d6945 | -3.2243 | -53.0727 | 2024-11-10 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 2cf741fb-ff1d-37c5-8d8b-013700217cba | -1.4926 | -55.431 | 2024-11-10 02:20:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| be1d7184-a673-32e4-ba51-e26175ab12dc | -3.3202 | -43.9917 | 2024-11-10 02:20:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 622a0dcf-27d2-36e2-89e2-d48bb50db1bb | -3.3389 | -43.9909 | 2024-11-10 02:20:00 | GOES-16 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| ab17af73-29de-3847-a5e7-176a45bd9046 | -3.9671 | -48.1283 | 2024-11-10 02:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| c3b7297c-ca0b-39d2-9fc5-51b959f5bd5d | -8.3778 | -44.1386 | 2024-11-10 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 86.8 |
| f4439c17-0bc5-3e22-8e93-536c283e2cee | -3.1423 | -50.4352 | 2024-11-10 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 350.0 |
| 8a5bab09-f65c-33fd-9e31-38dd4597b2f4 | -3.4383 | -50.2999 | 2024-11-10 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 2c3a012a-6d37-32ac-a447-a0bab8074c49 | -3.1239 | -50.4358 | 2024-11-10 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 305cffa0-09c2-33f5-8759-943ed0322c39 | -2.0954 | -48.8125 | 2024-11-10 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 572571e0-af06-3097-becf-591c9953b2a9 | -17.2933 | -57.4857 | 2024-11-10 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.4 |
| fbf3a9ce-613f-38ac-b600-9a15a3d56cff | -8.4156 | -44.1344 | 2024-11-10 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 57a2d26b-dffb-395c-b05c-6629d5ffd92f | -17.293 | -57.5062 | 2024-11-10 02:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.5 |
| 27f70678-2740-39d8-946c-9c88088ad0a0 | -8.3967 | -44.1365 | 2024-11-10 02:20:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 149.0 |
| ce19e331-da56-3f7c-85a3-6c44618851ae | -3.6004 | -47.3395 | 2024-11-10 02:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 102.1 |
| c7561c56-0505-3817-a3e4-f7fb5a90a0b2 | -3.9624 | -49.0096 | 2024-11-10 02:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| f16fc264-8397-3d7c-ad7b-a5ca59ae4aeb | -2.7587 | -49.3497 | 2024-11-10 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| cbf307cf-6838-3eab-864c-382b33779d8e | -1.5163 | -52.2106 | 2024-11-10 02:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 558cb29f-9eec-313b-9569-6fc13c4a2a6c | -3.9668 | -48.1932 | 2024-11-10 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| d33b37f8-6d1d-3d11-b579-24b16903f778 | -3.1238 | -50.4568 | 2024-11-10 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 157.2 |
| fe83bd7f-b8ea-3e93-9da0-24862b22f9ca | -2.8803 | -51.4628 | 2024-11-10 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |


[Clique aqui para ver as próximas entradas](README19.md)
