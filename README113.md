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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 187547db-a8a0-3d92-921b-fe1085feb0e7 | -6.05007 | -45.17141 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 92374008-f0e3-3e39-b5b5-d2e1aff11283 | -7.14087 | -43.52054 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| cfbc617c-87ca-364b-88a0-c96d12820138 | -11.4649 | -49.74507 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cfd8dc24-adbe-3e83-926d-c3a272385527 | -8.10216 | -44.0094 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 0568813d-e2b3-3d93-beb0-461d2724f9cb | -5.52656 | -37.05529 | 2026-09-28 16:26:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 06f8002f-264c-3afd-bc8d-dedc8e871d48 | -8.73359 | -44.2356 | 2026-09-28 16:26:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6ea4d287-5951-3730-9563-76310ba04ed5 | -3.8028 | -44.10394 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| aa2f980b-b181-3f24-b021-3412cfe9ed87 | -7.41648 | -46.71947 | 2026-09-28 16:26:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 3aa6e154-2422-345f-b86b-1bcdac54488f | -8.27297 | -54.70202 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f654e738-4ff3-3e78-919b-3c07f7a9bae5 | -3.80665 | -44.10691 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| feb30c22-ab66-3251-9341-6a5f0968d48c | -3.494 | -42.50311 | 2026-09-28 16:26:00 | NOAA-20 | MADEIRO | PIAUÍ | Brasil | 2205854 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 7f582066-16ad-3b6d-94e3-e7bc4f57915a | -11.02351 | -49.70607 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0e77e564-8ab8-3dc2-bb52-f9dc65327ede | -10.90594 | -50.70388 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f8bb400f-010a-3279-9e4a-c7f00afbcd30 | -6.36139 | -45.80414 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 32920624-f791-3ada-b146-b86a0c1931ba | -10.18456 | -39.69322 | 2026-09-28 16:26:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 7.4 |
| dd200e72-4b1a-33f5-a784-1054cdbbcb36 | -9.99509 | -50.12363 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 66b6decd-c3a9-383a-860f-eebffbf76832 | -9.52436 | -46.37009 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7792fd6c-b6ea-3478-98a0-99b925dd61dd | -3.80839 | -44.09598 | 2026-09-28 16:26:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4699d06-8454-3024-9355-c2fac15691ff | -7.02036 | -43.73138 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 6ccf5ffe-e908-301d-9848-5d53847feccb | -9.94354 | -50.23443 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5e77cbe5-1d6f-307c-9b59-0127fa62e426 | -10.20139 | -49.9881 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 24a1d776-cb86-3e86-a20b-0a80ca214a5f | -9.72116 | -48.01944 | 2026-09-28 16:26:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 81152137-0c8d-3bcd-96e0-19b55711f659 | -6.00667 | -48.37631 | 2026-09-28 16:26:00 | NOAA-20 | PALESTINA DO PARÁ | PARÁ | Brasil | 1505494 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2cd14920-4d32-3bc6-862c-cee98d5e7ed6 | -8.7318 | -47.27441 | 2026-09-28 16:26:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e66fab08-52e6-39fc-a067-695c73adcd38 | -9.93815 | -50.23219 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8e859c6a-510d-3270-8f42-3a061ec9f3ee | -7.38765 | -42.08587 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 56fd8800-e461-3dfc-8455-6842c4872c43 | -8.65464 | -45.36735 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 675298d2-aa93-31f1-97a0-6fdb974b4805 | -10.23462 | -49.99986 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6cc1e125-91ae-38f4-a761-451f0750479b | -7.2768 | -44.31775 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 95bb9fc5-9afd-3df2-a5ea-25044c93041f | -6.21093 | -41.6123 | 2026-09-28 16:26:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| a36c3a75-4813-3e34-bf9f-72c4dcc04d87 | -6.04603 | -45.1681 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 92fb1d14-8553-3d82-bf80-02864788c14c | -8.66603 | -45.3699 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ea493015-a95f-377a-9db4-bcf2e21bc73a | -7.84321 | -46.93201 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 544d14b8-a6fc-3c2d-81ae-c137d6776800 | -4.55937 | -40.71263 | 2026-09-28 16:26:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 3103a0ae-39dc-33f9-83b6-0bc5b9ddda19 | -9.85664 | -44.94752 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 71654105-14f7-3592-a124-e4cbcd2ba247 | -8.27436 | -54.70808 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b592a04-621b-3e86-98ce-c1fe367982d3 | -8.10253 | -47.18719 | 2026-09-28 16:26:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 88ad9b10-16e8-3977-886a-addc8930b551 | -9.98589 | -50.13066 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 9168878e-a898-3119-9c12-2123edab22ef | -10.11067 | -43.94482 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 6669389d-32fd-3188-8bfc-0a023bb2a41a | -5.85643 | -45.91426 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4ecc3f44-1662-3f78-af65-bc0b9b24b3de | -9.97669 | -50.1377 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| b4f76103-884a-34a3-a19d-c3c0b1cb5b9a | -10.96674 | -50.67618 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b5360559-2af4-351b-85c4-e79aee64bc4a | -9.44691 | -41.81519 | 2026-09-28 16:26:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 533c7a17-3a4a-3f3c-ac33-1b12e4d22a05 | -7.05902 | -42.86605 | 2026-09-28 16:26:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| f372ba4c-aa4c-3f94-9f31-64174390c99c | -7.25459 | -43.35184 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 08c45aee-3700-390f-b22d-83d1b004cbb5 | -4.21653 | -42.9894 | 2026-09-28 16:26:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f38def6a-e34f-3cd5-bfac-8e0f11f83eb9 | -10.19852 | -49.99316 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| cf7dc6f5-187a-3798-a1ba-58845e7b8041 | -5.01871 | -42.99556 | 2026-09-28 16:26:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fa0998ad-e6f9-3934-8ee2-f42c576bf435 | -10.20398 | -46.68856 | 2026-09-28 16:26:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| c657a943-5dde-31bf-95b8-d8dbd5399a1a | -9.7722 | -44.83453 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0d379c89-1c61-3f34-a4ec-a6bd1f013992 | -10.26507 | -44.62459 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 3a0d2418-cbb7-324a-9cb4-2e1b7b6b2395 | -10.88774 | -50.6865 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 06b56955-2984-345f-b3b7-811a3cea4ee4 | -7.70488 | -44.92107 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0e900102-e274-36fc-8bfb-1abee0946c41 | -10.97804 | -50.68129 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| adaf8802-0ba4-3ac9-95c2-1ff0c391e52b | -3.47649 | -41.7686 | 2026-09-28 16:26:00 | NOAA-20 | CARAÚBAS DO PIAUÍ | PIAUÍ | Brasil | 2202539 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 95a771e6-29d8-349d-a8ff-dddfd5c3fd88 | -6.77502 | -43.65718 | 2026-09-28 16:26:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cfd06ae-e523-3b21-89f0-e8dc0d80b7d6 | -11.12944 | -51.17585 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6955122c-56a3-3325-a2b9-83736660e81c | -7.68527 | -44.88441 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 9ccb81c9-2a96-3413-8cea-b07c79f50017 | -10.59419 | -50.56647 | 2026-09-28 16:26:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 390c6a0e-ba16-3381-b2d4-6165a11e0aa3 | -9.77574 | -44.83399 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4ee0f8ae-e887-3575-b0ed-98e4cdd16b30 | -10.99016 | -50.69293 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 2ff159eb-5039-389a-81bd-9592e7220b09 | -9.51351 | -46.37665 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ad3e1126-8fa8-3ef3-95ba-c161a6535e9a | -11.08157 | -46.07475 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 40cfe761-9212-394b-ba37-0cd3213c406e | -8.17534 | -44.43412 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 74a1cfbb-7c18-3272-9ce1-73f0c59a94f3 | -11.13547 | -50.07164 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1468e102-4448-3fb3-a391-b94f96b27ed5 | -7.63985 | -45.51778 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ca77839f-80a1-3b4a-8471-cf17824c076b | -7.39991 | -38.85138 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 944638bd-ddc0-3423-b7e5-2d9937eba732 | -9.79229 | -44.82323 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 58b33695-4573-30d3-af99-d469d100055c | -5.60462 | -43.36577 | 2026-09-28 16:26:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 58f6e894-1dc6-3052-b3a4-f720e5b1c982 | -9.50007 | -46.38078 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 7c1f1e75-4bb9-3438-a609-044dd24d8dff | -9.17621 | -49.65559 | 2026-09-28 16:26:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| aa5724ec-e94f-3780-9b1e-a257deb63a01 | -10.90543 | -44.66214 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 5ed90558-ab42-3da6-a508-e577c9ecd7d0 | -7.68471 | -44.88061 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f1aea03d-9fc3-34fb-8edf-e03e1dc106fe | -10.59459 | -49.98857 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4e1ea7a3-fe72-3872-8a6d-6d9d50207092 | -5.64106 | -43.71922 | 2026-09-28 16:26:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 896f10a8-54a0-3e27-8090-d8f01c0ad0c9 | -7.60633 | -46.9334 | 2026-09-28 16:26:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3307b514-0bd9-3de7-8cf1-c175e604ffe5 | -8.8569 | -45.9914 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d1c933d-0532-31d1-b6a5-36c4009f2e56 | -10.2029 | -49.9994 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 75bb6cef-5b74-3798-af67-a554353f33b0 | -7.25617 | -43.36234 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3a25fc1f-14d2-398c-87f4-47e6c431d07b | -7.62794 | -45.5269 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| ef43b048-bcf2-30fb-ba3b-9058730ec667 | -6.71666 | -36.47214 | 2026-09-28 16:26:00 | NOAA-20 | NOVA PALMEIRA | PARAÍBA | Brasil | 2510303 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| e1fc496b-4651-3087-b1df-77c11e782848 | -7.28592 | -44.30895 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1070900b-f5dc-317c-b5d9-9810aea7d2f4 | -9.02586 | -50.80416 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 74e1f764-50cb-30b3-983e-8cc6c914e244 | -10.21432 | -50.0094 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 197.9 |
| e5a24374-194b-3221-a0ee-3330109784cd | -7.30168 | -38.6081 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| c87cf39d-4d9e-3e86-b705-8405d8e3c5dd | -7.78843 | -37.64861 | 2026-09-28 16:26:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 12.4 |
| e54eac85-fccf-3b36-85a9-a888ba3c3557 | -8.73868 | -44.90393 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 9a8fe324-405a-3e37-a36d-d9f1a29c5bc4 | -9.97517 | -50.12625 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 649f6c23-20e1-3e5e-a3ea-de03bf4830c5 | -4.20437 | -41.76164 | 2026-09-28 16:26:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9bdb32b9-2968-3ef0-a430-ccd207602fee | -10.76564 | -52.12671 | 2026-09-28 16:26:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8a4728d1-fd48-3d6e-be95-23ee714ea19e | -10.21625 | -50.01384 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 225.1 |
| 0f9826bb-f1ec-3db2-b159-66c386381dcb | -10.20864 | -46.69312 | 2026-09-28 16:26:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 3fefa5e2-216d-3ebd-893a-5f16363d78ce | -3.69422 | -42.19695 | 2026-09-28 16:26:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2c4f55a1-0cc5-3748-aaa7-14bb27cbc7a8 | -11.12858 | -51.1688 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5a0d8e7d-1e5d-34fc-874c-569034951c49 | -10.86572 | -48.51274 | 2026-09-28 16:26:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 551fe338-98ee-3f9a-8465-f91101a375e8 | -11.1055 | -51.11486 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6884ba4e-dbdc-379f-99dd-177edba30848 | -10.41092 | -53.82262 | 2026-09-28 16:26:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 44b37976-74fd-3d33-84c1-d067c751832b | -7.6879 | -44.80539 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9bba055a-c275-3a06-9c46-cf220482009d | -5.41387 | -45.89372 | 2026-09-28 16:26:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64a3e6b8-c314-3f45-8efe-9d76f4df4bb8 | -8.02641 | -42.8472 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |


[Clique aqui para ver as próximas entradas](README114.md)
