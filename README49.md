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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e9df86c-336b-336c-848a-474dfc62cee0 | -2.20344 | -47.99678 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 830ed9d0-48d6-320c-9df7-623adaec0058 | -3.59312 | -53.45333 | 2025-09-03 04:44:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95a58a32-fbfb-3b7d-8d94-92ad1ee55568 | -2.91264 | -49.78736 | 2025-09-03 04:44:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67d9a4d9-39ce-3ba1-a357-e0fdc156e076 | -4.7927 | -43.6668 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ceebafa7-2d1c-321c-997f-5650ff131d53 | -5.74192 | -39.76162 | 2025-09-03 04:44:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da8493bc-b12b-3c00-9002-ea22bab85190 | -4.59522 | -46.59333 | 2025-09-03 04:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 598d0a21-2612-3766-a8b9-450703afcfe1 | -3.44527 | -54.63682 | 2025-09-03 04:44:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9814bbab-6260-3dde-a175-fb5554a1fd08 | -2.55857 | -47.71418 | 2025-09-03 04:44:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d99e59e5-4872-3cfe-b24b-0b487d1d7ecb | -4.59904 | -46.59389 | 2025-09-03 04:44:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68109b09-abc0-30ed-8733-2ab8020d3615 | -4.81496 | -43.54425 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e31a309-22fd-3138-8bd9-b6476fa76626 | -2.58787 | -51.92252 | 2025-09-03 04:44:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45398de5-c5d3-3e98-870a-3d3dbd8159c0 | -3.22675 | -47.13352 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 9666b1ab-f61f-3bcc-87b5-f87de7c2564c | -2.13226 | -48.00581 | 2025-09-03 04:44:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0facd6a9-ce9b-3f1f-b896-8feed182e501 | -3.22505 | -47.12025 | 2025-09-03 04:44:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 321c1635-879d-3b15-b7ba-455b37a189f6 | -4.90146 | -43.21308 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7d82e6e7-bf7e-3012-9458-97a2b0a2daab | -4.82992 | -41.81065 | 2025-09-03 04:44:00 | NOAA-21 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c74268d5-1d7f-3afc-be6d-f98caba11150 | -4.66861 | -41.95826 | 2025-09-03 04:44:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 98e26816-1b94-375d-a2f8-e20ae0899656 | -3.19806 | -40.74142 | 2025-09-03 04:44:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2bf5f543-ecec-3e46-b369-5a8bd72e54a9 | -3.98035 | -47.00237 | 2025-09-03 04:44:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3f23dca-664f-3b82-9a7c-64aae19a8662 | -2.42264 | -48.93697 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 188cc532-d088-398c-bb50-6ecc2a621a01 | -3.20079 | -49.11115 | 2025-09-03 04:44:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 447ff831-c772-38eb-bdee-96f12cea7a80 | -4.89665 | -43.21238 | 2025-09-03 04:44:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 132c3828-64fc-39a9-bcf3-a738b213bb0f | -10.759 | -45.27947 | 2025-09-03 04:46:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 973fb0dc-dad5-3c4a-a5e6-13c5c76150dd | -8.8708 | -45.74846 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8feb5c13-85be-3e89-8ab8-89d7b4f1066c | -8.02064 | -44.09175 | 2025-09-03 04:46:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e3189ec5-5b32-3eb0-b444-5fe52e4505e9 | -8.09052 | -47.59211 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6562411-d8b5-3581-a8fd-b98d88489131 | -6.79619 | -52.80478 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 846b4f18-d73f-3f3f-bf15-e557b0d2aad4 | -11.43884 | -46.91745 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a447e5e7-a6d0-3c6e-96a1-58a71daa6b9d | -11.59074 | -52.13566 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 404a135a-8d27-382a-b152-ffab12ee2235 | -11.60226 | -52.10518 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bb4390c3-e29a-3e44-9797-2edf07ccafd0 | -5.93169 | -43.36336 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bf96df32-16ed-32db-b399-1f537e43b6b3 | -11.08463 | -52.02228 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 33bc8a4f-acb5-3691-a3c7-b6ad5465a27c | -10.08087 | -48.06105 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb41a818-6f54-3b1b-bfaa-e503dbc1be38 | -6.1515 | -56.13039 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 164c2ed3-eb45-39ad-a460-74f89ca87b27 | -7.90982 | -46.47823 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cd4ca53e-987f-3504-ad78-17014ffaf430 | -11.60175 | -52.13024 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c6de7d4-19cd-3b37-8703-61d18658b2f5 | -5.89404 | -57.74637 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 879e4471-c116-3922-926b-827fb31a5a70 | -6.19666 | -43.36136 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 014fba0f-e215-3186-8bd5-7c2e69c0bc17 | -11.60883 | -52.08465 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| daa6336f-93da-3619-9b24-ec3ae9e98323 | -6.80574 | -52.80997 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f175134-2764-3085-b1c6-8d654792df06 | -7.92803 | -46.46632 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e43365d-758f-3e58-b19d-ddc316d65797 | -6.84506 | -52.82371 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 659b5641-7cb6-398d-b9e5-f5738f634084 | -10.08462 | -48.06169 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82b5ca92-29dc-37ed-adf2-97a67120fa97 | -8.36975 | -52.54129 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 695d3d09-3c22-34d8-b2c2-64dc59d02807 | -6.82984 | -52.83245 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b44fe70-1eff-3f69-9d79-a57ce58c99ce | -11.5874 | -52.11358 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 31d005ba-8a3b-3e3d-a3aa-7189a3be609d | -5.7099 | -43.10999 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a6aaca70-918a-3801-84b0-c983cb0e3010 | -6.8619 | -52.81505 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1d90bee-b087-3d62-a1e4-b0defe70561b | -6.83263 | -52.83662 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf7a0933-7148-3fef-bd8f-d07e7825572c | -9.62752 | -47.06789 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 775848a4-c734-3995-9174-9540a217d181 | -7.00019 | -43.2548 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 72d0a454-34eb-3ae9-b6c6-170cdd70e484 | -11.61486 | -52.06765 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50ed4e58-61f1-30fe-8bf6-568e6dc5df71 | -9.71552 | -48.30811 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6f97987-f196-39fd-96f2-8c531dbe6a51 | -6.57653 | -47.38303 | 2025-09-03 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 61a478c0-cff4-3156-bdf7-918bab5cce28 | -5.8618 | -57.7731 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d837abdf-d4b1-3789-aa42-d1c1272c1e37 | -7.7133 | -48.7537 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 44531d60-5bdc-392b-8f4a-efae65640dae | -6.55057 | -42.96326 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45f8831f-b971-34e3-87bf-e93505ccd350 | -9.70702 | -51.03735 | 2025-09-03 04:46:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c41ee64-0a11-36ac-a3e5-c07b5d4a1031 | -7.70175 | -48.73305 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 05143d42-31e3-3a75-8bc3-ce696265127c | -6.78753 | -44.46636 | 2025-09-03 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c48da9f4-95dd-389b-9128-9e8d59b4c2fc | -6.98622 | -43.10306 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7d8ee7d-c59d-3d8c-8440-a45a1588e644 | -5.91572 | -57.72704 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 75d43a53-45fb-3620-861e-4d7878f0b7c6 | -5.86409 | -57.7597 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64c8dc09-65fe-304a-bbf1-3d7a2d14163c | -5.8892 | -43.00883 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cdd84950-a09d-34a7-9a71-1d2dcfbe59d9 | -10.54192 | -50.4388 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d827acf0-b66f-326f-bdd3-94af6ee5fbf0 | -8.86666 | -47.95043 | 2025-09-03 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7778033a-e3c3-370e-8da4-9c264a76dd9b | -11.38078 | -43.61013 | 2025-09-03 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1144543-b5da-3f5d-99d5-74721aa9477b | -10.131 | -46.24654 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b36de90-ce53-3a9a-8522-1123cd45dc52 | -7.48262 | -49.47954 | 2025-09-03 04:46:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fea1eb0-dea4-307f-bd9c-9b6b71086dbb | -10.08393 | -48.06636 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c146652-da10-3cd3-8ba1-b1f37e2afd84 | -6.22748 | -43.38809 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7cc3564a-7fd7-3bb2-a6b7-957bf1f1e27a | -5.76958 | -46.60675 | 2025-09-03 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42606b02-f503-3807-8a2c-3838ba8aa6b1 | -7.60039 | -46.2318 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d925281f-13d8-3bd1-87e4-1e24b3d46a40 | -7.01774 | -44.36478 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 023897dd-f93c-3ff1-82d8-8c2d229c58d1 | -11.094 | -52.02736 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b50ae4b7-3a3b-36a6-a20f-70cc5d626dec | -11.92448 | -46.66928 | 2025-09-03 04:46:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4446f227-3d67-377b-be9d-d6c28e02a711 | -8.37217 | -48.31259 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 940cd0bf-ec3c-3b28-84f1-ca4ad64c16ce | -6.95843 | -42.97108 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dae9a80e-ff18-380a-b3b3-e7fb2927fd3e | -4.52493 | -54.97353 | 2025-09-03 04:46:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed59952-b4fc-3b3d-8886-fe80da07103e | -11.44463 | -47.3008 | 2025-09-03 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f4a807d4-23f2-3a14-867f-04f4cc61fbed | -10.7299 | -49.59352 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 078828dd-5705-3514-9b05-2a5146989cae | -11.61541 | -52.06414 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb1ee011-22d3-3e7a-aaa6-e8bbc663953e | -11.64844 | -52.04785 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13183a71-f997-3ea5-a3c6-0339d31f49ba | -7.26057 | -57.55096 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c167e975-647f-3613-9ae0-2fb87a9362a2 | -9.39755 | -48.0516 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 291e99dd-a1ee-3c58-9884-17f08b405774 | -7.70513 | -50.25859 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fb485e41-e1ba-371b-8d5a-c2628f213683 | -6.97623 | -43.10143 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3bc2edc5-9515-3df4-b88c-71223d895cc6 | -11.05111 | -52.06347 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 908c9eff-6d99-3af7-a26d-8a39d4afa534 | -9.63724 | -47.86688 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b77cc0b7-384f-3911-b849-f80a0f4187db | -10.09447 | -54.76161 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ced43e9f-c4b0-3dbc-980f-4da1f74d3eca | -11.42508 | -46.90462 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42040e7e-fc0e-3609-adf5-9eadbeb2beb1 | -8.82746 | -45.80854 | 2025-09-03 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4007489f-5a36-3ad2-aeca-bd97649e6610 | -7.94643 | -46.5481 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b32657f3-55bf-3204-a90f-fe82371bdb8c | -9.94968 | -51.6223 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4f85631-36f1-3fc8-9ed5-816754a1e5c5 | -7.71798 | -48.74641 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 72e1c8cf-0fa9-37fd-8ba1-a5cc012982df | -10.08144 | -48.06305 | 2025-09-03 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5f3e320-f91d-310f-b684-c0795927aa5f | -9.76725 | -46.93012 | 2025-09-03 04:46:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6788c75d-dd20-3820-94b6-f5c5b42e2cfd | -9.91553 | -51.62407 | 2025-09-03 04:46:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 657943f3-ad43-33d3-ac7f-1ea0249c9e28 | -7.92856 | -46.46272 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88006254-3700-339f-8bd9-e3cf3984f59a | -11.09951 | -52.03542 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README50.md)
