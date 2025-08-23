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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67c9eb9b-68e0-371b-ba1d-2bded0754d9b | -20.44728 | -42.12655 | 2025-08-23 03:17:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| e5649cd0-fb28-3db9-aebe-71f4a952d939 | -21.95271 | -45.59734 | 2025-08-23 03:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 59177a75-2b18-322f-bcd1-4979133b24cd | -22.0959 | -45.02383 | 2025-08-23 03:17:00 | NOAA-21 | SÃO LOURENÇO | MINAS GERAIS | Brasil | 3163706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| afb7fcad-8ef8-3cc8-b11e-d96c3ee1c595 | -22.16996 | -43.28172 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5afc1eab-b3e2-3df4-b6e9-ed291f94f88f | -22.12214 | -41.38083 | 2025-08-23 03:17:00 | NOAA-21 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a069c64e-c07d-3e8d-89e0-dd3dda34c900 | -22.53453 | -43.7232 | 2025-08-23 03:17:00 | NOAA-21 | MENDES | RIO DE JANEIRO | Brasil | 3302809 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| baf53fcf-84c5-37f2-8408-994e869b50ff | -20.86948 | -42.54261 | 2025-08-23 03:17:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 59f3d096-5677-37e4-b60c-ccbbd9664154 | -21.95942 | -45.59996 | 2025-08-23 03:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| b09febb5-67f8-3542-9f35-f4949640be2b | -21.96137 | -45.59241 | 2025-08-23 03:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| b085e8f0-1610-31d1-872e-d678548354bd | -20.87163 | -42.54636 | 2025-08-23 03:17:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4d552607-95b4-3266-8eab-a063d7a2ec75 | -22.16381 | -43.28084 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 218d3517-fc92-31c1-b8af-47396bd75f27 | -22.16508 | -43.27548 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 80ae1cd3-4579-3f62-a4ff-0a9336aec29e | -20.86803 | -42.54906 | 2025-08-23 03:17:00 | NOAA-21 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 65e619e5-2b56-35dd-a9a7-add121727325 | -23.50097 | -46.00393 | 2025-08-23 03:17:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 52037b8b-4ec1-3256-9bb2-ba34ddda7f9b | -20.44291 | -42.11885 | 2025-08-23 03:17:00 | NOAA-21 | LUISBURGO | MINAS GERAIS | Brasil | 3138674 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| b93dd3b6-e532-3ee5-8e30-6b14b9d0f6c2 | -19.67976 | -43.87135 | 2025-08-23 03:17:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a7df8c57-498c-33b7-8f78-57c55a64a2e9 | -20.39339 | -45.454 | 2025-08-23 03:17:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 483fbd4b-b505-3752-bf02-9cc0b0199c1d | -22.90003 | -46.39193 | 2025-08-23 03:17:00 | NOAA-21 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| e9beac6f-7558-3952-818a-932a8ef4d11a | -21.95946 | -45.59942 | 2025-08-23 03:17:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| a464f12b-f797-3a81-a227-6fd06877127a | -22.17595 | -43.28329 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 071345c2-1fab-3c77-b3fe-221bff64ddf3 | -22.17115 | -43.27668 | 2025-08-23 03:17:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fba53e1c-a76b-3a05-b717-7794ac9d3b2a | -5.9526 | -44.1326 | 2025-08-23 03:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 25507864-63dd-3958-ba29-16ecc0ff1478 | -9.9681 | -60.1743 | 2025-08-23 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 5fa5a0f9-d530-3ba5-94fe-d33b8dc9b563 | -14.7507 | -55.9947 | 2025-08-23 03:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| a2e768d7-ffb9-3f6a-8d46-ca9d8f25404e | -9.1897 | -59.6171 | 2025-08-23 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 0ace2183-eb2c-319c-ba7f-dc0375aef06c | -9.968 | -60.1937 | 2025-08-23 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 62dc9f6f-63d9-3d3a-8671-d896ae784bda | -20.4042 | -45.592 | 2025-08-23 03:20:00 | GOES-19 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 47.4 |
| b7763329-44e3-3de8-9729-b9527c51912c | -17.5979 | -46.5715 | 2025-08-23 03:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b5570618-54e9-3387-a3b5-b6b126547ece | -9.518 | -60.5268 | 2025-08-23 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 509933c1-b22e-3be0-85c5-40d2e1dea8a6 | -7.0352 | -44.6396 | 2025-08-23 03:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| f246bf22-5e26-3bec-80a4-f17546b9cae5 | -17.5985 | -46.5481 | 2025-08-23 03:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 729532da-3f9c-343e-998f-fe7c2c9dca83 | -9.5179 | -60.5461 | 2025-08-23 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| ce3e7ece-7db0-3b0b-aa5d-518b6ca52562 | -17.5785 | -46.5523 | 2025-08-23 03:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b8493e10-e072-3585-aa72-a4118789539f | -14.751 | -55.9742 | 2025-08-23 03:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| bab617fd-fe43-3c55-80ab-b3713e07c21e | -6.6044 | -44.5624 | 2025-08-23 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 0706e7b6-c5b9-30bf-9ab2-79653400185e | -9.5177 | -60.5653 | 2025-08-23 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9da63588-2d14-3f97-8a8f-8fb826cdacf8 | -8.5944 | -62.6126 | 2025-08-23 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 4537837e-a54c-35e1-874b-43722128b404 | -9.9495 | -60.1754 | 2025-08-23 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| 37e66602-c693-3dd9-b085-f955eeb26afc | -9.9493 | -60.1947 | 2025-08-23 03:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 233.7 |
| a5a0a51d-709d-3ced-865c-53b1b8224ad2 | -8.5943 | -62.6315 | 2025-08-23 03:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 22eba15f-89d2-3207-a3f5-43a8611b324d | -9.1895 | -59.6364 | 2025-08-23 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c0abb5cb-0ede-353f-b4fd-773d5637fc77 | -9.9495 | -60.1754 | 2025-08-23 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 1d5ed44f-5cf7-37a4-8c43-a0ce55e52028 | -20.097 | -47.7676 | 2025-08-23 03:30:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 673241a6-16a2-3364-ba13-6d2eb6b69970 | -9.5177 | -60.5653 | 2025-08-23 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d3e3fea2-371f-353b-b170-370f139c29c1 | -8.5944 | -62.6126 | 2025-08-23 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 50fc70c0-44d1-3c7e-b17d-53fec62df387 | -14.6703 | -54.9349 | 2025-08-23 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 443f91fe-970a-3bf3-88b5-2caddddc7229 | -9.5179 | -60.5461 | 2025-08-23 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 8b53e43b-645c-342d-8399-91833c540719 | -8.5943 | -62.6315 | 2025-08-23 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 94660287-8667-3d92-8e0b-9ec6f1c878ba | -9.1897 | -59.6171 | 2025-08-23 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 27ba26e2-7293-3373-a2a4-9dccf7b736b8 | -17.5985 | -46.5481 | 2025-08-23 03:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 51489894-de5e-37f2-afc4-406a8e2b132e | -14.6706 | -54.9142 | 2025-08-23 03:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 72.3 |
| c92c522b-0156-3cd0-b1e1-f38f7d7e8c02 | -9.518 | -60.5268 | 2025-08-23 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e2fba8c9-5bb1-3d5e-baed-a2c64c9cd335 | -9.968 | -60.1937 | 2025-08-23 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 166.7 |
| e68b4175-2ff7-3c50-a592-a9795b178e66 | -17.5785 | -46.5523 | 2025-08-23 03:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 61.1 |
| e782cb27-eaef-364e-9364-aab60138899a | -6.6044 | -44.5624 | 2025-08-23 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 8ed705f9-3683-3b10-9135-87d40ad0bb5b | -8.5758 | -62.6323 | 2025-08-23 03:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 78eb870d-09e4-3789-a161-cab25b92d31c | -9.9681 | -60.1743 | 2025-08-23 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| aafe894c-864b-3aeb-9a0e-679d7656a16b | -17.5979 | -46.5715 | 2025-08-23 03:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 322fc2ba-3248-3b74-8d47-8f5447ba3b5c | -9.9493 | -60.1947 | 2025-08-23 03:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 249.1 |
| 8f7419b3-f909-3b01-89c9-c5e2995a4e0c | -4.3482 | -46.4695 | 2025-08-23 03:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 99a60f08-d628-3511-b57e-4784a48586f6 | -3.55207 | -41.62281 | 2025-08-23 03:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| df543642-a275-3c93-b871-a8233d0fe00f | -3.5463 | -41.62511 | 2025-08-23 03:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3e817018-dd64-3df8-a4d2-4feae0b47105 | -3.55259 | -41.61964 | 2025-08-23 03:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 461ce792-3675-3fec-a63f-8dd2a376b8eb | -3.55782 | -41.62056 | 2025-08-23 03:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b8f85d99-74b0-3abb-ba42-351669618d30 | -3.5573 | -41.62373 | 2025-08-23 03:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d327ca9d-0830-3772-9d0e-c8ae554c64c0 | -3.54682 | -41.62194 | 2025-08-23 03:36:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 524d7819-cb98-35f4-873b-ed9eadd27c4f | -8.01339 | -45.49562 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4cd4332-220a-3958-be4a-724e7272a4b4 | -8.29858 | -47.26091 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55fc057d-0f6a-34f3-82c1-a253b948ab51 | -6.12427 | -44.40987 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cebfcde3-c339-384d-9b32-cff0c052ea52 | -6.4234 | -41.21978 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 8a68bd4e-f458-3073-9c5a-70051d1f2f13 | -6.42824 | -41.22074 | 2025-08-23 03:38:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 710dac24-3a66-3dc1-ac5e-a9aff1e63fff | -7.21476 | -45.31634 | 2025-08-23 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0d0ffdca-1190-3894-881a-8d63c3bc8aa0 | -7.02269 | -44.65464 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 4ab86f36-277c-30fb-98b3-e9fe370a9503 | -6.58511 | -44.57146 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b907847-7bf0-32ca-82d1-494c45de16b5 | -4.53085 | -38.23286 | 2025-08-23 03:38:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d3b506b6-1227-3274-9108-616350b1e16f | -7.4971 | -34.91032 | 2025-08-23 03:38:00 | NPP-375D | CAAPORÃ | PARAÍBA | Brasil | 2503001 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 776038ed-2dd7-33a3-97c3-289cd919a431 | -6.4804 | -43.46164 | 2025-08-23 03:38:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a18a96dc-17de-3c12-b0e7-2e86dc5f29c0 | -6.59172 | -44.57212 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3b15c51-5860-3104-86b7-d8bf6c06bc28 | -7.64591 | -45.24033 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6fd82c74-8c0c-3851-a019-ac346120dca9 | -6.11301 | -44.40335 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eec98bc7-1187-386a-981e-709a99f764d7 | -9.4434 | -47.65527 | 2025-08-23 03:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f107a22e-37d4-3264-aa9d-d0af70686424 | -8.2966 | -47.26768 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6320beb-c2e5-3f54-8108-5b433b7a83d1 | -7.02349 | -44.65017 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 36bd52f5-08fb-381e-9ebb-7c3e75b0307a | -5.90549 | -43.47185 | 2025-08-23 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d93f5163-747a-3237-914d-fd29415ff963 | -7.2117 | -45.31391 | 2025-08-23 03:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5815b036-865e-369e-b4ab-3884c4267a3d | -3.81503 | -41.55995 | 2025-08-23 03:38:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9ddbfbe-32ff-3a02-965a-adb159018170 | -7.64497 | -45.24551 | 2025-08-23 03:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a7e7916e-e66b-35f7-82b7-9e8337bdeef2 | -7.60706 | -44.37602 | 2025-08-23 03:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d59efb1-1559-354e-bcfa-aee39a7388a7 | -6.11901 | -44.40456 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7d4c6f2f-57c2-3c0c-a561-42c429f09f29 | -5.8912 | -43.45287 | 2025-08-23 03:38:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96a89297-a9be-3a36-a88a-a355005d24fc | -6.58489 | -44.57527 | 2025-08-23 03:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce467f3f-a5af-3fe8-a9fb-92644d9d9ad6 | -8.04689 | -47.313 | 2025-08-23 03:38:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75301f0b-774b-3ae6-b6c2-f21e89feef04 | -7.0684 | -44.61339 | 2025-08-23 03:38:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4fc10459-76eb-3515-8ab1-7b56f7c87b11 | -9.31288 | -40.22361 | 2025-08-23 03:38:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cd69776c-65be-32d4-9f5d-ce058aadc8a7 | -4.53145 | -38.2292 | 2025-08-23 03:38:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 928bd67d-1550-34c2-b158-696e8d2b2f3c | -5.49012 | -42.15763 | 2025-08-23 03:38:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 70d003f6-26d8-3c2b-bd12-7ad5df93f3b0 | -3.98319 | -43.24429 | 2025-08-23 03:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 269fa57d-23df-30cc-a492-749d488cd716 | -5.22853 | -37.85658 | 2025-08-23 03:38:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 13bc33ac-d78b-38f3-b8b2-09cf09d6edd3 | -4.52676 | -38.23217 | 2025-08-23 03:38:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4454085e-e4b5-30d9-9504-46d271a62b01 | -9.44749 | -47.66195 | 2025-08-23 03:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README14.md)
