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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0ef4d86-e7a1-3cf0-aed7-f369179aa56a | -3.45509 | -39.26622 | 2026-01-01 04:23:00 | NPP-375D | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 29805674-2dbb-348b-b7f0-34c4fd990ef5 | -2.37752 | -47.41718 | 2026-01-01 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c06a6d0-94d8-3653-b789-232f60fe2e62 | -4.01693 | -38.87145 | 2026-01-01 04:23:00 | NPP-375D | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6952eabb-7e7e-3105-84ab-ba94d7371784 | -1.79023 | -45.89769 | 2026-01-01 04:23:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 28560b7a-414b-3d34-b9bb-8b73c456766a | -4.40738 | -40.6933 | 2026-01-01 04:23:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b1058d95-d6cb-33f2-a847-9c86c69ac93f | -1.78963 | -45.90146 | 2026-01-01 04:23:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd7b15f2-9f83-33e0-9fce-86d5977304ff | -4.60404 | -45.99237 | 2026-01-01 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9cfa3d2-5504-38f2-ad2b-8e3220235c7a | -2.3395 | -44.90089 | 2026-01-01 04:23:00 | NPP-375D | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6fb154a9-1951-3883-bf57-72c7b486dd48 | -4.60006 | -45.99545 | 2026-01-01 04:23:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 56b7b773-64d9-302a-93db-50a74a1ef030 | -1.5451 | -47.21434 | 2026-01-01 04:23:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4ef6a6c-c419-355e-92ab-b89c4982bfd2 | -5.28683 | -45.83001 | 2026-01-01 04:23:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e395b5ca-f709-34c7-a20c-22b93aa0f440 | -4.32846 | -45.35135 | 2026-01-01 04:23:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f011047-4894-345f-b278-969b092cf380 | -3.89545 | -42.52411 | 2026-01-01 04:23:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 926602c0-c925-31fc-8a6b-a35f752f3072 | -4.40577 | -40.69507 | 2026-01-01 04:23:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6209d791-7b1c-3fa8-abfc-db1b46d3d252 | -3.37648 | -43.75631 | 2026-01-01 04:23:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4d80c8b-8f9f-3ab4-baa2-cfbe8ed7a930 | -1.48721 | -46.03107 | 2026-01-01 04:23:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a424670c-7093-3d4a-a558-bac907c70e17 | -6.59582 | -35.17613 | 2026-01-01 04:23:00 | NPP-375D | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d04c664c-9267-30b7-a81a-ca0c7ff17ebf | -3.02254 | -50.51107 | 2026-01-01 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 010a3a3e-7aa4-337e-a8e2-a8e0069bfcae | -1.48372 | -46.03052 | 2026-01-01 04:23:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36500035-7417-31e1-8220-f7bfba5e8d5e | -5.6358 | -46.31178 | 2026-01-01 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb3efb4c-7f3f-3c7a-a4ba-38eeac3e38f8 | -9.56791 | -44.59988 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 138abd53-f1e4-3ce4-b5ae-8e36603eedfe | -0.96496 | -46.78719 | 2026-01-01 04:25:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef777c40-be65-39c0-a445-bd35a57f6ae1 | -5.92564 | -43.4006 | 2026-01-01 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3257eede-4a62-3e4a-8a94-63efe5cd249c | -6.06147 | -43.73898 | 2026-01-01 04:25:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 868ebb60-cf98-3739-9f9b-c4ba8238b205 | -9.57517 | -44.5974 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9bbbefb0-9a33-3145-927d-7eee25e7ef7c | -12.61335 | -38.04374 | 2026-01-01 04:25:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8e42c321-b55b-34b2-a62d-74052bf50df4 | -12.61764 | -38.05021 | 2026-01-01 04:25:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 3b901ae5-ecea-38f3-b88c-8532b73341cf | -10.9402 | -49.42595 | 2026-01-01 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1acb2ec3-27a5-3f36-b654-614b918c02c2 | -1.36705 | -46.06022 | 2026-01-01 04:25:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f734838d-e36f-31fb-b158-4e07b72e2478 | -12.66037 | -46.76176 | 2026-01-01 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf25843c-c782-3735-8c6a-3b9ac0ac032a | -7.57114 | -49.39743 | 2026-01-01 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1156b1f-cb61-3fb0-adc3-7b6ebd6bc017 | -5.72515 | -45.03516 | 2026-01-01 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eeed02e6-a55a-3921-b584-4cfc6e1b759e | -5.72459 | -45.03863 | 2026-01-01 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cb8a0c95-d673-382f-92d0-0728f394836d | -5.14771 | -47.25419 | 2026-01-01 04:25:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8644fa2f-e655-3a02-bde5-ee393fae88fe | -5.52754 | -47.67059 | 2026-01-01 04:25:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2434619-22c7-3e53-94e8-19fa85dc37c0 | -0.96564 | -46.78301 | 2026-01-01 04:25:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fe691e7-9242-3c99-bc0b-cf10f6cfe072 | -5.72404 | -45.0421 | 2026-01-01 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3d958347-127c-3aff-b39c-50f08b0e3ac2 | -0.92141 | -46.89872 | 2026-01-01 04:25:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cc548e-78a5-3241-ac20-623f886a7296 | -0.9654 | -46.78474 | 2026-01-01 04:25:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b0d6c34-3ddb-3ff6-a20e-5345047b6539 | -9.18996 | -40.55663 | 2026-01-01 04:25:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f43f7c56-cb7f-3395-a57b-f0dc517e4536 | -6.29734 | -46.99728 | 2026-01-01 04:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b80cfe5-ddb2-3873-922a-da7d087b6e62 | -5.59163 | -46.36845 | 2026-01-01 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e5f3300-39c0-306e-95ed-7f3a3e827bad | -7.14104 | -45.2597 | 2026-01-01 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 507f0188-efe1-32b2-99c2-1a9b5cf51358 | -5.72349 | -45.04557 | 2026-01-01 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cc317b17-28c3-3072-a811-31775a0aaddc | -5.92902 | -43.40113 | 2026-01-01 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb2dec55-2c36-3ac6-ae1e-7aeb58939ec1 | -12.6637 | -46.76232 | 2026-01-01 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1843904-e301-33f6-840d-550d698f1d22 | -5.47896 | -45.43567 | 2026-01-01 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfb30284-b3f5-32c9-84d5-6fa700a73711 | -5.59505 | -46.369 | 2026-01-01 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b63e448a-1048-33b5-8e21-948517f4a276 | -9.57072 | -44.60397 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 99a4f7bc-4053-3878-b426-88843517cd8a | -8.11458 | -48.06361 | 2026-01-01 04:25:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e6427dd-4da7-3ede-abcc-58bb88fa4190 | -9.56737 | -44.60343 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 30319c2b-9d26-3b04-bbde-9205aebf32b5 | -12.65856 | -46.76122 | 2026-01-01 04:25:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 21e5569b-962e-30be-8352-35d38827a583 | -5.92508 | -43.40417 | 2026-01-01 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1a48e69-5d47-3a1d-b12a-0a376e104947 | -8.12104 | -47.99036 | 2026-01-01 04:25:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aff156c6-1b30-3914-8394-fbb1ad907788 | -6.42142 | -39.64534 | 2026-01-01 04:25:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac01b810-e9c6-347d-b467-da644e1a41b0 | -12.61264 | -38.04955 | 2026-01-01 04:25:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| beec87a7-4c31-3bfa-b5ac-31e19ad8cd8b | -5.93239 | -43.40166 | 2026-01-01 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 566c499b-3729-36b1-81d4-5e5a6db79926 | -12.61326 | -38.04914 | 2026-01-01 04:25:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| f02243aa-33dd-35d0-a749-929c2476f6f6 | -8.60846 | -49.16766 | 2026-01-01 04:25:00 | NPP-375D | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da717561-35c0-3cfe-96c3-c839a6a4d831 | -12.32476 | -47.89796 | 2026-01-01 04:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63b47423-f6cb-31dc-a066-33ef41d104c3 | -5.63239 | -46.31122 | 2026-01-01 04:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c12dd6b-e77d-385d-bb05-db44a1c4a060 | -5.71335 | -49.09974 | 2026-01-01 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4e2dac0-6d00-3b5d-8409-bfede099c233 | -13.26509 | -41.32336 | 2026-01-01 04:25:00 | NPP-375D | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf5d8814-29d7-3a7b-8f62-b7235354a00e | -0.08847 | -51.28076 | 2026-01-01 04:25:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73baf875-d725-34c4-80e7-dcb36ddda70c | -9.57462 | -44.60096 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 12f70ba8-bd45-3a59-a765-91b30e61a56d | -9.58187 | -44.59846 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af920757-27de-3363-a863-3bf2ccdde802 | -1.36355 | -46.05967 | 2026-01-01 04:25:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bc747b9c-abf6-3ac2-b623-61f07e61dd81 | -13.17731 | -39.89239 | 2026-01-01 04:25:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0cf89cc5-b217-376a-8667-fdc59258ce76 | -5.70946 | -49.09908 | 2026-01-01 04:25:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 53f36237-9c3f-3b85-a582-739ce81c2fd7 | -11.40359 | -54.99294 | 2026-01-01 04:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b615498c-138e-3370-b577-2404d3a46a88 | -9.57852 | -44.59794 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fa50c9c-6da1-3d0e-add8-0ac31821ec5e | -9.57182 | -44.59687 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 64b9311b-cad6-3c38-b0cb-9ae4cc13b9c3 | -11.06856 | -49.57542 | 2026-01-01 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3351712e-2430-3edc-a54b-d6f91d05ff63 | -7.57039 | -49.39515 | 2026-01-01 04:25:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4b07f696-5585-3747-bcdb-acad43c902ca | -1.12022 | -47.74561 | 2026-01-01 04:25:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d41f64c7-c6db-3a20-aa3f-c142d6b50106 | -9.57797 | -44.60149 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be590dcd-5fc3-388f-9428-bd413c26fff7 | -5.92958 | -43.39754 | 2026-01-01 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b6022a22-0e82-3002-9fc7-5930979a3e62 | -10.45087 | -48.72227 | 2026-01-01 04:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0894215c-2129-3a9d-8552-1430f6e15951 | -5.59223 | -46.36478 | 2026-01-01 04:25:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d01478cf-a44c-31e8-8b77-938c196c389f | -6.24567 | -44.65499 | 2026-01-01 04:25:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d5f1fb4-9600-34af-a1ba-0b91d4fbfdd1 | -7.14436 | -45.26022 | 2026-01-01 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 864c24f1-b2cb-338d-8432-f60f15921dc2 | -0.92074 | -46.90297 | 2026-01-01 04:25:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8c4a7df-09b7-3bd5-947d-1f29341d9cad | -8.11631 | -48.06455 | 2026-01-01 04:25:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7760b0e6-c694-3e3e-9568-d4dc80b8394a | -5.93295 | -43.39808 | 2026-01-01 04:25:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8ef7f1de-836d-3a77-8155-51dc7db7b685 | -6.29387 | -46.99673 | 2026-01-01 04:25:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a72c6a15-b5e0-3fd4-a11d-90b29e19e194 | -0.96475 | -46.78893 | 2026-01-01 04:25:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4900e604-3f52-3677-a91e-c0d25779cc0f | -8.11274 | -48.06395 | 2026-01-01 04:25:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47faf1ac-f2b3-3c09-9221-0d3f1466bddb | -11.40299 | -54.99611 | 2026-01-01 04:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee818921-327b-332c-aff1-767e11eaaf57 | -8.11748 | -47.98977 | 2026-01-01 04:25:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d7abf49-6f40-31fe-845f-748a27c10c84 | -11.06485 | -49.57476 | 2026-01-01 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c300ec08-645d-3a32-9dea-375220761fd9 | -9.57407 | -44.6045 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7fb662d8-8bc6-3dee-8963-a6c914af1d55 | -10.93945 | -49.43036 | 2026-01-01 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bb49c3c3-1ebc-39bb-945d-4ed637c94452 | -0.962 | -46.78244 | 2026-01-01 04:25:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fb6df6d-f80c-381e-bedf-0d17e9108fd4 | -9.58522 | -44.59899 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4e14cd1-97c8-385f-99af-6cac9ac89857 | -0.9244 | -46.90355 | 2026-01-01 04:25:00 | NPP-375D | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 766dae61-d104-3199-87e7-6042ced68d25 | -6.42195 | -39.64168 | 2026-01-01 04:25:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1ac1dd6a-91fd-3240-8337-cbed6332a3d4 | -11.40881 | -54.99403 | 2026-01-01 04:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7baf1d6f-c28f-3631-b419-65d795b02ed6 | -9.57127 | -44.60042 | 2026-01-01 04:25:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4b64beea-a319-376f-a924-90b2b363c3d3 | -0.96176 | -46.78417 | 2026-01-01 04:25:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f62fd64-a439-3684-8f94-ac9f8e136f46 | -5.72072 | -45.04158 | 2026-01-01 04:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README5.md)
