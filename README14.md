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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e946837f-18c3-38dc-bcfe-d3c86c932de5 | -4.1558 | -47.978401 | 2026-10-09 00:06:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdfe8758-04aa-36cb-b0d3-d111e956d2aa | -3.0198 | -54.062698 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e174b716-5da9-3f20-9e5e-c992405a530b | -4.5094 | -43.625599 | 2026-10-09 00:06:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 76f33917-2017-33df-8959-aa2428aa36b3 | -4.5481 | -47.032902 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0495a6b6-1f87-3393-84cc-941d909e5fd7 | -7.2124 | -55.072701 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4689e265-5d24-3116-a3fd-cf4b91249550 | -3.591 | -54.556198 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc242198-23ae-397a-83f8-1402008f9b28 | -4.5499 | -54.9557 | 2026-10-09 00:06:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56be80dd-61e0-3985-aeea-c1fdddca45f2 | -5.3381 | -50.9841 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87b6d979-29b1-373a-8474-493630c22dc4 | -12.167 | -49.3937 | 2026-10-09 00:06:00 | METOP-B | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 43316f61-0681-304d-bbd0-af16984f4c98 | -14.7393 | -48.219501 | 2026-10-09 00:06:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 931b1f8d-e2c8-36a7-93aa-c847d599366b | -16.964199 | -46.345798 | 2026-10-09 00:06:00 | METOP-B | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c22e4803-1392-3ec8-bbf8-4fb7a8e3a6cf | -2.7839 | -54.064201 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6544d049-117d-3558-9a40-d5faaee62cca | -9.077 | -45.114399 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ef83f665-c43a-3e0f-96a1-71a09723b541 | -4.9944 | -44.993401 | 2026-10-09 00:06:00 | METOP-B | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f1312d4-b19c-3cbc-928e-817f9595c03e | -3.2472 | -54.023201 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06374763-f445-34ea-ab3f-78245e4abd1e | -8.2858 | -45.705799 | 2026-10-09 00:06:00 | METOP-B | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29647877-59b1-36b2-aa24-d80167137192 | -3.3435 | -50.4021 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d0b40b3-85fa-3e5a-a199-7802cc1bd8ec | -2.798 | -54.0811 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82e68994-db7e-3a6f-b3d5-f614a719ae37 | -2.7392 | -54.093899 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 970777bd-85c7-3907-ad8c-c110b8893eaa | -2.9412 | -54.1707 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b8bd1dd-b3a7-336e-9780-b76df152bc0b | -6.8077 | -46.452599 | 2026-10-09 00:06:00 | METOP-B | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b01efe7-4327-3863-8678-27b24d1dae62 | -16.5896 | -46.748901 | 2026-10-09 00:06:00 | METOP-B | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| db5ad99f-dc51-3f9d-b46f-d0d264d39b27 | -5.2407 | -43.976799 | 2026-10-09 00:06:00 | METOP-B | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1994e20-4af9-3307-a27d-f7c11770a7ae | -3.2433 | -54.6535 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1664c95f-abc7-3eb3-a392-6013f8846004 | -2.9743 | -54.042599 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69f1c714-7503-3930-9af1-7d7f3e80fa19 | -7.3754 | -44.023998 | 2026-10-09 00:06:00 | METOP-B | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4333011a-e85b-3b03-b9c3-ef936cf61077 | -8.1863 | -46.390598 | 2026-10-09 00:06:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0074aaa3-6224-3f59-bd36-c7b5207407eb | -8.9576 | -45.177898 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 20a05dc6-1183-32a4-9070-31bcbb644908 | -5.7036 | -53.4818 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c018297-0164-3908-8d01-814ccf0c2384 | -8.2865 | -50.266602 | 2026-10-09 00:06:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27163c59-1b78-3aba-b1c6-5e79f2884c13 | -6.109 | -55.689301 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed73e160-9ccb-3e54-9ed6-76cd02038741 | -1.4043 | -53.229301 | 2026-10-09 00:06:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c49094-97d3-3abd-9b72-8dbb03ceba98 | -11.185 | -45.2981 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c1c172e-7aae-320a-9a82-8ea3644e46dd | -8.1771 | -54.712399 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87655acf-58dd-32aa-8c56-b7fcddbd95f9 | -2.5653 | -56.171001 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c89ddf69-3729-316f-a226-a222e4395cc5 | -13.168 | -54.3395 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 26cb5fd1-dec6-35a8-8b52-2077193ed105 | -13.4359 | -50.9245 | 2026-10-09 00:06:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 705f7ac0-b018-31f1-8581-1ee85ab98a82 | -5.2931 | -47.9011 | 2026-10-09 00:06:00 | METOP-B | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56a269cc-f2fd-3f92-a6a2-550ba1f59f3d | -2.9828 | -54.080799 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 037007c2-8b1f-3756-a77c-a80e66d88cf8 | -9.2902 | -47.428799 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9f9ac4d-7fde-37eb-94f0-517f479a8074 | -3.1752 | -50.569801 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ccbb4562-b814-3f88-af5e-7ff8cf892563 | -6.9957 | -47.678799 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b0cf717-07fa-3585-8fa3-03101f8a19ee | 1.5272 | -55.951 | 2026-10-09 00:06:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463b79df-5b25-34b1-80f9-543216846fe8 | -8.3308 | -49.119999 | 2026-10-09 00:06:00 | METOP-B | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57576876-524a-3217-8d50-a0e66af3a684 | -5.6963 | -49.088501 | 2026-10-09 00:06:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a122741a-d60d-3b66-8ce1-e1b5d5d88516 | -5.3501 | -45.725201 | 2026-10-09 00:06:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ec03d665-d0b4-3614-ad91-81f7686a075e | -5.083 | -46.130699 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16e5bab6-01d3-3234-b74f-e18a968087da | -3.739 | -59.4715 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2f156268-2d63-3747-bd76-964b1617a5ec | -4.296 | -48.5951 | 2026-10-09 00:06:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36e3b017-fdb2-3d84-802e-a9c683c0bfb3 | -6.8532 | -48.779301 | 2026-10-09 00:06:00 | METOP-B | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ba010336-964a-3699-bada-8d9b392a3202 | -8.7248 | -45.1534 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| edc72171-a38c-3684-a3b6-dc31fc9f35bf | -3.1043 | -53.934799 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d76600ec-9946-33a0-85d1-93fb128bd5db | -8.7346 | -45.1511 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5d5e4435-52a8-39e7-a670-41774854ee90 | -3.1669 | -54.725101 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 162d49b0-ab6e-3102-9130-3e4eac27b970 | -9.0183 | -44.381199 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2df4f080-23ba-3143-beaf-da55735ddc27 | -6.155 | -51.7005 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4072db30-ba48-3847-ab7e-28bd31318b1b | -5.7454 | -45.3405 | 2026-10-09 00:06:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 392713d3-cbaf-3c2d-9acc-f154357e2243 | -3.2644 | -54.2854 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76e12b8b-bb77-3b67-8e2f-571f20ac0798 | -12.0182 | -43.486198 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d8fbffb-dd90-3195-a957-8c168fb682c6 | -2.2325 | -51.921299 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fbd8ec3-746f-303b-a50c-8d22c1c712fa | -15.5578 | -44.5121 | 2026-10-09 00:06:00 | METOP-B | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 18357e52-9930-356d-80e9-5f3d54dbc4eb | -3.1684 | -50.448101 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e652859-1a88-307e-9db7-26ddd3b07abf | -4.7942 | -56.124802 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d0d8efc-4a14-3510-9925-e13f3c7ed31e | -3.734 | -59.4487 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3758de66-5c29-30c3-8746-724bda626226 | -15.5175 | -50.403 | 2026-10-09 00:06:00 | METOP-B | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e64eaf57-ba9e-3d02-8cf0-ab5ee43c2c8e | -3.1087 | -54.185101 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37d17d7e-0b32-3998-98a4-f2502ae87329 | -2.4686 | -56.058399 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b3ea141-126f-3dbc-aaf9-463fd324a393 | -2.9892 | -54.1096 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b273050-2a8e-3793-b201-78b20805a17c | -6.3847 | -55.260201 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99e509f4-e70d-3ff3-8c09-0a48fef227dc | -9.2887 | -47.421799 | 2026-10-09 00:06:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39b290c1-47af-316f-896b-9309d928746b | -9.1386 | -45.8223 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ed24f771-6c13-33a4-a852-8fa47b7b7321 | -3.1184 | -54.182999 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb9eaefd-5955-3e93-8976-bc1e496362aa | -11.9994 | -43.450802 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c27671c7-5518-3230-8010-42e54c7f5f59 | -4.0825 | -44.1315 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4fbb339-7e7e-3e44-b9c4-54544862d01d | -8.8982 | -44.924099 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 04bbbfb1-a754-34ed-a68d-969c8d69cc7b | -14.5603 | -50.031601 | 2026-10-09 00:06:00 | METOP-B | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37784f5b-1f00-3c50-aedb-ddc4bff12234 | -18.0889 | -42.2659 | 2026-10-09 00:06:00 | METOP-B | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb892bbb-346f-3d5c-ac63-0bf523a568c7 | -6.8867 | -43.702202 | 2026-10-09 00:06:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac07ea3-f2c8-3c05-89c5-618afbfc5e3e | -3.2668 | -54.019001 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58e795ec-d1be-37e5-96fb-7abf8ae9ed8b | -3.0815 | -54.293999 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 942bae82-c846-3612-a0cf-26ee3ea4b1fa | -4.2903 | -54.7994 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edb24401-2522-3329-a35c-a331ed145ff8 | -16.1238 | -43.749599 | 2026-10-09 00:06:00 | METOP-B | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8d20b603-29e0-3f55-a292-235c1d93b385 | -9.908 | -44.783401 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f893417-2e18-3113-b3c7-12f14b59400d | -13.1723 | -54.309399 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b55719b7-7081-3882-817a-8144f228f0d7 | -3.5728 | -54.659302 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2ed3c15-fedc-3e6a-bd87-4f50822e92ab | -7.2331 | -55.122101 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1bc7dc-381d-3a97-9154-0250ceb569b0 | -6.738 | -55.145802 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d40f6ed0-4cf1-36b9-9c7c-d27ad4a34b7c | -3.5826 | -54.657101 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a795d22-f049-3876-80c6-645c3a322dc2 | -3.5254 | -59.375198 | 2026-10-09 00:06:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa1573f8-1256-3e69-999e-8277aa0a57ac | -2.9892 | -53.8325 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83102ce2-7a0f-3b47-b79c-2a9fe564e612 | -8.9009 | -45.200001 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 620a94ee-e623-37c7-8591-524d4e7103ed | -3.3059 | -53.6861 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c646055-bfe1-39b8-b08b-4bbadffe23cd | -8.9977 | -47.730202 | 2026-10-09 00:06:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ef100aa4-45cb-3ba0-9cbb-6a14bd9eaeab | -2.7411 | -48.422401 | 2026-10-09 00:06:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e0a7236-ed16-35f7-b8b6-9fb32b66086b | -3.9172 | -55.8521 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c59b9959-d37b-39be-ad76-76ffaf5c5f41 | -3.4386 | -59.535301 | 2026-10-09 00:06:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a389299b-e639-3b97-8f20-0510a78e6cfb | -6.4895 | -55.943298 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ec2db88-0eb3-32d6-b8f7-e3a8b0a31489 | -11.8171 | -47.340698 | 2026-10-09 00:06:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ec3998d-280d-37ed-b5d6-77e401d31b2b | -1.1095 | -47.774799 | 2026-10-09 00:06:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68df6791-a1c7-313c-9d94-db6ce7dafa3d | -11.0914 | -44.063999 | 2026-10-09 00:06:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README15.md)
