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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e628908-ba05-35f2-b108-c86319ae2071 | -2.2636 | -53.74743 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21656a63-3a9d-3d1c-b57c-f707fdc90dc9 | -2.07194 | -53.28983 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48a0886d-90b0-3298-ba72-b469e39b2025 | -2.22678 | -53.66146 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4377179f-582f-38c6-9f19-345e40df8651 | 0.62556 | -60.08683 | 2024-11-11 05:35:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ddbd17d-5adb-37e0-9b1f-ebcc99462c50 | -1.71811 | -55.16334 | 2024-11-11 05:35:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 12960451-37bf-34e6-81d9-afee4a92c6cf | -2.16901 | -56.65151 | 2024-11-11 05:35:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbca6295-26cb-3ee1-b298-cba6b94998df | -3.10604 | -54.29451 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c8deb58-8d09-315b-83e7-8c651648c4c3 | -3.02595 | -50.97507 | 2024-11-11 05:35:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7e67be17-2c32-3b3b-b60a-1fc48cf4cf03 | -2.07139 | -53.2934 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2765cfbf-589a-345e-a250-d011db987a52 | -3.62644 | -54.70589 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6be9ae6-3318-3060-b298-19200d6d6517 | 0.86688 | -59.61461 | 2024-11-11 05:35:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ebabac1-1387-3706-883c-bfbd06342032 | -2.23707 | -53.66647 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4da4d7b2-fca1-30f6-9dd2-5fd56377dde0 | -2.23218 | -53.66225 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 400b3b38-7649-3454-bfe9-002dc2e85584 | -1.62941 | -52.53026 | 2024-11-11 05:35:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f6f85ece-38fa-3107-a979-2d1e5cb36318 | -2.82041 | -54.00732 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc4fd540-53cd-3d18-9444-f6aebf68f3db | -1.39931 | -55.45089 | 2024-11-11 05:35:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2314db85-dc5a-31b9-b81a-824b06e77717 | -4.28229 | -50.66811 | 2024-11-11 05:35:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1889d4e4-15af-3fd4-ae27-8737eff49451 | -1.20158 | -53.70111 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da6c6381-2c07-363b-84fd-532aed12859e | -3.70514 | -54.64914 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df43a53f-d8d7-36df-a516-979cbc5989de | -1.32539 | -54.60492 | 2024-11-11 05:35:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90547761-b9f2-365f-b87c-6d3452a7ee64 | -2.22431 | -53.67842 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15314254-6544-3df5-9b22-61b8e11a59a4 | -2.23369 | -53.67089 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0ace2815-39d3-35d8-a5cd-7f6da85d0933 | -3.10033 | -54.29688 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 702ef3c9-44fd-33a9-b849-096655961ab5 | -2.81558 | -54.00318 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06df15f9-3202-3cb0-b712-e003fa99478c | 0.62497 | -60.08305 | 2024-11-11 05:35:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eea82140-8703-3791-bfed-f4b71c9aa4be | -3.70041 | -54.64534 | 2024-11-11 05:35:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52e63180-35dc-3e0b-b4ff-f3ec250ae149 | -3.5251 | -53.50065 | 2024-11-11 05:35:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 840babe8-784c-3073-ad0b-9fdcbae53fea | -3.89956 | -58.62469 | 2024-11-11 05:35:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6de628a0-a95e-3837-9f90-1b6af9480bb2 | -3.45618 | -51.58006 | 2024-11-11 05:35:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 766919a0-30b7-3fe4-82f5-a75f701fd68f | -2.85327 | -54.0056 | 2024-11-11 05:35:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d3491fc-4347-376e-ab0d-1d01727b5c15 | -3.10557 | -54.29767 | 2024-11-11 05:35:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a175270-8c70-3e62-ac94-a2087f4a974d | -1.54448 | -55.87848 | 2024-11-11 05:35:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d3cfda0-3e29-3a16-96a9-580ee47601b1 | -9.92843 | -59.90276 | 2024-11-11 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c5963852-e158-3f81-9a30-5dce16f4c614 | -9.91907 | -59.91178 | 2024-11-11 05:37:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 196c35b8-ce04-342f-827d-1c4561e2804e | -9.76832 | -63.96682 | 2024-11-11 05:37:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4e11e3d-4285-36b9-a8d6-99cfa2a348d2 | -3.0295 | -50.9815 | 2024-11-11 05:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d212fac2-76b3-3082-a1d2-e6d9365c2065 | -2.2482 | -53.6619 | 2024-11-11 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 71cc22cc-3e6d-3d2b-8f06-6f4eebfae4ad | -2.7587 | -49.3497 | 2024-11-11 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 7e38aba6-c76d-36ce-b8b1-683ebaec2d59 | -2.2663 | -53.7422 | 2024-11-11 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| c72bd4da-ce82-3898-8ad8-43497c156c4d | -2.2298 | -53.6623 | 2024-11-11 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| e694a685-d349-3b51-9b26-0a59ae1bb4b9 | -2.248 | -53.7426 | 2024-11-11 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| cda0a761-3fca-3f18-a188-0754e7b280db | -3.1458 | -54.4859 | 2024-11-11 05:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b884e3cc-ebbb-321a-a0a9-fdef7a5a47cd | -2.7402 | -49.3502 | 2024-11-11 05:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| f2714be7-be36-393c-84c6-9b5efb5d99c8 | -3.128 | -45.2285 | 2024-11-11 05:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| ed694198-40a2-3491-a9ed-d331317477cf | -3.1094 | -45.2293 | 2024-11-11 05:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 105.8 |
| e7b34db3-2761-3cf8-801c-240e43177d04 | -2.2297 | -53.6824 | 2024-11-11 05:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a246ec01-8653-3586-8722-79e9a0e73021 | -17.25218 | -57.48193 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1727276a-7784-35d6-ad94-611d0a6ae2f6 | -17.24051 | -57.49335 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a2bb8a3d-8ce9-320f-a3ea-04eb3afc6fa7 | -17.68011 | -57.51548 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c934a2d6-8eea-341b-b12a-91e327295b92 | -17.26179 | -57.48963 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 46ac3ed4-123d-3664-9dca-c3d7ffa7e698 | -17.59327 | -57.52785 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| a349d9f1-2206-342c-a3ae-8ff3c03e759e | -17.64007 | -57.53054 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 2757b8b2-b66a-34fe-b331-a09d18b86f35 | -17.2934 | -57.48723 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 8f0a4fd6-f0b9-3e54-8b77-80c25b0a3b30 | -17.29996 | -57.47512 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 511ac62e-4759-3612-8eb3-5f61a270f426 | -17.62417 | -57.43689 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 63a883d5-9919-3721-acd5-0d9d1b9aa2d4 | -17.24737 | -57.47808 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2ecea1e2-441a-37bb-9606-84809329e09a | -15.99912 | -59.36255 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| aaf6911b-7d51-3bad-a6ac-22646a4a2333 | -17.58818 | -57.42897 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9467f052-ee85-3b81-b67c-1bc4cf905bb4 | -17.24512 | -57.47999 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b7c58f79-9b9b-30f0-823d-c207a6788d90 | -17.25183 | -57.48512 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| ff94094d-3c56-3d1a-a575-5c2da047151f | -17.76909 | -57.51699 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 6136b5b0-7e97-3b86-857d-2787cf8bf3c0 | -17.64559 | -57.52797 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d59dfe5b-0279-3fd6-a313-a0a1efc02b6a | -17.24017 | -57.49653 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6194b767-e085-3a6b-b081-4f1861cf6f00 | -17.66904 | -57.47149 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 73f4d381-d690-3720-bc04-88a19b308959 | -15.98182 | -59.35553 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0601d981-d3c9-3af1-a0db-0dad472f4102 | -17.61872 | -57.53434 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 77fd262c-9d60-3ee8-b91c-8ca9142a208b | -17.29269 | -57.49361 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8179a562-211d-3011-85dd-3f3f381153d6 | -17.61827 | -57.44272 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3780d241-6a68-31ef-b3e1-1fee38b4a921 | -17.30264 | -57.49811 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| b53b5fad-8c19-3edc-b890-15f0d66eb162 | -17.27689 | -57.49481 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 08bd5a89-ae29-3029-b4e5-406cf4070fe1 | -17.59397 | -57.52143 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 8dbd14ba-1dde-3416-bea1-5ecb04517a38 | -17.60305 | -57.43748 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 726778a4-81b9-34ef-8606-52205fa3ef3c | -17.29481 | -57.47446 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 0b7d5e32-7007-3049-8fc8-dde9f37ea88c | -17.60805 | -57.53622 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 332f0ed1-47b6-3c83-b691-68de965d792e | -17.60534 | -57.51311 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| a8b66e98-7a5b-37d1-a89d-97e894dfc504 | -15.99407 | -59.36666 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c58e2eb-cee2-36b0-b8c1-658398fcb54e | -17.60053 | -57.50924 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 4bb191a4-f1a8-3ce7-8ce7-870d9fe53e6d | -17.36183 | -57.43747 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 229be8bc-b111-3cf6-8f31-c4c04ec8be69 | -17.35853 | -57.43604 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cdab1c9f-3e0a-3fb0-9ffd-65b9fcb33e13 | -17.30299 | -57.49493 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bd805387-ed64-3ee5-839f-98855a25ed85 | -17.25664 | -57.48897 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d21d04c1-a774-3130-afc4-847d04d91c23 | -17.27759 | -57.48844 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| f81782b4-d449-330b-a780-65c9d171fa41 | -17.61863 | -57.43947 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d0cf50b9-173c-3524-b7c3-293acf08d85e | -17.28309 | -57.48591 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 0a7149aa-5061-3ad5-86e2-9a73d7cba7f0 | -12.78518 | -62.03329 | 2024-11-11 05:40:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e6201947-b73f-304d-9d60-20166224cc87 | -17.27794 | -57.48525 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 52487fb0-b6c9-333e-b814-8a737e2357d5 | -17.29516 | -57.47126 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 01e7b800-317e-3c94-b207-92fcada6fedd | -17.28379 | -57.47953 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d609c870-a8b7-362a-b2a4-4ae8063f2379 | -15.99699 | -59.3429 | 2024-11-11 05:40:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0b5c0580-7d4f-3e56-bbd2-f6deefa7f47a | -17.30067 | -57.46872 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 169c1770-bb63-3b4f-b6f4-bef6e3d03e12 | -17.62974 | -57.52924 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 186776b7-9cc5-3cd3-be52-c39eb54a4a5a | -17.6132 | -57.53688 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 431986c9-6b30-3eea-a073-85f8f00c615e | -16.93939 | -57.65445 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1661be71-2817-3cc3-ab85-77777bc13a62 | -17.35818 | -57.43926 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c68260cb-e1e2-3229-97be-238d236d43c3 | -17.64042 | -57.52734 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.2 |
| 8e6ec966-589a-32fd-b9f2-4e5f1946d4e5 | -17.6301 | -57.52604 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cd8c28d6-702c-3c51-a5e7-8f0735d6b1b0 | -17.24702 | -57.48127 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 2745431d-f7c0-3782-be41-511ae7d04fd0 | -16.93973 | -57.65137 | 2024-11-11 05:40:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4d8c7c7c-7d72-3cc5-88fa-0a70bf226834 | -17.59822 | -57.43356 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 9a8e6c99-bd32-3992-8004-559894c5ca96 | -17.59808 | -57.53172 | 2024-11-11 05:40:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |


[Clique aqui para ver as próximas entradas](README45.md)
