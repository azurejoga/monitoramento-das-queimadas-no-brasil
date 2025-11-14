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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b3438ec-b52d-31a3-8467-97146c7d7535 | -5.41497 | -43.25935 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da07412b-ebfa-33ba-b698-dddbf7dc3225 | -6.4909 | -43.96048 | 2025-11-14 03:53:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3dc57866-af1f-3768-8637-cc48820db56d | -7.77912 | -48.05424 | 2025-11-14 03:53:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af3a23d9-3197-3bd7-aba5-a8b690bf6d0f | -7.29176 | -45.4643 | 2025-11-14 03:53:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 466d19f4-7cb7-360e-ad80-57c9d802d5bf | -6.0985 | -41.60235 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 43be6944-9b9e-3b81-afe3-7aefd2e8851b | -6.11148 | -41.59158 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5b99bdab-c924-35d0-9330-25265ef4d1e4 | -6.14823 | -48.0528 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4c1226a3-ff37-34c3-8624-5104c966bc78 | -5.75509 | -45.10315 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f556700-24f9-3458-ab9d-fca22cf60fc9 | -4.2197 | -49.11708 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f68a796e-52b2-38c0-9159-ee911f00e1cd | -6.8126 | -40.08921 | 2025-11-14 03:53:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 154299e6-fdd6-3e8f-8ff8-774352df1d46 | -6.09919 | -41.59806 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c00296ff-9300-30db-8dd7-281d24ead14d | -5.97527 | -42.58988 | 2025-11-14 03:53:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bed4a3c1-79af-3e5d-a4af-4a7b4d24003b | -5.45785 | -47.10094 | 2025-11-14 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1da94ccc-9164-384c-a268-9c86b7270f5f | -5.7423 | -42.72929 | 2025-11-14 03:53:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 348a088b-e73b-3ac2-9c54-8f973e54778f | -6.15522 | -48.04584 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6bb2d7f8-ed03-30d5-9f44-510a5182c2fc | -7.14256 | -40.46088 | 2025-11-14 03:53:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f09bd67d-1e59-38e3-8a90-2a872f3ec9ac | -9.05003 | -40.65849 | 2025-11-14 03:53:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2cbf0b9d-330d-3edb-8faa-6969b4c19427 | -7.88581 | -44.32269 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce968cf7-c505-3a12-80ec-a0a43598f575 | -6.41562 | -39.75295 | 2025-11-14 03:53:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5bc6a366-6a9e-3211-ac38-b3a0d574d5d8 | -6.14891 | -48.04902 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9bb5b53d-1bb2-3fc6-a80f-2edde50892b2 | -4.10666 | -50.05582 | 2025-11-14 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ac87bd38-42f5-32b6-8efd-71729800bf92 | -7.85908 | -44.30204 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07d6abc5-5451-3a3a-8365-98edc3529a7e | -5.53431 | -43.67863 | 2025-11-14 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae2932e9-8e2c-343f-885e-1535e66a9899 | -7.15406 | -44.9722 | 2025-11-14 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 533e33c4-8a2b-3bb5-a602-8d915a1b72af | -5.45844 | -47.09756 | 2025-11-14 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f84ff95b-9cb1-36f4-9fc6-372238b6c0e8 | -6.88591 | -41.58159 | 2025-11-14 03:53:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 8adf0f12-8a57-3831-93f3-078161b5af57 | -7.85452 | -44.3008 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 00271ee5-ea8f-3639-8bbe-e3e0170f60c5 | -7.44797 | -42.57272 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59d9ae31-dbb2-3bf3-ab4c-e3a9ed83d936 | -5.41436 | -43.26299 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7cfbc0a2-2dc1-34e2-8fdb-15b85621aaf9 | -5.60387 | -41.06696 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 700d21c3-8b47-3d06-a3a6-a49a06c0426f | -5.88982 | -42.2668 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 76bb2fe5-19a7-32b6-a5c7-d190761b5818 | -7.39231 | -48.65737 | 2025-11-14 03:53:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8da4f08a-cdb0-3dd5-8e23-c596eb34cf8c | -7.14714 | -41.70857 | 2025-11-14 03:53:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| cda840c4-057d-391a-ab1b-3be4fb80e87a | -7.15145 | -41.26027 | 2025-11-14 03:53:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4c8c3b6e-e02a-3aa5-afa0-ef31e6854297 | -6.16014 | -48.05045 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a845991a-05ca-37d1-a48b-2b7eb0f7a526 | -6.99745 | -42.78606 | 2025-11-14 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2d1cc752-5336-38b8-898a-faae0a8a311a | -4.57956 | -46.68283 | 2025-11-14 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09cb0b3d-9fbe-3b69-820a-1b5ee0c58287 | -4.59887 | -46.69572 | 2025-11-14 03:53:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ff0a62c-771c-3d2f-bf38-e8bd1c36b1c8 | -5.52594 | -41.75552 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9d6a6c5d-cec4-3f08-afc9-5730d1a23e4c | -4.7746 | -48.68297 | 2025-11-14 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a13afa7-badf-3275-a7f2-1c684f17235e | -7.46013 | -42.5699 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8174d047-4873-3a94-a36d-2d0d389bc807 | -5.63287 | -41.04631 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5dc1a35b-af40-3fbd-8dc4-e950cb4b638c | -6.07271 | -41.57641 | 2025-11-14 03:53:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fd9fd95e-e50a-3844-b0f1-ddc1c7d904d8 | -5.74622 | -42.72996 | 2025-11-14 03:53:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 67195bb7-77b9-34af-9398-c19374530233 | -5.72991 | -46.54919 | 2025-11-14 03:53:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23d30223-9070-384f-87e3-3473f30c62b3 | -6.09641 | -41.61525 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be1397c8-cbdd-31ed-a3a1-d5a9656421f6 | -6.88061 | -47.24523 | 2025-11-14 03:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0dd372f-9d2f-3759-9794-9657a76c1e03 | -6.28152 | -41.7459 | 2025-11-14 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dc1dde55-3218-350f-8905-68fdfff43559 | -7.72375 | -47.18985 | 2025-11-14 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6371072-cb4b-31be-9818-7b70e270ba45 | -4.80303 | -45.05352 | 2025-11-14 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3835a743-3e46-39bf-a643-da744836a531 | -6.99824 | -42.78122 | 2025-11-14 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f8a5bb33-b42a-3347-99f8-0926d3d9ee67 | -7.86613 | -44.31128 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec3e349a-f17b-3373-8cbb-aea0fee28c39 | -6.14642 | -43.71102 | 2025-11-14 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| afe1e2e6-8592-3218-9625-5b4528a8f54e | -4.29615 | -48.23841 | 2025-11-14 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 371a6ae3-895a-320f-be6c-65c67c277248 | -4.98728 | -43.88349 | 2025-11-14 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ea254e8-0f35-37d4-81fd-c953f4340243 | -8.30082 | -43.80578 | 2025-11-14 03:53:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a41973bb-cf96-3a71-a044-23f3ee1d5e82 | -5.53368 | -43.6825 | 2025-11-14 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e1d03fd6-3d35-3686-b216-1da71e5fb29a | -7.51129 | -43.01565 | 2025-11-14 03:53:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0dfaf182-b6f7-32fb-be19-682e253983f7 | -5.36164 | -46.28852 | 2025-11-14 03:53:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a131a52f-f8cd-376f-ad49-c645b81df9b0 | -7.09715 | -42.36861 | 2025-11-14 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ec1e1819-42b6-3e6e-83ed-2f2a58bd0cd8 | -6.24011 | -42.1185 | 2025-11-14 03:53:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b023ef62-fdac-300b-8539-add37bb8d33c | -7.36008 | -43.34871 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4a06112a-e162-3ce1-8434-c10d80223b0f | -7.35951 | -43.35221 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c5764841-6186-3830-8ea3-ef8400d82026 | -6.16633 | -48.04788 | 2025-11-14 03:53:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 33107fc5-a5da-3223-8023-2ca8655bedf7 | -5.41528 | -43.25949 | 2025-11-14 03:53:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 23d74041-fe35-3ffe-ab0e-bf6560d73cc2 | -5.65393 | -41.07502 | 2025-11-14 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d764cbdf-5ffc-3f23-9ce8-b91ce1ff7786 | -7.38731 | -48.65258 | 2025-11-14 03:53:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 892a70bc-0570-34b8-b73e-a51558fba41a | -6.47375 | -48.36821 | 2025-11-14 03:53:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2eb814bc-fb1f-369e-afda-e04b12937f64 | -6.8092 | -40.08868 | 2025-11-14 03:53:00 | NOAA-21 | ANTONINA DO NORTE | CEARÁ | Brasil | 2300804 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aa9da77a-dd16-3dbe-aaa8-827454930aef | -7.28292 | -38.80785 | 2025-11-14 03:53:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 69f5f2cc-17eb-3dab-baab-8272b010ec44 | -7.85162 | -44.29225 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b0a13c56-b5b3-3b28-bb77-3c67f71c3c6f | -6.88524 | -42.85575 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 38.7 |
| c762ae6f-d1a4-308d-87fe-71e4602fe689 | -6.89818 | -42.08606 | 2025-11-14 03:53:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 595a0a2c-1b7d-38cd-8b7c-e943e6e9b7b3 | -4.2189 | -49.1218 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 2c928702-25f0-31c5-aa80-5e70f38ceb29 | -6.4457 | -45.6622 | 2025-11-14 03:53:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbf9977e-3d10-36e1-9ae1-752de14e827b | -4.21871 | -49.11982 | 2025-11-14 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 982ba75b-d2c8-300d-bde9-af0473f2637e | -4.53835 | -46.41225 | 2025-11-14 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d20a6b7b-37ed-3fd9-b883-86def03bc102 | -4.70081 | -45.67928 | 2025-11-14 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e3d66c2-cd30-30e2-8635-a3c8325e23d7 | -7.62186 | -46.83482 | 2025-11-14 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c44ed69-579c-3d94-a760-f5e923caf671 | -5.53013 | -43.67791 | 2025-11-14 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12794bde-0290-3d72-a42f-94c8d57fde86 | -7.05789 | -43.58591 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2b2f497c-0aa5-300c-ac7e-f248864f4202 | -7.45331 | -42.564 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b033342a-700e-3a5d-a9de-2e804a17bc9d | -7.27961 | -38.80732 | 2025-11-14 03:53:00 | NOAA-21 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5cc721e5-f970-3e79-a3f6-563e25910163 | -4.80112 | -45.05541 | 2025-11-14 03:53:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98316a71-0522-3050-9f72-ee6bc89add2e | -5.52295 | -41.75046 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e5ad8e7c-4b05-3af8-ad00-2ea42cf0a153 | -7.46316 | -42.55143 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 7143c758-f0da-37e0-a542-1990d46c08cf | -6.2174 | -39.65135 | 2025-11-14 03:53:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 705dca57-7bab-3682-b579-d16a55e68e80 | -5.75432 | -45.10569 | 2025-11-14 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 30cfcfb4-53eb-30ca-bcea-b01abfea7c95 | -6.9744 | -41.63883 | 2025-11-14 03:53:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d7d37a19-879a-392c-a6ef-9e44aa2530bd | -7.85066 | -44.30063 | 2025-11-14 03:53:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| a2a13708-6421-3964-a493-a7cdd794c3b3 | -4.99087 | -43.88826 | 2025-11-14 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 118876c6-0521-31ba-885e-446ccfa5f782 | -6.72022 | -42.95455 | 2025-11-14 03:53:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| db9baeea-b8f0-307c-b909-de5126c19056 | -6.10648 | -41.59938 | 2025-11-14 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cc5fc8bb-8234-308a-95ec-835796982822 | -4.84138 | -45.62539 | 2025-11-14 03:53:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4651f19b-8231-3216-a6b8-a6336b1b4ea4 | -5.25608 | -46.18222 | 2025-11-14 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8dc3b932-6b50-3ef3-af0a-7eb75615393b | -7.08181 | -41.57796 | 2025-11-14 03:53:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b2185041-289b-3ca1-9a88-a4ac72dbd094 | -7.48663 | -42.55068 | 2025-11-14 03:53:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f118b3cf-ad08-3bef-91da-a278d795b8e2 | -5.37853 | -41.04586 | 2025-11-14 03:53:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e660b040-f4b5-3410-acea-2dfcd52ac10e | -7.34924 | -43.36486 | 2025-11-14 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e903b055-3d09-317e-99de-1aec252a5205 | -5.97833 | -42.59536 | 2025-11-14 03:53:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README16.md)
