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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c043fb93-dc74-313d-80bf-89d5caad05bb | -10.7585 | -50.311699 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51743622-e20e-333e-bc86-6a1e614379ba | -20.155701 | -45.414299 | 2026-08-21 00:42:00 | METOP-C | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7e5c80de-dd02-34b4-bc39-96a09312aeaa | -15.0056 | -52.685001 | 2026-08-21 00:42:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a8102f88-c736-3c8d-a303-87a0d37f7c5d | -6.2316 | -55.609901 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed6c312e-0749-36a1-b9a0-0f3a7542edd6 | -6.8801 | -59.4212 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39576f3c-bb26-3cc9-871c-2ba43a6d27bd | -6.3541 | -58.316799 | 2026-08-21 00:42:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 320f1c83-afef-3095-b1df-522ff6297d13 | -12.7299 | -48.479198 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf1ae80f-87c3-387b-82ec-f5614855fcee | -6.2498 | -55.4109 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba680199-3a56-383b-8278-01251571ec0c | -10.8182 | -51.007801 | 2026-08-21 00:42:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 216bd477-25ff-336f-aead-dfec4314bb65 | -4.1774 | -49.400902 | 2026-08-21 00:42:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b4bbe40-03c6-3fa2-ad4d-cd68dd72f38e | -6.3473 | -44.070301 | 2026-08-21 00:42:00 | METOP-C | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c81568b6-0f5a-300f-b19d-394b8879724a | -18.204399 | -50.7397 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1aa7101-55b1-3f88-a8ac-2151b300ae24 | -9.3918 | -60.402 | 2026-08-21 00:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9329595-c388-3af3-b6a1-ff2efb2a5a8f | -7.2518 | -49.909599 | 2026-08-21 00:42:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eca1800-7a43-3600-b726-52edd099a31a | -10.2446 | -54.369598 | 2026-08-21 00:42:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae5e49af-8575-3ed8-a05b-461b12ffa7f3 | -6.0114 | -57.8046 | 2026-08-21 00:42:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3a5a268-dc66-337d-baf9-b553797bde2c | -21.327801 | -43.804798 | 2026-08-21 00:42:00 | METOP-C | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| da4f1581-3f18-3918-93ed-e75863e1e16f | -6.8851 | -59.445099 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e34e8365-82a9-389d-898d-5a2fd07880ec | -7.6384 | -45.769001 | 2026-08-21 00:42:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e63354f3-2c25-3ab5-b470-205c28b583ee | -14.5815 | -53.007702 | 2026-08-21 00:42:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ccc947b-745e-3fd8-aa3f-791f067ea7b5 | -6.9465 | -52.785099 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c0019a-78ff-313e-8796-375fccaf8272 | -12.8377 | -48.454601 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ed8bbb5-3aee-38de-885b-88534f3aff79 | -15.4883 | -53.895 | 2026-08-21 00:42:00 | METOP-C | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 73779e5f-df25-337f-8433-ea8bf6df88c0 | -3.967 | -43.1166 | 2026-08-21 00:42:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4e5fea1-b3b2-37e4-94bc-6c3eb61e27d2 | -13.2502 | -51.6437 | 2026-08-21 00:42:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 57d27487-2ed4-3437-b757-71e2fae6bb11 | -18.196501 | -50.7514 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1a94372-e04b-3b5d-b96e-a75831abf76e | -4.9633 | -56.259998 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2120ca5-513d-32e4-9b54-ddc3d1d9eac8 | -6.6878 | -58.937698 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0462422b-c048-38bd-8c07-41ee1495ec54 | -18.688101 | -47.497299 | 2026-08-21 00:42:00 | METOP-C | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6c0e5283-8a14-3444-84b5-fd3b48f9862b | -18.2082 | -50.7589 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2985dec6-41e0-365a-a6c5-5e9d697b8ce8 | -6.6719 | -52.890099 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 025e07fb-9011-38c0-a8bb-78ec4046f241 | -20.9484 | -49.1455 | 2026-08-21 00:42:00 | METOP-C | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 32c4a65b-4a8d-3290-880b-f84bdbbac19d | -19.668301 | -46.049099 | 2026-08-21 00:42:00 | METOP-C | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6d615ff2-27e3-3c1c-84e9-1c37d87defcf | -7.773 | -46.033901 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ffdd80cb-49eb-3cba-9f23-2701f564a844 | -11.1825 | -54.0256 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afbd19fb-9868-34fe-b8fe-ea7bb98e3b4e | -21.325899 | -43.797001 | 2026-08-21 00:42:00 | METOP-C | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 05bb42bb-941b-33a7-99d4-12fc45ffaea4 | -18.651899 | -43.169701 | 2026-08-21 00:42:00 | METOP-C | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0ca3ea0-24de-3c66-95f3-28c12910919a | -12.7511 | -48.481701 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2a2026ad-4c33-39a8-8f9d-f26ecf7bd18e | -12.7174 | -44.489601 | 2026-08-21 00:42:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e6858ad-73fe-3ec9-a994-1a9b5f9b9f01 | -14.5695 | -52.998199 | 2026-08-21 00:42:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a38560fc-6e97-3ac2-b3a1-4de1c5d9388d | -6.8463 | -59.4529 | 2026-08-21 00:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d4acd42b-cc87-3f9a-af6d-4ab11942942b | -8.0564 | -50.0975 | 2026-08-21 00:42:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dead2a38-7390-3b26-89ea-ea338bb57362 | -12.1263 | -50.127899 | 2026-08-21 00:42:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a009189-310b-3d78-beee-954ef04860b7 | -11.9989 | -53.437099 | 2026-08-21 00:42:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 247529b8-1637-3a1d-b04c-a3b389554552 | -10.3108 | -50.379299 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad020b04-470f-32f9-959b-783b1057afd9 | -21.3703 | -44.123699 | 2026-08-21 00:42:00 | METOP-C | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e5ca17c-619c-3c0c-9cac-bc80a1222171 | -10.2732 | -50.301998 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f894828-5a01-3595-a829-6bd9cd3353fa | -7.7292 | -46.154999 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb4b4e6-f438-3a6a-b1e2-d7a31f0f8a17 | -9.4592 | -51.6497 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d39f228-d4a6-3209-8b17-bd3f0d09067e | -10.2602 | -50.289398 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5cd8cc3a-f2ef-320b-9d7b-7aaf976dca36 | -6.8749 | -43.7342 | 2026-08-21 00:42:00 | METOP-C | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 631b0e1c-5d50-382d-afcd-5f9cb3bff547 | -17.691401 | -44.4883 | 2026-08-21 00:42:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a52d9a16-968e-3985-b730-e3a22b4f26d2 | -5.6016 | -44.012699 | 2026-08-21 00:42:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c2b982b-49de-36c6-941b-2addce5dfc0f | -7.3625 | -45.824699 | 2026-08-21 00:42:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c9d42d8c-914d-3528-9d2b-c50b015df214 | -12.501 | -54.752602 | 2026-08-21 00:42:00 | METOP-C | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4b7f1c52-29e2-3bbb-a05b-7cc279728018 | -4.9371 | -55.767799 | 2026-08-21 00:42:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d77f4dec-ac1d-33bc-b622-0318b41b1b43 | -12.6659 | -47.780602 | 2026-08-21 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1748e751-7778-3300-b8d9-e395bbb02c96 | -7.7604 | -61.109501 | 2026-08-21 00:42:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c8fac69-467e-3471-9b1c-5712f50051ee | -11.158 | -54.0061 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d1f0c61-90d6-36fc-9aca-0c843dab30e5 | -6.3942 | -54.9459 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5aae84e-d081-3b30-a408-480d370f9b92 | -19.855 | -43.877399 | 2026-08-21 00:42:00 | METOP-C | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7f83c845-6ecb-3d0a-a9a0-cc0bd8356e93 | -6.4279 | -52.762199 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c7a2a94-b654-3bd4-bd7c-2afda07dead0 | -6.6336 | -53.3689 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be3a3842-795a-304a-a7f5-715bbe47a141 | -13.2581 | -51.6325 | 2026-08-21 00:42:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae2d883e-89fe-3334-a343-153a0506ba48 | -6.2191 | -55.5994 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 905b35ce-5d83-374a-a61c-c7179cd33031 | -18.686501 | -47.490002 | 2026-08-21 00:42:00 | METOP-C | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7a6fd7a1-833e-35d1-acdd-8aba76aada73 | -7.3379 | -55.674702 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03f27803-b3c3-3c05-a851-0815abb70e36 | -11.1898 | -54.011799 | 2026-08-21 00:42:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14c03a30-d908-3414-a02e-2ea3ecbbd27d | -10.319 | -50.369701 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a439d0f9-66b8-325c-ae83-72ba845c08a6 | -11.6298 | -46.543301 | 2026-08-21 00:42:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce1185d1-d047-3800-b8ad-ec3155f1fe19 | -10.3174 | -50.362301 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ce268278-bae9-3e51-a71b-db63f29165c8 | -9.3955 | -60.3699 | 2026-08-21 00:42:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0587edc1-b356-3067-be75-783ae034a200 | -9.4485 | -51.6008 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49475bf7-3e0c-38af-ae84-cd308cc7a7e4 | -6.2219 | -55.612 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2eaeecc6-1784-3584-8c99-acdce4ec3231 | -10.8027 | -50.2785 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6095734-235d-38f9-a625-71bab06bc9ba | -10.77 | -50.317001 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec6b7490-d2f9-354b-afe4-7bdea26b9f24 | -12.8444 | -48.438301 | 2026-08-21 00:42:00 | METOP-C | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 617f948f-89d5-356d-a106-efc90e872e67 | -10.3585 | -48.244099 | 2026-08-21 00:42:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75f87732-e722-36c5-b28e-5e2def69e3cc | -12.8103 | -48.423901 | 2026-08-21 00:42:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19cea6ab-6371-3af6-a629-8895ace9b0a1 | -6.1171 | -53.074501 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 136c7b3f-f957-3363-9382-982716fc00cd | -6.2045 | -55.484901 | 2026-08-21 00:42:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 153711b7-c4a4-3cd7-9a5b-88abfc46d815 | -8.0874 | -51.670101 | 2026-08-21 00:42:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f252ed3-104a-36bf-9998-d15fc79aafe3 | -10.7667 | -50.301998 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 180259a2-aa34-3d65-af63-4cd5edfa3e44 | -18.2101 | -50.768398 | 2026-08-21 00:42:00 | METOP-C | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0d42de6b-e576-3801-abe3-0dfcfe945b78 | -14.5337 | -52.0172 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e006238c-f97c-396a-b45b-1329b6ee4892 | -10.3223 | -50.384602 | 2026-08-21 00:42:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a05e05b-073b-3641-a3f5-01b07d27c3d7 | -8.5443 | -54.7747 | 2026-08-21 00:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 109e4d44-8598-311c-8df0-e8f64bb5d995 | -18.9762 | -47.0233 | 2026-08-21 00:42:00 | METOP-C | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 286f567c-c6da-37fb-9caa-5dc1144b3973 | -16.961901 | -44.729 | 2026-08-21 00:42:00 | METOP-C | LAGOA DOS PATOS | MINAS GERAIS | Brasil | 3137304 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 382da479-08c5-3a23-be0e-5ede6afe04d5 | -10.752 | -50.3288 | 2026-08-21 00:42:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d3753291-9e70-3104-b4ad-a0cedf5c6177 | -7.6344 | -45.752201 | 2026-08-21 00:42:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a0ce4861-c57c-377a-9f99-9090a2282cf9 | -14.3292 | -51.916302 | 2026-08-21 00:42:00 | METOP-C | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c7dc16d-4b8f-31db-89f4-2e6919b83fbc | -13.439 | -43.833302 | 2026-08-21 00:42:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 09ddaaed-bd5f-3c76-9ced-a926ff39087f | -18.039801 | -46.465599 | 2026-08-21 00:42:00 | METOP-C | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d2256f70-0a33-347d-92ed-dfd2eea35edb | -9.4476 | -51.6437 | 2026-08-21 00:42:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7712d52-d4be-3c16-9ad7-04c76eb22ae6 | -12.6643 | -47.773701 | 2026-08-21 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a765cf8e-3709-37e7-b85a-35b64aa09a67 | -12.5057 | -47.847 | 2026-08-21 00:42:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3b915a6a-e2d8-303f-99ae-b9f69790dfb0 | -14.4615 | -45.617599 | 2026-08-21 00:42:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0302168f-7360-3ec1-84b0-840e4217bbfe | -6.8872 | -55.7141 | 2026-08-21 00:42:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b46107d-4c35-30f6-a468-c00bc10ce1a5 | -3.9818 | -47.209 | 2026-08-21 00:42:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
