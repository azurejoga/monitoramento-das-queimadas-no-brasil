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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9981be12-39d8-3585-ae68-976e1df7c948 | -10.66438 | -54.15571 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 97a48545-86de-357b-94bb-8cec9128eec0 | -9.9842 | -59.86747 | 2026-09-14 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23092674-9e11-3e43-b340-df398f3b7736 | -6.29232 | -59.94061 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a1faca7-6469-36d0-9a16-d30ebb7cce49 | -9.31845 | -44.35813 | 2026-09-14 04:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b46abe3-8509-38c9-a16f-d81f681fde73 | -10.11516 | -49.03567 | 2026-09-14 04:53:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33f3c7d3-dd35-32c9-b198-ec451dcd08c5 | -6.62476 | -58.37518 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8727bec-29ce-3621-a0cc-e683eb6a4851 | -6.37276 | -55.2597 | 2026-09-14 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3e4ebf2-23c5-3f06-b4c4-160887fe15ba | -4.38312 | -55.20444 | 2026-09-14 04:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b1919ece-7833-3483-9c3d-5d6176115f13 | -5.58662 | -60.18967 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35f66df1-7d7d-3c33-9b0d-01947f4a7b1a | -6.29696 | -59.95281 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4d774c1-39be-3cb3-92fb-9c414adb38d4 | -11.77963 | -46.3946 | 2026-09-14 04:53:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5f90f54c-b23c-34dd-ba16-4dd0432432ee | -11.25476 | -54.13017 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b159a231-82fe-32ed-8ebc-d037daf3fee7 | -4.13817 | -54.01971 | 2026-09-14 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9962a5d9-4e02-30eb-b2a9-905dddd33cdc | -3.71328 | -59.29821 | 2026-09-14 04:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4115732c-c506-30df-b50d-36247a3fc2ed | -9.43007 | -50.13601 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c97f597-bf21-30b5-832c-3455d1148f04 | -11.80371 | -46.59163 | 2026-09-14 04:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdc7cc4c-b897-3f73-af64-ddcdd3170cc9 | -15.56045 | -48.7964 | 2026-09-14 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 703a348c-6a4a-332f-851c-3598729b7093 | -4.98146 | -56.13893 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 133faf26-6016-38ef-b6de-97eeda4e71f7 | -10.17789 | -48.06585 | 2026-09-14 04:53:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb117986-9d6b-3bde-a29b-9ebd081474b6 | -6.31121 | -55.2815 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a6d7201-2052-3729-8fb9-15587df5a237 | -10.51523 | -51.31858 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fecff267-e188-3f2a-b143-c55061c6c723 | -5.61852 | -45.24515 | 2026-09-14 04:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d706fd08-4366-38f7-9a75-4f697ae1ef13 | -4.8671 | -56.02287 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e949b21d-0429-3f2d-afdd-8dcb13fda9c4 | -11.18182 | -42.81718 | 2026-09-14 04:53:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d3560fc6-a7a7-3399-8433-e43e3dd983d6 | -16.48241 | -43.42646 | 2026-09-14 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac3f6c0d-ff70-341f-90a3-54d81a57a054 | -8.14631 | -54.804 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cf8d012-3cbb-3cd7-8aa1-ea734afedae8 | -9.41071 | -50.1936 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96bf5284-816d-3ed6-9be0-be54d1f4ca77 | -5.80869 | -53.80725 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ac92127-e486-3f7d-85d3-ff88fc3df929 | -6.30364 | -55.28017 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 951ae26a-09fd-3e6d-adfa-d900797f1f0a | -9.71577 | -50.85036 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d125b475-5894-332c-a491-5e980fb5c880 | -5.8448 | -52.09349 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82757371-78e8-35cd-9a7a-b7976ef74347 | -6.32639 | -44.17826 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b62c8222-2ec6-35cf-83a7-dfa37201310d | -8.54019 | -54.71633 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4998211-e41d-37a8-a214-91d723024b58 | -9.36587 | -50.12224 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a67e70d5-4c49-30cf-8a7a-0a244facbf22 | -15.24094 | -48.07417 | 2026-09-14 04:53:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19a6997f-5d49-3b0d-a971-cfe57dd5c15c | -5.12207 | -55.96755 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 696bf960-8826-37ee-adb5-a5cade3c4128 | -3.4143 | -58.20824 | 2026-09-14 04:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 23902e42-88f7-3487-a8c1-1379b01a08d2 | -10.65257 | -54.14212 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 75df0286-f903-34ba-8771-f21e20582bd7 | -12.3969 | -44.41241 | 2026-09-14 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 498a2d99-3c32-31b5-9aaa-0638d86bab5b | -8.99812 | -50.81905 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 706715a5-7d73-3704-b192-d85268d014aa | -6.32704 | -44.1809 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fc34dc89-973c-333e-9556-35d97634319b | -6.32257 | -60.01905 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcf11bca-f31a-32f4-a1fd-c4190ac346bc | -15.55657 | -48.79581 | 2026-09-14 04:53:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4a7124f7-c768-37de-a208-a4fa26313101 | -6.74726 | -50.92424 | 2026-09-14 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d57c88a-f7bf-326b-8cbc-680e24e7c0c6 | -7.77812 | -46.66762 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1b2c69c-de7b-3a3c-90b4-6f69866fc7d2 | -8.53508 | -54.70286 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a803980-631b-3587-bf9a-b6c4e394a3cc | -5.12838 | -55.95419 | 2026-09-14 04:53:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f49e0e0e-e813-3bed-a5f7-496fa14bb379 | -11.22477 | -43.436 | 2026-09-14 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b42b202a-3680-3930-be03-0a7e5512c4b0 | -6.2991 | -55.28407 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b2b59dd-10c2-3881-9068-7e4c6e98264d | -6.81166 | -59.43068 | 2026-09-14 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9e700e0-c810-3c33-a867-2ff603d3893c | -5.19753 | -49.33311 | 2026-09-14 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03021aed-f8cb-3448-ba9d-dff08cac37b3 | -10.46791 | -51.24928 | 2026-09-14 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54df70eb-d9e6-3448-8992-57eea97bd84a | -6.33312 | -55.19508 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2e4340d-10e3-3ec0-9a17-18162741974a | -8.54223 | -54.70403 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbf958ca-f54c-3b4e-ba83-d0102d71d688 | -6.28393 | -55.2815 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9739f275-67ef-3951-8b80-6d378c64120f | -5.90081 | -52.10265 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c268079f-0598-36a3-b838-51df8f0af50b | -8.39542 | -42.22216 | 2026-09-14 04:53:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1f5abf63-563d-3f9b-a754-3720a0f338e8 | -11.37519 | -43.95884 | 2026-09-14 04:53:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36fbd18c-b823-3ea4-b266-e0ef788e901f | -11.26435 | -54.13568 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 208d3807-8329-3559-92b2-eb9d32601cc2 | -9.46045 | -47.84925 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dad45f0-0e1a-318b-a13f-386538739441 | -6.30061 | -55.27489 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c0d32f4-89a8-3466-96e4-244ff28d7875 | -8.11744 | -54.79914 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94b602ca-9ea2-3deb-bd72-aaa735c109cf | -10.0664 | -48.78571 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5433f9be-f7e4-34bd-be1c-d15c22d405ce | -7.30251 | -51.75128 | 2026-09-14 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 235e6b50-ed5d-38a6-bef3-987302029142 | -8.17088 | -43.11192 | 2026-09-14 04:53:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7040673c-c207-3827-98ca-48c59b43c249 | -9.43405 | -50.13282 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c98c502-7d5f-3826-98ed-fa6e99b9c147 | -10.51917 | -51.35898 | 2026-09-14 04:53:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6d04a4f5-6082-38ef-9607-65c1966cd863 | -7.77464 | -46.66357 | 2026-09-14 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 037bb2e1-d4b8-3ca7-9478-0ca47c0448ad | -6.30288 | -55.28477 | 2026-09-14 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3c673c3-d20b-3fad-b9d5-34a015cde332 | -7.11612 | -41.79679 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3a8012a1-19a5-3767-86e9-92c4265923ff | -6.54259 | -58.55912 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57835c89-c936-391e-b71d-5a43c7aef5ac | -11.22519 | -43.43277 | 2026-09-14 04:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d516f73-a533-3fc1-ba7e-5465a51912b6 | -6.10278 | -59.89017 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d93abc09-e641-367c-bd5f-038dfcf737a6 | -10.67464 | -54.15748 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.5 |
| ec892481-eea7-3457-acbc-a83152221e44 | -7.09087 | -41.81606 | 2026-09-14 04:53:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3597e142-eb7c-352d-b06d-6b24bcf0ec00 | -7.09956 | -55.62601 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f234747-67f2-3be9-85da-1125d473ba94 | -9.40392 | -50.16984 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| ef232d91-d1fc-3b47-971c-f069f8e4d3bb | -6.5866 | -58.85187 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86796cf2-c6b3-3b00-a7a4-5484433d951d | -10.94914 | -48.3658 | 2026-09-14 04:53:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 83f98ecf-9f74-3845-b32a-c86aa7b41e27 | -6.64586 | -58.82144 | 2026-09-14 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6bfb1736-8e60-37be-8e52-3d4804c3e13f | -11.80795 | -46.59225 | 2026-09-14 04:53:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15b872db-9da6-3334-b772-92251ff9d566 | -6.31949 | -59.97606 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e34c150b-e60a-34cf-abc9-e4cf3275194b | -5.84322 | -52.03907 | 2026-09-14 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1dd9751c-35f9-308a-9a07-881976e55f26 | -7.1026 | -55.63136 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca01f24f-e00e-3e2f-8bb5-5ad2d084f006 | -10.66345 | -54.14012 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 885e265f-8912-3c36-8b0f-11f1c39386ae | -8.99757 | -50.82259 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 93e25a69-bab3-3263-b0d9-1cbfa41d95cf | -9.42612 | -50.11639 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 7d058dc4-6115-38a6-8d05-c95ef27e3e44 | -10.11052 | -48.86886 | 2026-09-14 04:53:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3165e70-2baf-3e86-943f-5d8d86a9bba7 | -6.87459 | -55.29805 | 2026-09-14 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0811356b-ef86-3ae2-85ff-330f9f13e768 | -6.33344 | -43.36277 | 2026-09-14 04:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6851db95-deec-3a0e-9e4b-07cb1f7d126d | -10.65536 | -54.14645 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 82af3523-2041-371a-9fec-4f23050096b0 | -9.41018 | -50.15187 | 2026-09-14 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4d9db6b-af60-311e-99ea-e5c8d682d758 | -10.68117 | -54.13929 | 2026-09-14 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9469147c-e955-36d8-8f17-933d651e3aeb | -3.70554 | -58.86578 | 2026-09-14 04:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d7ed28e-2ae6-31bd-80c8-ca0f4c28814e | -6.13258 | -57.69613 | 2026-09-14 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 34d60e79-95b9-3e45-916e-c6e3e481395b | -16.47717 | -43.42238 | 2026-09-14 04:53:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4465cbc2-6b31-30d2-af38-8b074073db4f | -7.47694 | -42.1229 | 2026-09-14 04:53:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a5d7aadb-106b-3355-8df4-9c58add6a422 | -9.69401 | -54.33876 | 2026-09-14 04:53:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e95fa87-66c5-3d8a-ab02-46faa20779ec | -6.29424 | -59.96045 | 2026-09-14 04:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e50550e5-c410-3667-8817-e58b7d3a9693 | -9.45148 | -47.8574 | 2026-09-14 04:53:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README49.md)
