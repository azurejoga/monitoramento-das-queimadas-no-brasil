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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98d1ea70-e46c-3209-b4f8-a18599e8f9a9 | -10.59756 | -49.46701 | 2025-06-25 04:08:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e47124f-2c85-32e1-bbf9-52848a378801 | -13.64154 | -43.79373 | 2025-06-25 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3ae125b-0ee6-3455-800b-4f6fe4944756 | -11.13434 | -47.00861 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4677982-5eb8-36c4-be2d-cb2a63723886 | -12.50819 | -47.43402 | 2025-06-25 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66adcb7c-67f7-3db7-a24e-701eca9388a2 | -11.58249 | -44.63939 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bde68a0-a6ca-30de-9cef-a4cdeead50bb | -15.92279 | -42.57572 | 2025-06-25 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b70c41ac-0b7b-3131-bdac-b3ddd56dafb6 | -10.38659 | -43.34217 | 2025-06-25 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69d3469a-68a3-3d74-9ce4-a73f76e3ff5c | -15.56913 | -47.85719 | 2025-06-25 04:08:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9f407ae-fe75-31fe-917c-d16ad194da00 | -10.73549 | -47.60921 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cec9c72e-7c9e-3e5f-86e1-b0ca9e5f9331 | -13.64429 | -43.79783 | 2025-06-25 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a54c539-271d-31cb-b057-4d983f7c9bba | -8.87023 | -47.27345 | 2025-06-25 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52dedfc8-d610-331a-82ce-6ece1405ed64 | -14.38274 | -50.329 | 2025-06-25 04:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 960eea6a-a8f6-3a61-8a5f-5175f7257c54 | -8.98411 | -49.87044 | 2025-06-25 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 674fc226-a27e-3a27-b2e7-6f541ecd0cfe | -14.71733 | -48.41576 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8d0c00a3-75a3-3011-b936-b0a9d3db9875 | -8.66918 | -51.46148 | 2025-06-25 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7e8d86d-e39c-3258-8f75-1a9733d7add4 | -9.50708 | -56.10499 | 2025-06-25 04:08:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19ee2eca-49f8-3c07-b90f-b059b365a77c | -14.38005 | -50.32647 | 2025-06-25 04:08:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b9a9856-1bcc-37bc-996b-e5f5ef5f4ca3 | -11.93724 | -47.83718 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d32e8472-3af6-35a8-bffa-5f05cc7153ed | -11.6143 | -46.4966 | 2025-06-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3414d63f-db0a-3db8-af4c-d7573ee5c74e | -9.51533 | -45.44221 | 2025-06-25 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65868d85-b222-321b-92fa-c836b768c4aa | -12.79936 | -48.73713 | 2025-06-25 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 48a4be41-12dd-3b44-b276-7e3d8a1ad69d | -16.60899 | -44.25536 | 2025-06-25 04:08:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b39fe61-95d2-341f-b27c-e9f0563166ec | -16.39295 | -41.16889 | 2025-06-25 04:08:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 07c2f6d4-4230-3735-be3a-1b72ce9c1e74 | -10.82757 | -54.04765 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4be53ae7-2b92-3899-9d0e-e1355b9f2d2c | -11.13856 | -53.91787 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff05323f-53f5-3da2-bb2a-04acc318d04b | -15.39545 | -43.20496 | 2025-06-25 04:08:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9dab9f39-5248-3249-b585-e59e4249d5d6 | -10.83361 | -54.04914 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a863094-96b3-36a4-a828-40d0d7d4e1ab | -9.8106 | -48.38797 | 2025-06-25 04:08:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97407d84-bde7-33fc-9d3a-0e8dc10dfe07 | -11.80247 | -47.55003 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| db0883af-8f97-3f96-9651-e7194e6bbd56 | -9.99844 | -48.13203 | 2025-06-25 04:08:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fb762d6b-35d5-3787-885c-07d67c2ea626 | -8.57993 | -48.21534 | 2025-06-25 04:08:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f48c2b1-65ff-3998-b9a1-a85c9c54197b | -14.15703 | -50.42855 | 2025-06-25 04:08:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f90f17fd-d6b8-3919-be18-467e06893db7 | -11.79852 | -47.54944 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bbeeeaa-6fde-3ccf-b826-6778cc2e4acf | -12.75674 | -44.411 | 2025-06-25 04:08:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2757a4d-df33-3d13-8269-f20bc61b61c9 | -11.10958 | -46.89989 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d1093a57-0778-3349-8b46-3109c9a5d0d8 | -10.82895 | -54.00805 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85e572a2-41f9-3c7c-8cca-02aa5b37bd02 | -9.568 | -49.10307 | 2025-06-25 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fec51c2-df8f-3004-b24e-83fca7072c66 | -10.83452 | -54.04445 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d26de78-2605-3c78-aaab-9371c82486c1 | -10.86307 | -54.3194 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6dbff6d1-a6bd-3d79-8bef-97567143df25 | -10.5176 | -47.58144 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40c83795-3e3b-3090-9247-aad48793f627 | -11.9423 | -48.42368 | 2025-06-25 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 668299d4-e21a-3fbd-8f66-da0fa47a7394 | -11.95059 | -47.02501 | 2025-06-25 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a080ecf-1090-3d6e-b705-6c10181c1705 | -12.51206 | -47.43472 | 2025-06-25 04:08:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d40031f5-844d-3713-9bdb-03711a32c8e4 | -8.4733 | -50.27747 | 2025-06-25 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5d7ad511-58dd-3dfa-af57-56b25cba1701 | -16.43388 | -44.52106 | 2025-06-25 04:08:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3f4ff07-0ea1-30ec-847f-bebdbf382ba1 | -13.04494 | -48.82579 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04e98cc0-2b01-3c8f-88ae-2286f5ab1fd2 | -11.57846 | -44.64257 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 390e70de-fa67-3ded-9bf7-b629e1fc8f38 | -10.82291 | -54.04038 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 482980e3-697d-3ae7-b604-65574250ebdc | -15.40319 | -43.1989 | 2025-06-25 04:08:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce691923-6e92-3882-8a44-26e168b3d606 | -11.94162 | -48.4275 | 2025-06-25 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 492f4317-86f1-3374-b841-871a3a26c18a | -15.59932 | -42.00139 | 2025-06-25 04:08:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f40f8cc3-e0ca-3d47-9ccb-be747e662f91 | -16.14802 | -45.94121 | 2025-06-25 04:08:00 | NOAA-20 | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 404ef67b-d1bd-35d5-91cd-8af0e9d4ac31 | -10.73419 | -47.60957 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3edb67a2-aaab-3822-91e3-5aca93d6d4ec | -16.43056 | -44.52049 | 2025-06-25 04:08:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00d707c9-7d4d-3d97-8105-a43320131dfd | -16.42724 | -44.51991 | 2025-06-25 04:08:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f80ac631-a29c-3fb5-a16f-965770c7daa8 | -12.02858 | -47.77377 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03577c5b-087c-3376-bbf5-dd317fa29d4f | -11.58467 | -44.64748 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41505efa-db2f-30ef-8a53-d7a81a4a4895 | -11.58725 | -47.608 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82320b7d-c2a4-3dfa-b041-6094e74ecb02 | -8.71708 | -47.85523 | 2025-06-25 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efc3e0e6-4d60-35e8-8946-9deea772f9ca | -9.51172 | -45.44163 | 2025-06-25 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c867e755-b129-32f7-a067-db6d962f9977 | -10.84441 | -42.2333 | 2025-06-25 04:08:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cb60357c-9a89-324b-aa78-f61bad46475a | -11.10676 | -44.5231 | 2025-06-25 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c53769f-f3c7-3be7-a2cb-6598031bd1e5 | -13.0533 | -48.82729 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 766a028d-206f-312a-820d-f4fa72fed2a3 | -10.44497 | -47.95729 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 04f6deac-e061-39ad-a864-be704eebd22e | -10.45453 | -47.95108 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 26040d3e-82d7-3604-bca7-7a2078781232 | -11.93662 | -47.84076 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0ef18bfd-8f09-3e12-a488-1604b39b45a2 | -11.57908 | -44.63881 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ada56287-2b4a-3335-af22-c72f993fc138 | -10.5142 | -47.57709 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2db2f495-ab6b-3258-917e-1bbe3a68465e | -9.57089 | -49.11315 | 2025-06-25 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 040f189c-c7f5-3433-8900-835345f640b6 | -13.07415 | -48.83138 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 369de624-e8b0-39ab-8e52-123db9604448 | -12.79519 | -48.73636 | 2025-06-25 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 98062a85-ed31-3649-9426-8dcc9cf1d16b | -8.87086 | -47.26985 | 2025-06-25 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 053dcd91-270d-3720-bad6-44e1616c6b95 | -9.57252 | -49.10389 | 2025-06-25 04:08:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76d629ad-222f-3b07-873e-23712a0c89ec | -11.57442 | -44.64575 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a78703e8-f61e-31c7-a435-6ac1a3c28a80 | -15.07935 | -48.94482 | 2025-06-25 04:08:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f8dd83ac-c0f6-3a97-9138-7f292514fac1 | -11.57784 | -44.64632 | 2025-06-25 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6ec54da-692b-3944-9abf-850d377d3ed1 | -10.38602 | -43.34571 | 2025-06-25 04:08:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e25820da-b3d2-362c-97f3-df46928baee8 | -13.60918 | -43.97478 | 2025-06-25 04:08:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab73d738-246c-3115-859b-254a41c1a8a8 | -13.57991 | -41.79223 | 2025-06-25 04:08:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 04e36a1d-081c-3955-9949-500bab6f362d | -11.61352 | -46.50113 | 2025-06-25 04:08:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8686efa6-e10e-31ea-b82e-1c71e5b0349e | -13.04422 | -48.82972 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b1fbdb44-6797-3ea6-b46c-0066a325f819 | -10.86925 | -54.32069 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87a50f5e-3d29-3c66-add2-4db413f5d62f | -12.80005 | -48.73323 | 2025-06-25 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 096b9e7b-8f30-3017-b15c-d537badd23e0 | -11.93884 | -48.41908 | 2025-06-25 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8cd28ab-5ec2-3590-85d8-aec636f242bb | -14.80724 | -48.29309 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f12ff45-e2ff-3429-82c0-c7e6d8bbfdc8 | -10.44215 | -47.94897 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2c8fc29d-15d4-33e6-9752-160b6954b2ce | -10.82199 | -54.04492 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a534bc4d-42ef-3d2e-a2c2-590839ec3231 | -10.82241 | -54.04165 | 2025-06-25 04:08:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d143db91-f70b-3695-a218-cedc12a42a11 | -13.7582 | -44.12473 | 2025-06-25 04:08:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f9d2029-4afa-32db-b071-ca44898f4c0a | -13.04841 | -48.83047 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ef0e3d0-6a02-3f7a-94e6-8305825bdd2f | -13.0435 | -48.83367 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 51d5dd27-08ac-37a2-9725-a97fb603ada9 | -14.34826 | -40.90709 | 2025-06-25 04:08:00 | NOAA-20 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| dd42ae57-e6b7-3039-97a8-e336562203c6 | -11.09189 | -46.64072 | 2025-06-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 38af5d90-620b-3d41-8917-a30350897020 | -14.72043 | -48.41293 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fef1566c-1e3b-3e80-9dda-abc8f52ff1f2 | -14.7213 | -48.41643 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cddd9eb6-5ce8-3d90-80ba-2934d09b1bae | -15.83145 | -41.82803 | 2025-06-25 04:08:00 | NOAA-20 | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7fe0386b-b23a-3848-b158-066d780931bb | -9.81798 | -41.76121 | 2025-06-25 04:08:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd8c7aed-34bd-33a4-be8a-1fef262891bc | -9.56638 | -49.11231 | 2025-06-25 04:08:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8d0ba28e-4af9-3332-85ba-298d0ab31cfb | -13.04004 | -48.82898 | 2025-06-25 04:08:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1174a059-0acd-3d1e-8782-44a78548cab6 | -11.56925 | -47.43061 | 2025-06-25 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README12.md)
