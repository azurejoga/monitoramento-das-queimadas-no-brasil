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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ef5dde4-080f-3b73-9f8c-243806878bde | -22.76526 | -45.78533 | 2025-09-30 03:51:00 | NOAA-20 | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4bfa670-e466-34ee-844b-c749c1d1e881 | -22.5228 | -44.60484 | 2025-09-30 03:51:00 | NOAA-20 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 11.5 |
| 9e66ba7f-be10-3fa9-8ab0-fcd153d9e626 | -21.04597 | -45.6866 | 2025-09-30 03:51:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 83ed8fac-41a3-37f8-8133-0254f155546d | -20.41982 | -43.34909 | 2025-09-30 03:51:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 36f2f801-b497-3d3d-89ee-2ca367280e6d | -21.62015 | -44.06056 | 2025-09-30 03:51:00 | NOAA-20 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f482fddf-d9fa-3579-a6a4-3f56519542b7 | -23.15904 | -45.73034 | 2025-09-30 03:51:00 | NOAA-20 | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| cd5405e4-a9dc-34d6-8a7d-b35754296532 | -21.89055 | -45.75269 | 2025-09-30 03:51:00 | NOAA-20 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fea49b5c-1dff-33f1-9fe5-98543a5df3fb | -22.33551 | -49.48309 | 2025-09-30 03:51:00 | NOAA-20 | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f6f9dcb5-ad27-3a4f-80ae-121af0792f6e | -10.1847 | -44.917 | 2025-09-30 04:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 4e8bed53-f2df-3fb4-82ea-334b4c97e542 | -10.1851 | -44.8939 | 2025-09-30 04:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 184.0 |
| 83d2464b-6937-3b13-8f7e-a9a84b9f9473 | -11.1735 | -54.1242 | 2025-09-30 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| fbb59401-2a3b-349a-852e-55296b59d2c1 | -11.7712 | -44.7432 | 2025-09-30 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 77d215db-cef0-334d-969a-9defec4775a4 | -14.5137 | -48.4522 | 2025-09-30 04:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.3 |
| c62f894e-6e29-3012-a3c4-a7a96449ffee | -11.1548 | -54.1054 | 2025-09-30 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 3a3cf62b-5fca-3c7d-8747-fc3fb709cf08 | -5.5241 | -43.8878 | 2025-09-30 04:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 7da37b3a-2dfa-3672-9abb-88ffb3b1c5f1 | -13.2158 | -50.95 | 2025-09-30 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 241.2 |
| ee7d252f-db23-3ba2-b1db-0614e08c0128 | -11.1546 | -54.126 | 2025-09-30 04:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 206.0 |
| 36db5e49-adbe-3101-adcc-7b2b99499ed5 | -10.2041 | -44.8915 | 2025-09-30 04:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 53ab0e1d-2775-3526-8153-a2950743dfcf | -10.1855 | -44.8709 | 2025-09-30 04:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| ce4e5da6-40d4-3dc1-b951-760b08181156 | -13.2353 | -50.9261 | 2025-09-30 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| fab032b8-e23e-3e4a-96a5-c5025451256e | -13.1966 | -50.9525 | 2025-09-30 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 0aa91de0-6912-3f9f-b7e8-cde88e0263b6 | -11.7519 | -44.7461 | 2025-09-30 04:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| b900ca75-43e6-369c-b53a-50d2879eeb87 | -13.235 | -50.9476 | 2025-09-30 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 2d6f7668-7693-37e3-a0c2-e6c544cd9e1c | -13.2161 | -50.9286 | 2025-09-30 04:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 1273008f-f226-3e26-866e-0f99bad63003 | -11.1735 | -54.1242 | 2025-09-30 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| dbc03460-09ea-34d2-84ad-9886555d9659 | -10.1851 | -44.8939 | 2025-09-30 04:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 194.6 |
| 57fb5666-623e-3171-80e9-e693a6cb9838 | -10.2041 | -44.8915 | 2025-09-30 04:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 07bf887b-1f8a-3864-855e-1456b38c4d42 | -22.5205 | -44.597 | 2025-09-30 04:10:00 | GOES-19 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 81.3 |
| 9708e23d-c4e3-38d3-a341-42807a80b055 | -13.235 | -50.9476 | 2025-09-30 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d3d9673e-fe20-3ee5-9c76-40b95645cd41 | -12.8429 | -47.0063 | 2025-09-30 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2236ff40-d294-3ef0-89b0-db6e731e3000 | -13.1969 | -50.931 | 2025-09-30 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 6eb3f400-aebe-34a1-8ec1-d16d28549cf3 | -10.1855 | -44.8709 | 2025-09-30 04:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| d0b431d9-cb8d-3b99-bbdb-67dbb09f1b0a | -14.7465 | -45.6656 | 2025-09-30 04:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 2d6c1c42-b4d1-3dee-9929-358de50d08ba | -13.1966 | -50.9525 | 2025-09-30 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 10c6eb86-7f8c-3840-9e9c-392ff4332c75 | -11.1548 | -54.1054 | 2025-09-30 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 4ccde629-c92a-3ad1-a65f-e212355718e6 | -11.2516 | -47.226 | 2025-09-30 04:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 0c92661f-6aa5-3c33-af67-d30062a79304 | -13.2353 | -50.9261 | 2025-09-30 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a799e49d-3332-3bb7-b776-0023ea3661ed | -13.2161 | -50.9286 | 2025-09-30 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 307.3 |
| ce9d7c16-04ea-32b3-95c2-2ea52fdaa5e1 | -11.2513 | -47.2484 | 2025-09-30 04:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b94edce1-be6b-38da-a662-a7ea684d55d1 | -13.2158 | -50.95 | 2025-09-30 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 354.6 |
| 8cc2d50f-718a-317a-87d6-8e5e15ee2f99 | -11.7519 | -44.7461 | 2025-09-30 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 5cec108c-98ce-3bd1-a681-4bc656fb6599 | -11.1546 | -54.126 | 2025-09-30 04:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 192.5 |
| 7971a187-97cd-39db-a386-97ca30cd3f1d | -11.1735 | -54.1242 | 2025-09-30 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| fa78db6d-ec23-3162-ac03-cd11fb5e3c2d | -13.7703 | -54.7265 | 2025-09-30 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 5e9a5a25-d7ba-3187-9ce9-29d2dda65ae9 | -11.1546 | -54.126 | 2025-09-30 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.4 |
| 161e4100-fb8e-34f8-b513-fe1e3a664353 | -13.1969 | -50.931 | 2025-09-30 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8338e001-ffb9-37b7-a06e-e8e63214fbc9 | -13.2158 | -50.95 | 2025-09-30 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 159.3 |
| e5e15232-6df9-30a7-84fb-e3ee974d8c75 | -12.8429 | -47.0063 | 2025-09-30 04:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 5a9f5153-3709-305a-a2ec-b8afd91ba903 | -11.1737 | -54.1037 | 2025-09-30 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c6535843-4cdc-3563-9580-9160af12443a | -13.7511 | -54.7286 | 2025-09-30 04:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 18a0c1ab-8eb1-3659-b1c2-4530850ad5ce | -13.2353 | -50.9261 | 2025-09-30 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.4 |
| a46af8c5-fb51-3997-8621-b6573e3f7c74 | -14.5137 | -48.4522 | 2025-09-30 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 939d6780-d63c-37d4-b78e-e6fe20f04ef5 | -13.2161 | -50.9286 | 2025-09-30 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 475.0 |
| 872935d9-f614-399a-9e26-9e0d7652f26b | -11.1548 | -54.1054 | 2025-09-30 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| ae1341a1-f1dd-3939-9488-4b1555cefb38 | -14.5327 | -48.4715 | 2025-09-30 04:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| f32713cf-e53e-3346-9403-3116348f87ce | -11.1735 | -54.1242 | 2025-09-30 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ad89ec17-3cbc-3569-b58c-48b180133327 | -11.1546 | -54.126 | 2025-09-30 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 180.9 |
| e0c0c61a-fb96-3fcb-a4b9-89123831d6d7 | -13.7703 | -54.7265 | 2025-09-30 04:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d291ae91-dd5c-3dbb-9e49-0e47d34e0467 | -11.1548 | -54.1054 | 2025-09-30 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| b55ef52d-4c75-310a-93b8-e3f1ab8c6a53 | -6.25786 | -43.65831 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f84257a-f4ad-35fc-875f-00e1d1ab1a5f | -4.97959 | -50.64083 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38577a9-167d-3bef-a737-91a4d5580849 | -6.4556 | -45.91584 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a99649ab-2152-33d7-9590-030b45992d5a | -4.07403 | -48.04184 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8acf18f6-32de-3209-97b6-232cde844d66 | -4.39566 | -44.39949 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d026a0d5-4ed5-37bb-845e-bb0a495d9790 | -5.25469 | -44.45612 | 2025-09-30 04:38:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 68b79488-4643-37f3-8ecc-03333294326f | -7.30445 | -42.84328 | 2025-09-30 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8cf5ea2b-7776-31b0-98ac-1cf03fb88f70 | -5.31475 | -49.53381 | 2025-09-30 04:38:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80364803-379f-38a4-92ed-a8890eb81ee3 | -4.25593 | -48.55689 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41ac35c7-8d7a-3758-9ed7-5ed218538286 | -6.14943 | -43.9006 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9e055cb-1d09-32de-806d-7faa237603a1 | -6.40874 | -43.75218 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6f20a3f-ec3a-34e0-bddc-8a89e86aa1cf | -5.81992 | -44.99553 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a38e01e8-2f6e-33fd-ba1d-3aba6eb5ac18 | -6.50147 | -44.11719 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bba060e3-93fa-33b0-ad81-8f4ff461e15e | -3.10438 | -47.01505 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72435990-12ba-391e-ab1d-539aef3415c6 | -5.51611 | -43.87938 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4171e8a1-c3e5-333d-ba7d-09737ab1308d | -5.02938 | -42.98778 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 453736f8-c72b-3b2d-8e48-5236076ebae5 | -6.70711 | -44.56 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9bef995-ce6b-3b2c-b7af-5558e51a15a2 | -6.20389 | -44.21266 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f4df96f-e944-348b-b15f-212f9950b4c2 | -4.81826 | -42.77215 | 2025-09-30 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d20548d-9d76-3005-83da-c97af8b95c5a | -6.20896 | -44.2065 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a8b37b2-eb65-3770-8d9f-d9febf28d765 | -0.9086 | -47.54563 | 2025-09-30 04:38:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 599d6664-3a2b-3bbf-aa22-48607097f685 | -7.01576 | -44.4697 | 2025-09-30 04:38:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c3b934e7-6917-3090-bcf0-755fdb601f93 | -2.07594 | -56.87559 | 2025-09-30 04:38:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a5daf9c-bb42-37f6-b208-669b7bf14377 | -4.62553 | -43.5444 | 2025-09-30 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cf6cca51-6892-36d9-83d2-39de2892f271 | -5.88833 | -46.27974 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22c83d05-1b23-353b-a5a4-1815e727a6bb | -4.66959 | -45.69139 | 2025-09-30 04:38:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a8e7c0c-5421-3cf8-a38f-1abf7bafd944 | -4.6297 | -43.54501 | 2025-09-30 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c974220-ffef-3436-8f6d-0cc49013d93c | -5.50409 | -42.73262 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1a49e2c3-ce7b-3d5f-bde6-80bd54e27614 | -5.78116 | -51.75202 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddd97859-0430-3f48-a8a3-c499fea7a81c | -5.73689 | -42.68153 | 2025-09-30 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 016ec20f-530b-3fda-a78b-ff0513e626e5 | -3.80949 | -47.57908 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62d63e1d-419e-392b-b1de-c181aa6a45aa | -6.45523 | -45.9135 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac299b1e-5f7a-31a4-bf39-da5b0824e99f | -4.97973 | -45.29807 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de6fe973-7df0-326c-935c-bfe806283553 | -3.87431 | -55.40446 | 2025-09-30 04:38:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc2370fa-0182-30e4-8a96-74e27fc6876c | -6.37026 | -45.63763 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| de3c25c1-15f8-3a70-b194-c6695179c354 | -6.43467 | -43.07401 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bfc8b27f-a613-353a-91d1-93eb1b5176ac | -5.71193 | -42.87433 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 85f27c40-bbaf-36f5-8bfb-519504d37fc0 | -6.89952 | -44.52669 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fdc8a8aa-1002-3a94-9a01-e7dbe4274057 | -4.75199 | -42.70279 | 2025-09-30 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 593665ca-d32d-33ba-9ae1-78584f3e24ca | -6.47944 | -45.87697 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdce0280-2d2b-3714-8fe7-8bff4637b4b0 | -6.08038 | -44.06454 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README47.md)
