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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e0f6f63-62d9-3240-9b02-e2833a7168a8 | -12.9909 | -47.3217 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 10d190eb-197d-3eb8-8fb8-ab3e140deb0c | -6.3921 | -41.4811 | 2025-10-16 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 128.4 |
| 8eab02c6-1c14-345b-897a-fce5e869d3ec | -12.2844 | -47.1319 | 2025-10-16 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 198.5 |
| 0a2febe2-faeb-38cc-b6e9-88050a837f29 | -4.1338 | -42.2 | 2025-10-16 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| d85a840f-baef-3f4b-8cc8-62dc84584e79 | -7.0956 | -44.2667 | 2025-10-16 14:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 8c463cc4-0900-3685-9106-ff5cf23c7df8 | -5.8799 | -43.8844 | 2025-10-16 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 0411fa16-b0d4-38f1-b2c5-25701dde074f | -13.0106 | -47.2963 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 0539c895-2bfa-3873-9f7f-35ea4cf467d1 | -5.6097 | -42.6914 | 2025-10-16 14:40:00 | GOES-19 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| bc4466ac-7d01-3330-b478-fc00469b3ed8 | -12.9565 | -47.102 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 01adc53a-4943-3231-85f7-1780086c4098 | -10.8289 | -43.9482 | 2025-10-16 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 52972258-9c40-3510-90ad-7ed5faa58e66 | -12.9179 | -47.1078 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 4c050b62-5a31-3a83-908e-0f66c00e1dfb | -9.2694 | -45.2799 | 2025-10-16 14:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 159.4 |
| d6df8dd2-df32-3c7e-8ed6-187047ba544b | -8.4717 | -44.1746 | 2025-10-16 14:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 244.7 |
| 538baf1c-3865-3763-b5f9-dfc97beca02b | -8.2464 | -44.0832 | 2025-10-16 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 544a4acc-c2d4-3d95-8f01-f7fc9deee3d5 | -3.7628 | -41.6967 | 2025-10-16 14:40:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 111.1 |
| f7ce75f8-b0b5-3a60-b194-cb4a7815de49 | -4.115 | -42.2011 | 2025-10-16 14:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 142.4 |
| a52f46db-2bbb-313d-a610-f3666a66f8bb | -8.2653 | -44.0812 | 2025-10-16 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 177.3 |
| 9a665b33-aa9d-31ec-860b-66fb75c2bc59 | -13.4412 | -47.9483 | 2025-10-16 14:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| a05619a3-cd36-36e9-8c4a-d3f721a02fd2 | -10.673 | -45.3125 | 2025-10-16 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 01fd9210-ecd5-33ea-acbf-b9dc8456553e | -8.265 | -44.1044 | 2025-10-16 14:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| daec1b47-f792-3fed-8d7f-b3bca209d9f4 | -13.0094 | -47.3638 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 20b218d8-2120-3c01-82ef-8d89d330c4bd | -12.4866 | -45.4895 | 2025-10-16 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| ead41a88-c67e-3fd3-8145-723f24e936b4 | -8.2744 | -43.381 | 2025-10-16 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.6 |
| 53e35775-48c5-3d9e-a3a2-cb32783623c0 | -7.4866 | -44.598 | 2025-10-16 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 80fa6bf4-133e-366a-988b-563b638b1af6 | 1.8402 | -55.7034 | 2025-10-16 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| e8bcf0f0-1eb8-32df-80c9-82d5ad68d333 | -8.2924 | -43.4493 | 2025-10-16 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 6192b28b-a26e-3852-b708-3d476dcc6d29 | -4.3874 | -43.3827 | 2025-10-16 14:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 300.7 |
| 099f7c98-ebd2-3dcf-a2c7-5dd94c168913 | -6.4222 | -44.0258 | 2025-10-16 14:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 127.6 |
| a42e2487-f8a4-3b95-8f40-9abf65947bd9 | -6.3733 | -41.4828 | 2025-10-16 14:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 403.8 |
| 64db7607-ef26-33ae-a9d9-2fdb091c49e4 | 1.8401 | -55.7232 | 2025-10-16 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| ec681c77-77e7-3f06-9a46-b49b1baf1dbd | -12.9372 | -47.1049 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| e1379156-a87c-3cd0-9f18-d4124a432ba9 | -10.133 | -44.5777 | 2025-10-16 14:40:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 217.7 |
| e3fc9449-cca5-3142-aefd-592710a37321 | -8.2362 | -43.4086 | 2025-10-16 14:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.3 |
| a12bde3b-b3cd-3b47-a4fb-2b8e23c107be | -9.3788 | -46.957 | 2025-10-16 14:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| 0e0bf5bf-72dc-322c-9a3a-bb012ba3ebc2 | -5.4561 | -41.0054 | 2025-10-16 14:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 135.6 |
| bc691337-18ac-3e79-bfd4-9e1f0c4d4ae9 | -13.0102 | -47.3188 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| bfbba0b0-1f04-3c88-801e-82dab15bef06 | 2.0782 | -55.7789 | 2025-10-16 14:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| e8d31fdd-11a6-3548-a260-7cdc21311eab | -6.4255 | -41.8865 | 2025-10-16 14:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 1415e706-5238-3d6f-8c32-cf1ea40036c3 | -11.418 | -44.1435 | 2025-10-16 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 527.2 |
| 11a37521-80e4-3fa3-8e3a-65faf0069e7e | -4.7937 | -46.6228 | 2025-10-16 14:40:00 | GOES-19 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 70.8 |
| b1f82c2d-4d83-3e4c-b4f8-b2c55357c7d8 | -12.9905 | -47.3442 | 2025-10-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 6bdec9ba-939d-31ec-9b67-4f852fa3ca65 | 1.7479 | -56.0791 | 2025-10-16 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| b9faa19e-fb66-3527-862e-d78966890b4e | -12.3112 | -45.6311 | 2025-10-16 14:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| c31a59b9-6dc4-3473-82bd-ba3254be9a08 | -8.5608 | -44.5803 | 2025-10-16 14:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 4977f8b1-df79-36d7-a2bb-48016c359852 | -10.6539 | -45.3151 | 2025-10-16 14:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 0bf244a0-2649-3f0b-a3c1-4bab169973d6 | -19.0319 | -57.5382 | 2025-10-16 14:40:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 93.0 |
| 7644e011-e44f-3038-8328-37895d710512 | -8.2452 | -44.176 | 2025-10-16 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 137.1 |


