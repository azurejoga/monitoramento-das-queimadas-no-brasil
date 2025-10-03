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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22539f2e-fadf-3c1c-a5c7-de361c6a501a | -12.64454 | -46.87566 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53c50170-b42d-3904-bb3b-026dcef2f14a | -12.6146 | -46.96756 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a258b311-5336-39aa-8f6e-be95ed8d5cf7 | -11.90798 | -54.82988 | 2025-10-03 04:34:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d88ae1db-54e1-382e-b2df-48912043347f | -12.37254 | -46.51472 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f19366c8-2fad-3c55-be18-c3fd7d53983b | -14.87952 | -48.30122 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 329a0bdc-00a5-38c2-a719-d42800b76d44 | -19.14783 | -41.50003 | 2025-10-03 04:34:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d482cbf0-f0ff-38d1-84bb-eaf51e2965a0 | -13.97461 | -48.15868 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14da7453-200c-3404-b38e-8fde519f8d6b | -13.37803 | -47.28425 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19cafe01-b9cb-3395-9340-02ed8e992073 | -14.85876 | -48.27891 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4826a083-237a-316f-b035-77275ec2234b | -10.89374 | -56.19553 | 2025-10-03 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cd13076-acd2-3420-a1ea-3ed2caacc300 | -12.25883 | -49.16002 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccf506eb-ff73-3717-a042-8f479010d885 | -12.62796 | -46.96434 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d42d73c-0f32-3801-b3fe-717961e19118 | -12.93693 | -48.42797 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9238f568-784a-33f5-bc48-55ee384560db | -14.72031 | -48.20353 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 250eafd5-cc45-361d-a0ff-8126c8b21eef | -17.9876 | -45.02852 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa6ec3d7-b444-3a46-9209-dc5d16674ccc | -13.57993 | -48.19382 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86244ed6-c117-3a35-a2b9-b08b0bfd1bae | -17.35308 | -49.06936 | 2025-10-03 04:34:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81619e98-7739-33e4-9820-8e70e22db477 | -14.5534 | -48.23785 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc105808-6be1-32eb-88b6-03b29b087f8b | -15.24531 | -50.11781 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a82841e-6d41-3e7c-a27c-3c61a5340644 | -13.78385 | -48.0764 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 199a70c1-7c43-3beb-bd12-f4601129b276 | -12.90048 | -47.18155 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f3fea7c-27ea-315f-bca1-d8a485eefdd9 | -13.12422 | -47.85102 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afd992b1-95b3-329c-89e4-257ca2270be6 | -13.77551 | -47.57331 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4090f437-735c-3b07-bee7-c0a2c1ad4f7c | -13.17397 | -47.87372 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 770db09a-7652-3ab1-9217-7247c9147f0f | -13.23875 | -48.49506 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e0cdc68a-cce4-3512-84b8-a4e3008e77dc | -13.28437 | -46.99298 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22d7552a-49d5-3e73-b591-d4413562ab33 | -13.58383 | -48.19075 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 482f7f2d-b0a7-3ae9-ad3f-04f9a39c6b59 | -15.92214 | -43.33926 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 204baef3-2400-300a-8646-bb0f9fd88589 | -12.90726 | -46.36433 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d2ae801-695c-3437-bcc7-8fe096b0ca78 | -15.30799 | -46.28119 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241e6df5-f576-3920-8fb7-e55323bb1d02 | -16.05967 | -47.77993 | 2025-10-03 04:34:00 | NOAA-20 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27723b1a-8cc9-32fb-9666-c5dbc96d5a47 | -13.12648 | -47.88133 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aff311c8-88de-3f15-9617-f744cc4ffdd0 | -13.32747 | -47.20286 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0a6ba3ae-6ca5-3e56-be49-234cccaafbed | -14.90479 | -48.2938 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52f3b9fc-8916-3ef4-b3a0-c2b507497b95 | -13.80782 | -51.30322 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d9be544-8dfe-3404-b083-8e5366c578e9 | -17.18014 | -47.01554 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f07224f-7566-3a96-9473-f5f0dfe4aa76 | -13.56788 | -47.58136 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3a2b219-4101-3fdd-85cc-a6d46e24ad09 | -13.76038 | -48.06193 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ae28904-5a2e-363c-b333-e10e4a9e9f4e | -18.63025 | -50.68331 | 2025-10-03 04:34:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be2bc300-386e-3220-b194-80e22143020b | -14.66769 | -48.26725 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 54d580a0-6769-3d8c-a45b-a91b767cbf68 | -13.23039 | -47.35868 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 454dbb71-9c5a-36c6-b24c-ee2248a3c740 | -13.86749 | -47.93497 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5100cc7a-fb33-3094-a5d4-9eb75934a64b | -16.02533 | -50.93372 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23c460b3-29cd-362a-92b4-1cdb855fa730 | -13.75589 | -48.06868 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52e807fa-4731-3b39-bf5b-599fda02e133 | -14.93807 | -46.88871 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 311806f2-0f1a-39d7-bbf6-368650197197 | -16.68769 | -53.02489 | 2025-10-03 04:34:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df76d97d-6c5a-3d80-9087-28d9ce1a2cc0 | -12.63776 | -46.96971 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a55f3231-6993-3a7c-8642-f4229ed3d9ad | -13.76592 | -48.08098 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78d72771-1643-33f4-a195-e923738f6c21 | -17.98256 | -45.03549 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6506a668-20fb-3898-b834-5ff3e8da8caa | -14.72955 | -48.11052 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8911c1a3-da5d-3389-bae0-940202239948 | -13.84834 | -47.92432 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 351561c3-bc47-33bd-a9ef-9b52af3f445b | -12.69449 | -48.54642 | 2025-10-03 04:34:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37b1a7a8-a427-3385-8d40-dfdfa2b6e40e | -12.87794 | -46.93077 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70e7551f-272e-3352-97b3-5d1487b1d3f9 | -15.57072 | -48.19521 | 2025-10-03 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27291d6b-a89e-308e-87f9-8c5b536287dd | -13.24486 | -48.49966 | 2025-10-03 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 758b75ad-7223-3dca-93e6-7f28ff0713c6 | -13.77481 | -47.53128 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dd17ac4-28d9-3340-ab84-726de25c9f3d | -14.98061 | -49.96728 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b426d367-e0d5-36fc-892f-16aa8eab54ac | -18.64018 | -50.68504 | 2025-10-03 04:34:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c3d4958-f014-34b3-8206-f8eb1591bbfb | -15.20248 | -47.99501 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ae894ed-1f88-39b9-82e4-a0a93910b88e | -13.37851 | -48.13644 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5eb8f373-8e51-33f7-bacc-ce1ca6950895 | -18.40448 | -50.77917 | 2025-10-03 04:34:00 | NOAA-20 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 08ccbef5-5ec4-3a9f-b006-f3def0d9c74a | -19.97082 | -41.66022 | 2025-10-03 04:34:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fa6d0d1f-75af-3435-95c6-b7685fcedce7 | -12.62973 | -46.97624 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| aa0eb85a-4615-33ae-99ad-b9839ab50ff4 | -14.89635 | -48.34907 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 6b9b9582-8c02-3a64-8cbb-d07ba5432dcd | -15.5154 | -46.81256 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f8a1e98-0958-3f75-ba0e-55a4fccb0c2f | -13.16728 | -47.89508 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc2216d4-484e-3a25-bc6b-34821a00e593 | -12.75446 | -50.55864 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6ca24453-a74e-32af-9033-9b326e381770 | -13.14387 | -47.83544 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc219de9-60cf-36d2-b761-78481d8f4570 | -15.99764 | -50.91415 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b2f5362-af6b-3319-8137-221df8a94afd | -15.36625 | -43.66623 | 2025-10-03 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a49623f9-57ca-355b-816b-59e57a016bc4 | -13.30772 | -47.59135 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 54028628-f8a4-38aa-9a77-10584ef0f1af | -19.971 | -41.6571 | 2025-10-03 04:34:00 | NOAA-20 | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3ecd88e0-587f-397c-936c-895614d86edc | -13.74353 | -47.99154 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f76fdbe1-6d09-3fb6-b31f-ee83f8298fc9 | -15.22974 | -48.06882 | 2025-10-03 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| caaccfc2-243d-3a76-8f97-6cc4f502e34b | -13.22013 | -47.35696 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 31fd92c4-7a7e-3529-a049-880315d34082 | -14.74199 | -48.1051 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82b008e5-b227-3070-ae3c-5ba5d020866b | -18.19293 | -53.28794 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba6a3f62-e176-3a8e-8e7b-145d69901498 | -15.60406 | -46.92384 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12ec3b2d-011f-31ee-94f6-2b9bc63c6ce3 | -17.18375 | -47.01608 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8ae5cdcf-8b64-3ffd-8011-5d0dc0830bd8 | -12.59736 | -47.01167 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66521ff5-a92b-3f7d-badb-1babd9e2e829 | -12.81196 | -46.86107 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 533fcbd9-48ec-3830-a082-1af0ddaec927 | -13.20659 | -47.8861 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c493b6d-ec4b-3ebb-9154-617dc316596b | -15.91714 | -43.34299 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c556d353-eb31-3fa9-9ac1-1a3094806d9d | -13.79488 | -47.58388 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60abb428-7d9e-31f7-a344-bd4f0b752853 | -14.70111 | -43.89163 | 2025-10-03 04:34:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 4def9d81-b4aa-3255-a8c6-e4308e079382 | -14.23151 | -46.11568 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ac3a38e4-3330-38ed-b0d0-3228040f3568 | -20.12888 | -44.00402 | 2025-10-03 04:34:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c90e651d-58c9-31b6-81d3-1846ed8426d1 | -19.86933 | -43.64445 | 2025-10-03 04:34:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7b0191f9-46a1-33b5-b94b-8137b4586f6a | -14.91268 | -48.34412 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb370577-d885-3843-9b65-4754113c6134 | -14.87225 | -48.30363 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e8531886-0e19-32ea-9098-5a2fcfe550e2 | -16.01433 | -48.34419 | 2025-10-03 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d92745a-afaf-3289-a76e-611fb22dceec | -16.68979 | -53.0127 | 2025-10-03 04:34:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 407457c6-b470-3200-84d7-d0effe03b573 | -12.78033 | -47.72172 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78bb191e-144b-3f7a-b887-629c275dbb1e | -19.72787 | -46.56002 | 2025-10-03 04:34:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ae9a7133-5111-3ee7-8f06-a1002fdac866 | -12.38487 | -46.52861 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ca731d8-9cef-301e-84ca-c61ec0465dba | -18.22726 | -53.34254 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96ead3b5-6cf6-3eb8-b501-fb219e914c75 | -15.27567 | -49.32159 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67edaf1d-0add-35b7-ba1e-8082a42a92df | -14.5762 | -52.47103 | 2025-10-03 04:34:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25009ffc-2ca5-3460-b985-08e9cba9300b | -18.16804 | -53.34768 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e127d06a-ba72-3725-8c8b-14f17c8bfa32 | -13.34286 | -47.79514 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README133.md)
