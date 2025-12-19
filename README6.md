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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90303966-17f3-388a-bf08-a01e5bdff003 | -18.83623 | -51.61346 | 2025-12-19 05:12:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f566c393-7e9f-32ff-8f3e-a99cd6482e38 | -23.74467 | -55.39587 | 2025-12-19 05:14:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 358ac66f-333b-3139-86c6-da3e696e1e54 | -21.00357 | -54.47519 | 2025-12-19 05:14:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ff816f9-0634-3578-9387-efd5f68f3662 | -20.20276 | -54.76251 | 2025-12-19 05:14:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 89dced56-1c48-3dce-8139-e1cc59337741 | -21.19999 | -56.93491 | 2025-12-19 05:14:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 447ccdfa-8001-3cdb-92d1-f55bf79411b8 | -28.88889 | -50.47742 | 2025-12-19 05:16:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f4c64509-bfc9-3986-8146-1a3fb47d18e0 | -28.88918 | -50.47361 | 2025-12-19 05:16:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ecf71cbe-aae1-3f19-8373-d263bddf3c10 | 3.22559 | -61.19345 | 2025-12-19 05:29:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb5871cd-9523-3049-b8f9-208f2d18ba84 | 0.46111 | -60.42711 | 2025-12-19 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23ad8079-10d7-393d-96ac-b04538f75c15 | 0.46003 | -60.42024 | 2025-12-19 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e532cc83-512b-3c24-9bc1-8c222fe15450 | 3.80451 | -60.48895 | 2025-12-19 05:29:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77944439-e0d8-365f-8d79-127763cb3b59 | 3.22893 | -61.19294 | 2025-12-19 05:29:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76928fdc-35b2-312f-9056-25d5daa8e0b5 | -2.10942 | -50.91331 | 2025-12-19 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d7a10dd-210c-3639-8727-b889ad06545d | 4.13298 | -60.11646 | 2025-12-19 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70e8211c-57b4-3e6a-8db4-a173b6027ad7 | 4.13244 | -60.11301 | 2025-12-19 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aabaa944-0994-3de8-8f3f-0a032d765d05 | 3.18107 | -60.60819 | 2025-12-19 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7d4b9e0-1b2e-3ff3-a0ee-aa5004404005 | 3.90803 | -60.15501 | 2025-12-19 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0771d80-91ce-3913-89ca-1c2fb3d4a68b | 3.18823 | -60.61061 | 2025-12-19 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbf046ea-311a-3c8c-be9c-86e34c37ce04 | 3.18878 | -60.61406 | 2025-12-19 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fc0aa9a4-688d-3fec-a5b4-883fc1687de0 | 3.90473 | -60.15553 | 2025-12-19 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43955d89-c912-3a7c-bb8c-e89cc1496f2c | 0.46057 | -60.42368 | 2025-12-19 05:29:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c13e2432-1d42-3852-89a1-a85fc2668f9f | 3.51531 | -60.07631 | 2025-12-19 05:29:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af93080a-6a21-3de8-9028-ad5c57cd64fc | -2.11003 | -50.90926 | 2025-12-19 05:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2ace3bd9-f983-3554-81a9-9b564b30bfbc | 3.18438 | -60.60767 | 2025-12-19 05:29:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33aa138c-9c2b-340f-bab4-c2fde9df7377 | -18.83901 | -51.62556 | 2025-12-19 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b1bc2b37-f491-3edd-809e-ba818d48a787 | -18.83961 | -51.61868 | 2025-12-19 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fcbe5382-0aff-3085-8636-9bf9fde542a2 | -18.84018 | -51.612 | 2025-12-19 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a000a35a-5ac8-356d-a814-bbe8ecb4090a | -18.83218 | -51.62484 | 2025-12-19 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4ae8a378-bb72-322b-909f-2f1b12bf7200 | -18.83159 | -51.63165 | 2025-12-19 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e587e158-1be2-362e-a59b-d0e7426892e0 | -18.83842 | -51.63236 | 2025-12-19 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f0ac3999-1948-3274-8e18-ef82164cd43e | -18.83785 | -51.63898 | 2025-12-19 05:33:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3a95b50c-c761-3704-b706-c22c4c676af4 | 3.18004 | -60.60509 | 2025-12-19 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a90a859-cb4a-3dc3-b847-c8be809090d1 | 3.18116 | -60.6057 | 2025-12-19 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fe76c734-9dc7-3898-bcb0-aaeb47ae50bf | 3.18737 | -60.60931 | 2025-12-19 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8aea4ed3-dd26-3b13-94cd-8967df525d4e | 3.18853 | -60.60993 | 2025-12-19 06:18:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2f9bfc8-b689-380e-88a2-6e17c2a1b0e5 | -18.83969 | -51.61568 | 2025-12-19 06:52:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 9b00ecf2-6ce4-3903-a708-32989dccfa63 | -18.82635 | -51.62159 | 2025-12-19 06:52:00 | AQUA_M-M | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 14986e38-911f-3eb9-a3e3-0e50a9f5e0f9 | -7.63865 | -35.57434 | 2025-12-19 11:17:00 | TERRA_M-M | NATUBA | PARAÍBA | Brasil | 2509909 | 25 | 33 | nan | nan | nan | Caatinga | 8.8 |
| c3e730ed-eb29-3da2-a590-0f53a97064d4 | -6.7611 | -35.21316 | 2025-12-19 11:17:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 5fcea682-c3e9-3864-a85f-1e92f6a0317d | -7.6479 | -35.57526 | 2025-12-19 11:17:00 | TERRA_M-M | NATUBA | PARAÍBA | Brasil | 2509909 | 25 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8631f50e-474f-34e3-953b-478fc77ae645 | -6.63529 | -35.31519 | 2025-12-19 11:17:00 | TERRA_M-M | PEDRO RÉGIS | PARAÍBA | Brasil | 2512721 | 25 | 33 | nan | nan | nan | Caatinga | 11.5 |
| ba410152-3d7c-3288-b77b-4ca0265f61e1 | -8.21574 | -37.57897 | 2025-12-19 11:17:00 | TERRA_M-M | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |


