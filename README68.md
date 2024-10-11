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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a4662906-c1e9-302c-98aa-3fb7d119ac37 | -12.31182 | -45.30939 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 782e753a-9831-346e-928d-2ec3b7a62b78 | -12.31125 | -45.31324 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da4936b0-b0e4-32ee-bbae-382a1cb74a01 | -12.30952 | -45.30111 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f92a99c1-3c2d-38d1-b4bb-c741a36aca78 | -12.30894 | -45.30498 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edf9832e-cdd3-3b89-99e7-89f65961a498 | -12.30837 | -45.30884 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb388060-3cf1-31f7-93b0-f266a20f312a | -12.30492 | -45.33194 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01e1c87f-afa2-3801-9044-0f9baa477a9f | -12.30491 | -45.30829 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88921230-08e1-3b19-93ea-b3faf35e38a0 | -12.2934 | -45.33801 | 2024-10-11 04:25:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a55fb14-0785-3db4-8f5a-1079ec67dcc3 | -11.79008 | -45.19717 | 2024-10-11 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c1770e6-0316-3ce0-b1e4-537ef3f2dd3c | -11.13944 | -45.38156 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f3addbf-1dbb-3eb9-bf85-d9f08011812b | -11.10882 | -44.95107 | 2024-10-11 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41a91df6-d5d3-376d-bfd7-394f297456c9 | -11.0648 | -45.36617 | 2024-10-11 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 709428fa-2f8a-3d82-aa5d-e99655aaa6f9 | -12.95949 | -46.18985 | 2024-10-11 04:25:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1f2c20b-e7f3-357a-a45a-24d1a4da0802 | -12.69203 | -45.87539 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c069f68-efc3-3c02-9eb5-b2e15b562133 | -12.69146 | -45.87914 | 2024-10-11 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99e2a68d-2110-3f3a-b4b3-1aabff5b8689 | -14.84752 | -46.64262 | 2024-10-11 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 684a4c9e-efa1-31b7-8867-5375bba910fd | -14.84642 | -46.6499 | 2024-10-11 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7a0a12c1-aa50-3881-9e96-06d55008a9fc | -14.84304 | -46.64938 | 2024-10-11 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ff5fca-1773-3145-9591-4d71732b9223 | -14.84251 | -46.65295 | 2024-10-11 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07d1a634-788f-3a9d-ab27-9fe4c64f368e | -14.84196 | -46.65658 | 2024-10-11 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9ebe24a-1dd9-3515-a0f3-59b01c81cde9 | -14.83858 | -46.65604 | 2024-10-11 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dc9569c-f37c-3d0b-9ce4-c5683a59ff62 | -14.8702 | -46.9809 | 2024-10-11 04:25:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be4e2f17-8b64-3d76-a7dd-69a80616a6da | -7.81435 | -46.48741 | 2024-10-11 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35b65a11-20fc-3b2a-a4db-a89e9205b3b1 | -8.24287 | -47.02486 | 2024-10-11 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 98c2db59-ea3b-3927-9988-3930da5d5ed2 | -8.2108 | -46.88451 | 2024-10-11 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb309c59-751e-3cb0-adaf-afc8c3d6a899 | -8.21026 | -46.88798 | 2024-10-11 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a55a1659-1d3e-33de-9265-957ede119cf0 | -8.2075 | -46.88399 | 2024-10-11 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 338c4a34-d7a8-355b-a753-0e9ce7daa449 | -12.28394 | -46.78695 | 2024-10-11 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0ff9440-839e-3dcf-8b15-e4f3311e1d54 | -12.28062 | -46.78642 | 2024-10-11 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d6ec4674-0674-33d3-970b-a2aef033110c | -12.24681 | -47.1582 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35fb6e3f-69e8-3c56-84b3-87ee99c41940 | -12.24626 | -47.16172 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3225feb4-fe78-3183-8423-f1bf2595bf84 | -12.22918 | -47.18426 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a32afd60-1a83-3366-9635-2d51f9843843 | -12.21865 | -47.14285 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f91dcbc9-0d8f-3811-9752-fc3d9c7f46f6 | -12.21534 | -47.14231 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebda67dd-655f-3d43-9a04-3112907e438d | -12.19506 | -47.27257 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 354834e8-89cc-391f-9dc9-a5b04eea0358 | -12.17518 | -46.74437 | 2024-10-11 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29722171-3af3-3ee6-843e-e7661226f407 | -12.1724 | -46.74029 | 2024-10-11 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeee149e-10d8-35d6-9e56-ab48402f7817 | -12.17185 | -46.74385 | 2024-10-11 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ba3feff-1a08-3c7b-88db-f8533636731d | -12.16908 | -46.73976 | 2024-10-11 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| add77304-4bd8-3c14-9fde-415ee95dc6b1 | -12.16853 | -46.74332 | 2024-10-11 04:25:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2b92c46-894e-34a7-9d88-2852ef500e6f | -11.39284 | -47.19009 | 2024-10-11 04:25:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d631d8a5-aa0c-30d6-bdd9-69c4617ff4be | -13.51048 | -47.54621 | 2024-10-11 04:25:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56ca02ee-3709-360e-a7dc-83119d0fdce8 | -13.38287 | -46.90234 | 2024-10-11 04:25:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a898b51d-c973-3e02-8b72-5dc836c16003 | -13.01594 | -47.14703 | 2024-10-11 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24f0e3c8-c07b-37ff-a489-47e601da35da | -12.50211 | -47.28578 | 2024-10-11 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16576b04-b856-3af1-8212-79b61df84161 | -12.45456 | -47.30673 | 2024-10-11 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a8bea35-24b9-3a01-b122-ba7ce64ce406 | -12.45401 | -47.31026 | 2024-10-11 04:25:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80c06f6e-5df3-3047-85d0-bf4898a8555f | -12.30049 | -47.20679 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e442e40-ccf6-3ebb-82f1-028f63e5d1bc | -12.29994 | -47.21032 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9aae322-cd66-3e66-a485-fd08daecd1ef | -12.29939 | -47.21384 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d2a0f2a-153b-3331-86dc-025028621504 | -12.29718 | -47.20626 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfddad27-efd5-351a-a7cd-fa7c4d3a6441 | -12.29663 | -47.20978 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 284ccac0-319b-350f-a2fb-98b995436af6 | -13.38232 | -46.90592 | 2024-10-11 04:25:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8760cc90-d5e9-3428-a701-8c579589047d | -13.37954 | -46.90179 | 2024-10-11 04:25:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c654d0c4-e5ae-31fa-a23b-040ed1005c13 | -13.99216 | -48.02719 | 2024-10-11 04:25:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9892d332-554f-31c1-903a-509aa6a7ed35 | -14.72158 | -47.50896 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3e303da-41d3-3259-a5c3-8f4704d10dad | -7.68397 | -47.24997 | 2024-10-11 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0d2c8925-6c49-3b39-b508-aa052b0c1086 | -7.68341 | -47.25347 | 2024-10-11 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a92c22d-64dc-3264-a604-c33e6372619d | -9.16418 | -47.98364 | 2024-10-11 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1cfc119c-e830-3917-a10c-eff7e5802a76 | -9.09656 | -47.94028 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7ac88135-a174-3fdb-a83c-d847ff8746c3 | -9.08062 | -48.48158 | 2024-10-11 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 927cd163-6e78-3085-8ff5-9a14cdaf50ec | -9.07723 | -48.48102 | 2024-10-11 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9bc85cb-e157-3c89-8383-cc35ac6ec8d6 | -9.05564 | -47.85338 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af3add03-4ceb-36b3-b87d-95bc2ed95263 | -9.04466 | -47.8152 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6ec82da-3af4-35e2-8864-f486951faab5 | -9.04409 | -47.81874 | 2024-10-11 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 386eb88c-783d-3cb5-8b8f-d1f91d31d33a | -8.46549 | -48.27088 | 2024-10-11 04:25:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f929be9b-5e7f-3efc-a11c-1c6ad5f6041b | -8.46211 | -48.27032 | 2024-10-11 04:25:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3c6133d0-16e2-3c41-8747-123c65a6b274 | -8.40313 | -48.37705 | 2024-10-11 04:25:00 | NOAA-20 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d55db90-f105-3d5a-9d8e-1e38b5605264 | -9.89271 | -48.25148 | 2024-10-11 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef475fad-7c4f-39d1-93e2-28b7d2701fd1 | -9.87131 | -48.27765 | 2024-10-11 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3eb9eb0-0527-33e3-8357-ff5347ce394e | -9.86796 | -48.27711 | 2024-10-11 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3cd5d44-977b-3efe-9375-f5e566d36780 | -9.86139 | -48.25381 | 2024-10-11 04:25:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d93c41b-7c5f-3a7c-84c8-2b211cc6f88d | -9.82707 | -48.04707 | 2024-10-11 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50c665b7-ed04-37a6-be5c-241b99f29976 | -9.8265 | -48.05062 | 2024-10-11 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b8e0c14-c68a-393d-b893-9c17574518c3 | -10.67464 | -48.71282 | 2024-10-11 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3914f98-7b85-3bce-b14e-8f5b23cf34a5 | -10.67405 | -48.71652 | 2024-10-11 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48d02f0a-7874-3f22-848d-9349de1c204a | -10.63686 | -48.0176 | 2024-10-11 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec24f8e3-eb37-37ba-bc43-e724c57a5348 | -10.30949 | -48.88816 | 2024-10-11 04:25:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 313ba450-0347-3f7d-825f-541fd14d4b77 | -10.03249 | -48.54121 | 2024-10-11 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea98396f-dc4d-3fe5-ba92-2c275f292368 | -10.02913 | -48.54063 | 2024-10-11 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bca7735a-2384-3c23-aa2a-4853c21d3f23 | -10.00337 | -48.84925 | 2024-10-11 04:25:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3eaedd31-eb14-3ddf-8ee9-a5f48dcccf48 | -11.68026 | -48.4845 | 2024-10-11 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 572cab56-dd26-3168-bc88-128c754b5c04 | -11.67968 | -48.48808 | 2024-10-11 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d263e9fc-10b0-3365-95ee-619d212bc32e | -11.67911 | -48.49166 | 2024-10-11 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b2de59c-4414-3f22-88a5-f1e5f588e6d0 | -11.62956 | -47.90858 | 2024-10-11 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3ef613c-7903-374e-bc6d-61fa3696bdbd | -11.32512 | -47.77219 | 2024-10-11 04:25:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3be5154a-2db1-3ec8-a0a5-a06e2e702491 | -11.04537 | -47.90723 | 2024-10-11 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf15c698-e9ac-3828-b5b0-fb26dc9e3432 | -10.93937 | -47.93324 | 2024-10-11 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3de6c585-cd8d-33c2-9e25-92e7bc9b7b34 | -10.93881 | -47.93679 | 2024-10-11 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c0f7f94-b992-3640-8f99-d5259a460c94 | -10.93549 | -47.93623 | 2024-10-11 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07a0476c-cbc1-33f5-a2ce-d6ec71940c72 | -10.93161 | -47.93919 | 2024-10-11 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b014c4b3-62a0-3918-8685-28e92e715110 | -10.92774 | -47.94217 | 2024-10-11 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdde614f-cf30-3359-9ed1-db296245a152 | -10.82187 | -48.91051 | 2024-10-11 04:25:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64a7d3e0-b4f9-38d3-8c1f-5c6f3ff34f10 | -15.07961 | -48.94586 | 2024-10-11 04:25:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 923405f6-7b9f-38ee-83ba-1c2e18dec840 | -7.8431 | -49.44708 | 2024-10-11 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b2f6647-f6b7-387b-9be7-410ee36ba1d5 | -7.73236 | -49.03468 | 2024-10-11 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 870b051d-6e2e-33b6-8def-93f590c86caa | -7.7295 | -49.03017 | 2024-10-11 04:25:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb2480fa-92f5-3bbe-a595-7665500d156c | -7.68118 | -49.83928 | 2024-10-11 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1b0466d-d822-367b-9217-6d65920ae1c7 | -7.60028 | -49.40123 | 2024-10-11 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a39d1441-9776-3cc9-b968-314d4b411b60 | -7.35441 | -49.28867 | 2024-10-11 04:25:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README69.md)
