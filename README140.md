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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 569ecdb9-68ce-3a76-a234-c0f2d9ca7c55 | -17.02354 | -55.06653 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 393c3615-f102-317c-bb98-84a9eb73e234 | -17.02309 | -55.06875 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ab31cb57-de79-3b66-85bb-e00f021321ea | -17.02299 | -55.07217 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a04177d0-4c1f-3aa4-914e-0e96a3e8714d | -17.02258 | -55.07441 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 49eff9cd-3c3f-330e-9cd7-c53539f67a7d | -17.02243 | -55.07783 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2383a2eb-8ee4-3b09-adf3-96ef3f72fd83 | -17.02205 | -55.08008 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2e87a9a6-4b72-360a-bf01-afbfe63a60d3 | -17.01756 | -55.06021 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf8c0b65-345a-3714-acf0-8e2761570d41 | -17.01708 | -55.06239 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82ceb6b0-84c1-343b-bcdf-5c071c974668 | -17.01425 | -55.09409 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| e2cc887c-7e25-3e69-a066-dadcf147ed36 | -17.01107 | -55.05604 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6670e66-ed28-304d-a6ff-4045f114b4ce | -17.01104 | -55.05954 | 2024-10-07 05:44:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7633e94-4e3d-3801-8055-18e0391564d6 | -16.9022 | -54.53813 | 2024-10-07 05:44:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4120f360-d3ea-3603-b10f-9180e1e8e420 | -16.90159 | -54.54476 | 2024-10-07 05:44:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f101e53-d070-38e6-9a2a-e9e3f7973755 | -16.89888 | -54.53907 | 2024-10-07 05:44:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c6fa820-db33-38d7-b9e5-b10ae9362fe0 | -16.89822 | -54.54573 | 2024-10-07 05:44:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d300fac6-8ab7-3913-918e-017298ec0b8a | -18.89686 | -54.5406 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5a297d8f-0b22-3ec7-b103-08ed551b993c | -18.89638 | -54.54635 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17968d8e-fee9-3da3-b256-4b7e0d48897a | -18.89597 | -54.55122 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7724c7cb-8d82-3b17-99c3-fa442c18f158 | -18.89553 | -54.55647 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 521f354e-d4f4-3ae5-91a3-8dab06a284d4 | -18.89498 | -54.56313 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a8407b59-13c2-3aa0-ad03-ce61d6df0759 | -18.89453 | -54.48528 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0e9da2c1-e66b-398f-a7db-443fa3c4beda | -18.8942 | -54.48542 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6049e19-222c-3084-a575-476cd48288db | -18.89361 | -54.49195 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 282c5eff-80a5-3de6-99e3-35979155c9d4 | -18.88969 | -54.54363 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b53238f3-dc00-31eb-b714-030b62f6f97b | -18.88773 | -54.48369 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a45d37d2-0eb2-3d63-832c-0bc90df5d893 | -18.88747 | -54.57032 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3a36cee3-0092-39cd-ae37-83054024512f | -18.88662 | -54.57018 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| fdad8f92-2e49-3f52-bf06-21f914d9d249 | -18.88607 | -54.57632 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| af671926-e130-32db-a454-4df5d7fa8f6c | -18.88015 | -54.57541 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9c111ae4-5a98-33bf-9932-0bd2c3d8c3d8 | -18.87926 | -54.57532 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e253ba1d-4ef5-3645-814e-43d4677f5f94 | -18.87387 | -54.56794 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 44264447-4cbf-3732-9ab6-56ea6b5c6f6e | -18.87339 | -54.57377 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35dff61a-621c-3e8d-95a8-f4de57d82340 | -18.87303 | -54.5679 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4f014986-14b2-3431-a7ef-7213b9c09a20 | -18.87252 | -54.57363 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a49333f4-2a0c-32e8-8dfa-b436547f4083 | -18.86762 | -54.55996 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 577da23b-fcf9-37cc-9096-d693049a1bd5 | -18.8671 | -54.56634 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 59ab416d-21d0-3508-b4fe-3021d0b4656d | -18.86684 | -54.55979 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f134bc68-022a-3fce-8e3b-cbb19e3e8d29 | -18.86628 | -54.56619 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c0e8383c-ea2a-329d-9a57-97355aaa2378 | -18.86036 | -54.56441 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 26878426-0067-3422-a1c6-03739f17021e | -18.85953 | -54.56449 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1857952-bde1-377d-b279-8729d49951ea | -18.85895 | -54.57103 | 2024-10-07 05:44:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c99fa403-8ce7-3b3f-8f3b-a8951efbfbfc | -20.07383 | -54.53675 | 2024-10-07 05:44:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afc81457-976d-3b42-9246-e60b63817bbe | -20.06695 | -54.53532 | 2024-10-07 05:44:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 03f4ce1f-daff-3561-aedf-cd74bb4ff695 | -21.33746 | -54.65013 | 2024-10-07 05:44:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f1acb7f-61e1-337c-9a6f-c74d02594603 | -21.33696 | -54.6568 | 2024-10-07 05:44:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f02604f-2c8b-3947-8f8c-7aad76120b76 | -21.33628 | -54.64935 | 2024-10-07 05:44:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b2de240d-981e-302f-91bc-faf6b8a6c7ae | -21.33581 | -54.65603 | 2024-10-07 05:44:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4d9c4bf-72dd-31ab-be18-261f19899a4c | -21.33048 | -54.64966 | 2024-10-07 05:44:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b162bdb-c832-3730-ab39-c35bc40ca71f | -21.32997 | -54.65643 | 2024-10-07 05:44:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b23bcf1e-e45a-3926-a6da-a21fe52d0259 | -21.36493 | -55.69881 | 2024-10-07 05:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5596941f-ab5f-3709-8987-42f4edbb76c8 | -21.35932 | -55.69946 | 2024-10-07 05:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a38b95e0-43f7-364d-849c-0e2bdb40e333 | -21.32639 | -55.6974 | 2024-10-07 05:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 53b22cc9-1175-339b-bc7f-f99b4ff13526 | -21.32596 | -55.70282 | 2024-10-07 05:44:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4abb97f-4cc4-3313-bab4-4a5a7c386bd8 | -16.56584 | -55.9153 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 09cbccc8-951a-31b7-947a-08bc77adda52 | -16.56535 | -55.92019 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c95c91e0-61d5-3392-ade4-c51ee2f3c662 | -16.55967 | -55.91463 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 53f40974-1811-3e5a-8ac2-0b1e491505c7 | -16.5535 | -55.91393 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 327a563d-6074-3936-93d1-180d89bb14ca | -16.63876 | -55.56689 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d37b4fef-80b6-367a-a31a-4f705ee3fb81 | -16.63724 | -55.582 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6655b71d-4b64-3056-9929-6f80b398c663 | -16.63671 | -55.58715 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f96ef068-0ba5-3ac3-9b70-23a38ef9dc6c | -16.63242 | -55.56658 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b3f9527a-a6ff-3de6-8efa-03b4633e04e6 | -16.63192 | -55.57151 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 34246398-5a02-3b02-a9cc-24585c67ed11 | -16.63143 | -55.57638 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d6c2263f-24a7-35a7-a790-bac0cd1489ef | -16.62608 | -55.5662 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6adf96ae-443d-3373-845b-961dbfa13639 | -16.62557 | -55.57127 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 03620c47-59bd-3c62-93b5-95897cb7579e | -16.6251 | -55.57597 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b82337df-7a7c-3b8d-ae8c-3dcad525fcd7 | -16.62351 | -55.52805 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 77a0830d-b058-3606-97e0-c544d89e3cc4 | -16.61977 | -55.56552 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a3cac366-a692-3c0b-93c4-36f1e9a055a3 | -16.61925 | -55.57077 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 850bc250-3752-3e88-8cfe-ff0d04106538 | -16.61878 | -55.57545 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4e512244-0aba-392a-af21-453e56d5ec6c | -16.61831 | -55.58022 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 766a2bb6-e5e0-3d3c-b925-37b03e16720f | -16.6178 | -55.58524 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c8429e76-ef44-3836-964e-064766652e18 | -16.61719 | -55.52735 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| c2b8e35f-98b4-35b0-a334-5c11d1aa9142 | -16.61667 | -55.53258 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 121b0f1c-cf30-321c-a5a1-0dfa60acc7e5 | -16.61301 | -55.56945 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e4df9e95-b67b-3cea-9763-8834aa9d8a4d | -16.6125 | -55.57451 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c6f79447-4273-3f17-ba66-604fc7eadd00 | -16.61201 | -55.57952 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f085ad2b-e821-37a6-a903-d322515613e9 | -16.6115 | -55.58456 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 98147baf-538b-3c60-a26c-2d28a298a358 | -16.60572 | -55.57869 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b60844c9-c658-3ed0-aa4c-97fe67ce46f3 | -16.60521 | -55.58385 | 2024-10-07 05:44:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| df399357-a981-3c70-bb19-2dbe9bd26195 | -17.03433 | -56.67855 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 02707bc7-4b88-3952-be0f-af563481ad41 | -17.03387 | -56.683 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c7ea79fe-9ac0-3b5d-912b-0f7392e39fe3 | -17.02887 | -56.67347 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 768333c5-41cd-3263-858b-700a304ce3d2 | -17.02841 | -56.67792 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| d7867f14-58b3-30fa-9786-aee59ebc6cb7 | -17.02795 | -56.68237 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| d218653d-6e84-341f-804a-661970344840 | -17.02749 | -56.6868 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 39cc43f7-c997-3832-a83f-80d81fa1a422 | -17.02295 | -56.67281 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1aef2374-8928-3379-a4a1-b9af912544bf | -17.02249 | -56.67727 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 4cf0676e-e100-3574-ba11-d2d0ca80dfac | -17.02203 | -56.68171 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 60b7522f-4a97-3cd8-a72f-5b5d5f1e6407 | -17.02158 | -56.68614 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| e5e35565-a415-3163-a0b8-ec409b29577a | -17.02113 | -56.69057 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 20cd3a9c-38d4-342b-bc37-007c2ee561de | -17.01703 | -56.67215 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b00d9da9-2bb0-34de-b08e-829b10c172c8 | -17.01657 | -56.67662 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| f6a844a5-3f60-3b29-8dc2-97cfd564c5e6 | -17.01612 | -56.68106 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4c31399d-9f20-35bf-8795-09c2f96fe47e | -17.01567 | -56.68549 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 07091626-a8e8-34c3-bf6e-6701f5fcd96b | -17.01521 | -56.68992 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| ca3868de-32b5-3ad4-9a7d-2ab597a81e23 | -17.01065 | -56.67594 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 1a160eed-0ca9-3d72-843c-ab4515008f70 | -17.0102 | -56.6804 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| f6bf491e-46ee-3656-b82c-7dbece2299d7 | -17.00975 | -56.68482 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 076228cb-9b36-3160-b5b9-219e403cba73 | -17.0093 | -56.68927 | 2024-10-07 05:44:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |


[Clique aqui para ver as próximas entradas](README141.md)
