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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d8155e8-64ea-3c0b-9ecc-398bba6cd8e5 | -11.95611 | -47.02236 | 2025-07-21 03:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 860569c6-d6d7-356a-ae28-2f40a869a944 | -8.9199 | -47.36557 | 2025-07-21 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b55f472-e59e-31a8-bdf1-d03ecf1b4b8b | -10.15151 | -49.65514 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bf87660-1d2c-3d22-a7b7-ca12d08f970c | -10.66449 | -46.77434 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 117477cb-0f2b-3065-ac4b-ce727aee6d49 | -10.65885 | -46.77853 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9441f703-302d-3c00-9c46-c23e5097c5e0 | -13.89849 | -48.73601 | 2025-07-21 03:57:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db84c7b5-5687-32f7-9582-d0b4b6e7d8c9 | -12.37288 | -46.42807 | 2025-07-21 03:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fc20e42-a357-361b-85e3-db23a1c277ed | -10.68463 | -46.77462 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a30752d-b50e-36c3-bdb5-937be4746f29 | -10.7325 | -52.52254 | 2025-07-21 03:57:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 300cf0ce-fa70-3068-85c2-0638f93120fe | -9.59086 | -44.50048 | 2025-07-21 03:57:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2dd9401d-6233-3cf5-a1cb-cd79674a1b53 | -8.25888 | -46.06794 | 2025-07-21 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| feed22f2-6c5e-3cec-8421-4310983ef0dc | -11.95986 | -47.02837 | 2025-07-21 03:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 190e1011-f5a6-3b59-8916-f5a5c3cda735 | -15.61068 | -45.89735 | 2025-07-21 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df58d28d-5855-3a0a-9add-fa4ce2b0d885 | -10.15093 | -49.65805 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd633989-7d5c-3868-a5b0-ac77def5f92b | -9.61082 | -43.861 | 2025-07-21 03:57:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f9c58c5-b32e-39cc-a22e-6addde290e4b | -13.48867 | -45.502 | 2025-07-21 03:57:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5886212e-3e02-3523-909a-84ae3ac2134b | -10.65794 | -46.78358 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e3fc0d1-48c4-3ded-ae64-cc6c20368d4f | -13.09637 | -50.57603 | 2025-07-21 03:57:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71403da1-aa8b-3f62-9fb8-ca6d51590e43 | -10.64377 | -44.48492 | 2025-07-21 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43ec2f37-266d-3823-b236-5fed3395ceee | -11.3851 | -47.97826 | 2025-07-21 03:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 284be965-6908-33d0-9b77-d2f5f49751ba | -10.13286 | -49.6586 | 2025-07-21 03:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 01e9c5a7-7088-3388-a34c-2f34cb9871c0 | -11.77921 | -46.45487 | 2025-07-21 03:57:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 09b50af7-c690-3c10-86fe-e47474b47afe | -10.08749 | -46.60196 | 2025-07-21 03:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d63b520-8d68-317c-b3ee-2444d7bad0b9 | -14.74059 | -48.28301 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99dbbad7-52c2-3145-8fbb-a5cbe55cda70 | -12.48414 | -45.877 | 2025-07-21 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71b45e3d-0321-3835-8725-9499e176b4b8 | -15.80183 | -43.32127 | 2025-07-21 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3150a5d3-7389-3c67-a7a9-d2c3363a14e2 | -10.08935 | -46.59179 | 2025-07-21 03:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea48a2d3-3742-3e21-be62-4c5215e0c15b | -15.61341 | -45.89726 | 2025-07-21 03:57:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fb61d8ce-5998-3f13-93d9-27b3a9838704 | -11.60432 | -44.23472 | 2025-07-21 03:57:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d4706b6-3cc5-3602-a396-5ef1d7a54305 | -11.49555 | -48.07557 | 2025-07-21 03:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2239342-4c81-3eb4-bedc-34a54f89ef29 | -8.26359 | -46.06873 | 2025-07-21 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bab9ffe1-34b3-3a83-9c46-52b66ef2dc99 | -8.91482 | -47.36464 | 2025-07-21 03:57:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2fe0bd7-368f-305f-a0ab-987bbd45f99e | -11.50064 | -48.07651 | 2025-07-21 03:57:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5e7438f-d798-34fd-abf1-b3ed99fdfb33 | -12.47856 | -45.87782 | 2025-07-21 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8645b27b-e86e-342d-aa20-b37a71a83367 | -10.64439 | -44.48133 | 2025-07-21 03:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f713830-eb71-386d-9ca8-d1d188dd94c1 | -12.41286 | -45.89566 | 2025-07-21 03:57:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdcdf578-9354-39d2-8198-b7ad99eab40b | -12.37368 | -46.42374 | 2025-07-21 03:57:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6038116-ced7-34c5-93be-86751fe847d5 | -12.14232 | -44.77602 | 2025-07-21 03:57:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c720389-cf00-3ad0-bf20-caa9a0a1233b | -8.27303 | -46.07023 | 2025-07-21 03:57:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa3a569d-6d0c-3915-9874-68cd5eeeb3c6 | -9.63468 | -40.59938 | 2025-07-21 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8baa113a-c358-3830-9149-c364e4c4bc93 | -10.6799 | -46.77374 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88256203-8f2b-3fc5-946c-aa1d35874f84 | -14.77335 | -47.98956 | 2025-07-21 03:57:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f4e9419-e86a-3c63-b943-f8d3fe856f58 | -9.63748 | -40.6036 | 2025-07-21 03:57:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6746aac6-0fe7-38e3-845d-8c79e76cfbf5 | -13.23705 | -41.97705 | 2025-07-21 03:57:00 | NPP-375D | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f31449e0-3dd2-3734-a9a2-45049d96b356 | -13.09058 | -50.57479 | 2025-07-21 03:57:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 87d4168b-c48a-300c-9926-8776911fc631 | -10.67487 | -46.77097 | 2025-07-21 03:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 291d61c3-a826-38a5-b993-e04500bae7d2 | -7.2402 | -60.1904 | 2025-07-21 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 21114caf-e197-35ed-b058-1ea29134588f | -7.2771 | -60.1889 | 2025-07-21 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 04f54cad-88e5-3be2-9998-3e41b804f84a | -7.2957 | -60.169 | 2025-07-21 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 35843ed4-1c3a-387c-bc5f-c26bef58a292 | -7.2772 | -60.1698 | 2025-07-21 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| a0204ed5-9f86-3519-8b85-10ad767e987e | -17.24775 | -46.90987 | 2025-07-21 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa5b722c-c13e-3667-9c70-2bac19aa54a0 | -20.94426 | -45.82879 | 2025-07-21 04:00:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 371bd021-4049-3e67-8ac3-f2f7527cafc3 | -19.75647 | -44.01036 | 2025-07-21 04:00:00 | NPP-375D | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d7a46e8a-7e94-3cdd-9490-c5c7a7e498ec | -16.64381 | -43.8888 | 2025-07-21 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2258d7d5-3548-3eb5-859f-8ff5a8b6c937 | -16.70934 | -49.3568 | 2025-07-21 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32a178d6-5c52-39d5-836b-1908343b3cf2 | -16.70432 | -49.35574 | 2025-07-21 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 81c3586d-4f1d-3c72-8be5-3e9b0e4089e3 | -17.64778 | -44.74171 | 2025-07-21 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41a3cab7-a66d-353d-9271-4f8e8e2f875c | -17.33789 | -44.89433 | 2025-07-21 04:00:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1963a157-8457-3dc9-90df-efd0faf837a0 | -15.95116 | -48.31571 | 2025-07-21 04:00:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb98c8c1-6eff-3e4e-9645-08bfbb44893d | -20.45917 | -45.5514 | 2025-07-21 04:00:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6dcad53-ffe2-3dfc-a286-748640d2815b | -20.50015 | -41.91747 | 2025-07-21 04:00:00 | NPP-375D | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9386631c-0339-3a1e-bd24-1f9341db0365 | -20.45784 | -45.55384 | 2025-07-21 04:00:00 | NPP-375D | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bf3c9bf-a80c-3d8e-8218-8c4539abea58 | -16.70873 | -49.35979 | 2025-07-21 04:00:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cdc7ddb2-96e7-3881-bf5f-5fc1aad015ca | -15.76216 | -47.7648 | 2025-07-21 04:00:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49175573-0c0d-36ab-9c7f-7ed56fa24a52 | -17.64858 | -44.73711 | 2025-07-21 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21797be4-995a-3ab5-8dcf-9043cb577a44 | -16.64021 | -43.88812 | 2025-07-21 04:00:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6cff4bbe-c91d-3e85-926c-990d4748d936 | -19.3439 | -40.83652 | 2025-07-21 04:00:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 68e2caa6-7813-3839-969b-5cbd8d8ba34e | -17.64407 | -44.74095 | 2025-07-21 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ede6c566-9ebc-3233-ab1b-618193b826b1 | -16.08097 | -43.63618 | 2025-07-21 04:00:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f18e380a-7378-36a3-ad30-33af07d61f7e | -17.8425 | -40.42086 | 2025-07-21 04:00:00 | NPP-375D | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae69f567-7c35-3a89-bff2-92cf3d804011 | -20.79062 | -42.92867 | 2025-07-21 04:00:00 | NPP-375D | VIÇOSA | MINAS GERAIS | Brasil | 3171303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5a55109-b905-3034-8b43-f333a20eda77 | -16.07812 | -43.63129 | 2025-07-21 04:00:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 082bae46-2678-33c9-93ba-a9a5ed83f994 | -17.91308 | -47.76463 | 2025-07-21 04:00:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ca8a15f8-447d-3f30-9366-f25765a12e4c | -17.84194 | -40.42451 | 2025-07-21 04:00:00 | NPP-375D | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 75c263f5-caa6-36c2-9795-806c16963ab9 | -17.64488 | -44.73636 | 2025-07-21 04:00:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b85523e0-f54e-3870-8801-90ff0965f7b7 | -18.94654 | -41.49302 | 2025-07-21 04:00:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d43dc25f-4252-36cb-b058-673feb798241 | -21.36909 | -44.60598 | 2025-07-21 04:00:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 03a9f076-92ed-398d-a338-78d6df7a5b25 | -17.2579 | -48.05321 | 2025-07-21 04:00:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88b3026c-ebf1-355f-b285-5c35ed393556 | -20.05935 | -47.59005 | 2025-07-21 04:00:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bce20e3e-96a3-39cb-830a-5cd501b51140 | -19.17965 | -45.45761 | 2025-07-21 04:00:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8876843f-2abc-3033-bc0e-f6c62b47ed08 | -19.34 | -40.8396 | 2025-07-21 04:00:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8dbe94f9-3ac9-3060-9a94-a6f10b7c2af9 | -17.84527 | -40.42506 | 2025-07-21 04:00:00 | NPP-375D | NANUQUE | MINAS GERAIS | Brasil | 3144300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7f641aa2-dbb6-3777-a3cc-676d93040b94 | -19.34057 | -40.83593 | 2025-07-21 04:00:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 33addcaa-9f4d-37ed-8a94-0d75ac7f4836 | -20.94448 | -45.82554 | 2025-07-21 04:00:00 | NPP-375D | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 701f2bbb-763d-353a-81ca-e3f19882b4d9 | -18.12403 | -44.28495 | 2025-07-21 04:00:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03485aea-b97a-3357-b125-e1cf6d4c4538 | -24.54568 | -50.7998 | 2025-07-21 04:02:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ad03669b-b49c-364a-9998-37cbf045bdc2 | -23.70572 | -51.653 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1d7de180-bdb8-360e-b38a-67732ff89c0d | -23.72017 | -47.45702 | 2025-07-21 04:02:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c5005797-b3a8-3372-a1d9-120a9cc6cc9f | -23.22483 | -45.99483 | 2025-07-21 04:02:00 | NPP-375D | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bd684fa1-dca8-3a5e-890c-ce6caaebc3d6 | -23.33545 | -51.90574 | 2025-07-21 04:02:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c963ef62-8691-345e-9048-9f51440c7707 | -28.6219 | -49.74033 | 2025-07-21 04:02:00 | NPP-375D | SÃO JOSÉ DOS AUSENTES | RIO GRANDE DO SUL | Brasil | 4318622 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2474938b-73cc-328a-b370-7f5ff6cd877f | -23.43555 | -47.43032 | 2025-07-21 04:02:00 | NPP-375D | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 9c8b6443-1307-3a99-bbfe-35971e423cbb | -24.54603 | -50.7989 | 2025-07-21 04:02:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| b787202b-4540-349b-9124-646b3866533c | -23.57964 | -47.22164 | 2025-07-21 04:02:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d61f7036-4a79-3dbb-9aad-e3fb2bc02fff | -23.70167 | -51.65841 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| fbf61f95-4f9b-35ef-9ebc-d5042c4c51dc | -28.90774 | -49.96654 | 2025-07-21 04:02:00 | NPP-375D | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 61188bb7-c2c0-3d88-998f-2ed10b4621cf | -23.26975 | -46.40282 | 2025-07-21 04:02:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ec4f5dab-8037-3ab8-98c6-071cba9077ec | -23.33622 | -51.90229 | 2025-07-21 04:02:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6086ca9c-c9e6-3911-b49c-a3776d8ed9f5 | -23.7082 | -51.65297 | 2025-07-21 04:02:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 63e04d7e-df2b-3319-ba69-b1470624db25 | -23.57686 | -47.19366 | 2025-07-21 04:02:00 | NPP-375D | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
