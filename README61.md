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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9701d59-235e-3c0a-a7a8-9831bc06cea0 | -16.0183 | -59.53188 | 2025-10-09 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05e8bde4-df7f-3bb4-8484-06b51585c13f | -10.15486 | -64.25162 | 2025-10-09 06:01:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00acbb6d-c442-3014-955b-f876f640f04d | -9.62235 | -67.51837 | 2025-10-09 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c99eb6-ac5a-31b4-9f10-c338f065d6aa | -16.00343 | -59.5484 | 2025-10-09 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3b1c414-4c3e-34d1-b364-e9da3b050e3d | -15.99649 | -59.55177 | 2025-10-09 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5940acab-8dad-3d73-ae57-ea97c477f9c7 | -16.59979 | -58.15955 | 2025-10-09 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d085126c-8f9e-373d-abb5-2a9895c2f334 | -16.01752 | -59.53619 | 2025-10-09 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c268bee-ed00-3c37-bed5-07e3b7754760 | -16.01779 | -59.53686 | 2025-10-09 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bb3de70-2c6a-395e-aaba-5f2c223cca7f | -12.21912 | -64.35284 | 2025-10-09 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96228fd6-3817-30ba-8fca-def6df8554f8 | -9.68343 | -67.455 | 2025-10-09 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 593d9330-96d4-3e35-a34c-bc781b492ed7 | -10.0254 | -68.35493 | 2025-10-09 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7d0f789-9796-3a01-ab07-b04a90816d54 | -16.01799 | -59.53125 | 2025-10-09 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 523bc755-da19-39ab-99bb-ba5b5fe539a0 | -10.69962 | -68.57594 | 2025-10-09 06:01:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbad9b7f-7b52-3bdf-93f8-aaf5513493ee | -10.1111 | -67.8515 | 2025-10-09 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c4aee28-ece7-37f5-bbc8-4227d7a675a2 | -10.16798 | -64.73889 | 2025-10-09 06:01:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01474872-8305-353c-a482-813185721dab | -9.68406 | -67.45081 | 2025-10-09 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e36aa87e-2551-368e-8403-15e372982e8e | -9.62595 | -67.51891 | 2025-10-09 06:01:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 004160fe-5ed9-3f32-b803-7697247f9e85 | -9.96637 | -68.81744 | 2025-10-09 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 50ab8490-6ccb-3f80-b7f7-188bf5ebfa99 | -16.59909 | -58.16692 | 2025-10-09 06:01:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c52e483a-7ee3-35ee-8b0a-261d3215133d | -10.15042 | -64.25098 | 2025-10-09 06:01:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cb28da9-f912-3470-b45f-5666e62e36cb | -10.0508 | -68.44593 | 2025-10-09 06:01:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bc9caeb-f87b-3ebe-8c61-a03ed7771369 | -15.99696 | -59.54711 | 2025-10-09 06:01:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6a5c0416-069d-34a5-87e0-b1a6d694a0b8 | -12.21851 | -64.35747 | 2025-10-09 06:01:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32178d1b-bfce-3aa2-91d9-0297e0c405f2 | -17.9224 | -57.5128 | 2025-10-09 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.2 |
| 74af9752-9113-3401-a694-9d0f7110dfb9 | -17.9227 | -57.4922 | 2025-10-09 06:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.4 |
| 4276dc22-b4a9-3c44-a9e3-710acf8a3505 | -17.9029 | -57.4947 | 2025-10-09 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.5 |
| fde97ae6-6ff2-39f9-b988-cda92951e7d7 | -17.9227 | -57.4922 | 2025-10-09 06:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| e5b44dd8-de9e-3467-b5d2-e6d3d0baeb7f | -17.9227 | -57.4922 | 2025-10-09 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.2 |
| ebe36b27-5738-368b-9e38-c6a1f28c2686 | -17.9224 | -57.5128 | 2025-10-09 06:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.7 |
| 65f4d869-6f90-3f2d-9cf7-1e3f97d09ffe | -17.9029 | -57.4947 | 2025-10-09 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.3 |
| df13c38e-8777-34c5-b1bd-c4514252fda6 | -17.9227 | -57.4922 | 2025-10-09 07:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.1 |
| b56df0ab-3703-3a11-ba43-535a3f1c63e5 | -9.5808 | -65.7093 | 2025-10-09 07:09:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49b0432e-09c0-3df7-8d68-fa8b1ddf79ce | -17.9029 | -57.4947 | 2025-10-09 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.0 |
| 5923ba69-eb48-309d-8f6b-fd0ae42cb3d3 | -17.9227 | -57.4922 | 2025-10-09 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 090d128f-1eed-3f13-9ad1-9a6dce1e1494 | -17.9026 | -57.5153 | 2025-10-09 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 0518a749-cebd-318a-9ea6-078d843f17b0 | -17.9224 | -57.5128 | 2025-10-09 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 550ca7b2-48f0-30ad-9d50-d6cbaf480068 | -17.91854 | -57.48033 | 2025-10-09 07:12:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.1 |
| 0a21f48c-e6bc-324b-a4ad-25baf22bf38a | -17.9227 | -57.4922 | 2025-10-09 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| ad5bdaf2-6b01-3379-ab23-40ba40153e0c | -17.9224 | -57.5128 | 2025-10-09 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| f22c0283-ae93-3444-a555-108038daa3c9 | -17.9029 | -57.4947 | 2025-10-09 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 6ab8f0af-dde9-3afb-a782-969d33cbcc67 | -17.9227 | -57.4922 | 2025-10-09 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| 22632657-6861-3af0-a674-cb2f49409b0a | -17.9026 | -57.5153 | 2025-10-09 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.1 |
| 08ccb3d8-3e87-32d7-b536-32f9acd42371 | -17.9029 | -57.4947 | 2025-10-09 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.7 |
| f698a293-0e60-3351-9519-a0fef2aa1989 | -17.9227 | -57.4922 | 2025-10-09 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.8 |
| e6c221fa-0b40-332c-a675-394bd9161d1b | -17.9224 | -57.5128 | 2025-10-09 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.9 |
| 6fac9279-82b2-3afb-9e96-2629df36dbe2 | -17.9224 | -57.5128 | 2025-10-09 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.8 |
| f38ea51e-09c6-36f1-826f-893ef31b6136 | -17.9026 | -57.5153 | 2025-10-09 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 5ca7611b-4727-3078-b7df-30e71d6fb1d3 | -17.9227 | -57.4922 | 2025-10-09 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 28dcf4a6-2175-3439-8def-a4e78483baa4 | -17.6538 | -44.4339 | 2025-10-09 07:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 3c9c6063-4f4f-3603-8ee5-8f30afa98c49 | -17.6532 | -44.458 | 2025-10-09 07:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 6bf49a20-76fa-31bc-8307-3fb289611f12 | -17.9029 | -57.4947 | 2025-10-09 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.8 |
| 831f211c-a25d-3e84-b0d1-d91349de8d40 | -17.9227 | -57.4922 | 2025-10-09 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.8 |
| b0f47153-5f5f-34ef-a58a-72af452f8884 | -17.9029 | -57.4947 | 2025-10-09 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.6 |
| 32bfa18d-69c1-31f7-8636-8dd84f953436 | -17.9224 | -57.5128 | 2025-10-09 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.7 |
| 2636ed0d-9562-3f91-acf5-3f969f6fd725 | -17.9026 | -57.5153 | 2025-10-09 08:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.9 |
| 1d537f35-e2c0-3e7a-8369-891e26ac20c6 | -17.9227 | -57.4922 | 2025-10-09 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 9cdd3e0e-66c2-3fb5-b540-e819a4a4be78 | -17.9224 | -57.5128 | 2025-10-09 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.9 |
| 163376ea-e65f-34dc-8b75-5fb11f5aa3a6 | -17.9026 | -57.5153 | 2025-10-09 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.1 |
| 458cd9ad-0871-3bd3-8798-e5d00aba76c4 | -17.9029 | -57.4947 | 2025-10-09 08:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.0 |
| 902b2c31-c3ff-3ebe-bd2a-8527eaa817ac | -17.9029 | -57.4947 | 2025-10-09 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 00ab0ee9-b6b2-37ee-9d6c-913f3edc12ca | -17.9227 | -57.4922 | 2025-10-09 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| 67f602c7-86c7-3b01-b1bd-0bf6f16a411f | -17.9224 | -57.5128 | 2025-10-09 08:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.6 |
| 4bdaf568-af64-31a5-9239-6be2c778b42c | -17.9227 | -57.4922 | 2025-10-09 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 4b22b649-ee69-3864-8870-de3783e1e04c | -17.9224 | -57.5128 | 2025-10-09 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.0 |
| 64b7fa2a-42d2-305b-b3d1-281252447ec1 | -17.9029 | -57.4947 | 2025-10-09 08:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| 6d7d44eb-00c3-3765-bd0f-6516a67800c4 | -17.9029 | -57.4947 | 2025-10-09 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 93222e01-99a5-33f4-b6ca-61b59c3f45b9 | -17.9227 | -57.4922 | 2025-10-09 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 37334cfc-baab-3733-8fa3-19da6359de96 | -17.9026 | -57.5153 | 2025-10-09 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 804393db-1a8f-3184-a3d5-a8ab4da3b30d | -17.9224 | -57.5128 | 2025-10-09 08:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 5fa156d9-475f-3135-bd39-9d92e5cf5c07 | -17.6538 | -44.4339 | 2025-10-09 09:30:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 2f45122c-00fa-3f55-8b87-49e2061e9211 | -17.6538 | -44.4339 | 2025-10-09 09:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 250.7 |
| 82bec805-31c2-35fc-8153-d8bea8fc9f71 | -17.6538 | -44.4339 | 2025-10-09 09:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 670d3349-761a-3551-b2d4-f5ba85500d21 | -17.6538 | -44.4339 | 2025-10-09 10:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 81fdca11-3abb-35cb-84fa-d44ec97b5645 | -17.6538 | -44.4339 | 2025-10-09 10:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 131.1 |
| f5b26b5a-9609-3a50-8d05-0b9adaac3712 | -17.9026 | -57.5153 | 2025-10-09 10:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.8 |
| d909ff26-6372-3e43-bdae-c2dc2042a998 | -13.8302 | -45.8255 | 2025-10-09 10:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 6f0b6121-0bd7-3368-a25b-92c38205d4dc | -15.7516 | -49.7821 | 2025-10-09 10:50:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 119.3 |
| c52ef962-8296-3bef-8311-8fe3c604906c | -17.6415 | -47.2103 | 2025-10-09 11:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 7f7c842a-e9d7-3f60-a4ff-a49b728b73b8 | -13.7904 | -45.8782 | 2025-10-09 11:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 90ff761f-8d4a-3aab-937a-6fd6fedac3f4 | -13.8302 | -45.8255 | 2025-10-09 11:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 21239824-7753-3e8d-83e1-4119439a712a | -13.4282 | -47.6151 | 2025-10-09 11:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 120.3 |
| 80ff9881-57c1-35af-a42a-77018427ba10 | -17.6415 | -47.2103 | 2025-10-09 11:10:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 17b71e18-6dd9-352e-b83c-dbe68a346e2f | -12.6964 | -47.6776 | 2025-10-09 11:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| cc3ce744-3d5f-3404-b0c0-8945abf1db64 | -13.8302 | -45.8255 | 2025-10-09 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 224.9 |
| eab9096e-e8b4-3262-8fcd-9fe4d32fc8de | -13.8108 | -45.8288 | 2025-10-09 11:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 6b3a15c5-c070-3398-8177-d64010ff7a04 | -13.8108 | -45.8288 | 2025-10-09 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.0 |
| 5008182a-e08a-3966-9f60-49d282ecaa64 | -12.6964 | -47.6776 | 2025-10-09 11:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 02779102-4b57-3988-ae74-c634535ec0b0 | -13.4282 | -47.6151 | 2025-10-09 11:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 126.1 |
| c631fb4c-b5d7-3b90-ba9d-6cf71800acec | -13.8103 | -45.8519 | 2025-10-09 11:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 2de80cca-66a2-341b-8089-769f8f849329 | -13.8302 | -45.8255 | 2025-10-09 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 262.9 |
| f71c04a7-63d1-3898-a682-7c8c84708529 | -17.6415 | -47.2103 | 2025-10-09 11:20:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 57e2f4d0-c318-3c8a-942f-0fc9622599c6 | -17.6415 | -47.2103 | 2025-10-09 11:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 01812203-f50b-33da-a1c4-5abe899879a4 | -13.8108 | -45.8288 | 2025-10-09 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 34980e94-1587-306e-844a-1b3a15ae0fca | -13.4282 | -47.6151 | 2025-10-09 11:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 162.9 |
| f170519d-f2f2-37c5-8a83-96aa80fde122 | -13.8302 | -45.8255 | 2025-10-09 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 6e02cd68-b96f-3df6-b4b9-d2c3a7b92416 | -12.9509 | -42.4886 | 2025-10-09 11:30:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 03ad464e-fa50-3b15-a00d-8b852bf3b1df | -13.8103 | -45.8519 | 2025-10-09 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 8bf659ac-4282-3ec8-bd35-0864c5267c8d | -13.7909 | -45.8552 | 2025-10-09 11:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 97.3 |
| ae57a8d1-e167-389d-9995-eb9ad6884dc3 | -12.6964 | -47.6776 | 2025-10-09 11:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 8ba2c950-aa42-3c9e-93a7-e04b8b9583d9 | -13.4097 | -47.5731 | 2025-10-09 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 138.5 |


[Clique aqui para ver as próximas entradas](README62.md)
