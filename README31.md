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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47224e71-4d64-355d-9749-ec30677b16f4 | -14.78152 | -48.31569 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e060c9f4-dc95-3809-affd-695eb1b94db6 | -6.93435 | -45.40063 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 890ad1bb-b3a3-3dcf-96cf-483a346c4835 | -7.17346 | -41.70586 | 2025-09-30 03:49:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 9d10f395-ab30-3ff3-8f1d-727cec797c26 | -15.47072 | -47.94082 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6fce14d-4b10-35b7-994c-0a54ec062caa | -16.42392 | -47.04314 | 2025-09-30 03:49:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dce7d4f3-170a-3823-bae5-63f7ab406ac9 | -17.39416 | -47.14311 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 437deac6-996d-3416-b40f-0d2d0dcc5fcc | -5.70445 | -42.64227 | 2025-09-30 03:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2fcd0230-ed64-34fd-968e-0045dc7bceba | -12.8726 | -46.78224 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ee67ca3-d1cf-38ca-9d9b-329bf2ffeb4b | -11.64977 | -47.48867 | 2025-09-30 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c24a1ecf-8cf4-36bc-9d09-224052be38ae | -11.75274 | -46.8465 | 2025-09-30 03:49:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5a7c369-2172-3d18-9db4-decac21b7811 | -13.21781 | -47.31638 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 90d37aff-ab3c-30bf-b5d3-147939c18ae4 | -5.73441 | -42.68371 | 2025-09-30 03:49:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 05c81c21-6be3-33c6-9e3f-14db8992d7db | -11.75422 | -44.743 | 2025-09-30 03:49:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b9bd6b99-64e1-3196-be03-a4efafaeb197 | -15.25184 | -49.71431 | 2025-09-30 03:49:00 | NOAA-20 | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 44117c00-13ba-3380-a30a-e7c82c4e92b2 | -13.7325 | -48.67822 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b67f876-6f40-3e61-ace1-6ea0192d6d31 | -11.22474 | -47.2051 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67c3a581-2e1a-3b21-a6d4-ec7545e7f190 | -17.47062 | -46.20513 | 2025-09-30 03:49:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e847e8e3-7872-38d1-a8f7-fd8550014280 | -14.08396 | -44.0909 | 2025-09-30 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53352103-991f-3dd9-bfeb-4545f325fc22 | -12.95571 | -48.40826 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d9ae47c-7cdd-3fa6-9628-7bc17c8b072c | -6.37351 | -45.64547 | 2025-09-30 03:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f12ba848-f69d-3b8a-b1d3-d37b8e0e19b4 | -5.85804 | -45.7555 | 2025-09-30 03:49:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1729114-f331-3ec3-bfda-c369a39553d0 | -15.49185 | -48.55746 | 2025-09-30 03:49:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 435e9e25-f0e6-34b5-8dec-102756ca0b16 | -13.59827 | -43.46121 | 2025-09-30 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 875d65d6-83fc-3b99-9cb9-15cd1b37e055 | -13.59027 | -48.04932 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef0ffdc2-ec15-323d-9fe3-a2c6a0c66ea1 | -13.56423 | -48.0672 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ca9982e-1612-38eb-bb7f-bb89fa7fce60 | -12.82786 | -47.00055 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1ccc0a80-2468-3d41-aa43-56f18cd81d3e | -13.59911 | -43.46099 | 2025-09-30 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ab2ae741-3a93-3280-ac36-e263dd85f8b6 | -13.73553 | -47.90165 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 924cde4c-b2a3-31b7-8ae7-957aaeb2c07d | -6.40239 | -42.81662 | 2025-09-30 03:49:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e03b195b-edc9-3c25-b3eb-9db0f7133d01 | -13.15959 | -42.35541 | 2025-09-30 03:49:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 351a1b05-2b45-3853-b251-1d4b012d5df3 | -13.40051 | -47.54485 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d77ec550-e2fa-33a1-ae10-f68bddc2f7f8 | -17.71815 | -46.63428 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f4243eb5-e672-3940-a4c9-bf7fc02c0ff0 | -13.34707 | -47.84226 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5733cb57-60f6-37cc-87ec-2bd0d96da502 | -6.20547 | -44.21434 | 2025-09-30 03:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd8b81b5-b17d-3b88-93a6-979989a1869e | -5.52605 | -43.87709 | 2025-09-30 03:49:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3425e57a-50be-39b1-b83f-8954f4307625 | -14.55352 | -48.48298 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ea46a36c-fb71-3ed8-80fc-19409919e7d3 | -15.24506 | -49.71759 | 2025-09-30 03:49:00 | NOAA-20 | IPIRANGA DE GOIÁS | GOIÁS | Brasil | 5210158 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a9c20e43-9532-33fb-8af7-5c2b971b2ee0 | -14.71163 | -48.23483 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ea9e1d5-b172-3bb8-9eff-647f91fee2db | -6.93383 | -45.40362 | 2025-09-30 03:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ea4f385-51ec-3cfc-b6e6-07ee5f2529f4 | -11.88536 | -48.02666 | 2025-09-30 03:49:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2f7b83ba-7120-3853-9418-6c346c5d4374 | -16.40811 | -43.72472 | 2025-09-30 03:49:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41852fa6-d580-3a77-b007-f1d877d78143 | -14.5687 | -48.46408 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 484221cf-e980-39a2-b33d-03b13f2c1780 | -14.50625 | -48.4632 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c40e3392-1d63-35e4-b923-d09a85dda9a2 | -13.23849 | -48.44359 | 2025-09-30 03:49:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b7fc6e2-0cd1-39ee-a1be-d1255a3ac65e | -13.40536 | -48.15014 | 2025-09-30 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8ba33f37-7c05-383d-a711-c1bf4119fc17 | -13.06933 | -47.07635 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99c91bbc-6ee8-3f1c-b811-182321df3fc2 | -14.55234 | -48.26502 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72aa60a6-6ece-327d-accf-6dbd10a17e99 | -13.5944 | -48.03478 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 659f0c06-816e-3df1-a49a-b76f0eef6359 | -6.88848 | -44.52428 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d11ae700-457b-38f4-85ee-f7da6e904867 | -12.85257 | -46.99318 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ad742805-f183-31a6-b85e-ba4036771c63 | -16.03375 | -48.00362 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54f60798-04ea-389c-b712-92761bae8583 | -17.40955 | -45.04553 | 2025-09-30 03:49:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d913a22f-e219-35c2-912c-a77d05dcad22 | -13.40603 | -47.54456 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e2653f51-58a0-3205-af27-206b653c22a4 | -17.23759 | -44.11274 | 2025-09-30 03:49:00 | NOAA-20 | ENGENHEIRO NAVARRO | MINAS GERAIS | Brasil | 3123809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e363e02b-8a55-35c6-86cd-850b7a53071a | -11.05925 | -47.82755 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5cecdd61-4282-3c34-b082-6aa6494524b3 | -7.20805 | -45.47569 | 2025-09-30 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f1d9844-51ff-3e0a-a89a-38ed592640a8 | -14.69692 | -48.2524 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15f1d98a-9a54-3523-9dd9-95101968f8c8 | -7.21315 | -45.47671 | 2025-09-30 03:49:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f1ec767-97bc-3c3e-b20d-6db30b47f49c | -14.65212 | -46.96501 | 2025-09-30 03:49:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49e9dc04-652e-399e-8ee6-cccaa25cf9de | -13.36521 | -47.30998 | 2025-09-30 03:49:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75d99e2a-007e-34fb-82f5-cb6a48075be3 | -13.38196 | -48.06537 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 855fa351-e91e-337e-b0b8-de51567480da | -15.26468 | -47.85856 | 2025-09-30 03:49:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e524e1ed-2d29-38a2-b961-3a7eab81c421 | -14.72021 | -45.23916 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b756b675-d4f6-3405-90ff-c5627cd86730 | -11.94009 | -43.91932 | 2025-09-30 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85f3e1e0-d5cb-362b-8483-a0c73390cc88 | -13.21651 | -50.94392 | 2025-09-30 03:49:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 54fc9b00-b83b-343d-b90e-8adefa5d0642 | -12.69317 | -45.28444 | 2025-09-30 03:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6522a15-7f94-3c06-bfef-841c21b62155 | -16.85449 | -41.13947 | 2025-09-30 03:49:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96edeaf3-f8f3-33ef-9872-f7d11a953646 | -11.64184 | -47.49253 | 2025-09-30 03:49:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f2b78af4-d9fb-37cf-a4d9-949a6b35a1c4 | -7.30024 | -42.84298 | 2025-09-30 03:49:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9f6468bf-0f21-3bdf-abe9-4378c7978780 | -14.52464 | -48.48483 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 83c37dad-9a24-395f-8471-e067f43d077e | -11.25367 | -47.22832 | 2025-09-30 03:49:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3dbef319-ceb0-3163-85e5-a8cb6d711b16 | -14.5173 | -48.43698 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2daf227e-89ce-3c09-8429-b8cbe9c7f32a | -14.08811 | -44.09171 | 2025-09-30 03:49:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14160975-fc2e-3bf0-b14b-01804eea9afd | -17.72269 | -46.63545 | 2025-09-30 03:49:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3ceaff5-9ccf-3422-b039-2694e8aac1cf | -14.57815 | -48.22075 | 2025-09-30 03:49:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db008344-7de1-3334-8354-fb311df07453 | -6.49594 | -44.26868 | 2025-09-30 03:49:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 08fab6b0-5f9e-3633-b8d3-d62c2867f853 | -5.91303 | -43.70994 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da323845-18bd-33b7-ad3d-7fa5d4726de9 | -5.91365 | -43.91434 | 2025-09-30 03:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9053d2c6-3395-321a-b5ff-f95769cd6535 | -13.71502 | -48.64908 | 2025-09-30 03:49:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1892e435-97d2-3125-8e88-2a40fb7c501f | -13.36601 | -47.91625 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ed761d2-373c-323e-8e31-1b2c06556689 | -7.05258 | -45.19201 | 2025-09-30 03:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 40cbfb0f-8e1c-35d8-a474-c850caaade83 | -17.17393 | -42.83433 | 2025-09-30 03:49:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 04c70295-0388-3c3c-ac12-a8f59e0c4142 | -17.39185 | -47.15466 | 2025-09-30 03:49:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b558430e-b410-3cb7-84ef-2cefc28db906 | -13.78396 | -47.96627 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83dd5d02-d163-3a41-bb5d-5327f360b647 | -11.94083 | -43.91515 | 2025-09-30 03:49:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a10bcb15-3a5a-3a67-9e99-8035ac6c9820 | -18.48151 | -44.01888 | 2025-09-30 03:49:00 | NOAA-20 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f42b2aae-6525-39fa-9afa-914d233a5d35 | -12.83369 | -46.98083 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2884950b-744f-3ff3-9c3a-376747ab5a4b | -5.32384 | -45.23173 | 2025-09-30 03:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c69f61f2-cf00-356c-a263-505c616bad14 | -12.82261 | -47.00015 | 2025-09-30 03:49:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1efe25d-a4e0-3a8a-ab37-b0a861b7ed3b | -11.06393 | -47.83328 | 2025-09-30 03:49:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 56db1850-a9b1-32cd-8659-d34a0a4c4f94 | -14.62482 | -44.95123 | 2025-09-30 03:49:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d16b8b19-c253-3c65-8695-ee933586998c | -12.0183 | -46.61344 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07360924-f9e7-3737-9153-c971091de271 | -15.07072 | -45.06321 | 2025-09-30 03:49:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15389b31-8bfc-3eba-8884-f19635f8083a | -13.01309 | -44.11871 | 2025-09-30 03:49:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8e55ecee-f525-357e-bd6b-d0ea15fca7dc | -5.82143 | -42.78374 | 2025-09-30 03:49:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| acc8b6b8-63f7-3a7f-a9b3-20518efdb3e4 | -15.59706 | -47.82764 | 2025-09-30 03:49:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4cc9f5f8-df96-33a0-8af0-9f7b45472dc0 | -19.32277 | -43.79996 | 2025-09-30 03:49:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a6aa574-df31-3b3f-8971-778f8b6e8459 | -13.80804 | -47.48502 | 2025-09-30 03:49:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08077005-c743-3215-beb2-d916effc0cb9 | -11.99471 | -46.59889 | 2025-09-30 03:49:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9738aa39-8752-328c-8ba4-17d345af8ad2 | -12.58596 | -41.29176 | 2025-09-30 03:49:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README32.md)
