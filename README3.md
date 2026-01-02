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
| 49490cb5-6020-31f9-beb6-551808427cb4 | -8.17392 | -34.98154 | 2026-01-02 04:06:00 | NPP-375D | JABOATÃO DOS GUARARAPES | PERNAMBUCO | Brasil | 2607901 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cec43f4f-457b-3c5f-8d3b-e2ea60bfc3c1 | -5.28535 | -35.75523 | 2026-01-02 04:06:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2c28e5dc-c0e2-345d-81db-a1ffed34e874 | -4.51099 | -43.68894 | 2026-01-02 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbdb8b2c-7773-3b66-969f-13b45aafc04e | -5.28777 | -35.76511 | 2026-01-02 04:06:00 | NPP-375D | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c7fd5710-4fc8-3ac5-b708-711ce150b5b3 | -7.46295 | -35.1964 | 2026-01-02 04:06:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 9285dd2e-6774-34c4-818b-1d3d8122168e | -5.4731 | -45.41463 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64aad3cb-7c01-38e0-8cdb-961c6bf449f0 | -5.74397 | -35.37734 | 2026-01-02 04:06:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 23.9 |
| 6fc68fd8-e59e-3fb2-814a-4037d7ff4950 | -5.26221 | -37.60909 | 2026-01-02 04:06:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 2712ea0d-3a4e-352d-9fcb-9494105ebe32 | -3.52771 | -43.67281 | 2026-01-02 04:06:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2adc8349-0586-3fa8-80a9-0c1c80e8569c | -6.72934 | -39.27518 | 2026-01-02 04:06:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e0ae2ff4-4a02-3427-8b9f-3b4c81b78153 | -5.74362 | -35.38068 | 2026-01-02 04:06:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 12.6 |
| a9f94156-2faa-30c7-b6df-9c64ce519db6 | -5.72393 | -45.0371 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 173858df-afb7-3699-b9aa-c0acc6f094ae | -6.59732 | -38.37591 | 2026-01-02 04:06:00 | NPP-375D | SÃO JOÃO DO RIO DO PEIXE | PARAÍBA | Brasil | 2500700 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 327d0a70-77f2-335c-b70d-9475afe693d1 | -2.39986 | -44.93624 | 2026-01-02 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4a4f89a-4225-367f-8917-c6d3c41c8918 | -3.33079 | -39.99576 | 2026-01-02 04:06:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| df2b4b80-25f8-35b3-95a5-d1eb89861065 | -4.51024 | -43.69357 | 2026-01-02 04:06:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa545844-fec9-3bb5-88e1-3aabc8c43e66 | -5.28396 | -35.76451 | 2026-01-02 04:06:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 76a4c227-f1b1-3e25-aa3b-8cc0a70c56e7 | -5.28847 | -35.76047 | 2026-01-02 04:06:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6b38e612-e257-3517-973f-d6fd9d307894 | -3.43764 | -41.0249 | 2026-01-02 04:06:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| aa63e298-eddf-3a2b-925d-68659741e8d9 | -4.81295 | -38.42973 | 2026-01-02 04:06:00 | NPP-375D | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 975ee107-73ca-3004-94fb-eb52ed991c92 | -4.77098 | -37.82752 | 2026-01-02 04:06:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e0136da2-9907-35ac-aad8-4a6b56c98f5e | -6.08496 | -37.4069 | 2026-01-02 04:06:00 | NPP-375D | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1aba0172-4c85-3984-a4b5-73a8571a917f | -5.72335 | -45.04068 | 2026-01-02 04:06:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c496342e-123f-3f70-af56-3ba63ea85773 | -6.45313 | -39.97205 | 2026-01-02 04:06:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a3858450-0fa3-370b-a08e-3e89ff738bc1 | -4.39526 | -40.43231 | 2026-01-02 04:06:00 | NPP-375D | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d8c323ce-20b5-34a0-aa87-44181af4d917 | -3.07219 | -44.95618 | 2026-01-02 04:06:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b03500f2-96ae-3370-bb93-48e82ac415ad | -7.68967 | -35.2883 | 2026-01-02 04:06:00 | NPP-375D | VICÊNCIA | PERNAMBUCO | Brasil | 2616308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8428a571-de75-34d8-8693-a4b98af1d3b0 | -8.69774 | -38.64154 | 2026-01-02 04:06:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 211f6ffe-394d-3d4e-a6e8-145e0adb75b2 | -3.06797 | -44.95549 | 2026-01-02 04:06:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cdb94e8c-1e7e-3131-937e-1e3eb07acbb3 | -6.08451 | -37.4065 | 2026-01-02 04:06:00 | NPP-375D | MESSIAS TARGINO | RIO GRANDE DO NORTE | Brasil | 2407609 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b2fec56f-5651-3f67-902d-4675fac6e2c6 | -3.6632 | -44.81658 | 2026-01-02 04:06:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f0c4eae-5a90-3161-9807-c62a41985dbe | -8.7006 | -38.64582 | 2026-01-02 04:06:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ab36668a-e73a-323d-a1f1-18317a5eabdf | -6.29178 | -39.60396 | 2026-01-02 04:06:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6a8edde8-c937-3c65-89b8-6c36815e6a8b | -7.45428 | -35.1988 | 2026-01-02 04:06:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b00af9c7-dca5-3d0d-9615-facb000083df | -5.55208 | -39.38205 | 2026-01-02 04:06:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ef5e0d4f-4ae2-305a-a21f-7b0929fb8517 | -3.52005 | -43.62263 | 2026-01-02 04:06:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5dff143-61bf-3be6-ba03-2039eef8788c | -6.0242 | -44.54978 | 2026-01-02 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c112bdff-1f39-3524-8dcc-05c7f7e4430e | -6.74383 | -39.27019 | 2026-01-02 04:06:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd9a3abe-4053-363e-9105-81aa262f616d | -15.71676 | -46.65116 | 2026-01-02 04:08:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dac4a77-176e-3db0-9e9e-dabe1317701c | -14.50381 | -52.55832 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7d46b2ef-b167-3380-a965-11c8648660fd | -14.49811 | -52.55692 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 865f38a7-8186-36f3-a147-a3b460ffc991 | -14.49644 | -52.56522 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| eaab1e5c-42b8-3bac-b9b7-999435779792 | -14.49728 | -52.56106 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cf928bce-bc5f-3fdf-9694-695d5a35e05a | -10.23264 | -36.33963 | 2026-01-02 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 4e1e335d-21c9-3e77-ad43-0adbae7ecb33 | -12.94954 | -41.18318 | 2026-01-02 04:08:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef7f363f-55b3-37dd-b2cf-cb92cbbc4d93 | -14.45005 | -45.50156 | 2026-01-02 04:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8db12800-0728-3d56-8a32-a240c5f1ca3a | -10.22911 | -36.34237 | 2026-01-02 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 23f99fbd-a848-3d2c-babf-7ce413576180 | -9.5813 | -44.59633 | 2026-01-02 04:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bcf3eee8-1c2c-34df-830d-fc7bc82a2e17 | -10.23305 | -36.34293 | 2026-01-02 04:08:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 382ecf6b-66b8-3985-92f1-ad6550863d8d | -12.69609 | -39.73666 | 2026-01-02 04:08:00 | NPP-375D | ITATIM | BAHIA | Brasil | 2916856 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb1cc53b-dd03-34c3-be6e-92a91f351cd6 | -12.82814 | -38.24401 | 2026-01-02 04:08:00 | NPP-375D | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3aa1f086-c933-3078-8847-06aca591636b | -14.49738 | -52.56361 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| a8161f9d-ce83-3cbf-91bd-5f5126e8dafa | -10.40325 | -36.87654 | 2026-01-02 04:08:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f8d1d335-3460-3ca0-842a-c799477bee7c | -12.95287 | -41.18372 | 2026-01-02 04:08:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0582539c-5de3-3c55-a818-5c4e6d409fc7 | -15.6048 | -42.65873 | 2026-01-02 04:08:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7816a75c-d3f5-39b1-b78f-578e6056c76f | -15.30017 | -43.86404 | 2026-01-02 04:08:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e13d9a2-b74f-3d8b-aa62-1a694f040d57 | -10.77282 | -44.33373 | 2026-01-02 04:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da69ed17-cf62-32c7-bc62-0216b065555d | -14.49824 | -52.55948 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 63851721-269f-38d3-8ba6-e338a3e7ad8b | -14.50393 | -52.56087 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1ef6c53a-74b8-321a-8e79-ce9b2d209663 | -10.54662 | -44.69212 | 2026-01-02 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c15e35d3-f2ff-38d8-947c-000637820cff | -10.54998 | -44.68934 | 2026-01-02 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b764a56d-42b7-34a6-aef2-f4dfc13d67ba | -14.4991 | -52.55534 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e8372a75-c26f-3a4c-9f6e-ad5d54b16335 | -10.09707 | -36.45304 | 2026-01-02 04:08:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf862073-5c84-3cc2-82f6-af72565897ac | -10.54626 | -44.68869 | 2026-01-02 04:08:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d63afd13-7467-3da0-92ae-8f851063fc05 | -15.73386 | -41.34786 | 2026-01-02 04:08:00 | NPP-375D | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 003dda0b-b4d3-3f91-9650-7c5eb91c0427 | -11.9614 | -44.21009 | 2026-01-02 04:08:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d4fdc1b-231d-3043-8b62-c8ce78846930 | -9.57238 | -44.6021 | 2026-01-02 04:08:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 89007e5c-c451-35e4-8318-c077fe36a0e1 | -14.50299 | -52.56243 | 2026-01-02 04:08:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 115a212e-ec61-3fab-be02-7f0bee5773f4 | -11.74935 | -43.64455 | 2026-01-02 04:08:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6b0c1b4-1e16-36ef-ad10-ebc227f888aa | -15.50984 | -52.29282 | 2026-01-02 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9148e3d-6539-3013-9d04-10de476537fb | -17.05767 | -41.24279 | 2026-01-02 04:10:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 4a51bd6b-745f-3a84-8c62-892f88f8a7ac | -19.69395 | -42.69793 | 2026-01-02 04:10:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f7d1a2d3-e187-3d7f-b529-6541c545fb45 | -19.70063 | -42.69905 | 2026-01-02 04:10:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 42c8020b-45d8-38cc-b8f5-f2ee51f024c5 | -21.69453 | -41.98869 | 2026-01-02 04:10:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ab16ee8-68c0-3afc-8c9f-5dc71cca8171 | -18.2266 | -42.65069 | 2026-01-02 04:10:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 12de69cc-d5ab-3dc8-bfaa-6549fb92ebca | -18.48297 | -39.86712 | 2026-01-02 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d5ffd28c-f853-3187-b75b-3c3d29619135 | -17.06182 | -41.23913 | 2026-01-02 04:10:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| b2d56cf2-0de4-3570-9a89-03e60c486342 | -15.51059 | -52.28913 | 2026-01-02 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fb3aa234-2609-3aee-956a-b2458ea61f25 | -18.48655 | -39.86771 | 2026-01-02 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 907eb5c6-9faa-36e5-997d-9e63c6a42639 | -17.06126 | -41.24291 | 2026-01-02 04:10:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| c6a195ad-6679-36e6-8767-40cb9f14c3d7 | -19.7012 | -42.69534 | 2026-01-02 04:10:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 678a1698-28a0-33f4-80a3-0914aed1a0e5 | -19.69787 | -42.69478 | 2026-01-02 04:10:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4feb9255-f40c-3319-ac22-02a3b440d76d | -19.69729 | -42.69849 | 2026-01-02 04:10:00 | NPP-375D | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2763f86c-26e2-383d-9145-85ef6290fe8b | -15.50835 | -52.29092 | 2026-01-02 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab8f8af2-6b90-3106-9559-8f4b4f6b58d0 | -18.22328 | -42.65012 | 2026-01-02 04:10:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 136d36c5-6c66-3180-9ebc-4df1c9b4c003 | -17.05825 | -41.23902 | 2026-01-02 04:10:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 31f2b40e-b365-3638-8972-80d38b5d13a8 | -17.06164 | -41.23952 | 2026-01-02 04:10:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 48e6eec5-501e-3529-a2e8-0dee69355291 | -18.48595 | -39.87197 | 2026-01-02 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8d2d9433-cb63-3bc3-9922-065fa375de07 | -17.06106 | -41.2433 | 2026-01-02 04:10:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fd1a56a5-5e61-3656-932e-6a587d7c5937 | -18.48716 | -39.86343 | 2026-01-02 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9c650d1a-1c22-3ba5-b3d3-4a9adebb2701 | -15.50912 | -52.28722 | 2026-01-02 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 226d18c1-b076-320a-afbf-3b96623c7a09 | -15.51387 | -52.29216 | 2026-01-02 04:10:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d42b507d-cf41-32d6-b5e1-0f47128ba05c | -3.304 | -50.37024 | 2026-01-02 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a65fd3b8-affc-3961-a239-8df05634e163 | -6.29501 | -39.60331 | 2026-01-02 04:25:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a366347e-2679-3606-a2ca-1e94c0d4a46b | -0.0856 | -51.27833 | 2026-01-02 04:25:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8ed72e8c-ba21-3df3-9154-03379ddfa1a7 | -6.29436 | -39.60217 | 2026-01-02 04:25:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 414a55b4-b315-32a7-8d36-e22e0f586185 | -2.07896 | -47.87661 | 2026-01-02 04:25:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| be1c3975-bd93-3b10-8d86-4560eba05b9b | -0.81585 | -48.76762 | 2026-01-02 04:25:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f306960-c35c-3de5-84ef-59c0d3a9a1d2 | -5.93416 | -43.39886 | 2026-01-02 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b78af03d-c6d5-36ec-ba9d-7575bbcfc074 | -5.47326 | -45.4155 | 2026-01-02 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
