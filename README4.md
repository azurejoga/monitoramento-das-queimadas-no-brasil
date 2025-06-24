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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1823bc58-4eb2-3ba7-a4ff-e3d103fcc67f | -7.2025 | -43.1171 | 2025-06-24 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 8fab8c95-c4d6-3da7-b0aa-894eef0b7b1b | -7.2028 | -43.0936 | 2025-06-24 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| 0dafd257-8fc9-325d-9a82-1f1c7b1c2847 | -8.5907 | -51.5955 | 2025-06-24 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 79fec2ef-f220-3352-8517-421b78d2c2a1 | -4.543 | -47.9934 | 2025-06-24 02:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 9821651e-362b-3694-8d17-c74b83e6df55 | -8.5722 | -51.5761 | 2025-06-24 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 20bc716f-8309-322c-95fb-5ffc30a297ff | -4.5429 | -48.0151 | 2025-06-24 02:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 092d44a5-ddf1-3bb7-b225-7b43f00a132a | -8.0703 | -43.0981 | 2025-06-24 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.9 |
| d51e91e5-5695-38e6-a6c1-5ad3fe4ce12d | -10.0784 | -52.7393 | 2025-06-24 02:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| d5ed52b7-b668-369f-b123-e8e904a75adb | -7.2028 | -43.0936 | 2025-06-24 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 03d4c19b-786b-349d-973b-68c93ed9de93 | -5.7887 | -43.6134 | 2025-06-24 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 8bedade2-e67b-3243-a87a-5337c51f9bbf | -8.5909 | -51.5746 | 2025-06-24 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| bef95092-3a10-3a12-8316-d2bc6b518969 | -8.07 | -43.1216 | 2025-06-24 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 1150775a-f87c-3a85-91ef-44cb53c0eb3e | -8.5907 | -51.5955 | 2025-06-24 02:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a7a58cd6-a885-3c6e-9abb-e6c567d46550 | -8.5722 | -51.5761 | 2025-06-24 02:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 78c2e6de-2f2f-34f7-94f9-f43120132a48 | -7.2028 | -43.0936 | 2025-06-24 02:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| 37b4c26b-79a6-3302-9025-451042186eef | -8.5909 | -51.5746 | 2025-06-24 02:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 188dc1eb-1261-3bcc-a8a2-63dd1f1d044b | -8.0703 | -43.0981 | 2025-06-24 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| ae06f0af-ff99-32c0-9593-935465fa3d49 | -8.07 | -43.1216 | 2025-06-24 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 7c98af23-7b45-306c-b27e-f9372f358111 | -4.5429 | -48.0151 | 2025-06-24 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| affc764a-570b-3e02-8fd0-1988061cb019 | -4.5429 | -48.0151 | 2025-06-24 02:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 664311cf-09ac-3eaf-9d2d-732bce8cb77c | -7.2028 | -43.0936 | 2025-06-24 02:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.5 |
| 2d0e066b-2030-302f-a676-258c62ae20fb | -10.0784 | -52.7393 | 2025-06-24 02:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 7f24c444-3e11-3f2b-a347-2b05f0e160e0 | -8.0703 | -43.0981 | 2025-06-24 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.9 |
| 70dada75-8fba-3a77-9490-1ebaf75ad097 | -8.5909 | -51.5746 | 2025-06-24 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| ca372552-9141-35f3-a82f-6684c2a6c2d0 | -8.07 | -43.1216 | 2025-06-24 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 47069a71-f565-3751-8bcb-bdc34fee2643 | -8.5722 | -51.5761 | 2025-06-24 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 3cb546c7-a127-304c-95a6-2d2a6f6c3232 | -8.5724 | -51.5552 | 2025-06-24 02:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| ac7ce0b0-146e-3ed2-bc64-ee202f3510e3 | -4.5429 | -48.0151 | 2025-06-24 02:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 80d19373-c499-37e6-9967-568d4210a2f8 | -8.5724 | -51.5552 | 2025-06-24 02:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 72a38aca-1140-3018-bab8-c78e7fa1b00b | -8.0703 | -43.0981 | 2025-06-24 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 7c2700b6-2fdd-38cb-bfae-ea2fbc6bfe77 | -10.0784 | -52.7393 | 2025-06-24 02:50:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 72ba7022-eadb-3ce3-b6eb-bee36c74a968 | -7.2028 | -43.0936 | 2025-06-24 02:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 58.7 |
| bd870554-db24-3bb2-8ee7-d204abe95fcd | -8.5909 | -51.5746 | 2025-06-24 02:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 1176910d-b7f9-3627-9543-e6216903a7dd | -8.5722 | -51.5761 | 2025-06-24 02:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| b629c6d1-1a91-302a-a523-746482ec56e4 | -10.0784 | -52.7393 | 2025-06-24 03:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 0dd25ad2-1641-358b-934a-9b0e46aefea6 | -7.2028 | -43.0936 | 2025-06-24 03:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.5 |
| 486579c0-e7be-3e49-a92b-470eccbf9d6c | -4.5429 | -48.0151 | 2025-06-24 03:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 07467213-c3a4-38b0-903e-45dbe6402c87 | -8.5909 | -51.5746 | 2025-06-24 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 69f2db16-ba11-35cb-a238-4640bb919ffd | -8.5722 | -51.5761 | 2025-06-24 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 27aa2763-4175-3ec5-af0f-bd653666eb83 | -8.0703 | -43.0981 | 2025-06-24 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 91328eeb-66d4-3bc1-bf21-5626ba013777 | -8.07 | -43.1216 | 2025-06-24 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 46012af6-5a25-36d1-a4e1-4a29cdb0ab97 | -8.5724 | -51.5552 | 2025-06-24 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 380643d6-9267-3169-b1a0-d22b683764a0 | -4.5429 | -48.0151 | 2025-06-24 03:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 058054b9-2358-3544-b17a-8397e40d6b7f | -10.0784 | -52.7393 | 2025-06-24 03:10:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 77ec5666-99b9-3937-95fe-a9c976d3fa31 | -8.5722 | -51.5761 | 2025-06-24 03:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| c0fddde1-7f2c-3828-9985-6846b14ba645 | -7.2028 | -43.0936 | 2025-06-24 03:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 44.3 |
| 83510b75-77c4-3c1a-862a-98a6cf33b1a9 | -4.5429 | -48.0151 | 2025-06-24 03:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| d4735709-5239-3afe-beee-2bd5279439c5 | -8.5722 | -51.5761 | 2025-06-24 03:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1a4f27e7-9c21-303f-a701-4678e01334f2 | -10.0784 | -52.7393 | 2025-06-24 03:20:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5356c794-63ef-35d8-ade6-1925cd11c1b6 | -7.2028 | -43.0936 | 2025-06-24 03:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 39.2 |
| 4174e149-4971-3c59-9d40-5cddafa7e926 | -4.5429 | -48.0151 | 2025-06-24 03:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d2198370-1fbb-3efd-bb6a-bd4691ae1848 | -10.0784 | -52.7393 | 2025-06-24 03:30:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| ea9d502d-bc79-3d4c-90ee-40a1d1896b0d | -5.4886 | -42.14693 | 2025-06-24 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e2003aa1-706c-3543-8514-21fe11e656c8 | -7.44706 | -45.57651 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d9b2087-1ebc-3996-afb8-06ce61150d11 | -5.78223 | -43.61383 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03d59e37-72b0-3c69-b6c6-56a1f0425b8b | -5.78636 | -43.60989 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 509b6dee-c20e-3cba-a54d-75bb12ea9404 | -5.76392 | -38.90348 | 2025-06-24 03:36:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20e04fe7-f94f-3bae-bf83-9c7dd3246727 | -8.24302 | -44.95192 | 2025-06-24 03:36:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 55a160fc-cf5a-308b-8f69-ea836459768c | -8.06966 | -43.11473 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 3ddb1b51-6cfb-362b-824c-6d9fc5c463ed | -5.7857 | -43.6136 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6eb60111-5abf-3e03-b54a-b9dad9c87f2e | -5.49373 | -42.14786 | 2025-06-24 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bff1ba10-0eb2-391d-acc6-5fc42b9cf30c | -7.20039 | -43.10671 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a4bef7e7-48ed-39cc-88fe-f389f06abab1 | -7.47621 | -45.59192 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e3d66ebf-f7fa-3265-9179-50aea54d0936 | -4.83953 | -37.43757 | 2025-06-24 03:36:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| aed2ba6b-1e4f-3fd5-b5fd-546fc049606a | -7.86766 | -47.8828 | 2025-06-24 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c18b2927-e9a4-32b4-b311-253bc56e7d39 | -7.4721 | -45.58807 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 527c6a1b-cd11-3f48-ac0f-773151a38129 | -6.95696 | -42.8027 | 2025-06-24 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3cb346d4-5ac8-3b0a-9de6-94464e196980 | -7.20752 | -43.0975 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 75f45c29-b2da-3b3d-a5dc-66cacd5fca31 | -6.07853 | -37.94269 | 2025-06-24 03:36:00 | NOAA-21 | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d9ba9580-7f9c-3df2-a140-3a1be1173432 | -8.06442 | -43.11379 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a63386c0-5682-39c7-8542-bf538b4cf575 | -7.09227 | -44.37185 | 2025-06-24 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 106980a4-1055-3b13-a8e8-9194e0d9575b | -7.86898 | -47.87594 | 2025-06-24 03:36:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccd3f0e5-b19a-35d4-ad8a-b704bcaee204 | -7.09156 | -44.37576 | 2025-06-24 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 980f0e84-8990-3866-9a3b-9e5bd5e71116 | -9.40319 | -40.31485 | 2025-06-24 03:36:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| deabf100-4f7d-3c0b-8302-e38d2ae0e409 | -5.07024 | -43.72654 | 2025-06-24 03:36:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8cdf300-b4de-3391-aab0-c780c71125e7 | -8.05918 | -43.11287 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 9cf85c18-5954-367b-b093-fdd25cec5492 | -4.7957 | -37.79373 | 2025-06-24 03:36:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c12f8e7b-a4af-39c5-9869-d18c84cdbc58 | -9.40743 | -40.31557 | 2025-06-24 03:36:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2a955de2-2bba-35dd-a81f-72d282980ca8 | -7.20159 | -43.09998 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 30887309-47db-39b7-8e97-b9675c07898f | -6.55055 | -36.89941 | 2025-06-24 03:36:00 | NOAA-21 | JARDIM DO SERIDÓ | RIO GRANDE DO NORTE | Brasil | 2405702 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 496541cc-91c1-3114-b460-14e3984cbb37 | -5.48624 | -42.14718 | 2025-06-24 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6a412084-d885-3318-98b6-caa868149e8a | -5.48676 | -42.1441 | 2025-06-24 03:36:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5e40685a-a7b8-3c8b-bde2-9ff2975fb1a4 | -8.065 | -43.11056 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 63987949-4a33-38db-9abc-3063712ee103 | -6.9506 | -42.80816 | 2025-06-24 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 68121061-5715-3075-8720-fdbd66ae6412 | -7.00661 | -44.61005 | 2025-06-24 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1eed5885-cbf9-38cb-83b4-0267cc87b236 | -7.20571 | -43.1076 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d91a20ba-9ad3-37b0-89d6-6c4dbb944fe0 | -5.92341 | -43.47852 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e77d3019-7fbd-3c40-9539-2ed409f270ad | -7.44611 | -45.58149 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0630824-634c-328a-8946-e6192bf3bdd5 | -6.07671 | -37.94498 | 2025-06-24 03:36:00 | NOAA-21 | MARTINS | RIO GRANDE DO NORTE | Brasil | 2407401 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 48519224-795d-36d4-8a77-97110c292445 | -5.91854 | -43.47367 | 2025-06-24 03:36:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 633ca8d5-2da6-3d8d-84f8-10a12426f849 | -7.21164 | -43.10513 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ac8fed72-4009-33bd-86b4-41536470e222 | -7.45518 | -45.56748 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8e03bb8-ed0c-3eef-a366-0c38b93279ef | -7.44821 | -45.57851 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feffd231-4e2a-3888-b14a-10fd194f4e33 | -7.48337 | -45.58796 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0843c84-ef4b-3898-8cb6-efe030c0a7c8 | -7.44894 | -45.56661 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b990300c-417b-36c6-a895-92d43bfdb8c1 | -7.47714 | -45.58698 | 2025-06-24 03:36:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43b9c1a5-15e7-3bd4-97d6-f568e5dc0946 | -8.05859 | -43.1161 | 2025-06-24 03:36:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 67953ffc-b380-3ec6-b2d1-0dfe7f6b7876 | -7.05896 | -43.92682 | 2025-06-24 03:36:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9a6c25cf-c7cc-3ad2-8de2-5e59ba103b3e | -6.95639 | -42.8059 | 2025-06-24 03:36:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2243aa65-104e-3fae-83bd-250ba5bd1432 | -7.21224 | -43.10176 | 2025-06-24 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README5.md)
