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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4dc3cc6-b6fe-3534-87ab-297b8548363d | -2.7131 | -46.13128 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d13592-a7da-3c01-92c4-314cec3cd15e | -2.95169 | -51.79359 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8beaf7fd-a52d-3044-a50e-148868825168 | -2.80969 | -45.94183 | 2024-12-01 04:21:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c043dae-3576-3818-bc6a-b8299ab917c4 | -2.64812 | -46.12149 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 480bc3cc-38e6-3dc9-b631-aa0934a4e5f3 | 0.94387 | -50.75282 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 19dde53d-5beb-3de2-ba38-77b2fa7f67aa | -1.01372 | -51.72577 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 67c4f993-25ec-3913-9491-69658e9ac495 | -2.26992 | -53.46539 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3a64f2b8-74b7-3489-8118-b57ec287e5f9 | -3.84219 | -46.51915 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cdae7bc-9f57-37b8-9823-ba81e964de72 | -1.10624 | -52.30064 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3ee383e-1065-3cee-aab9-ef64f13af227 | -2.69392 | -48.66174 | 2024-12-01 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d42f7ce2-c9dc-3fd5-bb71-ff9616c9322c | -1.99552 | -48.67646 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05c296d8-3fa5-3306-affb-711dcc6cb8b2 | -2.03141 | -52.07747 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7085bf18-3661-3979-baca-8e95863e1ad8 | -4.31963 | -46.53907 | 2024-12-01 04:21:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9c8a9887-0529-3575-afb2-8baebe6fd0db | 1.16081 | -55.98046 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1f55d09f-bf93-3431-9aaf-9a2250186920 | -3.19332 | -46.57619 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbfbbbb9-d4f7-36c0-8768-9a5e0d2ccdf8 | -1.70323 | -52.46474 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3adc8260-6f15-3acf-b90d-4d2aed74569e | -3.78293 | -46.69282 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5919fb47-f57b-3383-b60d-f386f9ddd284 | -2.66126 | -46.12732 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0c82e40-05ef-3f88-95b5-c0ef05c614f5 | -3.16196 | -53.24179 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 376eb5cc-6f71-3b1d-8715-f15bc4808d3e | -3.21789 | -53.13156 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a23a2731-22ee-32a4-a7c6-33e506d387ae | -2.68878 | -46.28931 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ce8e0fb-57ad-3d1c-922c-790a6e8adfa8 | -3.09932 | -53.72559 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b50b01ca-5b9b-3ef8-a21a-a25163abb737 | 0.9368 | -50.73821 | 2024-12-01 04:21:00 | NOAA-21 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8abbe40a-e162-31e9-a672-7bf4181a508f | -2.85555 | -54.10015 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d90ecf7d-d546-3a2e-9f54-1da6b9aed421 | -2.69211 | -51.72668 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f8f622ec-4662-3f30-8211-a3e0e6b017aa | -2.81163 | -53.04532 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73f93bc2-627f-310f-ba64-f32c7beb3f84 | 1.1541 | -55.98159 | 2024-12-01 04:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| db400503-6e17-3649-b879-7dacdf6600b2 | -1.47992 | -55.38431 | 2024-12-01 04:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91832257-802c-3fd1-bb99-e9e018bfae39 | -1.70741 | -52.47168 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d834ee61-c0a3-357c-864a-c5ff8c69442e | -1.26726 | -51.75425 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0e3acd5e-84cf-3afc-82c8-3c386b1ab95b | -2.46545 | -46.56466 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96a8b98b-8757-3e42-be18-95f843ee76ad | -4.70204 | -42.40029 | 2024-12-01 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f0291b9b-d801-3b0a-a6b6-6e9f5b0a43ed | -2.99319 | -45.57691 | 2024-12-01 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7368fe45-42cb-346c-8ee6-fedd3ddd4f6f | -1.48158 | -52.67738 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54f307c8-47f1-3c2d-b8cf-f3a638cf930d | -2.66678 | -46.5992 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 52bfdab5-06f3-3b02-8dd3-e4d019c3cd85 | -2.8302 | -54.09274 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5e9d8bf9-e7a8-390b-98c7-55f3798a40a9 | -1.14509 | -53.6713 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88392828-5610-3b9e-8981-843f3335903e | -3.66234 | -50.95188 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e258e9ee-4420-3e01-a643-164dd09d5aa1 | -2.77733 | -55.34439 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4dae9c10-9e1f-30e5-884e-e3e91eb531d7 | -3.4529 | -44.92214 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69f87b9b-3592-30fb-8509-a22b8cec39d4 | -3.85951 | -47.05622 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07684d91-57ae-3e40-82a1-3b90c5544229 | -2.52233 | -54.07653 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3b178c2-54e6-37ec-ae0c-2027f3772ebf | -2.57277 | -51.88445 | 2024-12-01 04:21:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 48bc8171-3991-3900-a241-b2b3113f5d33 | -1.08941 | -53.63608 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e89b360-3ef9-3931-804b-4f98d6f51471 | -3.98721 | -46.64239 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e4e56aff-ee01-331c-8e90-26d88565496b | -1.85822 | -44.76469 | 2024-12-01 04:21:00 | NOAA-21 | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98573f8d-6d5e-312c-ba7d-699d5c496ac1 | -3.74107 | -45.46867 | 2024-12-01 04:21:00 | NOAA-21 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cbff28d-fca2-3ecd-9c74-12fd23737e66 | -3.89395 | -46.67888 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63fce9dc-8e87-3782-b6bf-737e44efc039 | -4.55085 | -43.30933 | 2024-12-01 04:21:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d8232a54-da78-375d-9a5e-9cb296a01ab8 | -2.64468 | -46.12097 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b41dc817-4892-3fbb-b4cb-f303e9bdafbb | -3.40654 | -50.66034 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3ab008c1-8456-35b8-b97f-9ea319ab42bd | -3.19618 | -46.58059 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9ff01fa-a127-3718-9048-7232b50db36d | -1.51939 | -45.91107 | 2024-12-01 04:21:00 | NOAA-21 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cae27275-8bb4-3926-ba85-b5ef902cfefc | -2.38256 | -46.79008 | 2024-12-01 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67c9ce93-0522-3a85-8b97-5fb5a87ad0d8 | -3.93402 | -46.40317 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2b235ce-3364-3b5a-aa4a-7dae380ccd73 | -2.64409 | -46.1247 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63ab2b6f-068b-3ccb-a992-8d0377424e64 | -0.82164 | -51.60742 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 065b273e-0ae4-38c8-a557-327d14ee1027 | -1.84963 | -55.61777 | 2024-12-01 04:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5954ca7c-79c3-3058-a835-a20e4762db65 | -4.01778 | -46.99833 | 2024-12-01 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a2eecd94-a839-3d0e-9012-957761a0440f | -3.3189 | -50.14552 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f34f5bad-8967-311b-83ab-6c2d9eabfdc6 | -2.08252 | -46.66845 | 2024-12-01 04:21:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b54deade-48b2-3f42-8f67-3688fe62f92f | -1.15528 | -51.7051 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 73f40ff5-1662-3dae-9b00-4d33888e5f87 | -3.20898 | -53.12053 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 357575e7-5b84-3c08-8acf-70db4b60f802 | -3.32507 | -45.30204 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19dd72be-278b-341b-95df-78546ef739fe | -1.01282 | -51.73139 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 54b8c72c-b83b-333f-b01e-25fb7893e2b5 | -2.29099 | -45.60413 | 2024-12-01 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 9329df8f-cb36-363b-902e-4ac0fbfff23f | -1.6575 | -53.75301 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7969eef1-230a-33ac-ad2e-bea818ec790b | -1.09115 | -53.64837 | 2024-12-01 04:21:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddaf7887-defe-355f-b8ba-7179ec27dcf6 | -3.14284 | -53.84113 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57f81f88-562d-3a58-892b-719cf88c5c25 | -1.20741 | -51.73772 | 2024-12-01 04:21:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40ba326c-ef2d-3ea7-a95b-be5bb272d865 | -2.63506 | -54.20158 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 2b7cb801-39d9-3d9c-b3f0-48f5222e3e78 | -2.6332 | -46.12685 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17b3f640-5150-3007-9261-ef90c5fbe921 | -2.80003 | -53.05117 | 2024-12-01 04:21:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43e650ee-7ebb-3e6f-9017-9d9976a8f080 | -3.1968 | -46.57674 | 2024-12-01 04:21:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0cee895-a197-3e9a-b6c1-41c5261ce9c4 | -3.82052 | -46.58958 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d21402a-475c-3197-ac49-5064209d774c | -3.79682 | -46.69501 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e6a1a78-66a3-3814-8ec8-9a3c3774cf45 | -2.26466 | -45.51911 | 2024-12-01 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 351fe336-b3c1-348e-8fe1-13fd075233c4 | -3.03523 | -50.2442 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b775164b-64a6-3e96-b46f-fb7ada52fe6b | -2.76257 | -49.22615 | 2024-12-01 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8beb8d20-682c-32e2-a298-2f31811ad9f5 | -2.10207 | -47.62465 | 2024-12-01 04:21:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0bbdda2b-495c-35d5-95e5-87f6d59f5782 | -3.68535 | -50.24288 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b56d389b-c3f3-35c7-86e4-555b840bf789 | -3.54255 | -50.40426 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 12b02280-5e24-3284-9494-010065966edb | -3.38565 | -50.11106 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3992b05b-7bc4-3271-a6eb-c29c8bbd0000 | -3.34439 | -50.82339 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c41ce773-289b-37ba-9a38-5f706dfa44fc | -3.90694 | -46.4408 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5789a0b1-d872-329e-a94e-93a3ae473957 | -3.46859 | -49.99807 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec85f063-6cb7-32f8-96fb-71d2812748ef | -3.74849 | -49.93476 | 2024-12-01 04:21:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 90b6eb4b-1b28-30f8-8037-78f26377236b | -3.8945 | -45.01267 | 2024-12-01 04:21:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0c0509f-d788-3ec6-bfe7-93749fae41de | -1.94999 | -53.34497 | 2024-12-01 04:21:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 96ae647b-e2eb-3fd3-b323-8020f76920e2 | -2.88283 | -54.21487 | 2024-12-01 04:21:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a2f2c29-17b3-36e4-a907-55a048eb3e60 | -3.89936 | -46.64471 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b79602f-8696-3563-8f30-9cfdd4672512 | -3.42318 | -50.01097 | 2024-12-01 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ddcc080-cab4-3056-a0dd-5466f5e8485d | -1.69316 | -52.63605 | 2024-12-01 04:21:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd35b76d-0195-3bcd-ba04-96928a529e03 | -3.53752 | -44.94587 | 2024-12-01 04:21:00 | NOAA-21 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 857b3890-fd24-3dba-a0c5-9324ea15782a | -3.26883 | -45.37632 | 2024-12-01 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9834065f-1874-37ec-881d-3091e476cffe | -2.8366 | -46.85374 | 2024-12-01 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ffeb3a5-ed9a-3cc7-9853-cb6b0c304544 | -3.82911 | -46.60255 | 2024-12-01 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e003bcf7-8c6a-36f2-ba5e-1cfd00bebf2c | -3.09138 | -50.34917 | 2024-12-01 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b560502c-b660-38d3-bd62-f22b30435048 | -1.48074 | -55.3793 | 2024-12-01 04:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 866b99d7-6483-3bbf-89a1-757a2c978b71 | -3.14221 | -53.84489 | 2024-12-01 04:21:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README27.md)
