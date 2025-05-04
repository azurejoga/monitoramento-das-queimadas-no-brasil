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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72543502-34a9-3d3b-bfb1-e72665184274 | -13.5285 | -52.9669 | 2025-05-04 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| e49cdd73-6438-3273-9858-46ad63d6035e | -6.5631 | -51.1126 | 2025-05-04 00:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| bbc8169e-96d6-3660-b131-5e9fe4f16e69 | -11.3921 | -52.952702 | 2025-05-04 00:50:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa9c532f-3adb-39b2-a509-7144b08b7318 | -13.7203 | -45.2052 | 2025-05-04 00:50:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6034ec12-10a0-3e36-bd43-bde3f0d09f31 | -11.3903 | -52.9445 | 2025-05-04 00:50:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bcd6856-87ab-3e24-8abc-2eb0b07cdcce | -11.4019 | -52.9506 | 2025-05-04 00:50:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77653ba6-86c2-3c69-be25-0cff654194d8 | -11.4001 | -52.942402 | 2025-05-04 00:50:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77ab08ad-6a7a-3453-b4b7-3557f7d1543a | -13.718 | -45.195702 | 2025-05-04 00:50:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b11dbf70-1f14-324d-ac92-40e270a2ea6d | -11.39609 | -52.93848 | 2025-05-04 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7d40e939-0478-3298-90cc-c6ba9afd2d6f | -13.05262 | -53.70938 | 2025-05-04 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 5853e19f-3eb0-33af-ba72-ddd09e45a6ff | -13.05423 | -53.72243 | 2025-05-04 00:52:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ff96b7e2-d3f5-38cf-b73b-831bced7259d | -11.3975 | -52.94951 | 2025-05-04 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.9 |
| a7ed23db-00ac-3ef9-be18-c83623a50387 | -11.38774 | -52.95081 | 2025-05-04 00:52:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 24a41531-9842-31e6-88ae-da6acff0df8b | -13.71363 | -45.2073 | 2025-05-04 00:52:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 6d93bf68-aa42-37a2-84af-3b6ae22da771 | -9.61618 | -37.0424 | 2025-05-04 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6c8f6dad-d156-3d58-863e-254084fc410c | -9.60378 | -37.04342 | 2025-05-04 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b8dabcfd-1118-3f68-9e43-150cc4bc7f4b | -9.6092 | -37.04078 | 2025-05-04 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d1997f36-3b6e-37f5-811e-0c2056ace710 | -9.61075 | -37.04509 | 2025-05-04 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 94a23f8e-d5be-3725-879a-e411d3edff92 | -9.61774 | -37.04668 | 2025-05-04 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fd357123-de4c-3105-93ef-382a3d9849de | -9.61908 | -37.03989 | 2025-05-04 02:51:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 77dc4cf6-8cbd-3dcf-9285-4e03d8358408 | -7.8289 | -40.90566 | 2025-05-04 03:17:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| ce27826d-8051-36b9-8d97-802d0a4bda92 | -9.75247 | -37.09638 | 2025-05-04 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4981e417-fbbf-3fd2-a503-b33dff38c42a | -9.70411 | -37.0663 | 2025-05-04 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1b25da36-7e8e-330f-a41a-65f4f2627ca3 | -5.17714 | -35.53382 | 2025-05-04 03:17:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| ebe48d3e-1a2d-3285-895a-8f8b0be64a8a | -7.83228 | -40.90408 | 2025-05-04 03:17:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b28921b9-f499-3eaa-9850-f27c0b7ae2f2 | -9.70442 | -37.06379 | 2025-05-04 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bb500dbc-ef8f-3465-8e48-0fd4dc1b667b | -7.83136 | -40.90911 | 2025-05-04 03:17:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 304c6fb2-414b-35ef-88f6-00c65203c9e1 | -9.75339 | -37.09131 | 2025-05-04 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b221cee7-434e-356d-ad76-ee94282acac2 | -9.70505 | -37.0612 | 2025-05-04 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 433780db-3b19-3e00-aa0c-ab7c833aa46c | -8.07336 | -34.9776 | 2025-05-04 03:17:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8db4501-33d0-399f-8672-331bccd7e349 | -7.82602 | -40.90285 | 2025-05-04 03:17:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 67da723b-e4af-32d3-b9e4-b64f278d22cf | -7.8251 | -40.90788 | 2025-05-04 03:17:00 | NPP-375D | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 246856c1-7101-36ac-add3-e23fc23a91c2 | -9.69969 | -37.06292 | 2025-05-04 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c02876d-f107-31e1-b76e-a18183fc9b72 | -8.42031 | -35.65211 | 2025-05-04 03:17:00 | NPP-375D | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 50a2532c-c593-3c33-a6c0-ac0e9fed2242 | -9.69937 | -37.06545 | 2025-05-04 03:17:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a91f3b19-6030-3996-b71d-8aa48fd442a5 | -7.16035 | -35.23428 | 2025-05-04 03:17:00 | NPP-375D | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a43dbb1a-1669-3d9f-be10-ecf3a0828aee | -15.4614 | -42.91011 | 2025-05-04 03:19:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7632198d-6a8e-31b5-a544-57f5d95f5179 | -13.70393 | -45.20392 | 2025-05-04 03:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a7bc44c-f8d3-3105-9eed-889b64c2486e | -15.45851 | -42.91045 | 2025-05-04 03:19:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a2c8a67-fb32-375c-ada1-bafa22e58331 | -13.71179 | -45.20399 | 2025-05-04 03:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc375852-f894-3a3e-ae22-e63c04c55670 | -15.45956 | -42.90564 | 2025-05-04 03:19:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b9370c3-ae45-3581-925b-9a592fca5a60 | -15.60355 | -39.62855 | 2025-05-04 03:19:00 | NPP-375D | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| aed93995-b350-34f6-a7e2-2009428454e1 | -13.70547 | -45.19682 | 2025-05-04 03:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b7248e6-87d3-33c1-a57b-64596d259eea | -15.46242 | -42.90526 | 2025-05-04 03:19:00 | NPP-375D | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f8596e3-739f-3e57-afff-3900bdb5b026 | -15.59858 | -39.6271 | 2025-05-04 03:19:00 | NPP-375D | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2d2de3db-cf6e-3868-9071-0224f4afd96a | -15.59798 | -39.63018 | 2025-05-04 03:19:00 | NPP-375D | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f2367c12-6e6d-3bfb-b07e-2f3432d732b5 | -13.70459 | -45.2022 | 2025-05-04 03:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42d256e5-0183-3f76-ac06-d0a86025e5e6 | -22.67688 | -42.85553 | 2025-05-04 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a89bb772-70e6-3640-90b7-36fb165aab00 | -22.67606 | -42.8592 | 2025-05-04 03:21:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2fdfebd8-e421-39d1-b48a-b109c444f657 | -9.41745 | -37.06539 | 2025-05-04 03:40:00 | NOAA-20 | DOIS RIACHOS | ALAGOAS | Brasil | 2702504 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa043392-15f8-31eb-bfff-3b2990ac0ef1 | -9.52295 | -37.06442 | 2025-05-04 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 449e10b1-496b-3e4c-b49d-bff020067a6b | -9.70261 | -37.06364 | 2025-05-04 03:40:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 233cc1a6-be3e-38c6-9d5e-21123ae12b4a | -9.9775 | -37.1676 | 2025-05-04 03:40:00 | NOAA-20 | GARARU | SERGIPE | Brasil | 2802403 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 392a9185-c50c-39d8-9236-0937efae283e | -9.61789 | -37.04228 | 2025-05-04 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 53a44e04-ed21-338e-a5bc-18d011b61bb9 | -4.93771 | -38.00054 | 2025-05-04 03:40:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3797e202-b7a5-38bf-b41d-f6395f23887f | -9.61454 | -37.04173 | 2025-05-04 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6709e669-44cb-373e-a9f1-007063580276 | -9.60783 | -37.04061 | 2025-05-04 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7d941b63-be56-3316-a34c-03594a3bafcf | -7.47652 | -34.844 | 2025-05-04 03:40:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 10e23272-02fc-3cd1-b7ed-8b3d99eb95a4 | -9.75469 | -37.09405 | 2025-05-04 03:40:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2049a825-ace7-315a-991c-513cb47e3318 | -5.17419 | -35.53102 | 2025-05-04 03:40:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 15e60719-b031-3e32-93bf-40a5f6ad98fd | -8.42243 | -35.65274 | 2025-05-04 03:40:00 | NOAA-20 | BARRA DE GUABIRABA | PERNAMBUCO | Brasil | 2601300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a53185e-762b-3ae0-9b30-27558670d55c | -5.17752 | -35.53155 | 2025-05-04 03:40:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4c581146-48cb-3291-b4eb-bd6a398786f1 | -9.61118 | -37.04117 | 2025-05-04 03:40:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 10a9c46f-544e-39ea-8fad-84f143726545 | -8.07353 | -34.97739 | 2025-05-04 03:40:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 87212f58-6877-3ed4-86aa-6e266374ec7e | -9.69474 | -37.06973 | 2025-05-04 03:40:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e2cc9a7-1b95-3dc7-9504-9041b83cce05 | -7.16044 | -35.23486 | 2025-05-04 03:40:00 | NOAA-20 | SOBRADO | PARAÍBA | Brasil | 2515971 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b67a39a0-b437-3679-948c-decdb3213a8e | -6.79601 | -35.67052 | 2025-05-04 03:40:00 | NOAA-20 | SOLÂNEA | PARAÍBA | Brasil | 2516003 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| aaffa5c0-4ff9-3ee5-bdcd-ee2aa90b1cba | -5.22504 | -36.1461 | 2025-05-04 03:40:00 | NOAA-20 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5dcf5b2-5b7c-3bef-babd-4c35a46c6c77 | -5.16896 | -45.10808 | 2025-05-04 03:40:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e4b9fe3-8500-33d5-8f09-4e425e0ec25f | -9.41932 | -37.06581 | 2025-05-04 03:40:00 | NOAA-20 | DOIS RIACHOS | ALAGOAS | Brasil | 2702504 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81e4bea7-5948-3369-a80a-06146bf55604 | -9.86795 | -37.10925 | 2025-05-04 03:40:00 | NOAA-20 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cdb9bc98-b688-35f1-bc1b-9419b2ebbe5b | -7.89087 | -35.31887 | 2025-05-04 03:40:00 | NOAA-20 | LAGOA DE ITAENGA | PERNAMBUCO | Brasil | 2608503 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a2939567-5a22-3a69-a983-1632b9d22d81 | -15.46049 | -42.90321 | 2025-05-04 03:42:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0dde0ff4-4154-3780-bb39-2efcca3e2109 | -13.71225 | -45.20362 | 2025-05-04 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8567d59-376b-3d3a-a6e4-c7e1e9905736 | -14.19885 | -44.35654 | 2025-05-04 03:42:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01dc17b9-4d6b-33fd-8c28-d71936b20240 | -13.70837 | -45.19691 | 2025-05-04 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8accd920-191d-3e27-ae78-1c424859bbcd | -13.70729 | -45.20257 | 2025-05-04 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 74f80ab8-b930-3706-9eed-e4bc688c43c1 | -13.70232 | -45.20154 | 2025-05-04 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d815267-7a3b-3ed2-ac69-e5a4635550fd | -15.45979 | -42.90707 | 2025-05-04 03:42:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c124a587-74a9-37eb-9f27-8b4a0cd6fea0 | -13.7062 | -45.20823 | 2025-05-04 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0929a5c-a38b-361c-a1a7-e7a3faecdea2 | -15.60133 | -39.62674 | 2025-05-04 03:42:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| be4b5e95-285b-33cf-8558-865a9636236f | -9.7837 | -42.03398 | 2025-05-04 03:42:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e3416d0c-19c5-3183-9115-d37e317cb58c | -22.67716 | -42.85434 | 2025-05-04 03:45:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9bde12f8-f766-3c01-b44a-a09ed719ead5 | -19.57335 | -49.68427 | 2025-05-04 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee61f2a4-ecf9-3e3e-a566-7530056ff377 | -21.18102 | -44.27246 | 2025-05-04 03:45:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fc339756-2f11-3de7-b0c0-2698f542f5ee | -21.6244 | -43.46712 | 2025-05-04 03:45:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1d879e84-66fc-39bc-83a1-cdd0388e6203 | -16.68089 | -43.88326 | 2025-05-04 03:45:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5d4ef1c-1409-3b27-9294-b5ac33901476 | -22.7484 | -43.27579 | 2025-05-04 03:45:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8a3e87e-1004-3db7-b48e-bee485abd9d6 | -17.04098 | -45.70556 | 2025-05-04 03:45:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2153aff8-18dd-3fce-89b9-271288c8392b | -20.89799 | -43.82076 | 2025-05-04 03:45:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e56f7cd-5a4e-3fe3-ac71-4436de418e11 | -19.57123 | -49.68123 | 2025-05-04 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 86292b17-5440-3340-82ec-9583d4c2d818 | -21.17793 | -43.9816 | 2025-05-04 03:45:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 900c6a6d-3e09-3247-85e1-68f364b0d3d7 | -19.4355 | -44.34116 | 2025-05-04 03:45:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c49f3500-6e02-3838-9d9f-6ae07d111bb7 | -19.57025 | -49.68554 | 2025-05-04 03:45:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b768ca67-b226-3d40-a9a6-6a1f636803e2 | -21.17793 | -43.97942 | 2025-05-04 03:45:00 | NOAA-20 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5377244f-0e3c-32cb-8101-0ecf8238f966 | -22.85703 | -42.98105 | 2025-05-04 03:45:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7374173f-16f3-3ddd-9dc6-9216e9a098aa | -19.97005 | -44.21586 | 2025-05-04 03:45:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3538cbde-9643-3b67-9789-16c5aa55ecf2 | -23.98156 | -48.91611 | 2025-05-04 03:47:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d55576a-d80c-359f-ae61-c8f48e30c747 | -23.98084 | -48.91941 | 2025-05-04 03:47:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6915660f-7b58-3d3f-84da-f881933e28c0 | -4.22724 | -48.44666 | 2025-05-04 04:32:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README2.md)
