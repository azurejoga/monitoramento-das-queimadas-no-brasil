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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b07941f3-8b2c-3d27-9edc-e2309865869d | -16.1859 | -58.4215 | 2024-10-01 01:16:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.5 |
| cd8cba18-999d-37f8-aee7-413b7ce06245 | -16.6459 | -55.1908 | 2024-10-01 01:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 91.5 |
| 046661b1-de28-35e3-8ec6-0d54e93c278c | -16.6455 | -55.2117 | 2024-10-01 01:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 81.8 |
| c9883e4a-fd41-3def-89d6-e6062f7f496d | -16.6263 | -55.1934 | 2024-10-01 01:16:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 95.9 |
| bff31dc7-77f3-36ee-b741-cc1d46720ca7 | -16.8103 | -55.8762 | 2024-10-01 01:16:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 69.4 |
| 0ca44f31-f068-3a01-90ab-1d16abc26daf | -16.898 | -57.7153 | 2024-10-01 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.5 |
| 905ebe86-af01-3e57-85e2-d61489b1f99b | -16.8787 | -57.6971 | 2024-10-01 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.3 |
| e32c864f-53e5-39cd-85ad-8f95f21b8dfb | -16.8784 | -57.7175 | 2024-10-01 01:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 81ba8c1f-ba7b-3cd5-b3da-0fb5040c4d1c | -17.0898 | -56.7297 | 2024-10-01 01:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.6 |
| 5d8f8977-01b4-3d96-9c7d-6a9334a25f55 | -18.543 | -43.4436 | 2024-10-01 01:16:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.9 |
| 77822649-bee5-3cba-85eb-55fd4286a4db | -18.5423 | -43.4683 | 2024-10-01 01:16:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.4 |
| 6e026e3c-c241-3687-8365-8c8eabc99df8 | -18.6011 | -53.0412 | 2024-10-01 01:16:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 78.1 |
| dcd476c5-7380-34ce-93f3-94347f3b3ed0 | -18.7172 | -57.3305 | 2024-10-01 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 908fc974-c6d4-3e38-8541-3b88233ae98f | -18.9253 | -47.0305 | 2024-10-01 01:16:51 | GOES-16 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 61.2 |
| b80f094e-5ff6-3431-b1b9-510264f98892 | -18.6977 | -57.3123 | 2024-10-01 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.2 |
| 32f22a7c-0245-3efd-807f-a61c5d9adb6e | -18.6973 | -57.333 | 2024-10-01 01:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| 412143ee-70a5-3f94-97e9-aa1c84abea0c | -19.1329 | -57.4628 | 2024-10-01 01:16:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.9 |
| aea0d9a9-a6e0-3488-9608-82a5a14dcc3e | -19.1325 | -57.4836 | 2024-10-01 01:16:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 65d28138-c3bc-33f6-8718-547ea5f22f5d | -20.5266 | -46.2783 | 2024-10-01 01:16:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 3096803c-6b75-3ec5-ae2c-6d092a9ff752 | -20.5259 | -46.3023 | 2024-10-01 01:16:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 38d75e6e-b46d-31d4-a213-454ff756672b | -20.6393 | -48.7549 | 2024-10-01 01:17:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| 333809e2-fa1e-35ad-92a1-29a9aac83d98 | -21.7122 | -54.8253 | 2024-10-01 01:17:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 986e1415-9b7a-3834-b6c9-1a97b5fe32ce | -21.7117 | -54.847 | 2024-10-01 01:17:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 92e755da-bd39-323b-a45a-87fe0a41f209 | -21.6917 | -54.8288 | 2024-10-01 01:17:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 42134b58-dd67-3549-bd7d-7e7a8ffc1685 | -21.6912 | -54.8506 | 2024-10-01 01:17:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 127.4 |
| ecbd6182-80e8-3283-aae4-d8232d0fb1d3 | -22.3922 | -49.2961 | 2024-10-01 01:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| c4a6de42-c1dc-3ec2-b45a-8b69aa6b68cb | -22.3916 | -49.3194 | 2024-10-01 01:17:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.7 |
| c544fb6a-35b5-3bca-bce3-45940c69f5f8 | -22.3713 | -49.3011 | 2024-10-01 01:17:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 155.1 |
| ce1e78cf-4cfb-30b5-b673-1f358a96f3d5 | -22.3707 | -49.3244 | 2024-10-01 01:17:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.7 |
| 0eea01ef-0193-30d2-9ff3-52e70240ab16 | -23.0793 | -45.3951 | 2024-10-01 01:17:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.9 |
| 2d005829-8f12-30ce-be80-c255a198e5df | -3.0282 | -51.3345 | 2024-10-01 01:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 0f3f9aa4-9e70-35d5-a6ff-c965f3e42407 | -5.9786 | -45.3847 | 2024-10-01 01:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 8980532f-0334-3324-82eb-dbfe8cd6f7da | -5.9788 | -45.3621 | 2024-10-01 01:25:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 94dcf472-03e3-3c25-bea1-3e5caea491fe | -6.9671 | -47.6215 | 2024-10-01 01:25:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| f928ee12-a570-33ed-8cdc-97240e46a72c | -6.9858 | -47.6201 | 2024-10-01 01:25:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d493bea3-2b37-34b2-b967-3b056d5caeed | -7.583 | -46.0407 | 2024-10-01 01:25:49 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a5224b22-8456-352c-86ca-40e674ad27b6 | -9.5721 | -40.3475 | 2024-10-01 01:25:59 | GOES-16 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.2 |
| 4b37cd3e-68c4-3f16-8059-3da0e8ad1e73 | -10.5743 | -48.0399 | 2024-10-01 01:26:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 358a3e66-2995-37e6-8686-e061a876b4b3 | -10.9429 | -50.0833 | 2024-10-01 01:26:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 5b9b7dc5-3c35-3dea-aeaf-4fd0192e29d4 | -11.6367 | -64.9999 | 2024-10-01 01:26:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| e158d698-6edf-3952-a220-545133ffda00 | -11.6554 | -65.018 | 2024-10-01 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| eea0bed0-c0c4-3ab3-a443-ada44fda5ba6 | -11.6555 | -64.9991 | 2024-10-01 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 288.4 |
| de62e27b-9449-33b5-8249-e7b75734c543 | -11.6556 | -64.9802 | 2024-10-01 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 6206e69b-576a-31cc-a06e-b2d8ad7db3d3 | -11.6743 | -64.9983 | 2024-10-01 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 684edbc1-c465-37ce-a7b6-a1c83661911b | -11.6744 | -64.9793 | 2024-10-01 01:26:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 103.6 |
| cbd16b9a-187f-3209-a35d-aaffc3f61a5c | -12.6039 | -53.4879 | 2024-10-01 01:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 1fa382dd-aecf-3ecc-bacc-aa5b4a91054f | -12.9605 | -51.345 | 2024-10-01 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 6405b846-598f-392e-997d-d7d43da1ed38 | -12.9793 | -51.364 | 2024-10-01 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 187.9 |
| e240af87-dd57-371f-b466-1dfde04fac1e | -12.9796 | -51.3427 | 2024-10-01 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 207.9 |
| ce7b5909-4b84-397d-afa4-ea92f1f62f2a | -12.9985 | -51.3617 | 2024-10-01 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 63224633-3587-3206-9ab1-a8c84855d351 | -12.9988 | -51.3403 | 2024-10-01 01:26:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 4cfbc253-83e1-3dc3-b61e-cc32bb8805ca | -13.2493 | -51.2452 | 2024-10-01 01:26:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e471362f-9441-3b66-a480-0a6ac5f0640f | -13.5391 | -51.1228 | 2024-10-01 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| b7949c82-be2f-3e6c-b04f-8053311fc82f | -13.5765 | -51.1821 | 2024-10-01 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| f260b7a2-31e4-3a48-9f47-d9ac727c9173 | -13.5768 | -51.1607 | 2024-10-01 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| ab50fbbe-468f-3473-9b7d-ffd1fa4d150d | -13.5957 | -51.1796 | 2024-10-01 01:26:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 1edda41c-cb24-35c4-b938-fb2472388715 | -14.7211 | -48.7529 | 2024-10-01 01:26:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 4f881e84-d48e-37a9-bd6b-c6430a1fcd31 | -14.7402 | -48.7721 | 2024-10-01 01:26:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 624ccaa5-5a9c-3b01-94ba-122bdae52bd0 | -14.7406 | -48.7498 | 2024-10-01 01:26:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 129.8 |
| e41c11cc-84c3-3f61-a4c9-c0abe84b01bb | -16.1859 | -58.4215 | 2024-10-01 01:26:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.3 |
| d260bb96-59aa-3f7d-8648-5d4014838080 | -16.6263 | -55.1934 | 2024-10-01 01:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| bee61bd4-f9c2-399e-8c6e-4bf5d1ec3ab9 | -16.6459 | -55.1908 | 2024-10-01 01:26:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| b94454f2-e945-3f13-bb34-ba9c3d33a5ad | -16.7525 | -55.8213 | 2024-10-01 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 67.7 |
| 8342bfaf-df95-30f6-b83d-324d7512e1da | -16.7528 | -55.8005 | 2024-10-01 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.6 |
| 5cd9689d-f4cb-38a0-858e-879462f40909 | -16.7532 | -55.7797 | 2024-10-01 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.3 |
| 0d9f8174-d181-3703-8b15-488d4e261119 | -16.7721 | -55.8188 | 2024-10-01 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 72.8 |
| 5cd1b07e-bf65-342a-a761-c84b11c50bb1 | -16.7724 | -55.798 | 2024-10-01 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 114.6 |
| 0746caf4-b8ff-33c7-9f52-c0e7b20dcc1b | -16.7728 | -55.7773 | 2024-10-01 01:26:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 9c7bfeec-de26-3a76-bde2-360c4481020b | -16.8784 | -57.7175 | 2024-10-01 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.0 |
| 832c582b-f83c-3f56-845c-3992b0757bb1 | -16.8787 | -57.6971 | 2024-10-01 01:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 757640d7-bf23-3321-bb62-c379a42d9279 | -17.0705 | -56.7114 | 2024-10-01 01:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 47.5 |
| 17334143-c094-36eb-b653-c2bacd74acb2 | -18.5423 | -43.4683 | 2024-10-01 01:26:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 143.0 |
| 68ae6047-0d47-3033-88ce-881fdddd17c8 | -18.543 | -43.4436 | 2024-10-01 01:26:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.4 |
| 7e2e33ea-aecd-3208-8f21-2c3bb8c9aadc | -18.6011 | -53.0412 | 2024-10-01 01:26:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 17712790-e6dc-3e0a-b1f5-0251dfe75ea8 | -18.6973 | -57.333 | 2024-10-01 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 170.0 |
| 4bb0245a-57b8-30b3-bb8a-a802e5d95103 | -18.6977 | -57.3123 | 2024-10-01 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.5 |
| d5689ca2-6f54-3d15-9930-31f225de8919 | -18.9253 | -47.0305 | 2024-10-01 01:26:51 | GOES-16 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 9a6cf4de-ff78-3177-bea4-ccfcea1841b4 | -18.7172 | -57.3305 | 2024-10-01 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 56.1 |
| bf237e62-e495-39a6-aed0-a0ed161be98a | -18.7176 | -57.3097 | 2024-10-01 01:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.4 |
| 683bd493-3205-35bd-bd36-ef24c61c7549 | -19.1329 | -57.4628 | 2024-10-01 01:26:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.0 |
| 0a974bc1-8782-3db5-a5de-b30aed122ba2 | -20.0218 | -55.998 | 2024-10-01 01:26:57 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 6d7f330e-5c01-3fed-9d94-2f5363869235 | -20.5259 | -46.3023 | 2024-10-01 01:26:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 84.1 |
| cc1d87c4-b75c-3801-96ba-659b01360d34 | -20.5266 | -46.2783 | 2024-10-01 01:26:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 77.7 |
| e915ad51-7a21-35a3-b671-9ece5bf1a49b | -20.6194 | -48.7364 | 2024-10-01 01:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 144.5 |
| be5d4a37-7e8c-3307-96e6-9158aa29c9a4 | -20.6188 | -48.7595 | 2024-10-01 01:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 307.4 |
| d1b7a39d-8602-3a9d-8d04-bbb41b98728a | -20.6393 | -48.7549 | 2024-10-01 01:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 273.7 |
| f1ba5e7d-7271-3401-bc30-1b75c649eb94 | -20.6399 | -48.7318 | 2024-10-01 01:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 129.3 |
| 7015fb85-1800-3a10-8b4e-1ad88f82814a | -22.3707 | -49.3244 | 2024-10-01 01:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 244.2 |
| c3d0c493-85c3-374e-ad63-e6cee32bad0f | -22.3713 | -49.3011 | 2024-10-01 01:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 186.1 |
| aabdc565-25eb-3dc3-ac77-13c2e3a77fda | -3.0282 | -51.3345 | 2024-10-01 01:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6ed59c91-1329-3e65-abd2-ede6f28f3632 | -5.9788 | -45.3621 | 2024-10-01 01:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 737617b8-0513-3d8b-bc2e-46e834e193ab | -5.9786 | -45.3847 | 2024-10-01 01:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 3d73be90-f493-393f-9ae2-3b0aea1e3126 | -6.2524 | -44.132 | 2024-10-01 01:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 53c0e8d5-e058-32c8-9d14-b13d8831bb85 | -6.9858 | -47.6201 | 2024-10-01 01:35:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 10dbda08-b67f-389d-bd08-50a7cd8aa93e | -10.5743 | -48.0399 | 2024-10-01 01:36:05 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 21408115-6b50-3d13-9d94-7a0a5c76fed2 | -10.9429 | -50.0833 | 2024-10-01 01:36:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 685fcf78-9aca-3d9e-b375-5dca6257f25e | -10.924 | -50.0854 | 2024-10-01 01:36:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| ba4b2ad8-6a51-34b9-9a7f-a156c279f8d8 | -12.6039 | -53.4879 | 2024-10-01 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 8864e914-ecb3-3f11-941f-8b3312f41c4a | -12.4942 | -53.167 | 2024-10-01 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| b566f3ee-3f28-384f-ba94-9c9a85affedc | -12.4939 | -53.1879 | 2024-10-01 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |


[Clique aqui para ver as próximas entradas](README24.md)
