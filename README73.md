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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee2def45-8957-3c1c-96cc-1e6372ef2640 | -14.90703 | -49.61888 | 2025-09-03 04:49:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5cd0e95d-1359-3781-872e-edca64bbdfa1 | -14.97768 | -50.21587 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1895058-bc5e-3366-908e-0c7fa320397a | -13.49563 | -46.81947 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66c7f91d-614b-355d-a9cb-07897986dbbd | -15.74866 | -53.66638 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78884e95-1694-30df-b172-b102be631fbf | -14.34986 | -52.80395 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 637277f9-837c-3677-8345-ed33ca22ff45 | -14.57605 | -48.06601 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dea7e7e9-9680-362f-8367-7422ce8b3558 | -12.89694 | -48.05518 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4915c108-58b9-3add-8868-7f3258f41daf | -12.49833 | -53.8377 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c02e396d-caa3-37c7-9e1e-3d8070b1972b | -12.94524 | -56.96391 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4712fa92-caa9-33fa-be92-045cf11f8fd7 | -14.81387 | -48.34877 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb04a7f8-73b8-3af7-8781-4aa46fd3fa4b | -11.85148 | -51.52697 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24122d19-9118-304c-93b2-f1b8fea7dfb6 | -14.78788 | -48.15683 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 042bacd6-0269-335b-ac5d-27d50671e440 | -14.96537 | -50.07391 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c0be483-f487-3510-b1eb-eea4df087685 | -13.8856 | -44.45345 | 2025-09-03 04:49:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b83eb8d4-b47d-3600-91e1-e52cafb1acc6 | -16.30326 | -52.96693 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 768bfe0c-ccff-3ec9-926c-2a6f1d27d5dc | -13.30531 | -46.82131 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55d195ba-dbf8-37c8-afb1-e40bff0470d2 | -11.85184 | -51.41364 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ed5e5b1-09ae-3534-8c2e-219795db26f8 | -15.59544 | -52.68553 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48e59781-4e2e-3a3e-a752-785b96c1474a | -13.48228 | -46.8218 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6358a7ad-2e80-375a-875d-289d76df978d | -16.29971 | -45.69029 | 2025-09-03 04:49:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e6b2c242-995e-383a-93e8-77b48771f1a7 | -17.91616 | -47.20784 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 696c376c-0c4f-3928-9e9c-2f0adb94ab32 | -14.52839 | -53.29499 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f593b26b-5773-320d-a6c9-a8439266b2e3 | -12.9516 | -56.99493 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 290d4a80-ae5e-3fbd-a1c4-64d82afc2303 | -12.94863 | -56.9894 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b3ad98a-e86c-329e-a61a-df4c81cf443b | -12.79318 | -47.6475 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15592407-075a-3f06-b1f9-7385abc093cd | -11.86223 | -51.54311 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87f8d629-ac75-36a6-9d4f-24075776d118 | -12.85037 | -48.0176 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4160f3e8-eef7-3e8e-a950-744a8fa34b91 | -15.27177 | -52.73573 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fcd753c5-47f5-31bb-949f-e475d5278221 | -12.94185 | -56.98322 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7f80d506-72d0-3a00-83c6-b7b06c31aff2 | -11.86549 | -52.42426 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bea1b502-de25-35f3-ac84-7d2810105bce | -14.60111 | -54.58416 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe126e15-3a9e-3c90-bc3a-a04ea90c50b8 | -13.01185 | -48.09263 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7ffd50be-4ff5-3167-80ce-77c488a6625d | -13.00975 | -48.10744 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23685511-2989-35f2-b2a7-36e57805b2c9 | -14.78462 | -48.15088 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1be58124-9104-3c37-9c38-b9a80861275e | -17.94822 | -47.23922 | 2025-09-03 04:49:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a648e38d-4dbb-3640-9743-b6bd306da770 | -12.927 | -57.00053 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b18c0203-5f58-3c00-a74a-1d4e30385cfc | -14.5765 | -48.06261 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f30bff94-4255-302c-9f85-1625c2df5da9 | -15.55267 | -48.34968 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f301d3c8-3fc9-3c5f-8ee1-cba2fbc2036e | -14.97472 | -50.21119 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ca2c8a0-563a-35f7-b7b2-b68f3e29261b | -12.93244 | -56.95325 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cac1667c-989c-3052-b916-12505483201f | -14.35041 | -52.80041 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e5cb0cf-f48f-3ec4-9fea-787275845975 | -14.57396 | -48.05126 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff0f605a-fc62-37bd-8fb1-c2fb628673c1 | -14.60508 | -54.58099 | 2025-09-03 04:49:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31faa35a-b491-3833-80c7-3e15a58409ff | -12.86461 | -48.02996 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a595a7ba-dcf4-369b-99bd-e38d7c64b0b5 | -18.03415 | -51.58881 | 2025-09-03 04:49:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 597f720c-79d0-3b65-91ac-01b597f80bc0 | -13.28206 | -46.83377 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f1309b1-b7e2-3c22-b1e7-4cf914e2991d | -11.41541 | -55.18474 | 2025-09-03 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a05cf4e9-76ca-327d-a95a-7e06d32fb128 | -12.49774 | -53.84132 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d84a7db1-372f-32b5-9fd9-ba9e6c1cb3d1 | -13.35578 | -51.7303 | 2025-09-03 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa6b1a5e-2df8-3769-a2ec-d60cac9c3cf8 | -14.78066 | -48.1502 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| faaacc59-9087-3d3f-8803-36b9f5a09541 | -12.92041 | -57.00095 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 388bc338-fb1d-32a2-b7f9-1f89f0c669fa | -12.18028 | -53.88948 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a681f260-f002-35c8-9ce6-d92dda3c553f | -16.54567 | -55.07846 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4591af32-0019-32ce-973d-1a339862d293 | -15.02633 | -50.07323 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b387b4b6-4ece-35f3-bff5-76a7b8bff2c4 | -12.1781 | -53.88165 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 569a1140-2843-3717-9041-43697b95f08b | -14.61219 | -48.0992 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a662930-0917-3f8e-8d25-b19b02b14b73 | -13.27542 | -46.88525 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfbe9380-24ec-3fce-89e2-62447643c73a | -14.32692 | -60.33997 | 2025-09-03 04:49:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e90b0c64-a277-3a65-a53a-bb74b1a82b16 | -13.30093 | -46.921 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab47f02c-e49b-37e8-b165-a0ac1fbe60cd | -13.30463 | -46.92557 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4f6dd7a-005c-31d5-8f65-d13a4e1595df | -15.00359 | -50.05264 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 82c108b0-fea5-3196-a6f0-b896384f29e5 | -16.29996 | -52.94432 | 2025-09-03 04:49:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4143aa19-04a9-3962-9485-f4abb70f7b31 | -12.94015 | -56.94821 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fdab510a-f3d6-3ddb-be98-c81256576c28 | -18.03221 | -51.58511 | 2025-09-03 04:49:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72a948c8-bd99-3aec-97be-606068fd028e | -12.85424 | -48.18942 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b8cf0ba-2cbe-33d4-97f6-8e71787094be | -15.2447 | -53.79842 | 2025-09-03 04:49:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 414125fe-cfdf-384d-9ef0-45c8f8232fb8 | -15.98305 | -55.96338 | 2025-09-03 04:49:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5e8a31f7-811b-38b1-b2a9-1928d2d51b30 | -14.83163 | -48.36589 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83d42425-ae5b-3a50-84b8-d3b49d3bc7c8 | -12.48827 | -53.83604 | 2025-09-03 04:49:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c99485a-cedf-321a-9f19-fabfb09b72d5 | -12.88727 | -48.03901 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4bff0547-d8f5-3632-acd3-1d411604659b | -13.70267 | -46.8827 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92bd6b75-e995-3111-bd36-8af791868f1f | -13.00722 | -48.09723 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7dbe7277-dc5c-3d04-83d4-03760f407812 | -12.89213 | -48.08925 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 924832f6-faad-3d1c-a233-4211b67be5ce | -12.7927 | -47.65103 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f040de4f-20c2-3feb-a44c-208f75f39a04 | -14.30394 | -53.09793 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b715cc8-093a-3c5a-87e0-ee3398690b8d | -14.34655 | -52.80341 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f9a735c-cd19-3803-8e02-ba83fe667785 | -12.92123 | -56.99613 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b2e6e302-dfed-321f-8f6c-b7d593be5f60 | -11.65779 | -57.35935 | 2025-09-03 04:49:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 711e9489-a4e9-34a2-b5ed-606473a4ddbc | -17.43756 | -47.20481 | 2025-09-03 04:49:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fadf6fd4-f6d5-3b47-a27f-b2bc4e0882f0 | -11.86273 | -52.42022 | 2025-09-03 04:49:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df078e1c-8c51-3eee-86b7-7bba3e909d8e | -15.54118 | -51.71545 | 2025-09-03 04:49:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e20a262-7d1a-3c99-b4cb-3217b80347ff | -15.01916 | -50.07216 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 77c72186-7bd9-308b-9dc7-292c12a0f3f8 | -12.78908 | -48.17511 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 55b978bb-0f8a-3559-ac80-8244ef37d6f1 | -14.34931 | -52.80749 | 2025-09-03 04:49:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9127f53b-c667-3e13-b47f-38b9cd54d24d | -11.86136 | -51.46282 | 2025-09-03 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23f94a1d-056d-3769-a5b0-01c5d17b67c9 | -12.98104 | -54.77562 | 2025-09-03 04:49:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ac8d1f1c-ef1c-3563-b638-6887d000397f | -13.51551 | -47.02598 | 2025-09-03 04:49:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad34cf53-7a85-3e8d-ab07-f24e5f516e93 | -15.55068 | -48.31538 | 2025-09-03 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dd64fe21-0f28-33f6-8653-c0e108b74ac1 | -13.90469 | -48.12043 | 2025-09-03 04:49:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 35c7d02e-ffe0-3270-9eda-0859b4c5564e | -16.86225 | -49.59101 | 2025-09-03 04:49:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a544608-faa7-3ce2-b006-606a377573fb | -15.16544 | -52.36547 | 2025-09-03 04:49:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c58053f8-6e59-3de9-9877-7b2049971c90 | -15.02692 | -50.06903 | 2025-09-03 04:49:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6db3ce40-bae9-3087-8dbc-1262c9481505 | -12.91553 | -56.99857 | 2025-09-03 04:49:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c5d4b2a1-03b0-352f-9c8d-669397d43084 | -15.71943 | -47.67068 | 2025-09-03 04:49:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 442983d2-4fd0-3f7e-973e-38099120cbc7 | -14.90275 | -49.62275 | 2025-09-03 04:49:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 366cd5da-88de-39ba-be6c-f63fd1dcd276 | -12.56799 | -48.26871 | 2025-09-03 04:49:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b36bb35-5722-3018-8f78-18ee166e7c33 | -14.57839 | -48.04861 | 2025-09-03 04:49:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d87e657-2d92-32a8-b51b-2f9d0975bbbc | -15.73479 | -53.68971 | 2025-09-03 04:49:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 303ff571-2074-311f-9ed4-d64a4d2f5ff8 | -14.56896 | -53.03618 | 2025-09-03 04:49:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 977d7293-498b-348d-bced-f8e3e50245cf | -13.70027 | -46.96408 | 2025-09-03 04:49:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README74.md)
