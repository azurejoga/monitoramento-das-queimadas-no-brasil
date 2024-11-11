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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b546e7f2-3d87-37e5-80a5-5ea73644ce19 | -3.52395 | -49.95243 | 2024-11-11 00:22:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 3db6d840-fd83-3b5e-8cf0-d2276fa459f0 | -2.40894 | -46.50845 | 2024-11-11 00:22:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 2ff87930-074f-302e-8fb9-b5d33974513e | -2.54472 | -47.31117 | 2024-11-11 00:22:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8b5fb4bb-4cf5-3178-a568-5b54bcd4f16d | -1.82566 | -47.87372 | 2024-11-11 00:22:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 56262a29-b00f-312e-aa42-043e6e90664c | -1.32212 | -47.70346 | 2024-11-11 00:22:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 66e74526-b9f1-38ea-b1a5-21cf82b6e847 | -2.23305 | -46.44551 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| a2bf0a12-558b-3fe7-93b8-095aad9b7464 | -3.26814 | -48.74762 | 2024-11-11 00:22:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 23f5b4d3-85fe-3239-89f3-0285c0759d96 | -2.1068 | -46.09588 | 2024-11-11 00:22:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9ed63d49-bcec-3392-9bdb-647c60ed10a3 | -1.32531 | -47.72551 | 2024-11-11 00:22:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 38e865c8-b0b3-3d18-93da-7190d3314fd6 | -2.84096 | -49.42187 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 144.3 |
| 4285a024-df9f-39a9-807f-1cdd6bac6285 | -3.24521 | -46.48574 | 2024-11-11 00:22:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 89d66179-7724-3543-b2bb-82fad9cd01b0 | -2.25516 | -46.51642 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 6b62bfb9-0732-360e-9ff0-1c03b41e48eb | -3.14125 | -50.44866 | 2024-11-11 00:22:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 5f942f2e-59aa-3a7b-9142-8f38bd0e4653 | -3.32296 | -46.09679 | 2024-11-11 00:22:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a7a0ec81-54c0-34ef-a1b8-ed43dd49cbf1 | -2.87084 | -45.3811 | 2024-11-11 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.0 |
| f7b084e9-db61-3150-ab96-43a785fda554 | -2.23065 | -46.42753 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| c7c6f262-15d2-3af7-ae9b-35e1fdd3161f | -3.02103 | -45.80829 | 2024-11-11 00:22:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4d73ec66-bfb7-3eea-acb3-004a7b6c7697 | -2.97798 | -45.84803 | 2024-11-11 00:22:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e6d13b2d-a9a8-35df-84d1-16a2f8b6ea37 | -3.2891 | -45.3412 | 2024-11-11 00:22:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| fff91233-831b-3688-a7d9-2d0b3424bf55 | -3.02328 | -45.82475 | 2024-11-11 00:22:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 112.0 |
| a161b059-eb82-38b9-86a8-072a1a05da6c | -2.30131 | -48.46261 | 2024-11-11 00:22:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 15146696-4703-3161-a520-a0ce91eeb7b2 | -2.24571 | -46.56154 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 8ff47203-7f78-30dd-9e58-156fc677aecd | -2.25295 | -46.52318 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 7a816c43-fadd-3a29-88b2-f747146bf33e | -2.88438 | -45.39479 | 2024-11-11 00:22:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 6ba7e297-e80d-3d5f-bed9-6707a3123e05 | -2.25762 | -46.53468 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 29d52633-54a8-38d5-9f62-2fbf7e3edff2 | -2.22775 | -46.43433 | 2024-11-11 00:22:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 7520ef70-11d4-3755-a075-0255ec2f58db | -2.47514 | -46.23681 | 2024-11-11 00:22:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4acaccb9-872a-3cef-81d0-dd85d4bb2b60 | -3.10961 | -45.28431 | 2024-11-11 00:22:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 7de4a55e-0c7d-3386-8580-ce819334f9f4 | -3.0187 | -45.12036 | 2024-11-11 00:22:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eeb150bd-9f34-3ca4-86b6-b8fb145eef3b | -2.38252 | -50.32708 | 2024-11-11 00:22:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 8ce1bcd9-e63a-3a65-8b28-7fbbdc4985c1 | -2.43253 | -47.63138 | 2024-11-11 00:22:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 578cc420-d324-3bc0-bc9f-79978292eb6b | -2.52533 | -45.453 | 2024-11-11 00:22:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 40ffa8a1-caf1-39b8-8777-7d824025d0b9 | -2.74397 | -49.37699 | 2024-11-11 00:22:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| a50c1dc0-3cef-3ba8-b2f4-ae670f5e7dc0 | -2.41344 | -46.5201 | 2024-11-11 00:22:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 91e21748-ba80-3857-92a2-ed4cb232c728 | -2.97228 | -46.98904 | 2024-11-11 00:22:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| b513d2c8-1c47-31fd-85cd-61c2975c3ef7 | -2.43561 | -47.65404 | 2024-11-11 00:22:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| afe2d4ef-65c2-3800-bddb-5923318af972 | -5.9788 | -45.3621 | 2024-11-11 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 9eef44a1-2091-39b5-985a-ea7abb5777fc | -3.048 | -50.981 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| ff1a1251-1dde-38e5-beb9-0b393ba1db25 | -4.0294 | -46.9484 | 2024-11-11 00:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 13838c97-62e2-36ee-879a-60026fcdf4f9 | -15.9791 | -59.3468 | 2024-11-11 00:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 7a5466d5-6522-3aa5-a059-6734d1b9089d | -15.9793 | -59.3267 | 2024-11-11 00:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| 7a29cf21-0e4d-3a20-9a9d-a78b8d5701aa | -3.2352 | -50.2855 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 189b4fd4-732d-32bc-8b43-ac420ae8085b | -3.2603 | -48.7582 | 2024-11-11 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| e1d53123-c926-3259-ab97-93bad6dd9d9b | -3.2168 | -50.2861 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1d154a04-70be-35d0-98ec-f1d97e43efd7 | -3.0323 | -45.8377 | 2024-11-11 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 27e10468-b4be-3834-9884-cdf61c52dd76 | -3.5331 | -42.5864 | 2024-11-11 00:30:00 | GOES-16 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 16a2d2d5-b601-3929-86e9-cf3230caacb6 | -1.5164 | -52.1491 | 2024-11-11 00:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| f8b06e61-51d5-3e0c-9a83-d7817b27c066 | -3.5347 | -45.6837 | 2024-11-11 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 05e5b5aa-8163-38b9-be42-088a889213a6 | -3.0324 | -45.8154 | 2024-11-11 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 225.5 |
| 21109796-87bb-329e-b1be-7ba291210d1f | -3.2244 | -53.0524 | 2024-11-11 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9c49f8b7-2dbc-3286-a693-f492cc57a0d8 | -4.0293 | -46.9703 | 2024-11-11 00:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 288b01da-c9cd-331f-ba80-1e738a57d7d0 | -3.103 | -51.0626 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 571ac224-345a-3215-b455-7c054770f313 | -3.2949 | -45.312 | 2024-11-11 00:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 25c43b70-22e4-3b31-9925-6331fdd0afd6 | -3.0295 | -50.9815 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| ef90236c-f5d8-37fb-8bde-d208197b4074 | -3.5346 | -45.7061 | 2024-11-11 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 76fa0f15-a9a1-3361-b2bb-c04135f86cf7 | -3.6604 | -50.2081 | 2024-11-11 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| f744dd5c-4990-32ec-b88f-5334ec289094 | -4.1286 | -49.088 | 2024-11-11 00:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| d1a52e74-4c54-30a1-84f1-037581de92ae | -15.9982 | -59.3649 | 2024-11-11 00:30:00 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c391f1e7-586e-37e8-88ad-2cdf174cce29 | -1.2201 | -53.6364 | 2024-11-11 00:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 49b0fdc0-d98d-31a0-bb9c-452c7e373af4 | -17.2936 | -57.4652 | 2024-11-11 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 104.8 |
| dbe61780-17d8-3885-a403-98b54e9522a1 | -3.5345 | -45.7285 | 2024-11-11 00:30:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| ef3837ea-f492-34fd-8edd-29c2540c81bf | -3.1984 | -50.2657 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| a09c2b6b-dd39-3bf7-a440-41846a3a0d17 | -3.0138 | -45.8161 | 2024-11-11 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 126.2 |
| eebe74d1-7ac6-3d86-9f93-aba2db9c37ee | -3.2427 | -53.0722 | 2024-11-11 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| d752767b-9435-3594-8e0b-a5bf87e6586c | -2.6662 | -49.3948 | 2024-11-11 00:30:00 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6dacc7f8-133f-3877-9fc9-f67010c96580 | -3.0214 | -53.2404 | 2024-11-11 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| a853d473-3885-3f5d-bf19-f8d520b00d7a | -5.9601 | -45.3635 | 2024-11-11 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 28b0a4da-fe84-38b2-9845-905208442a86 | -4.1285 | -49.1094 | 2024-11-11 00:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 528b3ab8-f428-3cff-8ddc-4c879b468aec | -3.1458 | -54.4659 | 2024-11-11 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 23aa85e5-efd4-3e70-95ee-8362ef31170f | -3.2948 | -45.3346 | 2024-11-11 00:30:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 5eb26231-449f-3810-be5a-9be95ab08cfc | -3.0296 | -50.9607 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 2ca5d8fe-fd2f-3b13-b61a-e5f26828ea53 | -3.3836 | -50.1336 | 2024-11-11 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 8ab49046-4cd8-39b3-83ee-0cd8e12c39ab | -3.048 | -50.9601 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| bb61450d-5cbc-3f21-b250-58bea3374dc3 | -3.2536 | -50.3059 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| d72d4b58-4eb6-34fd-a608-eb70d863979f | -2.2504 | -46.5282 | 2024-11-11 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8c659772-b076-30be-857a-cd2f2a560a73 | -17.2933 | -57.4857 | 2024-11-11 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 159.0 |
| ab7ff516-d6de-3ed2-b29f-27d8b7dd908e | -3.2588 | -53.6994 | 2024-11-11 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| cde75d53-d49c-3d20-bdd6-5369785a9d72 | -2.189 | -48.3815 | 2024-11-11 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| b29bd37a-ab13-3415-9495-6ea44ed0d8f8 | -3.0137 | -45.8384 | 2024-11-11 00:30:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 86.2 |
| b34eaf86-00d7-3238-ada5-69421e4e752b | -6.1323 | -44.9426 | 2024-11-11 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| cca86b97-3211-315e-8c7e-0fb593ebda4f | -1.4057 | -52.3758 | 2024-11-11 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| fdf9e29c-2932-3325-8b3d-25a3ad3cb538 | -4.1101 | -49.0888 | 2024-11-11 00:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6a6d2e1f-1abe-3b69-807d-02ea72039555 | -4.11 | -49.1102 | 2024-11-11 00:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 79bf310d-b7a3-36bf-b86e-84483df54a7a | -2.2504 | -46.5061 | 2024-11-11 00:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| e81d4064-fc3b-320a-aa49-c0fe861b41ef | -4.1246 | -43.5833 | 2024-11-11 00:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| ef81492e-a22a-3fd1-ba54-27849e266aa6 | -2.9901 | -46.9901 | 2024-11-11 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| edaa72fd-519d-3aab-b6b3-62a90667f10d | -6.1325 | -44.9199 | 2024-11-11 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c6ad0458-cdfa-3415-ac09-f8d7257b6944 | -3.5518 | -42.5855 | 2024-11-11 00:30:00 | GOES-16 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b7e7b560-f32a-3486-953d-914b49b8e82d | -3.1983 | -50.2867 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| f33766dc-2d35-35a4-8148-1eb734aa1504 | -2.8508 | -49.432 | 2024-11-11 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 211.5 |
| ca9931d4-69f9-3aea-adb7-e9be5cd5820d | -3.1458 | -54.4859 | 2024-11-11 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 7a9d8c83-c56f-379f-8653-d68de91ab76c | -17.2737 | -57.488 | 2024-11-11 00:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 47287ef8-90a0-323e-bd6e-82d83501b9bd | -3.5137 | -49.9606 | 2024-11-11 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 7b88e5c0-24d9-3f7d-a5f4-1bace85a50b0 | -3.2428 | -53.0519 | 2024-11-11 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 99f553ed-cf78-3583-8a1a-e7e04931e359 | -3.2772 | -53.6989 | 2024-11-11 00:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| bb156fb1-5284-3bbd-97cb-da2e5bff96a5 | -17.6086 | -57.4276 | 2024-11-11 00:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.9 |
| 46a7dff7-72a8-32f9-8237-78a9beee731a | -2.2075 | -48.3811 | 2024-11-11 00:30:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| dcecd57e-6ccb-3fcb-86ab-f6da85933c71 | -3.1092 | -45.2743 | 2024-11-11 00:30:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| fb1b3358-6a84-3575-9d0d-122bef279458 | -3.1423 | -50.4352 | 2024-11-11 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 01b36087-cb93-3735-be1b-498114bc8190 | -2.8508 | -49.4108 | 2024-11-11 00:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |


[Clique aqui para ver as próximas entradas](README6.md)
