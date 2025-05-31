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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c20e9c6-4a5e-3459-9540-31de1c79671d | -12.0212 | -49.523998 | 2025-05-31 00:38:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b843282e-1edd-37ae-b7a7-14fa214d953d | -7.2159 | -43.122101 | 2025-05-31 00:38:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e5d029b1-4310-3b37-becd-23b0b5b4bd16 | -13.0874 | -45.2813 | 2025-05-31 00:38:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 47a918ad-bfe0-326d-b4a6-fd28470fe8ee | -12.4567 | -54.914001 | 2025-05-31 00:38:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33eba019-93e0-3732-8f05-7dc34dfecbe8 | -10.8298 | -56.9505 | 2025-05-31 00:38:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2eb6508-b6c4-3be7-882e-5784a8563707 | -8.81531 | -49.84242 | 2025-05-31 00:39:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 00bd0e47-c356-37e5-abb9-8192aa128353 | -8.20404 | -49.80336 | 2025-05-31 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| d49321d0-822b-3f6b-897d-a1ef39b5e2fd | -7.25013 | -43.09455 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| ede78320-87b6-33a3-8433-3d4f0bb2f98b | -7.24779 | -43.08642 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 24.2 |
| 133bf1f3-52cf-376e-919a-074d2595bafa | -7.18977 | -43.22865 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| d8fe2c72-1206-3e02-a682-ea310e517875 | -7.24028 | -43.26465 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 89eb91f5-452d-315a-a3e2-ef0b639d3b0f | -7.22093 | -43.13542 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| d560eae1-37fd-3e28-93cf-cf14c93c6f8f | -6.56031 | -44.48446 | 2025-05-31 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 5193cbac-d506-3e81-a147-c3cc58e1c5c5 | -7.21875 | -43.12083 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 7d1162b3-48c8-3dbb-8bbc-0754567219e5 | -7.22714 | -43.25204 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.4 |
| ccc9afc0-ce91-3cf0-8d01-eba4f282ef14 | -7.22988 | -43.11918 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 9d12d2d9-2dbe-3601-a56e-dd5a9386d289 | -7.0087 | -44.60803 | 2025-05-31 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 33594771-7c25-358f-8e84-e5edaccd331c | -6.21621 | -43.34206 | 2025-05-31 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 2b613cba-a7e8-358c-ae54-33fdb1fddaf2 | -6.56204 | -44.49612 | 2025-05-31 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 8568d529-efcf-39cc-8092-40cffd0d253a | -4.48976 | -47.79157 | 2025-05-31 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 44d19372-dc52-3ae1-8645-913b9c99603b | -6.17918 | -48.07107 | 2025-05-31 00:39:00 | TERRA_M-M | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4209c79a-524c-34c1-ba64-83983b2f4eec | -8.47959 | -49.60908 | 2025-05-31 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| b1363cd8-70b3-36e6-88cb-b985bb5d59e9 | -7.87829 | -45.99224 | 2025-05-31 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 64cc6510-9882-3afe-9019-36cd664efade | -8.47029 | -49.61033 | 2025-05-31 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a39eb8b1-aeca-3de4-acbb-e31525d5d0d7 | -7.58339 | -45.86732 | 2025-05-31 00:39:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 1f6b7364-8706-3274-ae0f-a678b5bd74fc | -7.23882 | -43.10277 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 5e0c80e7-f43d-3d52-b861-e345b9e76f10 | -7.17873 | -43.23025 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 50ec059d-b387-38f6-85be-a67477d629e6 | -6.83175 | -44.65891 | 2025-05-31 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| bcda1cab-a7ff-3928-9594-b710650a1129 | -7.23204 | -43.13375 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 6d787013-362b-34dc-b943-b1755ea22ead | -6.54704 | -47.80585 | 2025-05-31 00:39:00 | TERRA_M-M | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d5c65250-6acc-34a4-bb68-604c384cd57a | -7.22928 | -43.2663 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 20073e3a-8745-370c-a817-a7e1a6448bd8 | -6.15573 | -42.62243 | 2025-05-31 00:39:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| 7cdf7a2c-99c1-3fc9-97cf-ab8a1329465e | -8.46898 | -49.60042 | 2025-05-31 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 521366c1-5749-31b7-a65c-7e265fd90008 | -6.15331 | -42.60603 | 2025-05-31 00:39:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| 4f7e05e8-bf0e-32be-a47a-838fdf80d06f | -7.01036 | -44.61958 | 2025-05-31 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 4623e246-8408-368b-ad90-050dff6a69ea | -8.19468 | -49.80465 | 2025-05-31 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 90144665-94a8-374a-96a3-f53aaaa59d93 | -7.18893 | -43.23451 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f3ee0616-f0e0-3400-9d97-cdf7d9c94d5b | -5.85685 | -43.6457 | 2025-05-31 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| dc5c15c0-92e1-3a0d-9828-abf1b7d14f38 | -6.83006 | -44.64713 | 2025-05-31 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 7a9cc3e2-e511-30af-8b1e-eed83235de18 | -8.47827 | -49.59913 | 2025-05-31 00:39:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 11ebca8d-8f6f-3eb4-a17d-72864e592b6a | -7.01201 | -44.6311 | 2025-05-31 00:39:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ecca39a6-8c47-3e36-beb2-2757547331a5 | -6.20507 | -43.34359 | 2025-05-31 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 51924869-0c59-344e-92a4-21e1580bed92 | -6.20288 | -43.32909 | 2025-05-31 00:39:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 1d6bba24-f75b-3925-afac-eaca0d076670 | -7.24995 | -43.10106 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| c689af6e-2344-3b23-bcca-ded296d2c2f8 | -7.23664 | -43.08809 | 2025-05-31 00:39:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 2776c282-6192-3f3d-8c70-f0428d8dc6e9 | -7.2403 | -43.1134 | 2025-05-31 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 574c1934-7d9a-3676-b885-5a76ddb80994 | -11.8368 | -51.2641 | 2025-05-31 00:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 135.7 |
| c4ec4755-e4a2-37f8-af2b-a8784adc5f3f | -12.0157 | -49.5054 | 2025-05-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| a6fb0bf5-7b58-35d3-8993-9597e524d4ff | -7.2405 | -43.0899 | 2025-05-31 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.0 |
| ee34a80b-6891-316e-af03-750f4bab9852 | -10.462 | -47.9428 | 2025-05-31 00:40:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 07508bbc-61aa-32e9-aed1-bcf591e8c423 | -11.8558 | -51.262 | 2025-05-31 00:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 55.5 |
| bfb7f41e-558a-3596-8bbd-5218fe36e265 | -10.6489 | -49.4483 | 2025-05-31 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| a2753f03-e617-3fd1-b7d8-bdd171435a43 | -13.1068 | -45.276 | 2025-05-31 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| f0ad581c-666b-378c-8d9c-da498eacb04d | -12.0345 | -49.5248 | 2025-05-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| b2359df6-4dd2-36db-bf6e-c3cc60ece80a | -11.8365 | -51.2854 | 2025-05-31 00:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5b1bcc03-e9f8-3b40-b77b-71dfb440eeb2 | -12.0154 | -49.5272 | 2025-05-31 00:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 169.7 |
| c74b6cb1-b2dd-3140-9136-97fb06c0013f | -10.6492 | -49.4267 | 2025-05-31 00:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 111.9 |
| 5428924d-1007-3e87-994b-bb4f6ddfbe8a | -11.8365 | -51.2854 | 2025-05-31 00:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| fdc1a3f5-2ecd-39b6-a11f-c1d9c3673f70 | -12.0345 | -49.5248 | 2025-05-31 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 7727a998-4c5a-3a26-9bb2-ac8665716034 | -10.6492 | -49.4267 | 2025-05-31 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 751df267-75da-3625-a0a9-7ab0eef0e099 | -7.2403 | -43.1134 | 2025-05-31 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 66.6 |
| 2cddfc03-5f66-3505-bf96-ce1b441f57ca | -12.0154 | -49.5272 | 2025-05-31 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 34578081-e92d-31a9-adce-b8600eefa9f9 | -10.462 | -47.9428 | 2025-05-31 00:50:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 9aba9977-9265-33da-be36-fb4303e92e5d | -9.4964 | -40.3088 | 2025-05-31 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.8 |
| 1f567f3f-4f6f-3c30-a551-7b4ba4826cc4 | -10.6489 | -49.4483 | 2025-05-31 00:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 8800ddb4-0821-381a-9923-6ea66ffcafbc | -12.0157 | -49.5054 | 2025-05-31 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 0ccfb912-87e4-3133-b9fe-7eef7896a358 | -11.8368 | -51.2641 | 2025-05-31 00:50:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 65a0c65f-8dd8-37f9-8708-6d7742b52138 | -7.2405 | -43.0899 | 2025-05-31 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| e5bf4133-eae6-336f-8456-50d0e2337454 | -11.8368 | -51.2641 | 2025-05-31 01:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 62ac3c5e-909d-3669-8b33-73122890625a | -11.8177 | -51.2662 | 2025-05-31 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 8f789e42-c11d-363b-a550-a4fc3f1e3168 | -11.8365 | -51.2854 | 2025-05-31 01:00:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 9082f0c3-d516-37c0-98c3-c11a0f6d43c6 | -7.2405 | -43.0899 | 2025-05-31 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| c33a6a95-d7fa-396a-9401-54c0ef0ddac2 | -10.6492 | -49.4267 | 2025-05-31 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 3c0a3efc-c20e-3b59-b974-c8b510d7d248 | -10.462 | -47.9428 | 2025-05-31 01:00:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8b970309-76ee-3797-b235-be48332daf8e | -12.0345 | -49.5248 | 2025-05-31 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 4e1b456e-2a39-3382-8dee-08d6f37a7e6d | -12.0154 | -49.5272 | 2025-05-31 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 125.4 |
| eaee93b2-99b8-3bdb-93d3-11223e190f95 | -10.6489 | -49.4483 | 2025-05-31 01:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 6cfea60b-c8e0-3cfd-b2d9-f7927a40da26 | -7.2211 | -43.1388 | 2025-05-31 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| 8fa60706-de0e-3f4e-a811-da4aef1e2ba7 | -12.0157 | -49.5054 | 2025-05-31 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| a7fae9ff-869f-3197-a081-fd28ba038746 | -10.6489 | -49.4483 | 2025-05-31 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| b0a01086-80a4-3d09-b808-fa12efd0cde9 | -11.8365 | -51.2854 | 2025-05-31 01:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 29aa30ff-f090-3e38-a168-5526fd91be74 | -12.0345 | -49.5248 | 2025-05-31 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 89c93a53-c8bc-34e5-91e4-3b70e9b68f2f | -10.462 | -47.9428 | 2025-05-31 01:10:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| ae3cdc8e-7fc4-398b-95d8-a017b0b76732 | -12.0154 | -49.5272 | 2025-05-31 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| 345515e2-abdc-3fd3-a3b7-2a4b3e22a56d | -10.6492 | -49.4267 | 2025-05-31 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| c012ed9a-5f65-3e4e-9fa0-4e571c789e25 | -7.2405 | -43.0899 | 2025-05-31 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 7f3c8df9-8493-3893-80cb-4ca76408340c | -11.8368 | -51.2641 | 2025-05-31 01:10:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 8274ef33-2205-3a37-a820-83202a99bb4f | -12.0154 | -49.5272 | 2025-05-31 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.8 |
| 0e01665c-2c2c-3fe2-a290-023d047b0cbc | -10.6492 | -49.4267 | 2025-05-31 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 8bdc0ade-4f3e-3a14-a2a7-bb08b849c534 | -7.2211 | -43.1388 | 2025-05-31 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.8 |
| f976b13b-d5ef-336e-95f9-0afb8e2b8a86 | -11.8365 | -51.2854 | 2025-05-31 01:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 2654f8f4-a906-3640-badb-09fbced2d9a4 | -7.2405 | -43.0899 | 2025-05-31 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| 4a23a3e8-0431-364d-80d7-7f8f5f2e1e1e | -10.462 | -47.9428 | 2025-05-31 01:20:00 | GOES-19 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 2c47cc3b-e536-3c04-a125-c8cc9bcfd179 | -12.0157 | -49.5054 | 2025-05-31 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| d4cb63c3-c288-364e-86b0-8ebc1d9db9eb | -12.0345 | -49.5248 | 2025-05-31 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| c9119b9d-8f7d-3f4b-af35-f4b8da85a698 | -11.8368 | -51.2641 | 2025-05-31 01:20:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 113.1 |
| aa077398-b7db-3d66-846e-4385781c6ea9 | -10.6492 | -49.4267 | 2025-05-31 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 76211b62-e079-3d53-967d-e42eaf7ddc79 | -11.8365 | -51.2854 | 2025-05-31 01:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 658df19c-a397-3b03-b1ee-7cf364f9e244 | -11.8368 | -51.2641 | 2025-05-31 01:30:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 05b08fea-9402-3557-8253-56e3287f6e21 | -12.0154 | -49.5272 | 2025-05-31 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 126.7 |


[Clique aqui para ver as próximas entradas](README4.md)
