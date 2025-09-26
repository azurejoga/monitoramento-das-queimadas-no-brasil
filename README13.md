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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d2fdfa9-a809-3987-a562-57a07c9920a2 | -10.11742 | -45.30841 | 2025-09-26 04:14:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b588ca46-eb67-3d3a-9fa7-9d491845623c | -5.42708 | -41.31767 | 2025-09-26 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7744c934-924b-3cfc-9ebc-67cbcfcba541 | -10.19441 | -44.84731 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1871e529-2923-387e-8bf6-0535d8b37fa4 | -3.64528 | -48.31965 | 2025-09-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4b48a847-8088-3b06-a149-2c48604407ce | -4.48177 | -47.67414 | 2025-09-26 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| efd3e018-99ab-3b58-a302-cb81840a30a5 | -9.55293 | -47.51965 | 2025-09-26 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fc5d7c49-5f14-37c5-b1b2-0816230635cb | -7.31403 | -45.75877 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 514b0ec6-4274-3d7f-bd2d-8765cc50c809 | -4.87028 | -45.67079 | 2025-09-26 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bede4b8-df07-36aa-8348-bd6cf6f467de | -5.73425 | -44.96188 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e094b16-262a-3c31-b07e-d3e92ee5bc20 | -3.92456 | -40.75426 | 2025-09-26 04:14:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d635ecea-609c-3274-bbf6-5a56120b3cf7 | -5.39354 | -45.84878 | 2025-09-26 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c793ec7-26cc-369d-8fca-f1573b03cf26 | -6.8276 | -44.18263 | 2025-09-26 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 799df48a-8ddb-3622-8275-f0b7fd90b0c5 | -10.93247 | -44.26773 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ef865f9-77ff-367e-8ea1-8df8499f74bb | -3.86561 | -40.34031 | 2025-09-26 04:14:00 | NOAA-21 | FORQUILHA | CEARÁ | Brasil | 2304350 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 474d1ccb-7e8b-36ec-98cb-2fef56beb27e | -10.9347 | -44.2967 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bc9491d-feb5-362f-8102-bdfc0e728574 | -5.72801 | -44.95715 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9d0d3dae-12b0-32cf-9f98-57a288f66025 | -6.63921 | -43.82369 | 2025-09-26 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44704316-837d-319c-af56-9c1ff866a34e | -5.77366 | -42.8135 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 17682020-8a1b-35b0-9f6d-859f6de3beef | -8.13254 | -42.3816 | 2025-09-26 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 301d0e75-d379-3d39-b1ca-85f4fce0a571 | -7.39033 | -39.1158 | 2025-09-26 04:14:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4eb77781-5009-37ad-b6cf-6d9b1c38e735 | -7.1087 | -43.7385 | 2025-09-26 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be0ccf3f-fbf8-3a7d-8005-a9fa59c19716 | -6.11566 | -44.22772 | 2025-09-26 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ffd12de-f685-349c-b2ff-6ae302cdf3ce | -5.53895 | -42.80799 | 2025-09-26 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 152c62d8-8780-37e8-a250-5616b63fd00d | -9.9818 | -46.70381 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7ff2743-ebc7-3c7b-89a8-420fba4fa16e | -7.11683 | -42.1779 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2dfa09f1-3f75-3b12-843c-c66a8b3abbe0 | -5.64616 | -43.92606 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 80a86407-fdaa-3eba-a1f5-e4dd5e8c0e66 | -5.77419 | -42.81005 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5623a10f-e73e-3ea1-9346-15fd5ffe47ab | -6.83755 | -43.16851 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| cf240d51-af92-37ca-a0cb-17e733b57fa3 | -6.69051 | -44.6141 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86d8f82c-b439-3365-814b-d693e2e0225f | -5.07854 | -44.07069 | 2025-09-26 04:14:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7d53d5d4-3f3d-3d09-9c52-cfde87f15ba8 | -4.74651 | -43.60825 | 2025-09-26 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d8a6686-1c83-3bc0-9346-3c20ce9abe15 | -9.55221 | -47.52403 | 2025-09-26 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38a525ab-5cce-3832-926c-563d7afd8e19 | -2.9229 | -48.30624 | 2025-09-26 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4a4bdaaf-9bcc-3c13-b977-e5d331af2045 | -7.93475 | -45.2014 | 2025-09-26 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b2581c2-ecec-3320-9a8d-d9750a567ccd | -3.81117 | -52.08421 | 2025-09-26 04:14:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28a07aad-16e3-321c-a08a-9d25325d02fe | -6.99558 | -46.99542 | 2025-09-26 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3e274c1-d6ef-3219-b0f4-c70ccf67cbc0 | -5.6165 | -43.46595 | 2025-09-26 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6d522c0f-f29c-3b9f-ba69-07f9f78689fe | -6.86891 | -39.26371 | 2025-09-26 04:14:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a4a2c112-9157-3864-adf9-b98a81387b62 | -10.01041 | -44.17923 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d28df0f7-3f28-3f33-8947-7f8cb542666c | -9.8906 | -45.73841 | 2025-09-26 04:14:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7377771-fe98-3378-b1de-c91cf90ef6fb | -6.48356 | -41.9166 | 2025-09-26 04:14:00 | NOAA-21 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 73d04fe5-4b25-31d7-94c7-ab4b914a6a45 | -5.4651 | -43.06413 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 3d606c83-cd32-36d9-b089-2666241a2be1 | -5.73932 | -44.97406 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 0f6c7d97-27d4-3c6f-95d7-5dbb99226ec5 | -4.38808 | -41.92038 | 2025-09-26 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 58ca717f-b59d-3e50-98d2-da5ee9329e83 | -5.74731 | -44.96773 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 0f1d3e91-f658-3ede-8cd0-17b9ed99abfd | -9.09423 | -47.61276 | 2025-09-26 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fae61fb-8c47-3c3b-962a-ea5ee8b7aa1f | -4.03669 | -46.9282 | 2025-09-26 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a8afcc4-5b09-32e9-8d20-451512ada6b4 | -9.42574 | -45.58749 | 2025-09-26 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a47c013a-e51e-37e2-9b10-bdf815a78770 | -5.74214 | -44.97833 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 60c76599-49ef-3dcd-a0d8-21bed865aeaf | -5.76843 | -42.89019 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4e3e46c1-0ecd-3580-a901-dce03385dbf0 | -6.53201 | -43.87777 | 2025-09-26 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9d362a20-d3fc-3022-a354-acec056b30ba | -10.56624 | -46.27033 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a209e44b-82c7-3f2a-bf89-f59d104d4863 | -5.69343 | -44.44483 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ded258da-1286-35e5-8c75-951b55ee82bf | -8.79338 | -43.06225 | 2025-09-26 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| accd36f0-e26d-3b6c-869c-23f314b317b8 | -9.37143 | -43.74214 | 2025-09-26 04:14:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1344cac8-15fd-3794-bda8-66a2f7ff8969 | -6.68715 | -44.61357 | 2025-09-26 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0689745f-893e-39c5-b2b6-fb11b4e332e8 | -5.62956 | -43.9234 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e3df8d0a-53e7-3e2d-861e-840a98384dd2 | -9.94036 | -47.44913 | 2025-09-26 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1efc64a6-7271-3a30-bf68-f78c77573194 | -8.132 | -42.38515 | 2025-09-26 04:14:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 11c4379a-45dc-36f3-8d99-de80b505b4d8 | -5.46732 | -43.07152 | 2025-09-26 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 8b6fc0cf-f624-3596-8077-3344a9e38118 | -5.74896 | -44.97942 | 2025-09-26 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dc4e4746-37f4-34bc-babd-4bc922ceeda4 | -10.00711 | -44.1787 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42b2bf50-56cb-361f-8954-22df7f70ab4f | -10.01864 | -44.16985 | 2025-09-26 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0169f0ce-a2e6-3265-8f6d-252f82e71cf7 | -8.32286 | -49.52932 | 2025-09-26 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4bef5c7-5d48-30bb-80eb-d813d0630e20 | -6.9587 | -43.24113 | 2025-09-26 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3745e8b3-9e75-31d2-9ab5-abe4d84a6181 | -6.88922 | -44.7554 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c84da777-a8c4-3c58-a859-a6d454844435 | -7.12466 | -42.19363 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 92701239-db87-3bb9-adce-f897c1d6d01e | -10.80133 | -45.37609 | 2025-09-26 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4092cf64-c6d1-3345-a3a7-640ebe870937 | -6.99412 | -44.7021 | 2025-09-26 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e75f5ac5-569b-37ba-b20e-727c6fd3be2c | -10.40871 | -46.15942 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e5c4235-88bc-3b7d-a9dd-d94be48240f3 | -4.81174 | -45.19629 | 2025-09-26 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb027a71-9c75-3ce9-93dc-b3d62daa35dc | -3.64464 | -48.3236 | 2025-09-26 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b8ad83c9-b69e-3d06-b80d-c1d7255d9ca0 | -3.4426 | -44.12823 | 2025-09-26 04:14:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 448e0dce-548d-3f94-b5ae-6f87a3509672 | -4.53662 | -44.07564 | 2025-09-26 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71ce7dcb-287a-3c21-a15f-2d3afa0a1d17 | -8.93463 | -48.66226 | 2025-09-26 04:14:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 936e7e22-8940-3f5b-9846-aa85e508228d | -10.1889 | -44.83921 | 2025-09-26 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f6517f2-132c-37f1-afa2-28b3f5ce5163 | -6.13562 | -43.45661 | 2025-09-26 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97504c84-13d3-37b4-b5ab-cd25c51aaa81 | -10.40501 | -46.18212 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6728751-a633-36d9-8288-971a0baad180 | -9.24175 | -44.26241 | 2025-09-26 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd01f742-ba86-368c-830a-06bec0eb197a | -10.02287 | -49.13381 | 2025-09-26 04:14:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e31b1b0e-9baa-3b5b-80a4-f7a17cb52d04 | -5.39289 | -45.85284 | 2025-09-26 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87559733-3e89-34a6-8298-e30d99fc938f | -10.57184 | -46.27911 | 2025-09-26 04:14:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6fe9008-f8ca-3774-8e45-d872f5a4a971 | -6.52271 | -44.00119 | 2025-09-26 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f09b7ae-73a1-3b04-a622-238c76693495 | -6.69386 | -44.61463 | 2025-09-26 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc5a7d1f-c060-3b77-8f1e-92f1c3648e55 | -10.93632 | -44.26477 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f80651bc-5b7e-3d73-9ab1-b6b69d52d640 | -7.1308 | -42.19821 | 2025-09-26 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 54095234-7dc1-3b5e-8491-f7319247efd5 | -7.68412 | -45.98722 | 2025-09-26 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 610997a2-122b-3d9c-99ae-f6468ca122de | -7.57392 | -42.41106 | 2025-09-26 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1c079cbc-fe23-3c00-8034-e85081017a9b | -8.49889 | -49.54214 | 2025-09-26 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f8e93bd-0d2e-314f-b163-55c957585bf2 | -10.9413 | -44.29776 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8c868c6-f16e-3784-9311-5766dc109c0c | -5.96199 | -43.67319 | 2025-09-26 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2b77a91-c776-3e04-a784-df5db583638c | -5.77688 | -42.79284 | 2025-09-26 04:14:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1d4c2110-7fd0-3832-9ce8-f2bd761f943c | -5.76588 | -42.55448 | 2025-09-26 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0b715e02-2b6c-31e9-bd42-336e967864c8 | -10.79799 | -45.37555 | 2025-09-26 04:14:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3080c732-a10f-3029-a6a6-74233ea091f1 | -7.31749 | -45.75933 | 2025-09-26 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bfadafd7-f8b1-38bf-8e65-00e16c0978e2 | -9.69522 | -48.94822 | 2025-09-26 04:14:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4b60c776-0827-3595-884a-784eb511fdb6 | -5.78708 | -43.83079 | 2025-09-26 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 690cd874-5cea-3e62-8d57-a608e3d5582c | -7.05233 | -46.4264 | 2025-09-26 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c1f885c0-ab32-387f-8162-826bbb39ff60 | -10.94239 | -44.29078 | 2025-09-26 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f60b1f2b-e08e-329d-891c-de2e9ef60a44 | -5.5348 | -43.87636 | 2025-09-26 04:14:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |


[Clique aqui para ver as próximas entradas](README14.md)
