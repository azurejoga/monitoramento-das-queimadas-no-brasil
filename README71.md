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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fd1c623-fbb3-3a2e-8acb-a26b542fcac9 | -13.40601 | -61.92615 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7533d125-a0a5-36d8-b8e0-6e285418dfb5 | -13.40559 | -61.93376 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50c144f2-7ac5-3029-a654-27cf6e9f186d | -13.40489 | -61.93159 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ce17f8f1-a1d9-3b5f-8164-91a72b6a54a5 | -13.39804 | -61.93781 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f393685-bd82-3223-b3bb-75182b2d40e0 | -13.39738 | -61.93566 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 456e5421-e14b-3e4d-950c-2ba287c2e621 | -13.39626 | -61.94106 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9009008f-f6f8-346d-ad67-e1327602e6a8 | -13.39166 | -61.93644 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 57b11eec-4fff-33f7-9ca4-f128d29349bc | -13.38644 | -61.92963 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| af4784d4-be23-322f-ac92-f5158daabaaa | -13.38575 | -61.92741 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 916b0672-3fef-30f0-81c2-b4ffb3fbcbb2 | -13.38462 | -61.93283 | 2024-10-08 04:36:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ebdba2bf-9cb3-3f1c-b90f-4ddca4dd43dd | -11.88893 | -62.77317 | 2024-10-08 04:36:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ea303c9-d086-366e-af7a-6973154fef9e | -11.88209 | -62.77154 | 2024-10-08 04:36:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6641c5fb-bb05-315e-b469-42199c62a6c4 | -11.77129 | -62.88593 | 2024-10-08 04:36:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6bbad009-5c4c-3f19-aa94-c096435a35c7 | -11.48045 | -61.98135 | 2024-10-08 04:36:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a77e7ce9-0f3f-3ce6-aa86-2d604149cf24 | -11.48166 | -61.97551 | 2024-10-08 04:36:00 | NOAA-21 | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b33dd634-3d00-3eec-8b48-d499c7463fdb | -12.85115 | -62.80167 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0cc8b558-d39a-3056-a782-d5a2184eb48a | -12.82959 | -62.46023 | 2024-10-08 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 333402c1-a28b-31ab-9fbe-80b07d8ed4da | -12.82592 | -62.46138 | 2024-10-08 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2edc555c-9241-3105-b3e2-39f68560b6ba | -12.82295 | -62.4588 | 2024-10-08 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23bbd6b1-f055-39c0-a689-1fc612410a06 | -12.82167 | -62.46488 | 2024-10-08 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9735a881-883b-307b-99f1-eb4b0653f119 | -12.70225 | -62.96275 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1f10aeb3-0a5c-391e-b5f6-edcd6957e5df | -12.6954 | -62.96126 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f8d4d5fa-85f8-3fbc-b57e-feeafd061216 | -12.69273 | -62.94025 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 844fe9cb-ee30-3b7a-ab6c-1481d98b9bc4 | -12.69134 | -62.94675 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ab1a0f6-e644-3081-a8c7-dfb2624de1ef | -12.68995 | -62.95325 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d1e4f98-1020-3aa4-bbdd-fd26725bbb4b | -12.45585 | -63.00802 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b1768c3e-40e9-3401-b927-a11232ea976a | -12.44896 | -63.00653 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| f00a260e-ffc5-3833-bdc6-50b72707c833 | -12.44611 | -63.01984 | 2024-10-08 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f5ee3a8f-29f2-3c91-82cb-75f01c52fe73 | -12.74882 | -62.26518 | 2024-10-08 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e77cead5-66b2-3432-95e5-311dc98c2fa6 | -12.74761 | -62.27095 | 2024-10-08 04:36:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bcb6c86a-aee0-32b6-bb4d-ee399c5de35c | -10.6256 | -55.9154 | 2024-10-08 04:36:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 41866fb9-e723-3fd2-84e5-b30580d09a9d | -10.8568 | -63.8988 | 2024-10-08 04:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 40.6 |
| e58ecd19-8cdb-3df2-9278-f7aa2a31412e | -10.8754 | -63.9169 | 2024-10-08 04:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 9887026d-4997-3758-8861-9255e014d44f | -10.8755 | -63.8979 | 2024-10-08 04:36:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 60511e78-52e9-345c-abfd-27e453df9916 | -11.5233 | -65.137 | 2024-10-08 04:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 41.9 |
| dbcfcafc-ced3-3bc3-bc90-c35de085e942 | -12.5717 | -53.0753 | 2024-10-08 04:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| ad49923f-c823-34c6-b997-d84193ae341d | -12.572 | -53.0544 | 2024-10-08 04:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| e78dc652-262e-3174-a722-4e25cb099ba1 | -16.5512 | -46.4592 | 2024-10-08 04:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 95.4 |
| d57fafa9-d74f-3e91-a710-8cac292c192c | -16.571 | -46.4553 | 2024-10-08 04:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 3f8abecc-6e07-3d28-a7d6-24cec277dcac | -16.5715 | -46.4321 | 2024-10-08 04:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 1837047f-244d-3535-95b5-16a0590063a9 | -16.5908 | -46.4514 | 2024-10-08 04:36:38 | GOES-16 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 85.3 |
| ff7ffa05-c5c4-38cf-926e-8c9f033d1488 | -16.8048 | -57.4197 | 2024-10-08 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 9bf7097b-31ea-3f71-83e1-f197ccdc7608 | -16.9211 | -57.4881 | 2024-10-08 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 5f320838-68c4-3867-aba6-97b307d486c7 | -16.9214 | -57.4676 | 2024-10-08 04:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.9 |
| 133d57db-5702-341a-8dda-0b4806f526f3 | -17.1074 | -56.851 | 2024-10-08 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.2 |
| 01194535-4aa2-3895-8a9a-3b97aae4234a | -17.0992 | -57.3651 | 2024-10-08 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 9e207238-ac69-3412-9aef-7bdf4edd961e | -17.1078 | -56.8304 | 2024-10-08 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.3 |
| 4580494a-10c9-34b9-9a03-e8af96f4c044 | -17.1178 | -57.4244 | 2024-10-08 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.1 |
| 4884205b-4c0a-3f00-91e9-bb4eaee1c9a4 | -17.1271 | -56.8486 | 2024-10-08 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| 0452ff70-0e2e-302f-95c9-aa8f22a73b45 | -17.1274 | -56.828 | 2024-10-08 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| ecac8bed-66ac-3cd6-b22b-bef459ab8324 | -17.0982 | -57.4267 | 2024-10-08 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.9 |
| d8f12514-6068-3715-8d07-95a8b248fd87 | -17.0123 | -56.6773 | 2024-10-08 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 67.4 |
| 6c971874-ca07-325a-9ceb-7a5001a9e028 | -16.9927 | -56.6797 | 2024-10-08 04:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| 7f2fd2a0-5ec7-3592-83da-1a0d6a58762f | -16.9407 | -57.4859 | 2024-10-08 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| d0a4730a-8c16-3e59-9ccf-096fa5be1d58 | -16.941 | -57.4654 | 2024-10-08 04:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.1 |
| 4fcd5ed7-b56e-3926-bc2d-bc85538770b1 | -17.1677 | -56.7614 | 2024-10-08 04:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 46.9 |
| 62faef14-2c1c-327b-b010-e39ce493b36e | -17.1681 | -56.7407 | 2024-10-08 04:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| 7a1ef815-fcaa-3b98-a7cc-aff54e0fc955 | -18.6192 | -57.2603 | 2024-10-08 04:36:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 36.0 |
| fa7bbdfc-efa9-3ed4-a4f1-ac41498d04e1 | -20.07727 | -55.96287 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b704f92b-ee92-3ab7-94bd-c3af4012e0f8 | -20.07629 | -55.96814 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 629e7f07-15ca-35b8-b0fd-3f26378902ab | -20.07337 | -55.96207 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| cf6d2ad4-befe-3ee7-a5a9-6a4756231ab2 | -20.07239 | -55.96734 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e9a7bfe5-8c90-3c69-9b7f-23563a4448ab | -20.06946 | -55.96128 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e7f8b824-e532-3954-b1d9-21b820f58cc1 | -20.06848 | -55.96654 | 2024-10-08 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 349b2053-de80-32be-86b7-7ce6af17c1d1 | -21.3505 | -54.61369 | 2024-10-08 04:38:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4612df80-b65f-369a-b3fa-c9443bea0dbc | -20.44067 | -48.79955 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37f35323-7cfd-3b85-9108-ee72a9b5992a | -20.42163 | -48.80883 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07ab5669-20c6-3bb7-afdf-78b3830665a4 | -20.42105 | -48.81284 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| edbe2dc2-0038-3041-a533-9577fbe027d5 | -20.42047 | -48.81686 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c84a94f6-c003-3e7d-a798-e66b5ae5c6d5 | -20.41989 | -48.82089 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b6b2e3e4-ae34-3774-870c-68de243ecb47 | -20.41761 | -48.78761 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41784970-7350-3b89-867b-be1d20906840 | -20.41759 | -48.81227 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 3b11f03a-df63-36e6-8cb4-affb208bad84 | -20.41703 | -48.79163 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98b1cf40-1c15-3b74-b4a0-360c6d60794e | -20.41702 | -48.81629 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 815acfee-4d3b-395d-aa12-bda43a45b301 | -20.41644 | -48.82031 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2643580b-a00d-3712-8b3d-0b5cd2c84953 | -20.41586 | -48.82432 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 22.1 |
| caf5384b-fd90-37ea-8bf0-004d675ef900 | -20.41528 | -48.82834 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7463938a-2883-3c16-a0e7-5a88c7eea3f8 | -20.41414 | -48.81171 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 12.0 |
| db85e37d-79d9-3f78-a6dc-fe908146b177 | -20.4147 | -48.83237 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8812a51c-4551-3a23-8b0f-952f17c27a13 | -20.41412 | -48.83639 | 2024-10-08 04:38:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad231ba2-eb7c-3f1d-8483-ac57c786240e | -21.85433 | -48.40965 | 2024-10-08 04:38:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e7cfc25c-68ca-332e-ac84-f59060dd0b03 | -21.85373 | -48.41399 | 2024-10-08 04:38:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9d05a843-0ea1-3797-bfdd-572d4a523e25 | -21.85196 | -48.40041 | 2024-10-08 04:38:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3f8073c-298f-3da2-9751-eb7a46759d5d | -21.85017 | -48.41344 | 2024-10-08 04:38:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ecacc6c4-3ae5-32ea-8f7a-49245c508276 | -21.84957 | -48.41779 | 2024-10-08 04:38:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c03125da-d37c-3714-b593-fb3b8597f851 | -22.80252 | -48.46312 | 2024-10-08 04:38:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4706859-3646-3043-b80a-aa9e71b81809 | -22.48291 | -48.37308 | 2024-10-08 04:38:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95dcada7-e947-3d6b-ad94-f48026fcac3a | -20.3842 | -48.82323 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23898542-1523-37ed-9ff3-9d165a00b561 | -20.38362 | -48.82725 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e34fdcb-cad1-3e0f-a758-c30f26a7e5aa | -20.38362 | -48.80257 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c9a87f3e-9c9c-381d-bde6-40bd673c314b | -22.30423 | -41.88109 | 2024-10-08 04:38:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| fec2a6c5-0c1a-3b94-a801-0b5d0df03811 | -21.96551 | -41.51965 | 2024-10-08 04:38:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 203cf318-d953-3942-b472-36f4d3fdbcc3 | -21.9639 | -41.51815 | 2024-10-08 04:38:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9e9f564b-793c-3e36-a72a-f9a825d80ae6 | -21.96007 | -41.51899 | 2024-10-08 04:38:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8c6371fb-532a-35e3-af53-1a0e9f62b6aa | -21.9331 | -41.55208 | 2024-10-08 04:38:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 268ada36-1c1f-3816-ab5b-2404ba278ae7 | -21.93274 | -41.55579 | 2024-10-08 04:38:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a2e479e6-60f7-31dc-acb4-beb62bc5eee6 | -21.16779 | -42.19572 | 2024-10-08 04:38:00 | NOAA-21 | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2782f5b2-82cf-35b8-842a-497e7f318647 | -21.16747 | -42.19896 | 2024-10-08 04:38:00 | NOAA-21 | LAJE DO MURIAÉ | RIO DE JANEIRO | Brasil | 3302304 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 66b9cf0d-5ca8-366f-a223-2bcaf411684a | -21.16232 | -42.19819 | 2024-10-08 04:38:00 | NOAA-21 | PATROCÍNIO DO MURIAÉ | MINAS GERAIS | Brasil | 3148202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c34f6c51-8edb-3686-b711-4f5563ed6a1d | -20.69444 | -43.29818 | 2024-10-08 04:38:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README72.md)
