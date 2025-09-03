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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 360ba475-befa-30af-8952-434fec06857a | -11.88545 | -46.67108 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 518922ba-ceac-3b94-bd79-1e7c2e9a39ca | -13.29726 | -46.93067 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ea17ee2-b418-3e06-b910-5cd31be69a3c | -11.60168 | -52.0717 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18b7b2b9-9b93-3570-9ca5-1f4cf3d1fc2c | -11.62221 | -52.06993 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d9b9b12-32ad-3c21-b71c-ce018ff6e1ef | -11.11503 | -44.64296 | 2025-09-03 03:55:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3116605c-3691-30ab-ac64-393b9f79be26 | -10.1468 | -46.26763 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 465bb100-e3d5-3fab-88f4-a3f17bb6c213 | -11.88068 | -40.95232 | 2025-09-03 03:55:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 58121d1a-cb4f-36ad-bfac-e04c8403ee86 | -9.39548 | -48.05199 | 2025-09-03 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae99f3ef-3f12-394c-8821-bc3c2a0f8ee5 | -11.85324 | -51.42414 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 970c2329-17b5-305d-80c5-5fb00a3fca5e | -12.83248 | -48.054 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17068493-7a52-3038-8998-e26c80527d13 | -14.62312 | -48.92932 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f44168a6-6e87-3dbb-82fc-a3108cc9f8da | -10.49094 | -50.33792 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a989bd8b-6264-3a0b-b297-42a1bffbe0b7 | -15.1171 | -48.15991 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 720d8737-86db-30ab-a952-5f0898caec5f | -10.94201 | -50.78084 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96bd1fd5-a794-3622-884b-047b9efe87da | -14.80108 | -48.20833 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27f637c2-5fcf-39f2-8bd9-3d084353a109 | -15.54543 | -48.32064 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1c6d055-797b-30e3-9982-4f65b2b18832 | -10.94898 | -50.77746 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a083326-9396-33f0-b102-77bf580489b2 | -11.96303 | -45.78778 | 2025-09-03 03:55:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1147e100-9b87-3deb-a72d-61da92833fa5 | -12.92505 | -48.08471 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| abab6f44-0f0c-3d09-81ea-76e53852e1d0 | -11.61301 | -52.14888 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4affec88-3a05-396f-a4c3-e2643467c41e | -12.98238 | -48.08547 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d9ca2b8-4d04-3baa-b58e-f517c06e1640 | -11.82325 | -51.44505 | 2025-09-03 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc7ba701-ef29-31e3-a09f-556e7556b369 | -15.16264 | -52.35924 | 2025-09-03 03:55:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c83fa72-25a3-3f31-890b-71dd24ee368c | -11.62468 | -52.05866 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e28f57c7-f22b-386f-803d-0e5de63cff1c | -14.16146 | -46.97527 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac81e0b6-0779-3a19-b516-32e224ceb989 | -13.693 | -46.95772 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcddf7f3-2152-3279-b504-32b3398f4df5 | -14.37145 | -47.07662 | 2025-09-03 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 473a59e6-ad98-324d-ae68-b09aa2e238fe | -10.53895 | -50.44004 | 2025-09-03 03:55:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba18e727-8d44-3fdc-8f1e-56f1855172f9 | -15.5498 | -48.39937 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a930e3d-c9b1-32ce-a68d-1ed621f12994 | -10.91751 | -50.87112 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 226a9bbe-fe1e-386d-8bfb-495fe8c6594e | -11.38195 | -43.5655 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56142e8e-19dc-313e-ac67-1affc3997af3 | -13.45825 | -46.92576 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 596847d7-69e8-3f97-bc82-059a5c9177a7 | -12.18663 | -48.2519 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af98adb5-ec0f-3a2d-82ea-f215838eb8dd | -10.1451 | -46.27732 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 898e0255-4b6e-31e5-a708-9291d98ebe67 | -13.33765 | -46.84019 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e054b51b-b1f5-35b3-8dc0-a8a909438d25 | -10.90354 | -45.79368 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c8e16bc-df8b-3633-837b-77f97fd59fb9 | -12.86409 | -48.03076 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| beab5d7c-bc11-3072-b50e-82b579911797 | -9.42624 | -48.35744 | 2025-09-03 03:55:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1a0e182-b75d-3e5c-b7eb-d95cecd6838b | -15.02042 | -50.07349 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1616ac97-dac1-369f-8524-9345528eaa42 | -14.90503 | -49.62188 | 2025-09-03 03:55:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d010891f-2b4a-31c8-b766-1ba8ba4a9654 | -12.99229 | -48.08688 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| df78e86f-dc93-3ea0-a214-7214b15aa04e | -15.71902 | -47.67384 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1618da26-06f4-3be9-8322-2389650f4a78 | -15.55464 | -48.4001 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 955f58f2-49f5-3420-a601-caefe69ae121 | -10.9066 | -50.83164 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51cb1263-43d8-3f9c-b0c5-1576eab7224f | -15.11698 | -48.15968 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 474c1ccf-a86f-3ba3-b505-dd49ef6f2671 | -16.34589 | -46.91802 | 2025-09-03 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ed3d104c-bbda-30d3-907b-f8fbdbfcdd16 | -11.59949 | -52.08249 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2682456c-3001-3b72-bd47-94b2b5929ae2 | -9.15147 | -49.64798 | 2025-09-03 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e53152cb-2a52-3c91-99a8-27739a716ad2 | -14.34458 | -52.79943 | 2025-09-03 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 292322d7-b832-3f9a-bf9b-bd2281ebecad | -14.26794 | -51.22558 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74fe6278-333b-395c-b62b-61ba017be372 | -11.38416 | -43.57541 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 630bc6ef-1fcc-39e4-b2f3-1c3a59191b86 | -12.90681 | -48.10023 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd10f1cf-ed94-3df6-b2ba-9dc471891dc3 | -13.90588 | -48.11562 | 2025-09-03 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0b71fd3-6b92-33fc-be9d-ae7c098b41cc | -11.86413 | -52.43329 | 2025-09-03 03:55:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd475df1-ad8e-374b-a32d-b7bc88dd1dce | -11.48476 | -43.21601 | 2025-09-03 03:55:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ccfc73b4-ddc6-3c4c-9995-86ec307359c8 | -15.89631 | -48.1629 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 85cb7b01-90c9-3286-908b-874fa7911dc4 | -11.38759 | -43.62152 | 2025-09-03 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 811c4a54-514c-344f-b7b3-e19c4482d1ac | -10.14901 | -46.28105 | 2025-09-03 03:55:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35af0855-c8c1-38d5-8152-f210105dcd9b | -12.95777 | -48.07323 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 76e87773-02fd-35ec-98d5-c91c73669e65 | -11.79975 | -48.35944 | 2025-09-03 03:55:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d15f7c4d-3934-348b-9661-9809658dce18 | -16.34779 | -46.92067 | 2025-09-03 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0117b8e5-6340-3c06-967d-ef0426699462 | -13.5821 | -46.92001 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6df15869-1ca4-32b0-9994-783c1966c439 | -12.83952 | -48.04368 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0127f17c-83cd-3f2f-9553-b3c3d1eef74c | -11.597 | -52.12789 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ebe90000-b087-3a68-981d-4e844bcd84cf | -10.05849 | -48.09517 | 2025-09-03 03:55:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17901553-6139-3523-bf71-14d9ffb8e0f5 | -12.6727 | -44.74825 | 2025-09-03 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 997916ec-6e8e-302b-86b4-ed2b71ed0c84 | -15.54491 | -48.34846 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b42e2db5-b131-38aa-9aa7-26badfef91f9 | -14.60318 | -48.03065 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c3eb49d-3cfb-34c9-a221-6f2e421c2c1e | -11.92315 | -46.67161 | 2025-09-03 03:55:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3c9a512-b8f8-3856-abd7-c0f94862d1fb | -11.60653 | -52.14751 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2519b0ae-69d5-3e19-8eb8-118f57bdf7d1 | -14.97072 | -50.20719 | 2025-09-03 03:55:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeac332f-396b-3d47-87da-96e1c62ae0f5 | -11.00422 | -46.82348 | 2025-09-03 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62049bd4-5dbe-30a2-b1b8-0a80bf08f1b7 | -13.30613 | -46.82491 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0e220f3-4125-372a-ab79-08f338990187 | -14.77996 | -47.51498 | 2025-09-03 03:55:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3920d6e6-ae46-34ca-b540-2e21c46002e1 | -11.57697 | -49.90867 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fd941cf5-e4fb-3a8a-acbb-e51ac6d8c635 | -12.99138 | -48.11821 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29c96727-15fd-3df8-a7a3-ae57b90f7b83 | -15.10399 | -48.12449 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4447b3a3-5b15-3b4d-a3b4-30086b8b54b1 | -11.11719 | -45.11322 | 2025-09-03 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b8f99937-e2b0-3b57-949d-63fa42fc9e31 | -13.50824 | -46.93319 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80f4d4bd-9e36-33d8-bd07-4ae8c036fb16 | -15.89997 | -48.16923 | 2025-09-03 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.4 |
| b5ad2b19-f448-315e-add9-b0ec03efb1de | -13.66274 | -46.94494 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f50c7fd4-5d0b-3652-9aea-f62cb50cd0a1 | -13.9863 | -49.55592 | 2025-09-03 03:55:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f6288da-82ba-3bc0-8d97-6e1f1e9cdf97 | -13.2763 | -46.83545 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 325b0586-5458-31f6-83e0-183ee31abdfa | -11.6028 | -52.06619 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fa9b680a-0885-36dc-b04a-fa10b38d026e | -15.11974 | -48.17114 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55ed6d38-379a-34a6-9054-8907e360bf25 | -9.63091 | -47.85666 | 2025-09-03 03:55:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bab0d314-aec3-3fa7-9626-307c2641be33 | -15.56564 | -48.42016 | 2025-09-03 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c98783f-7ef4-310b-be01-8c815ced692b | -15.12337 | -48.17815 | 2025-09-03 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 089400ce-adec-33c6-a362-e9c5f2b55da6 | -13.3385 | -46.83562 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b31a3209-2529-36e1-86d9-d924a3ce8473 | -14.80813 | -48.37745 | 2025-09-03 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 19a94ca5-4b05-31bc-b27c-5371f0e5f402 | -13.70112 | -46.96426 | 2025-09-03 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26e862c3-02a3-3fcf-aaa5-0e1d1ec14069 | -10.94856 | -50.77551 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ddd9f282-c80f-3352-be29-665b69dbf044 | -10.94164 | -50.77888 | 2025-09-03 03:55:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64ec1eee-1696-373a-b71a-3d132d7ec783 | -13.28982 | -46.83788 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fbd1f6a-2661-3736-81bf-e3f99d790765 | -14.40533 | -51.69955 | 2025-09-03 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6522129-692f-3c53-bf5f-23ff3f42c83b | -13.49219 | -46.81785 | 2025-09-03 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 975e367a-9ced-375a-b9c2-7ae4537ca76c | -11.62995 | -52.06561 | 2025-09-03 03:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 470b4224-7c86-37ae-b281-0cff7f029484 | -9.74599 | -46.91478 | 2025-09-03 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8d04c1a4-30d0-3a69-b736-a50a9ce68ac3 | -12.90796 | -48.09417 | 2025-09-03 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e424822c-6370-380e-b434-17dbe2c21f0a | -10.0597 | -48.08873 | 2025-09-03 03:55:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README41.md)
