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
| 0f7a8dc4-9822-3fe8-adda-8a7d57e8582f | -5.3849 | -47.2271 | 2025-10-04 01:20:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 81.1 |
| d1466656-1c22-3372-be9a-ebf91ae63447 | -10.3346 | -50.3188 | 2025-10-04 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 06c2816e-6ab1-337d-a5bf-837b2c52fcc8 | -4.9726 | -45.0683 | 2025-10-04 01:20:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| cf0d5f36-836d-3d10-8005-ba20925172ee | -18.17326 | -53.36259 | 2025-10-04 01:28:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 09fc78cf-ad51-3638-9098-4d0644758a9d | -16.38667 | -52.16368 | 2025-10-04 01:28:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 082114a6-f25a-3a04-93bb-ed11b752752a | -18.17592 | -53.35527 | 2025-10-04 01:28:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 09e14d43-f363-3493-a1b3-6c24ec4391af | -16.39412 | -52.15837 | 2025-10-04 01:28:00 | TERRA_M-M | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 40.2 |
| fb521199-8ea4-3d93-8618-db5c4f21da32 | -18.2375 | -53.3696 | 2025-10-04 01:28:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 53e35831-2c17-3f45-b057-c3beb15f5bb6 | -4.9541 | -45.0468 | 2025-10-04 01:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e9f5e4aa-94a4-3c08-abc3-4acb5ea7e51c | -4.4445 | -43.2397 | 2025-10-04 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a043bfbc-8245-3abd-9f78-2a76f03c98e0 | -4.6135 | -43.1361 | 2025-10-04 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 62f5e313-121e-3402-8733-3d9ced1261ea | -11.5072 | -46.7446 | 2025-10-04 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 1a5e2fa6-3583-3eda-a37e-037e9255517f | -9.3464 | -54.5201 | 2025-10-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 17146cb4-68d7-359b-a868-5745396494b5 | -3.8572 | -41.5719 | 2025-10-04 01:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| f8e37ef5-411d-3996-accf-070f37e9a0c1 | -5.3851 | -47.2052 | 2025-10-04 01:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 162.6 |
| 5f5ff37a-839c-38ae-b92d-acf05783634d | -2.9013 | -50.7351 | 2025-10-04 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 458af832-8456-3542-a482-2f9ad11ecde9 | -10.3343 | -50.3402 | 2025-10-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 26028c8c-6742-3323-8bb6-80c8f055a4c4 | -11.9151 | -46.3499 | 2025-10-04 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 79190f2b-c364-3291-926b-28d0af550fb8 | -11.8959 | -46.3526 | 2025-10-04 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| c3ad67ba-5c1b-3c6e-b1a6-61d334eae54d | -4.632 | -43.1583 | 2025-10-04 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 56073ca4-e4da-3b56-be92-a0d847a56b2d | -4.954 | -45.0694 | 2025-10-04 01:30:00 | GOES-19 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 164.0 |
| 335a23b5-9160-3da6-b085-1ff87ea74b0e | -16.0212 | -50.9425 | 2025-10-04 01:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 55e0680f-4d3b-36f6-9a95-228c432ca875 | -11.9143 | -46.3953 | 2025-10-04 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 59ce45ab-a238-3d35-9c7d-b4f8391f407a | -17.0903 | -46.2347 | 2025-10-04 01:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 959b7fd4-c655-3e90-a21f-6adf49f5c874 | -4.5946 | -43.1606 | 2025-10-04 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ea81c8f1-0e15-3022-8bb7-af5475361b61 | -6.8774 | -47.2334 | 2025-10-04 01:30:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| aa5252c4-28d5-39bc-9eb5-de18b2a0d5c2 | -13.3221 | -48.1439 | 2025-10-04 01:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 342a1295-2f68-3196-a242-4103fc420258 | -12.0502 | -45.2103 | 2025-10-04 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 133538b9-070e-30d3-8734-f79eb9b19362 | -4.6133 | -43.1594 | 2025-10-04 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 2645ebbc-414b-3b91-a600-f288ec37c0f4 | -3.8384 | -41.5729 | 2025-10-04 01:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 54.1 |
| 13b0f9d9-cde5-3f8f-bca7-4e0d230323d3 | -14.2321 | -46.0794 | 2025-10-04 01:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 66.3 |
| f12c47c5-2e8e-3d02-bf19-0747314efcb5 | -10.3346 | -50.3188 | 2025-10-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 113.0 |
| be94e319-ddc4-3fe8-afbc-dd181fbc9735 | -8.6322 | -54.9949 | 2025-10-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 88ff135b-6436-32ac-bff2-ea76e5ea4e81 | -5.3849 | -47.2271 | 2025-10-04 01:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 8093eafb-664f-3d53-a61f-4656ca0d1115 | -5.4849 | -44.0982 | 2025-10-04 01:30:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 625e489c-cd35-3203-9d5e-95ae5a8a63c3 | -9.3276 | -54.5215 | 2025-10-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| f58507fc-73e0-34d6-9f7d-bfa10d344caa | -5.3665 | -47.2063 | 2025-10-04 01:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| fa35367c-d8c8-3e9a-90c7-4b2652fdb0f1 | -5.1965 | -45.0768 | 2025-10-04 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 62850ab8-1073-3c25-af4e-4e52f03a7016 | -10.3157 | -50.3207 | 2025-10-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 389397de-a88b-37d6-8be0-751602c9aa86 | -10.1618 | -36.2726 | 2025-10-04 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 34d8bae0-2009-3849-9638-21a92275c3c7 | -4.4443 | -43.263 | 2025-10-04 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 546abe5c-1e66-3697-a337-cd59643a666c | -11.9147 | -46.3726 | 2025-10-04 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 276.6 |
| f5cbb523-e9de-3f1a-bb02-a178b5bcadde | -14.2515 | -46.076 | 2025-10-04 01:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| e1d03c0c-8cd0-3d3d-af5b-e8651333fd7c | -5.4847 | -44.1212 | 2025-10-04 01:30:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 27fb542f-5370-3863-b568-c78b3160e87d | -13.3225 | -48.1216 | 2025-10-04 01:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 1471309a-1a46-374e-8533-3904faed1c1c | -5.1967 | -45.0541 | 2025-10-04 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 1795b12e-685f-3100-8530-1895a298e58c | -10.1811 | -36.2691 | 2025-10-04 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 66.7 |
| 971ed596-bbd6-3ec6-96ea-ee7665035842 | -4.4446 | -43.2164 | 2025-10-04 01:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 818db2cd-8119-38bf-bbd1-0b9e8a1a6c7e | -11.9339 | -46.3699 | 2025-10-04 01:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 32c92068-9be2-3e68-abaf-31805dec26b4 | -12.0507 | -45.1872 | 2025-10-04 01:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 37b007b8-3e91-3e27-913e-8189320e0113 | -10.3154 | -50.3421 | 2025-10-04 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 6a9f96f1-d3de-30f4-ad20-ff18a590aed6 | -14.03702 | -53.92854 | 2025-10-04 01:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 41.9 |
| 59d4f240-c9bc-3e97-9637-9139a3b0e13d | -14.0415 | -53.95086 | 2025-10-04 01:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 5a3fc8d7-88ac-3bcf-85f4-a609d72a4b9d | -12.38329 | -54.46841 | 2025-10-04 01:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 307cb4af-5ec6-3603-9899-ca293e43fa3e | -15.22441 | -56.82084 | 2025-10-04 01:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 32.8 |
| d432d2aa-c3f5-3a69-8a77-8956b7469091 | -12.38327 | -54.4629 | 2025-10-04 01:30:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| bea6da6c-88a7-30e2-8c45-10d2feabcc4b | -15.21561 | -56.83951 | 2025-10-04 01:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 94e32b4a-1052-35f8-bd01-02e9f2239852 | -14.03625 | -53.92192 | 2025-10-04 01:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 29.6 |
| fb34a004-77b8-3d8f-a9b4-39da75351a9a | -15.22976 | -56.8533 | 2025-10-04 01:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 3dd378c1-a6c4-39a4-875a-21e959ccd672 | -12.79321 | -56.96 | 2025-10-04 01:30:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| b2943294-dfbc-33db-bba2-8f255c4720c0 | -15.22721 | -56.83782 | 2025-10-04 01:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 266d561b-4a96-3011-8564-ce9cf740696b | -10.60268 | -54.36374 | 2025-10-04 01:32:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| fa78de3c-dc06-3cc0-a655-bf147ad26650 | -9.34759 | -54.52006 | 2025-10-04 01:32:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| e6cea37e-1279-3d12-9d3f-e25e14655604 | -8.59078 | -63.25312 | 2025-10-04 01:32:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4c487bb1-fc5d-358d-b153-75c063d06aed | -11.12656 | -55.45912 | 2025-10-04 01:32:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| d31b4d14-c1a3-34c5-b678-32e1e58e1e61 | -9.33207 | -54.52264 | 2025-10-04 01:32:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.3 |
| cb9f7636-36ff-30f2-a8ca-41910258e570 | -7.87887 | -61.67983 | 2025-10-04 01:32:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 21f8eccd-5927-3b0e-a8d1-27780671ce0d | -9.63062 | -63.24403 | 2025-10-04 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 03bd531e-9f13-3d92-a7c4-11442fe74c7d | -9.08452 | -63.70049 | 2025-10-04 01:32:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 129a5906-9a71-3238-9730-a507511c8e8b | -9.92977 | -62.22351 | 2025-10-04 01:32:00 | TERRA_M-M | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f90c00dd-bf7a-3e00-902e-9190f74551c4 | -9.22688 | -61.82534 | 2025-10-04 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ad61ee97-0ac7-36f0-81d8-904a4e7a2f9a | -12.74694 | -60.1093 | 2025-10-04 01:32:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 0a580e9b-c8bf-33ed-96a3-6b4b00bf0b51 | -9.90789 | -63.59079 | 2025-10-04 01:32:00 | TERRA_M-M | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 53dcd1cc-b084-3210-97ed-149280b04250 | -8.6138 | -54.98064 | 2025-10-04 01:32:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 78c7742f-7f4d-39b9-9f01-48a277a5ee27 | -12.74214 | -60.105 | 2025-10-04 01:32:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 52e37fad-9bf9-39bb-a5aa-f9195135a865 | -6.86747 | -63.13457 | 2025-10-04 01:32:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94d15432-ecc7-32ba-adc2-36c59a72c469 | -9.70891 | -67.46853 | 2025-10-04 01:32:00 | TERRA_M-M | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a9d631bb-da11-3714-9ae5-74a26721a8c5 | -10.00429 | -60.01548 | 2025-10-04 01:32:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ecb9c090-0b58-3642-91ea-9e5945c4da98 | -9.3481 | -54.54525 | 2025-10-04 01:32:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 577bb90d-f049-3d72-97ba-55a4ff2e6cf7 | -12.7437 | -60.11567 | 2025-10-04 01:32:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 60ea9640-4072-3d00-b563-f579ba32c83e | -9.3427 | -54.51402 | 2025-10-04 01:32:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 76e1bf82-c251-30a5-9640-6ab02021bef9 | -8.63097 | -55.00231 | 2025-10-04 01:32:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 94d4fd13-48df-3ed2-ba72-3b1a81538e78 | -9.99429 | -60.01701 | 2025-10-04 01:32:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 62131258-c0c0-3e11-bee9-383649e25168 | -9.66814 | -62.39262 | 2025-10-04 01:32:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 71b396c7-3be6-3c0c-817e-1e360d5d5589 | -9.63943 | -63.24276 | 2025-10-04 01:32:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c2d478a1-6cf3-3845-9e3a-85d2e04b247b | -6.8774 | -47.2334 | 2025-10-04 01:40:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 7814f6bb-1716-37d2-b9ab-612e9d8fea52 | -11.9147 | -46.3726 | 2025-10-04 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 176.1 |
| fe5fd9fa-aaf2-3b4b-a48f-54fc3b7bfdae | -10.3343 | -50.3402 | 2025-10-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| c9f14622-9bbb-39c3-b896-682537dd8cd7 | -5.4849 | -44.0982 | 2025-10-04 01:40:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 25790bb9-4b11-31d2-b4c6-25989856be1a | -2.9013 | -50.7351 | 2025-10-04 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| bbd1247f-d7a1-3ae0-bd05-4bbd6f7cead0 | -9.3276 | -54.5215 | 2025-10-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| d57234df-df99-3f15-ac28-7f88aa8edd3e | -4.4445 | -43.2397 | 2025-10-04 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 506.2 |
| c5ab40b4-2371-371e-970f-4422fe730520 | -12.0507 | -45.1872 | 2025-10-04 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 297.2 |
| 6e42d4d9-5bb1-3aa2-bc80-e5fead51f990 | -4.632 | -43.1583 | 2025-10-04 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 784e170c-a40a-320c-9fb5-a4c026a55c59 | -4.4632 | -43.2386 | 2025-10-04 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| b520a70f-528d-3735-bb41-1134dad67cf3 | -5.4847 | -44.1212 | 2025-10-04 01:40:00 | GOES-19 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 15aeece2-becc-389a-9214-a7868d3675e1 | -4.4258 | -43.2408 | 2025-10-04 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 3a390c4c-aa4c-3cf1-b112-e9050abbb94f | -10.3346 | -50.3188 | 2025-10-04 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8c6186e4-89e5-3fa6-9274-a0c388ab64eb | -11.9343 | -46.3472 | 2025-10-04 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 59bb085c-a32c-3700-8cb0-934a2f84e67a | -11.4881 | -46.7471 | 2025-10-04 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |


[Clique aqui para ver as próximas entradas](README6.md)
