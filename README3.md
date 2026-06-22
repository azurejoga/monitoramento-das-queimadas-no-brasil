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
| a0dac798-d317-3dbe-b56d-0af9a43acb46 | -3.50313 | -48.05503 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a80ad638-f452-3858-83a7-19fb87626d55 | -6.23887 | -48.52742 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5eae3073-09fa-30c2-acfc-06598ea19df3 | -6.50803 | -44.69746 | 2026-06-22 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 73691b7d-fd7c-34be-a854-ce842728408b | -6.50298 | -44.70088 | 2026-06-22 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 40383463-5689-3d5e-b2d2-4dbbd3a46f87 | -3.5102 | -48.04802 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc1163b5-6fb8-3c7a-bd7d-73d3db68fcdb | -3.50446 | -48.0471 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83f49c4d-50c3-35f2-a5f8-6db5a3a8b1f8 | -6.49937 | -44.69586 | 2026-06-22 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a99b823e-7902-337f-8fc7-4e99a14e5a37 | -6.23772 | -48.53398 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ddf8e61a-e823-3d46-97c4-775c062e2e6c | -6.5059 | -42.21872 | 2026-06-22 04:04:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ce422d20-195a-3198-897e-9ca61f5b239f | -6.50373 | -44.69652 | 2026-06-22 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| ff3bb2bf-4938-367e-9288-83b5410df6a5 | -6.23504 | -48.53143 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| edab6215-d981-3118-85a1-7709d91e1f70 | -6.2396 | -48.53839 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a13a66f8-e594-3278-9afa-e6a9e3d8415e | -3.50518 | -48.04284 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0b82b4f1-3c22-33c9-96c7-b7465de72ec1 | -6.24083 | -48.53162 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 09ffbab9-cf8e-3d75-b610-0af054a13998 | -6.50961 | -42.2194 | 2026-06-22 04:04:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 3f886ff7-9fb0-3fca-9d64-8cc6bc9fd545 | -6.24281 | -48.53821 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 416d47c9-2de2-34ad-a6d9-f62620d59ca9 | -3.5025 | -48.05879 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e384fa2d-b9cc-363a-9e0a-d4694fb7141a | -6.23715 | -48.53729 | 2026-06-22 04:04:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e746037a-5ebc-34f6-999d-bb2e89eaf14c | -3.50887 | -48.05594 | 2026-06-22 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 87b03a70-c2a2-303d-9a21-d5e8ee5a5b4a | -6.5073 | -44.70176 | 2026-06-22 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c250697e-951d-314a-8eac-1afff3796d3b | -11.04907 | -52.48985 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 413112f1-9e16-3436-acee-68b39bab9666 | -10.56415 | -46.23307 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60f99355-0134-3201-b050-0bbc09992ab1 | -10.25261 | -47.34702 | 2026-06-22 04:06:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 599e6f0b-13c2-3f98-9d57-515d825b6e30 | -12.06618 | -48.43174 | 2026-06-22 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc80ab5e-ae8d-384f-ae70-a7dc6846f311 | -10.17059 | -51.66346 | 2026-06-22 04:06:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77da8121-3e97-3f98-9e3c-0f995d73cf8f | -8.87772 | -46.94759 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45ba7a50-9347-33d2-9109-bd214469e291 | -8.87087 | -46.95752 | 2026-06-22 04:06:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0a866fe3-0e26-3d15-8c10-da878b336fbb | -12.06515 | -48.42623 | 2026-06-22 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53a156de-293a-3c6b-95e3-5bfa30cd0332 | -13.29658 | -45.20971 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2742d559-9f77-35e8-8cb8-2bf582f5cb79 | -12.06731 | -48.42568 | 2026-06-22 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1e4b034-7fac-3454-8711-4297c1eb960f | -12.32536 | -43.44741 | 2026-06-22 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb2be8d6-29b7-3759-8390-44c7d191c020 | -11.90538 | -43.41223 | 2026-06-22 04:06:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc9007a0-3d15-3e2c-be69-577ef2e9a3e4 | -11.09975 | -54.14916 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db8d8163-2152-3ef5-81f8-e79cf5b02179 | -11.05236 | -52.49137 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ee2f78b0-c327-39a2-991c-f02a77d48c7b | -7.96429 | -47.42154 | 2026-06-22 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| de0ed3b3-e430-3869-bca6-0da71661e0ca | -11.20283 | -46.77603 | 2026-06-22 04:06:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 969e6358-db24-3449-ba64-3083cbf885aa | -7.95463 | -47.41679 | 2026-06-22 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3c53e128-bea4-384d-829a-05b814a85ffe | -10.0544 | -48.09342 | 2026-06-22 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1c6ae5b-230f-3d41-aa69-9472642e1333 | -11.05485 | -52.47938 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43e33399-430e-3833-adb1-e625e3d77e23 | -10.9103 | -46.31621 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 257d8730-110f-39b8-a0b0-c6b01487eaa4 | -8.87673 | -46.953 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85e37d55-3169-3c3b-9ae0-8106579a8f88 | -11.10141 | -54.14151 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 528a2dbd-967c-353a-bb7d-f0988ab4ab84 | -10.55267 | -46.24514 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 173e71d2-f3ef-3946-b729-6578eeb130e5 | -11.05361 | -52.48535 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fe757b8-20ca-37d5-a8b2-f5a2106d0822 | -13.29934 | -45.21762 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d833f04-2bd6-34de-892b-79d3ef60c025 | -7.27695 | -44.09203 | 2026-06-22 04:06:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6f22e60-d543-31ad-8cc4-b920ea8f3288 | -10.55715 | -46.24607 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e08e6906-a260-32d4-84a5-1008522302bf | -12.06456 | -48.42925 | 2026-06-22 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0da58701-c6b7-300d-85c1-b4f7080177cb | -7.95865 | -47.42362 | 2026-06-22 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 0221d07c-7852-3e34-a921-21b7c589320e | -7.32301 | -46.55554 | 2026-06-22 04:06:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bf667b6-0b88-31cb-a9b2-c5134097b205 | -7.9581 | -47.42664 | 2026-06-22 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9e755a92-b738-38de-9fbf-82e82c4eb0d2 | -10.94762 | -46.42561 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14d27204-8482-3742-803e-14aff099415b | -9.69083 | -47.69516 | 2026-06-22 04:06:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbb4cdee-0c64-34e7-956c-2c293a8c1845 | -10.94309 | -46.42478 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18627285-3c7e-3b1a-9654-1179823679f9 | -11.05606 | -52.47351 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9754325-92d4-3e86-b7de-9c602e5f4b1c | -12.85273 | -44.39886 | 2026-06-22 04:06:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14c4aa21-a25e-38f5-8571-86de29a61b1f | -11.05693 | -52.48508 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9c53684-e4f3-3976-8c92-1b79ffb3fd60 | -12.19896 | -47.96969 | 2026-06-22 04:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9aecc3c5-07ed-3171-ac4a-d65ae31aea92 | -10.5358 | -47.73307 | 2026-06-22 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f23e637e-19bf-35d6-9fe9-bbebb93e69b9 | -8.61782 | -47.7949 | 2026-06-22 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcd13fa0-309e-3a14-a8c8-80584c11e0d8 | -13.29042 | -45.19755 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 009dde90-11ae-3223-816f-d47011448b11 | -11.09908 | -54.14971 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f021578d-4f4d-3f1a-ad81-662e0be901e3 | -11.06024 | -52.48672 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0b147b5-20d1-304a-9240-e55207ce966e | -10.05494 | -48.09045 | 2026-06-22 04:06:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cc38b19-40dd-375e-be4e-73370d67b48c | -10.90946 | -46.3209 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b64ab6f-d4ac-3b91-8c8a-3d4ae74eabd9 | -13.28704 | -45.19326 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33fd6e00-a83e-3e57-9696-2406f8d24e79 | -11.1079 | -54.14381 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 577b4267-a2f5-357c-9626-851d54b20933 | -13.37168 | -41.35033 | 2026-06-22 04:06:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 326032bd-18e4-333e-865f-a62fe7b553ae | -12.07021 | -48.42725 | 2026-06-22 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf2083f8-77c4-39cc-aa48-31800cfcff8a | -11.84783 | -41.30757 | 2026-06-22 04:06:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 54a3ec39-d8a4-369a-aec4-60798dac770c | -10.56863 | -46.23397 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8a5762e3-acd2-3205-8400-5e41679dc7dc | -8.61704 | -47.79485 | 2026-06-22 04:06:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6ace4280-2fb1-34a6-9db0-cfe42412daad | -10.56332 | -46.23765 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 483cdc07-4591-3811-bd96-32ee936d11f3 | -10.56246 | -46.24237 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8d580e5a-1abe-3dc8-a941-8541d6445ed5 | -11.05027 | -52.48384 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d056bac4-a622-3139-bfbd-69008935c99e | -9.07927 | -44.75307 | 2026-06-22 04:06:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6ba45abe-66ed-3b35-96b3-d2c38dbe76c0 | -13.29319 | -45.20539 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86fdfc54-2764-3910-94e8-25d288950a9f | -7.9592 | -47.42062 | 2026-06-22 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2a86a550-0360-352d-b882-8bfbac4a8c7c | -11.04817 | -52.47827 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b9b5b50-b261-36bf-86d8-a2ffd3a4644c | -9.49968 | -42.99405 | 2026-06-22 04:06:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eab41ec1-14bc-3611-8283-4861176a4b64 | -10.93858 | -46.42393 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 09c81d08-d884-33ed-89d2-c75ff62629a1 | -9.27271 | -40.49024 | 2026-06-22 04:06:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f232d259-327f-30a5-bd11-b3c2818dfc40 | -11.11351 | -54.15323 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 104c5ad4-e37a-3711-a59a-85d8239131a0 | -8.88351 | -46.94339 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e449a9c6-8529-321a-a447-8114ef480482 | -13.2898 | -45.20111 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 688fb6ef-f6e8-3a66-bf19-a22e6de7ae62 | -13.29721 | -45.20612 | 2026-06-22 04:06:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e5e1928-82c8-34d4-ac9d-60a96354c567 | -11.05812 | -52.47912 | 2026-06-22 04:06:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be103587-97ab-3854-b90c-68be56f651ef | -11.10861 | -54.1433 | 2026-06-22 04:06:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 190658bc-d7fb-367e-b07e-38b2dc73c172 | -12.06675 | -48.42872 | 2026-06-22 04:06:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a1cd79c-dc6b-352f-ba61-e6e1cd9d0826 | -7.96324 | -47.42734 | 2026-06-22 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9f43890a-c536-3528-b7e3-7a08a82551d2 | -10.17808 | -51.65937 | 2026-06-22 04:06:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f09d0be1-6cde-3176-9ae3-fd3c82568591 | -7.96377 | -47.42442 | 2026-06-22 04:06:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 95b74df1-aca2-337d-a45e-02acfa26b23a | -10.17701 | -51.66469 | 2026-06-22 04:06:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4b41c6a-f37a-3122-b0f3-2d160866393b | -13.56318 | -43.51089 | 2026-06-22 04:06:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2695094d-56aa-3baf-a450-49f864ab51e6 | -10.90576 | -46.31565 | 2026-06-22 04:06:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 543b8811-8a12-3c7a-b63d-b396f4d99185 | -8.87187 | -46.95213 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d1da7330-e690-3882-b39f-b084e61c8c29 | -8.87868 | -46.94238 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39473629-a66b-3948-adf7-2ef0d48287d5 | -8.87343 | -46.95541 | 2026-06-22 04:06:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19e55924-c9c5-3989-9175-cba4d5e61fda | -10.53686 | -47.72729 | 2026-06-22 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 241dbf8e-604e-370a-85ca-b9a291334345 | -10.53894 | -47.716 | 2026-06-22 04:06:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README4.md)
