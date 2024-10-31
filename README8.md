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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce393158-f742-39bc-990e-d65939c881be | -6.12565 | -43.98039 | 2024-10-31 01:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 827b08bc-9d37-3003-a1fd-81820776d063 | -6.12315 | -43.97543 | 2024-10-31 01:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d2ffd892-dc65-330b-82f3-3823bc6998bf | -4.65817 | -43.13748 | 2024-10-31 01:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 0e289195-b793-3dbb-a0f2-07d0012eb67d | -4.65231 | -43.10147 | 2024-10-31 01:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 8af4fbcb-27aa-3dbf-b95e-9b49792fbf62 | -4.64709 | -43.1076 | 2024-10-31 01:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| c4e7d32a-a89f-33e6-b395-8a4b51881c3a | -4.38953 | -43.80149 | 2024-10-31 01:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 0077362e-4394-3856-90b0-9786a7e0aa71 | -7.90757 | -46.69692 | 2024-10-31 01:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 561e865a-5fd2-3674-9090-0036cec2f75b | -7.90496 | -46.68036 | 2024-10-31 01:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7fd63001-95c1-3435-9179-4763c9a3bfe6 | -7.89863 | -46.688 | 2024-10-31 01:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9d97702f-99a8-337b-95b5-cb90450d76d3 | -7.55279 | -45.54049 | 2024-10-31 01:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 916ab67a-d559-3542-92f6-3ac9613a27cc | -7.55196 | -45.52579 | 2024-10-31 01:11:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| d003685f-972f-3e1f-9dbc-77d949eee396 | -7.18898 | -46.3314 | 2024-10-31 01:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 75aaddfd-a21c-3b5f-b0bd-34f02f0b709c | -7.1766 | -46.33287 | 2024-10-31 01:11:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9d404f08-00a9-34d5-b567-ff4f79ade955 | -6.17239 | -47.30524 | 2024-10-31 01:11:00 | TERRA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| fd065daf-3c10-30a8-b25d-bcc27089ac35 | -5.97994 | -45.38683 | 2024-10-31 01:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0bc405fb-4463-356f-b943-476072ea0c6b | -5.97641 | -45.36431 | 2024-10-31 01:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 2a1f8e88-3840-33f4-9c1d-0101caeb1b72 | -5.96938 | -45.37088 | 2024-10-31 01:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| c47c3feb-d2ae-3ef6-9270-22c8dc13263b | -5.32781 | -45.01549 | 2024-10-31 01:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f4356eea-d349-376a-a542-1c97829d2305 | -4.60556 | -44.3193 | 2024-10-31 01:11:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 7a9f36b0-d51f-3bc8-a397-1a5f811dc086 | -4.60385 | -44.29655 | 2024-10-31 01:11:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 7179467f-2db3-3d5b-8333-5f4111017305 | -4.601 | -44.29034 | 2024-10-31 01:11:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 8d40086d-2f1c-3e70-9a4f-ba51e82615c2 | -3.9774 | -55.38467 | 2024-10-31 01:11:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 81a2f5e5-2001-3dfb-be59-55a53aeb89b8 | -3.90961 | -55.45712 | 2024-10-31 01:11:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2c0745f4-44fc-3c79-860f-6df9e86c5205 | -3.68425 | -52.40934 | 2024-10-31 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 71706629-42e0-382c-b601-d19438443101 | -3.68299 | -52.40041 | 2024-10-31 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 56dbf702-80b6-3630-a22c-efa60ce05589 | -3.35691 | -45.43462 | 2024-10-31 01:11:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 3c98f1d9-dd3f-3df3-a71d-bc314739c402 | -3.34948 | -44.09701 | 2024-10-31 01:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fcff005a-8373-383c-8b18-1ec58aaa6220 | -3.33987 | -44.10385 | 2024-10-31 01:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 59432eb5-e5a5-3ea3-9f14-37a222948de0 | -3.25803 | -51.01942 | 2024-10-31 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b8b2c6a9-98e9-3d82-b50b-3fa9a570d762 | -3.2419 | -48.47785 | 2024-10-31 01:11:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f6b3375e-ea64-30ef-ba7c-489c253f8f1b | -3.21346 | -53.39941 | 2024-10-31 01:11:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dae386ae-44b1-399a-9013-902872bd3332 | -3.19125 | -51.33365 | 2024-10-31 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 002dee02-0188-3ad2-b802-3ef16c5cd5ae | -3.18205 | -51.33501 | 2024-10-31 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 267745f0-9c2f-3ea0-8760-0a25ed18806b | -3.17877 | -50.59608 | 2024-10-31 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 54e10735-27dd-3554-98c7-affba22d0238 | -3.17729 | -50.58567 | 2024-10-31 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 6b1799f4-48c1-3946-8980-b0653a63380a | -3.1624 | -51.12999 | 2024-10-31 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8410098d-e37a-35cc-bbd7-6f978958c915 | -3.15311 | -51.13131 | 2024-10-31 01:11:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| f09b19a3-ecf6-344e-b614-5e0ed158519f | -2.94368 | -53.70792 | 2024-10-31 01:11:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8c59733-acd9-3f1e-9a28-dd28c956051d | -2.93972 | -53.88648 | 2024-10-31 01:11:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3b552c60-cf5b-3f32-b0be-abe2d0488394 | -2.93934 | -52.56083 | 2024-10-31 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 3c0f4225-feeb-34cb-bab5-7ef2116cec2b | -2.91957 | -54.20037 | 2024-10-31 01:11:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6fdf6874-a648-34ef-9d2b-be63bf159129 | -2.91833 | -54.19132 | 2024-10-31 01:11:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 54e1573b-ba16-36c6-8c41-66e61a72f82a | -2.90935 | -53.86352 | 2024-10-31 01:11:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 70decec1-bf14-3da0-a2dd-3b8bbac3db6c | -2.89834 | -51.48152 | 2024-10-31 01:11:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| c690daef-1695-36a3-b5f7-325b4c682fa1 | -1.4441 | -52.27724 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 74a9aa27-5bbf-3cf2-9de5-c42eb9609682 | -1.4428 | -52.26809 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9032cdde-fde9-3ad8-b365-bccae05db716 | -1.43306 | -52.26595 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 604d49e5-e68b-33a8-beec-a7a56f2fcfd5 | -1.42671 | -52.22007 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7666f3db-f0ad-3eaa-8d13-744764d4fddf | -1.42543 | -52.21087 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| b635dc43-2638-337a-a0f9-cb6c1e80f86e | -1.41641 | -52.21215 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 5a9c46db-5f25-3b3f-a440-ec7d7f22e55f | -1.39021 | -53.60801 | 2024-10-31 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 66f79f21-d338-3657-b19a-cf040e53c80c | -1.19774 | -54.14735 | 2024-10-31 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d8697ce3-a642-3b47-9ce7-8d29a207adb1 | -1.16558 | -53.38341 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95a6edfa-823a-3c19-8e7d-2b7fce5d9e65 | -1.15675 | -53.38465 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bd6171c6-6590-320b-9699-43814dfb3d2a | -1.13504 | -54.09896 | 2024-10-31 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6485e240-5440-303a-802d-ea0ee0d1529b | -1.13256 | -54.08126 | 2024-10-31 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a18d2f18-00f1-34d2-9e72-9f40c94d26c6 | -1.09378 | -53.65919 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2e25727c-0056-3107-8724-97d93863f617 | -1.09256 | -53.65042 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd78f4e5-9722-35d7-9267-b5666079a132 | -1.08496 | -53.66043 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dc9d6959-d647-33d7-b2b2-431ea885a6ff | -1.08374 | -53.65166 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| b6867d96-e747-3d29-8615-1766d03fc373 | -1.0648 | -53.66031 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 17b7848e-2c5e-3afa-a8e9-ff3030361346 | -1.03928 | -53.7354 | 2024-10-31 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| da398cff-f6b2-3fbc-8926-6fb2863a9bb4 | -0.88447 | -53.68898 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 9286fd32-4dc3-3546-a435-f5d16e3e63d3 | -0.84511 | -51.95286 | 2024-10-31 01:13:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dbfa4f84-b63f-3c1c-84d4-e6d592d27dc4 | 3.53968 | -51.27353 | 2024-10-31 01:13:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4aa4bdb7-754c-3d0e-b8ab-1e021fea9f6f | 3.5381 | -51.28504 | 2024-10-31 01:13:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1f31e90e-8728-3032-81a9-d796e062a565 | 3.44177 | -51.24232 | 2024-10-31 01:13:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0d57070f-7bd9-3bb7-a682-489dd78b060c | 3.27028 | -60.44799 | 2024-10-31 01:13:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 379ceb02-f55d-319d-befd-5d9aa73c1ac3 | 1.77557 | -50.49479 | 2024-10-31 01:13:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b928ab56-57c4-3cbb-920b-9030c7832186 | -1.43433 | -52.2751 | 2024-10-31 01:13:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 1e6aee26-698e-378c-b602-756d3915826e | 1.66629 | -55.80879 | 2024-10-31 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cb697faa-894f-3653-86b2-d61af1e36a45 | 1.65772 | -55.81091 | 2024-10-31 01:13:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| efdec199-f4c0-3984-972a-7b33503e6cfe | 1.6021 | -55.61122 | 2024-10-31 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8aff2cb9-704f-3439-bdbc-34c8b8ad9ebd | 1.60077 | -55.62056 | 2024-10-31 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 97c83214-2f5a-35ef-a84b-5e74d2422651 | 1.11912 | -50.95664 | 2024-10-31 01:13:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e176f02d-27f8-3810-8c84-517066d8487c | 0.44686 | -50.27893 | 2024-10-31 01:13:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d05b8e17-b5b1-3fac-8ad8-b94dcb5f1dd5 | -1.8475 | -52.1236 | 2024-10-31 01:15:16 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c3fcb21a-5927-3730-9119-7160ebacd88a | -1.9684 | -47.9552 | 2024-10-31 01:15:17 | GOES-16 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 13718a6d-5538-32c4-bae8-81eda80ddd67 | -2.1718 | -47.9506 | 2024-10-31 01:15:18 | GOES-16 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 4fc0d77f-90e9-3adc-a500-0395ec717a4f | -3.1787 | -50.5807 | 2024-10-31 01:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ddd5df06-83a6-303f-ae76-40724eabac9d | -3.2552 | -45.8293 | 2024-10-31 01:15:24 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 15a590fd-2970-3375-a4f3-9dad84a9cc50 | -3.3383 | -44.1058 | 2024-10-31 01:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 89.0 |
| bae84bf2-c85e-3d20-a7c7-56dbb9e2f96d | -3.35 | -45.4447 | 2024-10-31 01:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 9fa731bf-b72b-36cc-a4f3-b8312972c81c | -3.3502 | -45.4223 | 2024-10-31 01:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c8c94818-8968-3a46-a14b-2f4c639cf389 | -3.3569 | -44.105 | 2024-10-31 01:15:25 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 9b16c8da-4ca5-33a3-a1b3-d462a8b11bab | -3.3686 | -45.444 | 2024-10-31 01:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 149.5 |
| 3c1ee084-e5bf-3c4d-9806-782b2861f184 | -3.3688 | -45.4215 | 2024-10-31 01:15:25 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 144.7 |
| 5315c975-a4e0-39cc-b805-5fa7c30a6214 | -4.2749 | -43.4357 | 2024-10-31 01:15:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 841712f3-5346-3e94-9962-fe7389733e37 | -4.6511 | -43.1104 | 2024-10-31 01:15:32 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7233a2cb-f4d5-3cef-b7e2-a47a3962a24c | -5.0464 | -45.1768 | 2024-10-31 01:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| f3341403-64c7-37cd-b162-a44ee30243f2 | -5.0466 | -45.1542 | 2024-10-31 01:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 8e697a37-aad1-3758-af0c-249dda3b9738 | -6.1229 | -43.9578 | 2024-10-31 01:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 0fbc9d3d-4a9e-3d93-a80e-b5af7dc59699 | -6.1416 | -43.9563 | 2024-10-31 01:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 638a8a9c-beca-3db4-b71b-036d1261e631 | -5.9788 | -45.3621 | 2024-10-31 01:15:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| bfc8b015-c100-329d-acb7-96f98c84b09d | -10.0118 | -64.8023 | 2024-10-31 01:16:03 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| ba1c98a0-7c9e-3c2c-97e3-4aaf538cf63d | -12.424 | -43.7274 | 2024-10-31 01:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 4457c0ab-f631-38fc-9e89-2e0c69cd29ac | -12.4433 | -43.7242 | 2024-10-31 01:16:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 64f2fd8b-286b-35f5-9dcd-57704fafb15f | -23.751499 | -51.373299 | 2024-10-31 01:21:40 | METOP-C | RIO BOM | PARANÁ | Brasil | 4122107 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 97392db3-247f-33d5-8b8b-790e02bb4465 | -23.555799 | -51.2034 | 2024-10-31 01:21:43 | METOP-C | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70234884-f13f-3979-9875-28de181192c6 | -24.023001 | -54.0802 | 2024-10-31 01:21:46 | METOP-C | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README9.md)
