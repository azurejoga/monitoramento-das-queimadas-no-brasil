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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09e14cc5-33a2-37be-94d3-c236ef1e47c6 | -10.60156 | -48.70573 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9442a9f4-701c-39fe-9d85-7e527f41eb5d | -11.06264 | -49.53746 | 2025-10-04 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d47e219d-9256-3a6e-9b65-713142842b90 | -11.96231 | -51.47602 | 2025-10-04 04:14:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d967546-02ad-3348-b891-9af9dc9aae8e | -11.49533 | -46.76277 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57c5d701-671d-311b-91bf-e1e8ccd51f89 | -13.77807 | -47.81118 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f53c4f9-0656-3bb8-a491-2a5d56b36c69 | -10.27097 | -44.33395 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 54ecc9fb-c9da-30ff-9691-ea425c62d755 | -13.14075 | -47.93782 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e70cceeb-21a2-30d4-922a-1dd121d0f188 | -13.74774 | -48.09742 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 215960c6-e1f8-3dd3-8928-86b8c2d26b7e | -10.24539 | -44.93906 | 2025-10-04 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fd72dfb-d546-32cb-9731-dd314a199560 | -11.86589 | -44.96331 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4974acd-dcc6-3fbc-b588-375b30d94ba9 | -13.68002 | -48.62544 | 2025-10-04 04:14:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef0a5dba-2484-37ab-896a-9b791bfdbde6 | -14.16919 | -49.20423 | 2025-10-04 04:14:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6c685aa-ebd8-37dd-b052-732bb342c04e | -13.92889 | -48.15721 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f1e7ae6-33cc-3939-bb04-80f1513dc38f | -10.93893 | -47.58433 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85830562-1d03-3ac7-877f-708880092cfc | -11.74397 | -46.81849 | 2025-10-04 04:14:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e29a25f9-c409-3b7a-891e-c945873f334b | -13.65873 | -47.29589 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 281078f2-dc33-3ae7-a56f-cfd628806c71 | -14.66183 | -48.30396 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b8daea08-6b1d-30d3-a99f-2af94c3921d9 | -13.12253 | -47.82539 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 2312739e-f41e-386f-ac6f-fb8159ae56ce | -14.79141 | -42.83241 | 2025-10-04 04:14:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 35a61e6c-eec9-3e4c-9f17-4b0c19972489 | -13.68161 | -48.61618 | 2025-10-04 04:14:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 08422af2-a323-32c0-a63a-a7c4d368c268 | -13.97126 | -48.10701 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 532cc9dc-586f-38b1-88ce-ff2dae90288e | -14.91691 | -46.88842 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b0b2551-e377-367c-b406-90ffeddfbd30 | -9.94229 | -50.23064 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 426c6ce5-3b88-385b-9f3d-a12f41a998be | -13.68999 | -48.03901 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0cb2897-df78-3962-a1aa-2b4a972cc8cd | -11.91936 | -46.37836 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 22902fd9-4daf-3b7a-8158-2449c5b7c7f2 | -10.30759 | -48.26231 | 2025-10-04 04:14:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d569c570-1ede-35b1-a39e-04f4549069a7 | -12.08714 | -45.15277 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79e055f3-5836-3e00-a198-f08aa181cba5 | -13.20536 | -47.80294 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d357dc7c-0e6e-3e1c-bb9b-bee88f92da5e | -13.29597 | -47.59712 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 12c38874-005b-3e94-b120-b48d3be22d3f | -10.18628 | -45.49847 | 2025-10-04 04:14:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 21767e4b-d825-3d72-a5f4-646161c6f8e2 | -13.34447 | -47.20113 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65d92687-e25c-369b-90c2-1e96328d9f01 | -10.27537 | -44.34905 | 2025-10-04 04:14:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51d56564-6099-36fe-95df-59ed106750e0 | -13.33545 | -47.61602 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bf0f985-cae6-3b8a-9b03-7ecf2f392136 | -9.91279 | -43.72112 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f89fe497-710f-3636-9a90-d914b809379a | -11.70508 | -47.50942 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ffb766d7-080c-3c25-980a-2564a2a85248 | -14.89145 | -48.27898 | 2025-10-04 04:14:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c36c91aa-58c4-33dd-971f-5ba705127d6c | -7.76967 | -46.23384 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4ff88db-c5b2-3d3d-9e3c-11d2110cbe7b | -7.5121 | -47.56047 | 2025-10-04 04:14:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4084566c-6f27-35ee-9f87-8effa202660a | -12.65053 | -46.9692 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9e267f05-bf52-3f8d-84a0-9668fb55873c | -14.65776 | -48.24124 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4c12886-ddda-3f9c-9e17-7f4fdcf10063 | -14.87734 | -48.31726 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1550b80e-490c-3b70-9eb4-6fb46533edd2 | -14.35507 | -46.10612 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 35fb9556-d8a1-3e1f-ad37-d8000931b136 | -13.1444 | -47.93844 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40dde8c6-e599-3aa5-9673-39b7c70d3700 | -13.7061 | -47.33816 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80726146-8a60-328b-82b2-ab266ba86f38 | -9.75541 | -43.62063 | 2025-10-04 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1497ec63-b12b-32cd-8303-e402e527918b | -9.96308 | -48.77056 | 2025-10-04 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d1202d7-966f-36f7-b581-9b7cbfacd117 | -13.99431 | -48.19214 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 357b6bdd-34ae-3618-a162-7902bf5af702 | -11.20623 | -54.08879 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e2e850c-28ab-37bf-85bb-0d983e53b5a9 | -11.9109 | -46.3654 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 12468a98-7f30-3ab6-9195-2f40898e276a | -12.64652 | -46.99338 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 273a5aaa-e87f-33a9-8396-dfeb4268de63 | -15.35447 | -46.25679 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1471e12-1469-3787-a44a-61dbdbedda3e | -13.28863 | -47.83836 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c8c1bca5-94e2-3d29-aed8-2feae4c4a92b | -15.03253 | -46.97517 | 2025-10-04 04:14:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 421667f5-f4f7-3688-b41f-45315a8f55fa | -14.23623 | -46.09337 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 115e425a-a7f8-3111-9cfe-fa2548da0c36 | -12.03019 | -45.20918 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5c0ad36f-1318-3064-8f65-b22d9616e065 | -12.60248 | -46.99799 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16d877bc-c9af-36d6-ace4-437e82452a60 | -7.77017 | -46.27576 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ccfa2b5-711a-3a43-a7ef-45fc3de2f7ed | -12.38287 | -46.50673 | 2025-10-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da96e879-047b-3af2-81ae-081a0a0e6b59 | -13.1117 | -47.84502 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 094d2ba5-60de-39a7-b473-95febf7bf503 | -14.87337 | -48.36171 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| c3bff440-8a76-39c1-b6b2-ea05d3bf2ca2 | -13.1066 | -47.87476 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3f40acbf-dccb-382e-a2b0-dc85aa484661 | -11.13239 | -47.17258 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74ccec16-abaa-33c7-a3a6-862db0a5b04d | -14.23346 | -46.08914 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bc8bd71-0a28-34b6-b8d5-8d172fd249e6 | -11.54826 | -47.68364 | 2025-10-04 04:14:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1bc55411-fecb-3fee-87d6-8bd1a9f61417 | -14.37258 | -46.14674 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd56095c-fa08-3acb-ab3e-d691b37365ec | -13.32461 | -48.11448 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70f5799f-4d3d-3fd2-be07-73420ae4e7d1 | -15.36913 | -43.6643 | 2025-10-04 04:14:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 56776003-59a4-3da7-b2ac-f112b0d00b71 | -14.44018 | -46.11318 | 2025-10-04 04:14:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3eb8d87-8228-3028-8f86-b8817a25f8ea | -15.29757 | -46.28851 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89024252-cc3b-34b4-a112-1c6ecf3546c2 | -12.22072 | -43.77084 | 2025-10-04 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00b37924-80c0-3960-a81d-9a344a65d622 | -14.15971 | -49.2128 | 2025-10-04 04:14:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d03bf866-1fcc-378a-a663-e0d138a92c0b | -10.24873 | -44.93961 | 2025-10-04 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a587218f-ba2a-3da7-8883-4ccb2f54df56 | -9.95868 | -43.70994 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 224850f1-b2bd-3691-9bb5-519483bdee08 | -13.8837 | -46.51463 | 2025-10-04 04:14:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b8d50b42-4bfa-327b-b8fc-8d611bedd396 | -13.11313 | -47.92402 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 62e1827e-636a-3aa7-a787-3da3d3118b0d | -14.60621 | -46.73058 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 832cbddd-97e6-33af-9ce3-bc5f60a2643a | -12.95379 | -42.4245 | 2025-10-04 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 48192d64-5873-3d2d-ba6d-c909a7421f1a | -13.70203 | -47.33945 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ee8c9369-3aa5-3447-8f3e-1b852b872db3 | -9.37458 | -47.63294 | 2025-10-04 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70024f6d-cedc-337a-a598-f2d7f4a7a334 | -11.79724 | -48.91728 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c0ef78be-8123-3ca4-80f2-fcb53161c271 | -11.84117 | -45.03226 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ef2a3d2-6fc2-3f09-af44-17efedbf707a | -13.25445 | -47.26229 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 912dfb3e-269e-346e-bf53-3a18c1299cbf | -13.98085 | -45.07996 | 2025-10-04 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 67e66b4a-63e2-3fae-9183-1ef0c88b161b | -13.34097 | -47.20048 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 646ff5ee-2242-37bd-83ee-bd88ca6ff903 | -8.91828 | -46.61039 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6c3658f-cb47-3ce1-af44-79327570ed79 | -13.74933 | -48.0662 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e293784-9417-3e81-8fe5-d9857f8332b3 | -11.91117 | -46.38497 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cff0fa84-5edc-35d8-ae37-f33523dea94b | -11.41623 | -43.487 | 2025-10-04 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| af683649-54d8-3618-bc53-8fe473133804 | -11.80116 | -48.91798 | 2025-10-04 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a16bf28-c1ad-357e-bba6-25bb2582dbfe | -14.59662 | -46.725 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0578b4f9-5455-3fc2-8675-a03981e769b7 | -12.07965 | -47.99481 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1fb2c5f7-27a4-3029-a9ab-0b59ddfe9991 | -13.33807 | -50.95423 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 31e68256-ca96-3503-a21b-f6e4f41b7789 | -13.68491 | -48.0469 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a512f1bc-e737-38ba-acb2-ff2d2443b664 | -9.90672 | -43.71657 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7846055-cd7f-30b4-8cdc-0701861ccdd4 | -12.86435 | -46.9918 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22e8cda1-9ab3-3973-a41e-a2b4388de548 | -14.33872 | -43.83421 | 2025-10-04 04:14:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a26d4f9d-653b-3475-bdfe-fac92116e8d8 | -11.47641 | -45.0373 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46b48f91-132f-3c8b-9f7d-101e8a4d3867 | -13.20606 | -47.79887 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2754837f-3dfa-37f4-a65b-a104a0b4a5cb | -13.6552 | -47.29537 | 2025-10-04 04:14:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b9206572-28b5-32c0-b6b8-7b98fb61fca3 | -13.32298 | -48.1463 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README81.md)
