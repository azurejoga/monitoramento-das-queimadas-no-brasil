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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3698c40b-f197-3cea-ad25-1268b56ae9fe | -3.5646 | -43.6117 | 2025-10-28 13:30:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 6aec65b0-989a-3b84-9937-5bf4be9e8f24 | -4.4604 | -43.6337 | 2025-10-28 13:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f4eaf298-b7da-3245-8051-82d1e13dcbd5 | -3.7075 | -41.556 | 2025-10-28 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 139.7 |
| ed90ae2b-da45-39f5-b9bf-8a40e4da4e7a | -13.2258 | -47.1066 | 2025-10-28 13:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 9496821b-c777-3350-b2d3-c9322aa4a2a0 | -3.5831 | -43.634 | 2025-10-28 13:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 73d41563-993b-3c43-a091-e9fe5d74500d | -13.9465 | -47.7595 | 2025-10-28 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 8c98207d-8be2-31ca-941f-4baf7571be5e | -4.9985 | -44.1311 | 2025-10-28 13:40:00 | GOES-19 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 73735684-397d-3967-8f9c-7c8697a36c64 | -12.3484 | -50.1779 | 2025-10-28 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ac40215b-c075-3814-8c31-f0588ff32640 | -3.5645 | -43.6348 | 2025-10-28 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 793e5aa5-a5ec-3fe1-8898-fd346e2a56d8 | -4.8933 | -43.2349 | 2025-10-28 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 54ab5409-87d0-3ef5-aefa-4c36631a58c2 | -12.8299 | -47.7254 | 2025-10-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 453.4 |
| 9c377d79-b8c5-3f89-b9f7-6b13932ae7b3 | -7.3613 | -42.4399 | 2025-10-28 13:40:00 | GOES-19 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 537d94f6-fd6a-3eab-b788-4c40f2a99bb7 | -3.7261 | -41.579 | 2025-10-28 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 107.9 |
| 2b16cb24-79d6-3650-87da-0777d95dfca8 | -3.2232 | -48.7594 | 2025-10-28 13:40:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 2181abe0-af9d-3448-b414-ae4030fc5ae8 | -6.5605 | -41.5859 | 2025-10-28 13:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| f0bff839-f06a-3d4b-b21c-ffe76d15494e | -6.3031 | -44.7014 | 2025-10-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 26072f32-f854-391a-94ea-606a3aa9ce4e | -13.2695 | -47.8622 | 2025-10-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 60dfe616-68a0-32ac-a98e-c688e8729fca | -3.7075 | -41.556 | 2025-10-28 13:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 89fc805d-fa43-3f95-8444-989e5d0c5a0e | -6.0974 | -44.6718 | 2025-10-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 231.1 |
| d31eec40-73f8-3cf7-8040-4a04685c2823 | -13.9337 | -48.4305 | 2025-10-28 13:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 5b60702c-1f26-36bb-928a-14581322871d | -13.2691 | -47.8846 | 2025-10-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 0f8ea940-57cc-3e6c-92c7-d11a989a669e | -5.5878 | -45.1865 | 2025-10-28 13:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 09ee4a8c-7cc3-3ac4-a516-c4ac0dbf2ad9 | -13.9143 | -48.4335 | 2025-10-28 13:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 274e7c76-1029-3dc0-ad2d-92d2944c8164 | -12.7786 | -47.3752 | 2025-10-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| ad212ba7-a08d-362f-b29c-a7044bec6b0b | -11.7045 | -51.2152 | 2025-10-28 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 819d5ee1-282f-3458-9add-5bfae0ff5fd6 | -12.8303 | -47.7031 | 2025-10-28 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 1428e306-3afd-3fdf-ba9c-1d7a79829087 | -3.5833 | -43.6108 | 2025-10-28 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 71f35985-4799-385f-a94b-7f99efb0e761 | -3.5646 | -43.6117 | 2025-10-28 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 166.3 |
| b7b2c6e4-20a0-3246-8020-df6ff8ccc95a | -13.5655 | -49.5845 | 2025-10-28 13:40:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 116.2 |
| a8a73029-0050-3237-aa8a-39883f7f3205 | -3.6019 | -43.6099 | 2025-10-28 13:40:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 907401dc-90f3-3a06-adeb-ad4310786326 | -5.6055 | -41.1145 | 2025-10-28 13:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 6cb25ff0-b899-3928-a693-19ca3a1d6bc2 | -3.0946 | -44.4362 | 2025-10-28 13:40:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 928aa4d2-a05d-32c4-8baa-b2d4fef9f73d | -13.2258 | -47.1066 | 2025-10-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 5668a6e0-9b7b-38c0-a8ab-20a9fd35973e | -12.8941 | -43.363 | 2025-10-28 13:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 135.3 |
| d79f13a0-22a7-32d5-a850-581f6f16a6c6 | -13.9275 | -47.7401 | 2025-10-28 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 3d1baf6f-d87d-35dd-9725-c7be7e8605b1 | -13.2262 | -47.084 | 2025-10-28 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 3128fe81-f255-3b76-afc5-cc50a2fbb2c4 | -6.1189 | -42.4375 | 2025-10-28 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| c0ba025c-f7fe-3c99-95dd-a8c8a3b3036d | -4.5659 | -47.317 | 2025-10-28 13:40:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 1a4eb6d9-7130-30e1-8959-a0ec24cf5704 | -15.1964 | -47.3964 | 2025-10-28 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 7e10cd00-69b3-32cd-bb95-038417101436 | -4.4599 | -43.7032 | 2025-10-28 13:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 4202256a-e310-31eb-9937-5574c3b7996d | -6.0786 | -44.6733 | 2025-10-28 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 241.6 |
| 1a5dca7a-a485-32c0-8354-de9feb210ee4 | -14.542 | -48.0012 | 2025-10-28 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| a1ed276d-33a9-32f9-be3e-6c71aec5b1e7 | -3.5646 | -43.6117 | 2025-10-28 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 152.9 |
| 62ca8cca-d4f0-3795-a9b3-3b13130aad47 | -3.6019 | -43.6099 | 2025-10-28 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 3b0362f7-1462-3a27-8d33-eec653995b33 | -7.0693 | -44.9563 | 2025-10-28 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 0f7e7f1d-8d55-34df-97ba-1dbf5909bab1 | -13.2691 | -47.8846 | 2025-10-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| f358dccf-2bb1-393d-a764-c30b2108e870 | -3.5645 | -43.6348 | 2025-10-28 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 82d9b847-665f-33ce-9af2-56d7622a36cf | -4.4431 | -43.4259 | 2025-10-28 13:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7f5794b1-8837-3efd-b226-4ca5a9971f53 | -13.9469 | -47.7371 | 2025-10-28 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 56.6 |
| f6df3d1f-4f21-304d-b2b8-7ef74089325b | -14.3934 | -51.8226 | 2025-10-28 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 54d71187-270c-3cc7-b11c-48c15602011f | -6.5605 | -41.5859 | 2025-10-28 13:50:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| e887df86-644a-3f04-b32a-636634c76ba5 | -3.9992 | -49.0508 | 2025-10-28 13:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| f0e2c732-c347-3b33-8b87-03f6c69e6b12 | -7.3426 | -44.0359 | 2025-10-28 13:50:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 0eec4aa5-a97a-3340-9a24-6fc4e69be9ff | -4.7346 | -44.4457 | 2025-10-28 13:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 803c3d95-b357-3e38-abbb-b9a6c04f15b8 | -13.2695 | -47.8622 | 2025-10-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| fe5383e0-814a-32a2-bc10-93bb3e465e64 | -3.5833 | -43.6108 | 2025-10-28 13:50:00 | GOES-19 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 215.6 |
| d0c1ea14-404a-3934-b6ea-d647400599cd | -13.5655 | -49.5845 | 2025-10-28 13:50:00 | GOES-19 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| b158bc8c-1ca5-3481-9654-e647c44f6247 | -13.8743 | -48.506 | 2025-10-28 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 7989c491-c300-30d0-b33f-4c9237832304 | -6.6707 | -45.4214 | 2025-10-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 63264f87-17b4-320d-ba43-45765b31aa6b | -7.6114 | -43.5914 | 2025-10-28 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 58674558-c3db-3080-a62e-d98e04562bc8 | -12.5486 | -49.6119 | 2025-10-28 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 715a8861-cf01-3204-aa35-8fa3cd740ffc | -3.7261 | -41.579 | 2025-10-28 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 115.1 |
| 7f7b5479-9b51-386c-9160-48b6693f3f6d | -12.9135 | -43.3596 | 2025-10-28 13:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| deebdbe9-1baf-3f63-aac8-ed887e7c1959 | -13.9465 | -47.7595 | 2025-10-28 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| a7e9d02a-2975-30a4-aebf-800bb6dad582 | -7.0881 | -44.9547 | 2025-10-28 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| a2f13845-9294-3ec5-82c2-13519459b5d0 | -6.0786 | -44.6733 | 2025-10-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 204.0 |
| f65be3ed-1ea2-3670-9c07-3925a40db7c0 | -13.2262 | -47.084 | 2025-10-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b410ca1c-fa86-3e43-84ef-2b369ff04d97 | -12.5298 | -49.5926 | 2025-10-28 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 85a8e4f3-b67b-30d5-9cda-9ac3a2d128db | -4.8933 | -43.2349 | 2025-10-28 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 4572faca-981f-34d4-8509-ed6bd588dd52 | -13.9275 | -47.7401 | 2025-10-28 13:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 022f26fc-0348-3554-a67c-685a218dda43 | -13.9143 | -48.4335 | 2025-10-28 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 63aae180-d013-390a-bf04-d5575874f4a3 | -12.8941 | -43.363 | 2025-10-28 13:50:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 12df69c0-1e5e-3d8e-9c03-f45fd4eaa2c8 | -13.6237 | -46.4779 | 2025-10-28 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 71cec1ce-2f22-3527-82ff-eb6790ec86db | -7.0883 | -44.9319 | 2025-10-28 13:50:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 876baa5e-88e5-37ef-a2a1-43c27e181647 | -13.6435 | -46.4519 | 2025-10-28 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 62.1 |
| ec6541c1-31f4-37a6-b4a9-39844e1261aa | -3.5831 | -43.634 | 2025-10-28 13:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 122.1 |
| f3286db6-4dd6-346f-a6e7-94ff5396db82 | -12.7786 | -47.3752 | 2025-10-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 87ea6bd7-487a-3771-bdcc-fccc79cf7bf2 | -13.9337 | -48.4305 | 2025-10-28 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 713bd65b-4f1c-3b95-a49b-8313f057a88d | -3.9993 | -49.0295 | 2025-10-28 13:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 5020cfe0-badf-3ead-8159-7d8c2916aa5a | -12.5489 | -49.5901 | 2025-10-28 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 48bbb9cc-bfab-3417-8422-ca16c9202037 | -15.1964 | -47.3964 | 2025-10-28 13:50:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| bced3d80-5544-34d9-a4ae-3d3fb40e18e0 | -6.0974 | -44.6718 | 2025-10-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 212.8 |
| 1021b23d-4f86-3048-a719-75416d6c5859 | -6.4785 | -42.2159 | 2025-10-28 13:50:00 | GOES-19 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 1e803ff7-7868-362f-94c5-965a72a156a4 | -3.0948 | -44.3905 | 2025-10-28 13:50:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 3bc5ddc8-4211-3c54-bbb9-bd11f9220b9c | -6.9857 | -43.9997 | 2025-10-28 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| f5c8dbca-1211-32c1-9ba0-6734de12f8ce | -5.6617 | -41.1341 | 2025-10-28 13:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 02e8aca0-9d50-34d3-bb2f-d0ca4f751800 | -7.5928 | -43.5699 | 2025-10-28 13:50:00 | GOES-19 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 9d35d493-920e-3f02-ab2b-faf823252340 | -4.7252 | -43.1991 | 2025-10-28 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 8bafb09c-4b60-393d-89f2-0ee731b894e7 | -13.8739 | -48.5283 | 2025-10-28 13:50:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 9c40eca3-ce68-378a-919c-cdc647d4bbf5 | -13.6241 | -46.455 | 2025-10-28 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d03df304-bc08-3fc2-817d-1c90b4525b73 | -6.3031 | -44.7014 | 2025-10-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 353d8f91-65df-3c51-b428-dfb44289d174 | -12.8299 | -47.7254 | 2025-10-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 5a336608-eb97-3e61-9c18-93add8e4efae | -3.7075 | -41.556 | 2025-10-28 13:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 125.9 |
| a4d6e186-5646-3583-b562-4a8477014448 | -6.6414 | -44.6051 | 2025-10-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| e8bde315-d867-3049-aa42-6315234eb2da | -4.864 | -42.2015 | 2025-10-28 13:50:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 82.9 |
| 8b3742ee-ca70-3d5f-be19-ccd67c488c79 | -3.2796 | -44.6565 | 2025-10-28 14:00:00 | GOES-19 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 2f898960-76f7-319e-9a58-f29164cb3dc0 | -7.7678 | -44.6855 | 2025-10-28 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 609cad34-e781-31d7-927e-fa586caa117e | -4.2467 | -44.8833 | 2025-10-28 14:00:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 51ae2097-9910-39f6-b32b-aedc8c80f72c | -4.3237 | -41.8078 | 2025-10-28 14:00:00 | GOES-19 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 84.0 |
| 2753b01f-f8a3-3268-95b1-516e8e601362 | -4.5659 | -47.317 | 2025-10-28 14:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |


[Clique aqui para ver as próximas entradas](README91.md)
