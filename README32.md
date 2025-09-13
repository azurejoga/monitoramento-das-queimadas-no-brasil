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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8230e697-4a60-313d-b4c8-0709729d5d55 | -11.72696 | -46.59695 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e02831e0-1834-3c89-8645-b68132724b8f | -11.99505 | -47.75956 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5c9eea38-b634-3112-90ee-59ae1876191c | -12.90805 | -47.96552 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| adfb0b1d-5bde-38a7-957b-7653275c5201 | -14.20568 | -46.28356 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a45a15d2-680d-337c-88a1-63b58e844786 | -6.83419 | -47.8691 | 2025-09-13 03:47:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1ba1dff-e589-302f-a35e-fef8adb7e7c0 | -10.89712 | -45.57942 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c4e14b5-b7a9-3b94-b836-89144e9fe1a1 | -10.74152 | -50.50357 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 63cf0ced-4795-38ca-9553-a195db1bc55d | -17.99817 | -46.94221 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e98ddb39-bd34-36d8-94b0-816e5614f040 | -7.4137 | -44.35837 | 2025-09-13 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaea9462-8496-380e-937a-8a28933d6556 | -18.06902 | -45.45145 | 2025-09-13 03:47:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 79d938ec-a341-3ae1-b7b9-0dde2177044b | -17.32048 | -46.66211 | 2025-09-13 03:47:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9793d9e2-e6bf-3ee5-8e25-7083db0c1f6a | -14.29289 | -46.0589 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7e30ef4-8705-3ee1-99cf-c1fd575d22af | -10.77008 | -50.51748 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ef415737-da3b-3895-9dc5-1c4877495251 | -17.43531 | -49.22313 | 2025-09-13 03:47:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 65c59a9c-11a4-3db4-af8f-c22bc1fd7267 | -10.35252 | -50.51234 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3630e26f-28f2-3981-97d4-9a096056c4c7 | -13.47498 | -48.44435 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 579587c9-69d4-38a5-aa03-1b61a0aa1db4 | -18.00482 | -46.94269 | 2025-09-13 03:47:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07f394dd-1d06-33fd-b599-e57ba6b48fe0 | -18.45139 | -47.19413 | 2025-09-13 03:47:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 42b9b5bd-af9f-3995-b0a9-c8515784d4b8 | -11.81284 | -46.7392 | 2025-09-13 03:47:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33e0cbab-78a3-3f7d-859f-01bef267054c | -18.62535 | -44.26575 | 2025-09-13 03:47:00 | NPP-375D | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e9fdd75-a4d3-3a8a-b4f9-1c2f0e2bb5c7 | -17.13381 | -48.51068 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a142a1bd-a8e7-3f61-92e3-4f60ff9bb14c | -20.4479 | -46.4522 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbb61a85-a56f-3af7-8ea9-e8aa0249f94d | -14.69056 | -43.66872 | 2025-09-13 03:47:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 481ba551-acca-33c9-a399-3ba978f36ae0 | -14.29161 | -46.06527 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8eea504-d078-3936-a1be-6af73aa3d038 | -20.55418 | -45.83162 | 2025-09-13 03:47:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a89ab45-cfdb-38c7-9681-ac0448de3bdc | -12.11679 | -47.6014 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8615b18-df4d-386d-bee2-043c2bd0c002 | -12.11481 | -44.85386 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ffdea67-5831-3c21-8880-58bc379d0dcc | -11.42341 | -45.61549 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 876feaca-a3be-3be2-94ac-55b1dd556f6f | -19.06999 | -46.64371 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c6b39963-37c4-3692-82ae-8f37942c4ab5 | -11.84142 | -50.56692 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 89f19564-ab2f-395e-9c73-ccee0c358b38 | -16.53592 | -51.74683 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ff642c03-4cdd-3758-9efd-e9a68dccc893 | -11.99578 | -47.75958 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 35e97cdf-f684-37f6-9db1-561bf2f45bfc | -11.84653 | -50.56467 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| b1bb2ddf-e4c9-3cd4-a4e7-89aab35ecd80 | -14.21749 | -46.27955 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 9557b357-1a9a-3d44-9d43-c9785fb25915 | -16.52902 | -51.74475 | 2025-09-13 03:47:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4dd6f44f-ba41-38e2-9975-0ac9ea706dab | -15.3232 | -42.05273 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| c0dd8f63-8ca6-3c1b-9195-28494746bfc8 | -18.89606 | -47.06172 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4961492-9e7f-3db7-a141-86d2cc345449 | -11.41205 | -50.74951 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 16efe464-3c39-34e0-bc9c-9c3ecc906806 | -16.35192 | -51.55189 | 2025-09-13 03:47:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 37aca7b4-8b70-3690-84c1-f4afa39e1d33 | -9.74332 | -45.39103 | 2025-09-13 03:47:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb5346e8-7676-387a-9e7c-b75c8fee6d69 | -13.47953 | -48.4457 | 2025-09-13 03:47:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 821a289d-d19d-3b80-a6c3-b7d80cef3fca | -14.20265 | -46.27095 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a041060f-fa79-3de9-97e7-9630c246aea1 | -13.89923 | -48.25602 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7cb3d1eb-25dc-3a09-8e85-bcbba0522cc1 | -17.13368 | -48.48834 | 2025-09-13 03:47:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07bcc32c-64ef-3c75-89d3-f721129cb434 | -14.43144 | -46.40216 | 2025-09-13 03:47:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 92f2dbab-ea42-360e-9a28-2bd4589797ee | -10.76694 | -50.53223 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2ad243c-77be-3ad0-8d07-37c5da54a321 | -17.42049 | -49.26188 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5701f63f-3460-3175-9379-95dc61d9972f | -11.61733 | -46.60873 | 2025-09-13 03:47:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c7e0e46-0aff-316a-96aa-83a7359f2d5c | -19.73721 | -42.34755 | 2025-09-13 03:47:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8705ed88-48d3-3600-a43b-f6d2ac315345 | -10.7544 | -50.51416 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7eb2db69-e724-306c-937b-b223eef14a21 | -9.60839 | -40.62352 | 2025-09-13 03:47:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d53538e1-a54b-38c9-9f91-f2562fda5b76 | -11.42519 | -45.60606 | 2025-09-13 03:47:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4b69ddef-c816-361d-b29c-5f59b53cefe4 | -12.12194 | -44.84818 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f730e689-1ab1-3d9c-a9e7-b7ffed16a510 | -10.72111 | -48.6158 | 2025-09-13 03:47:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3c57356-8420-3d60-894b-696f44d73ad5 | -14.69476 | -45.14775 | 2025-09-13 03:47:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ebb84f1-c815-3c45-aa99-3aa7e8a855b4 | -11.41389 | -50.74519 | 2025-09-13 03:47:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 900e202e-c7b1-3d1f-a75d-a0159cf602a0 | -17.28009 | -46.10752 | 2025-09-13 03:47:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c54a6394-f752-3e55-8d89-adb00d817a8c | -11.20956 | -41.59727 | 2025-09-13 03:47:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1c13c019-da8a-32c7-b6c4-3e015663cf7b | -14.23292 | -44.25088 | 2025-09-13 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa3bc425-73a1-3532-9d03-96e65e22c50c | -12.10433 | -44.88691 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9783601-b7ea-3f63-93f4-858d667e767c | -10.76269 | -50.54694 | 2025-09-13 03:47:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d5aeb248-d0b6-3dee-8976-97789a1e11b3 | -14.17277 | -46.25505 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7252da9-8481-313b-818e-96c2cbcc86f9 | -14.18201 | -46.26395 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 57938241-865d-3d77-b43f-bca01b162abb | -13.23939 | -43.75446 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7d63cee-de5a-3ec5-9f3e-d47d5e7cf6c4 | -14.17475 | -46.27279 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6d4ac21-eb44-3629-b6ad-83cc5633f39f | -14.19674 | -46.27301 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a4c4cd6e-e21b-357b-a551-9a0a6a198419 | -18.16033 | -49.18913 | 2025-09-13 03:47:00 | NPP-375D | BURITI ALEGRE | GOIÁS | Brasil | 5203906 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| b0d0aee7-7fa6-33dc-a2c5-45fcea328c3d | -7.55699 | -42.63864 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 32b7133f-3052-3acb-9a2a-8fe82b9206ff | -12.1063 | -47.58348 | 2025-09-13 03:47:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7509db0a-052b-3b5e-8066-4783741e31aa | -18.89099 | -47.06049 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93925e33-cbc8-35e8-928b-2a6b3709a652 | -16.78778 | -51.35856 | 2025-09-13 03:47:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 634cfa54-0207-35be-a556-58e3106579b0 | -13.24941 | -43.75151 | 2025-09-13 03:47:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c88c5989-c7ac-39a7-b2b2-4868a0b4354a | -14.2844 | -46.0742 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a07bf6db-7ede-3b35-ae16-31308c479af8 | -10.36071 | -50.50677 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 01b4ba6d-a646-3bb8-b4bf-a60482480213 | -11.85966 | -50.58593 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 727a3c3b-c08f-346c-8abb-4802ec759b63 | -14.22658 | -46.307 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7b91645-0afc-3eca-baca-7cf6dd6a0ed2 | -11.48729 | -43.70604 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b0837d6-cdb6-3775-a955-0de6fdcafbc3 | -9.29055 | -43.26527 | 2025-09-13 03:47:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3d71208f-8def-3497-8749-39d87f4eaa63 | -13.90495 | -48.28933 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 52afdb86-0bce-37a5-82c5-6619c773319e | -19.3308 | -45.11654 | 2025-09-13 03:47:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| eeb17015-62ed-3554-bcae-a5e3bdc377f0 | -12.90398 | -47.9576 | 2025-09-13 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0893419d-b9bf-3ed6-9676-6e896e2a7d94 | -14.22401 | -46.27436 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b3881f1b-71d8-3ebb-a90b-908efd7cbab0 | -11.83085 | -50.56852 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 074df8a9-c1a4-3a3c-af14-28d76699a967 | -19.909 | -43.85445 | 2025-09-13 03:47:00 | NPP-375D | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8c887400-2642-34fa-82b4-fb4750dedfd2 | -14.17342 | -46.27948 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc289272-488a-3b34-8f75-17069bc62a02 | -11.37184 | -43.50754 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c28d465-f969-331b-b17d-a61281010855 | -18.85541 | -46.8343 | 2025-09-13 03:47:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9a5c045d-3e17-3ca4-81e2-9bb71eddf202 | -14.29097 | -46.06852 | 2025-09-13 03:47:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 028534ef-a84c-373d-85ba-e28b6f4e96c2 | -14.21936 | -46.26997 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 33bede4a-b192-35e9-89f7-838c5e65c9c0 | -11.46051 | -43.58654 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1dba3da3-9d2a-368f-88a3-eee22badd4af | -14.19076 | -46.24756 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d32acde4-d785-3bdf-9c7d-870cb6f239a8 | -7.56612 | -42.65229 | 2025-09-13 03:47:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 91d15ae0-3eeb-3daf-936f-778aa328a9f9 | -17.4114 | -49.24118 | 2025-09-13 03:47:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30e9f025-6164-36d5-aba0-832f48e40655 | -10.37826 | -50.49504 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| babf31bb-552c-3c3b-86dd-a91a00ad2b83 | -14.20126 | -46.27802 | 2025-09-13 03:47:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0eaa73b-c5e6-3294-83b4-018d360aaaca | -11.84852 | -50.56852 | 2025-09-13 03:47:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 548410e7-a548-338c-bd0f-bca49ff2eeca | -13.89218 | -48.25976 | 2025-09-13 03:47:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7e86768-ac44-3ce8-8101-2d22b9dcafc8 | -12.08191 | -44.89531 | 2025-09-13 03:47:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce8e8fa8-e13c-369b-beea-6f881c7e3a84 | -11.48457 | -43.70211 | 2025-09-13 03:47:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1a13cd89-b383-3b2b-b35b-f5faa3768c72 | -9.96999 | -50.30017 | 2025-09-13 03:47:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |


[Clique aqui para ver as próximas entradas](README33.md)
