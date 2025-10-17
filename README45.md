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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48cf9a01-b9af-31a5-b2d5-9f812d540b08 | -8.08648 | -45.41811 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16859f39-7d5c-3a58-b66b-37c5e8bf45ee | -6.29175 | -44.01079 | 2025-10-17 04:19:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7ba4e33-0646-31d4-94bd-3347faafe75a | -9.23895 | -44.37568 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bcbde72-f2ee-36a8-bd10-78865d5fc3e3 | -5.22861 | -38.16109 | 2025-10-17 04:19:00 | NOAA-21 | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3ee15c21-34ff-39ff-8c73-d094c68cc361 | -7.7146 | -47.84593 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1eec5e62-4d26-3e4d-806c-3710bbdaaa5d | -9.25273 | -44.35252 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4165695-835f-31fe-96a1-755b73a8bf8e | -8.23155 | -43.43308 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d345ea41-c0bf-33a3-bc9e-10233042ebea | -11.45668 | -44.23367 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34f85ddc-8999-3e26-8045-f83ac4feb5ed | -5.42133 | -45.65259 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3956804e-30a6-3c06-b31a-8f48b3ba3789 | -9.19302 | -46.87372 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5bde2d2-ae89-3539-9830-7c2845e361a3 | -9.71279 | -44.5441 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d44a6ddc-6d9a-3b8f-940b-5c9bb177343b | -11.41047 | -44.19642 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8012868-9973-3432-9209-5fe1d602d1c2 | -8.28548 | -43.38468 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73b77eb2-97f4-326e-a698-31adc4da919f | -8.39481 | -46.24351 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| debb16a5-f09a-30dc-bbab-c3fe3ec6d29a | -4.43945 | -50.54947 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bec4571e-7cfa-3e9a-9be9-d7865e7e7152 | -8.62226 | -50.44851 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28e64114-ecc4-3aaf-ba88-8f7a6f47183d | -8.37516 | -46.28075 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 94828b7d-ce2a-333a-b5fd-0f212127ae76 | -6.2377 | -44.6427 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a7ac5f5-74d7-37d6-8cfb-50468db04db5 | -5.08937 | -44.34784 | 2025-10-17 04:19:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4e9e4c1c-2a2e-36d8-8a31-c37f47c7f603 | -11.4702 | -44.25828 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fb34a11-9cb4-30ec-9304-0772db7a4222 | -11.48249 | -44.17751 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45a07aee-4fb6-3de8-83de-8fc21254041a | -7.72169 | -47.84711 | 2025-10-17 04:19:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98ed457e-c1fe-3127-974f-53d5660d81c5 | -10.10525 | -44.62365 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4a82dfdc-aafe-3d7c-8512-5200a049d11e | -5.09548 | -47.48263 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a11bde42-690d-3c42-ad5d-1e8372b7b387 | -2.87155 | -50.74298 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e7b81c02-58e9-3e49-a001-c778a79b9e0c | -8.82165 | -47.30468 | 2025-10-17 04:19:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1ddbf2a9-2b75-305e-9d7c-41738536c3fc | -8.27718 | -48.00472 | 2025-10-17 04:19:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9f38a50-950c-32fd-a9d8-7419efef997b | -7.16279 | -42.53311 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4cecb957-ee76-3445-a7c6-36387e409d6f | -6.33331 | -44.31195 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9e21b7d-d45f-3e01-9778-f25176a7a7d9 | -7.27938 | -41.95604 | 2025-10-17 04:19:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| cddcb06a-0f5c-3997-bc97-37079b68d045 | -5.71801 | -43.82909 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 871338e0-99a9-3a59-90e7-601269e8f1b2 | -8.84348 | -44.40402 | 2025-10-17 04:19:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de2676e1-ee1d-3b59-a92a-689238f8bbc2 | -6.37732 | -41.47479 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8796bede-a551-397a-b125-26b0a2dd968e | -6.89429 | -43.98769 | 2025-10-17 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bac4e331-7201-3914-8012-7184f014a6d3 | -10.998 | -44.501 | 2025-10-17 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4abc443-520e-3e00-82de-dbb63344e43f | -11.48981 | -44.17488 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 323c55f5-2d36-3fca-8468-f9dc9d9077d8 | -5.7074 | -45.52401 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee167e35-86d5-3e6a-b177-72d88d99ce02 | -8.12348 | -45.54856 | 2025-10-17 04:19:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ddab5cfd-a20e-392e-acc6-4f54e3c1cd0e | -6.30744 | -44.72072 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbd5a973-7a22-3486-b158-cef81a6bd2eb | -6.89047 | -45.44767 | 2025-10-17 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 407c45be-9c0b-3b82-953d-e4d2a8cf60ca | -9.24228 | -44.3762 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8600a6c1-5bde-3f47-af7f-1607497402b9 | -3.41295 | -50.13941 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 556aebe2-17f8-3651-8b2f-99b7c7c8c0ad | -5.96336 | -43.16806 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4bd70939-6ce9-3544-b710-106cc8466d9d | -4.28175 | -48.58644 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a51e5bd4-b68d-32b0-9179-73e039f09cae | -11.40427 | -44.19169 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c8699c-53b2-3052-a637-5ad94a9d5c7d | -3.52565 | -50.30655 | 2025-10-17 04:19:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2236af4f-a8bf-322d-bd26-6032e9c85398 | -11.47969 | -44.19592 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e73ca28e-9595-3b3f-8288-a88b41d3f0a7 | -5.24791 | -50.96277 | 2025-10-17 04:19:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dc1b9ef-370a-3885-8389-0d6c81a44793 | -8.16707 | -43.3106 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a66e9981-b11b-3fd2-87c2-e463a4436384 | -8.36778 | -44.7753 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b05ea47d-9ddc-3179-aac9-838c3cf4b4a2 | -7.95088 | -44.14983 | 2025-10-17 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6e552c7-f398-34c6-aa4b-f3f17614694a | -7.46424 | -42.14989 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7e742fb0-d0e5-300d-8f05-6d0377c1ba4d | -9.13401 | -46.62644 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c8ae549-c736-3751-a87c-46bc5af4bce1 | -9.71649 | -44.49771 | 2025-10-17 04:19:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07d932ea-3f61-34b8-b0c7-e0ce6f818ba4 | -10.59248 | -47.39564 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0442f882-eee1-334d-b89e-c5d97c5ba072 | -11.39366 | -44.21635 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a79ec3d8-0cd2-3878-bdc7-1118963f1092 | -5.71029 | -46.50448 | 2025-10-17 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef3679ce-7252-30a9-a38f-3f37acfe140d | -5.04074 | -49.7393 | 2025-10-17 04:19:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64c15f66-0920-3de8-aba2-c391a178fd59 | -10.08902 | -45.34145 | 2025-10-17 04:19:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2b66526-2a1e-32b7-b0aa-3fdab788cc85 | -9.50236 | -47.26842 | 2025-10-17 04:19:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d6ebe36e-e27b-355c-a5dc-609122ff9c0e | -6.48345 | -43.18921 | 2025-10-17 04:19:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 047ba40e-24de-3fe4-ab64-6eeaed46f372 | -6.07372 | -41.91042 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 9183cda0-0577-315d-a780-147973b27c55 | -10.28862 | -44.02566 | 2025-10-17 04:19:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d58f8a68-8fc1-3e2d-a763-9eb1e9a1ad13 | -5.75568 | -43.08109 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3a875888-99da-312b-a848-3514d22cd4fd | -11.46141 | -44.04181 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 675584a9-a794-302b-98b8-abb8379696f5 | -5.35931 | -44.81714 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6164dfc6-b111-3f09-841f-0106b0556baa | -9.97993 | -47.01307 | 2025-10-17 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e6d3192-ebb2-3273-b997-298e64ee864c | -10.58484 | -47.42109 | 2025-10-17 04:19:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 810cecc3-6369-3379-a6b0-801aa9290e37 | -9.24778 | -44.36259 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fabb9b50-866b-30f6-98ee-80c14899e10c | -4.86077 | -44.43824 | 2025-10-17 04:19:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d3d57e3-7b9d-36e5-b212-828e279280ff | -8.91971 | -47.7381 | 2025-10-17 04:19:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfc31d0c-840f-3239-98db-a841a3602b31 | -6.58426 | -47.0755 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1e481997-9eae-3bdd-a013-673da9db0570 | -8.30472 | -43.4176 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b1f41eaf-6645-397b-a271-6348f73eed6d | -5.27366 | -43.11711 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 361cf841-8789-3ccf-97ba-d97752b6eac9 | -5.17956 | -42.9313 | 2025-10-17 04:19:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3d946e0-ebdc-34c0-903e-4fbbe9a99324 | -9.25606 | -44.35304 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f76cd5e2-969f-38fe-bac6-b2ebf9c4cd3e | -5.6977 | -43.54342 | 2025-10-17 04:19:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e320112a-a587-39b8-9fc3-64bfb0f02794 | -7.47642 | -42.638 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| c077c799-f8e6-30d6-abaf-4b78cb8b48ab | -7.16985 | -42.18093 | 2025-10-17 04:19:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 08aa45db-b9bf-36d5-bfe0-b734295479f5 | -10.12278 | -44.55419 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fd4207da-b377-3ff5-b65a-7f59fd50d683 | -10.51527 | -43.38639 | 2025-10-17 04:19:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8dc5cced-3475-3a60-9929-ee0ba82e28ea | -10.81464 | -43.93687 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9a414182-70f7-3849-aa38-ce6181617f9e | -8.55811 | -45.49068 | 2025-10-17 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b3ec0a7-d0f9-34be-a9dd-456f3c8cd27c | -7.40204 | -44.74947 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7cebfa6-c150-3217-be64-5744a705b273 | -6.39639 | -45.12684 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7df515de-5026-3103-9140-df935e492810 | -6.3487 | -41.50522 | 2025-10-17 04:19:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dcc384dc-c4e1-3f79-9f7a-6c20857c2e09 | -10.28021 | -44.03564 | 2025-10-17 04:19:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 871ccaa8-31c1-3566-8ee3-9d36f084b26f | -5.71296 | -44.51692 | 2025-10-17 04:19:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c62ec880-3df8-30f3-8fb1-850577623b70 | -5.41489 | -40.89867 | 2025-10-17 04:19:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 21404882-8481-31e1-9989-223ec3a36b2f | -8.28321 | -43.37684 | 2025-10-17 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 57b8a8a1-e651-3a59-b99c-a2c1497d2bb1 | -10.81598 | -44.01979 | 2025-10-17 04:19:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55612b14-3cfc-392d-b6d8-61ea7874228d | -5.60674 | -42.72615 | 2025-10-17 04:19:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5d18248-c7ab-348f-8e20-28bc5264bdb7 | -7.17675 | -46.93452 | 2025-10-17 04:19:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dd5accc-ebb0-3eec-ad53-d975aef58e25 | -10.52504 | -43.36838 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ede3613-ea8c-3bfa-a337-a00da005158f | -2.86699 | -50.74225 | 2025-10-17 04:19:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c17ef187-4565-32ee-b4c7-093c79a0f117 | -7.35808 | -46.98639 | 2025-10-17 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69c5ff4e-45bf-321d-9fad-575a40de6fca | -8.26203 | -44.07175 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30a3eb10-604b-3752-a29e-6054ee1beda1 | -6.06977 | -41.90719 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 29a1f175-a383-31c3-bb7a-f9158ad04e48 | -5.5206 | -43.30408 | 2025-10-17 04:19:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21f6f777-b921-3c91-82a4-f3e861f1e809 | -4.61007 | -50.82979 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README46.md)
