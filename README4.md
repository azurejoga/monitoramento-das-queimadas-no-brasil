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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92bc8336-7be4-322e-9db4-9e181df103b6 | -17.0609 | -56.1138 | 2024-10-01 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 52.2 |
| 8b6809b7-b37e-3751-9c89-f065d81ecb80 | -18.6011 | -53.0412 | 2024-10-01 00:26:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 41046b27-206e-333d-aa29-e8e383e3fd13 | -18.6006 | -53.0628 | 2024-10-01 00:26:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 58da9c06-9a5b-3537-8d3b-e52403f74076 | -18.9091 | -49.2129 | 2024-10-01 00:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.5 |
| 0fb6d00d-786a-3803-bd9d-36237a2a939c | -18.9287 | -49.2316 | 2024-10-01 00:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 99.7 |
| 25f2c32e-b3aa-3adb-bb1b-cfb4bfebe3f8 | -18.9292 | -49.2089 | 2024-10-01 00:26:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 122.6 |
| 1ce26b52-0835-39e9-878c-65a5a814b42f | -19.1129 | -57.4655 | 2024-10-01 00:26:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.6 |
| f8016b6e-7a3c-3330-a53d-ee81ade39c37 | -19.1329 | -57.4628 | 2024-10-01 00:26:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 6e01b5bd-bb95-3df1-b36c-40147431426e | -20.8123 | -53.1364 | 2024-10-01 00:27:01 | GOES-16 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 2bb15b5c-8991-3905-bd7a-249b37044ce1 | -21.6912 | -54.8506 | 2024-10-01 00:27:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 90.9 |
| f0c32102-aa3b-364b-8e8b-dfc62df089f6 | -21.6917 | -54.8288 | 2024-10-01 00:27:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 3a532dbd-29c7-3f32-91f1-bb04947af4c1 | -22.1242 | -48.5469 | 2024-10-01 00:27:07 | GOES-16 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f0aaa795-35a5-3e08-982a-ab692499c151 | -22.3707 | -49.3244 | 2024-10-01 00:27:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.8 |
| c0f80084-9967-38fb-b67f-9d962da4b89c | -22.3713 | -49.3011 | 2024-10-01 00:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 183.6 |
| 3e01ace9-a53f-3028-84c0-34d76ff83f97 | -22.3922 | -49.2961 | 2024-10-01 00:27:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 67.4 |
| 7056ced8-89c8-3901-b037-0df070e58676 | -23.0793 | -45.3951 | 2024-10-01 00:27:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| ea875fdc-3baf-32e7-aecd-8139ef0ffa0d | -2.4048 | -50.3085 | 2024-10-01 00:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| e728581b-33af-3bbf-bd8f-eb9f91a19a24 | -2.3863 | -50.3299 | 2024-10-01 00:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 3fa82134-c81a-3f03-bade-12a4f46ad0b2 | -2.4046 | -50.3505 | 2024-10-01 00:35:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 5000df6a-49db-31b9-82fb-695ddb4f354e | -2.4047 | -50.3295 | 2024-10-01 00:35:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 217.9 |
| e209c8f8-38a3-3394-8782-4c6f2c512965 | -3.8166 | -52.3608 | 2024-10-01 00:35:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| a1496136-c621-348b-be75-e64671422186 | -4.6987 | -49.8062 | 2024-10-01 00:35:32 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6df8b454-eb16-35b8-b808-71f17af328b2 | -4.7172 | -49.8053 | 2024-10-01 00:35:33 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 540eaeb9-4ca3-3c05-b2d3-a89efea1c1c2 | -5.7448 | -44.3322 | 2024-10-01 00:35:38 | GOES-16 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f1b9fe26-2195-39a6-a9f7-9bbc3bd5c6cb | -5.7715 | -45.5574 | 2024-10-01 00:35:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 62849edb-458c-3c01-b2e4-7a48202f2fd6 | -5.9786 | -45.3847 | 2024-10-01 00:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 7a33b0c5-5de2-314c-8220-52fee7130b95 | -5.9788 | -45.3621 | 2024-10-01 00:35:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 345c2e1f-06a6-3d99-9e83-ab9ebce3bfd3 | -6.2522 | -44.155 | 2024-10-01 00:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 8d24257d-5733-32ac-aaa1-cf5dcd96007a | -6.2524 | -44.132 | 2024-10-01 00:35:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| a596951c-f1f5-367b-8336-5c145e9142d0 | -6.6953 | -43.0474 | 2024-10-01 00:35:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| b580daa8-9e62-34af-a2ba-d0d3e46a9597 | -6.9673 | -47.5996 | 2024-10-01 00:35:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 54a3472c-de2c-37fc-8618-2abd7eab412a | -6.9858 | -47.6201 | 2024-10-01 00:35:45 | GOES-16 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| bf25e5cb-b668-37b2-85ad-a139f49bb6c9 | -6.9671 | -47.6215 | 2024-10-01 00:35:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 690c8d87-190e-375c-b53f-a93a52ef480a | -7.583 | -46.0407 | 2024-10-01 00:35:49 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 92513b35-20be-3cb9-85a6-34df0f739531 | -8.4643 | -62.7124 | 2024-10-01 00:35:54 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 6c397644-edfb-3d5c-a8ab-4037619aa1d3 | -8.4828 | -62.7116 | 2024-10-01 00:35:55 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| cdd2e553-bcd6-361e-9312-acc4d32df1ad | -10.924 | -50.0854 | 2024-10-01 00:36:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| a5b3dec9-9363-38ca-9df1-ebdbd8f1082b | -10.9429 | -50.0833 | 2024-10-01 00:36:08 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 13f8e75f-f032-3f33-966e-6e3d6dd19d36 | -12.4942 | -53.167 | 2024-10-01 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 6f161c8f-0131-3ee5-bb8c-7e69af849f41 | -12.4945 | -53.1462 | 2024-10-01 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 1ce5913c-17bb-3fe8-96a0-00fca35c2f3b | -12.5132 | -53.165 | 2024-10-01 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| bf406b05-b8f2-3737-aa41-603210775aaa | -12.5135 | -53.1441 | 2024-10-01 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| b3d288b1-b513-325f-9b3a-f9c928aa5aed | -12.5848 | -53.4899 | 2024-10-01 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.6 |
| f778c400-7d9e-352c-be0f-645c2508be0e | -12.6039 | -53.4879 | 2024-10-01 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 177.3 |
| 70a9ba8e-a963-3c5b-989c-a3d7bc8551be | -12.6036 | -53.5087 | 2024-10-01 00:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 4f5708f8-8508-3528-aeb2-f01227af3d00 | -13.2493 | -51.2452 | 2024-10-01 00:36:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 7ae6d17f-19d5-3e91-89df-aef134983b98 | -14.7211 | -48.7529 | 2024-10-01 00:36:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b04f395b-32f7-3224-ad37-6268435dfa87 | -14.7406 | -48.7498 | 2024-10-01 00:36:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 25052297-77c0-3f79-a0b0-0333c043e309 | -15.6179 | -57.4491 | 2024-10-01 00:36:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ac02334a-c9dc-3078-a882-4106f5188f70 | -15.6372 | -57.447 | 2024-10-01 00:36:34 | GOES-16 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ddeaac76-6e6c-33ec-ac7e-e8137305b1ab | -16.6259 | -55.2142 | 2024-10-01 00:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 138.1 |
| 19b49db4-509c-35f9-98a4-b7ae21883209 | -16.6455 | -55.2117 | 2024-10-01 00:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 130.2 |
| fa95e963-0380-3d46-80a6-1acb1a8a7b26 | -16.6067 | -55.1959 | 2024-10-01 00:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 92.6 |
| ff9a410d-a19c-35ab-810d-e07e3e48113a | -16.5134 | -57.3305 | 2024-10-01 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.0 |
| 4c3eeed8-cdd1-384e-a0d3-f511923d3f4f | -16.5131 | -57.3509 | 2024-10-01 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.6 |
| 8c9a1efc-151b-3e4f-b68e-a91b9535679a | -16.4939 | -57.3327 | 2024-10-01 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 150.9 |
| 2b1f1849-5c45-3012-a6bf-cf82064d79df | -16.4935 | -57.3531 | 2024-10-01 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| d2e1dcbb-aac3-3868-995a-c4b34576cb46 | -16.4743 | -57.3349 | 2024-10-01 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.4 |
| 0d0edb92-9982-3f7a-815a-008006148c27 | -16.474 | -57.3553 | 2024-10-01 00:36:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.6 |
| ea455272-a156-3246-b92b-d751a2f4b857 | -16.6459 | -55.1908 | 2024-10-01 00:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 217.0 |
| 8efba383-0c63-3128-bde2-7ed6537b7494 | -16.6267 | -55.1725 | 2024-10-01 00:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| a2e5324c-157a-31c4-b996-53abf8a2770d | -16.6263 | -55.1934 | 2024-10-01 00:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 364.6 |
| 8c3e40fc-1b54-3fa0-9ee9-11dd6e32a0f6 | -16.7525 | -55.8213 | 2024-10-01 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.2 |
| d84eb56f-f1ee-382a-ad7a-3bcb62ad6661 | -16.7332 | -55.803 | 2024-10-01 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 240f9084-08b0-3f6a-a3df-255276a31679 | -16.8103 | -55.8762 | 2024-10-01 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 85.9 |
| d4bba360-2f78-39aa-a5f0-ad798ade4ee4 | -16.7724 | -55.798 | 2024-10-01 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 107.3 |
| 1d7c091b-dadc-3b40-ab6a-dc0f2458a0ab | -16.7721 | -55.8188 | 2024-10-01 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 68.3 |
| d2a42d58-b983-3a73-8f38-966f74b6c360 | -16.7532 | -55.7797 | 2024-10-01 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 6c4d3546-0820-3e71-9139-6ea6c1cfeb69 | -16.7528 | -55.8005 | 2024-10-01 00:36:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 144.4 |
| 69679373-d7e1-3271-bb99-cc7689426a40 | -16.942 | -56.1908 | 2024-10-01 00:36:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.9 |
| 4754737a-e501-3c38-843b-4e40ca6aec1e | -16.8983 | -57.6949 | 2024-10-01 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 137.2 |
| e37ae3f7-5551-3cc2-b8e4-cb31d72155f4 | -16.898 | -57.7153 | 2024-10-01 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 5e11196d-f2b6-3a4c-b9cb-1b20174c866c | -16.8787 | -57.6971 | 2024-10-01 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| a26856e6-f431-3bb2-9f70-ca9a4f545418 | -16.8784 | -57.7175 | 2024-10-01 00:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.8 |
| 40b32f29-c6c4-36bf-9b3d-e6165a37ca5a | -17.1195 | -56.1271 | 2024-10-01 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.4 |
| 3cef64d0-a282-3e69-bbfd-a6d6f5d7474b | -17.0609 | -56.1138 | 2024-10-01 00:36:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 47.6 |
| 296e7292-99b3-36ea-8a55-fd6ed9c4a039 | -16.9919 | -57.9696 | 2024-10-01 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.2 |
| 067e741c-7038-35b6-a38c-472653d0f419 | -18.6011 | -53.0412 | 2024-10-01 00:36:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 5f27d33c-1707-3d8a-ac9d-58b91bebdc7a | -18.6006 | -53.0628 | 2024-10-01 00:36:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e44508b8-1564-33e5-967a-449c7bc2ad29 | -18.9287 | -49.2316 | 2024-10-01 00:36:51 | GOES-16 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 029a3b4a-b3ed-34c2-95c2-ab17a794aa3b | -19.1329 | -57.4628 | 2024-10-01 00:36:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 113.5 |
| 7a187740-199d-3a31-baa3-13be4eae4a6f | -19.6862 | -47.2326 | 2024-10-01 00:36:55 | GOES-16 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| f0cfdcdd-b102-3ff8-a825-628b89c2da40 | -21.7122 | -54.8253 | 2024-10-01 00:37:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 933d96df-33d1-3b33-b507-f80ae1db5621 | -21.7117 | -54.847 | 2024-10-01 00:37:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 8544bfbc-e12c-3223-9107-39850e317634 | -21.6917 | -54.8288 | 2024-10-01 00:37:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 200.7 |
| 26e5ec96-2179-3aa8-8be9-0dee3aeddb15 | -21.6912 | -54.8506 | 2024-10-01 00:37:06 | GOES-16 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 234.7 |
| 41f1f818-dd18-3d8e-b60a-37ed13f4d733 | -22.3922 | -49.2961 | 2024-10-01 00:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| 71017025-a6e4-389d-b7b8-5d31be80e2c3 | -22.3916 | -49.3194 | 2024-10-01 00:37:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| 42d09f79-3efa-3657-af62-852d7d5179fb | -22.3713 | -49.3011 | 2024-10-01 00:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 143.1 |
| 6d6f2b41-2fb5-3ecf-b1ed-e7aa78f5a0f6 | -22.3707 | -49.3244 | 2024-10-01 00:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.7 |
| f7e2d72f-aa73-3288-93f2-d6c76c0b0dc6 | -22.61872 | -42.17552 | 2024-10-01 00:43:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 22.7 |
| a25b147e-6cc7-328d-bac8-c4aed1afc073 | -22.61735 | -42.1659 | 2024-10-01 00:43:00 | TERRA_M-M | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 7020c1e0-7e9f-3ffa-8f68-7959588a7556 | -22.59613 | -44.02598 | 2024-10-01 00:43:00 | TERRA_M-M | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b8626c10-a6bf-34d0-9c7c-93e46af5c900 | -22.5078 | -43.84306 | 2024-10-01 00:43:00 | TERRA_M-M | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 7c6fa9f6-b0bc-3434-85bc-4fc39b9121a6 | -22.50649 | -43.83325 | 2024-10-01 00:43:00 | TERRA_M-M | BARRA DO PIRAÍ | RIO DE JANEIRO | Brasil | 3300308 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 244ceb3a-c41c-3830-ab3c-053e8229726e | -22.49535 | -43.54549 | 2024-10-01 00:43:00 | TERRA_M-M | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 7571d951-1ed0-32ac-8a25-3935f7207aaf | -22.54093 | -44.30706 | 2024-10-01 00:43:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| d084c40c-8d3f-3842-8889-90a897c9e48b | -22.53179 | -44.30847 | 2024-10-01 00:43:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 86fa2365-c87f-3391-a03c-8e9d9fbd9077 | -23.07513 | -45.40627 | 2024-10-01 00:43:00 | TERRA_M-M | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 34.0 |
| f2e993d1-3153-3f1b-9d9c-f2df30f57cd3 | -23.07367 | -45.39443 | 2024-10-01 00:43:00 | TERRA_M-M | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |


[Clique aqui para ver as próximas entradas](README5.md)
