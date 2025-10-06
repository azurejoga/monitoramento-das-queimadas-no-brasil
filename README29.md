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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dca3fda4-7ebd-3037-8c15-f9f0eeca31b4 | -8.56856 | -46.32922 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef7ff0a4-d970-378c-9f8e-dc2f62bb2a8f | -8.18014 | -44.23315 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6cdd5ce4-670a-38dd-bd40-644fa50b086f | -8.89598 | -46.03728 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe67f11f-3831-31e9-8059-337c4f708bc0 | -8.6169 | -46.3012 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d06d55d4-6cf6-3b77-adb2-a0de9f2c07df | -7.91467 | -49.26822 | 2025-10-06 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9baab947-4434-3a80-b425-223868e4cc76 | -8.61515 | -46.2689 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 968bbe5a-4cf1-3718-803d-4cc7db4945ca | -5.48838 | -45.54945 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6ab88f7-8da4-30fc-9f6d-ad14432b471c | -3.90878 | -52.25333 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02b26e98-4908-33f0-a7ff-4c28f17f1943 | -8.62306 | -50.01949 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2449a0ee-5408-3081-92a4-62d767f4d699 | -2.85676 | -54.092 | 2025-10-06 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1165399-e73b-3a56-964f-e0474cbbceab | -5.81516 | -45.47996 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a927db9f-4ae3-39c6-85c0-4929bb1360fa | -8.63506 | -46.31826 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aec2e571-aaf0-3a27-b944-bcde92087a52 | -7.24098 | -44.89841 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4635dfa2-ae6d-3c4a-84bd-8039cbc301da | -5.13636 | -45.16396 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eeb42a7c-260b-310b-b6a7-7c6321844602 | -5.41213 | -41.06803 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b181c228-c50e-34dc-8e12-8764906d03f2 | -8.18303 | -44.23759 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bebd10c2-adbc-349f-b0be-a2b8c2d6f6dc | -4.6511 | -43.18661 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd28b22d-128f-37fb-8501-5889d2a8189e | -7.66515 | -44.59713 | 2025-10-06 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59756308-63f8-3087-87f3-8912ca160acc | -5.76538 | -45.75573 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75ad7e12-2873-3510-a636-eee05dfa8499 | -8.19872 | -44.1674 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75ab187a-6777-3d16-9c34-5f2cc396480b | -5.26007 | -46.48668 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b41eaa77-31eb-3500-bd96-129c124892e0 | -5.09044 | -47.51285 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ca5ca2b0-dee9-3483-9d80-45b25f6f84a6 | -8.76234 | -48.80557 | 2025-10-06 04:25:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5f8c980-ab2a-3da2-98ef-bad3c53fc5f3 | -8.56996 | -46.25471 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d8ac9d3e-522b-30a2-b0e9-df2112c7796a | -7.71606 | -42.55242 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2cd9fcf1-fdaf-3cd2-a30d-185b872041f4 | -7.74943 | -47.40687 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be920d13-8faf-370a-ad4e-5d4f41f9025a | -6.33043 | -41.62273 | 2025-10-06 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 25708772-2ccf-3ba5-ad9d-584a9e67977f | -6.61457 | -47.54239 | 2025-10-06 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c4b5127c-d93f-3639-847f-e945dcef9902 | -7.01213 | -42.78792 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bda382db-b679-382e-84fc-2696762694df | -5.52486 | -44.20857 | 2025-10-06 04:25:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5496ab5f-ec37-311f-a2bb-fbfbd2ea3df7 | -7.81972 | -47.39304 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52e50e8a-bf56-39e9-a751-aa8a250c73c7 | -5.46008 | -42.80392 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 006613f7-4cc2-34f5-bd31-c8e098924e0e | -5.18008 | -46.21622 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938d8597-e589-326b-9e51-3a1ef100aa5c | -9.26769 | -36.85004 | 2025-10-06 04:25:00 | NOAA-21 | BOM CONSELHO | PERNAMBUCO | Brasil | 2602100 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c00be3c1-7410-313c-8d42-846f94f82f0d | -7.5993 | -49.89191 | 2025-10-06 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0244a6c6-2e56-3051-9116-628c86c1e3c6 | -6.83281 | -45.98034 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9800295d-f253-3a37-9fb8-e9d797c61ba9 | -8.86975 | -46.83895 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c976bd18-3dc1-3b1a-b07a-8795558f721a | -7.78543 | -42.60544 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 86f5e6c0-0191-303f-ad3d-3c030af0845b | -5.22442 | -42.97129 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5c173c8b-16a7-3ff7-87bf-45fa0c5139b5 | -3.55352 | -53.52814 | 2025-10-06 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f54575c4-4fe9-3896-8c2b-3c0c237d1aa8 | -7.21116 | -45.89069 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d587818e-e0d3-3711-985b-e45f5dadee01 | -7.68869 | -42.58151 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 963fc8dc-ec73-3831-9c08-1727c4a64986 | -8.62027 | -46.32307 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 372414e4-a464-3844-8cf6-9a6d6d16a287 | -5.67985 | -45.32299 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb3434fb-ee54-3069-8bc7-8677dc121efd | -5.77344 | -45.37732 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bf0b72a-348c-3395-a20d-ce06147b5f2b | -8.56335 | -46.25364 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5557248e-61b8-31bf-a5a1-45f767b47bc2 | -8.66754 | -49.55338 | 2025-10-06 04:25:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8e69ee6-cc5b-3b01-a5bb-b0888a7c47cc | -8.54629 | -46.25447 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 694d994d-8787-30d8-a7fa-2c14612a098b | -6.10074 | -43.42272 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40b70978-38d8-308e-9530-160fb838af63 | -6.64715 | -41.97815 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 21665943-d2bf-3a41-b05d-97ad53dcf6b0 | -5.22261 | -42.44259 | 2025-10-06 04:25:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| ff575cd4-9f7b-3904-bb0f-b81cb9d99b57 | -5.46073 | -42.79967 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| de78308a-28f9-3d62-a249-decc2e76d8d8 | -8.5705 | -46.25123 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8ba65081-1216-3ac8-8636-372aa18eb85c | -6.82851 | -52.50544 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6fc11b56-a55b-3d51-97c7-2f71cc6d0963 | -6.6635 | -41.59485 | 2025-10-06 04:25:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 33fe3664-c683-372c-a312-6a4c87c040e2 | -7.26855 | -47.369 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e072df5e-e4d9-3a7f-b388-ad247159b5bd | -8.19757 | -44.17524 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66c6f73d-f73c-37e2-b6d4-072219921fd4 | -9.31753 | -46.01671 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fc90347-33a6-3a21-9565-f27170fb017e | -8.63836 | -46.31878 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3fdcbc74-631d-3ceb-8219-150ddf4a46b3 | -7.19522 | -47.61715 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd0fd0df-9496-3774-b97c-93273c54b222 | -7.02757 | -42.78577 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9ffc1548-dacf-3ff1-be5a-cb8c9d1b8ffb | -8.19211 | -44.13081 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea80053f-24e2-361e-a3f8-acf45e7c1b80 | -8.74504 | -47.20279 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ac6264c-aafd-3840-b0f7-1788a48c3834 | -6.83004 | -45.97639 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c936b8a5-e351-3230-b6b5-3e38e93a208e | -7.002 | -42.83143 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 564998cd-f5a4-3ce7-93be-e9960c6dffae | -7.70397 | -46.26684 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6727a5be-f4af-3314-8086-528d2e2cea3d | -8.61131 | -46.27185 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 15ddb90d-c07f-3fb0-97fd-35edf787b42a | -7.11672 | -47.80862 | 2025-10-06 04:25:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99c28f5a-7981-37cc-ac63-4ebcd4adfa53 | -8.666 | -41.6743 | 2025-10-06 04:25:00 | NOAA-21 | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f7150461-d0b7-374d-852d-262b9743c82e | -7.48608 | -43.02685 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7fe033b7-c7c5-379f-9bfb-2f3ee89deae5 | -8.62796 | -46.31717 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 57403766-c3b7-3076-a5ee-1c67a5d49246 | -7.72527 | -42.38136 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aa872152-38c9-3025-8794-75833fdfae8e | -8.55634 | -47.25408 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 946863a9-01fb-3f97-bf66-f2f883012283 | -8.25789 | -47.01042 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a1b3c9c-2aea-3128-9188-576c3258c7b9 | -8.87029 | -46.83549 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d44b42a8-b04e-3777-97f7-c136568104bc | -6.05774 | -42.56227 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e53e6e21-c18f-38c7-8fa9-efeb42f163a8 | -6.18516 | -42.71438 | 2025-10-06 04:25:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45ca3a30-879b-35a9-bbfa-a97aa6b24c42 | -7.22277 | -45.90319 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 624c7cd9-ac20-36c0-86d6-2f75828d372d | -6.35889 | -44.30724 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 53d0547a-7d53-37e9-ab8b-1355824ffed7 | -5.33028 | -43.36842 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf82e556-4dee-3bb3-abb6-f9f812ab0369 | -4.47223 | -49.10207 | 2025-10-06 04:25:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ca54e71-52e8-3a84-a524-ff4b48b7a527 | -6.52277 | -43.62512 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9dbd810f-9a2d-338d-97e9-16cec2c4dc17 | -7.01774 | -42.29882 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 899faceb-b6cc-3945-b9f5-d903beb4413a | -8.19952 | -44.17616 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae7e42ab-6318-3d72-8e8c-789f09acc668 | -5.99784 | -44.34808 | 2025-10-06 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9ad5967-1f6f-3e16-89da-f58f35c7bd57 | -7.87293 | -44.13271 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 700d1986-9ffa-3476-826f-dd82b3c9d3d3 | -8.17755 | -47.66968 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f1200e8-40da-309a-bd5a-9de7ff7c89b5 | -5.69483 | -44.8318 | 2025-10-06 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9f4a400e-f925-34e4-a5e9-56bead49290d | -6.09193 | -43.98639 | 2025-10-06 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c1f4b72e-13f2-31df-bd42-79a915220091 | -7.43467 | -46.53183 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e896ac41-a47b-36b5-9147-cf204858bab8 | -9.32195 | -46.01012 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 25fdf031-3ebf-379b-9229-b073b23717c6 | -6.28629 | -42.93912 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5ac2ad33-b8cb-3994-a271-be2a941bcb62 | -7.78561 | -42.60801 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9ec4030b-24b5-3374-aa4a-a2db25b844de | -4.56621 | -48.60416 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fd50ecf-133f-3f11-85a9-7d2ba9702f3e | -7.71489 | -42.39929 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| f38ffbbb-5d09-3a3e-bad8-b7fc818d55f3 | -8.62634 | -46.32759 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 663709d0-1ed9-367b-a849-d222062912e0 | -6.7918 | -46.04826 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8ef97f2a-7b26-3821-be97-3fd817e7182e | -5.33123 | -47.28366 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 99d8e50d-7d4b-3cf4-8775-157ea651becd | -6.51315 | -44.48939 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1e70f0a-8b67-345e-82ae-4224b6b9aff4 | -8.51688 | -46.35267 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README30.md)
