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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70120dba-2fc8-3bb4-b7fd-8753acdcda95 | -7.20032 | -45.33107 | 2025-07-23 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b6a0faa1-df6e-3b1c-bb56-39047e3183ec | -12.73166 | -46.61618 | 2025-07-23 04:34:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b00e8d0-a6f1-3a26-8d9b-ca4b34e5851f | -7.74506 | -44.01841 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 00bf512d-6e09-3131-a86b-8c0d196b6cb1 | -8.91346 | -47.35239 | 2025-07-23 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d75c6013-3e45-319b-bf0f-7354c2443730 | -10.88941 | -44.36768 | 2025-07-23 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 599f6a5c-7bab-35c0-8641-9c740ee959b0 | -9.05693 | -45.06778 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f3a1bf44-1964-3782-8899-c6a838de1603 | -9.05627 | -45.07215 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a6bdf4d5-98d5-3909-9c99-e9bcd7698693 | -13.68782 | -45.68981 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2789d52c-a6d9-3fd8-abf1-6105d4a6fc29 | -7.14157 | -46.09986 | 2025-07-23 04:34:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| be989da5-c917-3ff4-b027-9afc31b6cff7 | -8.91626 | -47.35649 | 2025-07-23 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e35f636e-d44f-33f0-8b77-8f5ae564797d | -10.29934 | -60.54337 | 2025-07-23 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54241945-5d0a-3ed1-92cf-4f23fae0d744 | -7.02907 | -45.84543 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efd47596-0d12-3d09-8d72-3a13d02bafe0 | -7.82558 | -47.22115 | 2025-07-23 04:34:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f5fc3a9-bca0-364a-b48b-99d9bcf7d6d9 | -9.06016 | -45.06625 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fd371dea-c095-3f92-99a4-f810c156dc7d | -7.73313 | -49.46135 | 2025-07-23 04:34:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c06847c-9f23-329b-87d8-a266b6abdabe | -7.04986 | -45.84877 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aac64634-df7f-3420-8c9e-b2a46e9197e5 | -12.49977 | -57.77796 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f70f251-5322-3a80-bad8-54f8a25b5274 | -13.63025 | -47.73302 | 2025-07-23 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ec1ca26-5c0e-3cff-926a-c9cd46f97262 | -7.19676 | -45.33057 | 2025-07-23 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| bf37f99b-52c0-3e5d-abac-b56d435d5b98 | -9.25957 | -48.5624 | 2025-07-23 04:34:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7ad2915-ba3d-3578-9833-2cc5dc134ae6 | -13.65696 | -45.71842 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0369c300-9231-3cf6-8d50-e5fa62ace681 | -7.0691 | -43.92858 | 2025-07-23 04:34:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 00b78248-20b1-3f21-bb7c-253b28b1d79f | -9.05391 | -45.0628 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8556b7cf-e9c0-36d4-a761-288e574fd76d | -13.09821 | -46.83141 | 2025-07-23 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00182a33-ee7f-3d33-985e-36ae4d089597 | -10.70474 | -44.06277 | 2025-07-23 04:34:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2835ba2-f37e-3687-8ff9-1c1581693a7f | -7.28034 | -44.36244 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7209fcd1-2262-39b9-b915-01c6658048e0 | -7.41306 | -44.59748 | 2025-07-23 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 986f9a34-c079-3dad-bcd7-f585b6d17202 | -7.52547 | -42.41938 | 2025-07-23 04:34:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4234971a-08c6-32c6-a4ee-41ca866999d9 | -13.64881 | -45.72185 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67010654-b7f9-3164-860e-11adf63a2ade | -7.75203 | -44.02453 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 49bf6afc-e43a-3c9e-9fd7-9c49616b3773 | -9.06145 | -45.05728 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 037e3ede-d748-3c32-8d6f-c2fe90e26aee | -7.27634 | -60.17472 | 2025-07-23 04:34:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beb10531-2878-3f40-b41c-2981e5796b85 | -13.72183 | -45.69759 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e66e8649-743a-39ee-a329-073bbb85778c | -7.75134 | -44.02926 | 2025-07-23 04:34:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6870f891-2825-32fe-982c-4ca0f234e7b5 | -14.17888 | -45.35456 | 2025-07-23 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa6bc786-2a27-33ad-b574-9a678747b4e7 | -11.88323 | -52.4911 | 2025-07-23 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b71ea2d-a728-3cab-a9d5-ef0059c95603 | -13.65256 | -45.72245 | 2025-07-23 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 45e236b9-38c0-33ce-b9f3-101c4d4529da | -7.02502 | -45.84871 | 2025-07-23 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3e1ef6ae-95b9-3ab0-911a-2a717119f903 | -12.50541 | -57.77184 | 2025-07-23 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5031f9c9-0a3b-3e6a-8376-c1428d074592 | -9.06753 | -45.06731 | 2025-07-23 04:34:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 108d2ce6-4454-30c4-b8d1-751b8a1a4712 | -17.575 | -47.50602 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 107f6dd8-5c5e-39a0-9e43-6564d341aeba | -15.28715 | -47.1358 | 2025-07-23 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 19c40e32-c49f-38c0-a781-cc0fe5fd44f7 | -16.09951 | -42.27853 | 2025-07-23 04:36:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4f5fd532-4ec7-3e02-8b28-54a020db5a47 | -17.44317 | -43.63777 | 2025-07-23 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fba9f4cf-a016-353e-810a-af0ca3630614 | -17.57439 | -47.51026 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cbff6fdf-cdcd-3018-86d7-2e5d006088f3 | -14.75023 | -48.23087 | 2025-07-23 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 018c66c4-b9b5-3b7c-999d-95fbf9cc1ced | -13.72362 | -52.01165 | 2025-07-23 04:36:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac549b64-837c-37a1-ab21-d550082658dd | -15.78372 | -46.06151 | 2025-07-23 04:36:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a49fb802-c4a4-3dac-8c19-3d4ec4db0018 | -17.57142 | -47.50547 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b385ff18-fc4e-30e3-a363-8b1d4861e030 | -14.3953 | -47.74568 | 2025-07-23 04:36:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6433ca1a-ca8a-3282-a868-d7e6d8fce3df | -15.60075 | -46.52168 | 2025-07-23 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf673eb-cd36-3c49-98d3-ba7eaae6f3ba | -12.35207 | -63.41968 | 2025-07-23 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 65d8422e-07b1-39d0-b933-f0a5c010a01e | -17.7869 | -52.43513 | 2025-07-23 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 777af33a-b86e-353f-9850-e56a10c78f86 | -17.56426 | -47.50433 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 702be327-bad7-3eff-94c1-a7e4b6e904e2 | -14.39209 | -49.02531 | 2025-07-23 04:36:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b34bab91-a28f-3be1-96f3-72fb0806ac65 | -17.84612 | -42.63984 | 2025-07-23 04:36:00 | NOAA-21 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e153b388-41e1-3318-95db-7d0ca006409d | -16.0488 | -43.79758 | 2025-07-23 04:36:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54f23ddc-0e53-3dab-a4d5-8cb77797ef90 | -20.41605 | -46.58198 | 2025-07-23 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f953dace-d7cb-314e-b329-c7b1b2a2feaa | -18.04829 | -48.89885 | 2025-07-23 04:36:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4a8abb7d-dff1-3d39-95af-7acd8f19015a | -18.66414 | -55.73143 | 2025-07-23 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| bb06fe1f-7d4b-37a5-af3b-dedaeff25ecf | -17.56784 | -47.50491 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f31cd78-36e3-373a-bee3-83eef2414ae8 | -14.39588 | -47.74177 | 2025-07-23 04:36:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03666306-ca27-357b-95fe-6e8f47df1bb2 | -14.6493 | -46.82913 | 2025-07-23 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 070a93c4-52ea-3585-8533-f01a068a16e6 | -16.9092 | -47.69074 | 2025-07-23 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 101e5dee-3d17-3953-8763-6a051edf95ce | -17.44463 | -43.63955 | 2025-07-23 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fe746a6-b454-32d6-9820-247784acb1b4 | -15.93117 | -43.5223 | 2025-07-23 04:36:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e31937c-edcc-3c73-8228-9cc605e0e1c2 | -15.84591 | -48.21113 | 2025-07-23 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 590b9406-a5c4-327e-a6e3-928b967903d7 | -16.03986 | -43.72441 | 2025-07-23 04:36:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 306f411d-2979-3a21-b444-da7a06ab0aeb | -18.66082 | -55.72871 | 2025-07-23 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d4dfe34c-febc-36b3-8af3-3f47b20e13be | -16.74895 | -54.25296 | 2025-07-23 04:36:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec9b281c-4cc9-32a5-b8df-bde1085dd9d7 | -15.60444 | -46.5222 | 2025-07-23 04:36:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5ab1d79-7b9d-3430-863f-cfeecb427e5a | -14.64733 | -46.83146 | 2025-07-23 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3601d43e-98e8-3b1a-b9d8-6177f2aa2211 | -16.73411 | -47.60171 | 2025-07-23 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfd77974-8ab0-3e26-a6cc-fe7362914eff | -16.04825 | -43.80199 | 2025-07-23 04:36:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9220edec-ec41-3e91-b059-b2492e3f6037 | -16.73764 | -47.60229 | 2025-07-23 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a18a29d-dc86-3e36-8643-d056308eeba0 | -18.66511 | -55.72623 | 2025-07-23 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 49e7489c-3f76-3944-abe8-437af5ebb875 | -18.0517 | -48.89939 | 2025-07-23 04:36:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5df265b2-b70e-3863-a287-7ab7abd57bc4 | -17.56724 | -47.50912 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d667922-f281-3980-88c8-3f8996d7e8dc | -18.39248 | -49.29187 | 2025-07-23 04:36:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0152a747-2ed7-34f3-9d70-2c78bc9b4d7e | -15.55646 | -44.75115 | 2025-07-23 04:36:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1c02f4e-2412-3c58-b837-145aeb60a807 | -14.77397 | -48.26476 | 2025-07-23 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e5090086-e0ec-3cb1-b20a-3a6b3148015b | -14.64511 | -46.83278 | 2025-07-23 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2167998f-1fe0-300b-b786-20e9107c7db5 | -12.3469 | -63.42126 | 2025-07-23 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 785e27f1-5d92-36e9-aa26-9291776193d5 | -18.66473 | -55.72949 | 2025-07-23 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7ab7f632-5db7-31e5-95c3-101ee6ae2f6f | -16.9125 | -47.69386 | 2025-07-23 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 492b540e-6905-3703-b68d-a31df6a6784a | -14.64869 | -46.83333 | 2025-07-23 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a59bb043-b096-3d42-b03c-a4de53fe1874 | -16.03959 | -43.72609 | 2025-07-23 04:36:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d95adc-4136-3814-b357-c6f39b3e2788 | -16.91214 | -47.69534 | 2025-07-23 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 726eb212-9535-3dc3-9b70-385ee4129c38 | -18.66566 | -55.72427 | 2025-07-23 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a1a1538f-d7fc-3a9b-8486-a470bad07872 | -18.16688 | -47.98995 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab316f07-88c8-3fb0-8bf6-19c77f8a2eda | -16.46173 | -48.90068 | 2025-07-23 04:36:00 | NOAA-21 | LEOPOLDO DE BULHÕES | GOIÁS | Brasil | 5212303 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d4d3535-87fa-3cd7-9fac-4344cc722fdd | -14.64674 | -46.83566 | 2025-07-23 04:36:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b00e2d13-e553-3dd4-a5cc-5ba10e1124c0 | -15.73143 | -56.04399 | 2025-07-23 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 582d2158-3766-387f-a3b3-692e1ebc5c39 | -15.84648 | -48.20731 | 2025-07-23 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5520b476-5c42-3090-9dfb-0ce9aeb29b70 | -20.41667 | -46.58318 | 2025-07-23 04:36:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a765fbe-0b37-33e6-b6f6-37b060d1c068 | -17.12859 | -52.69309 | 2025-07-23 04:36:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f37f1e57-104c-381c-bc8b-9c0cc15d778e | -12.35355 | -63.41282 | 2025-07-23 04:36:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 640e694a-b4c6-3152-b51b-9a8b596f74ec | -15.57626 | -41.06862 | 2025-07-23 04:36:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1519173a-8fde-34a1-893f-207019a4c0e0 | -18.16656 | -47.99142 | 2025-07-23 04:36:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c15b2383-518e-394f-ba69-b4c79155fc8a | -16.90955 | -47.68924 | 2025-07-23 04:36:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README13.md)
