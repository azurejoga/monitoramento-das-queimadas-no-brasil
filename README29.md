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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 641e06b7-3f89-3b85-8103-b52b49de6031 | -4.9682 | -43.2299 | 2025-07-25 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 2e761e12-ec8d-3853-991f-76e0f34e7e9f | -6.4875 | -45.0056 | 2025-07-25 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e7d08a4c-9f04-3c87-98bc-f04caadeed12 | -8.3485 | -44.947 | 2025-07-25 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| b7bb20cd-166b-3008-8cbe-04a61c73e234 | -9.023 | -45.3305 | 2025-07-25 14:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.0 |
| a0c8e680-0b92-3122-9e0d-996d43478018 | -6.5626 | -56.25 | 2025-07-25 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 61e256f0-acff-37e0-b1b9-f5b66a0f5716 | -8.3485 | -44.947 | 2025-07-25 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 05f7e4fb-f1dd-3f97-91c3-07f75a008182 | -4.9682 | -43.2299 | 2025-07-25 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.8 |
| e6677281-ef50-3891-944c-b39a36ca4e7e | -9.023 | -45.3305 | 2025-07-25 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 581c7b72-5d90-3521-b87d-f0fbf4b6025f | -4.9682 | -43.2299 | 2025-07-25 14:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 142.7 |
| e74b9e9f-6f37-3bf1-9a4d-f0a26e3efa1b | -5.7294 | -43.9651 | 2025-07-25 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 425a5c87-524b-3a00-ab90-6ea97f45b86a | -9.023 | -45.3305 | 2025-07-25 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 112.5 |
| dd39cb86-b8d8-3748-a992-4b1d27ba0131 | -12.7085 | -47.0036 | 2025-07-25 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d4a873f9-74af-331d-af4c-92cdb9929099 | -6.5626 | -56.25 | 2025-07-25 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| cbc038c1-b4a6-30bb-9067-1c8a62a2cac8 | -14.1327 | -45.2644 | 2025-07-25 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 35fa4ac4-b438-32da-9447-77da69f4f714 | -6.4161 | -53.3281 | 2025-07-25 14:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 561c8e06-0d53-3d9a-8475-410760d2f874 | -8.3485 | -44.947 | 2025-07-25 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 60de92e5-58f5-38c7-9271-366d4226880d | -6.5441 | -56.2508 | 2025-07-25 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 006ad02a-1193-3823-8f01-88022923c38e | -6.4875 | -45.0056 | 2025-07-25 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 06f8e17c-f2c9-346d-8403-4606396c355e | -6.5626 | -56.25 | 2025-07-25 14:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 138.1 |
| d912caf9-668a-3eaa-8853-8110e1e91948 | -8.3485 | -44.947 | 2025-07-25 14:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 2d7ba5fa-62a2-3ab5-b19f-9675a29fa41f | -4.9682 | -43.2299 | 2025-07-25 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 125.9 |
| dd22f09f-043c-3e5a-aaf3-a28e075552c9 | -5.7294 | -43.9651 | 2025-07-25 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8c6f7ead-bf79-35a0-889a-859d9b319e5e | -6.5754 | -45.5871 | 2025-07-25 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 6f18916c-a45c-3b2e-b84e-8dae7d415904 | -6.7309 | -45.031 | 2025-07-25 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a5a199c2-a7c0-31b5-8566-60182bacf959 | -8.8872 | -45.5954 | 2025-07-25 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 2faf1157-758e-3df7-bc1c-a113802b9b52 | -14.1327 | -45.2644 | 2025-07-25 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 3d1810f3-6c1e-3698-9093-13563c3ab27a | -8.9061 | -45.5933 | 2025-07-25 14:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.8 |


