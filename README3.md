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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42f22518-bb53-3735-a265-60aed8ecdf9d | -11.3678 | -45.9493 | 2025-10-24 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 39b29f0b-bc0e-39fe-85c5-d240cf6a3445 | -11.3682 | -45.9265 | 2025-10-24 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 08038d06-ce40-3978-9f7c-596fd8f7b874 | -8.6523 | -44.8001 | 2025-10-24 02:50:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 48ac6b53-5299-3e69-91f2-12ca55f4fb54 | -5.4551 | -45.4214 | 2025-10-24 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| d548b546-15d3-3fbf-b22a-4c12ddb52898 | -3.1416 | -50.6236 | 2025-10-24 03:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7fe4488c-407e-3a41-9be9-105b4b8f33f4 | -11.3678 | -45.9493 | 2025-10-24 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 21e6557b-f67c-3f34-9033-a428d3645306 | -15.5801 | -47.7143 | 2025-10-24 03:00:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 946084ea-c0b8-3af9-8ea3-ecaa92bb9def | -2.8149 | -49.1354 | 2025-10-24 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ac302d26-31e3-3e06-ad1e-6b7227a35152 | -7.5497 | -47.3766 | 2025-10-24 03:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5236debd-c14e-3ff5-9ca0-22e481e1781f | -9.6061 | -46.9099 | 2025-10-24 03:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 71163eb8-384d-32bd-84bf-9e1906a9748d | -20.13118 | -41.80559 | 2025-10-24 03:02:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 0875969b-0a80-34ff-9e2b-be256bcf25fc | -20.13286 | -41.79877 | 2025-10-24 03:02:00 | NOAA-20 | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 232064ea-586f-3fd4-9569-01aaedf30d30 | -5.4551 | -45.4214 | 2025-10-24 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 896c904d-6a0f-3b44-8d3d-645fc085f929 | -6.9293 | -44.0048 | 2025-10-24 03:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 74f1c207-118f-3d9b-b4b5-0190a1a9f8bb | -15.5801 | -47.7143 | 2025-10-24 03:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ee35ca39-4bdd-3a3f-82b7-49511d6d72d5 | -9.6061 | -46.9099 | 2025-10-24 03:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 9ba6229b-4433-30bf-a95c-c68ba642494c | -2.8149 | -49.1354 | 2025-10-24 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| c8e8b498-0790-32cc-bb96-aba92170606a | -3.1416 | -50.6236 | 2025-10-24 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bf1e7af7-02e1-3d1a-8849-23d5f51cc108 | -6.9291 | -44.028 | 2025-10-24 03:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| c5e73d65-7177-39f6-abff-d15ebe15a86e | -5.4551 | -45.4214 | 2025-10-24 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 83136b8b-9fed-3c94-b7e8-14678a90aa01 | -15.5801 | -47.7143 | 2025-10-24 03:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e82d2d29-329a-33ab-bf9f-a2257fc619f4 | -9.6061 | -46.9099 | 2025-10-24 03:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 123.7 |
| dfeea7e7-5ac9-3d66-a69e-98cd8e20b6ec | -3.1416 | -50.6236 | 2025-10-24 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| bccfd971-4acf-3bed-b424-90458400ddcd | -11.3678 | -45.9493 | 2025-10-24 03:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 7c17dfb0-f07d-3835-aad9-794d53be6c2a | -15.5605 | -47.7178 | 2025-10-24 03:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 1921fde8-8564-34c5-802e-55665aed9092 | -15.561 | -47.6951 | 2025-10-24 03:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 4ca39125-f521-3e38-9e72-d101d3e06ec9 | -9.6061 | -46.9099 | 2025-10-24 03:30:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 24f152ae-56b1-31b9-ae8b-ce1d2a3f274b | -15.5801 | -47.7143 | 2025-10-24 03:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 200.3 |
| dfb2b62b-d2fa-3d71-a25a-635a0d10b93d | -3.1416 | -50.6236 | 2025-10-24 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 69ed2aca-d36a-356b-8523-058d91117db0 | -12.8136 | -50.9576 | 2025-10-24 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 05efc81b-a7ef-34f1-9e76-c4400a845286 | -15.5806 | -47.6916 | 2025-10-24 03:30:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 961d90f9-2790-30fa-8a66-073a5c2de9fc | -5.4551 | -45.4214 | 2025-10-24 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 80265164-e218-3372-a73e-a0fb3d8b0e4a | -9.6058 | -46.9322 | 2025-10-24 03:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 47bdbf2a-f4a4-378e-9d1a-afd34de90ea8 | -9.6061 | -46.9099 | 2025-10-24 03:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 56bcd91a-b518-3180-ac6e-4f26dab6c7f0 | -3.1416 | -50.6236 | 2025-10-24 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 52951a75-b868-3a2c-b12b-caec3a3ad68d | -8.32613 | -46.25685 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 46d2d1f7-b2fa-3934-942b-fbf30b71e88e | -6.97765 | -45.28764 | 2025-10-24 03:47:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91d473e5-0eda-34b1-8f8f-fa35e80b9548 | -5.40644 | -46.4139 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 624bf62b-a951-35ef-bd61-e1fcb795ff73 | -8.65582 | -44.7931 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3a64a87f-1bd2-3f0e-a3a3-5b12ea169d14 | -6.53808 | -41.68929 | 2025-10-24 03:47:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 305fe19f-cb11-327f-8e93-9e3a697b604b | -6.30251 | -41.87836 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 97a2f636-72eb-3893-b437-ad7726e6dcc2 | -7.84792 | -49.65111 | 2025-10-24 03:47:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aae66e9e-917a-31eb-b97c-43605839ca3a | -8.32083 | -46.25599 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 728c5ff1-ca9e-39df-ae64-93144f89f10e | -6.1309 | -41.72964 | 2025-10-24 03:47:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 2558049c-9814-3831-97a9-3646e45a8226 | -7.83503 | -45.59381 | 2025-10-24 03:47:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7bcc161f-5542-38d1-ba93-fd4c65b8faa3 | -5.41093 | -46.41053 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cadb4514-e6f0-35c8-ac6d-2c48370b32d6 | -6.92494 | -44.01966 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 33d6396c-82ae-325f-9df2-08f27896351c | -5.56842 | -46.52282 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 14cede91-585a-3f20-925c-d4c877b24f87 | -6.32112 | -39.71795 | 2025-10-24 03:47:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 279d7ed7-729f-3aa1-82a0-af294a9bc2c7 | -8.29767 | -42.29858 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4487b227-9c78-3c2a-a48c-0131e72c07a2 | -2.26305 | -47.84195 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2425977a-e25b-3df6-aa04-3a9b1010a2ba | -8.64642 | -44.79079 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 355a7ecc-a5ab-3beb-92cb-74528e54cb5e | -7.39922 | -43.91693 | 2025-10-24 03:47:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9716dbc0-4bff-3a7f-85b5-f1a2107a0bde | -6.08963 | -46.23501 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1f79dd52-6a03-38bf-85f6-f6897cadf38b | -6.30069 | -41.8884 | 2025-10-24 03:47:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 280f1405-59b1-3b77-b19b-ccaaf4b6d882 | -6.92439 | -44.01336 | 2025-10-24 03:47:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0460afff-c33c-31ec-9044-516c2d48fe4c | -7.62981 | -41.8495 | 2025-10-24 03:47:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 80a30c32-34a6-39d2-8598-e8c543d2773f | -7.8224 | -45.37993 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3f828dfc-48a5-3cd9-a3c6-094255bc33e4 | -6.79229 | -46.46971 | 2025-10-24 03:47:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec6c11c0-31dd-3b9d-b3b1-2e5cc903ec63 | -7.98164 | -47.24108 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d3fb770-a7c4-335e-9889-d03e05bff090 | -5.40532 | -46.40964 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40619b93-3f9d-3dbb-ab36-3bcd9283dedc | -6.27809 | -47.01706 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e86a875c-4f43-37a6-8d91-12a7faa953c5 | -5.4127 | -46.41102 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f201779-16d9-3969-bcc9-75af02972cc6 | -2.26337 | -47.84619 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 3673ff67-73da-351f-8399-cb4668d44702 | -7.62925 | -42.19524 | 2025-10-24 03:47:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 30db26f2-50ed-368a-b378-59abf793e7a1 | -6.73032 | -42.681 | 2025-10-24 03:47:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| a370d7c0-4d96-3c47-a4a3-22223700a65e | -8.45091 | -36.38369 | 2025-10-24 03:47:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0a1b754c-927a-3e56-8a8e-c959f0b0f31b | -4.84379 | -47.80302 | 2025-10-24 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f6461c3-d0bc-3054-8f1c-7b5f6004d9e2 | -2.86785 | -41.74729 | 2025-10-24 03:47:00 | NOAA-21 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4ebfabde-7ece-308f-89e0-383554635305 | -5.60653 | -48.65871 | 2025-10-24 03:47:00 | NOAA-21 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99bed6c6-2f5e-3600-ac68-b8ee2b0367db | -7.05873 | -43.1675 | 2025-10-24 03:47:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 71d4ff67-8262-30d4-bfdf-16b341a2dddd | -8.66148 | -44.78887 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24534646-8baa-3f49-9636-6af49704b130 | -5.56776 | -46.52658 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab37ce06-8648-3906-ac64-ddd8316f37f4 | -8.32203 | -46.24934 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0c308d06-bf34-356a-9197-0b3e245d8478 | -5.65627 | -45.95464 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7475c7c1-b1b6-3f95-a844-59e991be8f7e | -5.48198 | -48.86646 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5028b1ee-76ba-36d7-9e16-54e1f76074d7 | -6.73669 | -44.14943 | 2025-10-24 03:47:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb1e6d61-1501-38db-b931-eed21747ef60 | -7.83303 | -45.3784 | 2025-10-24 03:47:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bb00b6f-a5fa-3a65-87de-599af7f54619 | -2.26777 | -47.85354 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a34a28a9-9232-3c50-842e-52e1d5788afd | -7.62584 | -41.84885 | 2025-10-24 03:47:00 | NOAA-21 | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| afcb2c11-7fb1-368c-93c9-263bda608724 | -8.32143 | -46.25268 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| f6bc694f-9abf-3f20-99cc-6f3f820ccca2 | -5.59906 | -45.19204 | 2025-10-24 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dbc6b3f2-e9b7-3d93-a826-b2cbb367ae01 | -8.10961 | -47.04918 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3ea34bce-fd97-3fe0-a3b0-19e077c23975 | -8.32733 | -46.25019 | 2025-10-24 03:47:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a8f58fd6-6aa1-3864-80aa-ba54fbe4751e | -8.50999 | -44.20671 | 2025-10-24 03:47:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d5acf4b-9264-3273-bf83-c62c06ce21b9 | -6.92121 | -47.1693 | 2025-10-24 03:47:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd2e8e4f-d75c-3b58-b486-9b6831616941 | -2.26219 | -47.8472 | 2025-10-24 03:47:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e9c3ecea-cf26-3577-b303-2ed8de9117bf | -6.09081 | -46.23166 | 2025-10-24 03:47:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7e33fbd7-571f-3661-89c9-5aac20c65d2e | -6.89398 | -38.27257 | 2025-10-24 03:47:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 295fd69b-35d0-30cd-b8da-2743614d3153 | -8.17694 | -47.7674 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ead44034-1f59-30e3-a610-01ad85ccffd1 | -8.73569 | -40.59528 | 2025-10-24 03:47:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f910c9d0-f713-3cf9-ab6f-bcbce8c28519 | -7.9824 | -47.23701 | 2025-10-24 03:47:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9ab33299-cdf4-3093-8fc1-a19346ca0222 | -7.30279 | -46.94822 | 2025-10-24 03:47:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2161820-e288-3f50-bc46-6b1b5187ff39 | -2.44464 | -47.1584 | 2025-10-24 03:47:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 997f4065-149f-32a4-8b41-e41afc57ca78 | -8.12925 | -41.08157 | 2025-10-24 03:47:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cc6d77b8-f3f3-311b-b8a4-8b685fdea586 | -8.05777 | -46.48499 | 2025-10-24 03:47:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4d2067c7-b956-3a05-a12d-16c7c41d9ea4 | -6.84096 | -41.55883 | 2025-10-24 03:47:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6eb9d7b0-8410-3617-8d86-cb08c6405cc0 | -5.64943 | -46.57563 | 2025-10-24 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29ec1311-4c6c-35b8-b41b-1d9453feed07 | -8.56931 | -44.86271 | 2025-10-24 03:47:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f242e3b-1fb1-3c13-bb27-2828ea4db934 | -6.72554 | -42.14712 | 2025-10-24 03:47:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README4.md)
