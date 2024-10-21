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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb23bb1a-e38c-372a-89fe-e68531c5c8b8 | -3.08375 | -54.17047 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 70a2927f-0d93-3b1b-8c6a-c67f64f101e7 | -3.08237 | -54.17975 | 2024-10-21 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| d6f5074f-e800-38da-af8f-9a439b76a5df | -3.06664 | -53.2313 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d41d90dd-dc58-3bad-8c1b-9b0ef46e6b4c | -3.06513 | -53.24147 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| f586e40e-67b6-3de1-adea-9fafbc03edb7 | -3.06065 | -53.27168 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| db4b8163-c873-3223-a87f-3a9cb8a10e29 | -3.02191 | -54.33966 | 2024-10-21 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea3b99e2-3733-380a-bc92-926e600d855c | -3.02057 | -54.34874 | 2024-10-21 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3ee57ef2-6190-3d52-becb-601d34809f8d | -3.00208 | -53.04867 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ec322a48-9de3-336b-9349-7d024b58b968 | -2.99406 | -53.03711 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9536b2f5-97cd-3606-8788-e68449fd320e | -2.99254 | -53.04737 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| cda1ce2c-92d4-3a2c-b760-7aa4e2583d3d | -2.95488 | -52.90398 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 670e385e-1048-3be1-9202-f1d88d8f1fdc | -2.94979 | -52.90835 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 092e5485-36b9-3ae8-a7ed-4348cff10365 | -2.84825 | -53.33098 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 4b6b90d5-92b2-3f86-8cf5-ce316a998cdd | -2.84679 | -53.3409 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b2be4aea-6399-3b8a-8069-a8b58d875070 | -2.83889 | -53.32963 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| a815def1-ac2e-3468-bba2-44f5b29621a1 | -2.82486 | -53.00018 | 2024-10-21 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 80538475-f82a-31af-bfbc-60949a9a80f3 | -2.80253 | -51.35415 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3c7e4fda-4cbf-35f3-b07a-38c793162f33 | -2.80059 | -51.36723 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 11dc8c32-bc9f-3821-938b-5096b044a27f | -2.79187 | -51.35262 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1629ca33-cf97-32c6-82bd-164fec71727c | -2.78994 | -51.3657 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| aa27d0e7-5a90-34aa-a1b6-a920839cd685 | -2.78043 | -49.29485 | 2024-10-21 05:59:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 7b8d42ea-7012-3030-b31f-de9fffc7937b | -2.7537 | -54.03193 | 2024-10-21 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2d60d0d3-06d9-368c-8787-3d4ae9895903 | -2.7179 | -54.77307 | 2024-10-21 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36bc0bec-1e11-3a56-87ee-ea4df827a25d | -2.56304 | -54.01089 | 2024-10-21 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b020dbe3-f71a-30b9-94b4-5a4b188fd6aa | -2.48091 | -49.09871 | 2024-10-21 05:59:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 39bc4b9d-11ea-3159-83f2-3c1fedb021bc | -2.47882 | -49.11105 | 2024-10-21 05:59:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| cbaa493d-3204-3491-afd2-2125d61b4425 | -2.36552 | -52.51523 | 2024-10-21 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dfac3b93-a94c-3cb7-aa16-67ad6021a658 | -2.36296 | -52.51931 | 2024-10-21 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fc134858-4c47-3365-83de-c5642320e0c1 | -2.26953 | -53.75284 | 2024-10-21 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bc16852b-0515-31e7-b175-1bf3bb0bd5b8 | -2.22261 | -50.45682 | 2024-10-21 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 400be433-6ece-3469-b397-d7807fd18a52 | -1.93377 | -52.09958 | 2024-10-21 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9ffaf8ef-513a-3238-81fe-b82fb3279c86 | -1.93209 | -52.11092 | 2024-10-21 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e3726643-dade-3043-ad3f-e84f009c9b7c | -1.19788 | -53.63519 | 2024-10-21 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| efbc807f-9325-3d7e-816a-d91a8cd912ba | -0.18437 | -51.53629 | 2024-10-21 05:59:00 | AQUA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 775fd9d3-6e5f-3119-bb40-6a9b15851aeb | -1.19017 | -53.62445 | 2024-10-21 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 32c0af42-a2a6-36d7-8951-d603b156ac21 | -11.87257 | -56.88179 | 2024-10-21 06:01:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ccc1122d-1d49-35b4-8fdc-c53c36bdfa67 | -11.8638 | -56.87397 | 2024-10-21 06:01:00 | AQUA_M-M | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fa16ed3d-4176-3c19-82f0-03bc16acb294 | -19.5595 | -56.61906 | 2024-10-21 06:03:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 52114cbc-945c-3814-9e17-ec0ff2577215 | -19.54995 | -56.61766 | 2024-10-21 06:03:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 78bbe78e-1792-34cf-9a2a-40fae2d3a18e | -19.54705 | -56.63948 | 2024-10-21 06:03:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 62833231-4efc-3fab-b4c5-0cced25cfd60 | -19.5456 | -56.65038 | 2024-10-21 06:03:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| b3a29690-1052-3a67-aa6e-cc769b25b4ac | -19.54162 | -56.64411 | 2024-10-21 06:03:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 6b7a5976-a00b-3837-8aa8-70229ab431af | -18.29807 | -56.1861 | 2024-10-21 06:03:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| c740ef38-5f56-3f55-86e2-052877dbeeec | -18.29293 | -56.15154 | 2024-10-21 06:03:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 541d7d6c-f038-31a8-89b1-7f084585fe8f | -18.29143 | -56.16261 | 2024-10-21 06:03:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 1c95c4a1-76c3-3d0a-be2a-27e0070936e5 | -18.28109 | -56.09316 | 2024-10-21 06:03:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.3 |
| a38eeeca-d3ed-3b51-9e28-c3a9435fea0c | -18.2796 | -56.10431 | 2024-10-21 06:03:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.9 |
| 8dd5f621-56c2-378b-acee-29e77b12b45d | -18.27141 | -56.09175 | 2024-10-21 06:03:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 3802fdfc-8fba-3145-8a3e-6d356b094432 | -18.01401 | -57.3003 | 2024-10-21 06:03:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 05b9227b-cc9b-300b-86df-53c074df465f | -17.70614 | -57.45424 | 2024-10-21 06:03:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 380c7e9a-9737-31f8-9629-5b7b3ebe310a | -17.70477 | -57.46389 | 2024-10-21 06:03:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.0 |
| 28b32ebf-7645-35a1-9820-66cf7bb9bf7f | -17.69076 | -57.43216 | 2024-10-21 06:03:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 219efa59-18d3-3661-9de5-85678beeb68d | -17.24908 | -57.30392 | 2024-10-21 06:03:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| a22286fc-0c4c-370d-86d1-867d256923ec | -12.52207 | -63.30287 | 2024-10-21 06:03:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| bfdfa85d-9fcd-3f1e-bcaf-6c52753bf9c4 | -12.51844 | -63.29516 | 2024-10-21 06:03:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 77ef7728-aca9-3c8b-9b83-6bbdab8ed01b | -12.51555 | -63.31253 | 2024-10-21 06:03:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 200b2470-92bb-34f7-a63d-d24bdd92bf9d | -12.51009 | -63.30075 | 2024-10-21 06:03:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 8e543b8b-f13f-3d23-a4a0-b38eed3632bf | -12.50647 | -63.29302 | 2024-10-21 06:03:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 6ac34332-d7c9-3374-adf0-802d839fdb21 | -7.8816 | -63.77901 | 2024-10-21 06:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 557ef28c-0961-3f0f-8cd3-09b0ac85e86b | -7.87544 | -63.77818 | 2024-10-21 06:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc1c3275-9d5b-3084-95c0-fc88a145613e | -7.86863 | -63.78214 | 2024-10-21 06:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35f0ca0f-62fe-366f-900a-2cd4caec2a3d | -7.86245 | -63.78135 | 2024-10-21 06:18:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ec86777-da86-3081-b56b-536fca75e678 | -9.76705 | -64.71915 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 027f024f-1803-31af-976a-9ba4b5bdcbcb | -9.76652 | -64.72352 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4849943f-5b45-3375-b8a6-b83921852484 | -9.76599 | -64.72788 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cb184cb2-ea57-34c5-983b-40c034e81130 | -9.76358 | -64.71969 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3051da7-3883-3b21-bbe3-d9494f4d9fb0 | -9.76301 | -64.72408 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a5e0890-9920-357c-997f-c26d7657909c | -9.76245 | -64.72846 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8bcfc1c6-037a-3be1-9e4d-1f7ecf5d1eac | -9.76057 | -64.72264 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b9887ded-86de-3db5-91e7-a49a3537ab28 | -9.76004 | -64.72702 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3bbfd87-f131-3666-b7fb-ea5fd598414a | -9.7595 | -64.73147 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7192cf04-914d-3f82-9330-f8b08d46550e | -9.75707 | -64.72321 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5837751c-60c4-3f28-9095-1e73b3187a87 | -9.75651 | -64.72755 | 2024-10-21 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9f5c79ea-e40e-366b-89ea-c5e34d9e0ad7 | -9.37562 | -66.48892 | 2024-10-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 830d1aeb-3425-3051-a477-a6e14bf88050 | -9.3752 | -66.49218 | 2024-10-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6861bf0-15e1-3045-b71a-03bc51c124ee | -9.37077 | -66.48501 | 2024-10-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ddf8937-4797-33c7-959e-47eaa95a5b49 | -9.37035 | -66.48823 | 2024-10-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 07bee3d9-4f5e-33b4-9079-1d0f678673e5 | -9.36992 | -66.49149 | 2024-10-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| beaa108c-24e5-3033-b8d0-08702bccfed1 | -9.36507 | -66.48754 | 2024-10-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5964863a-e70d-313d-a036-05a800e2b856 | -9.36464 | -66.49078 | 2024-10-21 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecea3837-212d-3ac6-976d-148f1e90ecb1 | -7.36992 | -72.87082 | 2024-10-21 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aabf9025-31cc-3944-8b65-15900ca8b6c9 | -7.36934 | -72.87461 | 2024-10-21 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7fdf389-54c8-36bf-9ebd-0ed9bbf00d68 | -7.36302 | -72.86978 | 2024-10-21 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ccdfe3c-76b7-3928-861f-7b8c12e331e2 | -7.35957 | -72.86926 | 2024-10-21 06:20:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbbac395-b494-3baa-a650-5b478f74c835 | -12.53261 | -63.03056 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9da23f6f-67e8-363c-8a43-6d86f0e16486 | -12.52578 | -63.02975 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5114dfb3-a3d8-3c37-ac83-78e798ca289e | -12.52363 | -63.0486 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c93180f9-2705-32ee-8466-1613115ebc6b | -12.51818 | -63.04988 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73fd2858-4d12-3313-bb9c-65fc0ba346ec | -12.51681 | -63.04783 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9024921-ccfe-3156-b707-41d474faae4f | -12.51135 | -63.04909 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6bf31ff-2386-3edd-b87c-5ccc19cd4008 | -12.48026 | -63.18829 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e70ff673-6103-3137-810a-f05513c05b49 | -12.47957 | -63.19443 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cee9978e-2d11-3ac4-87ec-aef6dce1d682 | -12.00814 | -63.51708 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e1b2c2e8-62e5-32f3-bc3d-3aadc275b4b4 | -12.00642 | -63.519 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b8b4abc2-20e2-3f00-a0fb-ff8b51428317 | -12.00088 | -63.522 | 2024-10-21 06:20:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efdc1443-634e-3dbf-945b-c5b0be683cfe | -10.52681 | -62.61824 | 2024-10-21 06:20:00 | NOAA-20 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 751bd75c-5405-3b46-94f5-745f357a60d5 | -10.20718 | -64.83881 | 2024-10-21 06:20:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87073abe-17cb-3e62-be8c-93f3d2f4ac00 | -10.20665 | -64.84309 | 2024-10-21 06:20:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78a12e8a-f305-3313-851f-16b1f45a0ecf | -10.20124 | -64.83794 | 2024-10-21 06:20:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a11b1932-d998-321a-9416-a06fd26b1aa3 | -10.2007 | -64.84232 | 2024-10-21 06:20:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README63.md)
