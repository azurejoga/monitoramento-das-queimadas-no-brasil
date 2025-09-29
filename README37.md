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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57c3f1fe-a39c-3b10-b7ee-00a0aa0a60d1 | -4.15014 | -40.0106 | 2025-09-29 04:06:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee6cb9be-6506-3386-a498-46810333a889 | -5.72971 | -42.67451 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 605dac0c-3a40-3a2e-acdb-bed2976f06b6 | -5.89719 | -42.94238 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1a60a3c0-1b0a-3533-a5be-a60bcebcf255 | -2.58089 | -48.40463 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 5d32f834-1207-3f6d-9c93-f872c187f76c | -5.12758 | -47.3855 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d16b4a37-cd83-3f85-89c1-21246179d993 | -5.97805 | -42.56768 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 92d84d23-477c-3ec8-a7c6-2de3c8ec4933 | -5.68805 | -45.10308 | 2025-09-29 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 69fe800e-8e4e-3847-a40f-f61ce8fbe0db | -6.74302 | -43.37354 | 2025-09-29 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3b723c1b-b308-30dc-a466-fd7133e7eaf6 | -4.11453 | -48.92884 | 2025-09-29 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82ec9908-a357-3a87-80ca-38ccd3bc51e9 | -6.46734 | -44.00925 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3bd2751d-06e9-33ef-b49b-eb20f84391dd | -6.49625 | -44.25413 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28c5451c-34b1-35b6-9980-e8f70db813ee | -5.68555 | -42.63831 | 2025-09-29 04:06:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 3e78d660-e24e-319e-9454-292016b599c5 | -4.71083 | -41.98989 | 2025-09-29 04:06:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 10e9c8d5-fce5-35fe-bea9-87be23feaea6 | -3.84139 | -48.95944 | 2025-09-29 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c9d5e53-bd48-391e-902b-8a7debc9a05c | -6.12511 | -41.81437 | 2025-09-29 04:06:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9cc6f2dd-3fbc-3ea9-ae8d-b13859cc0430 | -5.17083 | -41.25538 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9525d764-a22d-3553-9e8d-c5b0f3185a85 | -7.37901 | -47.03924 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fa92f1ab-d35e-34b6-9104-903c1c85cb63 | -6.90721 | -44.00157 | 2025-09-29 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26636e93-d00a-3e41-9518-b76a3d40b81f | -8.88518 | -45.03657 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d084e20-30e6-33c7-902e-caa5497bc923 | -13.36213 | -47.29589 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a513e37d-a217-301a-95ae-a61568fed31b | -13.26757 | -48.45293 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be09ff90-e7d1-3aeb-b04a-22ec7e675826 | -12.27689 | -44.1175 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 145a5678-97f2-3828-957e-aca27620867d | -8.88516 | -45.04674 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87dbe88d-80bb-3a2a-9c96-7ece00aabf68 | -11.9734 | -46.58269 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e777a24d-63b9-3328-b1e2-9078946b6638 | -15.04292 | -46.97237 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2af23928-3ccf-3f0b-a7ae-c027dea4d4d3 | -12.85727 | -45.18162 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc719611-5914-3064-babb-475e811c0577 | -9.79823 | -46.94344 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c0c3676b-c850-361f-b26c-55f8a0c9685a | -11.94024 | -48.06242 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7deaac18-c1e7-3f79-99b5-30f5017b8d87 | -8.71371 | -47.97869 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 292f2fc2-99f2-3ba1-93ed-cef0d6829513 | -12.94625 | -45.23621 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6169f88e-8f10-328b-b711-0fbe2e34807d | -14.42048 | -44.8741 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 859c5128-3c3f-39d4-9e43-131de039a4fd | -11.5097 | -43.54405 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58361087-a6fe-37e4-a410-a15e6ab3ae3d | -9.31463 | -45.69608 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ceaa40a5-8e29-3f25-b7e6-63fea0d13eff | -12.89961 | -47.11459 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c9fea6e-03cb-3cb6-a8fb-bfb3b2d87d47 | -9.466 | -45.50455 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc73f9be-06e5-3914-91f2-f10ada342a66 | -11.71578 | -44.44173 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17174cfb-75e1-3cd4-9919-dfb0ffff605a | -13.25597 | -48.44672 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 122c36e1-85a6-3276-815f-d207f669f202 | -15.52436 | -47.93176 | 2025-09-29 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b6932dfb-c524-38cf-af5e-4fd56656a19d | -12.8975 | -47.10429 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 78f811db-43c2-3a0e-9e54-399bcf02c9e8 | -15.28718 | -46.41879 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad0abcd5-f95f-3ca9-a7b0-91260b31ee47 | -14.6811 | -48.16028 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f880ac0e-8d21-351b-bc34-e187c11def32 | -14.70575 | -45.20849 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a98e1be6-7cb3-3d7c-817c-6c6ae4c1bc3d | -12.00275 | -46.61864 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51f97446-34ec-378f-ac26-825c6b0213af | -11.36254 | -45.07678 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| d5e962b0-8597-37f1-b295-1397570871db | -15.87279 | -46.21852 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2a61ef2a-6a48-3a06-9ee3-2958640f8155 | -12.5889 | -41.29014 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 62e9d7a0-95ab-308a-b67d-d0c62f1d1715 | -12.6597 | -46.90827 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f79adc0-77ab-3adc-97e0-a9dddaea9444 | -11.82945 | -51.79192 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 279cd060-d92f-3fa8-986a-a96fa6e44f01 | -11.82468 | -51.78979 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 90e45388-7d5e-3522-b204-2edb758674f6 | -13.82866 | -47.49108 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f037eb8-840c-34b4-8b7a-ca5022bea515 | -9.00756 | -47.84169 | 2025-09-29 04:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2045977a-ad67-32d4-90ac-1bc713f0ee7f | -12.85761 | -46.97725 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d174339e-34bb-3c09-9d72-8f6461106dd6 | -11.26664 | -48.93601 | 2025-09-29 04:08:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 953c7f89-5106-319a-897f-72a179c79efd | -11.80069 | -51.8019 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ab1fae7-7a13-30fa-9785-beb5c05a1730 | -11.45154 | -51.50399 | 2025-09-29 04:08:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5f31e6b-24e8-3b7e-bd18-ec6d40dfcace | -14.74449 | -45.67462 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a530eaab-cdde-3ace-95eb-3257c033bc4e | -11.44262 | -45.03279 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4e528c6-c613-3283-962e-9a76e6f5aeab | -12.28597 | -44.10406 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e23a0420-06f2-3db0-97eb-4b8d953f33ab | -13.39705 | -47.92096 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96b04402-3c85-34c8-a5b5-52acd3ff4dd0 | -11.81482 | -51.78448 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c25a814-5afe-351e-a234-b08edf26aaa7 | -8.719 | -47.98528 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1a37552-665a-334f-a656-2e5a9100565e | -11.50806 | -44.8527 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9331833e-972b-385c-a088-557cc128b582 | -13.5565 | -47.27184 | 2025-09-29 04:08:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f81ef65-05cc-3648-b699-2f6b98140081 | -13.60962 | -48.04056 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d10f1875-60c6-3af7-97b1-4f586cf38bc5 | -11.41126 | -44.89949 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ff45f5a-1f86-3405-bfae-4a73e78d7985 | -15.05732 | -42.33949 | 2025-09-29 04:08:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| b7c1b548-b2ad-3801-b72f-b8f60a59836f | -11.69847 | -44.4394 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cc62992b-8aa2-3299-b8c3-1c4584bbe0c6 | -8.88292 | -45.03793 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fce3e72e-ba66-3248-9b36-0b5b4fbf9cbe | -11.93829 | -48.07364 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c74c4717-52ad-3709-9684-e862737caff3 | -15.26086 | -48.77166 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 316642a4-b097-3fbe-ba46-57bcf18fa873 | -15.08872 | -49.5667 | 2025-09-29 04:08:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3b1de91e-9007-3b7d-8bdf-baa2d0f5a78a | -11.35776 | -45.08398 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 294b9123-a484-3166-add7-d2e05b19a252 | -9.43637 | -45.54784 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| feef55b7-2682-330b-a3f2-42439fc23d28 | -15.28801 | -49.50509 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f946073e-49e8-3a1f-a86c-093badf59ab9 | -15.52918 | -48.51472 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f542b5bf-c72f-3df4-871f-5da4a4cb78f9 | -15.03926 | -46.97174 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bc31943-d49d-3921-9715-f15ab9b092ae | -12.20681 | -43.75095 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3ced213-b145-3307-93ec-10c68373e179 | -12.27353 | -44.11694 | 2025-09-29 04:08:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d93b7734-1877-39a0-9be7-b643a65eb4bf | -14.40454 | -41.28954 | 2025-09-29 04:08:00 | NOAA-20 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a54ed2c3-6420-3743-ba4e-3f1ae12cf094 | -12.86378 | -46.96406 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3af5b76c-247f-38a8-b2ea-84a36b5bc7d9 | -15.07711 | -48.33424 | 2025-09-29 04:08:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9629e729-be0a-3712-9aeb-239464568187 | -12.79631 | -47.74212 | 2025-09-29 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b56b95f-157f-3b69-a94c-c924679a02e8 | -11.40451 | -43.50117 | 2025-09-29 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 903d7780-a553-35f4-b058-d693b9e814e6 | -15.87263 | -46.83919 | 2025-09-29 04:08:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6372a56a-29bd-3d30-a0db-875397f63d0d | -13.59363 | -48.06087 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ec49fff-9996-37c0-ad00-56368d54d38b | -12.75435 | -46.85617 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c55c8d80-bafc-3e33-b807-55c0eaf025f6 | -12.67367 | -46.87218 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7a1ea06-246f-3260-9076-6a0d34c8f4ec | -13.60152 | -48.06266 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a88b3ef0-ab05-3415-ab43-341330ced143 | -13.24719 | -48.44844 | 2025-09-29 04:08:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e86465bd-828d-30fb-b6b1-461f419007d0 | -15.116 | -46.4398 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be93e5a0-5d64-3257-a00f-5c0db25c8321 | -11.93379 | -48.02708 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 29c436c7-449f-38ed-a641-fce34775571e | -12.85922 | -46.96795 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 007c3659-78fd-30d1-93fa-2c93bb06e0f9 | -10.82818 | -45.41197 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac68c7c7-30eb-3ac9-9cd3-8106ed130d8e | -13.80663 | -47.9343 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 12e172ff-812d-304b-8f04-1dbfdab96d2f | -10.74855 | -45.39068 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d87ad3b-d261-356a-b9b7-6e603eb05cb3 | -11.91891 | -48.03989 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49c1a8b4-64b8-304d-90f0-7b0286c18807 | -14.70297 | -45.20407 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e7edfa9-3bac-358f-84e1-43e1f4e4689c | -11.26227 | -48.9352 | 2025-09-29 04:08:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e264ef07-ad24-32a3-80e9-ff486bd445e8 | -14.4374 | -44.87701 | 2025-09-29 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6464c5e6-8b75-3035-8a01-98b7cc084ba6 | -12.21193 | -43.74044 | 2025-09-29 04:08:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README38.md)
