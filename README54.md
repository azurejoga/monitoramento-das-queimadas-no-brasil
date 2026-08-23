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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98940d1f-e08b-3206-9c08-514774f69099 | -9.52615 | -51.64998 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4708c27f-f0d9-3936-82a6-4d9ad4749981 | -6.80236 | -59.68022 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf9744dc-aea9-3450-bf10-957cc2ab026d | -7.48611 | -55.32733 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 757fa450-31f3-36b6-a0ba-912809baaced | -8.58988 | -54.75225 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9649690d-7935-3af4-9dc3-3a2c2c71c185 | -9.85716 | -60.11208 | 2026-08-23 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d598ef76-b250-3bbb-aa96-aba8ab1d600e | -6.78296 | -59.42509 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c89c31f5-655f-3410-88a6-d65533eb7924 | -6.5553 | -55.09249 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0b50466-afdf-3b6d-b902-15c540371abc | -6.11413 | -59.94019 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b1728100-7667-3e30-bd95-1ae12e9c4277 | -6.76313 | -58.67334 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 412525f1-1842-3bd9-9ebb-1de187ef0668 | -9.21337 | -60.77359 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 107976b4-48dd-3047-8b9c-855d8984e019 | -7.78534 | -61.43254 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cde3dd4-8f91-3284-8e96-5d731543ef66 | -6.75471 | -58.67682 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45266138-f206-38f6-b2df-856cedce88e5 | -9.11263 | -60.3346 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 850bd4b0-8cbe-3d0b-b954-787734ff57a2 | -8.92694 | -60.7236 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 497e21ca-65e1-3595-8cc1-a63935d34afc | -9.02203 | -50.73232 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 811cc7f6-1477-3698-ad47-f6a045dbd36a | -6.80583 | -59.68449 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df7e2e44-09c8-380b-8c89-f837aadc3efb | -6.7509 | -58.67617 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1b3c2cc-574a-38dd-93fd-1401d6099ced | -10.30787 | -45.35939 | 2026-08-23 05:04:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 160941e4-2f56-3834-bfae-d4436fd49d90 | -6.86135 | -59.41019 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c6bdbd9-96f9-35f0-9bc6-f1deeec50b2b | -11.43574 | -44.53382 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ecbbd8c7-1492-3966-9f00-ed0501b0575e | -8.99073 | -50.76949 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 725d01b7-cc66-3a44-8094-87ced0be64f0 | -8.5326 | -54.81432 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bb209c7-aced-32bd-998c-685cf1be9821 | -7.29931 | -43.00154 | 2026-08-23 05:04:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| be10b24e-a510-3674-8956-05d32358e3c8 | -6.67238 | -58.74593 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 8d34f4ee-6bbc-36ab-a4ca-1d52af7a123a | -5.67443 | -47.48856 | 2026-08-23 05:04:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b774ef2-53ef-354c-8e3e-7732896dbd43 | -5.57033 | -60.17596 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28f9c5aa-fdca-33dc-8298-8a463fbb6fdb | -8.53205 | -54.81779 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df6388d0-eca9-39da-a45f-e91df5597ac4 | -6.13099 | -57.84026 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 20742a29-d00c-365d-91a9-ac904b393926 | -9.21319 | -60.899 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb0645c6-5a45-32cb-8e22-7b562e24ad2a | -4.96727 | -56.27214 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b0b3fcb-74b7-3384-a96e-e7943a46eecb | -7.55264 | -61.17986 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7cf8482-d3b0-3769-aaa0-0e7eae9b402a | -9.0127 | -50.76966 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 400cdf5e-7500-3f25-90e4-c496a30a3b2e | -6.80525 | -58.64933 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3441052-cd41-305d-aca3-3d677848fba1 | -6.80296 | -59.67662 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d11e083-43cf-336f-a9c6-a3351be39e9e | -12.24309 | -43.12478 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c16bc87e-fa80-3f5b-bbb1-653d1bc49c0d | -4.20981 | -55.63557 | 2026-08-23 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab23b047-4dbd-3247-9f86-081dac4e3432 | -7.78611 | -61.42804 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5ef9230-4f5f-3788-862c-6fc662bf9592 | -6.18431 | -53.52657 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 55ee582b-e3eb-339d-bbdc-ec77aacb6acd | -8.92853 | -48.53735 | 2026-08-23 05:04:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 11da195f-1f2e-331e-8be7-468589650aa1 | -5.78071 | -57.57556 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 20f01a02-9e4e-3b91-acdd-6c8befd7bdf1 | -6.12034 | -59.92176 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c84b53c-c004-3328-bf18-96cbc6e9d3fc | -6.76236 | -58.67806 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37b9273c-2a99-36de-a560-04596a681f88 | -6.22646 | -55.6176 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 5ceb5e1f-acfb-319a-a87e-b2cac25d2817 | -6.75931 | -58.6727 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb094855-c4c6-31b0-b589-ae9e6109d28e | -6.76216 | -58.69528 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbbbbf2a-2e01-377d-a202-b421ec6244b7 | -6.76238 | -58.65393 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4c45eb14-eace-3eb9-9f0e-6ffb6974bc6d | -7.22864 | -51.68886 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df8633ae-d669-36fe-9340-2fd826375b04 | -6.13061 | -59.91935 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2700574f-5d51-3232-84c3-642179c2b72c | -11.21006 | -55.04257 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4266988-95c6-378e-b805-287278c235bc | -9.06309 | -60.43267 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d367781-8fa2-39c9-ba96-c0fc75eb08b8 | -11.21836 | -55.07634 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9675a012-9c44-38b4-80ff-0256aeb9a3b1 | -9.1464 | -65.9513 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0312a6bc-5756-3f1a-bbaf-23a7ec69294f | -7.67782 | -63.34895 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e2f397d-8bff-3146-88a1-f45fb5583f68 | -8.55137 | -54.8458 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97659ded-e420-391d-91a8-613e05331fce | -6.80761 | -59.67374 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1b91aae5-8312-3d59-9ccf-e04671b7491e | -6.91911 | -46.40949 | 2026-08-23 05:04:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f729c095-0538-30ab-bee5-cb6b77f175e2 | -6.76537 | -58.67641 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d4b31eb6-24ea-3c39-8059-e8220d27222a | -6.56657 | -58.58971 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe866071-5d70-34e8-80f9-2e5b7c6f0f6a | -9.14995 | -65.9513 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69b8d595-c99c-3fdd-9578-a6d7a8404c6b | -6.54391 | -56.25916 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f250616b-1181-38b0-957b-5b75593e93ae | -6.68708 | -58.72888 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| dcad47b0-a407-3158-a391-e6ff8d8402ad | -6.80083 | -58.98482 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3de9fd50-f1cf-3d78-918e-3e6dc6172879 | -6.82811 | -59.4255 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 300bb884-6e39-34e7-9016-193aa90cb70f | -6.54346 | -56.17596 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75f6297e-377e-312f-a05a-e53fdba5f956 | -5.95871 | -53.62347 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 49f2742f-411b-3081-9995-8007ee50225d | -6.86943 | -60.01708 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 259198e9-9297-3154-8918-53c6427f8b7c | -12.40678 | -42.90004 | 2026-08-23 05:04:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b0f8130f-57d0-3058-9a1f-20f29636d723 | -5.94873 | -52.12811 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0ecb09d2-2afd-3cd4-b2f6-596730b64295 | -11.21891 | -55.07283 | 2026-08-23 05:04:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb8d46c8-3811-33fe-9c86-5ef8204f5bda | -6.75394 | -58.68154 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44ae5ded-f474-3b00-9c40-b986a6cd210c | -9.06531 | -60.44458 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b8d1a03-d5fc-3890-aada-71522fe8c4cc | -6.85495 | -59.41216 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7bd69c20-358c-39b0-aaf3-cead490834e4 | -6.7973 | -59.41321 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4db75e57-9562-3417-b80a-c35391901698 | -6.65499 | -58.80212 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 500dfd2e-d20a-3f2e-93fc-b4d0136d53bc | -6.85677 | -59.41298 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e50a9831-245c-38c4-b5d4-9f849bd4bbdc | -8.9845 | -50.75885 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| efce925d-d00c-35f4-a1c9-e2052a449e12 | -8.58766 | -54.7234 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dac48056-510f-3c3a-9e28-8327e8846078 | -6.75776 | -58.68217 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b85c5294-bcb3-344c-9289-ba19984f437c | -6.64728 | -58.80085 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfd15363-a5cc-3403-9337-8c5d258f7635 | -7.26533 | -49.90329 | 2026-08-23 05:04:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b1c7124a-f4ff-3bbd-847e-537a617aa922 | -5.13805 | -56.27566 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e994f9ff-af12-3078-88b1-1ebfd21e0abf | -7.17962 | -55.41819 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d53848e2-d711-3469-bda6-01cd59f593dd | -7.61816 | -61.61081 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d6f4e75-26e9-3ca0-8ee1-8f6c3f4a3686 | -7.28982 | -52.53474 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acd79b61-601b-3885-adfc-d1b906e30497 | -8.53591 | -54.81484 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf5b59c2-02a4-30a7-8b44-04c27fc3abcb | -9.14233 | -65.95893 | 2026-08-23 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbbc169e-60bc-32bc-a413-efe6e9a930e3 | -6.70784 | -58.72257 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4634c242-81c6-3161-ab32-91c90c5f5da0 | -6.88944 | -59.03232 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 39874ae4-a869-3f72-b934-92b06e8122bb | -6.22419 | -55.48216 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d76d36a3-0ba8-37bc-8ba0-b186a5878cdd | -6.9572 | -59.06148 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42ffa9b9-a75e-31b1-8a63-292fa5b6e74a | -7.17903 | -42.74673 | 2026-08-23 05:04:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31b4fe33-3718-331f-8471-34223a8d5898 | -8.99282 | -50.77198 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e6af5931-3500-38a9-92fb-d3544c92d9db | -9.79099 | -46.61475 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| efb93331-0f63-3809-b83e-676022759d32 | -11.42974 | -44.53304 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f8cf6e8-590f-3789-b47f-9a83ffdc2f85 | -8.54194 | -55.33269 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d1f483-c879-32af-89e8-c1a894845206 | -6.78931 | -59.41185 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14a9b0cf-03bf-3be1-b10a-cf8ed74ed4ed | -8.54144 | -54.84422 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ce99fdb-f81c-3718-81cf-f401f2889145 | -6.77694 | -59.65736 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cb7fef7-34c4-3286-ac8b-4ab7a47ee9a0 | -6.6986 | -58.73074 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ee950f98-8d58-31d2-8b75-d7c310e4c4b5 | -10.70415 | -47.73596 | 2026-08-23 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README55.md)
