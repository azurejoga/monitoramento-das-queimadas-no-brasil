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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ac5c202a-31c1-3cd8-b494-439ed665ddd6 | -13.37731 | -46.97868 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 60c4dcbc-ffe8-3332-a2dd-298c0ee4d2ee | -14.02468 | -44.55044 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 944e6348-f90d-3079-a617-dd03827c4ba9 | -14.0008 | -44.59348 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6df81d8c-bcd1-350a-a912-22ac939fdd37 | -11.83753 | -46.45384 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 259b3fe5-4d69-36c8-861d-82f2ab1fbf3f | -11.32048 | -43.5592 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad947d01-7880-3bf7-8ba0-0767c3cbb584 | -13.36429 | -47.0168 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6e2b9df6-f008-3ade-9964-6fdb2ee4c2f8 | -13.38443 | -46.99803 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e28e85b7-057c-345c-a457-b1f1d997a84b | -9.16903 | -59.57475 | 2025-08-30 04:21:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 786ec302-decf-3ab4-9ddc-7630fdc04d1f | -12.85092 | -48.16186 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d87ae98-a08c-30e7-b022-5e446ac8fdd4 | -13.19688 | -45.27329 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3856f68-59f2-373a-b15c-06e94c9e721e | -10.02941 | -48.07918 | 2025-08-30 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4549cce8-9c41-32ef-ad52-f00893fec443 | -11.84749 | -46.43377 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c313a5c1-cf36-3135-8976-92b42e4b34c3 | -10.66985 | -47.07466 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 627962f6-621d-360a-b5db-447bea2fe149 | -10.64911 | -48.66388 | 2025-08-30 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3ec81ee-3bb2-3fc9-8cf4-fa955f6c758d | -11.34657 | -43.52713 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6f04a7f7-7497-3b75-a2c7-e55d369a4b12 | -11.37236 | -54.33926 | 2025-08-30 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5e82c73-05c3-3010-901f-b0c825819938 | -13.36242 | -46.87816 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2831b32d-8cd6-364c-b2cf-e76751f70fb3 | -13.62843 | -48.18306 | 2025-08-30 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 842399b3-4faf-32e0-b2bc-42ec3d0122d4 | -11.25222 | -45.0125 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baa0a18a-0773-3dba-801e-090e0d7963f1 | -12.39142 | -46.43639 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7bd869f3-5e50-313e-82cd-7430566fd631 | -11.89849 | -46.71347 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63f453ff-2fde-3c10-b2bf-bbfd4ebd0749 | -11.914 | -46.70151 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 817172db-b0eb-3bb5-b3e1-5c90c8ebce61 | -9.64979 | -48.33868 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff345342-5276-3852-afe4-8730bb486bd8 | -13.68201 | -46.87999 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58292cf0-4798-3adb-97e7-46dd1e2a9bc3 | -11.88498 | -46.38949 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c5add35-cd00-3ed3-a55d-dfa495da8a15 | -12.37057 | -46.39348 | 2025-08-30 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 457d495d-74fe-3464-bb86-051efbf1e22b | -11.84866 | -46.38351 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fbc15a92-37f7-33e0-a2b6-98d140e37cf5 | -9.5859 | -54.46824 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae010115-317e-33c9-9afe-5edd9b0e9a3f | -12.82648 | -48.11874 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 592f02e9-589f-37b4-9c55-aaa0201b4f63 | -13.37997 | -47.00463 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0b52ac56-5781-3919-943e-a65202e092cf | -12.81662 | -48.17923 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cec089a5-1f9e-339b-ab40-d7a0e46087f6 | -11.30608 | -43.60883 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 642098cf-7c61-368b-9e03-9747bfba8907 | -13.38563 | -46.96911 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b5e7ae84-758f-3c99-845b-f1f5eba39ef6 | -8.56381 | -51.31074 | 2025-08-30 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d7192fff-a4a2-3e5a-8329-ab7f425a2217 | -13.40448 | -46.95753 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cac5ad47-fc72-32ee-aea4-f7f018bebc84 | -13.65215 | -46.91867 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a75e60fc-5298-38e7-b392-88c6922977a4 | -13.36848 | -46.88282 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95ca1bc2-37f5-3942-b110-86ae82ec5259 | -10.49214 | -51.62709 | 2025-08-30 04:21:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5982bafe-8b13-3a02-afee-082e5a29394f | -14.03433 | -44.48511 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02a1f8cc-d99c-37b4-8ef0-c7754dd4edf8 | -11.16693 | -47.16306 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2081d3b-5ab5-324a-8ce8-9ca8a2901f37 | -11.27255 | -44.92448 | 2025-08-30 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 763e1096-d33e-3c65-82ea-b2bbd49306b3 | -9.39288 | -48.22399 | 2025-08-30 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fefd6593-d1c2-3ca5-a192-949c4ee79d64 | -11.87674 | -46.3773 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 304533c7-8698-3537-b0b2-96adcfe32015 | -11.40753 | -48.95365 | 2025-08-30 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bfeb82de-4963-37a5-8fa1-a478e4fb6414 | -11.07034 | -52.05197 | 2025-08-30 04:21:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b37682d-47b5-34ab-b92f-81e5eae14102 | -9.66122 | -54.4368 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a57d419b-1212-3b22-a056-181fbc9f37a9 | -11.21952 | -45.02562 | 2025-08-30 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90851eed-0cb2-31a6-9c58-45004db8125f | -13.46794 | -46.96428 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4334ac58-f53b-3963-9f71-9e256e2df8ad | -14.04352 | -44.51808 | 2025-08-30 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c1573564-af92-3565-b227-b2db959925e2 | -13.50843 | -46.94541 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35318ea0-70db-3816-affc-1e3693d78d81 | -11.30551 | -43.6127 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20c4e7ef-1468-35ab-bcaa-75ed6d93d4a4 | -13.50182 | -46.83561 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e92dfb3-1e8f-387f-b6a8-1241a426a5a0 | -12.85372 | -48.16619 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6289c7eb-1e07-39dd-97c0-1638188f13c0 | -9.58062 | -54.49645 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa114908-a11c-3162-9e55-8b939222b2ff | -9.70479 | -49.46945 | 2025-08-30 04:21:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 21bfc073-958f-39fe-b8af-cb8fce198fe9 | -11.32805 | -43.60437 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 964c1b8c-dd42-3df8-948e-ddb7280d468c | -13.40116 | -46.95702 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 923e3f83-c066-3914-b9dd-4463aa5fe574 | -11.92109 | -44.85972 | 2025-08-30 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fda8a9f2-4e49-3a1c-a33c-65e9303c5759 | -13.37941 | -47.00819 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 32ced4fd-b65a-3105-af04-02450ae86471 | -10.37896 | -57.82566 | 2025-08-30 04:21:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 30065fce-e657-3a94-a666-0efba1757f71 | -12.06219 | -46.6461 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17787ba2-33ff-3376-ad74-70cdb2b1f54c | -14.99637 | -46.69754 | 2025-08-30 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f33d2123-bf67-3305-a43c-26f291fd423c | -11.30311 | -43.58061 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fa4d2fd6-d72a-3685-8cbe-19f517f74882 | -12.65267 | -48.19398 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb04954c-43b9-3770-af56-0adb76fd943b | -13.54865 | -46.9486 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6945733c-410a-37ce-87a6-11738bceb1db | -11.33961 | -43.59824 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f18234b2-0f29-3552-895a-b46168d36de9 | -13.19856 | -45.28465 | 2025-08-30 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82318d2d-8972-393a-91c1-65e408139179 | -10.93799 | -46.84673 | 2025-08-30 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ff2eb91-a127-3f20-8b3b-642d5d993d48 | -12.94365 | -46.14392 | 2025-08-30 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0eb73fce-deff-3145-a545-2ceb2d5b92bf | -11.84314 | -46.39701 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 682aab27-405d-3145-854a-f78e5e021778 | -14.47771 | -48.3839 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a96d8663-5ede-3d53-91e7-247ee07d2d2b | -11.91295 | -44.26395 | 2025-08-30 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f48d617-757f-34b4-8850-67d9f5710806 | -13.48748 | -46.84048 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03f160ff-6872-33c7-a56b-19d3aaa4c254 | -14.23291 | -48.07232 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9f0df709-cff2-333a-9485-716b1ea96a86 | -13.36024 | -46.87052 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e219dda-19a2-30a5-b632-ee2b399a220f | -13.44368 | -46.94587 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97fcbbed-ae05-3e9e-ab07-821ce018be31 | -15.80779 | -46.12829 | 2025-08-30 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f9d0b29-fc01-35dc-9b55-b9b5928a573a | -13.55749 | -46.93562 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11aed9ce-6636-31f9-944f-c4bfa984b165 | -11.87942 | -46.44622 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a6981d7-0266-3425-abfa-53bc39e0306e | -13.38506 | -46.97268 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 91378ab0-2de8-3a9e-bc28-e9142ac6b981 | -11.31191 | -43.64157 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1031a7c0-541d-3a0a-bf09-ca2c7d5520b9 | -13.39397 | -46.95948 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae405f3d-f5eb-3e8b-a2e3-5a19a474936c | -11.85359 | -46.39513 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a847aa99-bcbd-3fd9-8ad4-6e18cedcf9ef | -12.65795 | -48.18322 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d713c8bf-906a-309b-9ef9-1d875ee41501 | -11.93887 | -46.69469 | 2025-08-30 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b679ef9-dc76-3e13-9a8c-1f6c5a94b123 | -11.85856 | -46.38512 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c48bb955-e887-30a9-8f44-826514cb8bad | -13.65932 | -46.91627 | 2025-08-30 04:21:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d5c67da-8813-30b2-948a-d6af5c891440 | -11.31309 | -43.65761 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8e5df31-8715-346a-9b1a-55cdb51f698e | -11.32518 | -43.62373 | 2025-08-30 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 211c9d6b-790d-36ac-b731-1429b4e9f8c4 | -9.57898 | -54.47062 | 2025-08-30 04:21:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44f039b4-21d0-3f6b-9ee2-d1da08c95668 | -12.00928 | -43.99306 | 2025-08-30 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a66f7be-aef0-36f3-8d8f-766d9e4c865c | -12.93147 | -48.12098 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f44d957-ee11-39bb-a89b-4ce2a5d471cf | -11.83416 | -51.49061 | 2025-08-30 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5dfead91-bbac-3f75-bf74-420d56a3a5c1 | -14.61912 | -48.08059 | 2025-08-30 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 230c55ba-25ae-3ec5-9b6c-48b515997a33 | -11.84205 | -46.38244 | 2025-08-30 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 922f6ac1-6418-366d-adea-60b9056347da | -12.7181 | -48.2011 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dfb5f19b-cafb-3d88-8746-c421b1f309fe | -11.15641 | -47.14288 | 2025-08-30 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79741081-7515-3bd0-8de3-d9974797edee | -12.84623 | -48.12614 | 2025-08-30 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3457fa73-7eac-3d96-8789-fc98aad80f32 | -13.55385 | -43.59196 | 2025-08-30 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d2f046c-7469-3544-9ffd-8a63eba7f818 | -13.54478 | -46.95159 | 2025-08-30 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README37.md)
