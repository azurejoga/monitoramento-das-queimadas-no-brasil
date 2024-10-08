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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eb9b701-7e07-3ba3-b589-1ccd2afdfe7b | -16.5897 | -46.4979 | 2024-10-08 02:26:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 7805755c-3ec7-3c76-972d-53bae2fb9813 | -16.5462 | -57.7344 | 2024-10-08 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 9efbf616-297b-3834-a2b8-46225064604e | -16.5466 | -57.714 | 2024-10-08 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 55cad7fe-4f7b-34b6-b0be-9df05a31b8d1 | -16.5752 | -55.9055 | 2024-10-08 02:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 19ee8282-cf26-3a0e-a553-d152119684d3 | -16.5267 | -57.7365 | 2024-10-08 02:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.8 |
| a47ac249-b4f4-3342-ae85-635e2b4a054c | -16.5556 | -55.9079 | 2024-10-08 02:26:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 36.7 |
| 03df9291-a1f2-3395-b41c-a85534b3f3a2 | -16.6534 | -57.11 | 2024-10-08 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| 6973720b-a56f-3c6f-8e18-6d2a9871f98a | -16.5658 | -57.7322 | 2024-10-08 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 6adf747b-ed3a-3f5e-948b-f759bfe8c473 | -16.5661 | -57.7118 | 2024-10-08 02:26:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 45.6 |
| 65f90bdc-664a-33c2-bed8-7fcbc7ab93da | -16.5948 | -55.9031 | 2024-10-08 02:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| e429ae32-79bd-3b6f-833c-0a1f0db7b211 | -16.6143 | -55.9007 | 2024-10-08 02:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 34.7 |
| 1c9caed6-042e-3757-bc53-db849ad8e84a | -16.6531 | -57.1305 | 2024-10-08 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 144.0 |
| 329d8d06-2e9e-39bb-8d2e-93d15810597d | -16.673 | -57.1077 | 2024-10-08 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 157ca4c5-42df-311a-90dc-cf0291c1a18c | -16.6726 | -57.1283 | 2024-10-08 02:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| ba5e707a-902a-3cd9-9239-1b438aa33521 | -16.9211 | -57.4881 | 2024-10-08 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.7 |
| d632c310-bf30-338c-b9cc-f7d8e7f7387c | -16.8048 | -57.4197 | 2024-10-08 02:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 45d52844-b3f4-34ee-9548-57cb9e99a877 | -17.0992 | -57.3651 | 2024-10-08 02:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.0 |
| ec0cba68-af93-3e25-9b92-0d8fa685213b | -16.9407 | -57.4859 | 2024-10-08 02:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.1 |
| bf89aa98-1bfc-37f1-9d30-e4c7d1343e95 | -17.1584 | -56.1429 | 2024-10-08 02:26:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 29.7 |
| 3db05b4f-4fc7-329e-9e45-20b1c601bd25 | -19.2723 | -46.1305 | 2024-10-08 02:26:53 | GOES-16 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 11a2bf65-327f-3bab-9cb6-1bcb1c32f1aa | -19.2926 | -46.1257 | 2024-10-08 02:26:53 | GOES-16 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| d8a077f7-c9ef-31eb-b3eb-0bd361bff23f | -20.3732 | -43.9468 | 2024-10-08 02:26:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.3 |
| d6779e61-0a5a-3d62-8dea-31481e812e06 | -20.374 | -43.922 | 2024-10-08 02:26:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 64b84499-bffc-3864-ab52-3663a8d489b2 | -20.3938 | -43.9412 | 2024-10-08 02:26:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 189.1 |
| 2a0380b7-c637-348b-8302-9499052adb9c | -20.3946 | -43.9163 | 2024-10-08 02:26:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| e966ee20-29de-32d6-87ad-4e0155aedb33 | -20.4144 | -43.9356 | 2024-10-08 02:26:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.4 |
| 4238427b-f75c-3c52-93d6-d2d3858b5276 | -20.4251 | -47.6688 | 2024-10-08 02:26:59 | GOES-16 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 92.0 |
| c21a544b-a799-331e-8c08-89bf56b9ee3f | -20.4258 | -47.6453 | 2024-10-08 02:26:59 | GOES-16 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 69a78e3d-ae08-376d-8a22-c91ac73d5065 | -20.6602 | -45.9105 | 2024-10-08 02:27:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 143.2 |
| d5941756-86a2-3622-893b-21c112373762 | -5.5718 | -44.87 | 2024-10-08 02:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 46946f10-a397-312a-bc57-0ada377e9d9b | -5.5716 | -44.8927 | 2024-10-08 02:35:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| babfa3e7-61fa-3ad9-b6b7-5111ca955a85 | -9.445 | -66.7289 | 2024-10-08 02:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 1dd25ee6-91a3-3146-bbe8-60dfc47ad08e | -9.4087 | -66.5438 | 2024-10-08 02:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 00cfe620-ee44-3dac-a90b-b47aa63e8230 | -9.3901 | -66.5444 | 2024-10-08 02:36:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| adc86442-facb-3b43-850c-5cc9896be503 | -9.5537 | -63.5764 | 2024-10-08 02:36:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 55db47c4-3a55-3929-8de2-45ee6dda378d | -10.6256 | -55.9154 | 2024-10-08 02:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 4b26b161-cc7e-30c6-b9f2-56574473922b | -10.8755 | -63.8979 | 2024-10-08 02:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 6a7981b4-2383-350f-b9c2-9e3b499c4622 | -10.8754 | -63.9169 | 2024-10-08 02:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| c91d16de-c64d-32f1-84ef-9e10c4a2c4f7 | -10.8941 | -63.916 | 2024-10-08 02:36:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.2 |
| aef49aa4-db22-38ab-baaf-32afa76dabd4 | -11.5233 | -65.137 | 2024-10-08 02:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 3df95148-108b-381a-9fde-d3c3226a7c60 | -12.591 | -53.0524 | 2024-10-08 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1c773f22-3994-37ff-990a-00e7132d6fa1 | -12.5907 | -53.0732 | 2024-10-08 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 450e7c8a-ac36-3c74-97ac-3ec8d8a475e2 | -12.572 | -53.0544 | 2024-10-08 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| e2a4029a-76c6-30aa-a84e-19d25bccd66f | -12.5717 | -53.0753 | 2024-10-08 02:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 8cda9cf3-de1b-3aa5-999d-91bd7c39be51 | -15.063 | -45.4681 | 2024-10-08 02:36:30 | GOES-16 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| d49e4204-bd73-384c-ab6f-58ea0ae452c6 | -15.0434 | -45.4718 | 2024-10-08 02:36:30 | GOES-16 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 114.4 |
| ce91249b-4190-3c31-840b-c9777b61c5d7 | -15.0429 | -45.4951 | 2024-10-08 02:36:30 | GOES-16 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 5c3beecc-e113-3d94-a8d9-d5d7054529ce | -15.7068 | -59.4326 | 2024-10-08 02:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 7849c934-3954-397a-a8aa-21a9352ffca8 | -15.7066 | -59.4526 | 2024-10-08 02:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 52882cc9-dd00-39ed-a87c-9aee2b6c3476 | -15.6874 | -59.4344 | 2024-10-08 02:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| d0fa5686-4ed4-3f5d-9c05-4d50eec67ca6 | -15.6872 | -59.4544 | 2024-10-08 02:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 191b723f-d8a6-3e57-9104-e101ea53ff02 | -15.9082 | -57.4789 | 2024-10-08 02:36:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 8e8ed320-45c0-3391-ba82-2358b9c1456d | -16.5902 | -46.4746 | 2024-10-08 02:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a5f3d297-af96-302c-be88-606ad69a1b24 | -16.5897 | -46.4979 | 2024-10-08 02:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e28d8c0e-1414-3b28-84cc-3f005ab25c95 | -16.5752 | -55.9055 | 2024-10-08 02:36:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 32.6 |
| f65281fc-a1c0-333c-83e3-f7ef952f7776 | -16.5948 | -55.9031 | 2024-10-08 02:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 32.9 |
| 0987582c-9439-3dd7-a1c4-ee14c1db81aa | -16.8048 | -57.4197 | 2024-10-08 02:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.9 |
| bf6c42a9-e99e-3126-88fc-29630e5cc194 | -17.1178 | -57.4244 | 2024-10-08 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.0 |
| 483c8e71-d0bc-3841-a30a-0b90689fc5e7 | -17.0992 | -57.3651 | 2024-10-08 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| ed5b1d68-557d-3fe6-9ce1-a5f8e977d272 | -17.0123 | -56.6773 | 2024-10-08 02:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 34.8 |
| 070bc7b1-6e43-3d3a-8dee-47152ea76bc1 | -16.9407 | -57.4859 | 2024-10-08 02:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.0 |
| 1fe56b55-81cd-3328-af97-0075313ebc17 | -18.6192 | -57.2603 | 2024-10-08 02:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 541967f6-0070-36dd-b4f9-33645a3011e4 | -20.4152 | -43.9107 | 2024-10-08 02:36:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 98.1 |
| d75ff981-c178-36d5-8362-bb71753e0875 | -20.4144 | -43.9356 | 2024-10-08 02:36:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 237.7 |
| e822e980-0b30-3fc5-a3a3-3c7a91641989 | -20.3946 | -43.9163 | 2024-10-08 02:36:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 164.0 |
| 333b35d0-f2a9-301d-9642-74f808ee5610 | -20.3938 | -43.9412 | 2024-10-08 02:36:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 449.9 |
| 6406c8ea-01fe-34dc-a3d9-83803f85f014 | -20.393 | -43.966 | 2024-10-08 02:36:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| 86fac4d6-b665-3e7c-89c5-4867523e7fb2 | -20.3732 | -43.9468 | 2024-10-08 02:36:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| c674055d-dbc3-3a85-95d8-cfe0b16d1af6 | -11.6756 | -63.996498 | 2024-10-08 02:41:10 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 488cd18c-3a63-3ec2-a9f0-fe55646856d6 | -9.393 | -66.529999 | 2024-10-08 02:41:58 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8eebb145-8c30-3092-8c0b-fb4204134ba1 | -9.4026 | -66.527397 | 2024-10-08 02:41:58 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| effe1957-e57b-3e8a-a620-5cab3453068d | -5.5716 | -44.8927 | 2024-10-08 02:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e9db8c7a-946e-3215-8b8a-6348ebb2ad34 | -5.5718 | -44.87 | 2024-10-08 02:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 86cc076a-6ebb-342f-9191-7b73f14743d3 | -9.4087 | -66.5438 | 2024-10-08 02:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 9bc84d51-35a5-3036-9fa8-23cdb63b43a0 | -9.445 | -66.7289 | 2024-10-08 02:46:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1d38ed72-9ee4-301a-842e-a47616854b84 | -9.5537 | -63.5764 | 2024-10-08 02:46:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 8c48c72d-ab5c-3d84-a381-035fb670bb98 | -10.6256 | -55.9154 | 2024-10-08 02:46:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f83ab439-0c07-3bde-ad57-1b541fae5894 | -10.8754 | -63.9169 | 2024-10-08 02:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.2 |
| a5b6a05e-b9ee-327f-ba07-462eaf2ac05f | -10.8755 | -63.8979 | 2024-10-08 02:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 8f9b5a6e-7243-3ef0-a93e-6560788447cd | -11.3081 | -51.0676 | 2024-10-08 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| b3ee07aa-fd82-3258-a229-4e7edf1f9579 | -11.3268 | -51.0868 | 2024-10-08 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 9a305193-632b-3ade-9082-f67265e567e2 | -11.3271 | -51.0656 | 2024-10-08 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 247.5 |
| 1eb7b81c-5ff1-3b96-ba46-0540a2ef1d25 | -11.3458 | -51.0848 | 2024-10-08 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 328.1 |
| cd7082de-d183-3be4-a59d-1b7e2254b14a | -11.3461 | -51.0635 | 2024-10-08 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 437.9 |
| 7fe263d6-7bac-3b3e-b0a7-238a96b2c8ad | -11.3464 | -51.0423 | 2024-10-08 02:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| 846d24f7-123c-3da2-afc3-c8a8b7d58a03 | -11.5233 | -65.137 | 2024-10-08 02:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 65e24df7-4be3-32fa-8eec-50c7286398d8 | -11.5421 | -65.1362 | 2024-10-08 02:46:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 286c3854-84b5-3188-b6d0-ccfc6dcec2cf | -15.6872 | -59.4544 | 2024-10-08 02:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 7ab23494-297b-3de9-b6c7-ce096e3178d2 | -15.6874 | -59.4344 | 2024-10-08 02:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 1b500af2-5aeb-3ffc-ba6a-5ffcd87635c2 | -15.7068 | -59.4326 | 2024-10-08 02:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 405bbc62-cd15-3770-be7a-4bbe1b49c75f | -16.5902 | -46.4746 | 2024-10-08 02:46:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 854a5e4e-48e0-397e-92b9-bfa31a7dca51 | -16.4365 | -57.2575 | 2024-10-08 02:46:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.0 |
| a4c5453c-151c-3125-af16-1e757ed95e8a | -16.5752 | -55.9055 | 2024-10-08 02:46:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 30.2 |
| 42508b63-94b4-34a0-b0fd-64944b160c63 | -16.8048 | -57.4197 | 2024-10-08 02:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.8 |
| cf2ee353-5a77-3603-8bcb-b9d6a5ff9d93 | -17.1178 | -57.4244 | 2024-10-08 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.0 |
| ad921ce9-6ff8-3f60-a253-cd0d8d6cad50 | -17.0992 | -57.3651 | 2024-10-08 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 2718ae2c-5a2e-3e4c-8172-8bafa6da9101 | -17.0989 | -57.3857 | 2024-10-08 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.0 |
| 52cae379-44c4-3e98-9aea-0b5dacf6ca90 | -17.0123 | -56.6773 | 2024-10-08 02:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| da3623a7-9de6-3d02-8a3d-68b769633120 | -16.9407 | -57.4859 | 2024-10-08 02:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 384a2e4c-5b73-3178-bb0e-d96609d73771 | -18.6192 | -57.2603 | 2024-10-08 02:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.5 |


[Clique aqui para ver as próximas entradas](README28.md)
