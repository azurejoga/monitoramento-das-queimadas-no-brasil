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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 671b8c96-5df7-3a69-913b-2557e5d53cec | -16.59126 | -57.15168 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 8864afe9-e7a5-32f3-a4af-55f653b1065f | -16.58978 | -57.16125 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 9d0d27d2-52c0-34a6-a0a4-fef964debea5 | -16.58236 | -57.20921 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| 17779353-b060-36b8-9c9d-892cb333b18c | -16.58129 | -55.94404 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.4 |
| 4a2d4715-a469-3791-a487-43a3d1cb4a3e | -16.58088 | -57.21882 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| 5df1b391-eeef-30a2-810f-75910805517f | -16.57332 | -57.20771 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.2 |
| aea65b10-197f-3612-a4a4-b5c7b9e9be03 | -16.57243 | -55.94263 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 92a65d81-4b54-3671-ba7f-ddcf9ec64d74 | -16.57183 | -57.21732 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 3d856806-75a4-34b9-967e-fee3728f9953 | -16.56427 | -57.20621 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| e8bb452e-5651-3c0c-995b-dea09327b549 | -16.56278 | -57.21582 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| cfcc9c25-5c92-3d1a-ad27-4923863461c7 | -16.56128 | -57.22543 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| b8bb1e7f-9ec6-3b9b-9783-eefc5465b0bb | -16.53112 | -57.24015 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.2 |
| ed23d170-94a4-36be-9d59-805cfb5c30fd | -16.52671 | -57.73835 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| aa658e9b-f02a-315a-887a-9625fa8f251a | -16.50998 | -57.2564 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 5df09f34-2abf-3970-aee4-625e88d7152e | -16.50846 | -57.26608 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 6277d6b4-aa8a-36d0-83cc-e93e14395434 | -16.46545 | -57.31174 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7aeebd27-bd5d-33b0-9da8-921202007273 | -16.46089 | -57.2812 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| cb1276bd-73c1-3156-aa9d-2199ae04c4ae | -16.45181 | -57.27969 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 759dd1f9-4c3d-3068-a312-354b5d481606 | -16.4503 | -57.28937 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 83ccbe73-c1b7-305a-8b32-2cba305ba473 | -16.44122 | -57.34753 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 19faee2c-019f-3a5e-b7a8-205df8b06a3f | -16.42303 | -57.3445 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d4b4edb0-e107-3014-88f5-3c8d97ed1d9c | -16.40934 | -57.37215 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 3808b275-abcf-33c8-a8cf-4d4dba3b2afd | -16.40177 | -57.3609 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 59de472e-2a50-35ae-90a1-62bb117df85e | -16.40023 | -57.37063 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 17.5 |
| 1dd1ccfa-1703-36a9-8a88-b8a7cf160fbe | -16.39869 | -57.38036 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| bb330fc5-203e-3793-89a5-b17cd8e9a735 | -14.56311 | -48.81839 | 2024-10-06 05:53:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5b31c4d9-abbe-3afa-9296-c74c8d796188 | -16.39113 | -57.36911 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 0d092564-4abf-3c8f-bb9e-721a23467b38 | -16.16905 | -55.92908 | 2024-10-06 05:53:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 6beec62c-d034-3d7b-9649-b9dd241287ed | -13.68414 | -51.18414 | 2024-10-06 05:53:00 | AQUA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| aacd71f1-58a7-34f1-b584-6b406e4ab63e | -13.40313 | -61.96275 | 2024-10-06 05:53:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 32.7 |
| e38bb778-de0b-3f78-8138-079f732620d2 | -12.89802 | -60.51548 | 2024-10-06 05:53:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6d368ae6-0893-3de4-8ae0-56122d139278 | -12.89394 | -60.52033 | 2024-10-06 05:53:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 37f23712-9775-3ae0-854d-1f698060733d | -12.88628 | -60.51354 | 2024-10-06 05:53:00 | AQUA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 93bf380b-2aaf-3282-ad8a-29a77d1bb14b | -12.79508 | -50.52356 | 2024-10-06 05:53:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| fb2a354d-dfc5-3dc5-a105-99fe49d8e5ad | -12.78229 | -50.53624 | 2024-10-06 05:53:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 2aeab8d6-7708-35ba-bdd2-ee993db39449 | -12.6704 | -54.70265 | 2024-10-06 05:53:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a892152-44f1-3936-bb94-74a42c027b91 | -12.6533 | -53.11467 | 2024-10-06 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c412248d-dd69-3336-a0e8-1f3295363580 | -12.64405 | -53.11332 | 2024-10-06 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 20f7e61f-02cc-3638-96e7-6176e840c75b | -12.64263 | -53.12323 | 2024-10-06 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 7e54846c-1cb4-3191-b098-d9a8de115efc | -12.62273 | -53.13042 | 2024-10-06 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 16ffb642-0206-3c8d-b121-825f07145aef | -12.61349 | -53.12906 | 2024-10-06 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a3a3e4ee-0fbb-3a91-9cbe-3ad7b0c110e3 | -12.57418 | -53.47043 | 2024-10-06 05:53:00 | AQUA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 13edbfd8-0592-36f1-8a53-50a9cba3e698 | -11.66382 | -54.52816 | 2024-10-06 05:53:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9416a605-dd70-334f-8602-2a6b1c7a1f13 | -11.58355 | -55.6672 | 2024-10-06 05:53:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 35214a8e-7dea-3be3-acb5-d36d0c540f45 | -11.57461 | -55.66581 | 2024-10-06 05:53:00 | AQUA_M-M | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 0f10827a-3c8a-34e9-ab3b-5f5b6457d235 | -17.84183 | -53.76788 | 2024-10-06 05:53:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e9b81d9d-c668-3ac0-b069-41faef2dc949 | -17.84037 | -53.77876 | 2024-10-06 05:53:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| bee89035-345a-3897-91fd-0b746729bbeb | -17.83892 | -53.78947 | 2024-10-06 05:53:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 84ce5f4f-1f83-3f31-9135-0e554863147f | -17.83084 | -53.77779 | 2024-10-06 05:53:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 9b163e8c-8cd9-3584-a064-e19a4bea1f1c | -17.82941 | -53.78844 | 2024-10-06 05:53:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 233d985f-2296-382f-abbd-ea2d8cdf5509 | -17.82469 | -53.78245 | 2024-10-06 05:53:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 46f527b6-6548-3a2b-8463-439cf985fe39 | -17.8233 | -53.79248 | 2024-10-06 05:53:00 | AQUA_M-M | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7144febf-99c3-3318-8553-bce048ac0340 | -17.18717 | -57.36285 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.1 |
| bceb4c90-003c-3c37-aa05-fb2aaf53e757 | -17.17965 | -57.41116 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 956dc3ca-8b75-393b-98ec-1542603fe327 | -17.17812 | -57.36134 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| b04c7d94-7d0c-3c46-b822-d2f5479f43fb | -17.17013 | -56.75165 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| e579cc09-a2a1-34e0-8473-05ad24cb9299 | -17.16907 | -57.35983 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 5ba9288a-8372-343c-9bf0-bdaa2ecff2b5 | -17.1687 | -56.76099 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 58352d51-49eb-35aa-b91e-85d58e2b21d0 | -17.16756 | -57.36947 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 822fc320-d1e5-3d8b-8cee-c2cbb4c0dcb3 | -17.16121 | -56.75019 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.1 |
| e0015763-4fea-3d07-a0ff-de6428d3d286 | -17.15977 | -56.75953 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.0 |
| 4617a65a-d071-374e-bb14-4249332b4c50 | -16.34078 | -51.27592 | 2024-10-06 05:53:00 | AQUA_M-M | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 718309bd-a41a-39b2-b4b3-8ce87d821b2a | -17.15849 | -57.42749 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 2eb21f7d-7719-3fd8-9dcf-e3334bea33a7 | -17.14942 | -57.42597 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 18.2 |
| 9c4eeb08-4d6f-314f-aacb-373ad70c93f5 | -17.14035 | -57.42445 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c84f91eb-3c7b-35c8-a951-6aa5bfb2ff6f | -17.13762 | -56.78466 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.7 |
| bcbd64ac-564c-3b34-8f75-b07c32c7cc31 | -17.13474 | -56.80337 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| 2948d667-9b14-3d75-9426-2b4073bcfb04 | -17.13445 | -56.74582 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d9415b41-29f1-3d16-a0c7-298534b1f13d | -17.13433 | -57.40358 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.7 |
| 2a823239-3fe4-3219-8e64-a7eeb69c8465 | -17.13329 | -56.81273 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| faeadd95-ca03-320d-8955-ba7471b6b67d | -17.13301 | -56.75516 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 5689f4e8-be4a-3e27-bbb2-d8e648da99a9 | -17.1328 | -57.41326 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 1755dee3-8fa8-3bec-9f84-6b48496e97e5 | -17.13157 | -56.7645 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.2 |
| 18b956c4-8594-334a-be1b-e38f08ad5ea8 | -17.12581 | -56.80191 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| c6456d73-1e47-33cb-90b7-72312af165b2 | -17.12526 | -57.40206 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 29.8 |
| 8e2e26d1-dac7-3dd0-9061-cfcadb9eb040 | -17.12436 | -56.81127 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 74c2a3d8-1a04-3bf6-81ac-145f023709c8 | -17.12373 | -57.41174 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 30.8 |
| c5868850-ea01-3ea4-a1e5-7cd3ed5b947c | -17.12221 | -57.42142 | 2024-10-06 05:53:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| eecd48b0-02d9-3adc-bcc6-68771287a3e0 | -17.11688 | -56.80045 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 23169170-84a8-3843-96fa-4880d38184c0 | -17.10803 | -56.6774 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 8c48923a-1288-3cc1-9435-b1ab5a2a6c41 | -17.10733 | -56.80177 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.2 |
| 34268a08-769c-32d8-a370-f80a65079e93 | -17.10661 | -56.68672 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 0ad2659b-75b3-319b-8f3c-21535a99008f | -17.10589 | -56.81114 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 70ca8288-8f76-3380-bacb-758b67cd23b1 | -17.0984 | -56.80031 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| b8ab9334-b3f9-3252-8a0b-6336bb31dbc5 | -17.09696 | -56.80968 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 22.1 |
| 2fa822f5-0027-3937-b06d-d0a19a6f357b | -17.08803 | -56.80821 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 1d4173cd-d9aa-3c8f-a7c0-855370a991e5 | -17.0791 | -56.80675 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| c9e89d23-71ee-3ca3-a6eb-29364a4b990c | -17.07017 | -56.80529 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.6 |
| 470b60bc-8a1e-3cb4-b190-4a155ce12e36 | -17.06124 | -56.80383 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 854a6f20-e3a2-3392-8fe2-6c8cbb690752 | -16.09919 | -50.45801 | 2024-10-06 05:53:00 | AQUA_M-M | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cac1b1b0-1b11-3d8a-b946-e627923866e8 | -17.0598 | -56.81319 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| cc4f70d6-133b-3d7d-b9f1-341b240738fa | -17.05489 | -56.7261 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| faf00a0d-8320-394f-ac40-2163f2e97f09 | -17.05171 | -56.68733 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 2cfef808-a6a9-35d8-9ac5-b3a1a971dcc3 | -17.05087 | -56.81173 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 2ee9b58b-e499-37d8-9977-cd4768e80be6 | -17.04942 | -56.8211 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| cd18f321-80d4-36ff-8a25-2a7c6a88ecaf | -17.04597 | -56.72464 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 7fc02166-b639-3101-a3ad-79161017866f | -17.04453 | -56.73398 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 78110b8a-956c-34b7-b621-fef29f581473 | -17.04279 | -56.68588 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| d84f2366-a3a2-31d6-b9b2-285f93c9e247 | -17.04049 | -56.81964 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 9c12093d-1553-3d1b-aa14-c86e016f125f | -17.03992 | -56.70452 | 2024-10-06 05:53:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |


[Clique aqui para ver as próximas entradas](README150.md)
