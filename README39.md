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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9e80f32-cce6-35ee-885f-a49e155b3b68 | -3.82182 | -47.74245 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 23bd5c08-2a94-3843-9c14-0f37292530bb | -6.2732 | -44.96249 | 2025-08-16 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd2b01a9-f61d-3696-92b9-b24ce2a70c8f | -6.56064 | -43.02831 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 87801dbe-4f6c-3df2-836d-fd5c807786b6 | -7.4163 | -44.90966 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c2d2eb3-e561-3dac-b4c5-708b174d692d | -2.93144 | -47.76524 | 2025-08-16 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba138deb-cff8-39e4-b4cc-a318642c4ffd | -3.23122 | -50.80661 | 2025-08-16 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 252047e2-e996-308b-a6a1-6593219e2442 | -3.88235 | -54.2156 | 2025-08-16 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55857d56-d6f1-3db8-a40b-8a03274c3c22 | -7.59567 | -45.20694 | 2025-08-16 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5764f7a7-86bd-36c5-9fd8-2ce193cdddcf | -3.98106 | -43.24099 | 2025-08-16 04:32:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86d01275-57c8-37e0-b70a-e73654052f3e | -7.07037 | -59.2325 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 278540a9-5813-38ab-8604-06771b4fd1fe | -8.80157 | -52.07043 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc1adcee-8460-3ef7-b036-5eaf2de372b5 | -5.75646 | -46.67068 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55db3aca-202b-3d99-9f84-0d2f3a988694 | -6.68313 | -46.71202 | 2025-08-16 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ff7e81cf-818d-3752-96e1-7f9ff729033c | -7.59505 | -45.21109 | 2025-08-16 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c2e38c9-9be1-34df-b6a9-d6c7de2272a9 | -7.12437 | -59.65963 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6ec061b-8c62-3769-9cf8-7845a860c32c | -8.29281 | -44.96901 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef4851d3-0c31-3355-9aea-145f04e83a73 | -5.86397 | -59.91946 | 2025-08-16 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d11c322f-48bf-3778-8adc-e55d8f6c9b2f | -9.70547 | -46.26601 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38dcd4d9-1c24-3d6e-8f6c-3d127ae4e43f | -9.36021 | -47.98973 | 2025-08-16 04:32:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1264f4b-70a1-3fed-9fb7-50e3d29fba2f | -7.39217 | -44.89721 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42152778-2240-3ec7-9e16-9d0e2ea7cb28 | -7.52095 | -61.32029 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9d6fd70d-9718-3bf4-81af-b7bdf840de00 | -6.65802 | -58.81762 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1562d1df-269f-3182-8259-33af72e29b3b | -7.56349 | -61.43481 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bbe37a1-3d41-3e75-a4c5-bf7b0c7c3b4e | -6.56465 | -43.02894 | 2025-08-16 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 829b647f-8b96-3398-b084-e05a591990e9 | -6.95831 | -42.86136 | 2025-08-16 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| c26e3cd6-a411-3484-99eb-af6dbed565b8 | -7.80939 | -61.33323 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 999d1365-c6a8-386f-b290-626b239b7756 | -6.94151 | -59.52142 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ad1e18a5-5696-3a49-9335-f3220035704c | -3.82567 | -47.73951 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| beb398c9-8957-31a4-932c-d9267fd2ab44 | -7.41993 | -44.91016 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 89089f0e-820e-36af-9ea2-ddb4259fc2fd | -3.17579 | -48.76728 | 2025-08-16 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 84ca9a69-5a2d-3c70-99ca-fe683e5d0a60 | -4.47883 | -47.66976 | 2025-08-16 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 761f8354-fa2d-3def-8367-c2ee2986d055 | -8.19321 | -45.03391 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a48026a-f7da-3631-8682-f71ab1162f88 | -6.35369 | -44.6957 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e8eb405-8b16-3908-82c5-9497081d2861 | -7.85608 | -48.16167 | 2025-08-16 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70fa6570-4dca-399f-944e-2c482d2102d2 | -7.90727 | -61.75459 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd36be44-7a35-3899-8163-e630f1c3ef36 | -9.98977 | -48.54435 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 90cddbcd-cb03-34a0-968b-3e7f55426a63 | -6.93187 | -59.53936 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3fb021ea-6b0a-382d-b008-dd872f553022 | -9.70198 | -46.26546 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a16a99ad-5e0c-3499-ab48-249c3bc9699e | -6.94163 | -44.56233 | 2025-08-16 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6019ae78-9ee6-3b4d-aa6d-d00e59cf56c4 | -2.60528 | -51.94804 | 2025-08-16 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8524f887-712e-3ac3-b69d-787b40688c36 | -3.2349 | -50.80722 | 2025-08-16 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8f7dd46-bec1-364e-9626-011d7aa252e7 | -7.35986 | -43.83506 | 2025-08-16 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5f6f273d-6a8f-35e8-8809-83cca0d42786 | -5.06189 | -43.12116 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ddc62d4e-c4b1-3c6e-b92f-bd43f213d6f8 | -2.90631 | -48.24734 | 2025-08-16 04:32:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a288e3a5-b6a7-3383-b284-ae65ed0c8474 | -8.19513 | -45.02121 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19902426-9fc3-3206-8d26-9dcba1a6c8cd | -8.18721 | -45.02434 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4735f0d-b4fe-3d9d-83d5-9492a3b6f7a5 | -4.91621 | -43.26579 | 2025-08-16 04:32:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d7e7eeb1-9a8b-32f8-b21f-d1188367497f | -3.82622 | -47.73606 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e74c342c-05cf-37a6-8dac-966ee67ae115 | -3.56072 | -47.3737 | 2025-08-16 04:32:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8389a4df-92b0-3348-b78d-3c6bd0f0ba8c | -7.40859 | -44.88678 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 556525d8-ed4f-366e-9f17-58c134eedba7 | -8.80736 | -52.03545 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bc9c01c-a266-36ee-a953-41bac6fb38aa | -8.81032 | -52.04039 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 014a3f8b-d82f-380c-8ea1-93c5375f9978 | -8.1823 | -45.03225 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff315d41-fd3a-365d-8ae3-416ace9ff6bb | -7.81612 | -61.33463 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c041344e-213f-3344-b7f7-85bb1f9b3774 | -3.26505 | -46.92155 | 2025-08-16 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 863dbfbc-564d-3a50-9f88-b3b013de43c1 | -7.37142 | -43.83683 | 2025-08-16 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86ea874f-d92a-3468-adaa-c40878467385 | -7.55309 | -45.41658 | 2025-08-16 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a79fbd02-9454-39e6-8b5c-b59040b8d6ee | -9.70488 | -46.26992 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1099290-ad54-3a90-91f0-7704ef8251f1 | -7.14605 | -44.3912 | 2025-08-16 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2c08ccb9-8118-3025-9c07-9370b64f1711 | -6.54085 | -44.54428 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| be5ecac5-834d-3d09-81fb-9392f2d773ba | -6.51078 | -44.21748 | 2025-08-16 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72d356f3-ac2c-3f3a-8036-01459d66e69b | -6.94595 | -59.53188 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10c089d1-712d-3205-b156-9c2fd9901037 | -6.5372 | -44.54367 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce65b4a8-2c83-3c48-8d90-0eb3a713342e | -7.01009 | -44.31063 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06e6acb4-4d40-34dd-8df3-2e9723536110 | -6.65133 | -58.82088 | 2025-08-16 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f161109-7bac-3eb0-ad6d-a8098687eedd | -7.52656 | -61.32763 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b73c1ef-bf8e-362e-87d4-46b9aba7cc87 | -8.11049 | -42.35517 | 2025-08-16 04:32:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 730a3428-5f58-30bb-b7fb-c2fd64e5dc11 | -5.70239 | -45.87025 | 2025-08-16 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b649dff8-fb80-36e2-a302-19188877eef1 | -6.96186 | -42.8656 | 2025-08-16 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 69c245b3-55eb-36be-a19c-7cd514c0ad25 | -7.82404 | -61.32974 | 2025-08-16 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fcfb03a7-343e-3f51-bd47-b3abfa5b05fd | -6.95778 | -42.86501 | 2025-08-16 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 276f6d22-b47d-3db3-b23f-b97d46c3c18b | -6.93627 | -59.55008 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e750939-3e0c-3aff-806f-38c6d623bde7 | -2.72087 | -47.44196 | 2025-08-16 04:32:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aec18441-63f5-31c4-a4f4-a61a37a0b893 | -3.37777 | -52.71489 | 2025-08-16 04:32:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 182cabbf-2470-3f38-bdc9-dd25006940a6 | -3.3819 | -52.71563 | 2025-08-16 04:32:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e2246cf0-bdef-3a44-abf9-bfabe48b83e0 | -7.36057 | -43.83027 | 2025-08-16 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48857238-aef9-3e4f-b151-1a6c3e2b152e | -6.45218 | -44.56174 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fb09eca-cd76-3caf-b20e-b6fac719fa30 | -7.52641 | -61.32113 | 2025-08-16 04:32:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bd1726d7-1fa5-3ccf-98be-3f15f09c2869 | -8.19085 | -45.02489 | 2025-08-16 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50df839f-7ab9-3c65-8a33-f4b1cdf1de1d | -10.23725 | -48.30791 | 2025-08-16 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1459b7e7-7aec-3837-96ec-25960301402c | -8.99678 | -49.87112 | 2025-08-16 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 532cca80-d59e-3e39-ab0f-5e54cd9eaee9 | -6.35669 | -44.70041 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0c1cb3c-cb43-3013-8df3-8ad39b7a41a1 | -7.24036 | -44.78713 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1109889-a5c4-386b-84d9-f8dfad1bf7e5 | -7.40069 | -44.88988 | 2025-08-16 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 931523b0-18e1-372e-a9d4-e892c17dcc12 | -6.21728 | -44.46103 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a7bbdae-767a-3ebd-8749-8231a839efa9 | -7.20215 | -46.22812 | 2025-08-16 04:32:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b52b2344-8507-3184-acd4-95849630921c | -9.85076 | -44.68351 | 2025-08-16 04:32:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 606b03d4-cb76-31ac-92c1-96012566adea | -4.28689 | -48.06749 | 2025-08-16 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e64bffe5-94e5-33ec-9fb3-89988f23f385 | -9.33945 | -45.98359 | 2025-08-16 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8d0774e8-e89f-32d0-ae52-f0f025371782 | -5.76371 | -46.66817 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d3c2860-fc20-369f-ad65-317decfa3047 | -3.43171 | -49.04896 | 2025-08-16 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1981fcb2-ecf5-37d3-8cc2-6a4df5ea9934 | -6.9451 | -59.53654 | 2025-08-16 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cae82b9d-0215-3ef8-bd6a-d9e92be7273d | -3.65173 | -48.32449 | 2025-08-16 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2bcb19-78ee-3637-aa6f-f074f70960e3 | -9.81026 | -48.54107 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7e45dbd-2cab-33c0-aae9-c4a864f25b67 | -9.80695 | -48.54054 | 2025-08-16 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 663f4108-99a3-3ed8-945c-362f156cace6 | -2.66613 | -48.55546 | 2025-08-16 04:32:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1c32cb8-16be-3261-9bd0-94a268bc55e4 | -6.35008 | -44.69508 | 2025-08-16 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 628ada0b-f42d-3095-a52d-927239b84dfe | -8.80961 | -52.04468 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d13b1584-27dc-3173-8234-48e95482da30 | -5.76315 | -46.67171 | 2025-08-16 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67296484-03a2-38f1-b4e9-68da777a707a | -8.8037 | -52.03479 | 2025-08-16 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README40.md)
