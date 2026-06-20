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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b76d2f84-c65b-34ff-8202-cb3139e2a55a | -17.45074 | -47.16348 | 2026-06-20 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 318814fa-b8ff-334b-9d92-7f718290a5da | -17.35006 | -42.62822 | 2026-06-20 04:46:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1bab70b6-e58e-3178-9d25-124a11241570 | -17.45626 | -47.1507 | 2026-06-20 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34510dfe-6231-3db2-8158-f42633089e04 | -16.69582 | -51.84552 | 2026-06-20 04:46:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96d8ae28-85c0-3408-b204-92b6bd6c9889 | -19.70043 | -47.32811 | 2026-06-20 04:46:00 | NPP-375D | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e241b9f9-9b1f-3271-85dd-b2e29d6e19bf | -15.81119 | -41.89808 | 2026-06-20 04:46:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d70020d-cf7a-3182-a5fb-e6029934a34c | -17.44707 | -47.16295 | 2026-06-20 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9412d30-9560-329b-93aa-813d3349c57b | -17.32486 | -49.61123 | 2026-06-20 04:46:00 | NPP-375D | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d6905c92-2c69-3881-b8c3-ffc73c918906 | -17.11083 | -49.75404 | 2026-06-20 04:46:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cce88a60-2a2f-3768-851d-351f751b9f8d | -17.60556 | -46.67793 | 2026-06-20 04:46:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da175130-14c9-3cc8-9de8-8a5f0e53fc4a | -17.44824 | -47.16077 | 2026-06-20 04:46:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 822cdfb9-333e-3eff-8a71-614a1d0df9d1 | -18.4242 | -47.39319 | 2026-06-20 04:46:00 | NPP-375D | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4f59012-1ded-3353-96c4-d8d7ee63df0b | -17.35073 | -42.62257 | 2026-06-20 04:46:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5114ac70-7ad0-3ffa-8c40-74d3ffefee2f | -19.16795 | -45.58625 | 2026-06-20 04:46:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fa87ca7f-07b0-34c3-9e4e-593393526a4f | -12.5531 | -45.0174 | 2026-06-20 04:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 66c69a7d-ad55-3c48-91dc-a1c26d24a2dc | -12.5339 | -45.0204 | 2026-06-20 04:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ea3b417c-0db0-3308-a72a-b7700fa97a75 | -2.32545 | -60.06108 | 2026-06-20 04:59:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64eab95d-a16f-3850-b56e-40110ca79018 | -12.5339 | -45.0204 | 2026-06-20 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| b9769763-d584-3a21-80e0-f45a90c41c99 | -12.5536 | -44.9941 | 2026-06-20 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| d822a63d-b416-3894-bed9-fac26bf59fd3 | -12.5531 | -45.0174 | 2026-06-20 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 286.0 |
| 891b9e8c-aa28-3c44-8772-1238515eb8a7 | -12.5527 | -45.0406 | 2026-06-20 05:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d3be8267-c151-3d9f-a219-936caf745bbb | -6.35897 | -43.59684 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 606e3301-513d-3d94-901f-40046b872411 | -11.63863 | -48.54163 | 2026-06-20 05:01:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e5ae3f0-0b1f-30ed-a376-f03f31e6ee61 | -10.60454 | -44.32373 | 2026-06-20 05:01:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dede87a9-3ea8-33ce-9bd8-b7403c0fd81a | -7.63528 | -50.02557 | 2026-06-20 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e054ff6-16e6-3496-b6a5-629f7f988fa2 | -7.92953 | -48.25586 | 2026-06-20 05:01:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ea7a52f-50ed-3144-943a-ba5147f24e91 | -3.85261 | -54.22319 | 2026-06-20 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69586578-9db2-33df-a802-1669c23e90e3 | -11.21744 | -46.76551 | 2026-06-20 05:01:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d60a4a15-0e0e-3eba-91b9-1ed79f322097 | -8.97701 | -47.97922 | 2026-06-20 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 341ed8cd-14e7-32ec-8146-d06713867a9b | -11.21783 | -46.76251 | 2026-06-20 05:01:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f794d7ec-c026-3ef1-b91d-0385a1356c01 | -6.14566 | -48.49442 | 2026-06-20 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51c8fea6-c69f-3f81-bd03-fab27556c843 | -7.36776 | -49.85851 | 2026-06-20 05:01:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c8a9f353-db50-3a98-b0a4-a720bf52df7f | -10.76919 | -54.1067 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 098a7193-bfc3-37b7-aac2-0f7b9a2b28eb | -11.8896 | -43.83627 | 2026-06-20 05:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| fc0c4b21-68a2-368b-ba10-e725e6b7aec2 | -10.11663 | -52.19754 | 2026-06-20 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3263335-64c1-3f77-a257-4afabb744a0c | -8.64356 | -47.75291 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afedc01b-a933-3602-8a0b-cbc4b58a8ff7 | -11.22256 | -46.76619 | 2026-06-20 05:01:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56a0f2e5-b08c-36d2-bd96-115963889048 | -6.32937 | -48.41933 | 2026-06-20 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68b195e7-89ff-3614-bdee-456e3c5196df | -10.12323 | -52.17773 | 2026-06-20 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e8eca8b-27b8-3f08-80f5-bb76a5c71974 | -10.77198 | -54.11082 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ec52b14-dacd-32fe-b4a6-d2e45774dda9 | -5.81146 | -45.08482 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea40380c-0423-365f-b9a1-414b2798c38b | -10.78034 | -54.1011 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bf2289a-1466-3994-9abf-9c7b501e399c | -6.14989 | -48.49493 | 2026-06-20 05:01:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55fed985-646f-34a1-b01d-5062b27acdfa | -9.18078 | -58.05867 | 2026-06-20 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c4f0a97-c49a-3624-99a0-13e006a37fc4 | -5.81374 | -45.06843 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cf71221-b367-3a5a-84be-65a88125dae0 | -10.76529 | -54.10974 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 245ab7ee-5651-3b69-8cf4-43fffc80a992 | -8.63904 | -47.75436 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 363fec69-b6b9-3ffe-8370-dee7c5857303 | -9.02062 | -63.54917 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd1a923c-e709-3303-a358-3ddaa0f235e1 | -9.02118 | -63.54607 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c384677-0566-37b8-9f7e-0c73757b2966 | -5.80874 | -45.07361 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4e0d365-507b-3f7b-b4a1-06be91922316 | -8.97766 | -47.97455 | 2026-06-20 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 185e6cdf-a9f4-3483-924d-391edf21cd80 | -10.8005 | -54.17035 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 195018bf-c7ca-3258-840e-b6348e9467c9 | -9.0155 | -63.54821 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f4dc8b5-6d4b-3dd5-8caf-abaa276c4250 | -9.01661 | -63.54203 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88bf3ea4-967c-39e7-afcd-5e3c298c1585 | -10.46416 | -49.09337 | 2026-06-20 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cd0f85e0-3311-3262-8615-66add1d9ac32 | -11.63472 | -48.53622 | 2026-06-20 05:01:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35a1a427-fccb-3a68-9a2c-f8df41967968 | -6.37086 | -43.59792 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8cf36989-713d-3bbf-93d9-e96845d66fcc | -10.12262 | -52.1818 | 2026-06-20 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4bbe21e6-90d3-35b6-9eea-607c10ed330c | -10.57705 | -57.32264 | 2026-06-20 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 252e7349-1bda-3544-b3e1-dd2c7e4e271e | -5.81409 | -45.07409 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f779cc4-a0be-3b5d-9fc1-6a051320f4f9 | -5.81328 | -45.0717 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93545d00-5961-3a6a-8882-8a10181e8cbf | -5.81283 | -45.07498 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ad318940-dbf3-39aa-8297-a65ba14c72ec | -10.11724 | -52.19346 | 2026-06-20 05:01:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9482d14e-72a0-3f50-b2b4-9eaa3f8fa6b6 | -8.22623 | -46.84338 | 2026-06-20 05:01:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab6ed4a4-8d4f-3886-81bf-e6b4749e580a | -10.59857 | -44.32297 | 2026-06-20 05:01:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57d65e4a-f15e-3c4b-8cf8-29f7c99f3141 | -5.81265 | -45.08393 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba6beee5-106e-3bc3-928a-d5746074287f | -11.81544 | -47.34119 | 2026-06-20 05:01:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae537ffc-983a-305d-b4b4-ba5d5f5504e1 | -6.37145 | -43.59361 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| f4dc4a47-2e90-31cb-bbea-21eb7e502ba1 | -6.35956 | -43.59251 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9397559-3d4a-3994-87e5-06e964f3f4e0 | -10.77643 | -54.10417 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fdb4938-172b-3adf-a472-c2d6c7533f12 | -9.02006 | -63.55229 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c2013d5-2fc1-3e53-ab04-e0ba5dc5c955 | -6.39714 | -44.18363 | 2026-06-20 05:01:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5748eb97-ea85-38f3-9258-91cd9b0677b8 | -6.78046 | -46.33316 | 2026-06-20 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9173303-6714-3bb7-a998-79e4b80db19e | -9.85437 | -61.42636 | 2026-06-20 05:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0961764e-512a-3ba1-a517-5ac4212177b8 | -10.77253 | -54.10723 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 20aa371f-4f71-373e-8981-2c7cfa34f435 | -9.20156 | -58.04504 | 2026-06-20 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2bb3dc8-9c2b-3420-a382-1b3263b01254 | -11.07197 | -52.47818 | 2026-06-20 05:01:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59ab9fb4-21ac-3fe0-8be9-9222eea163a2 | -4.35365 | -47.76154 | 2026-06-20 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a17a7d20-9b26-3b29-a845-ea90deb39000 | -9.20959 | -58.06355 | 2026-06-20 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5fb47e6-69d8-3061-9b21-cc88ae19055c | -8.68484 | -48.30598 | 2026-06-20 05:01:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5158d84a-10fc-3ca8-96a3-44283d4967c9 | -11.89018 | -43.83136 | 2026-06-20 05:01:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc324c38-02c5-3233-b99c-daecdef2d763 | -9.01605 | -63.54513 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e79cd74-f2e2-36a8-a683-3bf2feb344c8 | -8.81442 | -47.06681 | 2026-06-20 05:01:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2c5371ec-7c07-39bc-a28f-941dcc8ed094 | -11.63408 | -48.54097 | 2026-06-20 05:01:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c3436f3-4c8d-3452-b18e-c4c8fc5c081d | -7.74574 | -55.33994 | 2026-06-20 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d29c716b-cb6e-353f-9897-04de801041b0 | -10.46903 | -49.08999 | 2026-06-20 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ce22c0d-5b3f-37f8-839f-9090056a5445 | -9.20668 | -58.05877 | 2026-06-20 05:01:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5792ee3c-f544-3ac2-a85e-2dd20eeb41ef | -10.57361 | -57.32204 | 2026-06-20 05:01:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c4aff36-a517-3d3c-94ab-b7bf3904e671 | -5.81457 | -45.07082 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 596465b7-ff7d-3c0a-86a5-a1b88a336f0d | -5.81361 | -45.07736 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b399c954-c322-385a-9879-1abbe451f46e | -8.64292 | -47.75769 | 2026-06-20 05:01:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51b197f6-3221-3e9e-baca-18987d619328 | -8.6861 | -48.3048 | 2026-06-20 05:01:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ecc1434-d63c-396f-b666-729f1ce45bb5 | -11.06781 | -52.48172 | 2026-06-20 05:01:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23f60392-645f-3e87-bcaf-f78609ea3d68 | -9.02174 | -63.54295 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| beeb667f-0998-3c8e-a777-6d407b577027 | -9.01495 | -63.55126 | 2026-06-20 05:01:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 945f5588-c9cf-3fca-af08-0db4fad1d539 | -5.81313 | -45.08065 | 2026-06-20 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2df7dbd7-ee1d-3102-82c3-0109f3e8bc3a | -9.55857 | -48.66901 | 2026-06-20 05:01:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6fef9215-69dd-36f2-8e8b-d7cadc73f273 | -7.92931 | -48.25705 | 2026-06-20 05:01:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8ac2a54-57f7-36f0-af9a-ca1df1f9d6d4 | -10.46846 | -49.0941 | 2026-06-20 05:01:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 630fd1a6-6466-3884-a942-8ab264d6be1d | -10.90752 | -54.13562 | 2026-06-20 05:01:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
