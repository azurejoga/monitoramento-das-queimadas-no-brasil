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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5a409f9-9165-36aa-bfa8-63b5610fa082 | -4.8176 | -45.8653 | 2024-10-31 04:15:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7faa9f90-f34f-3fac-99a1-e5ce4841769d | -4.8178 | -45.8429 | 2024-10-31 04:15:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 121.9 |
| f097e7e4-fdf8-30c1-962a-0e494be33a3d | -4.8364 | -45.8418 | 2024-10-31 04:15:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 76993710-3b7a-32af-b683-29024a92846b | -5.0464 | -45.1768 | 2024-10-31 04:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| fd37f31d-1a5a-3dc5-9722-df09d81e1e4e | -5.0466 | -45.1542 | 2024-10-31 04:15:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| a8d8e06a-6ebd-36fe-b0e5-bec7f20ecc12 | -6.1229 | -43.9578 | 2024-10-31 04:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 92270335-58a9-34cb-91ae-1cfd321c3721 | -6.1416 | -43.9563 | 2024-10-31 04:15:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| ab92856d-e549-318d-9497-d56031389e82 | -19.5083 | -56.5989 | 2024-10-31 04:16:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.5 |
| 8d309a71-a776-30cb-9e6d-e2ae8e02a2dd | 3.53699 | -51.27386 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bb4fe3c-b5fb-3769-8451-ab92259461c8 | 3.44506 | -51.24157 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0d84320-69f7-360d-9d8d-5d28e51da283 | 3.44445 | -51.24301 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb21c81a-4c90-3f9c-8aa0-47e77f11ffca | 3.43634 | -51.24801 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33a3e5ba-cb47-360d-9452-5ab171855301 | 3.435 | -51.24443 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ebe9f73-dcc1-30c0-9345-eafba8218682 | 3.43233 | -51.25374 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c572a0d-940b-3fbb-b475-138ad7c12430 | 3.43161 | -51.24873 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b696d3a2-f46c-3732-bdc5-fe5b726acc67 | 3.43104 | -51.25014 | 2024-10-31 04:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d2dfdfbd-e2f9-38c7-8661-9638de1733d3 | -4.64958 | -43.74395 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 336d1272-bf81-38b4-b06f-f8a253104e1c | -4.51222 | -43.7586 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 16bb3fef-ce83-35f8-a5bf-de6bd5dbfbf2 | -6.03789 | -35.28374 | 2024-10-31 04:23:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| ddc4c128-3be1-38dc-922b-fa3d581bf9d2 | -6.03728 | -35.28817 | 2024-10-31 04:23:00 | NPP-375D | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 91f758d3-58b2-3c1f-b3b6-9545b6a12c5e | -5.33112 | -35.65748 | 2024-10-31 04:23:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 073fdd1b-0f1e-302b-90cc-66c3755fd3b4 | -4.56819 | -38.48336 | 2024-10-31 04:23:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a264e3fa-7f38-3ca9-9593-35a5f493e5b3 | -5.16724 | -37.71102 | 2024-10-31 04:23:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 485b62fb-6d7d-34e8-a6c0-b0fa64a409ea | -5.69412 | -39.59158 | 2024-10-31 04:23:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d9650ea1-5e26-3b9e-ad65-cf7373ab5ced | -2.89243 | -40.6631 | 2024-10-31 04:23:00 | NPP-375D | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bd0a8078-a85e-3254-b188-2df95d24bfb7 | -3.94573 | -41.48494 | 2024-10-31 04:23:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 70e9b39d-f8df-3e40-9b5e-814d44eac72c | -3.9419 | -41.48436 | 2024-10-31 04:23:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf214e8d-937f-3286-b185-f59dfd54f29c | -4.83924 | -41.59509 | 2024-10-31 04:23:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 77fc463e-6b66-3450-a302-c9101b0ca318 | -4.53184 | -40.72948 | 2024-10-31 04:23:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9f5a499b-ed97-3a47-a41d-f4d399e6ad7e | -5.30266 | -40.50747 | 2024-10-31 04:23:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1bfd7f6c-f22f-3c91-9efe-9bc057046a2b | -3.4028 | -41.63668 | 2024-10-31 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 631b4023-affa-33d4-b122-3ce915eced39 | -3.4021 | -41.6412 | 2024-10-31 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| bd833345-43f5-39de-a3bf-28971a9df173 | -3.39903 | -41.6361 | 2024-10-31 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 2d00dca9-3d28-395b-ae48-2a4f2ce5a265 | -3.39834 | -41.64062 | 2024-10-31 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 3be197dd-01ad-39e6-bf47-3ef1d1333287 | -3.39527 | -41.6355 | 2024-10-31 04:23:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0a1fef34-af8d-30d5-ab2b-446309899e4d | -2.81177 | -42.30803 | 2024-10-31 04:23:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8893d952-8b52-3544-963b-6d087a9718f0 | -2.81029 | -42.3092 | 2024-10-31 04:23:00 | NPP-375D | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a7ea4f1-5d51-3bb8-9a9b-2f15f78c50c0 | -4.26447 | -42.18034 | 2024-10-31 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c8b8d183-c69f-3ddf-8574-fec78bed38e9 | -4.26078 | -42.1798 | 2024-10-31 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1a818d22-d0e2-3690-99e5-d607a90e4d35 | -4.25774 | -42.17489 | 2024-10-31 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca118792-9414-3f1a-ae26-b8742efbed5b | -4.25708 | -42.17924 | 2024-10-31 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 60b4d727-0994-329f-86d3-2fd3f009fa7f | -4.25338 | -42.17869 | 2024-10-31 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bb01320d-b62d-3f0b-a23c-95e2aa66629b | -4.24295 | -42.17269 | 2024-10-31 04:23:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 978be652-8b01-3124-bcfb-7413969419e6 | -4.00111 | -42.85038 | 2024-10-31 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cce6af4d-955d-3d02-9499-ee16a80b5110 | -4.8526 | -42.4752 | 2024-10-31 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7b079058-1078-31d7-8867-d461fdf4739c | -4.84958 | -42.47035 | 2024-10-31 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7aa40224-c0b5-35e9-a94c-0772801b1351 | -4.84894 | -42.47464 | 2024-10-31 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 836e4537-52cf-39fa-9209-229bc57dfc2f | -4.84528 | -42.47407 | 2024-10-31 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e9e174c-a6e8-3d3f-86fd-bd2a90f53b82 | -4.84464 | -42.47835 | 2024-10-31 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 847722c2-f979-39a9-a7d8-3cf649c1a5f5 | -4.84098 | -42.47777 | 2024-10-31 04:23:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| eca489aa-bc30-3fcc-8fc0-ccdd5d710857 | -4.65133 | -43.11841 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 00e01b8a-20e9-3673-b57e-283f958f7e2a | -4.64779 | -43.11786 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9c670af6-1005-300a-be6d-d9e8e4c5c4d6 | -4.64719 | -43.12183 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0187c752-e43a-3caa-9a56-ea4369877526 | -4.64425 | -43.11732 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67888aba-5888-3b92-9507-8ef9ca1550de | -4.50977 | -43.12741 | 2024-10-31 04:23:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cac2fee-1150-36f9-80ec-5394d0790b62 | -3.5744 | -43.23339 | 2024-10-31 04:23:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fe7cf2c-dda6-33ad-a617-d1ab5869db76 | -3.5513 | -43.47432 | 2024-10-31 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0062624f-e78f-3004-845c-7b91c0832c26 | -3.54785 | -43.4738 | 2024-10-31 04:23:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1738611a-1f98-3247-aed1-ca9bf12deb4c | -3.42249 | -43.16415 | 2024-10-31 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0ff7785-60fe-3ec1-9881-7149d4c8ca1a | -3.40842 | -43.18555 | 2024-10-31 04:23:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9aea16c2-810c-31db-858d-f8e521cae44b | -3.3659 | -44.23428 | 2024-10-31 04:23:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 350e4590-a88b-39df-84e3-65fd2f099f27 | -3.36253 | -44.23377 | 2024-10-31 04:23:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9958e24-a10a-33f8-9561-0a6adb0cf944 | -3.36198 | -44.23732 | 2024-10-31 04:23:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff23ec06-aaf1-360c-90a5-926b4dc3a15b | -5.0789 | -43.36137 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb1d473-0047-3220-9684-34aebf2284c0 | -4.2759 | -43.42947 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7ed49f00-f9e8-340e-8a58-ede3c4f054b8 | -4.27532 | -43.43329 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88ada901-dc0d-33af-aef6-3afa255a4e0f | -4.27243 | -43.42891 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdf6743a-3c61-3d98-875d-4e7b39adf0f4 | -4.27184 | -43.43274 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| db9261b6-fc63-371a-b260-f1088b961702 | -4.27126 | -43.43658 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49496c2d-8a11-393b-a38a-0aeb2edb0548 | -4.26895 | -43.42836 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 61b1eb14-379a-34dd-a95b-7de2857362e2 | -4.26836 | -43.43221 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eebfc0bd-9a39-3213-8361-0d64224f56aa | -4.26778 | -43.43605 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48441f9b-6dcd-3959-b565-fae8e840c744 | -4.26547 | -43.42784 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2008720e-aa4d-326d-9633-100b5526cd1c | -4.26488 | -43.43167 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5923dacf-029a-33ac-94d7-fb7bb778a4fe | -4.2643 | -43.43552 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34a9faa8-97e9-395a-8cc1-a1e801e61199 | -4.26371 | -43.43934 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0897828f-a265-3ecf-b352-8291c87da627 | -4.26082 | -43.43497 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 841ae2c2-8fb2-3262-bf5d-ba72c1d293c0 | -4.26024 | -43.43879 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2ce55ee-222e-3a53-b033-5d89d55d2bde | -4.25676 | -43.43823 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33d98a4f-002b-3d22-97da-09a935271c8e | -4.25618 | -43.44205 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf699854-c5cb-3895-a6f4-4f44c67c4e2f | -4.2556 | -43.44586 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71f44a85-3da2-3391-9916-ccc25f97b5be | -4.25559 | -43.43895 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab381b35-c13a-31d8-bf80-3f4bc8eabc27 | -4.25499 | -43.44276 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66066fa3-1bdc-32a4-b6b8-bafcabca9989 | -4.25439 | -43.44656 | 2024-10-31 04:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b49bfd4-67f6-3a27-9837-f31cced572d2 | -3.88001 | -43.19066 | 2024-10-31 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f74b917f-a3a0-3d42-ae96-92fbbd275ac9 | -4.30635 | -44.4949 | 2024-10-31 04:23:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7322d06-7635-3247-af07-bb465876ce58 | -4.30299 | -44.49438 | 2024-10-31 04:23:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd837798-514d-3a4a-95a6-c88f8c91c5f4 | -4.30243 | -44.49794 | 2024-10-31 04:23:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| caddb839-bd0d-3ac3-a74c-ea3746d57905 | -4.01282 | -44.52568 | 2024-10-31 04:23:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8879c3fd-aab1-3252-a265-28e65a506745 | -4.00947 | -44.52515 | 2024-10-31 04:23:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97f34e5e-a8db-3721-8839-e3ba9b5fb450 | -4.77329 | -43.64315 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ba76a0f-b7d7-3dd8-9ed8-eb9cbc078970 | -4.76982 | -43.64261 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b7c9c67-58e9-3966-b05c-a5bf29c5e6af | -4.74241 | -43.25209 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b87eb6e7-8707-3534-a95d-33bb7c2f6618 | -4.73889 | -43.25154 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad43c40a-f6da-3a20-840c-15c1f33eae56 | -4.73537 | -43.251 | 2024-10-31 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b650ae29-f29c-3a59-9b79-a033764288c2 | -4.88122 | -44.68473 | 2024-10-31 04:23:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c3ea81d-bb83-36ea-b44d-d1276af6b567 | -4.70436 | -44.47546 | 2024-10-31 04:23:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7498c8a9-90a5-3a86-9eca-7891ebf2cb69 | -4.70099 | -44.47492 | 2024-10-31 04:23:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d16ff7bf-b49d-39f9-b287-eebbbba62252 | -4.69465 | -44.38222 | 2024-10-31 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7f10edd-979e-3dc6-b905-46f6c2ca613c | -4.69409 | -44.38581 | 2024-10-31 04:23:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
