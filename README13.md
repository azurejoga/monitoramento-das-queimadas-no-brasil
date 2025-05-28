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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1515c36b-f282-3a41-baa2-73a213dc5aae | -9.84634 | -48.14343 | 2025-05-28 04:32:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 063bd38a-0919-3eb1-8454-a984cee67325 | -7.19466 | -43.10869 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 7b79554c-8b64-3f69-b84a-d273bae06c2a | -12.83702 | -47.39304 | 2025-05-28 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b25bfda-5caf-380c-809c-7a282051e061 | -9.03986 | -47.74253 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 71e350d8-01f4-332c-9365-5361b4db67ff | -11.14234 | -53.91965 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4818f86b-70fc-3c78-903a-82612f6fd69f | -11.82059 | -44.26641 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 8687e6a4-b772-39d2-82ca-d871cd702ce4 | -9.1521 | -49.65118 | 2025-05-28 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e713842-3f2a-3fe4-8091-5f24391e0c5b | -10.23216 | -52.2311 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8909460-8262-3ed9-95be-a46eb9d3d691 | -11.81913 | -44.27672 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 99b47b35-30d9-3c1f-a15b-239bda85ecba | -12.4053 | -49.99917 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d2b22b2-848f-3d95-8093-ed5d814143dc | -8.35899 | -48.03598 | 2025-05-28 04:32:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 212ab883-32d0-3571-bb0d-503398c013a1 | -7.60678 | -46.64664 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9f0ab51d-5f5e-3a33-9bf8-292d5fb2481f | -7.60962 | -43.39395 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31ee6bd3-a4fa-3b44-8a7f-577a476d00be | -10.95222 | -48.14902 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c25b2bdb-ef49-3eff-9792-14d7cdecceb3 | -11.28759 | -54.01796 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2cfbf824-1d9e-35fc-bf33-e102618a7347 | -8.3496 | -48.03093 | 2025-05-28 04:32:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fe9b344-e989-348f-a2b8-85b163c25e37 | -7.20614 | -43.11396 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1476cc83-1ea7-31e0-b1a2-c0a45e93e5f6 | -7.22263 | -43.11292 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 92bed03b-946c-3cdc-b4a5-2b7b6b8404f9 | -7.56776 | -43.32807 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f52a695-dd12-3ce4-85fc-5d85e99f79d8 | -7.61208 | -43.40466 | 2025-05-28 04:32:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38883cdd-9314-3813-88ef-91aec5c704ca | -7.62435 | -45.75491 | 2025-05-28 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 74eeeb98-1acc-3bcb-91fb-578aa16e3796 | -11.57619 | -47.62674 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8efb3e84-3ccb-3cd2-934a-7eca0a07fd5d | -10.65277 | -44.49513 | 2025-05-28 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c367182-991a-3c3a-9798-d0bed2390db8 | -8.17552 | -46.49801 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48e62942-8ec7-3cfd-86ad-52d42f405582 | -10.27785 | -47.98823 | 2025-05-28 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3ca87fc2-4e4d-35a8-a0fd-377518ae11f1 | -8.00406 | -46.15354 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67ed63fe-6d10-336d-9f9e-4acab1fc2435 | -12.28449 | -43.54548 | 2025-05-28 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29125660-6de4-325c-9f24-103483a024b2 | -11.29282 | -54.01157 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 211a6b2f-c33d-3918-9cf1-491a187e3384 | -11.76878 | -47.26301 | 2025-05-28 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 023d2e4c-165f-3129-a8d4-3725cf57112e | -8.8196 | -49.8415 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5251d98e-007f-34f2-bbfd-1f1b7eaeab30 | -12.07897 | -48.45492 | 2025-05-28 04:32:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad0f1bf7-64a0-3c7d-a4db-62123cd95c30 | -12.37029 | -49.98649 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00137302-c9cb-3029-8732-19bab172ec19 | -9.39069 | -48.42867 | 2025-05-28 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 74936e5d-6347-3ee9-a6be-db862c7080a9 | -9.60568 | -49.02468 | 2025-05-28 04:32:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd2fe1e2-bc6b-36aa-815b-d1f5a58ea170 | -9.67543 | -49.71411 | 2025-05-28 04:32:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9b1d120-8746-3d70-92e2-276e8341f1e8 | -11.97738 | -52.46798 | 2025-05-28 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 629a92a6-fc09-3974-bd3f-727732bdd71a | -7.95343 | -49.75467 | 2025-05-28 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b2cc94e-0159-3355-ad94-64c7a8ddd5f2 | -7.96701 | -45.93397 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa93d11b-1974-37cf-b288-1cb5e10ca8e6 | -7.63071 | -45.75987 | 2025-05-28 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99e60e79-c155-3b6a-acd2-07b9f9f4edfb | -8.14481 | -46.48964 | 2025-05-28 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8b0d48b-1558-3df5-bccc-8309a4d79ed8 | -8.74489 | -48.0437 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b7e1f91-1746-34cf-9a80-cd9477983cb9 | -10.66297 | -49.44472 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c71a2c2-3628-3480-a997-8a116b2e21e7 | -11.81194 | -44.27039 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7960659d-870b-364a-895c-03f9f7cf3506 | -11.13895 | -53.91547 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d832bef2-0776-3e53-84ee-ced1aaef4ba7 | -11.13772 | -53.92248 | 2025-05-28 04:32:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f2e4b67-ca49-39e0-9a55-2216b2d3695a | -6.63108 | -55.01042 | 2025-05-28 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7dabdd5-b880-3fcd-9b49-dc7e15a1768e | -7.20563 | -43.11745 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fdcfb868-dc9f-3551-84c8-57ca1d0d742b | -12.10979 | -54.67108 | 2025-05-28 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94aeea83-3ac1-3493-9652-b2830d23ae8f | -9.19799 | -49.47198 | 2025-05-28 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b7ab447a-7264-3979-8041-2f3d7434a0ef | -11.56946 | -47.62567 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a8c27c7-fe4b-38d2-98cb-ecaf34899733 | -11.29766 | -53.98332 | 2025-05-28 04:32:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8615f2a2-f24b-3282-9d33-4e3b84f32462 | -11.82382 | -44.27214 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 12461359-3118-3f53-ade4-dd44cbe3856d | -7.66992 | -46.09543 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e471dcc5-f62b-31bc-a523-7c41c324aafe | -12.26963 | -44.59688 | 2025-05-28 04:32:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 411ce57c-8ada-3ab3-9822-f4b44e0bdd81 | -8.01421 | -49.68587 | 2025-05-28 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7550db0-704f-304b-b3bc-a3167b621bd2 | -9.15267 | -49.64761 | 2025-05-28 04:32:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df734110-c1c4-3a8a-a53d-68057f5eefd7 | -12.25519 | -53.28265 | 2025-05-28 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41ddea6f-f3ce-3a4d-a6c7-0ffdf4239b18 | -12.11391 | -54.67184 | 2025-05-28 04:32:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0547925a-feaf-3df0-930d-c5c8bbac6324 | -7.74664 | -44.01149 | 2025-05-28 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d05dba2c-c9b9-35a3-b4f7-a5e78456a8be | -9.03654 | -47.742 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d21de9a-8bec-3f7e-933a-193bd4462c00 | -7.18615 | -43.11105 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| b1ddbe92-01ec-3c42-95a7-ca7bcd6e2702 | -10.45363 | -47.94742 | 2025-05-28 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5399156a-f3ad-373c-bee4-5b17ab5a9971 | -9.04209 | -47.75008 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aac29422-238e-34de-8dc0-02761931e5d5 | -9.03099 | -47.73392 | 2025-05-28 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a9f11f89-76b5-39c4-aca2-46179d93b27e | -7.66934 | -46.09919 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bf85ab1a-a00a-3337-b556-388fce443b13 | -7.19066 | -43.10811 | 2025-05-28 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| b65c766d-9977-302c-bbff-6b3237444739 | -9.51268 | -47.69054 | 2025-05-28 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a974df94-5a95-34fa-9041-d3c1df05bbcd | -11.39924 | -52.95127 | 2025-05-28 04:32:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1056dc7f-0b77-321c-bd8e-a5c6919f2adb | -7.67108 | -46.08789 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2883d70-cb00-3300-acd5-411a91f9effb | -12.40472 | -50.00274 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b6df6c5d-980e-392a-85a8-9752587ac947 | -8.79164 | -47.94039 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4bcf472e-19fd-3dbd-9874-11d6b5229e68 | -10.06293 | -48.27805 | 2025-05-28 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 195b70bc-3efa-3270-b2cb-62f5d3f18c4e | -10.66573 | -49.44879 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c4f724f-8d29-3aa8-a465-e0719b1986e4 | -11.04138 | -55.0805 | 2025-05-28 04:32:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c43b39d4-2e3f-3f56-bf0c-60154b777797 | -8.0986 | -46.28885 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae5ae860-1e4d-3b75-b609-75bac132edeb | -13.07703 | -45.27741 | 2025-05-28 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7d02b4cc-14ed-3358-a1cd-d8ce152c8cea | -11.81121 | -44.27555 | 2025-05-28 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e83dba32-fec5-34a7-ae0f-9c7a9e8dfdc0 | -9.0448 | -47.01189 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27e79864-d114-3ddb-bafd-593bf7633f7a | -7.67964 | -46.10075 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8acfcb7c-c985-30aa-b048-7221c247d6cb | -10.53487 | -59.22298 | 2025-05-28 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 341817ba-5047-384f-b351-6f8a7762af00 | -11.56273 | -47.62459 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af8eed4e-c43d-375c-ba66-b85678a7d787 | -8.77896 | -47.95625 | 2025-05-28 04:32:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74abc664-1058-3949-a714-6eb5d1e20d7b | -10.73195 | -49.28986 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff2f0800-e88e-360a-89c0-bd1e67c47b69 | -7.68308 | -46.10128 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a4adfda1-0ddd-3916-90b6-8ee3428738db | -7.67679 | -46.09649 | 2025-05-28 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 491f6b95-f979-3347-8f22-8314fc59edc5 | -6.83473 | -43.40757 | 2025-05-28 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 522352e2-cdb3-32c7-8fa7-7be9ecc9c79b | -9.39862 | -48.42252 | 2025-05-28 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7266dcec-bd9f-3036-be74-1942d3e4721b | -10.98215 | -44.6226 | 2025-05-28 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 215c0768-f8aa-32d0-bd76-1bda9f615104 | -12.40805 | -50.00329 | 2025-05-28 04:32:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dba1dceb-acc0-3abf-b500-caae3e8222e1 | -11.9781 | -52.46368 | 2025-05-28 04:32:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bb4ce07-3f2d-306a-b635-157d8ca48660 | -10.65965 | -49.44417 | 2025-05-28 04:32:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 373ec7dc-8cd2-3768-b0a6-57947f88efd4 | -12.82333 | -47.39094 | 2025-05-28 04:32:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8238c78a-89fe-3c32-891f-96ae26261423 | -7.62782 | -45.75547 | 2025-05-28 04:32:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a629f238-ce5a-3a2e-a41f-4682b083c6d9 | -10.23143 | -52.23546 | 2025-05-28 04:32:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6594d94a-b9d1-3093-bf70-1a7d00c70a27 | -12.25141 | -53.28197 | 2025-05-28 04:32:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af14f1db-8ffe-3b08-beb8-f125a486e3fc | -11.57395 | -47.61891 | 2025-05-28 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 416a1e91-ae6b-3f31-96cc-d0104572b9d8 | -14.53143 | -48.33932 | 2025-05-28 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53833293-df8f-351d-87c8-56d55dea871e | -15.80034 | -43.56892 | 2025-05-28 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d6a25d2-894e-3c6e-918c-3dfc58e75a26 | -14.68701 | -45.08986 | 2025-05-28 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eedc09cc-7145-35c9-a4a2-44b5f4e5f039 | -14.52806 | -48.33878 | 2025-05-28 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README14.md)
