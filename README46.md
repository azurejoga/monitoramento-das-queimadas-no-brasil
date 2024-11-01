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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27ba8458-0879-3fb8-ab66-9e1000ea746e | -2.7424 | -51.73086 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4c14b490-fe4a-3578-a3c7-1e0c7caefe84 | -2.74159 | -51.73648 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12c804f1-3142-36d2-8c4c-059f50bfd05a | -2.74062 | -51.73007 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1d62001-9897-3d79-b5ec-62a6c777f847 | -2.73977 | -51.73564 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8a6c4ce-9946-391a-aee1-d20740066e64 | -2.73746 | -51.73021 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6bf93af-6c0b-36f4-9b36-b70d046c7670 | -2.73569 | -51.72937 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c8f7e17-09a3-3d03-8fbf-4928534727b5 | 3.42287 | -51.26419 | 2024-11-01 05:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c46694e1-f41c-3b06-9cbc-752d0984357e | -2.73529 | -51.83026 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c56cff1-ec91-3f43-a02c-7ad1e6a64e60 | -2.73255 | -51.7294 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 337d8d22-1618-3a11-b5c1-ad992f1ed39e | -2.73078 | -51.72856 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56efeee4-c956-366e-ad31-fea6adbcdf5f | -2.64639 | -51.75485 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac39c5c8-523a-3b86-bf3e-a48f2c9e13c7 | -2.64229 | -51.74858 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b92fc0ce-0280-3730-b563-73c418e10736 | -2.64172 | -51.73687 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 043fd33f-45b4-39ba-b264-bcc0193f7c16 | -2.63766 | -51.73059 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16e16ff5-841c-3147-9eb5-5ac668c028b3 | -2.58343 | -51.92196 | 2024-11-01 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03152ea3-da24-3639-83c5-9d4d2179b045 | -2.57126 | -50.6551 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8fe97e0-4fa8-3483-ace3-c136428e86fc | -2.57082 | -50.65396 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f4c2a2d-bc65-3a0a-ae77-0b4f0ac6e4b9 | -2.56646 | -50.6511 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c9493eb-a180-3d57-8e53-89e6f15ee883 | -2.56596 | -50.65437 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8bee27c-8710-3798-a106-dfd79eafa87a | -2.56552 | -50.65319 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d780695c-f0bc-309d-ae7e-32683c065d1a | -2.41989 | -51.96466 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61e700a8-433f-38d1-9d6c-c8edd03891ea | -2.2948 | -50.66873 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31e30110-2b5d-3ad5-9368-b5b630da0d2d | -2.26847 | -50.62818 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c179970-ef6c-359d-8aba-424d57d9f58a | -2.26518 | -50.68731 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95d3e82c-1192-3d82-ac4d-57898f9bcbe5 | -2.2604 | -50.68325 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecfd6257-5e85-3fad-9b31-55e2dbfa4669 | -2.25993 | -50.68648 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 08f483fc-a3c5-3201-9475-1a75e09f5acf | -2.25471 | -50.68609 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d652c822-32bd-327f-a1d0-aab9dc06eb4b | -2.25468 | -50.68567 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dec35ab-b210-3596-baa1-07dc96c1c0f9 | -2.24897 | -50.68851 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41b8f40f-ed49-3acf-aa56-9a8535a3a8c2 | -2.24895 | -50.68808 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fa7a3a0-fe99-3c68-b426-188e0b255c92 | -2.24848 | -50.6913 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd118baa-af81-31e1-a5b3-dd9d634d3376 | -2.24847 | -50.6917 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02aa64bb-fc91-397b-a0ee-d187f0f6c63d | -2.24372 | -50.68771 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 26e12b5e-a188-33df-bcaa-8abfb17e2857 | -2.2437 | -50.68727 | 2024-11-01 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ec18d912-3c3b-35c0-8302-1a9e30eed237 | 3.42439 | -51.24426 | 2024-11-01 05:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 523c0f77-79f4-3b83-a3de-b943e14f24fd | 3.4221 | -51.2594 | 2024-11-01 05:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 217bcc75-3c4f-3bfa-8458-beace2795aef | 3.42132 | -51.25461 | 2024-11-01 05:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bed8eb88-29c1-36a1-8804-43547a433ee9 | 3.34825 | -51.38636 | 2024-11-01 05:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c50a1cdc-bbf6-39fa-9c45-ddcae97b0647 | 3.34749 | -51.3816 | 2024-11-01 05:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ac7d2c4-05a9-346d-b91d-52ee25ac9514 | 1.00872 | -52.21753 | 2024-11-01 05:23:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14bdbd47-12ef-308b-a903-9405d9d2b498 | 0.54503 | -51.68391 | 2024-11-01 05:23:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4219d6b-1a6b-30ee-89d8-7cef82f5e6da | -0.69363 | -51.67396 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ead5007e-c33d-36ad-9f8b-be75a50b0fe3 | -0.68899 | -51.67379 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 44c1889c-47b8-3626-8326-c235350b08f3 | -0.68885 | -51.6732 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8ecca78e-042b-3139-935e-2d9d10cb7f3d | -0.68822 | -51.67896 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.3 |
| c19f0c78-9ea6-3e28-ab61-89f3757b4196 | -0.68804 | -51.67836 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 084c4606-b551-3831-86ba-1a4f6c9c4341 | -0.68745 | -51.68414 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 37d06551-29dc-31f6-9b4c-a987492541c0 | -0.68722 | -51.68353 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 59123eae-9d63-31e1-bdb9-c96fbcf6e8da | -0.68641 | -51.68869 | 2024-11-01 05:23:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6703b0ba-9250-3939-a8f1-27cd8b4c2998 | -2.05674 | -52.03313 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba2b9a17-a793-3e12-896d-e430f13bfb01 | -1.89017 | -52.06278 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14933d1c-e8c9-3ff4-a5d8-ff8642ea879f | -1.88543 | -52.06203 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f18baf8b-3dc5-373b-8e68-02b7bb501627 | -1.88488 | -52.1294 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d8052d4-7825-36e5-97ca-8d35a22e54a9 | -1.73686 | -52.36099 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71e41320-becc-3d5e-946c-981d4a9e657b | -1.60632 | -52.38388 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e00530d4-da2f-3cd8-86c3-3f83e02c2e85 | -1.60169 | -52.38316 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dcdb06c2-d8a7-3132-91e7-aefd5e06fda7 | -1.58441 | -52.13393 | 2024-11-01 05:23:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e29af81e-e2ac-3336-a62a-75660edf6eed | -1.57971 | -52.13321 | 2024-11-01 05:23:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7249f1ad-37a5-35d3-8f7e-fa0454d8b260 | -1.57393 | -53.10336 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b2147e38-e1ce-34c1-86b1-a9b48c5dab98 | -1.56532 | -52.95389 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5b814f6-f524-3c9c-9e84-4984394fa868 | -1.5327 | -52.12589 | 2024-11-01 05:23:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12a16f36-18dd-34d8-a415-15b317ebba27 | -1.43589 | -52.20942 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a2458f-2840-332a-9147-edd85ecb8ea1 | -1.43197 | -52.20379 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d799e014-7780-3d2b-a828-22275efc451d | -1.42731 | -52.20305 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 10bd3cb6-a0f1-37ab-a769-cc51e6f546f5 | -1.42338 | -52.19743 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e2e19b40-bf23-39e9-a86c-94bd0bd7fe67 | -1.41723 | -52.2065 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fbceefa3-df29-3788-ac0f-977d13248b47 | -2.05657 | -52.03196 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fde7afc6-cfde-3b46-9b1c-34ecd1ebde6f | -1.8896 | -52.13016 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8cc5531f-cb5e-3c68-9db5-db3602c861ad | -1.88411 | -52.13446 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b716b6f-d200-3aae-8c66-08a57c4840e7 | -1.73369 | -52.35059 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc0c37c5-d1a3-3d98-89bf-b8c37e0d9445 | -1.6636 | -52.1327 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d65e0c27-b231-37dd-846f-b655a90f2f7b | -1.60777 | -52.37431 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 022f0975-cbbf-32c3-9f9a-ffb8eec3ee97 | -1.60242 | -52.37837 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a196568-5676-3a73-beac-1e719b5931ed | -1.5854 | -52.14046 | 2024-11-01 05:23:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 196fce47-7a1f-389c-969d-6e848f9339ca | -1.58364 | -52.13892 | 2024-11-01 05:23:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ffa22175-2452-37f8-a9b7-64ee3a1b1505 | -1.52875 | -52.12017 | 2024-11-01 05:23:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91576eb2-85b6-3629-ae25-26bfcd4ad021 | -1.42264 | -52.20233 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fa7d34de-980d-30e0-86eb-f71251a41be4 | -1.41797 | -52.2016 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45b77d76-cec8-3b60-89fb-efd464aea61d | -1.28104 | -51.93779 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df3639b4-b2de-3236-b729-eb0b98522eb5 | -1.27629 | -51.93707 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 163195fe-d444-330b-90f8-d64252a2ebb8 | -1.239 | -53.11351 | 2024-11-01 05:23:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 791e13f4-cb15-3123-9c98-6940870db467 | -2.99381 | -52.35878 | 2024-11-01 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3e68c4f-01fe-351b-87d3-23f225327a2d | -2.99233 | -52.36888 | 2024-11-01 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce0fd5b-df95-3fce-aea1-b695b6abde4b | -2.91244 | -52.5984 | 2024-11-01 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c757dbc-bbbe-3e19-aed2-c4706c3889be | -2.8823 | -52.89564 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2cb8a019-3fc2-37cf-864b-9d87f7a0962c | -2.88154 | -52.89399 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f3fc188b-ad1b-37b7-be14-afc728174bde | -2.87845 | -52.89009 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1c7c3102-ea0e-3a05-a412-cfbd1bc59c8b | -2.87776 | -52.89485 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3a59f71-9815-36d9-8d31-b27215d6b5e6 | -2.87772 | -52.88847 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a37cf135-ce92-30e7-b72b-75d4a854d6c6 | -2.87175 | -52.89712 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b342b1f7-0db3-3871-abfb-db4aa110ddc4 | -2.86907 | -53.32817 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 746803f9-fa8a-34d4-aed5-e9d0206a8aaf | -2.85701 | -53.34858 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c1937d5-88b5-30dd-bbe9-63b5a0508a6e | -2.84819 | -53.34726 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5ad810bf-26bb-384f-aab5-431b4055b144 | -2.62258 | -52.4548 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2cc6377-33eb-3e2c-af46-b93de7031caa | -2.62016 | -52.45315 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 27b52521-342d-396d-b3ed-b27a78ad65e9 | -2.61862 | -52.4491 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae6d4eb9-c43f-3903-a491-70de00a75dec | -2.23839 | -52.76781 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 31382179-71f3-3ba8-b5fa-b76b5a9f9e91 | -3.22179 | -52.20642 | 2024-11-01 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| bc485db6-e911-3318-9568-948bfa36f3e3 | -2.61791 | -52.45404 | 2024-11-01 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ecd1671-6807-328c-bf4c-3f9f60e4533d | -3.33887 | -53.10571 | 2024-11-01 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README47.md)
