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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0bc6dbe-dd43-3bce-9e78-37ab3ee9b7be | -11.9369 | -47.3143 | 2024-09-26 13:26:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| e527e024-e051-3dad-9d8a-9190d53dfed9 | -12.2367 | -45.5045 | 2024-09-26 13:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 205.8 |
| 6ddaa1e5-f3bb-3011-a7e6-af4f68e1d0e6 | -12.2857 | -50.5294 | 2024-09-26 13:26:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| b8c56818-fd7b-3722-802e-96db2c60e2d3 | -12.4835 | -48.9224 | 2024-09-26 13:26:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 85e17554-ef97-3ce5-8402-ca71e2a201df | -12.4974 | -50.4177 | 2024-09-26 13:26:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| ea549faf-b43c-3b00-b2be-30c414889c6c | -12.5026 | -48.9198 | 2024-09-26 13:26:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 5f9876e4-8496-38de-8944-08eebbac1a93 | -12.5464 | -53.5147 | 2024-09-26 13:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 2810b87b-3c37-31ef-80ad-906313dc7ff4 | -12.8653 | -51.314 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 759baf27-ed6d-3fba-b8f5-cd941bed16be | -12.7914 | -51.1525 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 8bcd5bdf-06b8-3af5-aa19-48e09d27bda4 | -12.8674 | -51.1859 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| f91bbe21-d35c-3f60-be2a-cb526e6924d2 | -12.8465 | -51.295 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 226f14b2-bc75-31de-8d1c-58dfac5436ed | -12.9823 | -44.7389 | 2024-09-26 13:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 15848d45-95bd-3d71-a5a5-ed8e0a601c6e | -12.8855 | -51.2477 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 1bd5d112-9456-3f2f-b513-4f1cce5be155 | -12.8462 | -51.3164 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 472ee7d0-0a84-39bf-b2a2-0d49fa98ca1f | -12.8106 | -51.1502 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 448.7 |
| 6c45cffa-ea53-32be-9480-452c44c70734 | -12.8294 | -51.1692 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 6e53df13-622e-3ac2-8851-dbce26d8e021 | -12.8852 | -51.269 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 95de76b2-aa85-368a-8b6d-d8d0e4d2aa9b | -12.8297 | -51.1479 | 2024-09-26 13:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 529.2 |
| 81dce05c-bc62-3c2b-98ba-93cd369b9a67 | -12.9714 | -45.2979 | 2024-09-26 13:26:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 138.1 |
| e8523c25-fde5-3f9f-8643-a740c215ecdd | -13.1418 | -48.5464 | 2024-09-26 13:26:20 | GOES-16 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 070e0100-3bef-354f-a152-eab401a0bff0 | -13.1967 | -45.6077 | 2024-09-26 13:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 8772eaf2-f86b-3007-95b6-4b4b9d9638c7 | -13.1796 | -45.4952 | 2024-09-26 13:26:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 460.3 |
| b5a1e0f8-da88-3313-925c-8799a5d25b83 | -13.3183 | -46.2987 | 2024-09-26 13:26:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 46b5cdb4-9fda-384a-a155-4e55362a98ed | -13.3179 | -46.3216 | 2024-09-26 13:26:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 112.3 |
| 684adff1-76f7-3670-86fc-3dcd9c07f9b0 | -13.2985 | -46.3247 | 2024-09-26 13:26:21 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 5ff7852e-89a0-364c-9b87-41d17108ef74 | -13.7335 | -50.9902 | 2024-09-26 13:26:24 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 7145bd72-2bf0-3237-9ede-737d31c866d1 | -14.5705 | -45.6973 | 2024-09-26 13:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| d7b54dbc-07a5-348f-86c8-807329019480 | -14.6924 | -45.4665 | 2024-09-26 13:26:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3855f583-2983-3d46-88ba-f0e3c1f7677a | -15.6998 | -41.0835 | 2024-09-26 13:26:33 | GOES-16 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 368.4 |
| 9e8e4b18-de5e-338c-b24a-9ad890b11030 | -17.8068 | -43.2338 | 2024-09-26 13:26:45 | GOES-16 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 202.5 |
| edbe70a8-e9b1-34ff-9553-94a431a410cc | -17.9929 | -44.4514 | 2024-09-26 13:26:46 | GOES-16 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 187.6 |
| 7c7eb4bc-d26b-3c1f-8426-5445a6d8f36d | -18.9102 | -49.1674 | 2024-09-26 13:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 147.7 |
| c6af24db-e112-30f8-b4ae-6516e8eee972 | -21.9583 | -48.5638 | 2024-09-26 13:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 222.6 |
| b23b46ca-ab13-3a56-841b-65616a0a2fc9 | -21.9374 | -48.5688 | 2024-09-26 13:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 205.8 |
| e1e66527-cd76-3e53-a993-4eb82cb0d2d9 | -21.9381 | -48.5453 | 2024-09-26 13:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 171.7 |
| a9fc10c2-86c5-3c97-abd5-396c228e4aeb | -21.9576 | -48.5873 | 2024-09-26 13:27:07 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 61228ead-ce12-34b9-84bf-cd0a837f3bb5 | -5.8808 | -48.0908 | 2024-09-26 13:35:40 | GOES-16 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d71753f2-d7f6-3e88-83f4-3197f676567f | -6.7908 | -41.2254 | 2024-09-26 13:35:45 | GOES-16 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 91.3 |
| 5755066e-d1df-3a94-806f-3f951e57b8e7 | -6.784 | -59.3052 | 2024-09-26 13:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 249356e4-37c1-313f-9b8d-13ef87b2ed2d | -6.8023 | -59.3237 | 2024-09-26 13:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 72492e6a-96fa-3273-8729-2004d08112a8 | -6.8024 | -59.3044 | 2024-09-26 13:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.1 |
| 3e361f43-6ac3-33b7-a488-05ed3b097e5f | -7.0595 | -44.1316 | 2024-09-26 13:35:46 | GOES-16 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9f541ad2-5ed6-31d7-860d-91449bd1d0e2 | -6.9306 | -63.1053 | 2024-09-26 13:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1ce88c8a-adf3-3927-a999-9c4ad629a8ba | -6.949 | -63.1048 | 2024-09-26 13:35:46 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 879ade6c-95d6-361f-a7bb-2dfe31dbd319 | -7.0981 | -59.2343 | 2024-09-26 13:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| ade49494-c9ed-3b3f-8517-a8d83790629b | -7.2006 | -60.6706 | 2024-09-26 13:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 6d8d6d0c-14fb-32fa-ad94-897c48bb4232 | -7.2906 | -61.0869 | 2024-09-26 13:35:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| daf3ba9b-98a2-3ddf-8753-8f6ff332ed10 | -7.3637 | -55.5134 | 2024-09-26 13:35:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3db85a35-2327-34f1-940e-bfa0308c5499 | -7.3639 | -55.4935 | 2024-09-26 13:35:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6b551d0e-e5ea-36a3-a943-67bee92e239b | -7.3824 | -55.4924 | 2024-09-26 13:35:49 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 498ac882-20ed-368f-b21c-10449a901884 | -8.3805 | -45.3994 | 2024-09-26 13:35:54 | GOES-16 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.8 |
| f04384f3-a67b-3d21-ab15-cf77e3df52d0 | -8.3153 | -55.0157 | 2024-09-26 13:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| c7b245ef-286f-3ad1-8326-2ca39d67b887 | -8.3155 | -54.9956 | 2024-09-26 13:35:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 96cd1d62-15d6-3eb7-987a-5b325edaf001 | -8.4646 | -62.6556 | 2024-09-26 13:35:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| a34d598e-0396-3d61-9818-1276f34ad300 | -10.0134 | -53.4875 | 2024-09-26 13:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 90be9aff-3583-3c1f-83c2-56835974332c | -10.0136 | -53.467 | 2024-09-26 13:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 4b0eebb5-0cb4-3ed8-ab0e-71ce3cff5d34 | -10.0139 | -53.4464 | 2024-09-26 13:36:03 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 0dc5c659-6754-33c3-96df-de9fdbac3d91 | -10.032 | -53.5065 | 2024-09-26 13:36:04 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 0a725455-03ec-36a8-ac6d-00f9dbabce52 | -10.1109 | -50.1066 | 2024-09-26 13:36:04 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 868455a8-01bb-3a06-8e7e-235d6ec4bf18 | -10.204 | -46.1451 | 2024-09-26 13:36:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 707f5bfa-40ce-3aed-8e53-419339d4d190 | -10.2044 | -46.1225 | 2024-09-26 13:36:04 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 52fb713c-9fa4-3ac2-bae8-97a2d553c278 | -10.6456 | -45.8407 | 2024-09-26 13:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| ea034b71-5d9d-3b77-9175-d57f5fbe79dc | -10.6073 | -51.1196 | 2024-09-26 13:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 74.5 |
| d20b52b8-154a-3523-9580-f82944f6dbea | -10.5878 | -54.2375 | 2024-09-26 13:36:07 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 6e133e67-55da-32a3-a9b2-a6e1618e2f7f | -10.8525 | -51.1581 | 2024-09-26 13:36:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 2b9f573a-7b20-3afa-8c97-517fe1fade03 | -10.8714 | -51.1561 | 2024-09-26 13:36:08 | GOES-16 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 46716e36-5d42-30c7-91cb-07690561341d | -11.1354 | -46.1623 | 2024-09-26 13:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 5fdf395f-0d11-33c0-9541-59a5bde103b0 | -11.1542 | -46.1824 | 2024-09-26 13:36:09 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 5306bd38-2ad7-302e-b280-bad0fd1535ca | -11.0535 | -50.3069 | 2024-09-26 13:36:09 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 201f40b1-dd7d-3d82-ad68-41ac1b1449ca | -11.0569 | -51.4328 | 2024-09-26 13:36:09 | GOES-16 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a9fb0016-d42e-3b29-a634-86b31a03685f | -11.0758 | -51.4308 | 2024-09-26 13:36:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 2a85e730-11cf-3b25-a0cb-eb7d7139d5eb | -11.2317 | -46.1041 | 2024-09-26 13:36:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.9 |
| e36965d2-8fd8-3005-87f6-f310a9f00283 | -11.2504 | -46.1242 | 2024-09-26 13:36:10 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 38d2c11f-1d93-366a-8062-7991bae76375 | -11.212 | -51.1627 | 2024-09-26 13:36:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c46a6b8b-5b06-3b49-b628-baa9a87c4ead | -11.2123 | -51.1415 | 2024-09-26 13:36:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 44e9f7ea-990d-3ad4-bc63-94b756373d5c | -11.1847 | -54.7565 | 2024-09-26 13:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 956ca6d4-7b9d-3c42-97d6-edf165bce0fc | -11.222 | -54.7939 | 2024-09-26 13:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 11b48c37-7bf3-3da6-bd66-f6ee0a1820bd | -11.6988 | -47.8576 | 2024-09-26 13:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0d402b22-ad4c-35bd-ae73-b7dca8414d65 | -11.7179 | -47.8551 | 2024-09-26 13:36:12 | GOES-16 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 157.8 |
| 1aa321ab-c82e-3e44-8c19-bd3c1ab225ff | -11.8422 | -49.635 | 2024-09-26 13:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 08746bc8-77f8-389c-bc22-269399247527 | -11.8613 | -49.6327 | 2024-09-26 13:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ff89f305-56e2-333b-ac3a-0ef79e56e151 | -11.8616 | -49.611 | 2024-09-26 13:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| c44e2a6c-14cc-3204-bafa-7eacbc65f409 | -11.9174 | -47.3393 | 2024-09-26 13:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 97594b94-47e0-3e25-aad7-a7b653633a11 | -11.9365 | -47.3367 | 2024-09-26 13:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 121.1 |
| a4f1d229-0da9-3149-98c9-648f0ddd474e | -11.9369 | -47.3143 | 2024-09-26 13:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| d9bddf17-217f-3965-b469-2cfb016c1da2 | -11.9564 | -47.2893 | 2024-09-26 13:36:14 | GOES-16 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| c9ca7c5e-988a-3eca-8848-c4190d75de24 | -12.2367 | -45.5045 | 2024-09-26 13:36:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| fd54d79a-ba93-3c58-8c6e-6a0f126088b0 | -12.2857 | -50.5294 | 2024-09-26 13:36:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 434b4576-f50c-3cae-b039-51b2e4b27beb | -12.286 | -50.5079 | 2024-09-26 13:36:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| b434f130-7264-3920-b532-25df2b708692 | -12.3048 | -50.5271 | 2024-09-26 13:36:16 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 23d31c8d-10ae-312e-8c1b-8d87342eaaec | -12.4835 | -48.9224 | 2024-09-26 13:36:17 | GOES-16 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| e86cdbd9-b0a8-3f9a-91c4-f4a01a44bd4d | -12.4974 | -50.4177 | 2024-09-26 13:36:17 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| b8195ad3-a79b-366e-92ba-cb342d5922ef | -12.5464 | -53.5147 | 2024-09-26 13:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| fe86ab2c-b0df-3a6a-9e0a-b26cc100d0a9 | -12.9516 | -45.3242 | 2024-09-26 13:36:19 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 66fc000b-9cf6-36fe-84fb-7d81411e98f3 | -12.8489 | -51.1455 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.8 |
| f99275ca-1150-350f-9280-8d23a994ecb9 | -12.8653 | -51.314 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 2291a523-3789-3f6e-a6a6-48bbd67c6daa | -12.8674 | -51.1859 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 2d13a860-5bc5-3270-94b1-6b945348d3be | -12.8852 | -51.269 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 89aa11d9-dc7d-3a4d-8eb6-e13cde55a1fb | -12.8855 | -51.2477 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 3f6adce8-7777-3c12-921e-d48b3dfa3417 | -12.7914 | -51.1525 | 2024-09-26 13:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |


[Clique aqui para ver as próximas entradas](README188.md)
