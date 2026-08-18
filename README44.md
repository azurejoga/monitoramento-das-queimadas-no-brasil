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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61f18649-3f55-3e76-a96a-f67c9b44237b | -6.9157 | -62.90715 | 2026-08-18 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eeb648c3-1a2d-3a99-8bcd-4a86e734eae4 | -9.47611 | -60.50533 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfdc99db-7d68-3a90-a745-6635ed285d2c | -6.73717 | -59.14651 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8df08f-d2f2-3fe5-a360-b9c2ea10ed15 | -7.60022 | -61.23542 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 875c5ade-0d31-3a90-8ecb-96076776d63a | -8.48905 | -48.81517 | 2026-08-18 04:57:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d8544b8-e8bc-34c4-93a9-0257513af551 | -8.58774 | -54.69086 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4077a48a-486d-35a8-ba0e-a326e57ca8d6 | -9.19271 | -60.80872 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0143b13a-8c54-32ca-977d-bd630314bbe6 | -8.51454 | -45.32595 | 2026-08-18 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 05cc2778-99f5-3188-be63-3f09ef51ce79 | -8.57985 | -54.69696 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2ad8f3c3-2f5f-3146-8ebe-099d90567951 | -9.46586 | -51.65832 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f9912ca3-3e59-3efe-a7bd-51637d360b2c | -10.31348 | -59.14542 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25d1fd7f-b8a1-33c0-87bb-d7ef8c9d83af | -7.53428 | -55.58618 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 67e94506-4d0a-34c7-87c1-ab71de82c9f7 | -9.16435 | -59.69678 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a6b98465-912f-34d9-a512-a65116358114 | -8.74562 | -45.31462 | 2026-08-18 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30aef3e6-f3ac-3108-807d-eb61bd4080d5 | -10.93482 | -57.10979 | 2026-08-18 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b8f8448b-b7b7-3145-a3ca-d1896fbef7e9 | -8.10024 | -51.662 | 2026-08-18 04:57:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6106e4dd-5408-3fa0-866b-1ab86a6be93f | -8.63875 | -54.70662 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 232e393f-e1a8-32fb-858d-44b27352bd26 | -11.92637 | -55.91177 | 2026-08-18 04:57:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 845debbe-afea-3159-bce3-6670ba77b622 | -11.2962 | -54.87546 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 49edb846-3506-345f-a7b2-c639dde89ab7 | -7.81894 | -44.60068 | 2026-08-18 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa0a0dc6-ebe5-3959-90cf-7b93e30c0a7b | -6.69712 | -58.96312 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb893307-aba0-3373-9b8c-e873b4ce872b | -9.42474 | -60.4499 | 2026-08-18 04:57:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b4932e57-eb3a-34a0-8c0d-279abc62bd36 | -8.53242 | -54.90535 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea826235-1d23-3894-8a76-16a47b9222fc | -7.90877 | -61.73066 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f364ab0c-db6c-30c1-b0f2-dcc73ef3665b | -10.1773 | -54.22736 | 2026-08-18 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b96d9fe8-85f6-368c-9eef-3755ce5d07e4 | -9.06971 | -50.84147 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| bc19febd-a548-3d1b-8cd0-41b8f566cade | -9.07735 | -50.83844 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c1921555-c43e-3dac-9d7c-b5d21c8863de | -6.75691 | -59.16265 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6691e004-4cfa-3330-b071-ef9af46c090d | -12.77135 | -48.42536 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7a164b29-2f30-3a68-923f-b7937693f9ed | -8.89314 | -60.55273 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a157ec8-d641-3f0d-8947-92941e4ea53e | -8.58217 | -54.68254 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b308606a-93e1-34a4-bee2-093d0bfdb3f3 | -12.4612 | -54.1791 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ea1bca6-1c21-3e6d-b1cf-f7b79a66a482 | -8.20707 | -55.0303 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc7494f7-543e-3be5-9a46-85620aecf2b6 | -8.60268 | -50.34777 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 50136270-a9c8-3d61-a3f6-638bdbd8b585 | -11.33645 | -55.25428 | 2026-08-18 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba642997-16e2-3a27-aadf-a8cd0a9fdc73 | -11.54769 | -46.22166 | 2026-08-18 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f54b9a6-bda2-3d18-bbaf-743298292e61 | -8.60071 | -54.68566 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 937e5019-c345-374e-a7fa-683b1f1b6a46 | -9.07272 | -50.82175 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56a8c216-561f-3ea3-9e5a-8982c5042433 | -11.52053 | -46.63839 | 2026-08-18 04:57:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ea7f4d5-8328-3147-9342-9ecdf57491a9 | -8.72732 | -62.90275 | 2026-08-18 04:57:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa4c79e7-9527-3eea-903a-7ef063a59d0a | -6.99232 | -59.05076 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6edcbad-1abc-3e64-8bdc-36d6bc153031 | -7.45542 | -46.15763 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ee4c883c-e690-35f8-aaec-df72019a653a | -13.55916 | -51.69442 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6cd6367e-0ad0-3eaf-befc-c201e2f1affc | -12.46008 | -54.18614 | 2026-08-18 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9c72415-c96b-3639-a6b2-33ad30c7c4af | -8.59491 | -50.35078 | 2026-08-18 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 837a1251-d9a8-39c9-8e5f-a72dd717fe4d | -12.13029 | -57.2077 | 2026-08-18 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5236210-1446-3746-9034-e013ed70670d | -8.56918 | -54.69887 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc28645e-aaec-3370-98f2-a65fe1ad1d33 | -7.90661 | -61.74284 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f85fac4-dcc1-3cb3-adc0-412c8ff48532 | -8.89692 | -60.55848 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e80d387f-6fb6-3e0a-8790-ba4bc93b1372 | -12.77036 | -48.43256 | 2026-08-18 04:57:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 751fc610-82fe-30e0-a922-5a70cf76948f | -8.20366 | -55.02973 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a994ddd3-872a-33e7-a767-1869ba93a6d9 | -10.78188 | -50.31831 | 2026-08-18 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5051b0ce-daee-33ad-8c2e-6047f730665c | -9.13583 | -46.02041 | 2026-08-18 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 87d61683-75ba-3056-b1a9-70fff777637e | -13.5621 | -51.69904 | 2026-08-18 04:57:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa3e34ab-7a15-3f5e-8b74-a14288f8e685 | -7.06991 | -56.66012 | 2026-08-18 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fdac658-a896-3c10-bb0e-6adb2ff0231b | -7.82474 | -44.09932 | 2026-08-18 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 694490af-6d2c-3310-a17b-5c30a0b925b2 | -11.20727 | -54.81691 | 2026-08-18 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fc1d222-c967-39c4-b604-644cf0b1396f | -6.74019 | -59.18189 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c370c570-0f88-371e-b567-dce7cd9e3bc8 | -9.47441 | -51.64815 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d7ce507-cd02-371a-a77d-4716627e8382 | -8.98114 | -60.50636 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5f287de0-540d-341b-8f2e-b7e0f14d1247 | -9.01266 | -60.48452 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5af0d319-b7bc-3ed0-8a56-36db517446ff | -12.34012 | -55.33544 | 2026-08-18 04:57:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 592b5482-2503-33cb-9d46-aa99d697052e | -6.84296 | -59.00459 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e9a212d7-38a7-3a80-b2b4-241a3c98971a | -8.74067 | -45.31401 | 2026-08-18 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e4f54f4-6ac8-3102-8390-19859c4eba07 | -10.28102 | -50.44747 | 2026-08-18 04:57:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d58e198-bfc4-3860-a365-f27c01eca672 | -6.85088 | -59.01023 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 07299099-9f1d-357b-a79d-4571136bfbed | -8.58485 | -54.70888 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96e2da49-18ca-3c20-970c-5a5beaffc81c | -8.21821 | -55.02791 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9d7281ad-a176-30b3-8f8b-5b80fd0c7954 | -9.00964 | -60.5064 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 8c243932-905e-3bd2-954f-3e91f1df0b27 | -8.57963 | -54.74138 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8164cb45-ffbf-35d5-a62c-3a3087aeebf8 | -8.89943 | -60.59904 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1928c1a9-a486-36fa-a6c5-2d71153a5dcd | -8.89687 | -60.55108 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9aba4078-0465-3ab6-84f2-a181334d6206 | -7.91278 | -61.73774 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a8c405a-9bf7-3f59-bc89-b89a5fdb411d | -8.58078 | -54.73418 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c9f26e77-af4e-35bc-a486-cb995df9690d | -8.96304 | -60.52794 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09968b1a-6356-3a68-a77b-3ed09991c9f6 | -7.88395 | -63.76622 | 2026-08-18 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67828ffa-3d5d-3d5e-82c8-05a1552aba1b | -9.17197 | -59.67376 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 370f1890-1ea3-3633-a88b-736605c8dfe3 | -9.46243 | -51.61223 | 2026-08-18 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 05518e67-7e5d-30b2-a40f-fc6968d235fa | -12.26157 | -45.87415 | 2026-08-18 04:57:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 98ebbae0-4d61-34f8-ba43-1293d9a2458c | -8.09522 | -61.35024 | 2026-08-18 04:57:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fd99aea-72b0-3947-862b-68ddc72fbd82 | -8.57916 | -54.72275 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8bd71c61-c451-3300-8351-fb1d4b09aa9c | -6.85157 | -59.00617 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d3e3e5f-6bfe-33ee-bc13-c49b1a4d7e8a | -9.15944 | -59.67419 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0c6ec97-404d-3b09-9e8c-18b7fdd2daee | -6.83863 | -59.00391 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 74d84a98-b384-3a00-835a-d916a0071979 | -8.57254 | -54.69943 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c4ebb9fa-ca68-31f9-83c7-cef6d8116779 | -7.38112 | -55.48573 | 2026-08-18 04:57:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09fb9174-b401-35da-a466-6fa0db5719ed | -9.28415 | -50.32367 | 2026-08-18 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e9f51ef-3d7b-3c7c-ba14-2de9492e2889 | -6.10225 | -57.7306 | 2026-08-18 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a90eb49-63a0-3008-894e-d8ecb1716799 | -9.93499 | -53.63644 | 2026-08-18 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29f9032d-63e2-3454-af79-90c92b40ab1a | -6.85365 | -58.99395 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 807a720b-b129-3dd7-9602-dc1dc1eaf481 | -11.11719 | -46.49593 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 944ab4fd-8369-389c-94f8-cda0419e94dc | -11.12045 | -46.49365 | 2026-08-18 04:57:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4da26bdb-df85-366f-b091-2eaafb18f9d6 | -8.94919 | -60.52548 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d76c1bf-111c-3017-9047-6037cc63315c | -8.62748 | -54.71223 | 2026-08-18 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40d78b56-774b-3739-b594-c15c1157f29c | -6.83792 | -59.00805 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 60874771-21bc-3691-9735-28d1f0d941d3 | -7.45609 | -46.15296 | 2026-08-18 04:57:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75b31de5-3c6e-30e5-8f1d-7446f1baa67c | -9.16691 | -59.67718 | 2026-08-18 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8edcb38-fcbd-3767-8dd2-c5c04143177b | -8.08151 | -61.36465 | 2026-08-18 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e0c2424-7356-37f4-914c-d161f24f404f | -6.85295 | -58.99805 | 2026-08-18 04:57:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21d52148-cb53-3569-b790-341204b52c9c | -9.73541 | -60.74641 | 2026-08-18 04:57:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README45.md)
