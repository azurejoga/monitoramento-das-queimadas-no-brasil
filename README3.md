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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93b19d63-8022-3386-89ba-70a8293dc812 | -17.16521 | -49.36829 | 2025-09-18 00:50:00 | TERRA_M-M | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 8af7ca16-4ca0-341b-9359-9528e9b4ff29 | -20.35343 | -48.78563 | 2025-09-18 00:50:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 18ba4be3-4df5-3b22-88cd-f073115d1fd4 | -15.4979 | -50.39438 | 2025-09-18 00:50:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 87a9c6be-d7fe-3917-8e59-4ba22bd0b9c7 | -11.0359 | -45.05877 | 2025-09-18 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 1df98036-96db-3032-8239-22524addaa71 | -18.9832 | -46.98287 | 2025-09-18 00:50:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| e02e1e50-4abc-3cf9-8d58-13e85e56c35a | -15.49929 | -50.40393 | 2025-09-18 00:50:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 997e44fc-a5ee-3d6a-bca7-d1f895f5fa20 | -19.04198 | -48.27947 | 2025-09-18 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fb127883-204b-3ab0-8227-11bafd58d43f | -20.88595 | -48.45634 | 2025-09-18 00:50:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 1254012a-c317-3b96-b50f-a55e6a13c3b4 | -13.07109 | -42.14581 | 2025-09-18 00:50:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 114.6 |
| bed519ef-4310-3b81-b0b6-f403b3affe50 | -11.49783 | -43.62226 | 2025-09-18 00:50:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 37.5 |
| ef648366-075f-3a75-afd3-15b3ccea0631 | -21.78092 | -47.79193 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dc073195-5648-34f6-97ac-0f8ce4604ee0 | -12.90832 | -44.66695 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 76296bc8-26d2-30b5-bc83-70adc107de75 | -19.04985 | -48.26686 | 2025-09-18 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| ae5f87e9-6800-32b8-b678-9d7c30cf7a90 | -15.50832 | -50.40266 | 2025-09-18 00:50:00 | TERRA_M-M | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8b92df85-addd-359a-9bab-1771da1e9bde | -19.58188 | -57.77498 | 2025-09-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.7 |
| 4736b244-20d2-376d-a646-b799b8c36daf | -17.08824 | -49.40741 | 2025-09-18 00:50:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 515ea0b0-b1f1-324d-951d-924dce136afe | -14.26758 | -48.31079 | 2025-09-18 00:50:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f950b1cf-3d6d-3d32-ab14-5bf9cdd54a27 | -15.74348 | -43.9345 | 2025-09-18 00:50:00 | TERRA_M-M | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 96648504-9e82-3de4-976d-3d58f1dece48 | -15.04234 | -55.2626 | 2025-09-18 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 51165723-bc45-3dd3-86d4-125d7d67bee1 | -12.44851 | -49.75022 | 2025-09-18 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c239493d-a777-3f59-bf52-77da8ad67e08 | -17.23757 | -46.749 | 2025-09-18 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dd7bfdc3-e23a-30ee-b940-15f1979ae337 | -17.51558 | -40.29535 | 2025-09-18 00:50:00 | TERRA_M-M | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 49.4 |
| 94bddace-045d-3100-b811-305b6760f087 | -21.56633 | -51.85863 | 2025-09-18 00:50:00 | TERRA_M-M | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| c9467bc9-1f54-3c11-9804-24d2d2972bfa | -19.07055 | -48.24571 | 2025-09-18 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a18c1541-39f4-3bbb-87b6-48c058419011 | -15.01104 | -55.34044 | 2025-09-18 00:50:00 | TERRA_M-M | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b4449d1f-5c4f-3e04-899a-40675ca9595f | -16.69039 | -46.94884 | 2025-09-18 00:50:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| e1c1e021-89fc-3638-84f5-ca6fcf3f4196 | -16.72515 | -48.47805 | 2025-09-18 00:50:00 | TERRA_M-M | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 18.0 |
| b258eb1d-4372-3e57-83a6-f5c964b7339a | -17.16672 | -49.37852 | 2025-09-18 00:50:00 | TERRA_M-M | CROMÍNIA | GOIÁS | Brasil | 5206503 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 526c89b6-0e27-3a90-b6f4-e7e65172e8c9 | -15.90583 | -43.89045 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 19.5 |
| a9447feb-b80b-3703-aa98-eb91a2c23cc6 | -12.40058 | -51.43565 | 2025-09-18 00:50:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9b9795b8-0348-35bc-bc71-982f611b4c7b | -17.71277 | -50.86035 | 2025-09-18 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6effdba5-15f2-3f2f-affe-208ac4c882f0 | -21.11444 | -49.12351 | 2025-09-18 00:50:00 | TERRA_M-M | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 77a9c8c2-81b8-3ee3-80bc-41a428e69d0b | -19.57101 | -57.79833 | 2025-09-18 00:50:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.0 |
| 1a8ac3fc-d7f0-373c-8dd4-7fb77b745e65 | -17.71407 | -50.8696 | 2025-09-18 00:50:00 | TERRA_M-M | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7b5c5e79-0ccf-3834-9d07-0df2f90a5b64 | -13.53 | -44.11845 | 2025-09-18 00:50:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 6781686f-5135-38c6-a7ec-c45fd06eccf0 | -12.40689 | -51.41585 | 2025-09-18 00:50:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7bde60ef-938a-3b69-b7f8-8b2f8e3d0140 | -20.67253 | -48.75366 | 2025-09-18 00:50:00 | TERRA_M-M | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 22.6 |
| d779d60f-5dd5-3375-af78-c9185686bb9c | -21.11301 | -49.1137 | 2025-09-18 00:50:00 | TERRA_M-M | ELISIÁRIO | SÃO PAULO | Brasil | 3514924 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 9617c9e4-75f5-316c-9f85-a8ead5ed71d0 | -20.34427 | -48.78725 | 2025-09-18 00:50:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 12bb5342-c31c-34d2-bc03-c7b6092adf80 | -12.40819 | -51.42509 | 2025-09-18 00:50:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| b5762a9b-d3ac-38e8-9473-f70ab66566b2 | -12.44219 | -49.73573 | 2025-09-18 00:50:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 80d4c818-62ff-37ac-a23d-09f6717fca77 | -19.05318 | -48.25994 | 2025-09-18 00:50:00 | TERRA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e9a7920f-2be3-3784-8893-e6d6ad78ae68 | -7.8078 | -48.37658 | 2025-09-18 00:52:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 590ff2af-d8a6-37f3-83dc-57dd61fd3d2a | -11.4669 | -48.70295 | 2025-09-18 00:52:00 | TERRA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a7efb49f-90be-3f2a-a3d1-09b2f2550d76 | -7.81006 | -48.39181 | 2025-09-18 00:52:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 36.1 |
| 184d050c-a10e-3dd7-9617-e1cf9998a668 | -6.69172 | -46.30799 | 2025-09-18 00:52:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 185.6 |
| b9bc2b74-8077-379e-aac5-533c83807eb7 | -8.02436 | -49.85249 | 2025-09-18 00:52:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4c023af2-0161-376e-93ed-351b52179d34 | -4.65505 | -47.5657 | 2025-09-18 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 857f66f9-7b04-3523-acf8-befb6e0c5931 | -8.63371 | -54.65262 | 2025-09-18 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f601ea8c-7054-3c5b-b512-2d45247b439e | -11.37553 | -50.84354 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3807a246-4325-344b-adad-a8cff0bb507a | -6.54484 | -43.58165 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| ce74c7c5-27f9-3f0b-8785-0cc34220228a | -7.45379 | -46.39153 | 2025-09-18 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 570a1507-0842-3bb1-aaa1-516d6dde1749 | -8.5398 | -48.96692 | 2025-09-18 00:52:00 | TERRA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3a7e79c2-e671-3b6e-b733-5931c5e14988 | -7.07201 | -44.37454 | 2025-09-18 00:52:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| d1cf7d8a-1cd1-31d7-8952-c61f4a15d0fd | -7.41791 | -49.98187 | 2025-09-18 00:52:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fdf90993-1df5-3569-9387-8168bf49b276 | -6.51078 | -52.23277 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6b8a1f8-f826-3cc9-b249-a5d28f7b1b7e | -7.7987 | -48.39344 | 2025-09-18 00:52:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 87c7b9de-7fdf-3eae-a784-64beaf2ca1c8 | -8.94118 | -44.50856 | 2025-09-18 00:52:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 255f7751-5524-3239-9224-870c92f852e0 | -8.8995 | -46.14693 | 2025-09-18 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 53be4fdd-42ea-336a-987b-dc95eff6647f | -5.81601 | -45.89765 | 2025-09-18 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 65c4496b-822f-3b74-8002-2cffefc3989f | -8.08018 | -50.15968 | 2025-09-18 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b30ae151-c108-3b8b-8d0d-4205bf87ca2a | -7.54555 | -44.75198 | 2025-09-18 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 6b880698-2989-35a9-8e5f-d473fa7dc479 | -7.54231 | -44.74725 | 2025-09-18 00:52:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 35.6 |
| f85fa750-4250-360b-b983-e825fa139924 | -8.93861 | -44.50379 | 2025-09-18 00:52:00 | TERRA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 701849bf-7aaa-391a-8efb-621ed3635b2a | -5.49512 | -45.40674 | 2025-09-18 00:52:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| cf24062a-eabe-313c-a086-c347c2099ba9 | -7.26645 | -44.93138 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 485d0b32-a347-32ee-beb5-b87c56a4a980 | -8.34351 | -44.68555 | 2025-09-18 00:52:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 36.7 |
| e131a521-6fd1-3d00-a4a6-943bc6f872a3 | -8.34124 | -44.67952 | 2025-09-18 00:52:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 11120e7c-cd1f-3e5b-a440-9c21218312a0 | -6.56193 | -43.57991 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| f0805522-55b8-30d3-9a54-5839bcdc86f4 | -6.72705 | -44.14093 | 2025-09-18 00:52:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| e6710119-399e-3b12-80a2-48380a8f4e45 | -6.68537 | -46.31459 | 2025-09-18 00:52:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 4d517b03-eb9c-305f-931f-469abb501272 | -6.13797 | -47.82632 | 2025-09-18 00:52:00 | TERRA_M-M | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 48168a9d-b3aa-3ff5-a497-c8abf3a8322e | -6.68186 | -46.29128 | 2025-09-18 00:52:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 38.2 |
| b4c3f103-4077-3efe-b4c9-2c69eda68e9b | -4.61927 | -47.41029 | 2025-09-18 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 51e47085-7631-31f0-8f21-2b2f93874866 | -8.97625 | -46.29012 | 2025-09-18 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 42aef1a9-4eb0-3d73-ac6e-b85cca8155dd | -7.19659 | -48.60122 | 2025-09-18 00:52:00 | TERRA_M-M | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 9aaaa84c-5fb1-354f-8ef7-84d0e4bd53e1 | -8.97282 | -46.28424 | 2025-09-18 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| b4e41dcd-b0c3-3deb-b0d1-857f9004779d | -9.18615 | -46.95794 | 2025-09-18 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 17a1b5e6-4e0a-345d-b78c-1587cf0fff21 | -11.59422 | -49.81377 | 2025-09-18 00:52:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 09ec41c5-cab6-31c3-b768-d32847d26392 | -9.54961 | -50.84003 | 2025-09-18 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 625da1a6-61ef-3650-9b6d-59883c6cdd77 | -9.18864 | -47.0761 | 2025-09-18 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d4ca8ec7-034c-3a9c-a7cb-7e309ce501ef | -7.80843 | -48.38557 | 2025-09-18 00:52:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 99449a3e-62e4-3218-af5a-dc98a04223ea | -6.52794 | -43.93575 | 2025-09-18 00:52:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 6b2b8cab-df56-3195-85c6-e6ebfa49f18e | -8.88635 | -46.15021 | 2025-09-18 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1e85e40c-47eb-3a84-bfda-8f5441ebbb04 | -7.52262 | -45.28102 | 2025-09-18 00:52:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a0fd9e51-ae07-35c8-a325-25d1a3ddeda9 | -4.76712 | -45.33078 | 2025-09-18 00:52:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 34f20570-411c-30ba-ab84-6e0917dd819d | -9.01574 | -46.29945 | 2025-09-18 00:52:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| be9e1ade-7dc4-37f9-a471-2d045c1f741c | -7.06532 | -44.37014 | 2025-09-18 00:52:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| d3e84eed-f35d-3f1a-84c4-a7fb1b867d4c | -7.41295 | -50.01264 | 2025-09-18 00:52:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f1bf3abf-9c19-3ec3-bce9-fa9dcf5551da | -10.91747 | -47.85154 | 2025-09-18 00:52:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 28118281-9467-3279-b350-18ebfd7f9b69 | -7.24199 | -46.62506 | 2025-09-18 00:52:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 6ae837ee-ce77-3750-954c-32a59b32fe45 | -3.74291 | -49.04803 | 2025-09-18 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| ce2d0a01-be41-340e-8cac-558b99b40f1f | -6.57145 | -45.64288 | 2025-09-18 00:52:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| ddb8eaf1-9a1f-34c4-8c1b-a17485c2b6a4 | -6.90492 | -44.77205 | 2025-09-18 00:52:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 3c31f592-7e44-3f1e-b7c4-a3b31a05438c | -9.07899 | -59.01197 | 2025-09-18 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| f17c9a75-19a0-332a-bbe4-dfe02e8f5a3c | -7.52718 | -45.30894 | 2025-09-18 00:52:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 231c1e7c-1f42-3f12-8f82-13cc417244db | -3.74518 | -49.06375 | 2025-09-18 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 95dcccc9-a773-34cf-8ed0-6a84fad6597a | -5.79391 | -43.91536 | 2025-09-18 00:52:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 7ad40f0c-0038-3e6c-a666-0e3deb617d56 | -9.19137 | -47.07013 | 2025-09-18 00:52:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| df0c0992-fd34-375e-a42a-1462cbe7f5ff | -5.32904 | -55.88779 | 2025-09-18 00:52:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README4.md)
