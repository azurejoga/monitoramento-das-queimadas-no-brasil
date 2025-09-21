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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 884ac27e-6d15-3ffb-a64b-2fefc285f9a7 | -15.978 | -59.4269 | 2025-09-21 11:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 4977e8b3-aba0-37ba-87d9-2c260f4cbbbf | -12.6088 | -45.1244 | 2025-09-21 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 155.1 |
| abfbfff4-e2c5-346f-afef-c0d95e2628c9 | -12.4357 | -45.1284 | 2025-09-21 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.0 |
| fcc3cbbd-2ef2-330d-9f27-96dcefd9fe83 | -23.1523 | -47.6245 | 2025-09-21 11:20:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.5 |
| f4944124-1b1d-3399-8409-d2ccfdc4bd13 | -12.4361 | -45.1052 | 2025-09-21 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| de35f264-0de0-3365-b2ae-d08a4bc1c242 | -23.1523 | -47.6245 | 2025-09-21 11:30:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.7 |
| c60424f6-38a3-3491-937c-79a998b627f8 | -12.4357 | -45.1284 | 2025-09-21 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9afced00-5380-3dca-9dc5-8bb19c4bec0c | -12.4361 | -45.1052 | 2025-09-21 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 101.5 |
| b14a5f18-306c-3302-91f0-a082aa183fbe | -10.0317 | -46.2561 | 2025-09-21 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 192.9 |
| cd0e86b5-9980-3bba-8095-1c287c5f819d | -10.0314 | -46.2786 | 2025-09-21 11:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 50fca98d-6eed-35f6-8a91-64b00dea0185 | -10.0317 | -46.2561 | 2025-09-21 11:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 8539ccec-4932-3227-a155-62861fa32b44 | -15.978 | -59.4269 | 2025-09-21 11:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 26951dd3-d21f-3e0c-9d65-5a3a113b3b0b | -12.4361 | -45.1052 | 2025-09-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 216.4 |
| 7ec1dada-fe65-3043-aca0-7dcabee18608 | -17.1179 | -45.9256 | 2025-09-21 11:40:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 57178337-0e6f-3203-9d7b-22fa60a17d31 | -12.4357 | -45.1284 | 2025-09-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 10db1561-7b8e-3818-8250-6c49ce19594d | -23.1523 | -47.6245 | 2025-09-21 11:40:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 121.5 |
| fb37a2fe-374f-361a-b9fe-ed7670b5f8e7 | -12.6088 | -45.1244 | 2025-09-21 11:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| ea960efc-f30c-377e-bcdd-b16d91ea7b40 | -17.1179 | -45.9256 | 2025-09-21 11:50:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 95.0 |
| fe20a1e4-47fb-31e9-b539-1565a2453213 | -12.7114 | -46.8454 | 2025-09-21 11:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| e6b4c1ca-cbbd-3216-a366-3e0ae065269d | -12.6088 | -45.1244 | 2025-09-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 38e30822-72a5-3230-aa0d-0ec09dc867f2 | -23.1523 | -47.6245 | 2025-09-21 11:50:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 170.0 |
| 7d8482b0-fcba-3b10-9cc7-a4280968c136 | -17.1173 | -45.9491 | 2025-09-21 11:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| dc6d7b47-4d8c-3e9a-9ead-6e0969fe89b5 | -12.4361 | -45.1052 | 2025-09-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 280.9 |
| a02e26d9-cc2d-3879-a69d-5728176059ad | -12.4357 | -45.1284 | 2025-09-21 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.2 |
| bcc46b7d-6f15-3f56-95e0-031582e319e4 | -14.8479 | -45.4846 | 2025-09-21 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 019fa7ea-cc96-360e-8df8-36dfdf141f62 | -7.82276 | -39.90019 | 2025-09-21 11:57:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 80398380-04db-3cc7-b452-e2bff740187b | -7.60172 | -44.49343 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1f6e1deb-7259-3c67-89ba-0723ebb7fbfe | -7.7195 | -44.45284 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 7969ed94-0024-3e86-8fa9-7822ceb40062 | -7.46127 | -42.63533 | 2025-09-21 11:57:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f3bf5422-7249-3fe5-89aa-8dc72015a030 | -6.84924 | -44.16771 | 2025-09-21 11:57:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 13d2c7e6-e98c-337d-bd06-33f3812f500d | -5.08877 | -43.08139 | 2025-09-21 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 271d4512-f6bc-3682-b2f6-193be193381a | -5.58435 | -42.14936 | 2025-09-21 11:57:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| a6b72698-cbc8-3479-aea0-2cc6c2a97c50 | -7.0315 | -41.70586 | 2025-09-21 11:57:00 | TERRA_M-M | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a14416b4-7d27-3582-acc9-97da33858427 | -6.19018 | -43.12089 | 2025-09-21 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 073efff0-799c-31c3-95cc-4c7cfc566f6a | -10.45701 | -39.55289 | 2025-09-21 11:57:00 | TERRA_M-M | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 9f75bd68-f815-3a23-b3ce-ff3053153c71 | -7.82137 | -39.91013 | 2025-09-21 11:57:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 9df95f88-1472-3d68-8f7a-05210dbc884a | -7.42005 | -44.54056 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 23.9 |
| dd8cc9a3-ac17-3ab4-88ae-5e98f9d11a99 | -6.92868 | -43.8648 | 2025-09-21 11:57:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| bfc4830d-6709-3d4a-9ca3-6e15e54b74d5 | -4.42061 | -43.0537 | 2025-09-21 11:57:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f9f7584b-c69d-3887-91b2-1addb412c710 | -7.17681 | -42.24166 | 2025-09-21 11:57:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7fd4f283-3e07-3e17-8b23-f71b387e84fe | -7.73857 | -43.93831 | 2025-09-21 11:57:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 054decf0-eb9c-370c-9ba7-c27062570889 | -5.59507 | -42.14821 | 2025-09-21 11:57:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 01163ce6-fa8c-3851-8154-364f6b0cf80c | -6.11538 | -44.01033 | 2025-09-21 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6e4b620e-0933-3707-afb3-ed4d91dfa06e | -9.88635 | -44.20885 | 2025-09-21 11:57:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 96a192a5-fa13-3997-b2f2-654c22a58268 | -9.18753 | -44.63316 | 2025-09-21 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 42d5ce10-7243-3264-b728-0e35d172cebf | -7.65456 | -41.61083 | 2025-09-21 11:57:00 | TERRA_M-M | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d3a7e253-308e-3a88-8075-a7dcf7f36fb7 | -3.68549 | -41.95817 | 2025-09-21 11:57:00 | TERRA_M-M | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d5f8be63-bf72-33b5-8d35-9151eda2e3df | -3.34372 | -43.22227 | 2025-09-21 11:57:00 | TERRA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 0a2b327c-1169-353f-8295-e8efee433fe3 | -5.52511 | -43.86681 | 2025-09-21 11:57:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 03ed262e-90cb-35a2-9b2b-4e4bdf0eed60 | -8.16341 | -46.78738 | 2025-09-21 11:57:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 493f9550-aa04-3e76-9cfd-0211afedbfa6 | -3.3917 | -41.628 | 2025-09-21 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 40.8 |
| f962aa0a-18b9-3f63-a1e4-1da4237d015f | -6.01879 | -44.32943 | 2025-09-21 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f59faa5e-028d-3a2f-8b0e-631b598328d2 | -6.74697 | -43.16204 | 2025-09-21 11:57:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 20.1 |
| bb9b9d09-3a48-39e3-8654-7ec8a81a06a8 | -8.30456 | -43.67634 | 2025-09-21 11:57:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9018d72f-0cca-35e8-a876-86022aae502a | -9.88492 | -44.21852 | 2025-09-21 11:57:00 | TERRA_M-M | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2285afe4-9df0-3443-96eb-289d59afeec1 | -2.96175 | -42.87544 | 2025-09-21 11:57:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6b8b4f59-8730-368f-841a-920fa5c4dd05 | -7.03617 | -42.0012 | 2025-09-21 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 93775aa5-fafa-39ae-9dce-3e51bdbf6038 | -7.18567 | -42.24291 | 2025-09-21 11:57:00 | TERRA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| c7e994fe-9fc9-3d3e-85be-6fefca2f515b | -4.61309 | -43.50084 | 2025-09-21 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 1a10a57e-2295-3d25-a478-360f2877afb7 | -5.56528 | -42.15577 | 2025-09-21 11:57:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 23e90899-530f-3d33-9c72-f882b11a0aa8 | -5.04528 | -43.06869 | 2025-09-21 11:57:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0d21ec8f-8c40-3efc-88d6-b041cf7cd71d | -6.5399 | -42.87693 | 2025-09-21 11:57:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| c34855e0-45f7-31c6-bdd4-d4f6d844e993 | -7.17915 | -44.10445 | 2025-09-21 11:57:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 382c1858-32c1-3e07-bee5-637ca044c4cf | -5.58306 | -42.15829 | 2025-09-21 11:57:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| af6bc979-d9f7-3b0c-b882-ba5fa85ffcf7 | -7.6191 | -44.44242 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 8c29c614-8f92-34a5-950a-50709644ddcb | -9.18903 | -44.62306 | 2025-09-21 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 39.2 |
| eacb729a-ce53-33d6-9b55-c2d1d2c80370 | -6.95677 | -37.87249 | 2025-09-21 11:57:00 | TERRA_M-M | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 2067f9a9-9532-3fdd-b0ee-38a88c4fd116 | -3.24129 | -41.96583 | 2025-09-21 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 89be2f4b-234c-357e-bb75-9c678c55cdf1 | -3.59144 | -43.90938 | 2025-09-21 11:57:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 40e4110a-e9ee-39f0-9848-b83d41373ca6 | -3.2426 | -41.95682 | 2025-09-21 11:57:00 | TERRA_M-M | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 22f84170-2030-38b4-9210-2349716b7aeb | -4.60221 | -43.50958 | 2025-09-21 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fb179137-05cb-3b13-9fde-e89f26d681c2 | -6.09144 | -40.99968 | 2025-09-21 11:57:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d657bce0-65da-3310-8556-60629e7b8056 | -3.39042 | -41.63688 | 2025-09-21 11:57:00 | TERRA_M-M | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 66.7 |
| 70110d42-f912-36aa-83f0-c630c924d778 | -5.09652 | -43.09227 | 2025-09-21 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7189b52d-aa3c-314f-955f-3e1df663fc5e | -4.60369 | -43.49952 | 2025-09-21 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0d876d1d-98fe-317a-a64b-181a66b02cc6 | -7.71795 | -44.46331 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 350ad080-65a5-37b9-a532-550853ad6ef2 | -7.95834 | -43.8925 | 2025-09-21 11:57:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a60e6739-445e-3a1c-b4c3-c677c30221d8 | -7.0395 | -43.43434 | 2025-09-21 11:57:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| e094ea5f-e2ac-3289-94a6-41f60e89e0b8 | -7.36698 | -44.56565 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 768eac5c-d4f9-3f1d-a200-a655dacbd24c | -5.80864 | -42.51171 | 2025-09-21 11:57:00 | TERRA_M-M | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| bc336f5d-bb6e-36a4-9900-a5a9c496bfa4 | -7.80698 | -44.70576 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7fafceec-4499-30cb-a20c-0c217df15ebb | -5.08735 | -43.09092 | 2025-09-21 11:57:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 84501004-4aba-3a4f-b235-c7e146691a11 | -6.81753 | -43.75521 | 2025-09-21 11:57:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c397731e-3f09-3d7d-b247-7dd5adb1ac81 | -7.51876 | -41.33421 | 2025-09-21 11:57:00 | TERRA_M-M | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| e50f0ae8-2ace-33b2-b3b6-457d593c3ea6 | -7.21242 | -40.24433 | 2025-09-21 11:57:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 47.9 |
| 0aa7e80c-a7bb-3b14-a1bc-f6d24cad50bb | -6.95507 | -37.88521 | 2025-09-21 11:57:00 | TERRA_M-M | CAJAZEIRINHAS | PARAÍBA | Brasil | 2503753 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 5834d6a9-a20b-314f-8926-86a4d96a838f | -7.37498 | -44.578 | 2025-09-21 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 526815e9-a34a-3249-8b80-af4fbf913c91 | -7.20329 | -40.24306 | 2025-09-21 11:57:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 692243dd-6aab-3966-99b9-4df8ccbf6ee2 | -4.61161 | -43.51091 | 2025-09-21 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 1981a888-d853-3553-a20e-c94cbdc560e4 | -3.9105 | -41.41634 | 2025-09-21 11:57:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| b18fb866-5ed5-3b8a-9f81-f022052bb488 | -2.94965 | -42.89359 | 2025-09-21 11:57:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6e9b66ef-326b-3b44-bd5b-16c30a223ff9 | -5.51972 | -43.86995 | 2025-09-21 11:57:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 20a42187-18fe-3741-83ea-f5ec57f9756a | -8.85291 | -44.40158 | 2025-09-21 11:57:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 14e9e238-3fea-3b72-909e-f319fa9e1925 | -6.39379 | -43.30696 | 2025-09-21 11:57:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d7f7f53d-824e-38a1-a990-e28bdb3dcfdb | -12.4357 | -45.1284 | 2025-09-21 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 132.3 |
| e87910cf-7e16-337d-8e9a-e4a1d8b67511 | -12.4361 | -45.1052 | 2025-09-21 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 153.2 |
| d2d7811a-ec3a-359a-a9ab-152d2a51d0ae | -12.7114 | -46.8454 | 2025-09-21 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| d18e57cf-996d-32bd-911e-560a9ab34277 | -14.8479 | -45.4846 | 2025-09-21 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 2b37052d-67a1-39d0-8d2d-462fd995b282 | -10.0317 | -46.2561 | 2025-09-21 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 5575c810-012e-3c87-addf-afd6f49d1c42 | -23.1523 | -47.6245 | 2025-09-21 12:00:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 227.3 |


[Clique aqui para ver as próximas entradas](README48.md)
