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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b3112027-ecbe-31b4-b3de-08c8ba55ba79 | -9.71749 | -67.47805 | 2025-11-11 05:44:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd318961-2cfd-3938-bf12-e218e946f1f2 | -9.72363 | -67.4828 | 2025-11-11 05:44:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8a0aff3c-3a70-32ae-b2e9-b7a64dd74377 | -18.38947 | -54.99658 | 2025-11-11 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1620a7b-f85d-34cd-a5e1-d50bbdb163ea | -10.51712 | -67.80698 | 2025-11-11 05:44:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24200db7-8a3c-3b7a-a57b-11e95cf9850d | -18.39308 | -54.99755 | 2025-11-11 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 72418d95-ccf5-38b1-8915-961c9c5496d3 | -18.39004 | -54.99054 | 2025-11-11 05:44:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c342fee7-2f21-3d7f-9083-8c7e1965e5c6 | -10.00077 | -67.36163 | 2025-11-11 05:44:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abef2404-cd79-33ec-b5a1-f91b3034b63e | -18.39061 | -54.98449 | 2025-11-11 05:44:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d23200d-bb45-3d4c-90d7-e84021f5fb40 | -20.10812 | -54.66011 | 2025-11-11 05:46:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 658c79d5-2636-3a21-8e6c-64f2898377d6 | -3.5344 | -45.7509 | 2025-11-11 06:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6f97da43-a4c2-36e1-a145-704f711915f7 | -3.2022 | -45.2707 | 2025-11-11 06:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 26c0a49f-1c11-32e6-9ea8-94598c73fa64 | -3.2207 | -45.2925 | 2025-11-11 06:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 41dc0874-efb2-367f-b727-045604175b28 | -3.2208 | -45.27 | 2025-11-11 06:10:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0f5e6cb8-bbee-3eb5-a21c-48d5a3d896ed | -3.2208 | -45.27 | 2025-11-11 06:20:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 68.1 |
| d7a2b6a0-ef35-3525-8846-336fd5ba3dda | -4.0014 | -45.393 | 2025-11-11 06:40:00 | GOES-19 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 0bfde222-a2ee-37eb-b787-7ed7dc6c4f98 | -4.0015 | -45.3704 | 2025-11-11 06:40:00 | GOES-19 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| db1e73d1-5070-305b-85a8-8c25d5bca88f | -18.39189 | -54.96443 | 2025-11-11 07:07:00 | AQUA_M-M | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 135df4ea-1a4c-3150-8fae-42e23e9fc5bf | -19.81998 | -58.03878 | 2025-11-11 07:07:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 18.5 |
| ff0ba2ad-6e68-3e37-bef3-289eea754630 | -2.7392 | -44.8586 | 2025-11-11 07:10:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 07591611-eae7-305c-8fd2-15f0d0ea7a5e | 3.53074 | -51.77662 | 2025-11-11 12:33:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c2905cf1-fff3-3e42-920c-232f12bb0843 | -4.2264 | -42.3367 | 2025-11-11 13:30:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 170c0462-6bad-334d-bb29-7d11ff0d8aba | -19.0323 | -57.5174 | 2025-11-11 13:30:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 100.6 |
| 4457281a-9d82-319a-b0bf-047711f07fdc | -1.6453 | -52.0447 | 2025-11-11 13:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 2bf8d3ff-2897-3ee9-8abf-33b8b2aca3f0 | -3.0904 | -45.3201 | 2025-11-11 13:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 09c989f6-3374-34b4-a6e2-3ec07a2fae1b | -4.2264 | -42.3367 | 2025-11-11 13:40:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 85.1 |
| eb7351b9-0ae2-31c5-b082-a3dc7ecba0b9 | -1.6453 | -52.0447 | 2025-11-11 13:50:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| fa294083-d450-3b6b-bcb7-239608933a50 | -4.2264 | -42.3367 | 2025-11-11 13:50:00 | GOES-19 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 104.4 |
| 199e69ba-64dc-3470-b85d-fda2add205f1 | -19.0323 | -57.5174 | 2025-11-11 13:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 110.9 |
| 461853a5-b023-37cb-96b7-88555c5ca36b | -1.6453 | -52.0447 | 2025-11-11 14:00:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 6dd0c31b-cb19-34a5-aaba-f98b7bb97a87 | -1.6453 | -52.0447 | 2025-11-11 14:10:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 275.6 |
| b8b9cc92-2ccc-31e2-b9e9-8ba07ed25233 | -10.2173 | -44.0557 | 2025-11-11 14:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 91ac7b85-b649-3bf9-ac3f-313edceeb27b | -10.2176 | -44.0323 | 2025-11-11 14:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| d5d1cfd4-bc35-3184-bba8-6cd1f5b1f60d | -3.0096 | -42.7274 | 2025-11-11 14:40:00 | GOES-19 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f59f6c10-8bd0-38a6-b6b0-287c13e8b1bb | -10.2173 | -44.0557 | 2025-11-11 14:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 163.5 |
| 91bc2954-3ad3-3093-b999-0039e9eb78e0 | -1.6453 | -52.0447 | 2025-11-11 14:40:00 | GOES-19 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |


