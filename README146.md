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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57407eb6-f7bf-3a73-885a-9983641a5b5e | -9.9372 | -43.7187 | 2025-10-02 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 126.3 |
| fc035cc7-c8fd-3e88-b384-9e7b0e203233 | -1.44222 | -48.93492 | 2025-10-02 12:34:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 4e01c730-820c-3a96-8267-3fd9c47c47bc | -1.06059 | -48.10797 | 2025-10-02 12:34:00 | TERRA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| ecbdea27-4f0b-3cba-b770-a214a502802b | -1.45289 | -48.92648 | 2025-10-02 12:34:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 2f7e43c5-a5c4-3251-a175-a3730e7ef55f | -1.45429 | -48.91675 | 2025-10-02 12:34:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 33ae9cb8-3816-382d-b777-d5b52f7b3b88 | -0.40272 | -51.80195 | 2025-10-02 12:34:00 | TERRA_M-T | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.7 |
| aad68507-8796-38a5-addc-566a4b7562d0 | 2.12608 | -50.91902 | 2025-10-02 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9714abe2-76a3-3af6-ad47-0bee73c5fe7d | -1.07944 | -48.95851 | 2025-10-02 12:34:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4cee586c-4265-3ad8-acbd-abf0207c7f9c | -0.88417 | -48.77095 | 2025-10-02 12:34:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3eebc360-a6be-3578-afe3-9a7c6e70e3c5 | -3.19597 | -43.45124 | 2025-10-02 12:34:00 | TERRA_M-T | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 1390763d-13b2-3998-8ba0-9e1f9d098dd8 | 2.12736 | -50.92794 | 2025-10-02 12:34:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d99c1f4a-4d3e-392f-9e14-4c1fa1147fb3 | -1.06209 | -48.09737 | 2025-10-02 12:34:00 | TERRA_M-T | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 0a090634-5f62-3f9a-9514-9a31b08eab4d | -1.44083 | -48.94463 | 2025-10-02 12:34:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| b2f4e7e0-fe83-3822-af5a-cdad2b72f110 | -0.87488 | -48.76967 | 2025-10-02 12:34:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 8ae380bd-32c5-3c61-b371-4a898a3bd56d | -2.15041 | -47.70452 | 2025-10-02 12:34:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 49b0128e-10fe-3e77-aba8-6218c165ec03 | -9.31777 | -45.72453 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ad5d6193-c840-35da-a7bd-c4a6aa26921a | -9.9225 | -47.70071 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 300f7cca-b85d-3b1a-a8ec-8566bc3684cf | -8.69694 | -47.69947 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 44.0 |
| 8033d478-6233-398b-ad9d-e7cb3cd926b6 | -9.4191 | -47.3556 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 46dd309d-9038-3671-9ff8-2fa02591fec2 | -8.52584 | -47.25076 | 2025-10-02 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 4e584c7d-59e7-3038-8a91-4f91efaa558f | -9.42438 | -47.56843 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 647.3 |
| d1856520-1027-335b-ada3-a768f95778c5 | -3.29237 | -43.52137 | 2025-10-02 12:36:00 | TERRA_M-T | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| c1b92554-1c1e-3030-b556-4934030f426d | -9.34423 | -45.92466 | 2025-10-02 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 15b1f376-8f7e-3bc2-95a3-0a5e663df601 | -9.92003 | -43.74057 | 2025-10-02 12:36:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 186.1 |
| b46b2f61-a3cf-3af7-b9e7-0288134f4b9f | -8.67465 | -47.69655 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 1e8555d1-0b00-34ba-acd2-474e1da0a902 | -5.9704 | -44.07761 | 2025-10-02 12:36:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 037946be-314c-3d79-bf18-88442253e91a | -7.89018 | -47.29795 | 2025-10-02 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| e552aa2d-2811-356e-b73e-a9b7c55f4130 | -9.33123 | -45.92286 | 2025-10-02 12:36:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 0b5724c5-fa5f-3d36-bcd9-963012c300ea | -9.9368 | -43.76822 | 2025-10-02 12:36:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 179.5 |
| faabbf27-f438-3ea8-ac1a-ef0d9f05998b | -9.40156 | -47.56567 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 8142beec-a9c7-3eb9-b8f2-33bd375cf620 | -6.60325 | -50.03186 | 2025-10-02 12:36:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e262c21f-3a0a-38a1-aa28-3ba17f5eea58 | -10.02186 | -49.31643 | 2025-10-02 12:36:00 | TERRA_M-T | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e33f897a-e18d-300c-9289-5a023655ec9e | -9.91077 | -47.70803 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f39d96d9-6bb8-3bb5-967d-6f97b0c8e826 | -10.31238 | -48.24312 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| d219e37a-f97d-3016-bb98-9f74d5c365c2 | -9.44571 | -47.93957 | 2025-10-02 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| f3c58fcb-182b-33b9-bce5-29d6b6ead77e | -5.34599 | -43.74532 | 2025-10-02 12:36:00 | TERRA_M-T | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 3fbb7784-01c3-38d5-983b-4912ee7678e3 | -8.88446 | -46.58476 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 2343f22c-1046-3dfd-bb16-3c4ae7ef845e | -7.74262 | -46.2117 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 211ed860-e441-3284-b194-c7cba47b624c | -2.70883 | -48.83183 | 2025-10-02 12:36:00 | TERRA_M-T | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| caf39bfd-b974-3ad5-8cb0-a47a9d99d898 | -8.20597 | -45.53448 | 2025-10-02 12:36:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| e1786900-7092-3b56-84be-1543cfb64872 | -9.84191 | -48.25254 | 2025-10-02 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d1c83f83-6116-3b78-bcb1-8894a037ea77 | -8.52065 | -47.83093 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 27.2 |
| db9a4721-be6f-3447-866e-89622eb009e8 | -6.22755 | -44.23838 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| bb9fb8d4-5126-3514-ad13-6b209e6aba82 | -7.79456 | -42.51633 | 2025-10-02 12:36:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 144.1 |
| db9bc9d4-cb61-3316-a486-9249f401f35b | -6.69545 | -47.84561 | 2025-10-02 12:36:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ca85b2b0-e589-3879-aef5-d5dde8309890 | -4.70791 | -43.85502 | 2025-10-02 12:36:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| c60a01f3-42ee-3590-8e81-c99503245ac2 | -8.20465 | -46.99073 | 2025-10-02 12:36:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 523d03b9-4121-3c68-8c9d-0c07afc45fde | -8.55429 | -44.65625 | 2025-10-02 12:36:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| d8f9a329-3944-312a-a129-63469143413c | -10.80407 | -44.23795 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1df09cd8-42e7-368b-8099-9868a3262cbe | -10.10049 | -48.09886 | 2025-10-02 12:36:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 439de565-e130-3164-b5ac-49b073c86db2 | -7.76818 | -42.54344 | 2025-10-02 12:36:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 4b05565b-e2b6-38f2-b52c-89179df67c34 | -7.78473 | -42.54563 | 2025-10-02 12:36:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 317.9 |
| b22de367-cd1a-307f-a52a-bd4ab7cdb553 | -8.71798 | -48.99133 | 2025-10-02 12:36:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 49dd5769-0159-3e9c-99c0-83b6217a5822 | -9.4149 | -47.55189 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 24666834-35a1-3af6-a367-f48a0a237691 | -9.45678 | -47.94102 | 2025-10-02 12:36:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 7c903f28-4475-3275-849c-2de42f5042da | -7.8942 | -47.26696 | 2025-10-02 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 8518754b-fec3-34c9-adaa-a9f1bd970bbd | -7.89223 | -47.28212 | 2025-10-02 12:36:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| d379fe67-6b6f-32e0-bedf-aebc71f166d1 | -8.13734 | -50.25648 | 2025-10-02 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| b83980dd-32ad-3c65-8815-083111c0a532 | -8.92823 | -47.59712 | 2025-10-02 12:36:00 | TERRA_M-T | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| b41518a4-68e7-3081-a21e-75db53e26eb5 | -8.1387 | -50.2466 | 2025-10-02 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| d1556824-c7f9-323c-bb1b-0085dd4710da | -6.23413 | -45.342 | 2025-10-02 12:36:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 881e44ae-aeff-34b3-867b-f4c0ff1de836 | -9.91114 | -47.69915 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| aa0934e2-6952-30ff-836b-098465e59bbf | -9.93219 | -43.77326 | 2025-10-02 12:36:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| d2a940a4-c964-34db-80c8-d96df97289e7 | -4.37947 | -43.01288 | 2025-10-02 12:36:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 04078761-bc13-3ea2-b0ab-4ba8d946ca03 | -9.88298 | -46.93813 | 2025-10-02 12:36:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| d440f1be-a07b-3b8a-941f-bba6e5601c34 | -9.33014 | -45.71022 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 20eb40b5-afbd-3465-97da-c41bb13cb0bd | -9.94423 | -43.70616 | 2025-10-02 12:36:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 94f60d19-4d24-3a4f-97a1-6cffa0360e98 | -6.79193 | -45.57233 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 009c87ae-db81-3a0f-a9b8-24cb5514a9ca | -9.40349 | -47.55046 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 22.8 |
| c6fbe04c-ee05-3d67-9aad-bb199cc42eae | -8.71959 | -48.97949 | 2025-10-02 12:36:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3f76e06e-2472-3a62-b740-4463e1fcc23e | -6.07254 | -44.68885 | 2025-10-02 12:36:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| d1b9c02a-9563-3d18-83e9-38063eed47fc | -2.92482 | -48.30138 | 2025-10-02 12:36:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| c59c89dc-1ac0-3a08-8ac7-982a77065b94 | -10.84615 | -45.39019 | 2025-10-02 12:36:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 58864068-db41-37f5-a9c3-38e8584fd66f | -9.32763 | -45.73142 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 6d9dd5e9-68c8-3091-92db-3cd4a4ed748f | -9.33098 | -45.72624 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 6541dfed-8cdd-37ac-9087-e2eb057949d4 | -9.93566 | -43.74237 | 2025-10-02 12:36:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 35922925-a19d-33fb-9342-a678a6de4ed3 | -9.42634 | -47.55319 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 1bc6c7a7-0642-3201-8ff2-c95e8e1637b1 | -10.22447 | -48.21294 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 2ceb12d5-60c6-3fc1-842a-c1d98f8df301 | -7.57413 | -46.8163 | 2025-10-02 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| a04c4f9c-4a9d-338d-b5c1-e3faf2b469e5 | -2.91585 | -51.96857 | 2025-10-02 12:36:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 90fd57d3-0887-337c-8169-39e040022895 | -8.71501 | -47.13593 | 2025-10-02 12:36:00 | TERRA_M-T | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 391aaad2-e525-374b-ab25-5176fec14d8c | -9.33627 | -48.94565 | 2025-10-02 12:36:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 0944d64e-62ba-3cd9-8764-2db271e4145d | -9.80121 | -47.84657 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 3a9ac7fb-d2e5-3761-a429-1edf7ac1a76f | -9.42241 | -47.58376 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| fac55cc5-449e-3d2c-8122-31868be4537f | -9.9405 | -43.73728 | 2025-10-02 12:36:00 | TERRA_M-T | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 210ebb27-94d1-3411-a512-0c449cf6e945 | -10.30868 | -48.25106 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| d9c08ea7-1c51-392a-b2fe-664e473b5532 | -8.81823 | -46.67785 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ee3cdf08-6f6d-3d1c-bd9b-f537a8c14404 | -9.04632 | -46.65336 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| d9484bee-a1f9-359b-a8f5-47213b633c3e | -9.45654 | -47.5883 | 2025-10-02 12:36:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 065c9986-3072-3325-9caf-fa0b47acdb90 | -9.75296 | -48.31778 | 2025-10-02 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5c443588-04cd-3675-92d2-102195618efd | -8.41556 | -47.74686 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 20a9325b-bf60-3ee6-a8d1-3f509d1670f0 | -11.02962 | -44.63616 | 2025-10-02 12:36:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 4e2dcd76-552f-3ba6-ad68-43a2cd945f29 | -10.31055 | -48.23706 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| f07fcca9-a952-36a0-a29a-69815e6627e7 | -10.2263 | -48.19843 | 2025-10-02 12:36:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 33944de2-a5b7-39ed-b5ea-ee22cb46729f | -7.45995 | -46.99164 | 2025-10-02 12:36:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 86fb20da-35e8-3a7f-88fb-7a89c18efa65 | -8.88068 | -46.5787 | 2025-10-02 12:36:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 1276795a-4322-3105-9355-70f5604b5804 | -9.84012 | -48.26673 | 2025-10-02 12:36:00 | TERRA_M-T | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 38.1 |
| c146b452-9b3e-355d-b391-f491a0c30f61 | -8.50824 | -47.82354 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 2f52f243-cc0c-34b8-88e6-c399292b4faf | -8.26452 | -49.93047 | 2025-10-02 12:36:00 | TERRA_M-T | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cb710cb4-ee75-3932-a0a6-419416d8b3f9 | -8.75586 | -47.3408 | 2025-10-02 12:36:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |


[Clique aqui para ver as próximas entradas](README147.md)
