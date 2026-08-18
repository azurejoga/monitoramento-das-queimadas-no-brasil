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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9ffdf58-65c2-3008-ba81-6c60518cd673 | -3.21276 | -49.05922 | 2026-08-18 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c695b61c-2fbe-35f9-a6b1-0c254c3e640c | -8.61021 | -50.34578 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e245f90b-f748-3085-9bff-8d0da0c7edd8 | -8.49426 | -48.81569 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e435535-8297-36a6-8f36-8a98e24b5533 | -9.45784 | -50.31165 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2c3797a-6345-3844-b4ff-a675f69fdb51 | -8.3411 | -46.46331 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75a9f351-9726-3f18-9fe5-86a90fba4bf4 | -8.36557 | -46.37234 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb2f4ef8-ae97-3a00-9e9d-df889c1a4d9a | -5.7406 | -43.27564 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cba9d3ff-3b58-3700-a67a-d92fa6ca0a44 | -7.8281 | -44.09671 | 2026-08-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8410c33a-826d-3aaf-ac43-962165964457 | -6.16274 | -47.79259 | 2026-08-18 04:02:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f3a5959-dbd5-3937-867f-706e81a12219 | -4.01001 | -48.90671 | 2026-08-18 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 060ee833-0797-3e9c-aafb-19e464c2e16a | -4.49206 | -42.56503 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 200ab2ce-24b7-37d3-9e0a-c48f321cd550 | -4.01059 | -48.90332 | 2026-08-18 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6ee02314-99bb-3f53-8680-11cc378baec3 | -5.7949 | -43.92097 | 2026-08-18 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b0e29a3-914a-35d3-a035-d967856ba608 | -9.01175 | -41.99662 | 2026-08-18 04:02:00 | NOAA-21 | DOM INOCÊNCIO | PIAUÍ | Brasil | 2203453 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 17e2dec0-e3b4-386a-8855-8ce7eb2c3934 | -9.28575 | -50.32364 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e70a7d58-9203-31e4-aa23-5e03027b4997 | -10.2706 | -50.41275 | 2026-08-18 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68ba43df-1ff2-3dc1-8597-3e7ee0d16e3e | -7.90491 | -45.00828 | 2026-08-18 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3cb7381-7b3b-33ba-9402-0d67c5a6b5ae | -9.08088 | -42.87884 | 2026-08-18 04:02:00 | NOAA-21 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e8d34d5-cecd-398c-9a58-7a9a95c87e25 | -8.37258 | -46.35703 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3e040f3c-0e6e-3f03-bf7e-dcf6bce33c7a | -7.16912 | -43.12133 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f1c1788c-ac9a-37ef-8183-1332d53f2ccd | -8.22285 | -45.78853 | 2026-08-18 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b47529f3-c7f4-35de-8982-9f12fb0cb27c | -9.4572 | -50.31517 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6f2b68f-d091-3556-84fd-7d45ea1cd3fa | -8.48879 | -44.73021 | 2026-08-18 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 815d8cc8-7182-3d8b-a85f-0e51f5a438e1 | -8.4927 | -48.82442 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 417e46a4-0589-3d39-867f-92521d2955ba | -8.33896 | -46.47568 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b28bf869-dc4e-3297-ae3b-88b4952943f3 | -7.82944 | -44.09978 | 2026-08-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a06064f-c4ed-39d9-9e90-e2d131b32d68 | -8.51272 | -45.31987 | 2026-08-18 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d4688c80-95f3-32de-976a-a8d8a5845e94 | -9.77749 | -47.28679 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7f7f330-6ab3-3dc8-a94c-761bb5f8f31b | -6.27667 | -43.27778 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4caa9f9a-8122-3ba0-8bef-db0bf896bfc4 | -9.12558 | -45.17673 | 2026-08-18 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e6a4d2d-89f9-3c1c-b0aa-917d5723c37f | -9.86096 | -46.77674 | 2026-08-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bc52ecf9-c0f7-3b44-81eb-cade8618038e | -9.46177 | -51.61864 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a70ed772-504d-3549-99a2-8e3ba2bbc642 | -8.59156 | -50.3539 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8d4f8c1b-b402-346c-b430-968b0fa4ea77 | -9.40319 | -48.2521 | 2026-08-18 04:02:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31576eba-4a9f-3341-9e32-ea385fb05d8e | -8.59363 | -50.34489 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 54ebe105-21d1-32e4-a0bd-d80c7266583c | -3.2072 | -49.05838 | 2026-08-18 04:02:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 566e8a8f-6f8b-3988-8d4f-848b4059a688 | -8.49665 | -48.83123 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 9.9 |
| cf5506af-6043-3095-8915-98aeba8adf51 | -10.28895 | -48.23996 | 2026-08-18 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7be9f341-cde3-3e05-81b2-0b865e9baa5e | -9.78191 | -47.28756 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90da73d7-ecef-3b24-a3c3-97af3cbd4874 | -5.79453 | -43.92354 | 2026-08-18 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a6dcc81-016d-3385-84cf-714aeb3e53a6 | -8.60534 | -50.34322 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a35919a0-0ee5-3a7a-be4f-5dc310b0fb46 | -7.45928 | -46.15865 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 418236a7-0756-389c-bc3b-976d6c0d551e | -8.32044 | -46.48077 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b93f9b74-a624-3f48-ab9a-10918f1cec84 | -4.96819 | -42.21262 | 2026-08-18 04:02:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 533fc3aa-a122-3d96-862f-e6d904776464 | -9.71051 | -48.37714 | 2026-08-18 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 14512b87-8d97-3529-81a9-12f5ffbf2fe2 | -2.87888 | -48.8562 | 2026-08-18 04:02:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1d766163-93ad-30c1-a497-a65d66609241 | -6.5333 | -43.12886 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f92e40de-4d7f-332c-a202-8a7c8d8fad11 | -6.43043 | -35.06894 | 2026-08-18 04:02:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 80a7bba5-9c8c-37c5-9bc7-170afbc25a12 | -3.50606 | -48.03284 | 2026-08-18 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28587c6d-2028-34f1-a888-1c92edb9b54a | -7.17552 | -43.42322 | 2026-08-18 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ec34d1f1-c1e6-3c71-bc0b-664f6f6b262d | -5.67258 | -43.5775 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6b47403-0dd4-3809-b35a-e67211076213 | -8.59431 | -50.34113 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 5fd5961c-513a-30a4-a019-3ca384308264 | -8.59915 | -50.34594 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 4e8af37e-3aa9-3e1d-add6-517211f1a7a0 | -9.45925 | -50.31205 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0107b54-d3b3-3773-b458-a6ed4f1a61f2 | -3.51125 | -48.0335 | 2026-08-18 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03d16db2-4a1c-3dc0-aa52-bf41823dba9c | -9.7961 | -47.30753 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ef8f955-729a-360a-90b2-fe5004c30f0c | -8.59917 | -50.34375 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4de4e1e8-b520-3cbf-bc50-d2b29e036b97 | -9.13795 | -46.01744 | 2026-08-18 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8ffed6f-3df0-38bf-8f1e-afd07b296e3b | -5.55388 | -43.42931 | 2026-08-18 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbb3b669-4da8-30bd-9d6b-2b855d8b64d6 | -6.27304 | -43.2772 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| cc9e6946-38ec-3fc9-a342-2b90d4ef8f05 | -8.60399 | -50.34853 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 20fc20e8-ee8f-3beb-8375-afd2b82f9569 | -7.45571 | -46.15385 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7b43332d-c1d0-3323-adff-520c1debd4f7 | -9.45858 | -50.31557 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0021ef3-9752-3b3b-9849-a2eff38e29a1 | -8.55667 | -47.39098 | 2026-08-18 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c532750-79a3-3d3c-b478-de306bcda235 | -8.49718 | -48.82827 | 2026-08-18 04:02:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 59ea4a9e-d4ae-32d7-b265-04eb0b2c6db2 | -4.7194 | -42.77087 | 2026-08-18 04:02:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a70cd99-4b03-31a8-be9a-986833850416 | -8.60466 | -50.34699 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a0e6779a-b620-3464-adb9-bb8c2916fc5f | -9.79581 | -47.31256 | 2026-08-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6bdc245-1ab3-304b-9ac2-de2948644271 | -7.28474 | -44.07106 | 2026-08-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16a0dd99-b874-3dad-9156-975044b78d4b | -8.59229 | -50.35237 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 521ae3fa-90bf-358e-82ab-bcdc460ae70c | -8.37125 | -46.36477 | 2026-08-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e09cea44-b69b-35c7-b62e-6f39e8319db1 | -5.80562 | -43.63897 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2d647299-64f7-36ee-9582-18d5e0d3fc30 | -9.15463 | -40.11225 | 2026-08-18 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0280aebb-4730-39d2-a8dc-1c669d3fe407 | -7.02393 | -45.90712 | 2026-08-18 04:02:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 739ac61f-f83e-3419-903e-47f409cb7acd | -6.58672 | -42.23083 | 2026-08-18 04:02:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9179d816-e140-33b8-a249-e1c32e190ffb | -8.59781 | -50.35341 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 3adbc95d-7ce6-3195-850a-d589103a85b2 | -7.24302 | -49.8944 | 2026-08-18 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 721b6ed8-a8c7-3d05-9fe3-35740e7be50e | -8.55295 | -47.38546 | 2026-08-18 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c4504295-2fdc-3deb-a7df-888a29edccfe | -8.59982 | -50.34218 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 5e726f02-4b68-3b05-ba87-9a59dcececbb | -4.53182 | -42.93187 | 2026-08-18 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc4ca140-ed7f-3f28-af2b-ef9f3b946902 | -5.26801 | -49.05344 | 2026-08-18 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d934fb65-c081-30ec-9ff5-5e9f5dcbda5b | -4.9717 | -42.21311 | 2026-08-18 04:02:00 | NOAA-21 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2fdd1e26-84ee-39d5-83a7-7f181164f9b4 | -6.70962 | -44.42468 | 2026-08-18 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39004f0d-a40d-348d-95e6-eaa5380f3a47 | -8.60469 | -50.34478 | 2026-08-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 44a00503-8f4c-3f22-a9ed-f3797295b20a | -7.1258 | -47.5441 | 2026-08-18 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| efbb0ffc-3fbf-3d49-a78d-2d4ab25bd88d | -5.2659 | -49.04894 | 2026-08-18 04:02:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d20f0794-73bf-3c26-b841-d62909f8d65f | -4.48619 | -42.55576 | 2026-08-18 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 30e64314-6a0a-38ed-bd84-70ad13a55713 | -5.01898 | -38.00838 | 2026-08-18 04:02:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f1ed308-dea8-3d56-a26a-2bb9a1e83caa | -9.4743 | -51.64907 | 2026-08-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 431c00ef-4714-3409-b8c3-7f5ce3b19a8a | -6.52971 | -43.12828 | 2026-08-18 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed9c1e94-40b9-31b9-9cf4-6da4aa9b059d | -9.13858 | -46.0137 | 2026-08-18 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c46683c-9712-3683-b9e6-1db90e5a4bdf | -9.07001 | -50.83782 | 2026-08-18 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5fb18a4e-5b9a-32e4-b387-de4bc9f9c78d | -9.13101 | -46.00858 | 2026-08-18 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95f66854-a874-36c2-ae67-fc8da55ac682 | -7.43587 | -44.87442 | 2026-08-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4a59c2db-919b-3e44-a9f1-d66599205eee | -7.21259 | -41.54263 | 2026-08-18 04:02:00 | NOAA-21 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 12384db9-ff94-3437-b7ad-77a2cf3605cd | -10.29358 | -48.241 | 2026-08-18 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 595dc41f-e607-3172-8e70-39fc7022640f | -3.68421 | -47.64883 | 2026-08-18 04:02:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 8cb94219-dd96-3075-b11e-00c08da19a37 | -7.16646 | -43.13765 | 2026-08-18 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 259dc5d7-17ef-377b-9b5a-88eda4b5311f | -9.97867 | -42.14129 | 2026-08-18 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1af2b825-5749-3d4b-bef6-76d9c015e268 | -7.5405 | -46.6172 | 2026-08-18 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README11.md)
