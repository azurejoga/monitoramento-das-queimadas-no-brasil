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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9005c38-37c8-3d20-8d2d-5adb741284ed | -4.83558 | -43.01173 | 2025-10-19 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a4b1643e-d500-36ce-9192-df0d00adb6fa | -10.15906 | -42.21403 | 2025-10-19 03:42:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c8edcc4f-09bf-3d9c-b6d2-cd27e8024092 | -7.19815 | -42.19553 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 625719a3-55ba-3a25-a291-3407a7b0a58b | -8.20158 | -43.95857 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0db22e25-00e9-3a7d-b5c3-b5ae445c91d0 | -7.0476 | -41.82661 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0cc58d43-1dd4-3f4e-8fb0-dd470c5dfe28 | -8.61061 | -40.19197 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 3d79019a-a759-317b-84d3-869ee63bf042 | -8.4539 | -44.16721 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| efce2e79-9e60-3907-add1-90a01ce4a148 | -7.41807 | -40.07028 | 2025-10-19 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 75664504-968f-3147-a4a1-046492c5c427 | -6.09977 | -44.02331 | 2025-10-19 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29deca7b-1cc9-3da5-bc29-1084d3bf72c7 | -5.71317 | -43.81998 | 2025-10-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d115843-304f-3ff7-ae09-2adc60a7c1fe | -5.48036 | -43.12733 | 2025-10-19 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3aa87cc6-f9b2-3aeb-a86c-d1491f807e15 | -7.4133 | -40.07468 | 2025-10-19 03:42:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 915a168d-ef5c-30a1-aae4-5834e3dfe006 | -7.20191 | -42.20098 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 49b8e112-709d-30ca-ab7f-00a157bbb03f | -7.77228 | -42.48151 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0377ca0e-e6c2-38ae-a46a-fa44d260028f | -4.15042 | -47.67852 | 2025-10-19 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5d026de4-8c72-3bd3-951c-9e9de19bd8ce | -7.84161 | -40.26272 | 2025-10-19 03:42:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e0a73205-1771-3adf-a35c-cbd4eb801d5d | -7.16578 | -42.35994 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 631cbf7f-35c3-3873-9186-d107c243545f | -5.35465 | -47.21604 | 2025-10-19 03:42:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9af4845c-4f4c-3238-828c-864193e2df9a | -7.18235 | -42.1784 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 74f69a24-8f09-386a-8729-d37f506773c6 | -5.36109 | -47.21751 | 2025-10-19 03:42:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 09ebbb8b-ef9b-34fb-9912-a67228784e89 | -8.3564 | -46.20727 | 2025-10-19 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02ee541a-db6c-301c-8834-5f78dabf1b45 | -5.08517 | -47.18743 | 2025-10-19 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec9272dd-d5e5-34a6-9727-5156b4845ada | -8.60979 | -40.19696 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 43.3 |
| 1e6627b7-a8bf-3511-8518-a8ec591548fd | -5.11164 | -44.58678 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37a4b53b-07de-3935-a0ad-d4e2650e626a | -5.77433 | -42.72932 | 2025-10-19 03:42:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2afa93e2-a6f1-3a70-95c7-997398e2805d | -8.43724 | -44.14311 | 2025-10-19 03:42:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28b26523-aba9-3826-b9bd-7a977289ffcb | -5.42209 | -40.89062 | 2025-10-19 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b765af70-7b7c-3c4b-b7f2-62ee184ce701 | -7.1958 | -42.20953 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1a80d8f5-a25e-3f4c-b071-cbe4f498e49a | -4.9171 | -45.70752 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4d78683-ef44-3d01-9b99-43e8f4acbed5 | -6.96592 | -47.45549 | 2025-10-19 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ede4a6be-93af-33f5-8bd8-4e888835b309 | -9.26353 | -44.33931 | 2025-10-19 03:42:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 837235b7-fa16-310b-a38a-f2500f163e46 | -7.84127 | -40.25941 | 2025-10-19 03:42:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3fd2ef8b-9a2d-3e13-b3a8-e49f69dd4acd | -7.16508 | -42.36324 | 2025-10-19 03:42:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8cd5afb8-8bf0-3169-8db6-6d53712049e2 | -7.2267 | -39.34469 | 2025-10-19 03:42:00 | NOAA-21 | JUAZEIRO DO NORTE | CEARÁ | Brasil | 2307304 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 31ad2bea-1870-3717-a1b7-4379bd472957 | -8.34924 | -46.21344 | 2025-10-19 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 877dfb7c-5856-3201-8290-24217eca9606 | -5.10086 | -46.13665 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| fb1c9881-b08d-32d8-a65e-d261141ae50d | -5.96224 | -44.19461 | 2025-10-19 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75fc3830-94c0-3835-87b6-952411db2a1a | -7.84245 | -40.2576 | 2025-10-19 03:42:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fd023e8a-6294-3b82-b3d6-62bae98ab239 | -5.75783 | -44.00092 | 2025-10-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53234efc-fa36-3c98-9563-4abe8d9e01fb | -5.6409 | -44.80748 | 2025-10-19 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2910a5f8-8ec9-3fd3-b6b9-3eedc82b73d6 | -8.24215 | -43.99306 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ccadc9e-90e4-37f7-bbe8-bf2241b1fcaa | -8.21165 | -43.96034 | 2025-10-19 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e2ace14-e9a7-3125-b9f3-239835930f76 | -4.23825 | -43.10154 | 2025-10-19 03:42:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0716a1e3-ab47-30a5-8185-1c968274c1ce | -4.77699 | -45.89441 | 2025-10-19 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 405bdbcb-7409-3dcf-8630-c169420959c8 | -5.89132 | -46.69613 | 2025-10-19 03:42:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5147a3ef-9a58-3c8b-8280-03c5b55f09ef | -4.91953 | -45.41687 | 2025-10-19 03:42:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 36bd4a90-7de5-3499-b6f9-0da08b0a362b | -5.89762 | -46.6969 | 2025-10-19 03:42:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 743d5d8a-3d1c-3882-8c18-7096bb34b6a4 | -8.89901 | -40.60689 | 2025-10-19 03:42:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01ffebfe-11b5-37e8-97fd-c6eed6b0077a | -4.97139 | -44.60899 | 2025-10-19 03:42:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35c07579-67f3-3ddb-9faf-280aeb516c74 | -7.18733 | -39.67215 | 2025-10-19 03:42:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 32467af6-9deb-31d3-8128-b49362f2cd79 | -4.2521 | -40.35054 | 2025-10-19 03:42:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 91822c6a-93a3-36cd-a175-4f3364d0678b | -7.19423 | -42.21885 | 2025-10-19 03:42:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 112c48ab-fd8e-3563-b2fa-81d77a2ab625 | -6.86983 | -40.04828 | 2025-10-19 03:42:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 26416074-9a10-39a5-90df-3d3d9424374a | -6.00703 | -44.18153 | 2025-10-19 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a0db4c10-5b22-3d9a-8425-59ebc7334c13 | -5.7121 | -43.82629 | 2025-10-19 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aab6c320-ad7b-3523-82f4-75e2e34fdc84 | -4.23336 | -44.68247 | 2025-10-19 03:42:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fd68517e-d242-3140-b259-71293489de96 | -5.3001 | -45.08107 | 2025-10-19 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 62d7c755-10b7-3230-bdff-abea2705acc1 | -6.41507 | -43.91956 | 2025-10-19 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6255ee34-7fdd-3706-8a30-e291e8c7485e | -7.18348 | -39.67153 | 2025-10-19 03:42:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 944e2ae1-8c70-3b2b-bf14-1a49dae92124 | -14.0636 | -44.67847 | 2025-10-19 03:45:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aadaac7-b916-37e7-8a45-7830c71ee82d | -10.53014 | -44.14285 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 764c2413-30cd-3caa-a673-9e9d783e961f | -10.8693 | -43.9442 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6cea58d2-a097-3439-9026-bbac6a1e3409 | -16.77652 | -40.63116 | 2025-10-19 03:45:00 | NOAA-21 | FELISBURGO | MINAS GERAIS | Brasil | 3125606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 16590485-b01a-37ae-8fb0-c39625ba481a | -16.78459 | -42.76669 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c3e97b52-7dda-35ca-916d-db729bafa978 | -13.93547 | -45.61307 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76537cac-3299-365f-9fa7-215a327fcf22 | -10.1483 | -44.52248 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 701149e1-57ee-3718-88fe-552578da0cb9 | -15.26577 | -43.5812 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68a8924f-0ce9-3643-8f47-3a05325d5774 | -16.7427 | -42.80774 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b0676e9c-4158-3e68-88bf-7280b64aa130 | -10.89137 | -46.07331 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5162987b-8aa7-3186-a6fc-322354fd3d0b | -16.76159 | -42.7952 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9aaa2d5-0426-3275-8db4-3eb0ade656a9 | -16.75422 | -42.79 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb35fc3b-dfaf-396f-ae85-470291c42157 | -10.10227 | -44.55338 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44794948-a363-31ac-ad3a-cd8b80f24c89 | -16.74685 | -42.78487 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f80071bc-ab85-399b-8525-634c421a6a8f | -11.62502 | -44.07765 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e7275a2-ee47-36c2-836b-75e7f814a58d | -11.65394 | -47.3206 | 2025-10-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 216865d9-80f2-3e1f-852f-a6e1e8ea1cb9 | -15.90744 | -41.57109 | 2025-10-19 03:45:00 | NOAA-21 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 82a484b5-962d-304d-95c9-f52b28f9de24 | -15.79895 | -43.64567 | 2025-10-19 03:45:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 704d9106-ae0b-3459-b0c3-04e7dd11961e | -13.53481 | -43.01491 | 2025-10-19 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| e0c5e388-01ea-31bb-a0d4-f6726b40514a | -15.77759 | -41.33366 | 2025-10-19 03:45:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8bd40c53-69c4-3912-b410-7d81441f3f37 | -17.41091 | -42.44352 | 2025-10-19 03:45:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37cf9ce3-edd0-30c8-a650-98eadbbf7181 | -11.47311 | -42.21988 | 2025-10-19 03:45:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f2c4e257-ca71-30e3-8c43-b4960372f902 | -16.14367 | -41.13499 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f5a86ba6-6fbf-3f14-a13c-e8798d1b4df7 | -13.53558 | -43.01067 | 2025-10-19 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 29.5 |
| f7b1e83d-5a13-3b82-9e29-36815e98221b | -12.66006 | -41.25761 | 2025-10-19 03:45:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 23a4b870-c0b1-359c-b7d4-b8c526a754a2 | -11.63224 | -44.09193 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1bce9bd1-b3c9-3ad6-a99d-57cd9b5342fd | -10.85596 | -43.93579 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 85019944-217f-35ac-bc65-01f5cd9cf60c | -16.75074 | -42.76336 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34076a05-5afc-3f2f-ab1b-c0c28c876ec5 | -16.76149 | -42.77273 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4734a480-4e83-3634-9583-a8e7efd6aac3 | -12.98532 | -47.27204 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51710e8a-15b4-3bf7-8a33-a752f415cd02 | -15.26144 | -43.58036 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fcbd200-f415-3fab-8ea6-f00b81f0ec91 | -16.77956 | -42.76449 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e8129956-304b-3637-8e68-ccf4b9e61e78 | -15.26064 | -43.58466 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad6fe79a-da97-3629-9483-ff5cccc8b0dc | -12.30246 | -47.25989 | 2025-10-19 03:45:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d049f01-7212-33a1-9f84-080090ee4843 | -10.23418 | -44.89898 | 2025-10-19 03:45:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ec67422a-a3a8-390e-9ffd-4823f304df1a | -15.82014 | -41.49079 | 2025-10-19 03:45:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1b294c75-fbdc-30c4-9262-8de314ac1440 | -12.47046 | -45.43521 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 360cb2fb-be68-37bd-9fe2-b4487ba210bc | -13.74484 | -43.60424 | 2025-10-19 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 569ae75b-aa7d-318a-a948-454eeaef3592 | -16.75218 | -42.77835 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a4db3239-a838-3016-9125-8048860b457d | -15.70899 | -39.68382 | 2025-10-19 03:45:00 | NOAA-21 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 178e215e-2174-3cc0-afc1-8365bf4adfbe | -10.13611 | -44.5317 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README13.md)
