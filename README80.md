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
| bdfb698c-83ee-36e4-8ce2-8328ffacccfb | -3.49758 | -42.14258 | 2025-10-29 12:17:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 0c844598-ac7c-3cfc-bff3-2ab96f3ad171 | -6.67632 | -44.69144 | 2025-10-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 2af49b9b-676d-3164-ad5f-529124a5f5ac | -6.27805 | -41.82602 | 2025-10-29 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 20.8 |
| c2b405a8-fc11-3a8c-b0fa-46c03080a36d | -6.09819 | -42.43905 | 2025-10-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 35.0 |
| 627a1d79-29f5-3656-8589-aa82e9b618f8 | -3.81992 | -44.96898 | 2025-10-29 12:17:00 | TERRA_M-T | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6a5e1988-f429-380b-9921-8097e15b0581 | -7.03279 | -44.92136 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ac1e10a4-bf56-36ac-a5b8-2f5600a72f67 | -6.50151 | -38.03482 | 2025-10-29 12:17:00 | TERRA_M-T | SANTA CRUZ | PARAÍBA | Brasil | 2513208 | 25 | 33 | nan | nan | nan | Caatinga | 59.2 |
| fa25dc91-7a80-3aab-876e-4b92fd48d49f | -7.07191 | -44.94498 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f75b3b6a-633c-3a32-aa57-570deb6f9250 | -3.66689 | -44.19321 | 2025-10-29 12:17:00 | TERRA_M-T | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| a9b4b4fa-5c90-3e82-88d4-2a1233dd2fd5 | -5.96107 | -46.31829 | 2025-10-29 12:17:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 9ce71484-1903-397e-83d0-eca35eeca81c | -4.47906 | -43.42796 | 2025-10-29 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| f7142f37-3ee7-3b20-9051-889ea25e3c30 | -7.09818 | -45.25308 | 2025-10-29 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| deccb26b-f937-3f6f-82e3-3c848217b3ec | -3.86246 | -43.35913 | 2025-10-29 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 39bf5f9f-39f9-3166-a0ac-3a947b01b3c0 | -7.31777 | -46.70134 | 2025-10-29 12:17:00 | TERRA_M-T | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0d89a0d4-1f50-3437-ab89-eb7918580da7 | -7.29075 | -46.89245 | 2025-10-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3c461e7c-688c-3e49-974c-e9ca089d712d | -3.49963 | -42.12745 | 2025-10-29 12:17:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 5aee681b-261c-37ff-8f80-d62cc9d2c4e1 | -6.1063 | -42.44667 | 2025-10-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| f9ff48de-15ac-3530-afdd-f83381c89792 | -6.16234 | -41.59662 | 2025-10-29 12:17:00 | TERRA_M-T | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 7052a281-1168-30ef-a3bf-b1c282e4d300 | -3.5054 | -44.76414 | 2025-10-29 12:17:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c6a6b55e-2efe-3f1c-98ff-6607d274ef6f | -6.87515 | -45.03861 | 2025-10-29 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 6e706825-77d6-31db-92e0-7b17e885faf8 | -5.63193 | -41.5468 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| caad90bf-d5b3-3af0-891e-c786214a8284 | -3.77207 | -42.48378 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| b156173d-b865-3d13-b49d-a4b481d3573d | -7.35656 | -43.90521 | 2025-10-29 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| cc2a476a-84a8-3ddd-8071-b8971d075763 | -7.3423 | -42.47282 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 281.9 |
| 521241e2-d4c2-380d-95a5-73daf108f67a | -6.10837 | -42.43068 | 2025-10-29 12:17:00 | TERRA_M-T | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 66fdb599-322c-36d7-af02-701d6e633471 | -3.87455 | -43.34802 | 2025-10-29 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 0c99de24-600a-343e-be38-da60e30d6b27 | -4.48189 | -44.29199 | 2025-10-29 12:17:00 | TERRA_M-T | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 99d5a09d-2ec3-3ca2-bead-c67cd5864b7f | -3.77407 | -42.46938 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b5e56302-2aa1-3973-b3b3-0d46fba8f290 | -6.88001 | -42.84888 | 2025-10-29 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 602641c1-6fa5-3e2b-aeaa-d3a4c8543744 | -3.51836 | -41.98893 | 2025-10-29 12:17:00 | TERRA_M-T | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| ce760373-0fc2-3ba2-9e13-b8b78ff89e9f | -5.23657 | -40.59232 | 2025-10-29 12:17:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 24.7 |
| 47680735-bf74-389d-b0ff-a0db74cccb49 | -5.24581 | -40.59995 | 2025-10-29 12:17:00 | TERRA_M-T | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 20.9 |
| e7beca5f-f62f-39cc-9447-1377f8d0b5cc | -7.42746 | -45.98651 | 2025-10-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 73e10e46-95df-32c0-9a0f-82c7e6e397fa | -7.30566 | -45.67578 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| aa310384-a9b6-3059-8db0-22d4a47ca35c | -4.46931 | -43.70892 | 2025-10-29 12:17:00 | TERRA_M-T | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 49.0 |
| f15da138-e758-372d-8019-798804ff2285 | -5.95978 | -46.32749 | 2025-10-29 12:17:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d41d2f10-7698-3f00-bf66-3d22f96750f6 | -7.14468 | -44.70504 | 2025-10-29 12:17:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 8d8e812f-077a-3c6b-b6f8-272800434c6f | -2.84786 | -43.67771 | 2025-10-29 12:17:00 | TERRA_M-T | MORROS | MARANHÃO | Brasil | 2107100 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c2754c57-077a-329e-a627-cd366d035aa2 | -0.98026 | -48.22698 | 2025-10-29 12:17:00 | TERRA_M-T | COLARES | PARÁ | Brasil | 1502608 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 387f9f06-e291-32fe-9351-962eb2b71bcd | -6.54414 | -43.55673 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0588b897-cc14-3afa-9c32-31f5c724c170 | -2.7615 | -45.39959 | 2025-10-29 12:17:00 | TERRA_M-T | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e104d935-1b9c-351c-8d3c-c515668c349d | -7.33052 | -42.47118 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 551ef7c1-a0ca-3cb5-821a-85538414f95b | -7.08163 | -44.94644 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 23c9d337-f38e-3b70-b125-d2a6bedcc6ba | -7.95554 | -38.6767 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 46.3 |
| 96e30062-2c5d-3073-8e03-c8995bf2d3a8 | -7.30425 | -45.68582 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 171e3619-89e1-3423-b261-1719615318c0 | -6.95559 | -40.91236 | 2025-10-29 12:17:00 | TERRA_M-T | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 26.4 |
| 9b50f7e5-649a-3a27-883d-0e4cfb09eb9b | -5.63613 | -43.92136 | 2025-10-29 12:17:00 | TERRA_M-T | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1e59098f-170d-32ef-819e-071730de18fb | -3.66889 | -45.18237 | 2025-10-29 12:17:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 18.8 |
| fd4c7f5a-1720-36d4-b804-8404ee5ed5c7 | -7.34602 | -43.90388 | 2025-10-29 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| b5668881-d395-311a-a9a9-c1c211ec8a39 | -4.56068 | -46.6922 | 2025-10-29 12:17:00 | TERRA_M-T | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 0ed70721-0392-3fdb-b9be-36c40f11113a | -2.32675 | -44.82615 | 2025-10-29 12:17:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 0e901227-9cc7-3642-8e21-cc9442ea159a | -4.48949 | -43.42939 | 2025-10-29 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 3e40d3a0-683f-3c5a-b483-c51c1ff89060 | -2.93921 | -44.03828 | 2025-10-29 12:17:00 | TERRA_M-T | CACHOEIRA GRANDE | MARANHÃO | Brasil | 2102374 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 937687c4-b803-320f-ac15-1a9a39eb56d0 | -3.67951 | -45.17393 | 2025-10-29 12:17:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5624f205-0a37-3922-94e8-d61a9ba7fef3 | -4.48772 | -43.44196 | 2025-10-29 12:17:00 | TERRA_M-T | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 439.7 |
| 3598f6a2-6e88-3192-967f-769c1c7174f3 | -6.95959 | -40.90692 | 2025-10-29 12:17:00 | TERRA_M-T | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 44.0 |
| ba41d70a-6828-39e9-8349-876a1f4a90e4 | -3.76293 | -42.46803 | 2025-10-29 12:17:00 | TERRA_M-T | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Cerrado | 350.6 |
| f0de3572-4290-3a57-97c2-262c0a15eafb | -7.43874 | -45.31342 | 2025-10-29 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e3977d59-be8a-3927-af76-adbf818f78f8 | -3.83824 | -40.67624 | 2025-10-29 12:17:00 | TERRA_M-T | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 26.6 |
| dcb6ae21-314f-327a-a741-280fe48d0da3 | -6.27422 | -41.8198 | 2025-10-29 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| aa0dc549-c304-380b-be82-19a0910b103d | -6.92244 | -45.50668 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 52af37ac-c16e-3d9a-a985-a5eb5546bcd0 | -7.61056 | -43.57798 | 2025-10-29 12:17:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b1db581c-2db3-3686-9147-c555c53f97cb | -6.05338 | -42.09468 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 29.4 |
| 1eebcd19-9ab1-399c-b275-34c2713c921d | -7.09944 | -40.71282 | 2025-10-29 12:17:00 | TERRA_M-T | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| dfc28449-ed5c-34e8-bb26-02fc2ffc570d | -6.88209 | -42.83373 | 2025-10-29 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| b60038f2-5cae-3734-af93-11ff8507ab66 | -6.43736 | -45.08843 | 2025-10-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 672df7a7-8e9d-31b0-972a-3e9c7f9a6c28 | -3.59587 | -44.84452 | 2025-10-29 12:17:00 | TERRA_M-T | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 696d075d-b10e-3af8-a1e0-a0fe3c44fa88 | -6.85781 | -45.16589 | 2025-10-29 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b1a253d1-6ecd-3c5a-89eb-6b15ecb6ee5b | -3.82057 | -42.79619 | 2025-10-29 12:17:00 | TERRA_M-T | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3576d596-a963-329e-9c94-a5bac4d1febf | -3.67813 | -45.18363 | 2025-10-29 12:17:00 | TERRA_M-T | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d00f5182-74ec-3c4e-8b80-4674677a22cf | -3.72861 | -41.56056 | 2025-10-29 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 8f1b6e29-4497-3df6-b821-e48e028cb385 | -7.31503 | -45.67695 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ebb946a8-1208-3f0e-a336-108200a9fb29 | -6.43879 | -45.07814 | 2025-10-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| d03a39b0-4352-326f-8824-643996b20d3f | -7.41748 | -44.65535 | 2025-10-29 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| d80b4ae0-38b4-394b-8c09-0595d63ebeb0 | -3.72626 | -41.57743 | 2025-10-29 12:17:00 | TERRA_M-T | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| f7752c2c-ee26-3b0c-9d38-8fd64adb04d3 | -3.90118 | -40.79107 | 2025-10-29 12:17:00 | TERRA_M-T | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 25.7 |
| 55cb0fd7-51bc-36c9-8f5a-313e4503cf5c | -5.63436 | -41.52859 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 34.6 |
| 221e4e43-f3be-3948-8082-44c2f115a1fc | -6.13311 | -46.99517 | 2025-10-29 12:17:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| bb252d5e-3b32-36e5-be55-233649eecc3e | -3.76494 | -42.45354 | 2025-10-29 12:17:00 | TERRA_M-T | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d57c5a1a-60d5-3994-8cd4-f4d4c9c08725 | -7.0735 | -44.4791 | 2025-10-29 12:17:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 325571d5-aed0-3a7d-804b-a2b331c0e7df | -4.52047 | -38.78436 | 2025-10-29 12:17:00 | TERRA_M-T | BATURITÉ | CEARÁ | Brasil | 2302107 | 23 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 0ad89fbb-bc20-3d1c-94cf-72b445ee9612 | -6.49476 | -38.00381 | 2025-10-29 12:17:00 | TERRA_M-T | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 56.4 |
| 0f978284-bf8e-3f25-9a22-8661665b2bde | -6.88066 | -42.83945 | 2025-10-29 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.9 |
| 663c9b2c-1159-3ca6-9e5a-3b9a9df62c25 | -6.13185 | -47.00406 | 2025-10-29 12:17:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| cbd755de-ddc9-362d-81e1-8c8e7eda7c6f | -6.12925 | -41.84832 | 2025-10-29 12:17:00 | TERRA_M-T | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 19.1 |
| e463e3fb-3c9b-3788-b757-3527c4128db9 | -5.41184 | -46.28941 | 2025-10-29 12:17:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 49719213-ccf6-3c7d-99a3-688e47779059 | -7.60794 | -43.57111 | 2025-10-29 12:17:00 | TERRA_M-T | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 3c976f53-f127-30e6-985d-5ed081f662e6 | -4.90428 | -42.00586 | 2025-10-29 12:17:00 | TERRA_M-T | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| f3e30850-9e14-3017-a34b-ca8f5aa14eb1 | -3.87285 | -43.36054 | 2025-10-29 12:17:00 | TERRA_M-T | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7e88d636-e4a9-32fa-a97f-d4fe4449de74 | -6.88482 | -45.03984 | 2025-10-29 12:17:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 25c869a9-b40d-3dbc-9c9a-1d9bb2a6bc02 | -6.42924 | -45.0766 | 2025-10-29 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 31acd30f-6c0c-369c-a820-24f02a64860c | -7.13051 | -46.97733 | 2025-10-29 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d9cbc67f-7416-3fe6-849b-38a9a4f09f57 | -7.42882 | -45.97677 | 2025-10-29 12:17:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| f0dba831-2fa0-3c0a-9dfb-adf4c45a2444 | -10.11444 | -46.60972 | 2025-10-29 12:19:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 677eb736-ca47-3a7c-92ca-fd8f051aac37 | -7.99842 | -47.23332 | 2025-10-29 12:19:00 | TERRA_M-T | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e0d3cda-8c0d-38e9-b405-09da1f54063d | -10.23498 | -49.83025 | 2025-10-29 12:19:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 81adc144-6c99-373e-bc96-8babac031231 | -11.57713 | -47.94719 | 2025-10-29 12:19:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8fc9065f-6bad-3c5b-852e-221efeb31dd6 | -13.94704 | -48.47157 | 2025-10-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 20.4 |
| bb4c4a0d-0857-3b0f-bfe0-de7b412d87a1 | -14.42906 | -47.8482 | 2025-10-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 367a8798-b8e9-3243-bb7a-f346c74b5179 | -11.33682 | -46.06918 | 2025-10-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README81.md)
