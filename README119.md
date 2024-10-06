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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d2240b0-2564-3f7c-a3c3-da2fb37fd923 | -16.5695 | -57.21907 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 2c250f66-c222-3d02-b85a-9c4d86d9b1b4 | -16.56776 | -57.20649 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d5e2a8fd-8213-3886-814e-78a28b1aacf8 | -16.56776 | -57.15719 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 659f425f-fc5a-34fa-a8e4-5d84fae80b4a | -16.56718 | -57.21051 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2b6c34e9-216e-341c-a942-0823c344e31a | -16.56718 | -57.16119 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 07527ba6-722d-30dd-bafe-cb3481a5f513 | -16.5666 | -57.21452 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5431f0fa-1fb7-3c2a-a0e4-2268b6e443a9 | -16.56544 | -57.19792 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6687e1bb-8c37-332d-8257-2097f946eb02 | -16.56485 | -57.20193 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 67b48020-dd7e-3dbc-b315-ac8bfb48c686 | -16.56369 | -57.20996 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 7251436c-e7d3-3e12-a01a-f213826d85d9 | -16.56253 | -57.19335 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0a152f2f-afb5-3930-ab6e-59ffdaaa9b63 | -16.56252 | -57.21798 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 519b9e7b-330b-34b1-9b0d-eb7143fb4341 | -16.56137 | -57.22599 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| e694aee2-86f6-31a0-a792-b09e60c38960 | -16.55846 | -57.22144 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| dcf45361-692e-3fa0-abf1-b94a2e6f4228 | -16.55788 | -57.22545 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 8ad7b0b1-4a69-3e16-8548-d64fb36e8a97 | -16.55614 | -57.21288 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| 455a3b8c-8c25-3a40-a136-73bbd2e8d105 | -16.55439 | -57.2249 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 214b338c-63d0-33e4-89a5-780952197953 | -16.55265 | -57.21233 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.4 |
| ed4abe7a-5171-3663-bf0b-9da51559b7f7 | -16.55207 | -57.21634 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2f958083-c30d-39ee-83b2-dcad4981199a | -16.55149 | -57.22035 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 42e650ad-1d0e-353c-9324-f102c8905d18 | -16.54974 | -57.20777 | 2024-10-06 05:14:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| d788855c-9eba-302c-a358-a5a0610cda05 | -16.54103 | -57.21872 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 003a00ff-2a35-36e2-91a8-e5753b3ddcc5 | -16.54046 | -57.22272 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 843e69c0-b66c-3c74-8884-003dfc6c3d8b | -16.53755 | -57.21817 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9575bf25-11b1-3efc-b928-27d392ce5205 | -16.53349 | -57.22162 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d8655b5f-160f-3420-8690-81eccd2a41e4 | -16.53118 | -57.23766 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 48070b00-8f07-31a6-870c-d898fe00ef96 | -16.5277 | -57.23713 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3646b252-1679-3eaf-b07a-6fddee0efedf | -16.51901 | -57.24803 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e6d9fcac-9b3b-33d1-8f34-197919ca9552 | -16.51725 | -57.2355 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8fcfe374-1566-3588-890f-c9bf2ae93fb0 | -16.51667 | -57.23951 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 60667af2-f3b2-3cb2-8ef5-1f96e977c769 | -16.51553 | -57.24751 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c36b49f0-d1bb-31b8-8ea7-549bf49cd884 | -16.51376 | -57.23498 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 3038aa6a-341e-336c-b1cd-f3c356d3876b | -16.51319 | -57.23899 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8d7e99e3-e4b1-3db8-8ddd-7cd4222745e6 | -16.51204 | -57.24699 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c661bb98-6351-378d-9c5c-69186ec431ec | -16.51028 | -57.23444 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| dda57ff6-38e2-3f36-a6b8-f7f7985e3ab1 | -16.50971 | -57.23845 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9ce5ddc7-df20-3a81-a1ad-1429bba37eb3 | -16.50913 | -57.24245 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8afc2dd4-662a-369a-91c7-e037fe0d7789 | -16.50856 | -57.24646 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9b553dc3-76cc-3f59-84cc-abbb5648b949 | -16.50742 | -57.25439 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 97f560fe-1f8f-3003-a260-29c3394e9686 | -16.50622 | -57.23792 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 97c06a82-487f-33ae-bd0a-da0fd566855c | -16.50451 | -57.24989 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 7edcaed9-0b0a-3222-8ef9-ce34b74224dd | -16.50217 | -57.24137 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 66a80d6b-1e39-31bb-8d90-28de62bc49e7 | -16.5016 | -57.24536 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3f924626-bfb4-395c-a3b9-26c8baa19e60 | -16.4999 | -57.25727 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4b41ed88-ba74-30a8-85b3-0dbc7573a8b1 | -16.49755 | -57.24877 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5a284f94-75b9-3438-aef0-1f76010456e6 | -16.49642 | -57.25672 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 33c2d9b3-ff8b-3c19-96e9-d5d6aa79ab3f | -16.49471 | -57.2687 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 88ed38df-997f-3315-92e2-090d8ff8e14d | -16.49464 | -57.24423 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| eecc4fc0-8fbd-34ed-b225-1d43b963b81e | -16.49408 | -57.24821 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 68c7cc8f-d5a4-3582-bf57-30cc97e878f5 | -16.49237 | -57.26017 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b6979d35-a6d5-369e-99b7-08934da1803c | -16.4918 | -57.26417 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 32f3d53e-8afb-3d6a-a0eb-384b86da701a | -16.49045 | -57.26059 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ed4692c9-121a-3c10-bedb-43f056491421 | -16.48987 | -57.26459 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 9f02cbc6-cd4d-309f-bbd6-79d7729cfa28 | -16.48946 | -57.25563 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fafcde47-d885-3562-a94a-656021dcb380 | -16.48889 | -57.25964 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0804c28e-4333-3b73-9f6b-e40354f29c27 | -16.48832 | -57.26363 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 30f8cec8-ac98-3ff8-82ab-0b707d9b9e6d | -16.48815 | -57.25207 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f7b57954-6f3b-369b-8cef-51da59539c84 | -16.48698 | -57.26005 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0dceb1ee-8450-3696-a654-4ff675bd205a | -16.47188 | -57.29023 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 781d30df-191a-3d0c-b4df-99f76c1f129d | -16.46841 | -57.28968 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 245d6301-2c8b-3d4e-bb01-4ae076054934 | -16.44931 | -57.27451 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| baa15e83-f5c0-302d-b36e-bbe1bcc80f27 | -16.44815 | -57.30681 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 03a8a840-9a46-3884-8063-c8e56db09b16 | -18.66976 | -57.26423 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b7641b23-f669-3755-be8f-0468852765a4 | -16.44757 | -57.31078 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4bd3f0c8-47de-362d-a895-1bad4329de35 | -16.447 | -57.29038 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c8a55c94-c4ef-3cf6-9cab-aff27331b127 | -16.4441 | -57.31023 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a4dfab8d-a770-325d-8182-8133a3676baa | -16.4441 | -57.28586 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 63d7de11-6def-35b9-9be0-0cd6bcb0ac4d | -16.44353 | -57.28983 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 38691df3-d902-34ae-9e62-97e82bc7605c | -16.43947 | -57.29325 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 46785a7c-1535-3231-be25-f5c2704666b0 | -16.43831 | -57.27684 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 4e3e67f8-c992-36c8-b85e-c22a5b56972d | -16.43773 | -57.28081 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 951e52cf-348a-3ad8-a792-9bf2b7d08a10 | -16.43426 | -57.28026 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 9ba3afaa-bb0f-3aff-a1a0-402784064f30 | -16.43021 | -57.28368 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 5668bd39-aafd-3d1d-b4ff-f2def66dd6bf | -16.42852 | -57.39268 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8000907d-101e-36ad-98b9-e171a8dc6cfe | -16.42158 | -57.34315 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4ccf2ac5-990b-3b1c-b12a-5548a5277462 | -16.42101 | -57.3471 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0a72f0c8-1c07-345d-85be-db0ba4bb4251 | -16.41987 | -57.37923 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 17f7624f-127b-37f0-988f-55b61b1f1ab0 | -16.41872 | -57.38711 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c2678348-d7f2-3c42-b3de-5d842a421d9f | -16.41754 | -57.34656 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 39757a36-2ae1-39d6-9f6c-6c4ff4c7de68 | -16.41408 | -57.34602 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bef042e1-0c50-3b01-bdda-f8cc5b7d6a8a | -16.41118 | -57.34152 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 016972e6-b9d7-3abe-86cf-7ff700345515 | -16.40715 | -57.34494 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8d2989f4-447b-360b-9212-07fdff33df49 | -16.40658 | -57.34888 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 86759073-3e62-3012-8b96-9081e2d00801 | -16.40311 | -57.34835 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 63c76754-a623-366d-9e3c-3877c0faecdb | -16.39911 | -57.37596 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c2cf035c-edd5-33db-900a-6155e639e025 | -16.39908 | -57.35175 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e06192e8-c407-3b01-91ce-b0c28326aff2 | -16.39851 | -57.35569 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d9a67513-46df-309d-828d-5fa7ba90a707 | -16.3922 | -57.37487 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| d837bada-bdd9-3c0b-a887-01b3a8ac5bc3 | -16.39158 | -57.35461 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 03508812-7753-36a2-a90b-5bbe57ee5091 | -16.39101 | -57.35855 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 145adfd9-f683-36ac-b66d-9ded9172d2cc | -18.6662 | -57.26368 | 2024-10-06 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bfdd4d40-01ca-3e61-8443-360b813744d7 | -16.38931 | -57.37038 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e55adc39-5759-3ea5-a038-ae6de6af5b85 | -16.38698 | -57.36197 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 936179ca-8e8e-3bb7-be4b-40090decb09b | -16.38352 | -57.36142 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a5e3ce7e-407c-39fd-b813-1ede2ccc478b | -16.38295 | -57.36537 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 962ace25-4873-3172-a7ed-2b7e195ba2d9 | -16.38239 | -57.36931 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 18e7daf3-cce7-35dd-8840-50c7b924bc49 | -16.38182 | -57.37325 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 263387c6-e9bc-322a-9918-9c8883172e0f | -16.37949 | -57.36483 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e39d85f5-451b-3554-a256-a8f87566ca85 | -16.372 | -57.36769 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4a196b65-f8aa-333f-8f18-bbcf888a41c4 | -16.15443 | -57.42102 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5f2adcee-7cba-3024-a0eb-ca1bd30560b3 | -16.15098 | -57.42049 | 2024-10-06 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README120.md)
