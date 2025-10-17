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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93ef35a0-2e6a-3d25-a35d-a70dd3f76f97 | -9.88497 | -49.12136 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4e19c80-2ec4-3acc-90a9-715b1e13679d | -9.25218 | -45.25456 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b51f1cf-c590-3711-a4ae-293c818e8ede | -8.25782 | -44.06773 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3baae93-2129-36a3-a3c3-3a22a606ee73 | -8.42372 | -49.59543 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b90df5e-6300-38bf-8361-a99b21035539 | -12.30722 | -47.25979 | 2025-10-17 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4dbbf8c-a1b4-3ff7-b056-638807617924 | -7.90786 | -50.38695 | 2025-10-17 04:51:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d2ee639b-adf1-373a-a3d9-8e172a13a092 | -8.49553 | -48.49586 | 2025-10-17 04:51:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a61bc207-24e9-3858-8707-c49b86987b3c | -10.50106 | -43.43747 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4cd874ce-d5ac-33eb-b2e6-952d876f5af9 | -11.97612 | -46.56452 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3be42a0c-5c17-378a-9f9b-cc1d65c0d4ff | -11.97561 | -46.56417 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94e8561e-466c-33e2-8e4a-8b1282f0f1a6 | -8.4068 | -46.29006 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bb62de8e-5ce9-3f6c-95f8-a52c9bf2bf9e | -14.32276 | -51.44629 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5eecf854-e1f6-336d-9f04-845ed9523940 | -10.26721 | -44.02365 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 61c29a6b-70f8-3ce5-b8c0-92a7fc28637a | -10.28111 | -44.02496 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| da95f98a-87c7-3401-8de0-a044ac3932a8 | -13.42305 | -47.94335 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1d6fbc92-f141-3273-bd44-939395569dea | -15.78363 | -43.6549 | 2025-10-17 04:51:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcde5fbd-ffba-366f-976f-e9e787068572 | -13.43599 | -47.96663 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4fa160dc-dde1-38f9-98c4-18d045813c6e | -9.14343 | -46.6297 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b023c932-3c46-3949-9393-f31c62e8b1b6 | -10.86936 | -59.16878 | 2025-10-17 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2c90c61-6a29-38f5-94ab-9e00e3e41a6e | -10.97884 | -50.26185 | 2025-10-17 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ac7f3f3-949c-3589-8e53-55785288c96f | -8.70085 | -46.98212 | 2025-10-17 04:51:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d29c3d14-011c-3e4d-a309-9c51d300eb13 | -11.49694 | -44.05158 | 2025-10-17 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b767e26b-ec83-3d9e-bf1e-ddc4ac920571 | -11.09482 | -45.8734 | 2025-10-17 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11e42ed5-e549-3ee2-adc3-3778d5d294d1 | -10.50472 | -43.4093 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2ca65461-0974-3842-83a0-03dfa626c2d5 | -12.45003 | -51.33199 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a22bb91-bf89-3fe7-a420-b01ac534eade | -9.09471 | -46.68076 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c08471dc-1822-3682-9c9e-8608459e7754 | -13.26068 | -47.11419 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5715c510-1bc0-3f31-bf8d-9d2df22246c5 | -8.37389 | -46.31517 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae8337b9-098b-3539-965d-20ecc13be028 | -10.51778 | -43.38959 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ee404d7-7e90-3e80-b994-0abce65b16d6 | -14.23531 | -54.91352 | 2025-10-17 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9022d4ed-9d80-30ec-9638-771f098c7104 | -11.58699 | -44.05818 | 2025-10-17 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6d4ec44f-ac21-3cb7-9791-be49a7e02c4c | -10.50332 | -43.42003 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f54288c-0091-373d-85e7-af13ac55ac3d | -8.45549 | -45.12806 | 2025-10-17 04:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e11a1bee-a92a-3b0c-82a7-8f27a466ab55 | -10.92036 | -47.86596 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 25746d23-869d-30fd-9b13-175c2c6ba47f | -8.37798 | -46.31589 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1882cee1-7ac1-319d-b0dc-abd758d4fa4b | -12.45396 | -51.3289 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11942b00-df37-3f29-aad7-1c2f1efaec8b | -10.25757 | -44.05046 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 277741ab-0a64-3a82-bd8c-695bc7410067 | -11.75062 | -51.14509 | 2025-10-17 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eecdd6f2-3522-3862-9799-9e9b7eec4399 | -10.50548 | -43.40343 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 94ef0fbd-039c-3499-87bc-b3a62768f4c8 | -14.33239 | -51.47443 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1076b4c4-3e9d-324f-a95c-883696b953c5 | -8.38617 | -46.31714 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2381c138-8424-3e68-a652-e73eb29c0d49 | -8.25711 | -44.0729 | 2025-10-17 04:51:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6cefeffd-1d55-3fc8-a55e-411c1c03195e | -11.97778 | -46.55275 | 2025-10-17 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adc3b9a9-8ce1-36cc-bff1-20db46c1626c | -8.15919 | -47.98134 | 2025-10-17 04:51:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a4849017-4d9a-38f4-b8ab-d7976fffd2fc | -10.92103 | -47.86134 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 880fd896-8286-3107-96aa-142ef1d87a25 | -10.49593 | -43.39608 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5eff4ed5-aea0-3b17-ac45-2c30fc4d185f | -13.72796 | -48.21747 | 2025-10-17 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bde1ff22-146e-313a-99bf-4704a76b8814 | -9.94674 | -45.71059 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0ca07d1-394a-300c-9383-ae0bb48312a4 | -12.42083 | -51.2976 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 37747f77-e85d-323a-8d6b-e49e27816dae | -10.65143 | -45.24441 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5fddd46-5494-3789-aaa4-a52ba26bc255 | -12.16815 | -45.07367 | 2025-10-17 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c0e1c4e-1fc3-389b-8dd5-692fd3b180f3 | -8.37502 | -46.248 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f0325cf-fad1-3c12-b1ad-2663e3cab3ec | -9.13071 | -46.63169 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cfb5f23-8fb2-3dad-ba8a-004b23bef54d | -10.35622 | -47.52721 | 2025-10-17 04:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5dc7b645-a834-3561-a401-cfc96ca5820b | -14.34651 | -51.45009 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c7e0d837-735a-3420-beee-9d92dd0a86ee | -8.9364 | -48.65524 | 2025-10-17 04:51:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 968dfdda-4f51-328b-a4ae-08c07bc496e3 | -10.29289 | -44.04861 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 40d370df-84fe-31d1-88f8-6e444da2f0d7 | -10.26569 | -44.03552 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 326eb0cf-35da-387d-b96d-159e1b22c049 | -10.08385 | -45.34296 | 2025-10-17 04:51:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4b5844c-7f87-3b5b-8945-84dfdddfae35 | -13.38839 | -47.20963 | 2025-10-17 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6580af8f-435d-3288-b07c-59179eefe1db | -10.05298 | -43.83555 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ddacde7f-9cfe-3fc3-90ef-72a767f739de | -10.15731 | -44.53627 | 2025-10-17 04:51:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 762d7643-082a-311c-a560-3a854039c8a7 | -9.22496 | -48.59231 | 2025-10-17 04:51:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02fc04f8-af95-3f15-9208-a3605af933a9 | -9.09204 | -49.78786 | 2025-10-17 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33eec607-9165-34d1-b0d6-0cd32e498fed | -8.37958 | -46.24551 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3276f491-8cf3-3c9f-ac77-68f8185ea07f | -8.31857 | -47.86347 | 2025-10-17 04:51:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f6b61d0-8546-30a1-9146-f3c50dd13014 | -14.34821 | -51.43894 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b033088-b09c-3965-8967-a58de763d5dc | -10.12349 | -52.34351 | 2025-10-17 04:51:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03f2eac2-3908-33eb-a7e6-e02d610c2227 | -14.33067 | -51.43995 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 712d9656-dd0b-3e43-b2cb-45b3db58175e | -10.26992 | -44.04162 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2163dc2-f68e-3682-8d9b-df22a92c9051 | -10.50813 | -43.42337 | 2025-10-17 04:51:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90311a4e-5851-3e9f-8b28-9a531bd5c9f7 | -8.80834 | -49.31336 | 2025-10-17 04:51:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a84fee19-ada9-3a75-98b3-b8ba0624567b | -10.27702 | -44.02536 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83ee5d89-d8ec-3c5a-88f1-5ada51bbac7e | -10.27385 | -44.04127 | 2025-10-17 04:51:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84864d45-2e06-3a76-b688-0eb016136ff0 | -10.64414 | -45.30355 | 2025-10-17 04:51:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5828a995-fd1b-3457-8870-35f6ac7afab1 | -10.76082 | -47.87329 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0759bdc1-37e0-3e77-8215-a2ef817e8ff2 | -9.14644 | -46.63748 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d68e7418-e5b6-3dcf-b529-f3e8b24ad7f0 | -10.94191 | -49.48346 | 2025-10-17 04:51:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f8a3982-e0df-3f2f-a054-2faf935d3a77 | -9.50486 | -47.26767 | 2025-10-17 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a66d9757-6cd8-342d-bd9e-cfb33e147560 | -8.16333 | -46.06313 | 2025-10-17 04:51:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9e837f0-04c2-3a58-bfbd-8f6c04546559 | -9.2655 | -45.27335 | 2025-10-17 04:51:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7815a44e-a664-3cd7-8d43-0af4d902a5a3 | -11.52377 | -49.14178 | 2025-10-17 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b5fa2543-c824-3f16-887d-9874be03bc7e | -12.43712 | -51.30391 | 2025-10-17 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 622253b5-3e1d-3fce-87d1-13797ce94a1c | -11.47209 | -45.09001 | 2025-10-17 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d3f0d8b-8194-3dcd-ba7e-0c0cd239e7d5 | -8.39502 | -46.2257 | 2025-10-17 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9239c151-571e-3e3d-9b91-be4b193f4ec8 | -10.80617 | -47.93835 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8d46ba1-8724-3fb1-af54-7bda4e3bc123 | -9.26378 | -44.35414 | 2025-10-17 04:51:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 986dec5a-9e5d-3b53-9b5e-d626c2f44f1f | -11.41084 | -44.20135 | 2025-10-17 04:51:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f54de619-24da-3ac4-9758-c7c09b82a564 | -13.44788 | -47.9682 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5bdeff58-6d9a-3092-9934-5a04294c8448 | -13.93442 | -48.69549 | 2025-10-17 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e4bf224-9885-332f-bba3-7e6ef82200c2 | -14.30241 | -51.44304 | 2025-10-17 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4bc9a744-1c2e-3aa2-a847-3e4a959f9af7 | -10.29105 | -44.03318 | 2025-10-17 04:51:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 6adb7b00-9749-31aa-99de-a076c473e8ad | -11.61291 | -48.78654 | 2025-10-17 04:51:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 53c2174f-fade-3301-9c9f-38f4decf24ad | -13.45157 | -47.94171 | 2025-10-17 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f386aee5-02f8-3104-a9e6-2b0336a546f1 | -9.98072 | -47.01601 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4bb4f953-934b-3677-84a1-a39541a756bb | -9.34194 | -46.91261 | 2025-10-17 04:51:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f35e8a2b-c0f8-3cae-94b4-18bbb39930fc | -10.978 | -47.91486 | 2025-10-17 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50518349-17ee-3415-8c1a-a21c7bc0184f | -15.19155 | -49.31146 | 2025-10-17 04:51:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 739ae595-c646-3448-9b79-41c3edc1b862 | -10.17565 | -44.78698 | 2025-10-17 04:51:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5e4aebab-c9f1-3308-900b-d063fc3b282b | -9.83804 | -49.3107 | 2025-10-17 04:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README95.md)
