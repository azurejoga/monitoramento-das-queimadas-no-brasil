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
| fcbfdab7-5586-3c26-b81b-8a3b65efeb53 | -10.80267 | -50.75933 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbe84413-a6ff-385c-b498-515e0474503a | -10.3777 | -48.91529 | 2026-09-21 04:21:00 | NOAA-20 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e0dc544c-9b2d-3443-a74a-c9732ca6e7dd | -9.8215 | -48.43238 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 575905b6-6579-3d17-ae4f-d41ddf5ec59e | -10.41952 | -50.24241 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| 6bf66ce1-c36a-3fec-bd69-3baeb48d064f | -9.66386 | -54.33295 | 2026-09-21 04:21:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 967bfad3-6b17-35c2-8bae-7c1488e5ccec | -10.7996 | -50.77676 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dcde0b98-6632-3ad3-80f2-40efa9980d31 | -12.66491 | -47.01995 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15e11879-db6b-3089-b33d-8a1356d6362a | -9.92842 | -45.27152 | 2026-09-21 04:21:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2752a55-a3fa-3a73-a4ee-6ceed9bb6ec7 | -15.45758 | -48.47221 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0dde6fed-a2f5-329f-b35a-470b29dbf05c | -10.87951 | -53.97574 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e5bd4ec-1344-3972-a462-d81d33ca00c5 | -11.67868 | -43.42337 | 2026-09-21 04:21:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2df184c9-cda0-3189-9110-eb404dedcf48 | -10.87944 | -54.09918 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6494b1f-7b1d-3556-aa3d-9a3cdd64318f | -9.84498 | -48.34253 | 2026-09-21 04:21:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fae0a978-330b-3379-a7a9-1228bddc0903 | -12.63093 | -50.91794 | 2026-09-21 04:21:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1f112c3-5288-3934-8110-bf1ea176b96f | -10.5366 | -57.44739 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 02f18d8b-fea6-3737-9da7-ef1be2b6fd9b | -11.41004 | -47.3372 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b720e04-0d5f-317b-b2d5-b15e9a63c772 | -15.47106 | -48.40314 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78ce3e4d-49e2-3f92-9b0e-1011c8ca504c | -11.27177 | -54.13232 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d1253d-5ab0-3f92-b2bc-edfd580dfaa2 | -11.79755 | -51.11396 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 34ddbb58-1654-35c2-b249-d77206835ed1 | -13.93259 | -47.84497 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af1b4277-7628-3cad-baa1-f418781ac65a | -14.22873 | -44.63623 | 2026-09-21 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41c78c52-6eae-3f25-b02a-8ac5557eeab4 | -11.43607 | -47.29152 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 682f6d9c-11b2-381e-9099-30520be4da75 | -16.04808 | -52.53583 | 2026-09-21 04:21:00 | NOAA-20 | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f834ce4f-e6a3-3f28-8edf-9985171c6103 | -16.10588 | -49.81312 | 2026-09-21 04:21:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf93a6a9-2785-370f-832c-8073922bc895 | -16.18481 | -51.11996 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97f62b95-6c12-32ae-99b4-cd43d0fe1b6f | -10.11298 | -48.43884 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fba9fd9-db28-336e-912e-f2b81abdcab9 | -15.45461 | -48.47845 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f6da6f5b-5022-37d5-9777-8535996fd64c | -9.95329 | -45.72227 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7fde0bb-8289-30c0-bb02-7dfddd4ba722 | -11.05291 | -54.90413 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f4b54508-8bdb-3b3e-9b89-aaf690d999d4 | -14.78586 | -48.52793 | 2026-09-21 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99edfaae-990e-3269-a87b-f9fd90f37f9e | -16.74757 | -47.61446 | 2026-09-21 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9c460f0a-b6b8-3dbc-9cc6-3c155dbaa477 | -11.43968 | -45.4053 | 2026-09-21 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db4cb636-344a-3d97-a554-d45e7a48e0ed | -14.0289 | -52.08105 | 2026-09-21 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a5fe617-97d0-305b-a836-ab58166a7593 | -9.9487 | -45.72907 | 2026-09-21 04:21:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 71a7eae9-8ab0-30a0-aad6-59326a090b7b | -12.82611 | -54.05418 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e3926f87-73f8-31ad-a3d0-8404366dde5f | -15.16188 | -48.17094 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 58080b6a-f2dc-32a8-9dcf-b59d93edc900 | -13.9333 | -47.84088 | 2026-09-21 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1f62b99-4541-39de-8634-cce1264c97ca | -11.84695 | -46.89708 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 039503b9-cb42-34e0-ad8b-278647cce275 | -12.02605 | -47.81369 | 2026-09-21 04:21:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86875104-e0b5-3aef-8d51-54f652a9f73e | -11.02766 | -48.33246 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 36266fba-4040-3b04-8186-f16b3486deec | -11.79393 | -51.10869 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 836d9304-f7dd-3630-97c7-36fafe5d3a81 | -10.75376 | -50.80428 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| aba46957-f693-3616-81e5-4b7bbae3d743 | -8.17515 | -54.76847 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae09d01d-e293-304c-bfb1-eb5aa46d354c | -11.04397 | -54.91925 | 2026-09-21 04:21:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c11ac64b-38c6-342a-a196-41e243ddb828 | -10.86413 | -57.16532 | 2026-09-21 04:21:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4992a051-e6d3-38f2-87b0-df95bb6218ea | -11.04518 | -47.6688 | 2026-09-21 04:21:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bae3fe3e-7e6a-3656-b6e2-6a7c348980dd | -10.48341 | -51.28434 | 2026-09-21 04:21:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5bf08a0a-0d1f-3372-9b7a-99cf331caf7e | -12.19142 | -47.04663 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2895f5fe-bd6f-34df-afec-6213cd46744e | -11.0276 | -48.33538 | 2026-09-21 04:21:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bf8450d-3dbe-307a-85cd-b85db3261336 | -11.16492 | -54.12463 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 827ba6f3-d9a8-3419-8584-b79b936156ae | -10.462 | -50.29171 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| beb5bd16-d4da-3ab8-861c-fe0923dd73e1 | -12.66143 | -47.01948 | 2026-09-21 04:21:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d2e450f0-3fde-350a-818f-0be920cc8516 | -11.80197 | -51.11482 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 47852b34-45b6-3c8b-8360-c98ed38522ba | -10.42874 | -50.2652 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f2a6261-649f-3c89-8aaa-0bf12bc2b63b | -15.44753 | -48.4551 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4f6f38cc-40cf-30c6-8d8c-2737e6ada800 | -13.59424 | -51.46592 | 2026-09-21 04:21:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac6f9a27-795a-3a96-a591-7bd0337b6daf | -15.51779 | -42.6557 | 2026-09-21 04:21:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e5334bac-5f6d-34e7-b3f2-1876d94bfbc7 | -10.88016 | -54.09547 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 57ddf0a5-6429-3d55-bb92-2cf880576d14 | -11.02851 | -54.15174 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7c40d97-cca1-38ae-94d0-c14e7fea5696 | -11.83415 | -47.61887 | 2026-09-21 04:21:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 40a1934b-751c-39d3-8e90-db404aad7b02 | -11.10011 | -48.29602 | 2026-09-21 04:21:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9df7b1f5-950d-3711-8b6f-85bf15a3e894 | -10.47204 | -50.28509 | 2026-09-21 04:21:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| a67cdb42-c675-368f-8d19-ad7c1c916dba | -8.18628 | -54.77524 | 2026-09-21 04:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bff1ec1-6cf5-3a91-8121-543de792cf2d | -12.80007 | -54.05306 | 2026-09-21 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a683c69e-79d7-3557-a1ba-bcdeb1944f2b | -10.15384 | -44.82426 | 2026-09-21 04:21:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7547329f-e46b-35ac-90c4-df761569cf9b | -10.48093 | -45.09143 | 2026-09-21 04:21:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df55bf91-2872-373e-8e22-130635cbcd7e | -7.57388 | -57.67358 | 2026-09-21 04:21:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6847fec3-a58f-377a-a217-b9d8f7a99b09 | -11.4747 | -47.76834 | 2026-09-21 04:21:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2080dd0b-c6aa-3066-baee-c79c64b98ea7 | -10.80126 | -50.84499 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db757d5b-3472-3362-bee6-0e8770a8ad6e | -11.84761 | -46.89317 | 2026-09-21 04:21:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8689fc56-ae48-3fae-a17b-66e32531b76e | -11.8744 | -49.01612 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a33b2a42-b7c9-301f-9748-66aed10e8803 | -11.41001 | -47.34222 | 2026-09-21 04:21:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5ad8bdd-7acf-3d60-8ccf-6f44cec72a25 | -11.04021 | -46.55732 | 2026-09-21 04:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec25e8dc-ed52-3feb-a91d-a8bdcf0d4bc4 | -12.1114 | -47.0456 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 568cebc7-6603-3966-9d38-381882b0e517 | -12.10792 | -47.04499 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3a373b7-585f-3be4-85e5-8d48600d7255 | -14.17237 | -51.79377 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d55ffbf-047e-34da-bcce-d645fb42dabf | -10.87397 | -54.09813 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54e41d3e-2184-3fa7-bd12-6d5a47444c9f | -15.16966 | -48.1681 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9eee3c12-abf5-395b-aa66-105bdd7c2be7 | -10.52968 | -54.50438 | 2026-09-21 04:21:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ceaebf-be80-3169-9d1d-58d368465738 | -14.62188 | -52.07408 | 2026-09-21 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a4463f5-8e0b-33f0-82ce-6fe92a3ba302 | -10.88564 | -54.09649 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02f7dacd-6e3a-37db-b6ab-a3cabf6c8141 | -10.88662 | -53.97417 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c95693f-1a89-3edb-97fd-619906179e17 | -11.1006 | -51.05967 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef5d2b60-99c0-36e1-ae04-fd9843b00506 | -12.54379 | -50.0751 | 2026-09-21 04:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 725a2d5d-c974-340b-b69e-e6a458016754 | -16.1012 | -49.81724 | 2026-09-21 04:21:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fb9389c-425e-37c8-8a57-338121378b41 | -13.28419 | -43.54854 | 2026-09-21 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 13451726-b845-306c-88de-7c673bd229d1 | -15.44824 | -48.45091 | 2026-09-21 04:21:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dcdd53f0-390d-3857-8d55-1ebd706bcbb8 | -12.18404 | -47.00489 | 2026-09-21 04:21:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69a4f367-f6c5-31ce-8862-23005940fdb5 | -10.7618 | -50.81031 | 2026-09-21 04:21:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5f763a6-fbe0-3115-8b0d-3f808559b71f | -16.19023 | -51.12868 | 2026-09-21 04:21:00 | NOAA-20 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 909e469b-628b-3e82-9a14-e5e7cbbc3b33 | -13.17605 | -43.56908 | 2026-09-21 04:21:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| fa477ead-2d65-3c92-8024-ee63eba67e93 | -12.76967 | -52.85107 | 2026-09-21 04:21:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 62fa23b6-4e53-33a1-8fd4-793ac21ebc0b | -11.89403 | -48.99437 | 2026-09-21 04:21:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2db33f3-063c-3bd6-846d-ef21586437dc | -11.8961 | -44.87061 | 2026-09-21 04:21:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2cc7d908-fedc-3329-bd6a-de70f32e0820 | -10.87271 | -54.07528 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25886d3c-ba38-39ab-a14e-0356c73e8c07 | -9.163 | -50.08078 | 2026-09-21 04:21:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8530bf8c-5536-34db-83c0-3c9ca75a0381 | -10.81549 | -50.14049 | 2026-09-21 04:21:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f404f80-140f-3148-aa12-dc0291e252b5 | -10.89998 | -54.08092 | 2026-09-21 04:21:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd59e922-0bbf-315f-9d9f-74f99b5abb30 | -14.66798 | -54.4771 | 2026-09-21 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8aae247-969c-3b37-ac61-bcd2f300123a | -11.33189 | -51.33956 | 2026-09-21 04:21:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README50.md)
