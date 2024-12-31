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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56592e81-49e1-34f8-9502-f07507131c22 | -2.48916 | -45.45814 | 2024-12-31 00:49:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 73572988-fdbc-38d4-92dc-5ee7b4d27e74 | -2.7198 | -45.57152 | 2024-12-31 00:49:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 35672b42-7c72-35a2-a09f-c1a99aa902fa | -2.32805 | -45.61869 | 2024-12-31 00:49:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4c2292c2-d25f-3d08-a101-56f19a3e0c0a | -2.5789 | -51.90754 | 2024-12-31 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 79cc36ea-170f-3fd2-b913-0a5e6f179c5f | -4.693 | -44.4951 | 2024-12-31 00:49:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8c15ef02-1403-3926-a044-5c07b97c8d7b | -1.25678 | -46.60801 | 2024-12-31 00:49:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4a84571-31ae-3027-9bbc-4620126c1af7 | -6.13114 | -39.80294 | 2024-12-31 00:49:00 | TERRA_M-M | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 72f3b035-d630-36c7-ab4c-c9f74692a654 | -1.57068 | -46.04837 | 2024-12-31 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| ef1345c5-0004-3bd4-8cb8-d461b22cda9a | -1.64526 | -45.85542 | 2024-12-31 00:49:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6d2572eb-be34-3415-88fe-8a1dd3dbc4fc | -2.45112 | -49.30623 | 2024-12-31 00:49:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cdaf662e-ba7e-3120-80af-fca28572a50c | -2.0983 | -45.59111 | 2024-12-31 00:49:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 03a83817-436a-385c-8066-a2eab5c2f802 | -1.65505 | -45.85403 | 2024-12-31 00:49:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| c20aa156-3c58-3523-b0ef-1615fff4ced8 | -1.64681 | -45.86632 | 2024-12-31 00:49:00 | TERRA_M-M | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 40f8a30c-2c13-3208-902d-41567d178730 | -6.94806 | -43.00764 | 2024-12-31 00:49:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 553bde14-c870-3439-9030-3cd3f39e5261 | -2.5773 | -51.89582 | 2024-12-31 00:49:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6a4620b8-1cbd-3b22-9c3d-732f3b5e6bd5 | -5.3152 | -44.5556 | 2024-12-31 00:49:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44f330c7-ec19-39c1-bf78-d2136733db55 | -1.86283 | -48.5192 | 2024-12-31 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1460dd1f-edd9-351c-a690-a35ee1128abc | -1.24737 | -46.60932 | 2024-12-31 00:49:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| c835b7cc-bcd2-3678-adb7-7cbddd341f61 | -1.51671 | -46.49115 | 2024-12-31 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 0100bca4-4277-3913-86b5-3c5fb3bdcfdd | 1.5504 | -55.874901 | 2024-12-31 00:59:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37322775-55be-3b4b-892f-c6af5586794e | -17.7444 | -56.306099 | 2024-12-31 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f57f43c0-f51b-33d3-8d55-3935c1dc3c53 | -22.116301 | -51.453701 | 2024-12-31 00:59:00 | METOP-B | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e5e07392-dcb5-3830-8ac8-b79c2a4999df | -10.2017 | -59.422798 | 2024-12-31 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b5ac79e5-8789-3986-ba8f-a90b2fa5ba0a | -2.5711 | -51.9058 | 2024-12-31 00:59:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 904c7666-b5db-372e-bda5-ae29d1a99682 | -17.746 | -56.313702 | 2024-12-31 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| bae9818c-bf8d-3af3-93f5-8e76a58d7aba | -10.2052 | -59.439098 | 2024-12-31 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cca69c1f-69cd-3ee7-ac97-479a945d2ea5 | -19.834 | -57.4618 | 2024-12-31 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| de483972-f40d-3b19-8d3c-77a98c628e52 | 2.1009 | -60.520302 | 2024-12-31 00:59:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 62c816c0-7217-3f46-a281-09d69df03833 | -19.340099 | -54.1651 | 2024-12-31 00:59:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| be51c7b9-0f5d-351e-bcef-d60da7b651ae | -17.747601 | -56.321201 | 2024-12-31 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7ca5dcec-b461-3ac6-8cac-b5dacd4f93ee | -2.5681 | -51.893101 | 2024-12-31 00:59:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ecaf6ad-be5a-3535-af35-5d90f46f8280 | -9.925 | -59.902401 | 2024-12-31 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 74d67430-f333-3185-bd94-bbcfac36725d | -19.8358 | -57.470501 | 2024-12-31 00:59:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b2c5137f-397f-3e48-bfe7-852de17e695d | 1.5406 | -55.872799 | 2024-12-31 00:59:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e7b36c0-32fc-34bf-b21b-32d6406e2812 | -19.3386 | -54.157799 | 2024-12-31 00:59:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 40609f4e-5ff7-348a-86c3-71c4e574f46a | -9.464 | -59.188801 | 2024-12-31 00:59:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7282c4ff-74a9-3dda-9102-8d531a2711c3 | -22.120001 | -51.4697 | 2024-12-31 00:59:00 | METOP-B | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 35eabab3-3015-30ce-b4dc-4c1deb3cd52a | -22.118099 | -51.4617 | 2024-12-31 00:59:00 | METOP-B | PRESIDENTE PRUDENTE | SÃO PAULO | Brasil | 3541406 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e93be0e-20f1-3882-a942-5977180914ea | -10.2034 | -59.430901 | 2024-12-31 00:59:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a0838f9-2fac-3a3f-8934-03ce17676dd5 | -10.1901 | -59.426998 | 2024-12-31 01:56:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4823f86d-97d8-3000-8c2d-835edb641450 | -9.4709 | -66.0411 | 2024-12-31 01:56:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bd05bac2-0f93-3dca-a510-64ffc2f747a7 | -10.1939 | -59.442001 | 2024-12-31 01:56:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eec9e8cb-bddc-3d72-8f90-16586179721f | -9.2345 | -60.350399 | 2024-12-31 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 91f669ce-d4dd-3182-b44a-a01219a7a54b | -9.9168 | -59.8997 | 2024-12-31 01:56:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 80417b9e-4c18-3ad9-82d9-f359c978adab | -10.1977 | -59.457001 | 2024-12-31 01:56:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b4738e98-ba83-35de-ae51-0d48cb1344fe | -9.2311 | -60.336899 | 2024-12-31 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb29fb8c-c33e-3ff8-a89d-ccda3aca35c9 | -9.9203 | -59.913799 | 2024-12-31 01:56:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc84b76c-7b1a-30cd-ba70-db92d4eea584 | -9.2408 | -60.334499 | 2024-12-31 01:56:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| caa300bb-9aad-3769-ae2f-61ae09cae928 | -7.8164 | -35.23179 | 2024-12-31 03:17:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ad8e4cbb-e309-3132-96fc-9dc19cc891ae | -6.95122 | -43.01024 | 2024-12-31 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6faccaff-b49d-3d65-8968-ff4ec8f8ed0a | -8.09009 | -35.23547 | 2024-12-31 03:17:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8761b0b8-0fac-31b9-bebc-ae46d8cfee5e | -6.13327 | -39.79861 | 2024-12-31 03:17:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22e6b9ea-d086-3058-9434-0f9983d6abb6 | -6.88067 | -40.6182 | 2024-12-31 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d7b1cb91-526b-31a1-90f7-207a57c469f5 | -9.86593 | -37.19537 | 2024-12-31 03:17:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e43b28d-135d-3de1-9ba8-7c82c73ffa82 | -8.05652 | -35.15219 | 2024-12-31 03:17:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| a343d976-cc7a-3172-a60e-7d87ca81d926 | -6.87978 | -40.62301 | 2024-12-31 03:17:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 78f3b284-96f3-3d58-ad59-0f24de0d1d5a | -7.81244 | -35.23503 | 2024-12-31 03:17:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 166b89a4-e51c-375c-bce5-5091e7df25c7 | -8.08585 | -35.23475 | 2024-12-31 03:17:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 51b82e00-396a-3699-b372-7559735a35ab | -7.81569 | -35.23584 | 2024-12-31 03:17:00 | NOAA-21 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 17b3bea7-a4ac-3480-9fde-8e7ba61d3533 | -9.19121 | -35.50682 | 2024-12-31 03:17:00 | NOAA-21 | PASSO DE CAMARAGIBE | ALAGOAS | Brasil | 2706505 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5586f47b-5c2e-326a-8770-afdace6b6540 | -6.95256 | -43.00328 | 2024-12-31 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 29fa5674-f6c9-3191-b694-df1bad9d492f | -7.80608 | -34.96272 | 2024-12-31 03:17:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2334f1b6-429d-3f9d-90b3-5a606b448b57 | -8.05719 | -35.14832 | 2024-12-31 03:17:00 | NOAA-21 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 21b25413-973b-38c5-ad43-76f0e62bb207 | -6.59629 | -39.4256 | 2024-12-31 03:17:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ca722ff-82a8-3765-a593-5f3588a51829 | -10.15838 | -36.36623 | 2024-12-31 03:17:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 66d63018-a8ab-3432-878c-90826491ccf6 | -6.13254 | -39.80256 | 2024-12-31 03:17:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 26aef870-6bb6-3324-9cc3-1575e3b6da36 | -6.12974 | -39.79913 | 2024-12-31 03:17:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eb7c4755-c8cd-318d-a7bf-fb7c4475b8fa | -6.95556 | -43.00412 | 2024-12-31 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8153a51c-afad-3c22-8cde-5cdbaceeeb6b | -7.8254 | -35.17997 | 2024-12-31 03:17:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 10e88973-e792-3458-b8d2-b7509e5c6b7c | -6.95426 | -43.01109 | 2024-12-31 03:17:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| dbabf2bf-1f8d-34f2-b438-31d7aaca4ce6 | -7.80255 | -34.95813 | 2024-12-31 03:17:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 56531728-995d-3fef-a6fe-061b686a129f | -6.59701 | -39.4216 | 2024-12-31 03:17:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6403bbcf-d78b-313f-a4ea-a39347128875 | -9.86737 | -37.19799 | 2024-12-31 03:17:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7d165bd5-5553-36cf-a8a0-a9eaaed26b91 | -6.70629 | -34.9646 | 2024-12-31 03:19:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 350df843-f6cc-3216-bff1-16c8a6a84e44 | -5.85398 | -39.08273 | 2024-12-31 03:19:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c51ccde3-5522-31b3-869e-f254def8e5f6 | -5.52863 | -37.7612 | 2024-12-31 03:19:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dbbfb04a-3362-3a76-811b-8a5618bde5ed | -5.85601 | -39.08245 | 2024-12-31 03:19:00 | NOAA-21 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b9e6475d-831e-34ab-9bee-3b5c334fee61 | -5.52829 | -37.76376 | 2024-12-31 03:19:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| caafa95e-815d-3df6-836e-5621c69cce99 | -5.21948 | -37.6117 | 2024-12-31 03:19:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b61994f9-6be6-3c49-bdb6-cf80f53b7857 | -20.04273 | -40.94184 | 2024-12-31 03:21:00 | NOAA-21 | ITARANA | ESPÍRITO SANTO | Brasil | 3202900 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3aa7f90e-f5db-30b1-8c31-6ce95d44eeeb | -6.95056 | -43.00482 | 2024-12-31 03:42:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0ed1d624-0a9c-30ba-be94-cc65eba25f53 | -6.88224 | -40.62086 | 2024-12-31 03:42:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4ac8336d-764f-3e31-95a0-4ffb22bb737a | -1.26859 | -45.73514 | 2024-12-31 03:42:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 965fff29-5070-3a9c-adb2-c85cb6bb6aa5 | -4.8765 | -39.05094 | 2024-12-31 03:42:00 | NPP-375D | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5a3abe03-841a-33b2-b1cd-04f7365b4f65 | -3.91374 | -40.75287 | 2024-12-31 03:42:00 | NPP-375D | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 4cb53646-a38c-38a9-8810-80bd2c267bcf | -6.59606 | -39.42622 | 2024-12-31 03:42:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 16b8a7a1-6f71-3fae-b99d-2b2764c0139f | -6.12994 | -39.79797 | 2024-12-31 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6e152285-48bf-31a7-83a0-926c0ed66e33 | -2.81204 | -41.78187 | 2024-12-31 03:42:00 | NPP-375D | ILHA GRANDE | PIAUÍ | Brasil | 2204659 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bde7dd6-d36c-3ff3-ab4d-4c6859b18918 | -4.62135 | -38.48554 | 2024-12-31 03:42:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 15a4b94e-c11c-349e-aa9a-09043d45eedd | -1.64764 | -45.85849 | 2024-12-31 03:42:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a338a796-0ed8-39ae-9cb7-5113bd0adb1d | -1.64681 | -45.86353 | 2024-12-31 03:42:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75629ccc-0f28-3d15-b218-7cb94b47289c | -1.65395 | -45.8595 | 2024-12-31 03:42:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff33a149-3be9-3255-912a-dfb379dc1437 | -7.78261 | -35.17279 | 2024-12-31 03:42:00 | NPP-375D | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c0c77e3c-eb6d-3cf9-b373-662a44136976 | -5.22249 | -37.61163 | 2024-12-31 03:42:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0e7b1025-fc55-39f5-9169-97ba93abf0ff | -3.76461 | -43.95997 | 2024-12-31 03:42:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89c03a97-6e2b-31cc-881f-1f5c140346e3 | -3.55403 | -43.56178 | 2024-12-31 03:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 451ea93e-a60f-30ee-a71e-9a230131771f | -8.05425 | -35.14749 | 2024-12-31 03:42:00 | NPP-375D | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5d751e23-a54b-3ef5-a5f1-5f5de2a5002f | -6.50713 | -35.63155 | 2024-12-31 03:42:00 | NPP-375D | RIACHÃO | PARAÍBA | Brasil | 2512747 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2bf11e20-f19b-36d8-95fd-67f9c7e7cc05 | -2.83718 | -40.29591 | 2024-12-31 03:42:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 475bbf9b-c893-300e-bea8-b70e256e536f | -8.09085 | -35.23574 | 2024-12-31 03:42:00 | NPP-375D | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README3.md)
