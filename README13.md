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
| 87d965cc-a577-3dea-b1f4-1dd9fd32fb70 | -17.0637 | -56.0005 | 2024-10-13 00:56:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4baf2ae1-b434-3aa0-aa2f-d8278b2c317c | -17.066601 | -56.015598 | 2024-10-13 00:56:36 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a398f2a0-0d7d-334f-9239-4b75cd0dc5fc | -17.1847 | -57.4235 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d36851a-ffe7-384e-a48a-f482a4693299 | -17.188101 | -57.442402 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2afb6c60-c3fd-3247-9844-85e692099a76 | -17.1915 | -57.461399 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b044adf3-6798-312e-b0b6-d229488ffbbd | -17.174999 | -57.4254 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b613e520-8de3-398f-8463-9086f9eafbf8 | -17.1784 | -57.444302 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 400b1b82-c589-3c67-b5d4-561975b7a2fc | -17.181801 | -57.4632 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a7f1e84-b692-3e78-9bf4-fe3f71174dd8 | -17.165199 | -57.4272 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6643117a-f0cb-3d1b-a186-812ebb0e58e2 | -17.1686 | -57.446098 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ae6ef60a-70fb-3d37-a27d-74fb31a25104 | -17.172001 | -57.465 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82cc3c60-8cef-37c2-a723-13c70a5c8973 | -17.1623 | -57.4669 | 2024-10-13 00:56:38 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c6b7028a-3a4c-3c77-8c88-31ad032efcfe | -17.1103 | -57.4571 | 2024-10-13 00:56:39 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9b772785-c055-31ff-9081-37834f36354e | -17.100599 | -57.4589 | 2024-10-13 00:56:39 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 501fa09f-e503-3fa0-b8bf-e2c0ac00b3a1 | -16.993099 | -57.420799 | 2024-10-13 00:56:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b3a3baf7-4134-3679-81b0-3597f696c632 | -16.9965 | -57.439602 | 2024-10-13 00:56:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8ab45dfc-4e86-3ba6-a467-7d6f86aa5cb8 | -16.986799 | -57.441502 | 2024-10-13 00:56:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 47d0f7f9-0485-31bd-afa8-c8e7e63a7190 | -16.990299 | -57.4603 | 2024-10-13 00:56:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6d1d92e-e595-34cb-90c2-e7eda045eba6 | -16.9806 | -57.462101 | 2024-10-13 00:56:41 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 33d1e7c5-8530-3e30-abaf-0de6374ffbcf | -16.9998 | -57.4586 | 2024-10-13 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.2 |
| 4ff4d96f-06fd-36c0-89b3-333013ff7d0d | -17.0001 | -57.4381 | 2024-10-13 00:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.6 |
| 020a4af5-1b0d-3942-9382-4998a00216ea | -17.1957 | -57.4562 | 2024-10-13 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 151.1 |
| b35bc6bf-fb27-3a5d-9829-0ac383bc6a0e | -17.1758 | -57.479 | 2024-10-13 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 43b1d9ba-65e4-369c-a92b-4ab690058baa | -17.1761 | -57.4585 | 2024-10-13 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 177.2 |
| f7902206-d52c-35e7-8251-ff1c92ca79bc | -17.1764 | -57.438 | 2024-10-13 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.2 |
| 908cce26-4e06-3115-9bb5-7d021262892b | -17.1954 | -57.4767 | 2024-10-13 00:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.4 |
| f7c99230-9204-3f07-b429-96c7d62ea107 | -13.6574 | -43.0854 | 2024-10-13 00:56:44 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 821ef7b2-1e4e-37f9-865f-b23d3c7badef | -13.6476 | -43.088001 | 2024-10-13 00:56:45 | METOP-C | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 17b9f67e-16f7-33ef-9eac-95f7daef2fb8 | -13.8641 | -44.406601 | 2024-10-13 00:56:46 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c36f9d6f-525e-388b-845e-ce14b68f405d | -13.8544 | -44.4091 | 2024-10-13 00:56:47 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1a51be3b-0912-3ee0-9480-4ff2cecf8f5d | -13.7848 | -44.337299 | 2024-10-13 00:56:47 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| df952215-b914-3c62-855a-aa688ed966fe | -17.964 | -57.3843 | 2024-10-13 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 132.1 |
| 511c88b1-61e8-3745-b562-7c1289a8fd2a | -17.9643 | -57.3637 | 2024-10-13 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 166.7 |
| 6e5b10e5-d87e-3c7e-a1fc-2defa4a5ce2c | -17.9837 | -57.3819 | 2024-10-13 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 112.4 |
| d21d4b2d-8f68-3502-b9e1-31cd863aa3f9 | -17.9841 | -57.3612 | 2024-10-13 00:56:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.5 |
| f1307955-7d39-3d42-8a1d-bfcbd081d4b0 | -18.1953 | -56.5691 | 2024-10-13 00:56:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| 982f66d2-22dd-3480-81fd-abd8f6275418 | -13.1399 | -41.954201 | 2024-10-13 00:56:48 | METOP-C | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| e207e03a-34fb-3fab-a27f-6acaab9b8fa9 | -18.2147 | -56.5873 | 2024-10-13 00:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.6 |
| 4bffd692-d9bd-360a-982b-a5285b2c06d9 | -18.2151 | -56.5665 | 2024-10-13 00:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 204.2 |
| 2597aa73-bf37-3dcd-9f0e-7da8cb12f265 | -18.2155 | -56.5457 | 2024-10-13 00:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 8de8b894-3c7e-3d62-bd01-b1da7b29918b | -18.2166 | -56.4832 | 2024-10-13 00:56:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.2 |
| 1bc7277d-c7d5-3af3-8119-a6f35254061b | -13.4606 | -43.659599 | 2024-10-13 00:56:50 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8f80d5f5-ab82-3e0c-b084-1c936d16bf60 | -15.6352 | -59.910599 | 2024-10-13 00:57:11 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87984c4d-4c2f-317d-bb13-bfaaf1b6cbe3 | -15.6398 | -59.937099 | 2024-10-13 00:57:11 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b2080701-efad-39bc-9aef-c55a59adfc41 | -15.6445 | -59.9636 | 2024-10-13 00:57:11 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6580d739-9a47-32cb-ad85-4853678800cd | -15.6301 | -59.938801 | 2024-10-13 00:57:11 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04ad9465-33e5-37c7-b739-85666783111a | -15.6348 | -59.965302 | 2024-10-13 00:57:11 | METOP-C | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84fe2e3f-7aad-3e33-9dae-0429a1f59e03 | -13.0242 | -48.645699 | 2024-10-13 00:57:16 | METOP-C | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2382cd4a-0bfc-3fda-8e62-a600b0a31408 | -12.5229 | -46.810299 | 2024-10-13 00:57:17 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab9db6da-97ca-3261-916e-16ed70cdc8f7 | -12.5248 | -46.818501 | 2024-10-13 00:57:17 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 247c4a12-89c0-30e4-803d-f6821233a274 | -12.5267 | -46.826599 | 2024-10-13 00:57:17 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60f34579-649b-3535-961b-504b07637e8a | -12.8381 | -48.554199 | 2024-10-13 00:57:19 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3eb1085a-065c-3029-87e1-941094f5cccd | -12.8397 | -48.561401 | 2024-10-13 00:57:19 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fb34608-1607-319d-af72-2a72ee73c8b0 | -12.8413 | -48.568501 | 2024-10-13 00:57:19 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 469edd9c-461e-3607-9043-f6f9563cf4c6 | -11.722 | -44.530102 | 2024-10-13 00:57:21 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b9edd319-0754-34b2-97f7-1a61b82c7477 | -11.7247 | -44.5411 | 2024-10-13 00:57:21 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6cd25a06-b239-33c9-8dee-4ab74d9ccf94 | -11.7274 | -44.552101 | 2024-10-13 00:57:21 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 299c6e4a-6e97-3308-b4f8-fbe73192ec65 | -12.2788 | -46.783401 | 2024-10-13 00:57:21 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0957487d-eae6-361d-a2a9-bbdc7cbd4ee7 | -11.8453 | -45.115898 | 2024-10-13 00:57:22 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| eac28384-cf93-3507-914c-093a9c3f0d73 | -12.183 | -46.728298 | 2024-10-13 00:57:23 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7585a7b2-7965-3bcb-a019-039cdead8ecf | -12.1713 | -46.722401 | 2024-10-13 00:57:23 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35c2f603-33da-372a-9fda-14605236db38 | -12.1732 | -46.730701 | 2024-10-13 00:57:23 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 960cccff-101b-393f-a002-b63cae35eb38 | -12.1752 | -46.738899 | 2024-10-13 00:57:23 | METOP-C | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7b56793-9243-30c1-8c0c-c00a3a2f002a | -12.2614 | -47.1455 | 2024-10-13 00:57:23 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11cd5a63-f2de-3358-9612-955819283e51 | -12.2632 | -47.1534 | 2024-10-13 00:57:23 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c70e627c-7b32-35ce-be63-8f358ef4c203 | -12.6015 | -48.602501 | 2024-10-13 00:57:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| adb54040-6296-348b-9526-1377bca29baf | -12.5917 | -48.604801 | 2024-10-13 00:57:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f7df68a1-eb4e-30fb-8c52-b70065ab11ab | -12.5934 | -48.6119 | 2024-10-13 00:57:23 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 82718c65-33a8-3aae-ac7f-dc270c01688e | -12.5544 | -48.711399 | 2024-10-13 00:57:24 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4f33d8a1-e2da-3146-9bf0-53e538d57eb4 | -12.556 | -48.718498 | 2024-10-13 00:57:24 | METOP-C | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6cb5cea3-cedb-3d9b-b745-27845a08375d | -12.2865 | -47.647099 | 2024-10-13 00:57:24 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e82a7ec4-c1a0-3c8f-abc6-630aef6a5d29 | -12.2883 | -47.654701 | 2024-10-13 00:57:24 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c489343d-2918-3185-aac8-bf0464b590b1 | -12.2634 | -47.6366 | 2024-10-13 00:57:25 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7234c683-4aa2-3b55-839b-7b69b7389eee | -12.2749 | -47.6418 | 2024-10-13 00:57:25 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5708c779-e9c0-33f5-aa55-aad0a3007eb1 | -12.2767 | -47.649399 | 2024-10-13 00:57:25 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8ee748e6-31b7-3532-96e9-94b0a087112a | -12.2785 | -47.657001 | 2024-10-13 00:57:25 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 37471708-f855-3d72-af92-b1a97cebdc06 | -12.2652 | -47.6441 | 2024-10-13 00:57:25 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9490ace-0694-3c21-9584-c9dd60b864b4 | -12.267 | -47.651699 | 2024-10-13 00:57:25 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2bc9e301-7084-347e-984b-42a7abc418f3 | -11.1124 | -43.329498 | 2024-10-13 00:57:26 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 7c68eef8-8a40-3975-8c86-7517efbc8001 | -11.1158 | -43.342899 | 2024-10-13 00:57:26 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 74be9d93-f008-3d1f-a8f1-e6016be74fe5 | -12.1645 | -47.523201 | 2024-10-13 00:57:26 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 602f06a3-6263-3187-b1f1-75d3b6ef81b6 | -12.1547 | -47.525501 | 2024-10-13 00:57:26 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d0fed1dd-d605-3efd-aa0c-b7a91d1419a3 | -12.1886 | -47.979401 | 2024-10-13 00:57:27 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4fc7dcf4-a019-3b8f-8128-05cb513ed9cc | -12.1903 | -47.986801 | 2024-10-13 00:57:27 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f238c28e-e728-3fc0-9d96-2fe48b19be11 | -11.1027 | -43.332001 | 2024-10-13 00:57:27 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0b979989-c06e-3865-833b-1ee5bff3bc8c | -11.1061 | -43.345402 | 2024-10-13 00:57:27 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 198849d0-6d11-38f6-9099-2a33e5531d17 | -10.858 | -43.633301 | 2024-10-13 00:57:32 | METOP-C | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 624e8b65-5b2f-3407-abdb-ba797775ac7a | -11.1309 | -44.942699 | 2024-10-13 00:57:33 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b71f882c-9669-37d3-af3b-979f6e41e181 | -11.1335 | -44.9533 | 2024-10-13 00:57:33 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b7772565-ef11-3790-b7e8-8ad28f2b7a90 | -10.5096 | -42.4986 | 2024-10-13 00:57:33 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 85d78bd4-6686-3b62-b39f-7a32d08ff186 | -11.1212 | -44.945099 | 2024-10-13 00:57:33 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5a577ba4-af5f-3547-b44c-71d28184a9cb | -11.1238 | -44.9557 | 2024-10-13 00:57:33 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f9257b7-8aba-38ec-991f-dd88c0333671 | -10.4959 | -42.485401 | 2024-10-13 00:57:33 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f220b566-cdcf-3a87-9d46-d8ff51202bd4 | -10.4999 | -42.501099 | 2024-10-13 00:57:33 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| da5e8988-b5ee-3dcd-be96-4bd1f01af4e2 | -10.5039 | -42.516701 | 2024-10-13 00:57:33 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ad6f0070-14b7-3fb0-8874-874aa2a64dda | -10.887 | -44.3312 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4d00cfd0-173f-3c12-bd2c-9bb1ae72fc6f | -10.8899 | -44.3428 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 258a6702-551c-340d-9b54-0da74d748e93 | -10.8928 | -44.354401 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bfdfd380-7e87-39b2-b3db-70d5e138cb01 | -10.9603 | -44.627602 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d2bf29f-71c8-3264-ad8e-c762c8409698 | -10.8802 | -44.3452 | 2024-10-13 00:57:34 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README14.md)
