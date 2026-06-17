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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e934d582-f604-378c-b9d7-eb04bbea2a09 | -12.0756 | -54.6131 | 2026-06-17 02:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b1f6dec2-2303-331d-9b59-f5d083985d7b | -9.3048 | -45.4581 | 2026-06-17 02:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| bb2d4cf2-30cd-3922-b8d3-6d90876e44e5 | -12.8354 | -44.3657 | 2026-06-17 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| e59a185a-e786-3b52-bec0-e1c70210a866 | -11.5499 | -52.7867 | 2026-06-17 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| af56a1b1-418c-3624-9309-c141bbac8353 | -11.5312 | -52.7678 | 2026-06-17 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.0 |
| b124e4b2-9f5e-31db-831b-d73fc86b87a8 | -9.3234 | -45.4787 | 2026-06-17 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 39341079-e3fa-31ed-a3fa-24b1214015d4 | -9.3423 | -45.4765 | 2026-06-17 02:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 57.8 |
| cb6deceb-3410-372b-ba67-1479b193ddab | -12.0756 | -54.6131 | 2026-06-17 02:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| c2725baa-9167-3eb5-a0a5-de7c1fb7a93e | -12.8548 | -44.3625 | 2026-06-17 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 9de45c5d-70de-3978-b859-d512c81344d0 | -11.5502 | -52.7659 | 2026-06-17 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 486a5520-60be-3f67-8326-d4c14713a7f2 | -12.8548 | -44.3625 | 2026-06-17 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.3 |
| c5e25938-0dfb-33f8-8a1c-0624b6e66d1c | -11.5499 | -52.7867 | 2026-06-17 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 80978b08-f1e1-3007-8bbb-cbd0fd19cdd1 | -11.5502 | -52.7659 | 2026-06-17 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| c007fa0e-7828-3044-8126-ffa3a3e97086 | -9.3423 | -45.4765 | 2026-06-17 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 31beffe2-fb0c-3536-9cad-4bab11927a2a | -12.0756 | -54.6131 | 2026-06-17 02:30:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 926736fe-49be-3085-bdf6-1d2f2c4d49ce | -9.3234 | -45.4787 | 2026-06-17 02:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 62b25a58-6073-3974-8143-90bcf6ccb93a | -12.8543 | -44.386 | 2026-06-17 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 8257a1dc-6ef9-352f-a682-cc611eb22356 | -12.8354 | -44.3657 | 2026-06-17 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 57627d7b-423d-3053-baaf-813dd485e66c | -11.5309 | -52.7887 | 2026-06-17 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 754e25e3-57c5-3c3a-ba44-b1a36075534a | -11.5312 | -52.7678 | 2026-06-17 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4fb81f32-918b-3bf1-915f-72e18bbc7f45 | -12.8543 | -44.386 | 2026-06-17 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| f5f4fef4-959a-355c-a65f-7a17b04afc4b | -11.5309 | -52.7887 | 2026-06-17 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 9b61b690-db49-39a3-aa8e-a3851a1c2683 | -11.5312 | -52.7678 | 2026-06-17 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f9b4cecc-15d3-3cd6-8e71-0f914a3b6e75 | -9.3234 | -45.4787 | 2026-06-17 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 80cb2948-bd62-3e5c-8563-2ddacc68dffe | -12.8354 | -44.3657 | 2026-06-17 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 43f48d04-2b7b-3b46-9bf2-be48b3644852 | -9.3423 | -45.4765 | 2026-06-17 02:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| f1ddea22-6061-3965-8225-6dde3a63a2e1 | -11.5502 | -52.7659 | 2026-06-17 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 309bfbee-c553-3112-91d1-1d563a47b5b5 | -11.5499 | -52.7867 | 2026-06-17 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| f2fd0441-535d-32ce-8fda-283b50aed874 | -12.8548 | -44.3625 | 2026-06-17 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f1207765-db8b-3a12-89ca-aad3fbac1b4c | -12.0756 | -54.6131 | 2026-06-17 02:40:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| b5d46601-3aae-3305-a9a2-fbd276a8c5ed | -9.3234 | -45.4787 | 2026-06-17 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.5 |
| cec82a2a-a5df-3370-8bb2-04c60c5b1c10 | -9.3423 | -45.4765 | 2026-06-17 02:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 2e588c1e-e44b-350e-903b-a54958001880 | -12.8548 | -44.3625 | 2026-06-17 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| eb2bd1c9-a48d-31b4-907d-242d18305f46 | -12.8354 | -44.3657 | 2026-06-17 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 5e585c32-ae08-32a2-8d72-ed5e94f2dfd0 | -12.0756 | -54.6131 | 2026-06-17 02:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| af357f4a-a6c3-34ab-a0c6-afa8bdb06d45 | -11.5502 | -52.7659 | 2026-06-17 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7b81b377-ebd4-33ee-ae4d-1ec67497496e | -11.5499 | -52.7867 | 2026-06-17 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 40.4 |
| a7ff790b-ad6d-3583-9bb8-31d03571eef2 | -12.8354 | -44.3657 | 2026-06-17 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 18023299-af79-39a3-88fd-59d5815f4ebe | -12.8548 | -44.3625 | 2026-06-17 03:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 409e5d69-6473-388f-8a96-7bf2a058ec6c | -9.3423 | -45.4765 | 2026-06-17 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 167fd445-8286-3cfd-ab7a-a4f432e28f4c | -9.3234 | -45.4787 | 2026-06-17 03:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 131.8 |
| a53d2192-33d5-3581-9d1c-9a8b717a8da9 | -9.3234 | -45.4787 | 2026-06-17 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 28d1c7e3-109f-3342-8253-a58680813f30 | -12.8354 | -44.3657 | 2026-06-17 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 8f2bbc1e-941d-329c-9c23-0aae3588833c | -12.8548 | -44.3625 | 2026-06-17 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 6b888938-df44-3aa7-9904-d5d5337a08e1 | -9.3423 | -45.4765 | 2026-06-17 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 273e4340-113a-343e-9cb8-d5e2ae289a0a | -12.8548 | -44.3625 | 2026-06-17 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 59a0661b-9a14-3ef1-9cd6-6df9c4a2a72f | -12.0756 | -54.6131 | 2026-06-17 03:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d8ce904b-bc16-35e6-be15-3723affcb06f | -12.8354 | -44.3657 | 2026-06-17 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 49733168-4f67-3f08-a976-5a0cebd9ad1b | -9.3423 | -45.4765 | 2026-06-17 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 191.2 |
| ce8549a3-8970-3505-8210-fbde0425ad9a | -9.3234 | -45.4787 | 2026-06-17 03:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 410b7aa4-cdac-350d-9780-755357741aa9 | -3.77976 | -41.59472 | 2026-06-17 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 0184be30-ce88-3164-8041-5855577a9381 | -3.77656 | -41.59827 | 2026-06-17 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 960c30a8-1060-32da-a4ed-223c69245df7 | -3.77338 | -41.5938 | 2026-06-17 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 74f38795-b300-3bf0-ae7e-e78e3d8cfb81 | -3.77744 | -41.59304 | 2026-06-17 03:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fc64e2ed-618a-3d9d-91ce-109965609b69 | -10.46525 | -37.43752 | 2026-06-17 03:23:00 | NOAA-21 | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7695cd94-3993-316e-813a-691e54b25bd2 | -6.90254 | -42.84971 | 2026-06-17 03:23:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8a7b5f07-548a-308d-9d21-6043fecaec20 | -7.7238 | -44.16032 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 0b50badc-124a-307a-bed7-c5ec2b8fe14b | -7.72259 | -44.16678 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e3d3ee51-ca54-36da-8436-1716e4adbb42 | -5.6131 | -37.53223 | 2026-06-17 03:23:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8646455a-b7ad-3533-b12b-7e56095bd0b1 | -7.72273 | -44.16085 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b03c1121-ace7-3fcd-a878-03cd915b0ff9 | -6.29044 | -43.63299 | 2026-06-17 03:23:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8dfd389a-f5db-3aae-ae62-f66adec26b64 | -7.71688 | -44.1589 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8fd84b96-2e57-3380-8580-cc20591e7d6a | -7.71579 | -44.15955 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 98d6c92c-092c-38e3-a012-b280615f361b | -7.71563 | -44.16555 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 84868d4d-f77c-3c56-891a-5fa9c1b81836 | -10.46713 | -37.43678 | 2026-06-17 03:23:00 | NOAA-21 | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fdf327d5-f898-3f46-85e3-1062bd1a892d | -7.72146 | -44.16737 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 3a32248b-c76f-307a-a258-dab9b1946419 | -7.71449 | -44.16619 | 2026-06-17 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f55f531b-650a-306d-942c-c8713b61233c | -10.60065 | -44.32727 | 2026-06-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 461fb195-08d6-3b28-a772-5be07b995cf0 | -18.83116 | -40.13206 | 2026-06-17 03:25:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 90b8d052-8e18-371c-a897-2102ab75c2f0 | -10.82001 | -44.30633 | 2026-06-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9f719160-7311-3105-806a-c09ac1a582df | -10.93289 | -44.66703 | 2026-06-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c0711a0-2920-381a-8a3a-060263c93957 | -12.84575 | -44.37896 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 1d220f26-3a08-3a81-97ed-ee2342965e76 | -13.27433 | -46.06771 | 2026-06-17 03:25:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4e220b3c-d45f-3206-8719-4a2972a94c17 | -13.28279 | -46.06272 | 2026-06-17 03:25:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c9e96cd-04b2-33a2-a311-cbb1d29e822e | -10.9316 | -44.67325 | 2026-06-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a591aeec-1de1-39de-a060-304c010c1176 | -12.84664 | -44.37494 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 36ebaed4-5809-37c5-8033-83f8b12f73d8 | -15.51636 | -40.79303 | 2026-06-17 03:25:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 712d8ee2-5ae8-3a7b-8660-9fc548bcdc00 | -12.83928 | -44.37767 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| ae983288-3e99-3dfb-91c6-62d349ac83f4 | -12.26465 | -43.50482 | 2026-06-17 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7914384f-e20d-3d26-afc3-471542c3627f | -12.26716 | -43.50101 | 2026-06-17 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85dcae6a-a3d8-35ee-8bd3-91a3b8a78411 | -12.84783 | -44.3693 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 90fb54b4-98bb-39fd-9249-0a5341676bf0 | -12.84017 | -44.37368 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 7625a4ca-18f0-36da-96f5-a177fe324def | -10.59765 | -44.32623 | 2026-06-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97d230ca-3f4c-3dd0-8512-8d9d002b6512 | -11.03255 | -44.31933 | 2026-06-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20136e73-56ae-36e5-9900-19dc1415ccc2 | -15.5144 | -40.79726 | 2026-06-17 03:25:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2c4b9246-0956-303e-9a41-2753950adbba | -15.59188 | -41.79983 | 2026-06-17 03:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7f657f95-8fac-3dd9-b642-b49eeddc6a7b | -11.41746 | -40.82085 | 2026-06-17 03:25:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 16e3d7ba-9728-31c6-87bb-77576cca4cfa | -10.60189 | -44.32116 | 2026-06-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ffcc4339-2710-3f89-97a9-43ac97ef483c | -11.4181 | -40.81747 | 2026-06-17 03:25:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6a064de2-3a69-338e-a972-3a9e144c485a | -12.84136 | -44.36802 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| de3025ef-d05c-34f6-b2e0-438fa2ab8a01 | -11.28755 | -41.99778 | 2026-06-17 03:25:00 | NOAA-21 | PRESIDENTE DUTRA | BAHIA | Brasil | 2925600 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3381df6-fd23-3863-9806-1868b02d8517 | -15.51552 | -40.7914 | 2026-06-17 03:25:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 8ce6592b-9b2d-3cdf-9204-ef32673c0f3e | -12.84805 | -44.36763 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| ea2357d3-a142-3bab-962f-06e407926a8b | -13.27583 | -46.06082 | 2026-06-17 03:25:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 206e05a9-7c80-3fbe-bf5a-3f51ca5a0979 | -12.84043 | -44.372 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| dd6c2e47-dcfb-3413-9eaa-e0f42eb7b512 | -12.8469 | -44.37328 | 2026-06-17 03:25:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| d8e656d0-01dd-3972-a6f8-9e2046b8dc34 | -12.26617 | -43.50601 | 2026-06-17 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0de4c87-9e5e-3cdd-bd0b-98a2a82eaa36 | -19.30177 | -40.37481 | 2026-06-17 03:28:00 | NOAA-21 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3d12ff3d-bd35-3697-ba55-aa01f3ade279 | -12.8354 | -44.3657 | 2026-06-17 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| fecef666-1146-3288-aef9-7409bcbde3de | -9.3234 | -45.4787 | 2026-06-17 03:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.3 |


[Clique aqui para ver as próximas entradas](README6.md)
