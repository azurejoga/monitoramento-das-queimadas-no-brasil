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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa88b04a-5169-3d3e-b3c0-18ee5fad2f1e | -5.41398 | -44.31486 | 2026-06-06 04:21:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6653c04-246a-3094-83c4-1d50aabd77af | -5.73861 | -43.95893 | 2026-06-06 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a03af607-8b70-3e66-8234-27dc9a0ce3a6 | -5.813 | -43.78866 | 2026-06-06 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d636d6ba-7039-3d1b-8d02-a00f2b0fb132 | -5.92519 | -43.48226 | 2026-06-06 04:21:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fe400e2b-d00f-3f82-8a51-41624aa295e2 | -5.2336 | -45.55411 | 2026-06-06 04:21:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4c757a8-23a3-3464-a192-12763ee30585 | -4.17529 | -47.53165 | 2026-06-06 04:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea3ffce1-bf21-3d2d-9455-39f4dc3a52fa | -5.44415 | -44.81148 | 2026-06-06 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f974c0a0-2232-354b-9ae9-cd8d568a9e88 | -5.72424 | -45.03713 | 2026-06-06 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fe81cd7-bfc3-34b4-b4f2-79f6e65f637b | -5.44691 | -44.81545 | 2026-06-06 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55734f15-4dff-3d63-b1dc-dde4e5ccc527 | -3.98949 | -47.93216 | 2026-06-06 04:21:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bba6501e-9d6a-3b16-bda7-408b59e6e4bc | -5.55311 | -43.97224 | 2026-06-06 04:21:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f9ce884d-6845-37e5-bce1-64a57b26383a | -7.3347 | -37.42985 | 2026-06-06 04:21:00 | NOAA-20 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 18444915-6f64-3ee8-bd62-a2bfe7a2e6a9 | -5.80858 | -43.79512 | 2026-06-06 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b3a804f-f775-3ce5-8f78-61dfd6a26039 | -4.66518 | -40.55958 | 2026-06-06 04:21:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 030b112e-5b7e-302a-8080-b50551ed11df | -5.35093 | -45.18428 | 2026-06-06 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 46f15bfc-e971-3768-ba02-abea708061f7 | -5.30281 | -47.24047 | 2026-06-06 04:21:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71af0f13-5594-3e63-99bc-8c6dcb8c4ee6 | -5.80526 | -43.79459 | 2026-06-06 04:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2f4ce1a-8965-3e4c-8c51-526599a1cc0c | -7.33353 | -37.43239 | 2026-06-06 04:21:00 | NOAA-20 | IMACULADA | PARAÍBA | Brasil | 2506707 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d9a263fd-00b1-3c57-854a-194f2c099392 | -8.50503 | -47.20738 | 2026-06-06 04:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c85438a-e282-3030-aa3f-ef26f053e6df | -8.40634 | -46.86633 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a2b6f2f-3c21-33cc-bda6-8975f81976dd | -12.0611 | -48.07438 | 2026-06-06 04:23:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 51941097-f6b2-3324-bee8-53660ab5071d | -8.92762 | -45.68243 | 2026-06-06 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 661a23ba-776b-370d-98fc-f77f469051b2 | -11.12238 | -45.13995 | 2026-06-06 04:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b9a063d-8d21-3343-8ca7-b01b48c9b4ad | -12.00558 | -45.3535 | 2026-06-06 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e628ad1-2919-3c5f-8780-75978b3904bb | -9.08511 | -50.60832 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c4a0084c-af4f-360f-b7c6-6d774176105c | -8.45394 | -47.00322 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ef95127-9aba-30ee-bd86-0571474a699c | -9.37307 | -50.53878 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c81dc74-9f68-30e6-a3c4-5b53ae6b6db0 | -9.08447 | -50.61196 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2834da30-194b-3345-8380-dfdb90724792 | -6.11591 | -48.56419 | 2026-06-06 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df9a944c-5451-34a3-b74e-1fc381fc9cda | -10.7471 | -43.66562 | 2026-06-06 04:23:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05db769e-e0a7-3dd6-87f2-fa8e4529c6b9 | -11.73575 | -47.44826 | 2026-06-06 04:23:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee69fe9e-5e0c-337c-9382-4a6e28b8a161 | -9.08856 | -50.61266 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35a69e72-06c6-3601-8bf3-a018d3f1078f | -11.07986 | -48.25947 | 2026-06-06 04:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2bf2583-c90e-3777-bd0c-af7d79c0a76d | -6.72679 | -44.37091 | 2026-06-06 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 31e7da1b-d446-3f69-b72c-e773e945612f | -8.13846 | -47.41004 | 2026-06-06 04:23:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95fea62c-d8bd-31db-8291-6e01e9b9fc08 | -9.9222 | -48.00336 | 2026-06-06 04:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86cce7e8-7968-354c-bf5b-b8b0207e62e2 | -9.08919 | -50.60903 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b88aae50-cbea-3ff0-af79-ef03eb850152 | -7.15865 | -44.06364 | 2026-06-06 04:23:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 486ce6ba-61d2-3da9-bb47-fea64526564d | -8.49035 | -47.38421 | 2026-06-06 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc44bdc7-579e-3f20-a279-96add8a775dd | -6.98591 | -42.87661 | 2026-06-06 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| d603f3af-a320-3508-b1dc-9bf9df0c163b | -11.07702 | -48.25496 | 2026-06-06 04:23:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9deaf4b4-c9ad-380e-ab80-f37b8a02a262 | -11.46828 | -47.98374 | 2026-06-06 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ace008d-0f3b-3e56-97ab-9b9cf2b95a06 | -6.98934 | -42.87713 | 2026-06-06 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 9e294f8f-7056-36cf-ad31-494e1e644688 | -9.09327 | -50.60976 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76c90fd7-3fab-39f7-bc89-716fb10516ec | -11.0425 | -44.32091 | 2026-06-06 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67a0e4eb-91bb-3cb9-9817-43b440b0e3a8 | -12.06515 | -48.42454 | 2026-06-06 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1efb6fc8-7de2-38cf-83e4-a278cc93defd | -8.46196 | -46.99688 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86c48c70-beb3-38fe-850b-9542777161ca | -11.03576 | -44.31986 | 2026-06-06 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cbb4d20-9850-39c4-874e-9d3aa4ad5c21 | -8.72467 | -47.83554 | 2026-06-06 04:23:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74311c5e-e869-36e9-8cfa-199ae6189b94 | -10.81133 | -44.3 | 2026-06-06 04:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 574f292f-97f6-3ca0-990e-990ccd7f715d | -8.93204 | -45.67598 | 2026-06-06 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46a7b06a-bf2c-383c-b4d5-e339b59b75b3 | -10.14521 | -48.07899 | 2026-06-06 04:23:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1bafd15e-a7db-3ffe-8e30-41247500ac7b | -6.85319 | -44.9686 | 2026-06-06 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b679f08-c454-32d2-ba49-5b1be4e36251 | -11.00588 | -54.31369 | 2026-06-06 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 419f1065-7294-338f-9cb7-f8d4d0189076 | -6.04274 | -47.89212 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b3e8f61-47cf-3606-b24d-5a8e216f8642 | -12.06236 | -45.98654 | 2026-06-06 04:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c51937fd-d464-37eb-828c-973b8e7629a4 | -12.06448 | -48.42847 | 2026-06-06 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bebff564-680d-3d31-992e-f023aa5b9a89 | -8.92818 | -45.67894 | 2026-06-06 04:23:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40b2640e-6171-3558-b56d-b4984fba3a07 | -6.98534 | -42.88034 | 2026-06-06 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2df14728-4b4d-3017-a470-e68a6a0d6e75 | -9.92284 | -47.99945 | 2026-06-06 04:23:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c376fe51-0c0c-30c6-9808-64838a63acdc | -7.2026 | -47.10459 | 2026-06-06 04:23:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf091e39-5888-3d1a-a4ac-0aeceab31535 | -8.45795 | -47.00006 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fe5cbf4-50e4-322f-802d-e19a10629ef7 | -8.86886 | -50.19125 | 2026-06-06 04:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df9aa4f4-aa41-3016-9e48-ce916b7264c5 | -9.0939 | -50.60614 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 875c6c60-95dd-3a11-a3d7-90a3967e0add | -12.06348 | -45.97951 | 2026-06-06 04:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2fe6bbe-895f-3f55-8cf0-ffed33bd3657 | -9.07351 | -50.60249 | 2026-06-06 04:23:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9c10cc24-9d13-3a68-af45-8bfbd530ebec | -7.23995 | -49.66898 | 2026-06-06 04:23:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edd1eee8-99c1-3abf-af56-5a25469d2a8b | -9.90199 | -47.48291 | 2026-06-06 04:23:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d5498de-5f8a-30f9-bed9-c2734864e926 | -8.46477 | -47.00117 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71a0c934-4d6e-35da-acf6-b893c56ee81b | -6.04563 | -47.89412 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 218c1e7e-4d77-3d1c-af52-c2d954ca75e9 | -6.4361 | -44.576 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1330802d-051e-306a-a816-04235b0766a4 | -9.16984 | -58.06475 | 2026-06-06 04:23:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8fb2131-d39e-34bf-9c6c-fa177c11247d | -6.84989 | -44.96808 | 2026-06-06 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eeccd00c-75cf-30eb-909a-3428dbfa4f6a | -8.45735 | -47.00378 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 059ddf1e-8df1-30ff-9c63-0b775e4a32c2 | -8.42193 | -46.89901 | 2026-06-06 04:23:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef61ced9-fc31-3678-839f-0c13d48b3a86 | -12.06863 | -48.42515 | 2026-06-06 04:23:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c2a4307a-1d2e-30ca-bec0-754a78a12a6b | -10.1417 | -48.07843 | 2026-06-06 04:23:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c4517a8-6e0e-328e-8b9a-1ffc4bf85b26 | -8.50564 | -47.20364 | 2026-06-06 04:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44e51e8d-3703-3580-a555-d3b58c8ff357 | -11.46852 | -47.98845 | 2026-06-06 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1ea1e830-daca-3608-8282-d8bd2124f2dc | -10.23869 | -46.51249 | 2026-06-06 04:23:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0ab7234-12db-3d06-96ff-559fa6874542 | -9.00039 | -47.43826 | 2026-06-06 04:23:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84a8d778-f501-30d5-9ac0-8bf06ebbf5ee | -8.5016 | -47.20681 | 2026-06-06 04:23:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60c8ea65-c22d-36ec-950f-eb7291edb6cb | -6.44821 | -44.56374 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e0ea0154-683f-3803-9878-1e2b1ff74525 | -6.44875 | -44.56028 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a7596a80-1ca2-3438-95a0-c78346c89bd4 | -6.99219 | -42.88139 | 2026-06-06 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 40693262-58e6-3901-ae40-48f1013fba92 | -6.96801 | -45.22835 | 2026-06-06 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05d7fb65-493f-3d1a-9869-84c669335ede | -7.64384 | -45.22996 | 2026-06-06 04:23:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6273a891-f229-308e-a620-abd013fbe89f | -7.00348 | -43.86321 | 2026-06-06 04:23:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 826edb7c-6efe-31a4-bccd-b970dbcc9e94 | -10.51922 | -42.37285 | 2026-06-06 04:23:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7e71e9e1-8697-3c7c-a247-3f8c53400ad1 | -6.82511 | -43.39445 | 2026-06-06 04:23:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 11f632bf-0099-3c2c-96f1-855a37464d3c | -6.042 | -47.89355 | 2026-06-06 04:23:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c7bd4d89-7e9c-36bb-8912-79d9d5c57af7 | -10.18411 | -52.64972 | 2026-06-06 04:23:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da920e89-543f-32b0-b28e-72a524560bf7 | -6.43334 | -44.57202 | 2026-06-06 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c5f1845-4d99-31fe-bef1-259d886012a6 | -9.13374 | -49.00114 | 2026-06-06 04:23:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b739237-35c7-365b-b77c-e118c9841fb5 | -12.06454 | -48.07498 | 2026-06-06 04:23:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e042770e-ff60-3c7f-9227-e1f70bd59920 | -6.84934 | -44.97153 | 2026-06-06 04:23:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd0ccfbc-72e6-32d4-b82b-18d13b77bc09 | -11.00964 | -54.31202 | 2026-06-06 04:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b675ce09-ebc2-351e-b3b5-5daac861076c | -12.30989 | -46.73677 | 2026-06-06 04:23:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f8ff91c-92bc-3dcb-b908-16ebe280271e | -12.06292 | -45.98302 | 2026-06-06 04:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f47d806-e79a-3c89-b665-158575d236de | -11.46764 | -47.98757 | 2026-06-06 04:23:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README7.md)
