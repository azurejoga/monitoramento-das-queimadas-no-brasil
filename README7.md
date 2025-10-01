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
| 478015b0-384d-36af-a3ff-6f8fde155edc | -7.84334 | -48.21334 | 2025-10-01 01:11:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 672dfcc9-cc94-35e0-bcf1-e4ec6a62b1d8 | -10.02634 | -50.25375 | 2025-10-01 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| dbb2b163-1f55-3f38-aa69-2b7a4927274d | -9.28975 | -54.53605 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0b0eb1a6-4e9e-3e90-b6bd-218b101c975f | -10.20168 | -53.86205 | 2025-10-01 01:11:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 02ebe4cd-78db-3668-b1ae-029b0975b28f | -12.82768 | -50.54393 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 362.2 |
| e80a5b88-e307-3a2a-a294-4551928d3917 | -10.09881 | -50.31549 | 2025-10-01 01:11:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 5e5d47be-ec95-3f01-8c96-c1136ecc4956 | -12.81945 | -50.55185 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 273.4 |
| 9a6259e4-ffa2-3fe2-a0ce-4e2e108ac4a7 | -9.43803 | -54.57903 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c6e0d46c-440d-352c-9ebb-5708531c8fda | -12.83281 | -50.54943 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 414.4 |
| d259732e-49e5-38ec-8caf-42394e781016 | -11.96653 | -50.57166 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 7c4b63b3-128e-36be-b939-c5505fb4abcc | -11.15131 | -54.31915 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| a7492f2e-88e4-37cb-9846-8683f5ca34c6 | -12.82411 | -56.56025 | 2025-10-01 01:11:00 | TERRA_M-M | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 05932426-12ca-362e-9566-646169431aa0 | -9.07424 | -48.03753 | 2025-10-01 01:11:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| c24dde14-a889-39b5-a2ba-33488902678d | -9.42817 | -54.56104 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8f0a5494-373e-39a8-902c-a6139e436d1a | -9.55365 | -54.59338 | 2025-10-01 01:11:00 | TERRA_M-M | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8efebd8f-2fa0-3828-99cc-7175198faf19 | -12.29263 | -55.14269 | 2025-10-01 01:11:00 | TERRA_M-M | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 682e7e9f-58af-3042-a0d3-e4a986bba966 | -11.31158 | -53.95446 | 2025-10-01 01:11:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 276d51f5-225f-35be-b979-100edbed77cf | -11.15131 | -54.1122 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f6efe1fa-3da9-34d1-883a-b823c2bc9db6 | -6.57271 | -51.12831 | 2025-10-01 01:11:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 9dad576d-54cb-3b48-a99d-07aa6e6131ed | -6.57468 | -51.12187 | 2025-10-01 01:11:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 1a2c6baf-067c-36f6-9f2a-2c2df9504562 | -9.31065 | -54.53294 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| af03662b-2bec-316d-8abc-44d265d87ae3 | -11.14938 | -54.30664 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f982fd99-a49f-304c-add7-5771331c0e37 | -9.43614 | -54.56668 | 2025-10-01 01:11:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| a1314e34-eff9-397a-8bf1-a6b7db2d14aa | -11.96265 | -50.54853 | 2025-10-01 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ea25d65a-f2c6-3471-8d35-aca2dc811e52 | -11.16369 | -54.12332 | 2025-10-01 01:11:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7e2778ba-0672-3f99-b2a6-a648239b58ed | -3.47317 | -50.10789 | 2025-10-01 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 6c447bb3-ded5-30ba-b5e8-b1a727a2cce5 | -3.50364 | -52.47439 | 2025-10-01 01:13:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4b339452-9a2b-3407-ac41-065cf514daa3 | -2.69412 | -54.76987 | 2025-10-01 01:13:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 6ec4eb38-c571-3e85-ba09-a8b0e9c42034 | -3.51759 | -49.43423 | 2025-10-01 01:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 34346aa9-a46f-3b5d-ac02-e27ae1efbbdc | -3.49662 | -52.46943 | 2025-10-01 01:13:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 4f414188-2d4c-34fe-abc7-f071342c6274 | -3.46772 | -50.07195 | 2025-10-01 01:13:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| c9f9f52e-7b19-3ec6-90f6-cdcb7abef47c | -3.51578 | -49.44165 | 2025-10-01 01:13:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| afeefadb-747d-34af-b13e-6b27c451a7ec | -13.2973 | -50.6605 | 2025-10-01 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 87c2ab4c-4f97-3052-9529-adafdb48ff63 | -5.3382 | -43.7391 | 2025-10-01 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 5e3229b9-dfd8-3a75-954d-99add87e07c2 | -13.1969 | -50.931 | 2025-10-01 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| f3ed59b9-2b43-3838-9112-a157cbfcf939 | -5.3195 | -43.7405 | 2025-10-01 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 84364dd6-2133-384a-9f71-4b325d88284d | -10.8242 | -45.3841 | 2025-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 7bee3f4e-5a9e-3e3d-bf99-4bbaf11c1395 | -14.7826 | -45.7981 | 2025-10-01 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| abdd3830-f6e8-3fce-b801-74f427b48a77 | -10.9773 | -46.5217 | 2025-10-01 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 60b1a984-fe1f-35e1-8b36-9a5c3ee3c1f3 | -13.3463 | -47.8732 | 2025-10-01 01:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| b7164d3f-643c-3654-8a71-f1c2c940e68b | -11.4021 | -45.0515 | 2025-10-01 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 631c2320-88d9-3c42-bda1-5517286aaf58 | -9.3089 | -54.5229 | 2025-10-01 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3040ccce-30d9-3e31-80f9-66fc01f2a591 | -10.862 | -45.4019 | 2025-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| ca4310cc-3cfc-3cb5-8132-1efe26944852 | -10.8429 | -45.4044 | 2025-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 27e2fc41-535f-3cef-9a7b-1bb4314368bc | -8.4196 | -46.8108 | 2025-10-01 01:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| fc6fc461-841e-3f6d-bccc-fd4a6781bc6b | -21.0572 | -45.6638 | 2025-10-01 01:20:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 917b7470-477a-3a8c-8c8b-347bf707ce99 | -10.8433 | -45.3815 | 2025-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 04c5270f-427e-34c5-9f78-855c393ac0f6 | -9.938 | -43.6718 | 2025-10-01 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 2af179f5-6ad4-3d67-ac36-e76249de0b0e | -10.1081 | -50.3203 | 2025-10-01 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| f5849d29-adde-30d3-a3ac-14a0ae5fbd48 | -3.1012 | -47.0301 | 2025-10-01 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| e4beca9e-ad92-3748-bc26-a2a864705621 | -13.1777 | -50.9335 | 2025-10-01 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 637f6595-0d9c-3451-893d-e6c14094d66b | -16.2562 | -50.9275 | 2025-10-01 01:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 245.4 |
| d643a429-32ad-35e0-b777-c122f8dc217b | -14.3657 | -47.1291 | 2025-10-01 01:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 099796d2-1632-3b3f-8fce-408b62cbb7a4 | -3.1013 | -47.0082 | 2025-10-01 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 522ee412-6583-30a1-8643-5b72866d4367 | -9.2902 | -54.5242 | 2025-10-01 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b6ecd3c6-eb29-3b60-b586-4c6fd7d67b9e | -8.559 | -44.7184 | 2025-10-01 01:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 50406cd5-d789-3a8c-955b-d13d73e50813 | -13.3467 | -47.8508 | 2025-10-01 01:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| c2183ed5-bddf-39b0-ab41-cfffbdfeaa66 | -20.6309 | -46.2046 | 2025-10-01 01:20:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 9640bf15-ccd3-35ef-8bee-fd57b8606616 | -11.383 | -45.0543 | 2025-10-01 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.4 |
| e336eeca-4918-39db-af30-acb83c9bef69 | -14.7831 | -45.7749 | 2025-10-01 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 251.7 |
| c6d666c4-6629-39f4-a467-d9b0e23f1349 | -10.1084 | -50.299 | 2025-10-01 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 57749ddb-6b99-3db2-b3c3-f76f28893005 | -20.6103 | -46.2098 | 2025-10-01 01:20:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f9cb137e-db71-373a-8ee6-fae73363cf59 | -10.9769 | -46.5443 | 2025-10-01 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 9386d9b1-3bc6-3e41-b1aa-484f7516dc44 | -15.3381 | -46.2744 | 2025-10-01 01:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 35b63dce-0ef8-31d4-bdbd-6b3d0e4f08c5 | -13.3274 | -47.8536 | 2025-10-01 01:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 70.9 |
| ba3de619-9316-35d5-94c4-3631d97bf906 | -15.1806 | -49.1011 | 2025-10-01 01:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4baf5812-08f7-3027-b389-1df244c597ce | -3.0827 | -47.0088 | 2025-10-01 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 47efe69c-9628-3bfa-9518-d49a58b63e52 | -3.4577 | -50.089 | 2025-10-01 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 36f57b12-44ba-39f0-87cf-43228d49b234 | -5.8657 | -43.3981 | 2025-10-01 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 8ed3a7db-7bf9-3373-80c6-941d0df394ed | -16.2366 | -50.9306 | 2025-10-01 01:20:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 157.3 |
| b44319a0-d5a5-3b5e-8011-8b181aeb198c | -13.3165 | -50.658 | 2025-10-01 01:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 78711f02-e899-3882-8f46-540291b2d942 | -11.1523 | -54.3104 | 2025-10-01 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 9a969d56-6aab-32d9-8176-b1bc8bf9370a | -20.5998 | -45.878 | 2025-10-01 01:20:00 | GOES-19 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 2f5c44e6-ea6c-3bd5-85e8-c7a492d4651e | -9.9189 | -43.6743 | 2025-10-01 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 6cc29b0a-6ddd-36ef-916e-ae782637eeaa | -14.7836 | -45.7516 | 2025-10-01 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| c6eaab25-0875-31e6-86da-96cc53bdc78c | -9.9383 | -43.6483 | 2025-10-01 01:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 0d70c9a0-b7cd-325d-af93-3f69d7c21032 | -15.1611 | -49.1042 | 2025-10-01 01:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| d313941b-8b62-35c9-b327-d336843ad377 | -14.9914 | -46.9549 | 2025-10-01 01:20:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 91.3 |
| cfff32f6-eefc-343d-ab37-1e7560f0bbf9 | -14.8026 | -45.7713 | 2025-10-01 01:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 3cca3769-82c5-3f9b-959e-7be49e522716 | -10.9204 | -46.5065 | 2025-10-01 01:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 8f6f2a47-3623-3396-a1ba-ec0c365ac269 | -15.9431 | -48.1245 | 2025-10-01 01:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 225d9d65-fb91-3887-9552-1bd407c7755f | -16.2366 | -50.9306 | 2025-10-01 01:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 4a069f52-e9c1-314a-b792-5d024f838073 | -15.9431 | -48.1245 | 2025-10-01 01:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 4fb4d3f7-604d-3f67-8641-eb2d7163c35b | -6.1342 | -44.7375 | 2025-10-01 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| d6df9031-d059-39fc-89cf-285022e5a846 | -14.7831 | -45.7749 | 2025-10-01 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| 135251d0-f864-3e6e-a305-6888acf9b84d | -5.6361 | -43.9258 | 2025-10-01 01:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 00532c64-6d9f-398d-90fa-9dad70590504 | -20.6309 | -46.2046 | 2025-10-01 01:30:00 | GOES-19 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 436c53aa-7818-3f50-ba1b-14a0835ac8ca | -16.2562 | -50.9275 | 2025-10-01 01:30:00 | GOES-19 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 297.5 |
| 4e62dcc8-5651-322a-a98d-3f7745e53eaf | -15.1193 | -46.4521 | 2025-10-01 01:30:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 42.8 |
| deaa8563-24d0-3f5e-8ec7-d4a64c9a1c8b | -10.9773 | -46.5217 | 2025-10-01 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| e00940ed-d9cc-3292-94d7-0566fdd5dd8d | -3.1012 | -47.0301 | 2025-10-01 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| d934afa6-9d26-3638-aaae-7d5c6a72cd6e | -10.8433 | -45.3815 | 2025-10-01 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 86.0 |
| aaa5f31c-7ef3-3582-aeba-8c12b2eee975 | -16.2567 | -50.9057 | 2025-10-01 01:30:00 | GOES-19 | ISRAELÂNDIA | GOIÁS | Brasil | 5210307 | 52 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4197b5ed-0192-34f0-bf95-73f1bca235a8 | -14.8026 | -45.7713 | 2025-10-01 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| be62603a-5cff-3df0-a536-18ef6d6b5536 | -11.478 | -45.0868 | 2025-10-01 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| eb92b980-f388-32a6-941e-ddee539ae976 | -5.8469 | -43.3995 | 2025-10-01 01:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| a33a0214-016e-3ee8-a300-677ffced1863 | -3.4577 | -50.089 | 2025-10-01 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 578b681e-6905-39e3-ae67-cf86af95417b | -14.9914 | -46.9549 | 2025-10-01 01:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f0d3212f-6a71-3181-8e63-cfa8da69b183 | -20.5998 | -45.878 | 2025-10-01 01:30:00 | GOES-19 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 108f8622-14c9-3e9f-a81c-130db03fa1af | -21.0572 | -45.6638 | 2025-10-01 01:30:00 | GOES-19 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 64.3 |


[Clique aqui para ver as próximas entradas](README8.md)
