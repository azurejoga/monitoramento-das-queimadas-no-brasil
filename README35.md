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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac316ad7-6b65-31b1-ab25-b743e44174be | -8.90381 | -47.83062 | 2025-11-08 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 114d372d-66ab-3262-b37e-3730df04667d | -7.55082 | -41.66079 | 2025-11-08 04:57:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| eb91db37-cfdd-31f4-ab24-0a4144f14a0a | -7.03652 | -46.98175 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ccd2f224-09af-362a-b4fe-36bfdc5393e4 | -8.06697 | -47.12736 | 2025-11-08 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d0417bf-33b0-3298-b485-bb2d423a5cec | -10.37677 | -57.27448 | 2025-11-08 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29f397f7-d6b1-3da7-a877-4cb5faf1dbb8 | -6.00329 | -57.83113 | 2025-11-08 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc3a620f-23f1-3b1f-8792-deb99d045875 | -10.99149 | -53.98653 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 430b3443-113c-370b-b569-c6200f139c9e | -9.50025 | -66.77451 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72b1198c-c8ee-34bd-bb73-7d532c3c27cd | -5.00168 | -56.07093 | 2025-11-08 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57632067-c0e3-3845-8d38-8e7342ea412f | -8.0677 | -47.1221 | 2025-11-08 04:57:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08b88a85-d01c-3290-afdd-c9a4b67705a9 | -8.63025 | -67.0414 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89c6888f-0e7f-3d48-ad3a-c054466a204f | -7.4888 | -45.92613 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e734ed4-1d6f-3f13-b923-7b8287fa01f6 | -6.01015 | -49.13513 | 2025-11-08 04:57:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 58cdf97a-b994-3168-ae6c-b770e3eccc70 | -6.51935 | -55.03373 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 549c2db8-e0ff-3b7f-9128-78ea21125db9 | -4.36885 | -55.77257 | 2025-11-08 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b1cca63-9267-3728-aab3-630c984061e9 | -7.5508 | -47.2464 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 59ddef62-8a07-3363-b1ca-267e15322ca9 | -9.77417 | -62.50883 | 2025-11-08 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66ffbc1c-4af6-3370-bf10-e47631332fc7 | -7.79608 | -46.65496 | 2025-11-08 04:57:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 33463c4b-2bcd-38ca-95c3-2a4951c37e6f | -9.19823 | -62.39863 | 2025-11-08 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dfd742b-1050-3937-b236-9205f70bba5d | -9.079 | -61.69424 | 2025-11-08 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28db0dd6-3dea-3482-896a-642f08035d06 | -9.71203 | -61.29848 | 2025-11-08 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37e7085c-431e-3bbc-989f-246c1932e079 | -6.62372 | -55.01805 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78e7b671-e4ab-32cb-aa4e-cd0038d1f7be | -10.99429 | -53.99066 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86d473c6-f011-37c7-b48b-7a93f8b18c05 | -8.06295 | -54.96629 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5292a896-d670-372b-8c46-f7a244c51554 | -10.36562 | -49.87077 | 2025-11-08 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9ad87dc-c974-3f79-bd55-a4df34c8c893 | -9.76397 | -55.61721 | 2025-11-08 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fdca432-fc16-3221-8f7d-5bb9aeaa91b5 | -8.33118 | -46.25798 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b28376e9-9064-31c9-b4bc-28863aa814c8 | -9.99578 | -63.65392 | 2025-11-08 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 089b683f-7e8a-37d5-869a-a4d06f4a6eb9 | -7.80923 | -61.57125 | 2025-11-08 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d26d58c-167a-3e38-9999-b5ead2ae599b | -6.65229 | -44.48844 | 2025-11-08 04:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7b9cb5d-1485-3a2a-942a-b7dcdfa6a136 | -7.53458 | -47.38469 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28c1c4f7-9aff-3db8-bc40-f2213922df0b | -9.86444 | -64.89078 | 2025-11-08 04:57:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35ce4003-f9b8-3019-8b47-40095e3c00fb | -8.01638 | -61.52012 | 2025-11-08 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53bcda2e-87fa-3853-ab85-aaa03f1a1991 | -6.65343 | -44.48734 | 2025-11-08 04:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5497dec6-492d-3b12-8315-2a41a09c807d | -11.06028 | -60.88372 | 2025-11-08 04:57:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2f93760a-e54f-3022-85f4-a87b131a7544 | -9.92367 | -63.64421 | 2025-11-08 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdc7ccbb-1456-3540-815b-5b0767212cf6 | -9.3054 | -65.83251 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 497cb833-9ddb-3b11-b83d-bf5b01ad15df | -8.52466 | -55.03318 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3b400852-bc00-3853-be63-9c1506394cd4 | -10.99094 | -53.99013 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8383c51a-5402-3694-84d5-5ecb03e02432 | -6.8534 | -46.27 | 2025-11-08 04:57:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c199e2db-062f-386a-9114-407ae60fd24a | -8.43909 | -43.87228 | 2025-11-08 04:57:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e806a45e-a30a-3cf1-a857-85909ca28ea4 | -7.90822 | -54.82727 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b53c4234-feff-3eb3-a4f3-55d895ca0405 | -6.65292 | -44.49091 | 2025-11-08 04:57:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b1dff562-8890-3136-a935-ba31e19d1ee2 | -9.07981 | -61.68953 | 2025-11-08 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc95370-f907-389a-a8bd-1e172eaabc0f | -9.5992 | -54.72812 | 2025-11-08 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ed50d1c-717e-39d4-bdc5-0cec2e380f2d | -9.76341 | -55.62072 | 2025-11-08 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 756d0279-bb03-3534-b89f-20dc6a4ebdbe | -6.46813 | -43.27301 | 2025-11-08 04:57:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 44f0e7c4-b680-346c-8296-6315f5472a21 | -7.04049 | -46.98753 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7207044b-56e2-3537-862a-7cdc3c6da8e3 | -9.04576 | -47.00446 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 801c68b1-782d-346e-bbc6-3d72bfaff2e4 | -9.05207 | -46.99444 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bd6f80f-897e-3058-bf8d-50281c24f387 | -9.32429 | -47.83156 | 2025-11-08 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0148e83c-5e33-3e19-b948-d70b38c9ad9a | -9.44559 | -56.64148 | 2025-11-08 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9ef8e53-a28b-3688-9d82-027c50447d97 | -10.71124 | -48.54944 | 2025-11-08 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d1c3990-e347-3a9d-88df-51514286623b | -9.09424 | -44.32322 | 2025-11-08 04:57:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c5032216-7821-3d6e-b60a-072ec0dc1266 | -10.37494 | -57.27098 | 2025-11-08 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 334e56f6-3076-3129-87b6-c6920f6c5be0 | -9.94527 | -55.54546 | 2025-11-08 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43c2ad0d-65aa-355f-a558-b5918d081457 | -10.35648 | -47.33374 | 2025-11-08 04:57:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3eb8f2ab-2419-3785-8d57-b352a59f263e | -11.20065 | -53.8374 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c9cd1c8-5e48-3b23-818c-9ca4a3128ad5 | -6.85215 | -46.26858 | 2025-11-08 04:57:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65d30106-03c1-3384-a595-aca91ca4b439 | -7.31979 | -47.38315 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1909befe-d293-3696-a6df-39f2acc9717a | -9.55809 | -66.74385 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6bcd811-dc2f-3d5c-8f34-b29a7ea2bc49 | -4.88796 | -55.92612 | 2025-11-08 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3088814f-e92d-335e-b151-1a2147f1572d | -9.30621 | -65.82819 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b75765f3-87aa-341e-9381-2fe5b02a3fe6 | -4.49104 | -55.79903 | 2025-11-08 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12296c53-52a1-38a6-9b52-010628bd6bfb | -8.63014 | -54.55892 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 918a28c5-3c22-37d7-ac53-bfa0e2328435 | -11.20121 | -53.83376 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f067757-a8ab-3ded-aa04-c10a67495247 | -9.44194 | -59.2073 | 2025-11-08 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad82ad56-4c59-3061-bb0f-9b7d0f43d616 | -9.99519 | -63.65714 | 2025-11-08 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 642c2bab-8450-3f0b-ab98-4fe24e4cef4c | -10.99484 | -53.98706 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 889704e5-4e0f-3500-acb6-ae1b6dd62e65 | -11.19896 | -53.82592 | 2025-11-08 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2d380da2-5cee-3bdc-8f8f-8a6d7ebdd012 | -8.32573 | -46.26017 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b46c87cf-9f7a-3efe-8547-d3cde5b7fddc | -6.531 | -55.02481 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b837214-22a6-3e1c-b368-507c540d821b | -9.00828 | -51.11201 | 2025-11-08 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d971d525-88f5-35fe-a21d-012e536ab75f | -7.56762 | -45.8658 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 163ee45e-cc01-389d-92a4-311f412fafe0 | -7.08913 | -48.31178 | 2025-11-08 04:57:00 | NOAA-20 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 034ce637-9a73-31d3-8d35-9e36ecb513c9 | -7.48371 | -45.92535 | 2025-11-08 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10d57a0c-2bff-355c-93f1-c7af8e67569d | -7.53508 | -47.3875 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd79c3e5-b498-3ebd-8bec-34cba9a255f1 | -6.01416 | -49.13572 | 2025-11-08 04:57:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a98cba1-2159-3755-beb9-63a137b3ba43 | -8.63057 | -67.04036 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ee182fc-73bb-3bee-8369-6ebf5d78158c | -9.92425 | -63.6411 | 2025-11-08 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32549ae3-2b31-33e0-8ab7-8086a5d0ca20 | -9.50652 | -66.77578 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d714b42-e8b5-3642-b6b9-579d24229497 | -9.10802 | -48.9066 | 2025-11-08 04:57:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76ca9c1f-29ef-3417-b51d-e7badb580536 | -6.6204 | -55.01752 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5885cc48-457f-37e4-aed5-e3acef1f9378 | -7.52996 | -47.384 | 2025-11-08 04:57:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ee9f01f-7b60-3084-8a8d-56905519d76f | -9.9414 | -55.54843 | 2025-11-08 04:57:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47892105-9521-3293-a2ec-d88fd4a875e4 | -9.33351 | -47.83263 | 2025-11-08 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d1c3a08-e620-361f-9027-8c5343ab3201 | -8.32352 | -55.03688 | 2025-11-08 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3d2dc0f-678e-3cc2-bf41-b524c2872cf5 | -5.1843 | -56.11132 | 2025-11-08 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 895cf349-d5a0-3c61-a2ec-3065f1267b66 | -9.38199 | -50.72799 | 2025-11-08 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f83204e-2d82-38f1-9673-332e8482313b | -9.44219 | -56.64092 | 2025-11-08 04:57:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ff0c2519-5972-384b-9cb2-473eda89f5a6 | -8.62556 | -66.82143 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42a28fe6-1381-3e54-9f13-89629640b235 | -9.77508 | -62.50368 | 2025-11-08 04:57:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83d128ed-b867-37f9-aa3c-96d9ef96c6fd | -7.79061 | -48.53027 | 2025-11-08 04:57:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2eb5be3-cbcb-3a12-b51c-11df7b359d30 | -8.90444 | -47.82598 | 2025-11-08 04:57:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57c4129b-7b25-3fb0-b148-593623023a25 | -4.48701 | -55.80223 | 2025-11-08 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0402ed92-9bef-3406-ac5b-6afbc8e3c2c2 | -10.00025 | -63.65837 | 2025-11-08 04:57:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e5d26bc-a00f-36bf-a32d-43c0aac3c22b | -6.12719 | -52.64159 | 2025-11-08 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31ff6797-3a04-363a-9e13-96e0dfe35bf8 | -8.63671 | -67.04266 | 2025-11-08 04:57:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3116dcc2-8737-3ed8-b20c-3e7001a832a4 | -7.05149 | -49.29181 | 2025-11-08 04:57:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daf6c52e-6d54-34d8-88a9-c4c3a2e9d8c5 | -9.36941 | -62.29295 | 2025-11-08 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README36.md)
