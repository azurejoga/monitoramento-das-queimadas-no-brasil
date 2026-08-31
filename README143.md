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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc32d979-5f81-3db0-9f55-53e7765d8fff | -19.11519 | -57.36567 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 4dd3e8bc-79e4-3723-bd0a-707abc56bce5 | -19.22746 | -57.33619 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 02e02f5e-7800-37b8-86b6-3229b0072ff9 | -17.37271 | -44.88561 | 2026-08-31 16:48:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c376dc02-c816-3954-9b4a-78f3931601b1 | -13.66913 | -39.82867 | 2026-08-31 16:48:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 9eec54c0-db4d-31ee-8c0a-81d014c976ad | -18.88791 | -48.24576 | 2026-08-31 16:48:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4548d36e-b9b2-3cb8-8817-85803ccbe74d | -16.70822 | -49.352 | 2026-08-31 16:48:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3e61aaa6-fa43-36eb-9597-8f6978b18c78 | -14.57951 | -54.10855 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 99f88efa-3b21-337c-bbb4-7a2a8124429e | -17.84969 | -52.10635 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 8f4c34d6-6d7b-3394-84c8-139a872e1bcb | -19.13436 | -57.37746 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.2 |
| 67ac68c6-633d-357e-bc3a-2f3741ae00ee | -19.15421 | -45.49777 | 2026-08-31 16:48:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 525ec5a9-0917-3b7b-aa16-246bfa3649a2 | -19.11827 | -57.36266 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 139.0 |
| f437bbbd-75c2-33bb-a3af-cc82bf49d56c | -17.4494 | -52.4115 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 81063381-a052-35d8-b4d3-179c1a5c3b90 | -16.57645 | -52.50718 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2f2a30f6-fb27-3fdd-8757-39b4484b84d1 | -15.04247 | -41.16092 | 2026-08-31 16:48:00 | NOAA-20 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| f35ff971-ff69-33d7-9e03-f06a5fb4370c | -17.53531 | -52.5537 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c7b20623-45ef-3abf-9a5d-2bafb50d591b | -17.87075 | -50.50624 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| c80bb9d3-d292-337c-a410-38abbf0e2279 | -15.78449 | -47.79824 | 2026-08-31 16:48:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 107.8 |
| d3c2e55c-b3c0-3933-a293-b6f24f637448 | -17.8804 | -52.0827 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 154a9be9-7ec4-36a6-bcac-f73f23a83af9 | -15.22042 | -56.36311 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1c424434-8f8a-3c1a-a394-6b0dca3683fa | -13.08119 | -45.17314 | 2026-08-31 16:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a851b3aa-dc75-3a68-9637-49505b1af756 | -18.26854 | -52.68085 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 42.2 |
| 8236712e-6974-37be-bcbf-5fc40a84b591 | -19.15303 | -57.41405 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.4 |
| 1c0f82dd-9314-3d76-be0a-8be3df22ec59 | -17.81969 | -50.61533 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0f304fa6-4031-33b1-b9d5-3b0b0169898c | -19.12158 | -57.36961 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 222.1 |
| 46f62429-816f-3250-91a8-46d20978e935 | -17.76751 | -42.28556 | 2026-08-31 16:48:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 8efafd95-badc-3bfe-8381-520375b4772b | -16.44544 | -51.4096 | 2026-08-31 16:48:00 | NOAA-20 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1c312baf-3fcc-33b7-97c4-880a87406e43 | -17.46622 | -52.40935 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 236f2e3e-c7b8-336f-9cba-5437d5fee83f | -15.99841 | -43.55555 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| f7ad9f68-6cf4-36ce-885b-38c913cdd2f1 | -14.44827 | -49.00288 | 2026-08-31 16:48:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1bc82375-d05a-3ab0-b5a9-57fb28496668 | -17.87265 | -50.52052 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| f523b6ec-7ed9-33bc-8b2e-61c572e6b1c5 | -14.593 | -54.10621 | 2026-08-31 16:48:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c3d07bbf-a83d-3c1d-bca2-1ecc1c598fa8 | -17.70695 | -49.14857 | 2026-08-31 16:48:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 881a3a3e-2ee2-3a65-9fef-424a5b497c32 | -16.01336 | -54.39937 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0d3461f3-b0bb-3ef1-9f19-0d4d2a0b537a | -19.09317 | -57.38621 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b8f0e37a-1542-3ec1-931e-8efad0f98ae0 | -19.11564 | -57.37021 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| ffe8af3f-dd38-3213-a0e3-8cb93a265b0b | -15.23027 | -56.35495 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 5b2c2951-a904-396d-bd13-1906c6de0827 | -13.54584 | -48.24411 | 2026-08-31 16:48:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4483361b-25d9-3ecf-8306-208ef4af0341 | -15.39498 | -45.62649 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| abb06a17-fb7f-3f6e-bafd-b90fad30a3d0 | -14.22879 | -51.94388 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 5e43ac21-cba8-360a-874a-557f6865fd2c | -16.99614 | -51.83532 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 33.0 |
| 517a3fa3-14e9-3c32-8b8f-96d36b4907fd | -15.97907 | -55.96132 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| 2672d54a-ee2e-3961-9af5-583b66587aa7 | -19.1951 | -57.35017 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 0d6ed490-a7f8-39a6-8360-63c5021f0962 | -15.79771 | -41.97987 | 2026-08-31 16:48:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.2 |
| d8d65be4-0cac-306b-bd6b-fa6d61bb5b60 | -17.88504 | -52.08614 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 240dc9ad-1dde-391b-b0c6-60147a419b3b | -19.20061 | -57.34506 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| bc75f755-80e3-359e-86d6-7c14a04f2bf2 | -19.1756 | -57.39796 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.8 |
| cfb858c1-db8a-3eaf-ab9a-aed54299b3b9 | -15.04556 | -48.09517 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 29.3 |
| b69676c9-b00f-392f-b639-c561ad10c690 | -14.56873 | -53.59818 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 70a3d43b-1096-3074-9fe5-6e18d854611f | -17.1841 | -54.30977 | 2026-08-31 16:48:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3642065b-9189-3a08-86ab-cfe8a1b21724 | -17.45413 | -52.41519 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 40670989-3d09-3ee2-960f-6c3a30443b16 | -17.6952 | -44.28124 | 2026-08-31 16:48:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e9d554b-a750-3554-9be8-20c61c08ebfa | -12.9812 | -40.71291 | 2026-08-31 16:48:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 630ed6e7-7c8e-3d5d-88ae-2307b62b94de | -15.98392 | -55.95744 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| adebee59-34d5-32e0-b8b5-aa98d526c516 | -19.2164 | -57.34647 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| d25a772c-9918-3d4f-bed7-4a8f619e1185 | -15.54707 | -56.28372 | 2026-08-31 16:48:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f45c731-4e15-3c23-a278-8337af525fd6 | -15.65863 | -56.38035 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fa05b07b-0c9b-3fe9-be2d-f91e3aa71ddd | -16.89348 | -40.21797 | 2026-08-31 16:48:00 | NOAA-20 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c6856e0a-0d25-3f95-bfe5-7d8b84390ba4 | -19.12504 | -57.3711 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.9 |
| 5764e251-e36d-3ed9-a507-e379e55c180a | -15.19493 | -46.24977 | 2026-08-31 16:48:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 824525fc-b689-3f7f-b74f-43b6f95022b1 | -17.8507 | -50.49951 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 1b6a020d-3d91-3e01-83fc-09b35e25ff34 | -15.63688 | -56.37966 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 45c23732-ae96-329a-95bb-52e2bc972492 | -19.15089 | -45.49835 | 2026-08-31 16:48:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e6ad9f43-9634-3cca-9abd-078452184fb3 | -14.97847 | -48.14302 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 18.7 |
| a5259de2-809d-3927-950a-030e00c5ea9c | -17.94749 | -44.57919 | 2026-08-31 16:48:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c16c97e-77c1-348a-9104-5699b4a07d74 | -19.23581 | -57.33693 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 2230e361-2fc6-328f-ba03-5b13b9cf9341 | -16.20242 | -48.7365 | 2026-08-31 16:48:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 1e052951-df23-3ba3-999a-3806902b86c0 | -16.17432 | -52.96562 | 2026-08-31 16:48:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e2c466c5-7c0f-3910-a4e1-a5dc5294e4b5 | -14.52377 | -52.18172 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c8be76d8-60de-3208-81ec-c41eee0efc6d | -17.53407 | -41.31707 | 2026-08-31 16:48:00 | NOAA-20 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.4 |
| 419e4f0e-18a0-343e-be72-7853e5d240e5 | -15.17543 | -48.71808 | 2026-08-31 16:48:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e979f1e5-fbb1-3838-8044-9c35b7788dcd | -15.46061 | -53.96251 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fe05bc36-d912-3e55-9cb1-30b10d25a000 | -16.97081 | -53.28434 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 4fc29d9b-7e9d-3687-afe1-e9ca32730e11 | -15.40532 | -52.70822 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9c387a93-72e6-3a37-954a-b3a47ef45c88 | -16.00863 | -54.39982 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e123d9f2-4d24-31a9-b7a7-853d66c0d7de | -18.50746 | -43.97306 | 2026-08-31 16:48:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0acc6bbe-8c97-3334-82b3-9dfee81da013 | -13.62008 | -40.64394 | 2026-08-31 16:48:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 29.8 |
| c6b660bc-cf99-3477-bed3-313972d8c0bd | -15.88174 | -56.47605 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ea14d020-e6c7-3f81-9164-4a913f1406e8 | -13.19339 | -44.07334 | 2026-08-31 16:48:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69e002b0-ba52-303f-86c7-67e5f901f257 | -13.07707 | -45.1698 | 2026-08-31 16:48:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6fb8a0f2-b071-37e3-bbff-5201fb7c31ee | -18.21102 | -43.98096 | 2026-08-31 16:48:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8b92be21-a852-3e25-94ff-c10f656249a2 | -17.85017 | -52.11025 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 4b0b0eaa-fd17-3a42-aef7-9ae307e848d3 | -17.87556 | -52.111 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 96b01077-c97a-3139-a711-205d5642c55a | -14.96122 | -54.58933 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| d0ebebc3-6460-34b2-bb00-ae1acaecc77f | -14.95927 | -41.40006 | 2026-08-31 16:48:00 | NOAA-20 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 65e73a07-e764-367f-b601-a4ff8a246ebe | -15.45723 | -53.96091 | 2026-08-31 16:48:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 68b23fd3-12ff-3b75-9697-4e3c73d8cba5 | -15.46463 | -52.82948 | 2026-08-31 16:48:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bbad824c-0194-36ef-b537-e214e8d14518 | -14.22962 | -42.41153 | 2026-08-31 16:48:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 557ee198-4c8b-3645-bcc4-f07861520322 | -17.88455 | -52.08224 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 96b65eb4-f3e6-3abb-b02d-85fc0e1b3ead | -16.55975 | -52.50958 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 48680a39-9a3c-31a7-8560-2e10c2479f16 | -19.16922 | -57.39402 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 8b60ab02-ac1b-3c7f-8777-34e6bab9f883 | -15.6468 | -56.37133 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff4075f7-569a-3f68-a79f-adb01815762d | -19.12032 | -57.38528 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.6 |
| 1dea0a83-5d23-3ec4-92ab-b3c1bb3976a3 | -14.36059 | -53.10665 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f0592b60-ff28-3474-b406-ac4d3915ba26 | -17.53585 | -52.55268 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5aabd96f-045d-3e27-8584-740c960e0335 | -17.85432 | -52.10972 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 9e2dac52-0ca3-301b-a298-ad77375beede | -13.55089 | -48.23236 | 2026-08-31 16:48:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 62e6193c-ff75-3bed-830e-fb611d4e033f | -19.17432 | -57.38433 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| de2313f8-82db-38c0-b992-26e2bf40391f | -18.26344 | -52.74733 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8b8f9516-83fa-3e81-b670-bab3c052924a | -14.40412 | -53.27275 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0477f3b2-835f-39fa-82df-f1e894cdcf4f | -18.41316 | -47.95779 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 20.1 |


[Clique aqui para ver as próximas entradas](README144.md)
