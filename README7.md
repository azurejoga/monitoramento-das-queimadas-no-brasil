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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36db9eed-1ba3-322e-87f7-13230345c0a8 | -3.36589 | -44.20285 | 2024-11-28 00:11:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 880cca37-3e84-3fd0-9bc5-3a787df3bd83 | -3.6675 | -45.80091 | 2024-11-28 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 141.5 |
| ae034caf-8c00-349b-b9c3-ea4ea92a67a0 | -4.93814 | -45.42377 | 2024-11-28 00:11:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 0df420bb-d0ee-3606-b37d-ce1fe2564982 | -4.92417 | -45.42593 | 2024-11-28 00:11:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| ac6f2def-3658-3a49-b1b0-fcdcace7a200 | -4.13513 | -46.12142 | 2024-11-28 00:11:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 5ee09db6-500c-3ef6-84ea-7d9aed7e78bf | -4.00403 | -44.28159 | 2024-11-28 00:11:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1c11021b-e9bc-303e-8ce0-2f2bac9ecc19 | -2.39084 | -47.17251 | 2024-11-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 34cd8c78-410d-35e2-8eff-ef824aae3bdc | -4.76807 | -44.4316 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 367.6 |
| ef251754-8728-3833-987f-3772d702b66a | -4.90935 | -38.73929 | 2024-11-28 00:11:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| d28f7554-4eea-325a-81cb-8fe25701be82 | -3.95224 | -41.49054 | 2024-11-28 00:11:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 1bc7ed26-2dbc-3f00-bf7d-dc6e894e9ef1 | -2.88512 | -45.36875 | 2024-11-28 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4389edf3-0724-3b1f-8b11-465134221abb | -3.3339 | -45.50724 | 2024-11-28 00:11:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 77966b00-22a9-369e-90ad-1945c6d2d6fd | -3.67071 | -45.82554 | 2024-11-28 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5a912c5d-4fd9-36bf-9276-8ee8d7a6f3b6 | -3.70812 | -43.41992 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 98a9615a-1f50-3f01-ada3-45db4ca5c164 | -6.16907 | -42.6197 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 191.7 |
| 09c22a63-d282-3bf7-a9ac-95ac0ddcda15 | -4.79807 | -44.4627 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| bf011209-45c2-39d8-80ba-dc41fcdbbb4e | -6.08822 | -48.01072 | 2024-11-28 00:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f268b6a8-12fd-3bab-b241-3d7b892ca62c | -1.96002 | -46.56631 | 2024-11-28 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 33.3 |
| 4a4c4a88-65ad-3a9c-9fef-3c07c38ebcd2 | -2.88821 | -45.3907 | 2024-11-28 00:11:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 37.5 |
| c6b9637a-e59e-3a81-a6b5-126ee091ff46 | -6.37319 | -45.70584 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| a61cc131-4dc4-3da2-bb50-ef5d5a97383a | -6.16712 | -42.60453 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 27.7 |
| f4e58572-0e02-3d1e-a02c-57f28d48ed23 | -3.20877 | -46.58956 | 2024-11-28 00:11:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 8fca2d76-71ff-3473-8fea-00b31776621d | -3.54466 | -44.37949 | 2024-11-28 00:11:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| f245b082-cbec-3d34-9003-e34225797dc7 | -3.19479 | -46.59696 | 2024-11-28 00:11:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ed0458dc-f618-37c6-8076-6e7d3b4e2b2e | -3.54726 | -44.39838 | 2024-11-28 00:11:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 827826c0-2e23-3dab-9958-e60e97363600 | -3.67761 | -45.80496 | 2024-11-28 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| a73cae19-123f-3b73-9a19-dfd085b0b834 | -2.86485 | -46.86255 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 254.3 |
| a8a8a021-8b12-376a-a8a0-1ad5e8e67696 | -3.70256 | -43.44248 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 0f8d94cc-dcae-3b2b-8a6c-7c7806456537 | -3.67842 | -45.77461 | 2024-11-28 00:11:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 61.2 |
| bcfd694e-0249-3098-9171-e92534c25068 | -2.29402 | -47.13008 | 2024-11-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| a3c9a6c9-684a-3b1e-b37c-f1336b664995 | -5.21026 | -41.2793 | 2024-11-28 00:11:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 72209c7c-acb6-3325-b3fb-8f6a7cd8951e | -2.23108 | -46.12043 | 2024-11-28 00:11:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9f39467b-f488-3d51-8d0e-7c95e3b02ac9 | -4.7373 | -46.55346 | 2024-11-28 00:11:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| ff080fdf-4af2-3f79-87ce-9bfce3eb8d3d | -3.08658 | -41.14106 | 2024-11-28 00:11:00 | TERRA_M-M | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 45828396-bd16-3195-9d31-7b1b102d1ce1 | -4.78257 | -44.44465 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| eb5ffe6d-83c0-3c40-a591-456b98fed7ff | -2.48589 | -45.42478 | 2024-11-28 00:11:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8925fac1-1ec2-3da7-bb70-35438b4400bd | -2.29002 | -47.10011 | 2024-11-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 39218653-99cf-313b-a3fa-384b0d4fb324 | -2.3305 | -46.17714 | 2024-11-28 00:11:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f5ead25d-f970-3d9c-8c0f-773fde62f9e5 | -3.49691 | -44.60059 | 2024-11-28 00:11:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| c6ea4dcd-16df-3a99-be85-c4dacfc154bb | -6.17101 | -42.63486 | 2024-11-28 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 4ca811bf-fc3b-375d-9c53-a1e83cd23751 | -4.0384 | -46.54453 | 2024-11-28 00:11:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 375493d2-664d-36b1-95f1-c615e68aff98 | -3.86205 | -40.44169 | 2024-11-28 00:11:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| efc74340-305d-3cb3-8c3a-0de06f5f40d4 | -2.05091 | -47.12199 | 2024-11-28 00:11:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 64fc4e5a-dcfe-3f69-83e3-1741ac0552ff | -1.5273 | -47.28985 | 2024-11-28 00:11:00 | TERRA_M-M | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 69408f88-0f59-3a53-b478-04d54f8c95c6 | -6.1047 | -48.0544 | 2024-11-28 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| bc61ecb4-c6a4-3669-9c40-8a1739ae57a1 | -3.6644 | -45.7676 | 2024-11-28 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c4df81a0-3c8b-3698-ae3f-6d923410c9d7 | -1.5897 | -52.271 | 2024-11-28 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.0 |
| a5755d7b-cc93-3795-be10-a391144131ff | -3.4022 | -50.1119 | 2024-11-28 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a03fcaa0-223b-316a-930a-c0f30015fd5e | -6.1737 | -42.5985 | 2024-11-28 00:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 61.4 |
| fb29fc4c-9b5d-30c3-bb65-2f298255255c | -2.8424 | -46.8413 | 2024-11-28 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b77a2511-aebb-3576-882d-8eb0e0afb837 | -3.1114 | -53.8041 | 2024-11-28 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| afa03a7b-20b9-3caa-a9c6-8da69fed409b | -5.9788 | -45.3621 | 2024-11-28 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 22a6fd6e-96b4-3dec-8637-50b2363a73a8 | -6.1048 | -48.0327 | 2024-11-28 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 174.3 |
| 19c9b1f0-61ac-3dc3-8733-f3f6de2f3970 | -2.5963 | -53.9771 | 2024-11-28 00:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 746ad8c2-eea3-3ec7-add2-99b7ac5b809b | -5.979 | -45.3395 | 2024-11-28 00:20:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 22d0f3ca-7ef1-362d-901e-5c622df80f09 | -2.8795 | -46.84 | 2024-11-28 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| d13e6fe3-216b-3d5a-9875-eb52b5ec31a2 | -3.9674 | -48.0851 | 2024-11-28 00:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| b28cb024-a086-3a67-8844-222f6bf161bd | -2.8423 | -46.8632 | 2024-11-28 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 599617ae-e648-33ee-8547-0b8ede3cb9cc | -3.6643 | -45.7899 | 2024-11-28 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 162.2 |
| a7ce3633-fbb5-31cb-b654-63dc01da6242 | -6.086 | -48.0557 | 2024-11-28 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4be5dfd6-ff94-31d9-b6ed-c390a27c337a | -6.1735 | -42.6221 | 2024-11-28 00:20:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 84fe6835-5cbf-372f-82d4-e86f2c819cb6 | -2.8794 | -46.862 | 2024-11-28 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 4c490e5d-d3ad-33c5-85a8-e66a010f89a2 | -3.093 | -53.8045 | 2024-11-28 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5693ec75-8151-3a27-93aa-63b6e7b00f3b | -3.1113 | -53.8242 | 2024-11-28 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| ecd7631f-3619-3c72-a09c-6438699146e7 | -6.0862 | -48.0339 | 2024-11-28 00:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 208.1 |
| d33eb19e-3d35-3a4c-9294-1aa73a65aa32 | -1.3329 | -51.9463 | 2024-11-28 00:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 532b5e53-51a0-34da-8f50-17c0abc09ba6 | -2.244 | -48.5306 | 2024-11-28 00:20:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 45cb34f9-d469-3d20-a1db-d2564a1c1a03 | -2.8347 | -54.1125 | 2024-11-28 00:20:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 308405d3-fd2e-3628-9138-0787db9a6d2b | -3.6962 | -43.4432 | 2024-11-28 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 0e96c5eb-40f0-3f94-9d82-709115787eea | -6.1547 | -42.6237 | 2024-11-28 00:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 1113e04e-cc38-368f-a3d4-8e01c706757d | -21.0803 | -49.8023 | 2024-11-28 00:20:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 6ec5f155-7f84-3138-9fa4-e132cf7695fc | -6.1041 | -43.9593 | 2024-11-28 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 161.8 |
| cb5f8730-7d00-361a-b256-c0ec5794fdc2 | -3.0929 | -53.8247 | 2024-11-28 00:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 0ba1e2df-fbac-3884-a8e9-564cfff0aa66 | -2.861 | -46.8406 | 2024-11-28 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 142.8 |
| 45a1c12e-5133-34e9-a610-be50b0c1ce41 | -6.1039 | -43.9824 | 2024-11-28 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 16a9a51c-4b3f-3072-b8f1-dff8a7f95eb9 | -21.1009 | -49.7978 | 2024-11-28 00:20:00 | GOES-16 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.7 |
| f3afbd05-d800-3331-91cc-18f2c733a002 | -3.3837 | -50.1125 | 2024-11-28 00:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| b10a80ef-3b75-397d-bc58-9fba2da6a318 | -3.6963 | -43.4199 | 2024-11-28 00:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 79dd5649-905f-3986-96e8-8f98d35fff7f | -18.784 | -55.8416 | 2024-11-28 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.1 |
| 4ecc79a1-565a-3ca0-a714-2b6b5de8af10 | -21.1329 | -48.6426 | 2024-11-28 00:20:00 | GOES-16 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.3 |
| 99f9b276-3777-3c87-90a6-b5d75d58594b | -2.8609 | -46.8626 | 2024-11-28 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 2b9a02dd-3780-3627-a91b-c9f4c9d66535 | -18.764 | -55.8444 | 2024-11-28 00:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.5 |
| 8233fca9-8f6e-3f27-98a3-98c4961970da | -3.6829 | -45.7891 | 2024-11-28 00:20:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 11ec21b6-9734-3dc7-aa74-0625319eeb39 | -2.8347 | -54.1125 | 2024-11-28 00:30:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| e4c1808d-5ce7-3868-9407-88d7fc087cfe | -6.086 | -48.0557 | 2024-11-28 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 136ec092-9084-3c55-857d-c5fe7bc365e8 | -1.3329 | -51.9463 | 2024-11-28 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 71fc0ee0-daf8-3741-beda-90429abcbfe8 | -5.9788 | -45.3621 | 2024-11-28 00:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 214.2 |
| ea6fadf8-d0c6-3f5c-ade3-f73b6eb87a68 | -3.6963 | -43.4199 | 2024-11-28 00:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 8bd752fe-240e-361d-8807-a657c758b890 | -1.5713 | -52.2713 | 2024-11-28 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| cc952df3-4f73-3d6e-abd6-0bd650dc6f76 | -18.7843 | -55.8206 | 2024-11-28 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.7 |
| 80189b8b-1bee-30ea-93f7-c2c3d4914bc3 | -6.1039 | -43.9824 | 2024-11-28 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 23e39b0b-5dd6-3607-ab28-1b49c8079bb9 | -1.3329 | -51.9257 | 2024-11-28 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| aa3fea1c-048b-38d5-8a15-4a61787f8008 | -1.3145 | -51.9259 | 2024-11-28 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| d7399718-06a0-3718-af07-adc2747e4f87 | -1.5898 | -52.2505 | 2024-11-28 00:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| f6cd8c3e-5c29-3deb-abe5-a9089c961647 | -3.4022 | -50.1119 | 2024-11-28 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 73c52533-5a0d-3a0d-90bf-a857520c89da | -1.3145 | -51.9465 | 2024-11-28 00:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| f25d9b5a-a0f1-35e4-9cca-9fdc08d11a0d | -6.1047 | -48.0544 | 2024-11-28 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| f5f48c0f-2a88-3694-905b-341792231d14 | -20.6702 | -49.1155 | 2024-11-28 00:30:00 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 36e526dd-ab09-3747-8a58-81e848256ae3 | -18.784 | -55.8416 | 2024-11-28 00:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| 2d2ba8bd-338c-317d-bded-2111c4d80f62 | -6.0862 | -48.0339 | 2024-11-28 00:30:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 197.7 |


[Clique aqui para ver as próximas entradas](README8.md)
