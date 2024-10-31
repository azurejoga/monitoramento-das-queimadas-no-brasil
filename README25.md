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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0194c72-0964-3add-a0d4-9ed3eb657e90 | -5.01873 | -46.7608 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20565ff0-de11-3ee7-be14-30d74a69a989 | -5.00687 | -46.46859 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4b1a2d4-aaee-3eaf-a687-741f31ac25ec | -4.99021 | -46.46601 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b635e5b9-2923-3644-a42f-0ad42586cd78 | -4.98966 | -46.4695 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ae1202c9-c275-3ab1-94dc-01e165e8e9fb | -4.87773 | -46.70625 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4239c875-2411-331a-b04a-5b158f6c8d1d | -4.7995 | -46.47506 | 2024-10-31 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f4c423b-6247-3e6d-b32a-61b70a1ed861 | -4.79616 | -46.47454 | 2024-10-31 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd93186c-1919-3e28-9235-228b070983a8 | -4.77226 | -46.41003 | 2024-10-31 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4d0760d-b3ed-38c4-92bf-d47dcf69d7fe | -4.76893 | -46.40952 | 2024-10-31 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90454a4b-ba08-3ab3-a1ae-3043a47dc297 | -4.75399 | -46.56799 | 2024-10-31 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf2c2e19-1253-3f23-81e8-d61dc2063476 | -4.75343 | -46.57148 | 2024-10-31 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c84d25f-849b-358d-a317-76d977aae08f | -4.7501 | -46.57096 | 2024-10-31 04:25:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dcc45566-e10c-3e9b-9ed6-91217c04f896 | -4.67141 | -46.44778 | 2024-10-31 04:25:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 06c31869-863e-3567-9351-981b4d627f4b | -5.93042 | -46.70377 | 2024-10-31 04:25:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4bffb206-5713-3e29-8346-b460af1fba96 | -5.10612 | -47.16265 | 2024-10-31 04:25:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03b581c7-c595-3bba-a3ca-3cb3e79493e0 | -6.04963 | -46.93799 | 2024-10-31 04:25:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 726e4908-7aa0-30ed-9404-0bd0105e649e | -5.74133 | -46.65931 | 2024-10-31 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7af39c4c-3d36-3ac9-a2d9-ad858ef9839a | -7.66816 | -47.33268 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 319a4944-c486-3740-bace-7c9ef146848a | -7.66651 | -47.32157 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9f79ffba-ca07-361b-8cbc-e6e1ed0d8e30 | -7.66595 | -47.3251 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d80ba83-dd99-3b55-9622-2a23f2641d95 | -7.66482 | -47.33215 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40f5fa7e-b8e4-3f68-8ddd-ba9d22f41620 | -7.58769 | -47.11432 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb19cce2-d721-3257-8fe1-93e83f70625b | -7.46829 | -47.18493 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43df03b6-7d3d-39a6-b07f-0b0be38ea265 | -7.42246 | -47.11291 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 062d923f-4a66-3373-8e96-f5ae959b3a9a | -7.41912 | -47.11237 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d931cca8-aea8-3c84-95ba-3cea700209bf | -6.97958 | -47.02423 | 2024-10-31 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 423ea0bf-df15-35d7-b43a-0fd53dada690 | -6.69238 | -47.22033 | 2024-10-31 04:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 804b9df7-f9d9-3bdb-a314-e1ea6c16d1b9 | -7.43692 | -46.93577 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e77bc76-6033-3319-bc13-2e5b44f45a66 | -7.66872 | -47.32916 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ddb8325d-6053-3533-8823-62c8349f4225 | -7.66707 | -47.31804 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6543232f-ea27-3f96-9cc4-bd2260827b86 | -7.66538 | -47.32862 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b09c3c3e-131e-3c0f-a157-2bc8fb4c18a6 | -7.66425 | -47.33567 | 2024-10-31 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad813a78-c3fc-31ed-8b60-c0aa3ab134b3 | -7.66147 | -47.33161 | 2024-10-31 04:25:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b7a27f7-9b0e-30dc-9275-a7b3c3505f15 | -7.58436 | -47.11379 | 2024-10-31 04:25:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 23c34bfe-d478-3241-aaf0-5ac2ab701b06 | -7.48946 | -47.15948 | 2024-10-31 04:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7b0c71f-8aea-326b-8cf4-4605cc2e8939 | -7.1562 | -48.32161 | 2024-10-31 04:25:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77ed7895-544a-36e5-8e89-8bd3a11a6017 | -7.1556 | -48.32534 | 2024-10-31 04:25:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d419226-6bb3-3009-9804-ecdbb188bd9d | -4.92971 | -49.15125 | 2024-10-31 04:25:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00a3d314-4417-3364-b439-321c9c8d3af5 | -4.46869 | -48.11371 | 2024-10-31 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8e0eff2f-8536-3e24-81cc-d7eb6529d3b2 | -5.71096 | -49.30652 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e23bc59-9442-3a3b-bc02-77188439fd1e | -5.71028 | -49.31076 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccb388d7-0694-3396-b3e9-77ff7238e28b | -5.7101 | -49.30893 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 479172f6-cd5d-3632-acc2-68d3e5cf0ded | -5.70961 | -49.31499 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc519cf7-64af-333f-b125-6ea09dccdb96 | -5.70893 | -49.31923 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1f0de82-8c07-3d29-ab48-24833942dc6a | -5.70869 | -49.31738 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3168b60f-ce86-31c8-9d4b-61cba8f7f6ab | -5.70799 | -49.32162 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d13cde45-fe39-374a-b1b0-2b019db654e2 | -5.7046 | -49.32287 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2da3c2ea-61f3-3580-8a5d-bdfb2b8d22ac | -5.70434 | -49.32103 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a75714b4-87a0-30a6-a3df-e1fb9eb17260 | -5.69477 | -49.2909 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3eed0f71-52b8-39a9-9977-822560816de4 | -5.60687 | -49.43874 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06680413-a00f-3f7b-9363-725aed14fdcb | -5.6032 | -49.4381 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f57ea7f-a75f-3b2a-9a75-6a4f3648bbd6 | -5.5242 | -49.48897 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae3d1668-bba7-3944-9253-1fc5fe1dcd22 | -5.5205 | -49.48837 | 2024-10-31 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b978ed70-bf75-3a35-a377-73568918e830 | -6.99685 | -48.63967 | 2024-10-31 04:25:00 | NPP-375D | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cd8fab6-d74e-367a-88d4-52f2dcee5160 | -4.78368 | -49.62487 | 2024-10-31 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 44864d1a-9a66-30e9-a340-6a3f8d9075ef | -4.78331 | -49.62641 | 2024-10-31 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b3bcfcbd-0c3a-3ec5-beae-43f18e315abd | -4.77955 | -49.62582 | 2024-10-31 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 616600c7-53e3-3469-9b63-24d8a2cc5d0b | -4.01985 | -54.80057 | 2024-10-31 04:25:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3be22b0-1b31-37e9-a7c5-c4ff5d54b893 | -3.49495 | -55.41627 | 2024-10-31 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d648ab00-c804-317b-b94e-8b17971c2371 | -3.5012 | -55.41348 | 2024-10-31 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8de552d7-3783-34eb-8816-96a99ccf97f7 | -3.50058 | -55.41725 | 2024-10-31 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb5929cb-09f2-3e7c-ac85-69240f2a4dd1 | -3.49809 | -55.41608 | 2024-10-31 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c68b382f-a376-3026-9b88-1c7b55f00ca0 | -3.91418 | -55.4544 | 2024-10-31 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61afda3e-9568-386a-82db-8030d93cfd65 | -3.91072 | -55.45428 | 2024-10-31 04:25:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a1cf311-306e-320a-bd7d-c9d1543f9293 | -2.8431 | -46.6871 | 2024-10-31 04:25:22 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| a0a53343-fe64-3c98-aed4-d9a6157aab74 | -3.242 | -53.2751 | 2024-10-31 04:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 82ad4d26-ef73-3474-bdfa-519028ab8ef4 | -4.8178 | -45.8429 | 2024-10-31 04:25:33 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6744befc-81ee-3e99-955b-774a44d16be2 | -5.0464 | -45.1768 | 2024-10-31 04:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e88dc024-f862-3013-9760-ffa7e52933b4 | -5.0466 | -45.1542 | 2024-10-31 04:25:34 | GOES-16 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 6fdda627-961b-3d3d-a4f3-9cb855753146 | -6.1229 | -43.9578 | 2024-10-31 04:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| e8f1ca2e-93b9-3f55-996a-d52a7ad9f90b | -6.1416 | -43.9563 | 2024-10-31 04:25:40 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4d8de3ad-99fc-3e81-9b73-9afff92c9d7d | -19.5087 | -56.5779 | 2024-10-31 04:26:55 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| e7e13b47-c0db-3f45-a813-e559c0589a3a | -19.52178 | -44.26075 | 2024-10-31 04:27:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffc159fd-10e0-3c25-a27c-f9cb2b96ce9d | -20.29619 | -44.30536 | 2024-10-31 04:27:00 | NPP-375D | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8464e8d0-5e2a-33d1-8c1d-65e6b33f7e43 | -20.29558 | -44.3043 | 2024-10-31 04:27:00 | NPP-375D | RIO MANSO | MINAS GERAIS | Brasil | 3155306 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f061b3da-126b-31be-9bed-3186f379e464 | -17.31007 | -44.9291 | 2024-10-31 04:27:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2104f6a-68b8-32ad-b39e-9ae8e557eb55 | -19.68108 | -45.89998 | 2024-10-31 04:27:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e64dbf5-4075-33bc-a764-123093893272 | -17.2904 | -46.30101 | 2024-10-31 04:27:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 710c4d50-6a23-3ac5-b097-ba0aeb0c24da | -19.97902 | -47.29121 | 2024-10-31 04:27:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57cd5fbc-9699-39aa-a29b-92056195fdd2 | -19.78195 | -47.5403 | 2024-10-31 04:27:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6e6c55e-4f61-308f-b817-79524ebc1055 | -19.45496 | -48.61769 | 2024-10-31 04:27:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2811be4a-4503-30dc-b9fd-520ee5be912f | -19.45163 | -48.61712 | 2024-10-31 04:27:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5597b77-e47d-3aba-b711-293f27671c28 | -19.5271 | -49.638 | 2024-10-31 04:27:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39ed2987-00f1-3b69-9d2d-5424055583fc | -19.52651 | -49.64167 | 2024-10-31 04:27:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5e49c240-d99a-302b-928a-6566dd87b395 | -17.35871 | -52.00883 | 2024-10-31 04:27:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3bd01b2-faf1-3b4e-b633-a52231114897 | -16.33825 | -53.35261 | 2024-10-31 04:27:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 330c3dbc-af06-3461-a822-44244d76b7e5 | -17.57029 | -52.40044 | 2024-10-31 04:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec571db7-7959-3637-ba9b-bfce09c86689 | -17.56948 | -52.40498 | 2024-10-31 04:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a69d925-5530-3a78-889c-063813f31364 | -17.56661 | -52.39973 | 2024-10-31 04:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 210c9547-4d19-3302-abbd-407610310235 | -17.56581 | -52.40427 | 2024-10-31 04:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 56e0fc41-8c9b-3659-bd84-a97fb82a1a63 | -17.99983 | -54.44685 | 2024-10-31 04:27:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6f26c9a4-489f-3c5b-a770-1fc5cda5bda5 | -16.97668 | -54.81575 | 2024-10-31 04:27:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5346e0b3-442f-3939-95ff-13b75a46e6b5 | -16.97589 | -54.81997 | 2024-10-31 04:27:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fe244b3-cfd7-359e-aafa-f0479eefa5c3 | -16.97241 | -54.81481 | 2024-10-31 04:27:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 41c8fc1b-072b-399e-9c4b-e56998f85f07 | -16.97162 | -54.81907 | 2024-10-31 04:27:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 532c9e11-e007-35be-9062-ead7963b83eb | -16.96735 | -54.81812 | 2024-10-31 04:27:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b49eb8f4-9575-394c-a7b3-d7b4d6102a6a | -16.96072 | -54.82989 | 2024-10-31 04:27:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e9f4b62e-74c8-3ac6-8b47-8dc3c6f027c9 | -16.5572 | -56.23218 | 2024-10-31 04:27:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 46f55449-dce6-3a66-b501-816ae0334b24 | -16.55618 | -56.2374 | 2024-10-31 04:27:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 6df57fe4-6e2a-3cb3-b95e-0ad955c3cb7c | -16.55146 | -56.2364 | 2024-10-31 04:27:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |


[Clique aqui para ver as próximas entradas](README26.md)
