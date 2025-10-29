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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 260fa26f-f83b-3355-965d-3d954a3d6592 | -5.65416 | -47.82659 | 2025-10-29 03:53:00 | NOAA-21 | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07002472-0b45-3877-8243-66a87e769666 | -5.33537 | -45.43188 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 066536bf-4e8e-3b68-800c-a8c6d082b52b | -5.50539 | -43.62228 | 2025-10-29 03:53:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb4b7bed-b9bf-3cf7-851a-f6ce15081554 | -2.41747 | -49.3045 | 2025-10-29 03:53:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8409132a-5067-366b-bca0-857d3c140846 | -7.93023 | -45.51706 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b0546dc-22c0-37ab-8a8d-0e34b5fb5082 | -4.23263 | -43.62393 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eda9dc7a-e0cf-3fc1-939a-132672097253 | -6.30243 | -41.88178 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 3adb95e7-73a7-390f-8187-ef14e5198f99 | -4.22446 | -48.56242 | 2025-10-29 03:53:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e13478e4-8374-3b3a-805b-5a4ef076e027 | -3.11803 | -40.99199 | 2025-10-29 03:53:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 0ddd2b21-c832-39ee-ba35-54bc682dce6d | -7.80002 | -46.44364 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7183767c-b1bd-3bc1-bbbd-805c408f65ef | -5.61429 | -45.18348 | 2025-10-29 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9e3108d-00d0-3e31-aa79-9737ed0ff131 | -7.44537 | -45.11814 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 181e7f53-9b17-3cbc-90bf-3cd7a60bd355 | -7.07443 | -44.95325 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d69578bc-8813-30e5-8240-8ddaa7170a04 | -7.86337 | -44.23446 | 2025-10-29 03:53:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57282537-3718-33b9-bcf9-b96fe4c86114 | -7.34487 | -42.46886 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 16a7e1fe-c1a2-3213-b9b8-1b1923410ba9 | -8.52269 | -44.09633 | 2025-10-29 03:53:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ad86cf0b-c463-33ca-8ea5-35a6a0734bb9 | -5.53455 | -41.70871 | 2025-10-29 03:53:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 31cd4377-e800-364f-a68a-f47beb809f34 | -7.60792 | -43.59819 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 22c30c53-0558-35ec-be0f-6e665f099ac0 | -4.75336 | -46.97864 | 2025-10-29 03:53:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56f8335b-0f3e-3a34-a9d5-9367366f5060 | -7.0937 | -45.2469 | 2025-10-29 03:53:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 074dac01-2345-3aed-987d-5d34eaafb219 | -7.96381 | -46.7421 | 2025-10-29 03:53:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f3d4fe4d-d0e3-36e5-8d99-25f96bdb365f | -4.92059 | -44.01556 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1ae89adc-d7cc-3212-b27e-8231e3314a04 | -4.92539 | -45.67022 | 2025-10-29 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e75bd6f-03b2-3a86-8b0b-795895a44635 | -7.80195 | -46.43272 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fab288c5-71b3-3e1a-93e4-5940c4b8b764 | -6.99885 | -42.79296 | 2025-10-29 03:53:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 54bf5419-43ed-30c6-aa80-497c47d4c20b | -7.12823 | -46.98217 | 2025-10-29 03:53:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d77b8f75-1331-3d45-9fe4-f8c013c3f910 | -4.86253 | -45.77525 | 2025-10-29 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ea9f4cb-e673-31fc-bcca-3d2dbe8e5f24 | -6.97525 | -39.1011 | 2025-10-29 03:53:00 | NOAA-21 | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 094d0fd9-a41d-3c40-8e5e-253fc22cb151 | -6.54174 | -46.76215 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b27e5187-a192-3a02-a919-4d0a881e44c2 | -4.35597 | -43.64003 | 2025-10-29 03:53:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4608a6da-ca76-3625-9793-4b77f4f10c5e | -7.45251 | -37.3301 | 2025-10-29 03:53:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 85f2f143-3cd1-3bf7-8e4c-d3573da3dbf3 | -8.13865 | -37.224 | 2025-10-29 03:53:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b304cb3f-cc43-3812-ba4a-a5fca34b0413 | -5.55092 | -42.70335 | 2025-10-29 03:53:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ea28bc9a-f7da-375c-92d7-b098d23f300d | -6.64954 | -44.60599 | 2025-10-29 03:53:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a73afd71-d43b-3ae9-9104-4cd62d5a586c | -7.60414 | -43.57194 | 2025-10-29 03:53:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b3e7eb73-526b-310c-ac3c-a749dcf9a3f6 | -6.16474 | -41.66837 | 2025-10-29 03:53:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 01220f33-3ff6-3db3-b989-52d5364ea765 | -6.21372 | -41.82764 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f002fec5-94df-3626-bf7e-647cc9912a8b | -7.49846 | -47.03912 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b39fa78-0fca-380b-b059-a54c52aa59cd | -4.47688 | -43.43738 | 2025-10-29 03:53:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 08f8d16c-d8c0-35b1-b504-eb0da26feae6 | -6.16706 | -43.7529 | 2025-10-29 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 30804773-a183-3c49-b134-61b7081bfef8 | -6.99665 | -49.00603 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c46c3c7-a1a0-32eb-8f34-43102439907b | -6.60806 | -43.3466 | 2025-10-29 03:53:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 661ad928-1167-362d-b088-1f3bbc558ffa | -4.93022 | -45.67108 | 2025-10-29 03:53:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30f3b154-c4bd-3ea2-8849-e375acd01ff7 | -2.77079 | -45.40598 | 2025-10-29 03:53:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 437b78aa-1d47-3848-880e-4f9c7c3b6d62 | -6.9179 | -43.49475 | 2025-10-29 03:53:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02b54811-75ee-3fb3-a604-4d53d6c934e8 | -6.11038 | -42.43535 | 2025-10-29 03:53:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0170d4f2-a0e3-3ead-960f-8aeb6551b6f8 | -6.09422 | -41.77744 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 43f808ff-5a42-3ecb-b3a0-2d987a0c4c3d | -8.61781 | -44.80194 | 2025-10-29 03:53:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e55e7fe1-52a3-30e6-916e-710a4a7ae502 | -5.0124 | -41.04455 | 2025-10-29 03:53:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3ed92e24-8665-3f7d-9f9a-64d4768858f6 | -6.64777 | -41.51777 | 2025-10-29 03:53:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4fea18db-7226-3ade-bcff-d3d08b396ebb | -8.55225 | -45.68523 | 2025-10-29 03:53:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b6d1ce42-4273-3439-83b0-98544f4808f3 | -8.02582 | -47.39615 | 2025-10-29 03:53:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d82b55a-8840-372b-b760-5878f5111b8c | -5.34056 | -45.54358 | 2025-10-29 03:53:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e52cd26b-0536-3d3d-a177-1526053debeb | -7.93042 | -46.00783 | 2025-10-29 03:53:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cb6c3c6b-8cdd-3df9-ad38-c6ee545832af | -6.16291 | -43.75216 | 2025-10-29 03:53:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3e09368b-6b67-3564-9f0a-f6b407f8711c | -4.69427 | -46.00153 | 2025-10-29 03:53:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c192e80-1322-3a0a-a66f-df679c3369d9 | -5.19032 | -44.35654 | 2025-10-29 03:53:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 84fd8f45-c2a8-34c6-b979-ed13b2db02c3 | -3.72193 | -41.5722 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c516a960-af16-3821-bc46-1fa642967f02 | -5.65981 | -41.10339 | 2025-10-29 03:53:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 127bf65f-f7a8-3a97-afcc-c11d6de651a8 | -7.07308 | -44.93462 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9c6459a9-fa0a-32e8-99ed-4223d3d64ce5 | -3.81067 | -48.65212 | 2025-10-29 03:53:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 884dea05-20e5-3382-bcf4-1c0c65079f7e | -5.48919 | -35.34606 | 2025-10-29 03:53:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 89df727d-f8e4-3507-9fc3-9873c8a466f9 | -6.20738 | -43.26548 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14a54dc8-9269-3fb9-8146-b8e4fbfc514a | -6.62917 | -47.18313 | 2025-10-29 03:53:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f9fd7b8-63d6-338e-8d82-4e874efd2b78 | -6.26227 | -41.80848 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de1e7452-2ffa-33f9-bf27-bc1cf2f18b2c | -6.54409 | -42.10966 | 2025-10-29 03:53:00 | NOAA-21 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 78b81766-bd46-3688-a93c-c56c39ce8088 | -7.20185 | -44.16142 | 2025-10-29 03:53:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f82011e2-defd-326f-ade0-18e2ae3a0a18 | -7.34934 | -43.91056 | 2025-10-29 03:53:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b7056b70-cab6-3752-b074-13307f49fcaf | -3.71589 | -41.5619 | 2025-10-29 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2527b126-0999-31f9-a42d-40dc48683094 | -4.20841 | -50.09085 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 27d25601-adee-3308-b899-96dd5917faec | -5.18517 | -44.36034 | 2025-10-29 03:53:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b829edbe-f85d-346b-b283-a9b29a111295 | -4.14596 | -43.35749 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e77f165-c1e0-31b5-a260-417fe82d1414 | -4.29383 | -49.64885 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 506e73de-b833-39f0-b98a-ef8d5ccf75c7 | -4.29305 | -44.48717 | 2025-10-29 03:53:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e05c9436-0397-3a75-a9de-b55b7deaeafe | -8.21664 | -43.80465 | 2025-10-29 03:53:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9cad4ae1-69e5-3b1f-8e3d-de5cbbe1f504 | -6.12039 | -41.70983 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6897081a-f3cc-3c9d-88ad-bffc5085604c | -6.2683 | -41.81287 | 2025-10-29 03:53:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8d872c59-2268-3809-919d-d62c0b8bf559 | -7.80194 | -46.46112 | 2025-10-29 03:53:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ebbcaf43-4ebf-30d3-b7df-736df54fad9e | -4.08511 | -46.94254 | 2025-10-29 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f177d386-4045-3ad0-9771-14703dec11d2 | -7.35461 | -47.63398 | 2025-10-29 03:53:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c151d28a-fd09-3e40-94c9-be0d23b70b01 | -8.61853 | -44.79784 | 2025-10-29 03:53:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffe0f894-41e3-32b8-a97d-6542d1f51265 | -7.89053 | -45.69212 | 2025-10-29 03:53:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 426633a9-9d0e-3b8c-b7a8-fa57ec59a81a | -4.14534 | -43.36134 | 2025-10-29 03:53:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cd0a705-2e10-3c47-bc03-0fbc4ac9a486 | -6.98477 | -46.2341 | 2025-10-29 03:53:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ebe53fb-401d-3cca-9d98-5b846181fd36 | -5.08743 | -44.81473 | 2025-10-29 03:53:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ee58acba-f2f1-3930-a108-09ff3236b55f | -7.98622 | -45.54608 | 2025-10-29 03:53:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cf0be147-7f0e-3ab3-a114-720b1521d38b | -5.89983 | -37.82169 | 2025-10-29 03:53:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 79df3365-b29c-39ba-a817-6ececfc9f437 | -4.27084 | -46.92453 | 2025-10-29 03:53:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 048af67e-7e04-31d6-97d0-cf4249d7099d | -8.66954 | -43.92363 | 2025-10-29 03:53:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f774ca16-add2-3fda-8c15-c1fb095e4cab | -4.84985 | -43.43806 | 2025-10-29 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6316e0c9-239a-3cc0-a2e7-f2540f58b2bf | -5.87845 | -42.59592 | 2025-10-29 03:53:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf26be39-fbc1-3851-9bbe-7e4aba549ed1 | -3.59738 | -47.51595 | 2025-10-29 03:53:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f07a78b-5a37-3a4d-9a9c-b6ab25912619 | -7.37217 | -42.44484 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 43b0d5c3-65a8-3aea-9063-a138e129bc5d | -4.66791 | -46.40039 | 2025-10-29 03:53:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb403b34-552d-397f-8b29-6acaf5e9588d | -5.48978 | -42.16799 | 2025-10-29 03:53:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| a347c093-83f6-3009-bb9f-f72ff8c1a56f | -4.21046 | -50.08126 | 2025-10-29 03:53:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 2042bbe9-6986-3913-8655-bb775dc7e8ec | -7.34129 | -42.46555 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 76e2dfb7-fb6f-3b83-8ad0-f1b44686525b | -6.28266 | -42.88153 | 2025-10-29 03:53:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8b4d1e5c-a91a-3a2a-8362-89df044f30f9 | -6.12107 | -41.70566 | 2025-10-29 03:53:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d6074505-d817-3a44-b6f1-c57056a653cb | -5.61424 | -47.11588 | 2025-10-29 03:53:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README8.md)
