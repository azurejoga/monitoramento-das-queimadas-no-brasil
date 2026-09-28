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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 68706609-44e9-3687-915b-23bde4a773ac | -11.0991 | -54.0285 | 2026-09-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c8df6b6f-f038-3c31-b02b-0b5acb67db85 | -12.7677 | -54.0296 | 2026-09-28 15:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| d167aad4-ff07-30ab-ba96-1bd2da428e6e | -10.8184 | -61.4191 | 2026-09-28 15:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 498815d9-4e9c-3b99-b7c7-a2e1fdcbcc4f | -13.468 | -48.5881 | 2026-09-28 15:30:00 | GOES-19 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 05111d6c-a302-33a4-a2d2-b4707dac4ccf | -10.7726 | -48.7399 | 2026-09-28 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 37.6 |
| 33aa6eb8-7761-3c48-b348-9aeee1f5b140 | -10.4237 | -53.7809 | 2026-09-28 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| f578e928-7c9e-3401-94e5-c386e1343dbf | -11.0424 | -54.0336 | 2026-09-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.6 |
| b27a16a7-7af2-3195-b20b-9974325e0210 | -12.2824 | -50.744 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 6f762a55-6b71-34ae-aa55-9b20504ac32c | -11.5628 | -50.5069 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7d8fa3cd-b082-37ff-9e82-e8ea1be5022b | -13.6866 | -56.6131 | 2026-09-28 15:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| a0fc40a4-3d92-39e2-9bf1-b7e81612c3f8 | -8.3608 | -45.4695 | 2026-09-28 15:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| b4b182ac-f3e0-307b-8b68-25953cfa5733 | -10.9156 | -50.6845 | 2026-09-28 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 74355b46-3db0-37f9-9c6c-f80be5f65f95 | -11.5818 | -50.5047 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| d589483c-5513-32dc-996d-ec7ced7cdc50 | -12.2445 | -50.7271 | 2026-09-28 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d650ebd6-d313-317d-bd8e-ee2a3de924cf | -11.7141 | -50.5538 | 2026-09-28 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 9bbd7771-e292-3402-bb9a-e1225d9d575e | -10.8534 | -54.0711 | 2026-09-28 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 84d25e61-4d9b-3e7d-8eca-334d1071615c | -11.0761 | -51.4097 | 2026-09-28 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 191cb8a3-64dd-3538-8834-9e067acec6c0 | -7.6851 | -54.7734 | 2026-09-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 896def79-8ff5-3954-88bc-bdc276291a33 | -8.2623 | -54.6969 | 2026-09-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 35d80bcf-11c0-3e9b-acf8-817809114c2c | -12.6267 | -47.2851 | 2026-09-28 15:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 0e12b14a-4bb2-3134-b59e-b19d8e00df74 | -6.6872 | -45.6456 | 2026-09-28 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a998c7f7-cd5f-33cd-8173-9f468cc83b25 | -11.0991 | -51.1111 | 2026-09-28 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9c7b73d1-3229-390f-81f2-de539b31e41f | -7.7037 | -54.7722 | 2026-09-28 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| b234b42b-9679-383e-870c-d28c33c2ab95 | -12.9649 | -51.0671 | 2026-09-28 15:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 314.6 |
| 40e56d8d-4b88-39dc-b184-cecdc2a78fe7 | -10.9154 | -50.7059 | 2026-09-28 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 220.9 |
| df00c9ee-af46-3c4d-a1e5-d5f31321cb32 | -12.1952 | -52.7821 | 2026-09-28 15:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2ee6d5e6-ec4e-3366-a7be-b26d0be7d4eb | -10.8944 | -50.8569 | 2026-09-28 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| d765d953-2814-344c-ae7b-31374e6d85e2 | -13.4325 | -57.061 | 2026-09-28 15:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| eee271a6-5a7b-36d2-8d54-e54b9b48bd6e | -10.1713 | -63.0571 | 2026-09-28 15:30:00 | GOES-19 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 41fa62cb-8e45-3a33-a039-3f04ce207d0d | -6.97385 | -42.8807 | 2026-09-28 15:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 153083a9-167f-3a39-8d18-6ad2ed0f18ad | -8.02887 | -42.85633 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| a427bc61-5591-3b3a-b30f-15aa305946e4 | -5.81705 | -35.56648 | 2026-09-28 15:31:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 8.5 |
| c721db50-566b-3281-bfd5-77eb97f8693d | -7.90225 | -38.02993 | 2026-09-28 15:31:00 | NOAA-21 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 59fbd9c5-dfc2-3eae-a8ad-a04e7da7d9c4 | -6.14204 | -37.81145 | 2026-09-28 15:31:00 | NOAA-21 | LUCRÉCIA | RIO GRANDE DO NORTE | Brasil | 2406908 | 24 | 33 | nan | nan | nan | Caatinga | 8.9 |
| abd15cb5-dcc4-3202-8955-33069f735619 | -6.94621 | -41.59983 | 2026-09-28 15:31:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 5c149a40-aa9d-37e0-80e3-aa6691915ba9 | -7.25611 | -43.37057 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 0912cdb9-fa75-3262-a5de-7f889d57dab4 | -7.0574 | -42.86795 | 2026-09-28 15:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 31bb2075-479a-3e14-b3d1-578ed793e0ff | -7.02174 | -43.73447 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 37468fb9-adbb-30e2-81c7-53b572ea9240 | -7.2992 | -43.31857 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0ca82a3c-9da3-3382-902e-e64a27047f76 | -8.02637 | -42.84758 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 53a40dae-ced6-3471-a8b8-f9f665ccd6c9 | -7.2562 | -43.36393 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 643ad6e0-2b90-3251-8f49-4c060a42e038 | -8.03427 | -42.84362 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 4b62b1b1-fe43-3a93-8bf1-fc2c6c56a686 | -7.72636 | -39.43587 | 2026-09-28 15:31:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 150fda70-83dd-34d4-924f-e058f1e58dfb | -7.01779 | -43.73397 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0d84d6de-d55f-3919-bf9d-0c13781e6a3d | -7.25528 | -43.36388 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| e90da592-b9af-3474-a11c-ba46a0de3c0f | -7.25696 | -43.37737 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 55.0 |
| 2deba72d-a47a-3043-827e-abbe3f562ebf | -7.90186 | -38.02706 | 2026-09-28 15:31:00 | NOAA-21 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2a450805-b683-3746-a952-87631830e951 | -7.02896 | -43.84805 | 2026-09-28 15:31:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 58c636a2-5248-3049-ab55-1328ee7044a0 | -7.26149 | -43.35017 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 70761e8c-2000-3649-a21e-9ef6264ff360 | -7.72083 | -39.43641 | 2026-09-28 15:31:00 | NOAA-21 | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 2f4c27fd-c3db-3af5-8e3a-a228e2981945 | -7.0582 | -42.87401 | 2026-09-28 15:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| afc56e3f-f332-30aa-9fd5-b95384276411 | -7.05259 | -42.83137 | 2026-09-28 15:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0181d2ca-a4ca-3df3-a7d2-ce2ff7ac1bfc | -7.15188 | -42.07833 | 2026-09-28 15:31:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| a323e1ce-dd89-3414-940a-75a07d2d9cbf | -6.94627 | -41.61646 | 2026-09-28 15:31:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| f6155c3c-1416-3eb9-9644-682a7891d603 | -7.25797 | -43.37735 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 58.3 |
| 57d35682-1982-3a37-9e1b-99d3c037802f | -7.03777 | -42.87576 | 2026-09-28 15:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| c54595cd-235a-3cc6-873d-36282ff276ed | -7.26237 | -43.35683 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 8321def4-fb5e-32d1-bde0-a818327daa83 | -7.90247 | -36.08551 | 2026-09-28 15:31:00 | NOAA-21 | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 59a1d0e6-130a-3ff3-89ab-4b18b8f9fd3c | -7.2631 | -43.36967 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| a5b19d98-e96d-3605-96ce-bd8f7f3511d1 | -8.02812 | -42.85018 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 2893c0ab-a74e-3404-9bbd-feaa8b9ed147 | -7.02806 | -43.84101 | 2026-09-28 15:31:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| c5f677ee-638b-3434-84f6-6f4787741db1 | -8.03166 | -42.83472 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| bc1228b9-5d86-3890-a316-ef05676ae189 | -8.04103 | -39.56366 | 2026-09-28 15:31:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| e6a5721c-3fdb-3dd2-b5ce-becc45a05c69 | -7.4197 | -38.09323 | 2026-09-28 15:31:00 | NOAA-21 | PEDRA BRANCA | PARAÍBA | Brasil | 2511004 | 25 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2377cfb2-3575-30e7-bde0-cea5d3e4fd8f | -7.03698 | -42.86974 | 2026-09-28 15:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 23.1 |
| f1f75c76-baeb-30b4-8973-bf0d617574d3 | -6.97673 | -42.88295 | 2026-09-28 15:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| f81a5a21-bdbe-3e00-9cfc-4632514ab94f | -7.26148 | -43.35674 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5fdbfad1-c437-357c-93ba-7c5251ca5a2f | -7.25708 | -43.37059 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| fa68aaaa-3835-3940-9e25-75d66ece0661 | -7.45489 | -40.21852 | 2026-09-28 15:31:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 20d9342d-7521-315f-a426-e8e996b1e305 | -8.02715 | -42.85371 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 21e774da-3991-3446-a705-fa3cecfcee96 | -7.2545 | -43.35102 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| e5d6e75d-e712-30ea-b957-9cbffb79d1d7 | -6.94428 | -41.6012 | 2026-09-28 15:31:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7fcbc162-cd33-38fa-b13c-74e183bb4873 | -7.25366 | -43.35094 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 48.5 |
| a4345fa3-1032-3224-8842-d95cb309ff19 | -8.02736 | -42.84401 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| eadfce5d-005d-3b3a-bf73-b780303dcc88 | -8.03503 | -42.84982 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| ffa78622-6fab-316c-a19c-0b2ec152ff71 | -8.52331 | -39.33706 | 2026-09-28 15:31:00 | NOAA-21 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 3264af06-0724-32ac-8c64-56b54c052871 | -7.25448 | -43.35748 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 37028f46-5f7b-3de7-bad1-2fc81ba2ae7e | -8.03245 | -42.84088 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| acdeb056-f568-3537-be82-c9c3f9bf891f | -7.25536 | -43.35754 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 0adfb9ac-bd7e-3f06-8bb5-7b009653519e | -8.03618 | -39.56397 | 2026-09-28 15:31:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 9.5 |
| ebca58f8-13b4-33d9-8ec7-98f7926ea5f0 | -7.42023 | -38.09329 | 2026-09-28 15:31:00 | NOAA-21 | PEDRA BRANCA | PARAÍBA | Brasil | 2511004 | 25 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 030088fd-458d-3fb8-b425-642a48799a76 | -7.3053 | -43.31089 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ce07d4fa-4766-34af-ad57-417200bc2c43 | -7.26228 | -43.36314 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 24.6 |
| c68fdc3d-c742-33aa-98eb-4d6cea8d5366 | -8.0335 | -42.8374 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 95c6865a-e3e0-3e46-85a6-e548998c4bfb | -7.04379 | -42.86911 | 2026-09-28 15:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 9662fa0a-6a27-35f5-aa18-880f0f99dc6e | -8.03326 | -42.84708 | 2026-09-28 15:31:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| eb9db4b2-f1cf-3245-b852-3073820a9dbc | -6.97597 | -42.87697 | 2026-09-28 15:31:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 8975922e-46cb-33b4-9a45-f44b593246ce | -7.02567 | -43.84718 | 2026-09-28 15:31:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2aaecba3-5ee0-3c82-90b4-8f7097a2b315 | -7.26321 | -43.36322 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9e48cdd6-77b5-3331-95e6-128554133001 | -7.92112 | -38.09296 | 2026-09-28 15:31:00 | NOAA-21 | TRIUNFO | PERNAMBUCO | Brasil | 2615706 | 26 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 2b4f41db-d7c5-36a6-b2ca-ab07c8647ade | -7.26064 | -43.35006 | 2026-09-28 15:31:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 9963aa10-43e4-3704-8e8c-34942c343b1e | -7.05661 | -42.8619 | 2026-09-28 15:31:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 973d3e96-4f64-3c45-90d0-8e866db0a29f | -12.2248 | -50.7722 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 27bfd723-c0fb-3d57-b6cd-eb58b7ece12e | -3.0616 | -58.0086 | 2026-09-28 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 161.5 |
| 657c3adc-92f0-38f0-9033-12641254c2ba | -12.7674 | -54.0502 | 2026-09-28 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 44b3596b-5e47-33c4-81d2-1997051abf50 | 3.9876 | -60.4824 | 2026-09-28 15:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 0db4ede1-3787-39ce-8190-ee2c6c192f34 | -11.9783 | -50.6943 | 2026-09-28 15:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 60a6155d-428f-319e-8a87-976fe81c76b2 | -10.7712 | -53.0699 | 2026-09-28 15:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 5d880308-2d16-3348-be7c-3662f224730f | -10.8001 | -57.2007 | 2026-09-28 15:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 4e9000a6-8235-3062-b0dc-082bf624e5bc | -11.751 | -50.6351 | 2026-09-28 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |


[Clique aqui para ver as próximas entradas](README89.md)
