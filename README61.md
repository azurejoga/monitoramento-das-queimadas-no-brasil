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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 367c8980-cd07-33e6-953f-1cfe76095148 | -3.0963 | -47.0183 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9e1737f-52f0-39fb-9d03-5c99e15e26c5 | 0.9916 | -51.24705 | 2025-10-08 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb0608d0-6baa-325b-a04f-71fa19dcbaa3 | -3.08888 | -50.57047 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2db764f8-fd48-3b17-955b-d8a50f00b7e5 | -3.1433 | -50.2953 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b771b539-b653-3c76-91a1-86ead8ed18d3 | -3.7396 | -44.26575 | 2025-10-08 04:36:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f84f13e5-5c03-3ed2-8d3c-ad446720d4da | -3.43128 | -43.14658 | 2025-10-08 04:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39d3deda-7d11-3cd1-8f3a-1a8ed417063c | -3.258 | -49.12402 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bba7103-f4fd-3883-8579-463dfd7294fa | -3.08768 | -50.57794 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8808c2e-eb1f-39cc-9047-fdbf6ffee4fe | -2.82446 | -51.38326 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17c4fdce-7832-3d44-bf7b-571362ce1ea3 | -3.12388 | -49.21974 | 2025-10-08 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af2c25bb-85e1-378e-b9cc-b573b0707f28 | -3.12148 | -48.78431 | 2025-10-08 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab548623-5cba-3a8b-ae62-7a27987ae248 | -3.1008 | -47.01162 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8519a58-5569-305f-8862-2d6f063e49be | -2.88471 | -50.7318 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce05e6a5-a795-3ed8-9f60-5cb178680295 | -4.05148 | -42.51405 | 2025-10-08 04:36:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 05c6e5ec-f5a3-3c62-9d41-90e2a6d7cb0e | -3.11432 | -48.78671 | 2025-10-08 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bceca56b-bc3b-3019-85fe-5c4b18b3581c | -2.5337 | -48.24503 | 2025-10-08 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1934fc33-4c66-3aea-9b54-6389f0ef3125 | -2.30156 | -48.145 | 2025-10-08 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b16e7ba-10b0-3ecd-afbf-886f6a27ff5b | 1.21043 | -50.68584 | 2025-10-08 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 32a6ec31-b885-3181-ba42-7f3621d52bef | 0.93519 | -51.12069 | 2025-10-08 04:36:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d4dd33c2-8e6a-3478-b315-53b093db4756 | -3.19811 | -51.02228 | 2025-10-08 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 38151dbe-f284-33a4-8495-b1545f4590f0 | -2.90201 | -50.73455 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd5eb4a2-47f7-3cb3-8b59-5e8a65c30132 | -3.14213 | -50.30261 | 2025-10-08 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1573ce82-f5e7-3ea5-9391-71f06fe7bbe2 | -3.24021 | -46.79079 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c18be7ef-2a45-387b-9688-24a7c3277f74 | -3.90118 | -44.90621 | 2025-10-08 04:36:00 | NOAA-20 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3eef7a53-1776-31cd-a8a8-8ed589bf846d | -3.24078 | -46.78713 | 2025-10-08 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7dd22920-625d-36af-9b0e-044e384d29e9 | -0.90136 | -47.54477 | 2025-10-08 04:36:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b72df02-7187-3a47-af7a-7b0ee3871a0e | -2.51885 | -51.92801 | 2025-10-08 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c236b10d-786e-30ec-8200-8bd192047ba1 | -10.22039 | -48.17116 | 2025-10-08 04:38:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b99d003-26a3-38b9-a0b5-3f2767080505 | -10.48052 | -49.37199 | 2025-10-08 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 522c3bbc-01f4-3937-8853-056044a0e254 | -4.68351 | -49.49822 | 2025-10-08 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7742181-52e4-37ca-8df7-6a16bbd3c874 | -6.66011 | -41.3879 | 2025-10-08 04:38:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b316625d-0b25-38cc-9208-65682fc33810 | -6.21812 | -44.30004 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed23e6f4-ef82-35f4-93ad-b30726953060 | -8.78679 | -48.00206 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a21b5ce-5640-36d3-a9c1-90ac085064f4 | -8.40893 | -49.7213 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c0f53fe-7571-3a60-8449-e3d6f6a54dce | -5.86085 | -44.30387 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00b1f201-4879-34d1-82d4-71557bb9c999 | -9.44744 | -56.65601 | 2025-10-08 04:38:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 861241e5-84ca-377f-9028-582a952dc794 | -8.88862 | -46.03096 | 2025-10-08 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c80fcaf-8972-323b-b754-139191ef8223 | -7.44754 | -43.12894 | 2025-10-08 04:38:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f6ea38e9-ddb1-3fb8-81c8-61ac468fa5f6 | -7.22957 | -47.1741 | 2025-10-08 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 624ea95b-aa2d-34da-9282-31d0f67d4c5d | -7.15619 | -39.3138 | 2025-10-08 04:38:00 | NOAA-20 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eeeaff03-f6b6-3200-a68b-0a90614f8ee5 | -8.15454 | -50.16887 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3e20ae3-701b-38c8-b615-bd6dc8d3d340 | -6.28017 | -45.31902 | 2025-10-08 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| badaf2b2-aac7-3683-9f3f-b7f2ed8bd86b | -5.91733 | -44.19746 | 2025-10-08 04:38:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51e2f059-f60a-3540-8310-34141d7d26ae | -7.76142 | -49.54044 | 2025-10-08 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23ca1d32-a3b0-304c-8507-6e27ec4dd563 | -4.05036 | -47.5009 | 2025-10-08 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2389cce1-1a8d-3534-82ea-224ade820283 | -7.42858 | -46.6273 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a292387-ec85-34ed-9522-768daeb9c06f | -7.77078 | -44.1931 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a23acb2f-b6bf-36ea-9791-81b956c2a57b | -9.77562 | -48.28756 | 2025-10-08 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4757f179-30da-3a98-8eae-652ed5b25fb4 | -11.66958 | -46.40361 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c088a703-96bb-3619-9a40-9aec7e72fde9 | -8.56046 | -46.23326 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac74ba8a-299e-3304-9f09-add4b718ae98 | -9.7902 | -47.74825 | 2025-10-08 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 34663f7a-85d3-3dea-87b3-738e60758dc7 | -5.74238 | -44.51264 | 2025-10-08 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6580dc59-adc0-353b-8435-b7fc130facd1 | -8.17554 | -50.16504 | 2025-10-08 04:38:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ff93d27-ee67-347a-879b-0861f607f578 | -7.78501 | -44.21124 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecc13df5-e866-3b52-a2f9-54ebbe4aa896 | -9.21176 | -46.90192 | 2025-10-08 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f5a8629-1443-3e3b-b5d4-ddef14619d3f | -8.56415 | -46.23376 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 362d6711-1b84-36ab-8196-c5fe712e0ebf | -10.61527 | -48.65583 | 2025-10-08 04:38:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 972b6038-eb7c-3c59-a439-08beb2ed6248 | -11.70055 | -46.35021 | 2025-10-08 04:38:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8459b130-024a-3f9c-94f4-9fa286f382bb | -10.40342 | -50.23388 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 66c693e8-c50d-372a-b089-22221fefa873 | -10.46685 | -52.16611 | 2025-10-08 04:38:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cdaad45-c019-381d-8f10-8830db84dce9 | -6.064 | -44.32241 | 2025-10-08 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 743ef1cf-90ac-3d3d-80e6-e574a7103e56 | -7.81212 | -44.14156 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73524907-1050-3c57-ac92-d8c96fd62db8 | -5.14279 | -44.96149 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 4994222e-ba57-3c2c-bdfb-c9aa6a6a7722 | -8.46601 | -47.20241 | 2025-10-08 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 986017bb-198e-3084-a333-8f2067f24234 | -11.18755 | -49.78112 | 2025-10-08 04:38:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e598c102-ccae-3c95-b25b-192680e83eaa | -10.3946 | -50.22529 | 2025-10-08 04:38:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 70f0bfc1-f98e-31f3-9d00-4cd19b7794c4 | -10.85736 | -47.11825 | 2025-10-08 04:38:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 331920f1-c86f-356a-8782-b12679949640 | -10.8308 | -49.3912 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5609fe1-70b0-3a23-859f-960de598bdb2 | -7.82056 | -44.17031 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7e128998-289e-37dd-afe3-dd276b5100ce | -5.35985 | -44.44568 | 2025-10-08 04:38:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b407114e-8e9f-31fa-ba06-2e40440fd1d5 | -7.39334 | -45.18708 | 2025-10-08 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 087dab3c-c132-30a3-9c03-b56c950c1b67 | -3.83607 | -50.96704 | 2025-10-08 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7073881e-cd23-30b7-a735-e44ced9857a4 | -8.62021 | -54.99113 | 2025-10-08 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3ae1f27-1ef1-36fb-bf91-2dd4ffab48ba | -8.39393 | -49.70823 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 029565cf-700f-3ee6-b12d-790b29234924 | -11.78954 | -45.11594 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0a836595-d536-36f5-bb01-5cb79797e995 | -9.63648 | -55.13071 | 2025-10-08 04:38:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e107501-f7ed-3a42-952a-4a76f2fc235c | -5.73599 | -45.26171 | 2025-10-08 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ad83857-81b1-3c39-9f47-16791216349d | -11.78651 | -45.13736 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6374a56f-e5df-39e2-b72d-7275c5b744e4 | -10.48162 | -49.36491 | 2025-10-08 04:38:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 484e7b34-00d6-3571-bffb-b137acb1cddd | -6.36879 | -41.62191 | 2025-10-08 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 54f1b652-2cb8-3219-b93d-37d9e2309412 | -7.34842 | -43.86224 | 2025-10-08 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a13965dd-2c41-327c-95be-e4fbd17cd111 | -6.59575 | -59.12218 | 2025-10-08 04:38:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 438f08b4-2a4b-3f78-a19a-573a6b9dcf29 | -4.91896 | -45.0866 | 2025-10-08 04:38:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bddd0b37-d2ae-3c26-9061-62354913fa25 | -11.29662 | -44.92417 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f823a2a2-0add-3177-b0ce-8c4d480ba452 | -4.68558 | -45.83702 | 2025-10-08 04:38:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fafc13ea-fbb6-358c-98f2-13c7ec212ecb | -8.54335 | -50.15989 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b00c41dd-0cc9-3572-b209-617c3b797589 | -5.71596 | -44.66492 | 2025-10-08 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d27e8e9-4560-3844-bc34-3fcecdc7d00c | -8.22715 | -44.16936 | 2025-10-08 04:38:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 39c30bc3-bfab-39f6-924b-b808be1b8101 | -8.56479 | -46.2295 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f1157fa3-bebb-322b-b9de-bec9293b0772 | -8.52592 | -46.26336 | 2025-10-08 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bc45347-917f-3270-9158-3324bb1ba5a4 | -10.83469 | -49.38818 | 2025-10-08 04:38:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1d2e33f-4006-3624-8c5b-86898e509eb8 | -5.76887 | -45.74174 | 2025-10-08 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f82b0e1-8084-325e-91f8-e42627d7e370 | -5.30379 | -45.84784 | 2025-10-08 04:38:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87d965c0-ebd2-389e-a552-db657b0af5d1 | -11.79463 | -45.05043 | 2025-10-08 04:38:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a054f74d-69e6-39a2-a5cb-225366102db4 | -5.27218 | -49.51305 | 2025-10-08 04:38:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fd42ab9-d76e-3f93-8d7f-9796d9c0122c | -9.18484 | -47.80027 | 2025-10-08 04:38:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2731f72a-c840-3303-a9d7-49939fec30b5 | -5.36571 | -40.99865 | 2025-10-08 04:38:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2626ddc9-9254-3e86-b9f8-7b9f6ead783f | -4.26506 | -48.55543 | 2025-10-08 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b1505e5-86e9-328b-90fd-b9a0bf3d9390 | -10.7508 | -47.87266 | 2025-10-08 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63d62498-de76-3b02-8520-2a534123871f | -8.41445 | -49.72929 | 2025-10-08 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README62.md)
