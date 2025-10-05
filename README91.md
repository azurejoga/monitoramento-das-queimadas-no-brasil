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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3daf48b8-a0a7-347a-ab40-8cb854152629 | -11.91432 | -55.90856 | 2025-10-05 04:46:00 | NOAA-21 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16ea0413-ca5d-3364-852f-b413281cdcc3 | -13.31678 | -48.06948 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a034bf93-383e-330c-9857-49c6914ac338 | -13.2738 | -47.59017 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea85f43b-33b2-37f8-b4bf-e53b67d288ad | -11.23337 | -47.8053 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25746efa-cd14-3b59-97c2-ef6f5bd1d3ad | -11.23924 | -47.79177 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 670ede7e-942e-3f83-89a9-0b5b66b0923e | -11.4548 | -51.5224 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0891be0-64d1-35f4-a352-35349967001b | -8.86916 | -44.84505 | 2025-10-05 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a16f4d2-6757-31d8-a98d-c02eabac2085 | -13.32968 | -47.57034 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6feecae9-344c-301e-be6a-f7811c603bba | -12.30635 | -55.12925 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f2d21e9-4b99-39e2-a016-7e4b02441e7a | -11.04023 | -47.79584 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40cbd708-238d-3f29-9ac1-493ff49b1613 | -12.31434 | -55.12967 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dd5b909-ef5f-3148-a3b6-ec46fdd6e541 | -13.11542 | -47.93175 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76d81f16-6861-333b-b1de-dd357d53b860 | -7.78856 | -42.59483 | 2025-10-05 04:46:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c2afdb27-9bc7-33c8-b991-ebbd0efbf7fe | -10.84073 | -57.18489 | 2025-10-05 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bbc7a1c8-bee7-3b67-a1e4-b8f692435775 | -13.32473 | -47.17783 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 443c3724-b3c2-3275-8ad3-faa58f09dde1 | -8.54269 | -46.30668 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aea1b17b-2c0e-33bc-9278-3484cf03055d | -11.5504 | -47.69242 | 2025-10-05 04:46:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10310fd0-8d04-3d3f-99be-ad909ca388b1 | -8.6209 | -54.99741 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f2beae04-2713-3b37-b4e0-fa1644a32635 | -13.10759 | -47.87138 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4d69a49-6536-3b69-82ca-e7690189b2aa | -11.83774 | -45.07679 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5219b09-dfbf-396b-9ee7-0336c233b8ab | -13.49806 | -47.27764 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c12bb899-2505-3f39-99cd-eeb873a65fc4 | -7.61267 | -45.46911 | 2025-10-05 04:46:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8ac29589-0a7d-315f-9f5e-1c7a4f04aa71 | -10.65201 | -58.75986 | 2025-10-05 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d785d66-fd63-385a-895f-c428170a2c9e | -13.2699 | -47.18813 | 2025-10-05 04:46:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba602fa2-7d35-37db-b7a7-d632bf607c1c | -9.19441 | -62.52835 | 2025-10-05 04:46:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d2f0d5a-d806-348f-adfd-3cb843f366a2 | -9.12492 | -44.39029 | 2025-10-05 04:46:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9d4e4ee7-4486-3b29-bb84-886a31301e6e | -12.5666 | -48.16228 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 63f37702-d3fa-3e32-8acc-58c6abe6cb29 | -12.91232 | -47.31283 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 16e1341f-2b42-372d-a7e9-ae1aebb1c6af | -7.04192 | -42.75918 | 2025-10-05 04:46:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a5735d9c-d786-3aa2-b55d-54f5242bcad6 | -12.53385 | -54.74646 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08d41ba0-1d00-3f43-90b4-422494337ddc | -7.78125 | -42.6007 | 2025-10-05 04:46:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ea5a9b02-0156-3fd9-aae9-4fc04b04b5f6 | -11.53533 | -47.2298 | 2025-10-05 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4600850d-71d8-3f5e-a3cb-d95d23d77015 | -9.28971 | -46.01806 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 04b8d574-7ec1-3ff3-b4cf-c1214e09cfc5 | -8.87121 | -46.7172 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7a7b7ff7-b47b-33bc-9237-bd4fb1e293cb | -11.51384 | -54.47105 | 2025-10-05 04:46:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eab1bbe6-f9bf-3e29-bc73-64fa55d2fed8 | -7.01297 | -40.31575 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c628ab43-ae0c-3b90-ba07-f7b23edc0489 | -8.60071 | -46.27785 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9c48dca4-cdc6-36d6-9563-6055e067db95 | -13.1599 | -50.88092 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 620563ed-dc75-3ee8-b288-c2967d301575 | -7.72026 | -46.26948 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4e9491d-09ae-3df9-9825-223268ecdf83 | -11.13088 | -47.90133 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 167fcafd-5286-3750-a3e9-c2a562fa56ba | -12.91689 | -47.30973 | 2025-10-05 04:46:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d97079df-1913-3743-b8bf-2f4b2f22ee88 | -13.28343 | -47.60955 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bab36ff9-6e38-3b02-b992-f403dba9c74b | -10.84457 | -47.98145 | 2025-10-05 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 711f6158-78f6-323b-8a3c-7ec2c9786e6f | -8.62231 | -54.98877 | 2025-10-05 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4febe7e3-154d-3219-be1a-92e911ba28ff | -8.12409 | -44.10208 | 2025-10-05 04:46:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b538a005-b59e-3ada-a4e2-5f96d61af90f | -8.24076 | -46.80864 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5323226b-df93-325a-9889-b54e6951a452 | -7.24041 | -44.88259 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee9e693d-f857-3d50-bf7a-ff10faf1b4c5 | -8.54322 | -46.30302 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6c816ba-d228-33be-9469-2f55252f65b4 | -13.59889 | -48.16669 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da22c673-5b0b-3746-9477-21100a4714d4 | -13.50211 | -47.27868 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efdfc4d0-f69d-3a79-bb59-41ace99738b9 | -9.32577 | -45.66319 | 2025-10-05 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cdcde183-7d5d-34be-a262-a20101122b70 | -11.78117 | -47.9258 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f985acdc-bfa0-32cc-b9c7-5908af858336 | -7.24731 | -44.89692 | 2025-10-05 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55124653-4522-353f-9c38-e5b64330d484 | -11.81639 | -45.06934 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 551f753e-445e-3f0f-b7b9-f94113a370ff | -13.13284 | -47.97904 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 32db5b67-ec52-3275-aa31-7836b26869fa | -11.23405 | -47.80056 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 541b1aeb-65ff-36db-869e-153525091f0c | -11.31657 | -49.04659 | 2025-10-05 04:46:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63b9ace6-f913-36ca-b352-707837edfbda | -13.59284 | -48.16204 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbd72f67-4eaf-3afb-b304-61ccf66c7768 | -12.6035 | -48.12272 | 2025-10-05 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 17390820-fb6c-3094-84df-34a001ababe4 | -13.28296 | -47.61303 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f1b9bfa9-6d8d-38d5-ac8c-858a99e7caa9 | -7.72272 | -46.28121 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ebd16a9-66af-3645-850f-501dae9929e9 | -13.45935 | -47.29058 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 7d7c8448-504d-3dca-a420-1732e09c598a | -11.45245 | -44.95099 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64046444-9386-3b54-bcc5-345eb9491c5c | -12.29004 | -46.78262 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09398bd3-0a6e-3ddc-9f45-46c94f08bef2 | -11.78661 | -47.5504 | 2025-10-05 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65959367-5dfc-307a-b07d-fcb0cc513fd5 | -11.21092 | -54.98797 | 2025-10-05 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bce0b15d-4454-3981-8fa1-5579234632f8 | -10.39171 | -45.39274 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d9c2e70-db0c-308e-850c-5e731863c44f | -11.48325 | -45.04194 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b1a2ed78-1337-3a79-a2b1-3833f2788655 | -9.30035 | -46.0032 | 2025-10-05 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13e30890-74f7-3300-b17d-c0a6748e1b60 | -13.28699 | -47.61343 | 2025-10-05 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5458a2be-6ed0-3cc3-a849-c54aa2895fcd | -11.82023 | -46.85781 | 2025-10-05 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 6ca21062-c248-3e90-90f3-b9b6d35f92b2 | -11.93177 | -46.42796 | 2025-10-05 04:46:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5c78271-792d-3089-8c22-650fcaa623c0 | -12.59247 | -54.75645 | 2025-10-05 04:46:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b31b8e7b-83af-3b8f-922b-8ee417f6553e | -8.16821 | -43.34787 | 2025-10-05 04:46:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5d9a85a3-6022-34c0-ab74-6e43bf54e5df | -12.32136 | -55.13088 | 2025-10-05 04:46:00 | NOAA-21 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3cb6d5c-eb41-3439-90c9-8f4363a18e3e | -7.52012 | -41.26952 | 2025-10-05 04:46:00 | NOAA-21 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2763a8e4-f76f-3323-9cb6-2fa0c2cbf472 | -10.80703 | -48.81894 | 2025-10-05 04:46:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1137ac83-186a-3ce4-a324-535766a9cd11 | -10.07254 | -48.18271 | 2025-10-05 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 98a0d311-1586-30f6-bbe1-c8a88ca7bb1c | -13.16441 | -50.87399 | 2025-10-05 04:46:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ebe8350f-44de-3859-88e8-184b950b73c8 | -12.46034 | -45.50996 | 2025-10-05 04:46:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04f30a36-af98-3722-8464-cb53e0a262ab | -6.43178 | -46.02057 | 2025-10-05 04:46:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ecd47fe2-542c-3e92-98e9-622b7bfe01c5 | -8.24148 | -46.8037 | 2025-10-05 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2f974dd-fad6-3aca-a8df-045b49889168 | -8.90065 | -46.68239 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 4c4ac842-84c2-3584-938c-ad3eaf5956ef | -9.91179 | -58.56394 | 2025-10-05 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4286203e-829e-3225-bbfc-f9a70eb6b521 | -11.2268 | -47.74086 | 2025-10-05 04:46:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ad2c7ac-96e5-3d08-be71-a2341ce661b9 | -11.13404 | -47.92781 | 2025-10-05 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a491cff-3f07-3db8-bfaa-3152e6dc3624 | -11.50106 | -44.97853 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05b3bffe-d89b-33cb-b249-42811ca1341f | -7.7462 | -42.54716 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24bd0107-7213-35b8-926f-20b4e1c3172c | -10.39664 | -45.4146 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5742f4dc-5847-32b0-b14e-9d7dcbfeb299 | -7.00136 | -46.03085 | 2025-10-05 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78edbc0c-e445-3c07-ac6e-ce88d2529a4d | -9.1605 | -58.30858 | 2025-10-05 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0db16154-2c42-3b9c-927e-7cd1260dd8f4 | -13.12076 | -43.84707 | 2025-10-05 04:46:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a4fc8e2a-cf26-30ed-bd54-f0b1ba8b89bc | -9.64047 | -54.31456 | 2025-10-05 04:46:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d72cf8f4-a8c2-3556-bc72-bf08f47f9d0f | -11.26366 | -47.78601 | 2025-10-05 04:46:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42d4d718-f0e0-3d7d-8b93-4dd47649f903 | -8.55031 | -46.31151 | 2025-10-05 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40beaa04-d09d-3f76-b78b-1c7900fecc2c | -8.22245 | -49.1418 | 2025-10-05 04:46:00 | NOAA-21 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 8fbb8f22-531c-38f1-8eb7-e7d8010f93e3 | -7.74665 | -42.54386 | 2025-10-05 04:46:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a72d5200-4d7f-3006-92ca-0773d70091c3 | -13.05957 | -44.9363 | 2025-10-05 04:46:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e51e870-f6c6-3e4a-b129-1dbb488ee26a | -13.59501 | -48.16611 | 2025-10-05 04:46:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01468734-3622-3d37-a7d8-1ff7e174786d | -11.48711 | -44.97641 | 2025-10-05 04:46:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README92.md)
