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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a07d3c9-8020-307a-a8e2-f7b3d80eb4b2 | -3.0689 | -50.3326 | 2024-11-12 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6fbe2e15-a992-38f5-adb5-b96904ddc09b | -3.0913 | -54.287 | 2024-11-12 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| bdc34681-5eaa-37f9-8411-bc61c6216061 | -3.0913 | -54.307 | 2024-11-12 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| d6ab7306-9bac-38e5-9870-d178149bca7e | -2.1272 | -50.6703 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| feebfc9b-b6df-3bce-9afa-42d98eba1483 | -3.0689 | -50.3326 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 3e126530-17b9-348a-81f4-f4a0b0caa1ae | -2.1271 | -50.6912 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 163.7 |
| c151abbe-82b8-3f5c-b3c9-c52d7d457f33 | -2.1087 | -50.6916 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| d7d8b5d0-d3d3-3cec-b641-26a90af24ea5 | -2.1455 | -50.6908 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 602ccd70-ed0e-377d-96d0-0223fe7c3298 | -2.1271 | -50.7121 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 72afe622-586f-34af-add7-2d0f04912ef6 | -3.1097 | -54.2865 | 2024-11-12 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 9de75ffb-99a2-337b-b723-4a8d30b1bed8 | -3.0504 | -50.3332 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 991eb5fe-83d5-3619-83a2-00db562c36e8 | -3.1096 | -54.3066 | 2024-11-12 03:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 5b8bf400-4eaf-3248-a301-f0e4fbb2ec79 | -3.0504 | -50.3542 | 2024-11-12 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 765aaffa-afbb-3640-816b-95ca8b7f0ea7 | -4.91213 | -37.84848 | 2024-11-12 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37c1abb5-dda2-3bf5-8096-05f27a64f343 | -3.34372 | -39.90678 | 2024-11-12 03:36:00 | NOAA-21 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4ee332e6-3c19-3960-bbdd-44251c81bdd0 | -5.12811 | -37.85741 | 2024-11-12 03:36:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 6701d10a-1186-36b7-90a1-927bbd97280a | -3.29826 | -43.54273 | 2024-11-12 03:36:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c08dfe6-3ed8-3f4c-91d6-9d9f3ca0dca6 | -3.29958 | -42.48447 | 2024-11-12 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53f88863-660a-3532-a8af-49926f33e131 | -3.46419 | -39.5844 | 2024-11-12 03:36:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0c036a28-c130-3a14-81a9-7693ecdee7fc | -3.30502 | -42.48529 | 2024-11-12 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2aa533e-2468-3ea7-a91d-f6663ad49b16 | -6.57579 | -35.12733 | 2024-11-12 03:38:00 | NOAA-21 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| a46534b5-6deb-3330-af85-8f571ec151ca | -4.80708 | -44.46502 | 2024-11-12 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c32ff4f6-0507-31ce-b9a2-6730271d8c30 | -7.78127 | -34.92417 | 2024-11-12 03:38:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d012834f-83b8-38a0-b72b-c4c957d5d824 | -7.51624 | -34.83501 | 2024-11-12 03:38:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b568c9a0-2f7a-35fb-b10b-586989596ca9 | -7.38723 | -35.26401 | 2024-11-12 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 6c1fe148-1cba-3423-b492-57ec32256f67 | -5.80885 | -35.53925 | 2024-11-12 03:38:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7058da4e-9d05-3896-b2fa-e8d26918f215 | -7.18084 | -35.01954 | 2024-11-12 03:38:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d882c9c9-ff5d-37c6-98ac-607e577adb34 | -6.8578 | -38.88922 | 2024-11-12 03:38:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 227d858d-f4bd-3c4a-8026-26751807d9c4 | -6.92623 | -38.1405 | 2024-11-12 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5c243814-6454-3b77-98a2-ed5c76bc8fdd | -5.9322 | -39.4754 | 2024-11-12 03:38:00 | NOAA-21 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 84ed49f9-55ba-37f3-beed-00fad12ea8f8 | -5.73881 | -35.55896 | 2024-11-12 03:38:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 04a773a5-1c0d-3010-bdbf-6ca1380b3eea | -6.75256 | -35.0388 | 2024-11-12 03:38:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 44163050-821f-34c7-b2d5-bb64637469de | -6.12886 | -38.89612 | 2024-11-12 03:38:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fec3f7f3-3787-39ee-a1fd-84355fa313e6 | -4.84983 | -44.47963 | 2024-11-12 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e027c29-235e-3d2c-ade6-a73e598e76d8 | -6.74185 | -35.10631 | 2024-11-12 03:38:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cd6bb005-8726-3d19-9865-1b30e77129b6 | -7.42584 | -35.23721 | 2024-11-12 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| eddfd740-dabd-3972-9e8e-144f491bd9dc | -6.8544 | -38.88501 | 2024-11-12 03:38:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 18ff6d7d-9ffd-31ad-9f27-d780ebf64d0a | -5.51361 | -39.09819 | 2024-11-12 03:38:00 | NOAA-21 | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| af6a10db-c501-39b6-9ef9-1a00839eb483 | -4.78338 | -45.84002 | 2024-11-12 03:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0d6598dd-5899-3f37-92f4-cc745080af28 | -7.47768 | -34.84324 | 2024-11-12 03:38:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1cd3acc5-0f18-3f6d-98ab-79832220037c | -7.38331 | -35.26706 | 2024-11-12 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7514e8fd-3e2e-3aef-a29c-f10d437bf61a | -7.70611 | -35.14 | 2024-11-12 03:38:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7fb509f0-6a55-3cab-9c93-9f9f1c9f7a8a | -4.80245 | -44.46699 | 2024-11-12 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 61adc709-6e59-3825-8576-6039614cf71d | -7.71002 | -35.13698 | 2024-11-12 03:38:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 75026f9b-4470-3e33-974a-5c6997d6ad9f | -7.77794 | -34.92364 | 2024-11-12 03:38:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 764cbbdb-0dc3-3d15-b03e-a916c37b2568 | -6.752 | -35.04236 | 2024-11-12 03:38:00 | NOAA-21 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a9e6c478-d90b-31f5-a622-bf7aa2da618f | -4.84908 | -44.48394 | 2024-11-12 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 85cd2780-c610-358f-83f7-9bbc2070ce4c | -4.80324 | -44.46253 | 2024-11-12 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dee85300-2c95-3adc-a088-005210dfe9b6 | -5.49266 | -37.2439 | 2024-11-12 03:38:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c50631e4-550b-3d6a-a3b9-dbc8d450ebb5 | -7.78071 | -34.92769 | 2024-11-12 03:38:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 614068c7-5a4d-318a-9bd2-f479ab9a79b3 | -7.70946 | -35.14053 | 2024-11-12 03:38:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 690316f6-f554-3c6b-b4f7-fd7ed91516ec | -7.39394 | -35.26507 | 2024-11-12 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 432b6731-0963-308c-a197-3874cee209ca | -7.42918 | -35.23776 | 2024-11-12 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 64205a64-71f7-3123-83dd-8e70c3f2c5f4 | -7.38667 | -35.26758 | 2024-11-12 03:38:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 245a274b-1d45-37fc-bb76-8ba08c6daf4d | -5.80175 | -35.58374 | 2024-11-12 03:38:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d476541-3517-31cb-9328-257c9c4fa774 | -6.6322 | -35.30607 | 2024-11-12 03:38:00 | NOAA-21 | PEDRO RÉGIS | PARAÍBA | Brasil | 2512721 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9ceee6d1-fbb8-3cf5-83d4-63f0b8a892e5 | -5.81226 | -35.53979 | 2024-11-12 03:38:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 25355fa9-3616-36fd-9058-28057b579150 | -4.78439 | -45.84113 | 2024-11-12 03:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fafb5b56-bd96-387e-931e-022c9ef5d2f4 | -6.97773 | -40.03253 | 2024-11-12 03:38:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8756fa51-05ca-3652-8e1a-5f704c0186f8 | -7.1814 | -35.01601 | 2024-11-12 03:38:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b98244a-af0f-3b36-a2c6-f6231296612a | -2.1087 | -50.6916 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 0ffeec66-3535-33a9-af48-faf30df3ebfc | -2.1271 | -50.7121 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 89d26860-c042-3f0c-ab54-f4546a2d839c | -2.1272 | -50.6703 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a00efb7e-bdca-3f56-95a4-50609787447a | -2.1271 | -50.6912 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 162.4 |
| a68c0416-48e0-30ff-aa9a-94c536dfd49d | -3.0689 | -50.3326 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| bae8819d-81ca-3329-b17a-aa2cf5547b8c | -3.0504 | -50.3332 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 136.2 |
| 892709c2-7aeb-3067-ac55-db5407639780 | -3.0504 | -50.3542 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 781b7009-f6ae-3f07-a58b-7400efcdf465 | -3.0505 | -50.3122 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| f4dfda3b-af4e-39f1-8192-e1dfac235cbc | -20.1193 | -49.1895 | 2024-11-12 03:40:00 | GOES-16 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| d3fece84-123a-3766-9f72-e8f01e928167 | -2.1455 | -50.6908 | 2024-11-12 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 9d23d54d-29bf-3782-b554-c737bc55ecde | -19.4574 | -39.75898 | 2024-11-12 03:40:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 9b283f00-4f5d-3ad1-8cb7-2136aee41cf7 | -17.75521 | -42.89375 | 2024-11-12 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b115a1c4-5aa5-3da7-b6ef-e8c993fa0e6d | -19.45814 | -39.75477 | 2024-11-12 03:40:00 | NOAA-21 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| f049a1b9-e5e9-38ad-8b1e-5f4d1da981f7 | -16.17532 | -42.19164 | 2024-11-12 03:40:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a4ce7ccd-00ab-300b-836a-a8b87e006ce2 | -19.17834 | -40.12593 | 2024-11-12 03:40:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a6933faa-1a38-3166-a8b9-c7c72c72b8c4 | -19.17318 | -40.13402 | 2024-11-12 03:40:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d567d467-07a7-3e03-b3d3-660dcfa2e272 | -17.70774 | -44.72923 | 2024-11-12 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8438b75a-ee36-3233-88de-4187b3ab84b6 | -16.17208 | -42.19215 | 2024-11-12 03:40:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 82bb1d76-982e-388f-806b-3de4f5c26282 | -18.3506 | -40.01607 | 2024-11-12 03:40:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8b95f63c-e370-3ea6-88fc-da4067c09191 | -16.57018 | -44.06603 | 2024-11-12 03:40:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64798e88-90cb-3132-887d-59dcf4d6ecc7 | -17.75441 | -42.898 | 2024-11-12 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31644243-f9bb-3fc8-bccd-2805a0c35d71 | -16.57384 | -44.07257 | 2024-11-12 03:40:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a78ce576-07e9-363e-9ff7-5e2f91d19a10 | -18.34697 | -40.01539 | 2024-11-12 03:40:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 13c268fe-1a65-315b-ab0b-26855721856a | -16.57087 | -44.06399 | 2024-11-12 03:40:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9ef73cb-dbb5-3b43-9524-6ce01b4395ec | -19.17679 | -40.13471 | 2024-11-12 03:40:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 4e4fda39-40da-3950-a880-641bfe5497f9 | -16.57457 | -44.07055 | 2024-11-12 03:40:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09941150-58c0-3d5c-bc34-a3ba8066e3c7 | -18.39671 | -45.97871 | 2024-11-12 03:40:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5dacdc31-bf0a-3d58-9d3f-f9fa84edd475 | -16.57493 | -44.06711 | 2024-11-12 03:40:00 | NOAA-21 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a11862bf-b50d-371b-b408-a4d64b99689e | -18.44629 | -47.55284 | 2024-11-12 03:40:00 | NOAA-21 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| daa75c81-e76e-3adb-a574-0b55a174325a | -16.42771 | -42.63361 | 2024-11-12 03:40:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c729aa7b-16ef-32d9-b0ac-96d2e5962fb1 | -18.03984 | -44.52826 | 2024-11-12 03:40:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 77b9089f-5b4c-3c0e-a6ba-3c560d10ffed | -22.67627 | -42.85813 | 2024-11-12 03:42:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1e6ddba0-4ef0-3152-90d5-9566a63a6aac | -20.9319 | -47.43773 | 2024-11-12 03:42:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3816a092-28ef-3990-8664-a3d8899209a1 | -20.3232 | -48.82858 | 2024-11-12 03:42:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9c80ba05-3ca9-3df3-9d73-0b5a6c444f29 | -22.86077 | -43.52274 | 2024-11-12 03:42:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0b42fd7d-21a5-3bca-91c4-40d39e6cdc29 | -20.76638 | -46.76968 | 2024-11-12 03:42:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 035ddf83-38d8-32ef-a275-681fb498e34a | -20.11338 | -49.18544 | 2024-11-12 03:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| b4c5931c-5317-3877-8659-41c6c8d48234 | -20.11107 | -49.19547 | 2024-11-12 03:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 86cd0e97-bbd7-3d8d-b98c-0717e479a9a5 | -20.10609 | -49.18913 | 2024-11-12 03:42:00 | NOAA-21 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 9679d20e-1734-3f96-abd4-b52f43f34993 | -20.39431 | -47.07976 | 2024-11-12 03:42:00 | NOAA-21 | IBIRACI | MINAS GERAIS | Brasil | 3129707 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README9.md)
