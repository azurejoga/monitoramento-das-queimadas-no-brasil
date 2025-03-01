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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50877c84-bc6b-3fe8-906e-2b730c7fd77d | -22.83907 | -42.76965 | 2025-03-01 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1357f6cd-d83d-3bb4-ba0d-8fb446692085 | -22.56393 | -43.62701 | 2025-03-01 03:21:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5a90d796-0673-34e6-8563-c2d60d63a0f3 | -22.83824 | -42.77342 | 2025-03-01 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b1e22a54-f096-35cb-b970-4751ec48f965 | -22.8337 | -42.76861 | 2025-03-01 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8982a364-2a64-3bc8-bd19-258fe14740cf | -22.8329 | -42.77225 | 2025-03-01 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8148f57d-ac9a-35d4-9f2a-e109de554069 | -20.04102 | -40.94228 | 2025-03-01 03:21:00 | NPP-375D | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2cfa7790-c4ce-32b1-80d1-9e91456b71c6 | -9.48762 | -35.5651 | 2025-03-01 03:40:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 44a5ccc6-bd89-3729-8e72-c5d379f1e57b | -9.92076 | -36.99173 | 2025-03-01 03:40:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 551612d7-1099-391d-a902-a6aabdaa93cb | -9.80133 | -37.94901 | 2025-03-01 03:40:00 | NOAA-20 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c7b75c20-ffc4-3236-8646-455234e15be6 | -8.40484 | -37.03544 | 2025-03-01 03:40:00 | NOAA-20 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 003559c1-01b0-3861-a7ad-dfbcf9303422 | -7.47416 | -34.84365 | 2025-03-01 03:40:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 76168f4a-e480-3780-b080-9594cd2d7a45 | -12.85997 | -38.36641 | 2025-03-01 03:42:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ea016b42-af2d-3459-a22a-272fe76cabdb | -12.5497 | -44.66933 | 2025-03-01 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea5f8dc-5cad-3c6b-b174-7b30baac8c0f | -10.69676 | -37.04895 | 2025-03-01 03:42:00 | NOAA-20 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4e8ae7a1-e95c-3d88-b105-3d42b09e1ac5 | -14.03977 | -41.45703 | 2025-03-01 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5a348235-fa7d-3134-a237-246f57e38fbc | -12.55232 | -44.67024 | 2025-03-01 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 050fd45e-c975-3952-9f0c-fc3370d7e0e3 | -12.55455 | -44.67037 | 2025-03-01 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e96de79-6fd4-377d-9fbf-e1c5c0ca0d01 | -12.51427 | -45.49687 | 2025-03-01 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11236fa1-4f4e-3745-ae15-b48590212a5a | -22.81979 | -43.34243 | 2025-03-01 03:44:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6872c0c2-fdb0-3e1e-8c75-9dee7d4e5bb8 | -22.56302 | -43.62777 | 2025-03-01 03:44:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 267a3564-d975-3781-ba1a-d39610396cc3 | -16.07116 | -46.61431 | 2025-03-01 03:44:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 34ce4f92-da08-31e9-8be7-af5d6f0543d1 | -20.25532 | -50.78745 | 2025-03-01 03:44:00 | NOAA-20 | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a0c7de7a-07c9-3e5e-95c1-ec365f6f06e1 | -22.72447 | -43.45576 | 2025-03-01 03:44:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 84c08f40-ee38-3fc3-8d5d-d6985e7242d3 | -17.53461 | -42.28649 | 2025-03-01 03:44:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4523a175-e902-3e6d-b81d-4b57878b0bb1 | -19.70168 | -44.77113 | 2025-03-01 03:44:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8490b820-2b66-3c4e-9b63-66c9a42d7eb2 | -22.83554 | -42.77058 | 2025-03-01 03:44:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 1a38f46d-e351-3c31-97c2-d7f88a68fbc2 | -21.61823 | -48.4679 | 2025-03-01 03:44:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d96ccb85-8f46-33bb-9455-ad3f2efef0cc | -21.64902 | -41.02932 | 2025-03-01 03:44:00 | NOAA-20 | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1b3f55fc-299c-31a7-b07d-51704517fde4 | -22.90322 | -43.75315 | 2025-03-01 03:44:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 4709dcb2-216b-3c42-9a12-09c46a1f0757 | -21.65453 | -44.20003 | 2025-03-01 03:44:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d0a0ba49-68f9-3402-a4b5-dc383c55459b | -16.07631 | -46.61559 | 2025-03-01 03:44:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f6d40bd3-e734-308a-b441-c1277739f523 | -20.25415 | -50.79255 | 2025-03-01 03:44:00 | NOAA-20 | SANTANA DA PONTE PENSA | SÃO PAULO | Brasil | 3547205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 975b9623-978e-3fe5-8edd-8fde7f816503 | -17.53845 | -42.28726 | 2025-03-01 03:44:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03f4a470-a242-3793-bc24-31c4eb324234 | -21.61142 | -48.47385 | 2025-03-01 03:44:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63699011-26a8-30ca-a961-7cd2893ef84d | -21.85678 | -45.42046 | 2025-03-01 03:44:00 | NOAA-20 | CAMPANHA | MINAS GERAIS | Brasil | 3110905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f7b4f45-fac3-369e-bac3-94730ca3673e | -22.67376 | -42.85712 | 2025-03-01 03:44:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e9f5afcb-282c-364c-b7e2-de91be566bd3 | -22.24357 | -45.92431 | 2025-03-01 03:44:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3f8d942e-fe66-38b3-a88e-a2fb86e3ceea | -22.55927 | -43.62653 | 2025-03-01 03:44:00 | NOAA-20 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0ab732ec-bb6a-3fdb-8fbd-cb26187694d9 | -22.81922 | -43.34435 | 2025-03-01 03:44:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c8bc9d9d-9ca8-3f8c-86e8-45b17f35952e | -22.78517 | -43.75692 | 2025-03-01 03:44:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f96a1380-7ed3-3ef4-ac6e-7bc3a44d5acd | -20.04311 | -40.9444 | 2025-03-01 03:44:00 | NOAA-20 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ad96da8a-7db8-3f8a-86f7-2ee9914d14b5 | -21.6122 | -48.47033 | 2025-03-01 03:44:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d45ec4f5-4aae-364b-89e1-2c3f11b884f7 | -19.69994 | -44.77267 | 2025-03-01 03:44:00 | NOAA-20 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1c62965d-3b73-3fd2-bc3f-6a83411c875d | -21.65854 | -44.20087 | 2025-03-01 03:44:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 15cc795d-ada5-3f08-91d8-9ae5ff7a9fb8 | -22.94434 | -42.77246 | 2025-03-01 03:44:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b2d605ee-d43f-3173-8e72-2cc54306b6b3 | -20.0438 | -40.94037 | 2025-03-01 03:44:00 | NOAA-20 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d24c0f20-a47b-30f2-9ded-3fc45c653455 | -21.54784 | -41.82388 | 2025-03-01 03:44:00 | NOAA-20 | SÃO FIDÉLIS | RIO DE JANEIRO | Brasil | 3304805 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76f01aa1-1586-3ee7-8e17-4169159a03f7 | -23.98547 | -48.91886 | 2025-03-01 03:46:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 709f13f9-553e-3d2d-a0bd-750b5b60517c | -28.5855 | -49.44156 | 2025-03-01 03:46:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1e2477b4-6795-3fec-a3ff-c11d7ba0f45e | -23.33904 | -46.7714 | 2025-03-01 03:46:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 191d8408-241d-393d-93a9-04da65357791 | -23.3387 | -46.77403 | 2025-03-01 03:46:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 73bb6593-d359-3be4-b575-0a2b7c5a4d3c | -23.05883 | -47.8494 | 2025-03-01 03:46:00 | NOAA-20 | LARANJAL PAULISTA | SÃO PAULO | Brasil | 3526407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| acd315c7-8667-37e9-8728-08579f2234d9 | -3.01327 | -54.57176 | 2025-03-01 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 116e2db8-6076-30ff-b646-bb4494be0165 | -3.01244 | -54.57683 | 2025-03-01 04:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3671a0e-b6f4-3652-8f7a-2aea2a7c589d | -9.26015 | -60.31347 | 2025-03-01 04:33:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 965d3a1a-bac5-3a4b-90c5-38fa8763efce | -12.51807 | -45.49667 | 2025-03-01 04:33:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9636fd11-5a47-3b30-af1b-41bb9963a931 | -11.85367 | -52.25911 | 2025-03-01 04:33:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98fa021c-71bb-363d-87f3-843fad57d9ff | -15.37571 | -43.72416 | 2025-03-01 04:33:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 4508cee3-f2a7-3b61-9297-9bd9c2d02816 | -15.3782 | -43.72165 | 2025-03-01 04:33:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| d7008b31-6a23-3928-bccb-0a10d7630121 | -14.03885 | -41.45561 | 2025-03-01 04:33:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a46a2d4a-4e29-3b54-8f73-e7258ef67f68 | -15.37624 | -43.71992 | 2025-03-01 04:33:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e878bb45-637c-3d7d-8030-4bf027e17ca5 | -9.8017 | -37.94897 | 2025-03-01 04:33:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5017af46-994c-395a-8ed7-4f56099b2907 | -15.08004 | -48.94342 | 2025-03-01 04:33:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92cd9d8a-3e04-391e-9ef0-d038e55ea5ab | -12.51435 | -45.49612 | 2025-03-01 04:33:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32bad47c-ac8c-35ed-9f49-a1b5d089288c | -14.27958 | -47.41282 | 2025-03-01 04:33:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5605edcc-1b46-3fe8-99cf-7186a9db7e80 | -21.61104 | -48.47261 | 2025-03-01 04:36:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 03e7c2ad-7d76-3036-b1a1-c644b112e011 | -19.87546 | -54.66387 | 2025-03-01 04:36:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 235f5d17-2c4b-3218-bba3-7a15ae6f2681 | -17.98084 | -47.22112 | 2025-03-01 04:36:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1c6c9be-49e7-361e-8f0d-2ac8db0410f9 | -22.12598 | -43.90019 | 2025-03-01 04:36:00 | NOAA-21 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1a1cab39-c595-3511-8476-03034b9e3614 | -17.42152 | -46.56428 | 2025-03-01 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1d211dc-9ec4-36f4-b9f8-920132a07b1c | -20.31153 | -45.58358 | 2025-03-01 04:36:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6aeb7bf5-4191-3648-8af9-5fc63b6ba009 | -17.32737 | -53.73748 | 2025-03-01 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8631a3ca-41a1-30c3-9094-648991ead7f8 | -21.61871 | -48.46956 | 2025-03-01 04:36:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 49177363-6701-3062-b599-b3d0c32c4014 | -16.07898 | -46.61523 | 2025-03-01 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bea162d7-65db-3b19-8524-f3d98580c100 | -21.61162 | -48.46835 | 2025-03-01 04:36:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0d169cac-de7f-3a66-9887-7ff1c9375c14 | -21.65637 | -44.20103 | 2025-03-01 04:36:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d0556247-168e-3399-bc42-4a5945a2685b | -20.98399 | -43.03937 | 2025-03-01 04:36:00 | NOAA-21 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b0f6cb3-c932-36a4-818c-b794f6566eb0 | -19.24393 | -46.70116 | 2025-03-01 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38b56f7d-ebba-30dc-85e3-13dd379a4387 | -21.19507 | -44.93715 | 2025-03-01 04:36:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 15602897-fbc2-37ad-9d07-248760d74a9c | -21.6193 | -48.46529 | 2025-03-01 04:36:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc3b71e9-5319-3340-a873-bb2645004416 | -20.76587 | -46.76817 | 2025-03-01 04:36:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a53ebba1-3d77-3c7c-b306-0037ace7a366 | -16.07529 | -46.61668 | 2025-03-01 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9091d521-4540-3b84-aa5d-b8a3fc360960 | -17.42587 | -46.56018 | 2025-03-01 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 024644fd-4141-3438-ba25-50e4c3e22558 | -17.69863 | -47.43185 | 2025-03-01 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7f4e4b8f-6e94-3b21-937b-487fce64d914 | -20.99565 | -51.79151 | 2025-03-01 04:36:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8f8be344-1f09-3c01-9dd9-4b3602e90286 | -17.42215 | -46.55964 | 2025-03-01 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1c0c821f-ef63-309f-8d6a-eae596e162c7 | -15.56957 | -47.85738 | 2025-03-01 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 365e6e1a-94fd-34c1-aad8-4bf0b012693f | -17.69642 | -47.42915 | 2025-03-01 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a360453a-c0c8-3b40-85eb-0299b945c924 | -17.33097 | -53.73814 | 2025-03-01 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eba85cad-375a-304d-b50c-5bc5a2ee1e9f | -15.20797 | -51.18115 | 2025-03-01 04:36:00 | NOAA-21 | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 422d2ebd-754a-3d74-bfed-099eecd9265f | -17.33531 | -53.73453 | 2025-03-01 04:36:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41998b6f-3e07-3867-98b6-0728e30cfc2d | -16.07532 | -46.61472 | 2025-03-01 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ace8ca67-4dc4-3b72-8e34-f5c9d7662f29 | -22.83406 | -42.77085 | 2025-03-01 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| be87cd87-5a6f-38aa-8f61-4b0fb40af1b0 | -23.50423 | -45.41865 | 2025-03-01 04:38:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8071e6d3-0fa6-3b3b-b156-eda44ea53aa5 | -23.40746 | -46.55595 | 2025-03-01 04:38:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0fa9eea0-3a19-343e-bebc-9c6152176339 | -22.83437 | -42.76772 | 2025-03-01 04:38:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 1f63999c-30c5-3961-9f26-b53b0a9a61fa | -24.2427 | -50.7407 | 2025-03-01 04:38:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ef56f587-cccb-3b76-be8c-ab3d5d9f72db | -20.88157 | -54.78608 | 2025-03-01 04:38:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65bc13bb-4741-37a9-9757-7f7e64fe458a | -22.5421 | -48.81208 | 2025-03-01 04:38:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53eaaeaf-1a02-3c46-b39a-39807167300f | -22.24717 | -45.92466 | 2025-03-01 04:38:00 | NOAA-21 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README3.md)
