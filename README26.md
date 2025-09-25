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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47ee1a75-442e-3b75-aad4-eebd03ee95fc | -22.36586 | -54.63678 | 2025-09-25 04:38:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f2240431-7ae2-3aea-9e1f-44c328a096a4 | -20.73528 | -57.85992 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ab6ed0f3-0ae0-3075-b7fb-2aad6fe30465 | -20.77849 | -56.91755 | 2025-09-25 04:38:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b63a964e-2acc-3790-8520-3954bdd8ccc3 | -20.24462 | -56.05704 | 2025-09-25 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a98a846-ed05-3fe1-a70f-c96e48d1b0e3 | -25.94186 | -52.05889 | 2025-09-25 04:38:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0898768a-eb6c-39a2-b415-1c7c40e301c4 | -21.83072 | -50.58029 | 2025-09-25 04:38:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4ce07c06-1190-3ebd-91a1-8900ef41e9c9 | -20.46992 | -56.65738 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6523dd51-64bc-34dc-bae5-b5e7264ea833 | -22.37764 | -49.48298 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 382aaaf9-d511-3c21-828c-d3600feba3de | -21.85897 | -55.95679 | 2025-09-25 04:38:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7334b5c-32b1-3f40-b581-9fb86bc8df80 | -20.70635 | -56.74517 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67d88cc8-1a64-38a6-a658-0d1882aee94c | -20.69609 | -57.82122 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d5af9c30-9e55-373e-8fa1-32dd23617208 | -21.976 | -49.50346 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| f50905ee-a147-3f3d-8ef6-944f921d08e9 | -20.76452 | -57.87089 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 78a20ef8-146b-3ebc-8842-fe137ffaf16f | -21.83405 | -50.58086 | 2025-09-25 04:38:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| df2a093e-e2d3-3b13-8f19-4a48eaa5fd4b | -20.70267 | -57.82095 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 39585386-2fbb-3212-8bd5-499436970099 | -22.70695 | -53.01247 | 2025-09-25 04:38:00 | NOAA-21 | MARILENA | PARANÁ | Brasil | 4115002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8588a418-f77c-3619-b07f-c2db2564b2cb | -21.98571 | -49.50918 | 2025-09-25 04:38:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7a328073-d968-33dc-b6f1-8a600e676cb5 | -26.06059 | -51.76727 | 2025-09-25 04:38:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 309b2871-2df7-3c5c-a7a4-637a23be32ef | -20.69284 | -57.86155 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4e2030f3-df11-372c-a7bf-5f7c675e0e9f | -20.7023 | -56.7445 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89348f5a-cf20-35ee-b673-b74dca24adec | -22.37018 | -49.48586 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3989bdc-d56a-30cf-8997-06c6f8474eee | -20.61552 | -56.71306 | 2025-09-25 04:38:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cef08c32-16d6-3966-9c95-f5dd96b21e87 | -22.60907 | -49.02035 | 2025-09-25 04:38:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b0170d2-5e17-3b83-9063-dbd6008b1813 | -20.70121 | -57.81781 | 2025-09-25 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 587b50e9-788d-3e5e-80da-f3312f94a5e1 | -21.83795 | -50.57766 | 2025-09-25 04:38:00 | NOAA-21 | IACRI | SÃO PAULO | Brasil | 3519204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2bdbd959-264b-3cf4-81f9-702787813f02 | -23.09503 | -52.44611 | 2025-09-25 04:38:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7f60aff7-403e-3ab4-90d2-e08a8330f313 | -22.37075 | -49.48185 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c1400aa-53cc-3a46-b6ce-e6465f2e82ee | -22.37877 | -49.47499 | 2025-09-25 04:38:00 | NOAA-21 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ec7b84a-502d-3188-88d8-9275c078e3a1 | -22.41112 | -49.14452 | 2025-09-25 04:38:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76228a4e-db19-3728-b195-9fafe8cebd61 | -29.71816 | -51.10552 | 2025-09-25 04:40:00 | NOAA-21 | NOVO HAMBURGO | RIO GRANDE DO SUL | Brasil | 4313409 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d52ca1da-4bca-38a1-bffc-0dd084a6b875 | -29.75531 | -56.02996 | 2025-09-25 04:40:00 | NOAA-21 | ALEGRETE | RIO GRANDE DO SUL | Brasil | 4300406 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 2304499a-091e-3134-803a-760008875aa3 | 0.91696 | -51.20945 | 2025-09-25 04:57:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65546cc5-7561-370e-ba74-169c0bf20950 | 0.91639 | -51.20587 | 2025-09-25 04:57:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| def54062-9c12-32fd-9adb-50e11e14e915 | 4.63027 | -60.69739 | 2025-09-25 04:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab271288-6375-3868-8327-507d722b3417 | 4.63072 | -60.70044 | 2025-09-25 04:57:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b18581ff-53b6-30d2-81ac-8977d7628433 | -0.90994 | -47.54414 | 2025-09-25 04:57:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e550895c-2b1b-3d93-9169-f744e2508f05 | -0.45615 | -52.15558 | 2025-09-25 04:57:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05ae3a96-92fa-3a6d-bb91-46a7904b49dd | -7.31565 | -45.76172 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e57f4fd-02c2-3357-a802-d5ce52d3ff86 | -3.4376 | -44.4862 | 2025-09-25 04:59:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7cb5defe-64b8-3d34-b20d-1b11aee2c7a1 | -4.89033 | -44.95703 | 2025-09-25 04:59:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f079b0c7-8c33-3321-9005-3988be3373cf | -4.5236 | -43.64257 | 2025-09-25 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 724e21b2-0c0d-3ce9-88c4-af24629f1423 | -2.24922 | -47.88462 | 2025-09-25 04:59:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dac9ad4a-356b-387e-9e54-d2791a479b9e | -5.72664 | -42.61463 | 2025-09-25 04:59:00 | NPP-375D | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 458b9b49-387c-3e25-997f-e6bae6c9eec4 | -1.76525 | -47.22542 | 2025-09-25 04:59:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b70b700-304d-3e1d-851a-33317c1d3145 | -3.37826 | -52.71362 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5921e21a-ffe6-3956-b970-4c36eab1a1b2 | -2.83198 | -46.72725 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1cc0bbee-6ddd-34d0-9d71-1c31cae3cca8 | -2.91965 | -48.31342 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 62ed687a-9973-3a69-ae2a-1d0c2dae5595 | -5.96098 | -42.90796 | 2025-09-25 04:59:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f2792d9-08b6-3282-9d83-3e8a0d453dfb | -6.82594 | -43.17938 | 2025-09-25 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9207bb9-a31a-32a6-9419-1a8cb9c73ac7 | -5.00831 | -45.17755 | 2025-09-25 04:59:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d39d674-cbbf-32c4-83f4-31ab37a06562 | -3.23638 | -46.80232 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b01088bc-8ea1-3809-82f6-c25f5f054928 | -2.17797 | -56.63826 | 2025-09-25 04:59:00 | NPP-375D | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab68645f-9661-3366-867f-723614212997 | -4.60297 | -43.91078 | 2025-09-25 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03023968-4c9c-305a-996b-02b693857a52 | -3.83132 | -50.97799 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dbad7197-1447-3a1e-9fd4-00aa1d820973 | -6.59721 | -44.61773 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec948ca5-1c0c-3b13-bf09-374e22f7bde0 | -7.31649 | -45.75551 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 533bc2b8-608a-31c9-b2c8-23ce86cb9ea0 | -3.21022 | -60.6074 | 2025-09-25 04:59:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| beabd8be-fbec-3a69-87b1-53d2d50accae | -3.83256 | -50.97011 | 2025-09-25 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c50dad7c-e47a-3e9a-99e5-ac5e79af2414 | -5.22931 | -43.69911 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0bb0c7bc-dbf8-328f-a404-d6dd25f2913b | -3.34406 | -51.63432 | 2025-09-25 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15cbeef1-fedc-3da3-ac14-1ec6c45b38d4 | -3.08619 | -52.9179 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96d9a8dc-d73a-3e58-a025-496347b6221c | -3.39554 | -47.4988 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 89189f56-e3a6-34b9-8110-0582c03b445a | -4.52194 | -43.64644 | 2025-09-25 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cba03df-9f59-3843-8d89-e741838b80bf | -4.45465 | -55.43563 | 2025-09-25 04:59:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 355bc498-e158-379a-abff-280094f7533d | -2.19593 | -54.46384 | 2025-09-25 04:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| dd4fa713-105d-38dd-be24-7852f502ec10 | -2.71193 | -54.95561 | 2025-09-25 04:59:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1cf48d9-bb0b-3182-813b-d5670333f2c2 | -3.3947 | -47.50023 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d6546f8-b536-3918-b637-67910750fca2 | -7.04615 | -46.4249 | 2025-09-25 04:59:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd153ce0-6df7-3552-9a18-b89b2cd14012 | -4.54351 | -44.02573 | 2025-09-25 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72eb3a1d-9ebe-361b-8b5c-a203807a894a | -3.39904 | -47.50085 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bd0f972-414f-3515-9c97-7dfd40618bae | -3.43809 | -44.48286 | 2025-09-25 04:59:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 352779d3-2d97-30fe-a150-bdf66a061f2f | -5.52969 | -43.877 | 2025-09-25 04:59:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d4d4a435-bf69-33a2-b804-c9431979d205 | -5.60056 | -52.15457 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 811ba9d2-dcb9-373e-8537-095f6e700d24 | -6.14152 | -43.45219 | 2025-09-25 04:59:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de2aeb11-0042-37c6-b4de-ee8b65524e48 | -7.09795 | -44.09311 | 2025-09-25 04:59:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4ba285a-acfc-3de0-a24d-7c6fe5d2d931 | -2.91594 | -40.39114 | 2025-09-25 04:59:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 90bab356-64bc-366a-837e-507a8bfeda0f | -2.92428 | -48.31047 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 89bbd54b-2ec1-30bd-b1ca-328442e10bec | -5.23567 | -43.69581 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 010a3aa5-62e9-343f-b28f-83eef12d957b | -5.23511 | -43.69987 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fff0a40f-3ac3-3bbc-a0f0-7055476daa35 | -4.52252 | -43.64252 | 2025-09-25 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c3a2349-a338-3b8a-af50-4db11d0e1462 | -5.59557 | -45.36261 | 2025-09-25 04:59:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6f03917-97fd-3183-8727-53ece565bc61 | -3.08898 | -52.92189 | 2025-09-25 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d42d0b08-0004-31a2-8eb4-6893292c2a52 | -2.92539 | -48.30332 | 2025-09-25 04:59:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ba133e5-a84f-395e-8f07-274bd2ad2c4d | -3.80489 | -41.56995 | 2025-09-25 04:59:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| ca006dee-9abf-3220-8e98-ef7ae20e45bd | -4.73676 | -44.42569 | 2025-09-25 04:59:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c6c3b86d-0e4b-378a-9da9-0586083185b2 | -1.34365 | -54.64659 | 2025-09-25 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bf3cb246-968e-37e4-963d-ff2645aaf6d9 | -6.59194 | -44.62611 | 2025-09-25 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b8bfa63-2081-3987-b4b7-a631a0fa75ef | -2.95969 | -48.59394 | 2025-09-25 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a95bec63-ee9b-3a16-869c-b9787c6daf52 | -2.38299 | -57.24431 | 2025-09-25 04:59:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f0ec76f-c6e4-358f-842b-4d48f46693ad | -5.52452 | -43.87196 | 2025-09-25 04:59:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 557db803-0814-3799-8092-63dbb039f0cd | -2.192 | -54.46686 | 2025-09-25 04:59:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a94af35a-8a23-312a-b6ce-70f63bf36098 | -4.8049 | -43.53353 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fe58f70-5d9f-39a7-a94b-af82f3ee0bcb | -2.26668 | -47.19681 | 2025-09-25 04:59:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5055ad8c-3490-34c5-8414-3ed6d9b6cc66 | -4.03109 | -47.77082 | 2025-09-25 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e47776ed-0b79-3f99-8e32-b75be0a63e76 | -4.80314 | -43.54569 | 2025-09-25 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63c3be01-cd10-397f-a0c2-db174ba00b3a | -3.39989 | -47.4994 | 2025-09-25 04:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5f4bea9-ad70-35e3-8885-18449f919341 | -6.75291 | -44.63174 | 2025-09-25 04:59:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 65fa9fe0-74bc-37ea-9cc1-f91d592b0f31 | -7.31607 | -45.75862 | 2025-09-25 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 696100d3-7744-3734-b895-ba23a8a44d29 | -7.25787 | -44.90491 | 2025-09-25 04:59:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d3df63-bfa4-3bf6-99c5-2b18e9033e8c | -2.70753 | -54.65314 | 2025-09-25 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |


[Clique aqui para ver as próximas entradas](README27.md)
