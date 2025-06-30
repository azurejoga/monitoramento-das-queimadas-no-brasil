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
| 5cd25cdb-554c-3bb1-95f1-217d318c7e95 | -12.76761 | -44.40545 | 2025-06-30 00:41:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bbb0a554-198c-311d-9b8a-1cc6bf804d38 | -10.2949 | -57.05774 | 2025-06-30 00:41:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| f9cdfc5f-768d-38a5-b93e-8f68f512b4d1 | -9.23738 | -58.7683 | 2025-06-30 00:41:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 6594001c-fcd3-329f-8218-1d5d05c6d012 | -10.54926 | -52.05116 | 2025-06-30 00:41:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| ec9ea060-88d0-3953-97fc-6d7ad62a2cc1 | -8.55087 | -48.26286 | 2025-06-30 00:41:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c7e8b7bc-5dc7-3d9b-a929-4ddebf929540 | -11.02267 | -56.27026 | 2025-06-30 00:41:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 00f4dee4-adf1-37eb-8095-cdb44fc195a9 | -10.87601 | -53.7837 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 73b43731-0711-37b1-8fb0-96347cb19716 | -11.81231 | -57.36386 | 2025-06-30 00:41:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 00de1a0c-8370-3a7b-946f-cbc74408ef73 | -10.64943 | -44.49146 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| cb0634b4-9d51-3e25-9576-b9a9c18a5b7e | -11.20665 | -55.92839 | 2025-06-30 00:41:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 26.1 |
| bc5d8598-4063-3ff7-bbfc-cba4959bd3fb | -12.6216 | -54.23087 | 2025-06-30 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 712066d7-4c4c-3526-ad1d-11628184dcd6 | -10.87407 | -53.76842 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 37.3 |
| a7b6407a-8c78-392d-941c-4ccd5aeacc37 | -8.65234 | -47.80888 | 2025-06-30 00:41:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b3383a80-e83e-3fa3-9b62-314825a479b2 | -11.93039 | -57.46928 | 2025-06-30 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 9a706558-342d-37d2-8911-0e3d4a769498 | -14.433 | -45.17148 | 2025-06-30 00:41:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 561222a6-739f-3235-9d7f-c317961d7e21 | -10.86919 | -53.73253 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 59ed831d-b19d-312f-b1fe-86dc06dc98ab | -12.63155 | -54.21149 | 2025-06-30 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| ee676444-51cd-3042-ba7c-1306d151a326 | -11.94586 | -57.4674 | 2025-06-30 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d0b2d7d3-a3b6-30c8-af9c-bea875b52954 | -12.09958 | -54.66286 | 2025-06-30 00:41:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 0a3c960f-ed82-3f1f-ab20-4321789a81cd | -10.1079 | -52.18701 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 9f35498c-fc49-3c6a-809a-5a358750beaf | -10.8476 | -53.74095 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a8785e26-3905-3d87-81de-e7079c0611e4 | -9.09814 | -47.96066 | 2025-06-30 00:41:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| c240d697-7e74-356d-b0aa-d4d3e11155a7 | -12.09717 | -54.66872 | 2025-06-30 00:41:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 27.5 |
| f45a337c-fcb7-35d1-ae7b-225d0ac969b9 | -10.79668 | -44.25201 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fc38ca7d-04ef-3459-8147-6f5eb5873fe5 | -10.80547 | -44.23598 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 713c1bb2-32a4-3e18-974d-27d1917fd9c6 | -10.8608 | -53.75451 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 70558601-179d-3074-bf7a-06d911e38d56 | -10.4444 | -47.44868 | 2025-06-30 00:41:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 137cd6c6-513f-38e1-a1c9-2d88d955bf60 | -9.15786 | -51.33764 | 2025-06-30 00:41:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3faed360-62ab-307b-89cf-9481aea775fd | -12.06923 | -48.44512 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94e3c7dc-f1a0-361d-bb43-59861e53f22f | -12.75711 | -44.40716 | 2025-06-30 00:41:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 9eb7ecc1-25cc-3eab-9ead-7837d6dcb905 | -8.54191 | -48.26419 | 2025-06-30 00:41:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f8e75ce5-08c1-3647-a98b-7cd82b54879c | -9.08978 | -47.96814 | 2025-06-30 00:41:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 0941e853-e31a-32a9-aefd-63e086c0b53b | -12.06415 | -48.47337 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 0516054a-d777-31ca-aaef-77f529890da8 | -12.06164 | -48.4554 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 321c31a2-bd73-302d-b6e6-d105c7b82b0a | -12.06289 | -48.46439 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 94f44f6f-5df1-3455-b53e-3d685e45c37d | -11.92693 | -57.43852 | 2025-06-30 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 351ad7d3-e172-374f-9add-74d8aa8af6f5 | -12.63368 | -54.22934 | 2025-06-30 00:41:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| afc7d1e1-c0a0-3ed9-b825-ad54248da26a | -10.87099 | -53.74753 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 8434debe-a28a-3f2a-b365-aa2b30ab0403 | -10.87466 | -53.7781 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.0 |
| 74c53692-44cb-322a-946a-964bbb434be3 | -10.80767 | -44.25023 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1f481fb1-a2eb-3fa1-bab5-e5b60055be0e | -10.79446 | -44.23772 | 2025-06-30 00:41:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 308921b2-1f27-3b50-a8d8-211957c0c05c | -10.84948 | -53.75592 | 2025-06-30 00:41:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 67bea5db-4317-3586-9c83-be0f5402c94d | -10.54776 | -52.03974 | 2025-06-30 00:41:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 7d6f1475-7427-3d75-bbf7-ccde68d76064 | -11.94176 | -57.46136 | 2025-06-30 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 118.3 |
| dce4306a-01b4-3e55-9e0a-db8f2d4dc4cb | -11.94237 | -57.43667 | 2025-06-30 00:41:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 29e548b2-3c07-34b3-9610-bb6cdee69659 | -10.55767 | -52.0384 | 2025-06-30 00:41:00 | TERRA_M-M | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 2820c6bf-d66f-3601-8991-e1dc3d4344ee | -9.09947 | -47.96996 | 2025-06-30 00:41:00 | TERRA_M-M | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 86225f89-af28-32ce-b944-b89ef9d22412 | -12.06539 | -48.48235 | 2025-06-30 00:41:00 | TERRA_M-M | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 043cefa4-b611-3263-8bca-def401baa119 | -8.71495 | -47.8606 | 2025-06-30 00:41:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f310826d-9adc-3b0f-a32e-0989a32d5fbe | -6.64102 | -47.85867 | 2025-06-30 00:43:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1d367645-57b2-386f-817b-1e32636b3664 | -4.31362 | -48.07426 | 2025-06-30 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 13550f81-167e-3830-977a-9443c70966a6 | -5.56733 | -45.22305 | 2025-06-30 00:43:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2813eaab-a05f-381d-93a9-08d7c325cf15 | -4.48334 | -48.30802 | 2025-06-30 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9765dcff-8265-35b2-9d0d-df51c6516520 | -5.56705 | -45.21667 | 2025-06-30 00:43:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ff29dbc7-06da-3999-9f6c-905676b43334 | -6.44856 | -44.57022 | 2025-06-30 00:43:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 186708a0-1be7-3e32-831c-78e6aa1e53d0 | -4.31501 | -48.08427 | 2025-06-30 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ad687381-0594-3f1e-808d-2573e03b3fa1 | -4.32031 | -48.07703 | 2025-06-30 00:43:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 728b2880-43a6-39b2-bf33-1c81e03de4ab | -4.81373 | -47.32396 | 2025-06-30 00:43:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b4b5d6d7-ad7e-3bbe-b0a1-28ca4c7d3feb | -7.19396 | -45.32724 | 2025-06-30 00:43:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a8989f81-4d9c-3250-a900-b76fc6d173a1 | -9.2522 | -58.7584 | 2025-06-30 00:50:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| e4356afd-a8d5-3957-b506-e4be870a44fe | -10.805 | -44.2319 | 2025-06-30 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 6b344dc1-4d91-3e4b-871f-c520b58b120c | -11.928 | -57.4518 | 2025-06-30 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| b039902a-79ee-31e7-af4c-4ad375947773 | -10.8762 | -53.7408 | 2025-06-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 03f29856-5af0-3434-b86c-d1535118564d | -12.6128 | -54.2107 | 2025-06-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 341c4b89-43f6-328e-8fa1-8dd15b4d409b | -10.8573 | -53.7425 | 2025-06-30 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 650979af-83b2-3c5c-be9c-6d59a68a15ca | -12.6319 | -54.2087 | 2025-06-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 318c760f-2a72-3fa4-acd3-7749c9404627 | -12.6316 | -54.2293 | 2025-06-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| a6449429-dc87-3d04-9778-8e2e8d7ccdff | -11.9469 | -57.4503 | 2025-06-30 00:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 6990df65-c3d3-39aa-b2a3-f53af5b9730b | -9.2337 | -58.74 | 2025-06-30 00:50:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a6a8c38f-4989-3510-a316-288c98c2d468 | -12.6126 | -54.2313 | 2025-06-30 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| b4a123bc-5229-3b46-bbf2-f9bfba1383d9 | -11.9469 | -57.4503 | 2025-06-30 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| caf66715-efdb-3842-8b5f-dcbfea388912 | -12.6319 | -54.2087 | 2025-06-30 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 76.0 |
| dfb35f29-ddea-33cd-8122-65d90791e63f | -12.0708 | -48.4495 | 2025-06-30 01:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 49010964-0fa1-34d9-9477-8ed3185e2530 | -11.928 | -57.4518 | 2025-06-30 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ed1655ad-f798-3809-8864-dd9bbbc735db | -9.2337 | -58.74 | 2025-06-30 01:00:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 82aff15a-19d3-3008-b372-3d92c7b4d3ec | -12.0705 | -48.4716 | 2025-06-30 01:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 46.7 |
| ab403b16-87e0-374f-8d9f-680d08b30648 | -12.6128 | -54.2107 | 2025-06-30 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 010b4bee-b4d5-3a6a-b03e-d06b3e695a80 | -12.6316 | -54.2293 | 2025-06-30 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3975e983-7512-36f2-934e-eb41aeded429 | -9.2522 | -58.7584 | 2025-06-30 01:00:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| f488e160-a912-38a4-92a6-8f74e2314a24 | -10.8573 | -53.7425 | 2025-06-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 628fef3a-67bb-3ab6-ac31-a039fe30c11a | -10.8762 | -53.7408 | 2025-06-30 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7d3edb77-20c7-378a-a26a-6d45f27c11c6 | -12.0708 | -48.4495 | 2025-06-30 01:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 872d9d71-8d24-3db5-bda5-c349775831ff | -9.2522 | -58.7584 | 2025-06-30 01:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 10f0cdc2-7e81-380d-8726-4a44a841af20 | -12.6319 | -54.2087 | 2025-06-30 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 1a2da841-fa58-3d55-a83a-c353a19fb5f0 | -11.9469 | -57.4503 | 2025-06-30 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 8147f350-a13d-3ba0-bfaf-2d8b5ba51a53 | -10.8762 | -53.7408 | 2025-06-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| b046714e-1ee6-3e8a-91b8-1c91aebfdcdc | -11.928 | -57.4518 | 2025-06-30 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1a7bd771-fcd3-33aa-b278-cce676dc6650 | -12.6316 | -54.2293 | 2025-06-30 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| b07d61da-215d-3c45-95d5-4e8457136bef | -15.9921 | -41.9885 | 2025-06-30 01:10:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 3a9f0c3f-3db4-30d9-8e11-061a958423df | -10.8573 | -53.7425 | 2025-06-30 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 8199e0d6-76a2-3027-9a1b-5aa2b196f5ad | -10.5576 | -52.0499 | 2025-06-30 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9665a353-110e-33dc-b991-e304c7411c16 | -9.2337 | -58.74 | 2025-06-30 01:10:00 | GOES-19 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| bc255df4-39a5-338e-8e7b-eb73ea0d6dd1 | -12.0705 | -48.4716 | 2025-06-30 01:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 18d040c5-b4bb-34b9-b95a-946c67ca07c7 | -11.9469 | -57.4503 | 2025-06-30 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8699b7ad-6590-38da-8e2f-c93e22f62c4c | -12.6319 | -54.2087 | 2025-06-30 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ddb92909-fda4-32d8-8b62-c21aab8f929d | -12.6128 | -54.2107 | 2025-06-30 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 742d1ee8-ec95-317d-b8cc-3e2da63891cb | -12.6316 | -54.2293 | 2025-06-30 01:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 047c8336-db92-3327-9508-94b9d5ad6539 | -10.805 | -44.2319 | 2025-06-30 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 06e6d276-2eb3-302b-a89d-aa4dc4b6dac2 | -10.8573 | -53.7425 | 2025-06-30 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| e00723d2-8f7a-38e6-85ab-de033e7efe3c | -11.928 | -57.4518 | 2025-06-30 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |


[Clique aqui para ver as próximas entradas](README3.md)
