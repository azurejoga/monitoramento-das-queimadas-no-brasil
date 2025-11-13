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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d81a5fed-cf27-36e4-af03-0d1f1bafe317 | -9.35068 | -46.59078 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 523aa2d7-f6ed-3c9f-820d-a171f34ff3b1 | -8.86493 | -50.19442 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5df4f25-e8f7-3794-a24d-39dabca8c410 | -9.44566 | -44.87458 | 2025-11-13 04:44:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10058b54-963b-3dd3-90f9-bb15672d3c8d | -12.41696 | -54.48573 | 2025-11-13 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb27bccc-fe19-304f-9ff7-fdb391747a43 | -9.63409 | -44.54561 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d7cdbf3-f438-3bfd-b562-33d353bff8e1 | -8.74528 | -44.23678 | 2025-11-13 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c812728d-b978-3d83-91f7-28b50f962998 | -10.92963 | -44.61354 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0de3da59-9418-354c-a1d7-ccef230f436e | -8.94716 | -49.82499 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a98f6abe-101e-3510-8f64-190e9bac4b88 | -8.71654 | -44.25686 | 2025-11-13 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0f01cc4-5ca8-3a2f-8470-0cf909bb60cb | -8.94439 | -49.82097 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5869af98-d00e-3290-8ccb-963d0debc894 | -9.64249 | -44.54694 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e9f8113b-1068-37ca-97c9-bb7ff6862dfc | -9.34573 | -46.59895 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f084061f-e8ec-3836-93dc-f68529e10551 | -9.32838 | -47.83746 | 2025-11-13 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a1142cb-c7bc-3b53-b4fe-3c46a65c7d63 | -10.82068 | -44.65645 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 340e33c4-7e4e-3501-8028-e93148396df3 | -12.59811 | -48.33562 | 2025-11-13 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f6caa3b-b7fc-34a3-9732-5aa3a8807af2 | -12.65255 | -46.74398 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| b5ca6dbf-e1b9-39b7-92ae-a60b1daabbb6 | -13.33241 | -43.17602 | 2025-11-13 04:44:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 819f92ce-5504-36a2-8f51-b68a6387f7f4 | -8.40957 | -48.05395 | 2025-11-13 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 97df0b01-c722-3ecf-a756-99deff1209aa | -14.0996 | -43.46585 | 2025-11-13 04:44:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fef29b7-b80c-3e10-862f-98fbb68fbe5f | -9.22576 | -45.21976 | 2025-11-13 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0be1080b-d625-39e6-9a1b-58cbbaa17f79 | -15.01636 | -46.68104 | 2025-11-13 04:44:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e575728-5dba-37b8-be29-9df0386575d5 | -10.92319 | -44.62903 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db75097a-37a6-3808-8ec1-856cba11a3fd | -10.53317 | -47.99039 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a2ec19b-1326-3841-b3c2-4560a110bab6 | -13.02644 | -46.53181 | 2025-11-13 04:44:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53832d66-6417-3027-948a-8025883cf386 | -10.55246 | -44.82829 | 2025-11-13 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ff0044c-495c-346d-981b-fbf1c48ce999 | -10.55192 | -44.8321 | 2025-11-13 04:44:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d7d36cb-bc1f-3ddd-8889-1a3289377871 | -13.33171 | -43.18148 | 2025-11-13 04:44:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59b1dddb-bf85-37ac-b1f0-d7bdee6b8f64 | -8.71718 | -44.25851 | 2025-11-13 04:44:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d014ff7-8427-3b1d-affd-5d788153473b | -8.20843 | -47.88631 | 2025-11-13 04:44:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ccc2016-2309-3d8f-9f17-107a8771fc31 | -12.66202 | -46.74727 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 271dc3b4-b69f-3039-8463-ac59d1765b8b | -10.92423 | -44.62962 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 061bb7ad-7107-3744-a446-a90d2f9bd113 | -14.94873 | -42.36898 | 2025-11-13 04:44:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| de174438-9c49-319f-9291-3fe97cb0adc3 | -12.99893 | -49.79337 | 2025-11-13 04:44:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4083236c-91b9-34e4-96b3-dd1de1ef6d99 | -10.62535 | -45.24313 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c5fa84a-3609-3e2d-af6f-25798ce12178 | -10.53666 | -47.99096 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3da5437-fa74-34e7-b524-1c45bd3d1e2f | -10.37411 | -45.0579 | 2025-11-13 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e955e41c-a60f-3af6-829f-d54254cb1bab | -9.01373 | -45.43309 | 2025-11-13 04:44:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9fe47626-b4fc-3d27-b1d8-79bb18ebf658 | -9.34636 | -46.59459 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1539b7f4-9c4b-3b78-8155-8b5a0f2d954c | -12.43558 | -43.75287 | 2025-11-13 04:44:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce8d2212-6baa-352b-8d01-8df3743edaf3 | -12.65186 | -46.74876 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f9a7e1ab-7a73-3a81-b148-7b097659dca7 | -15.39559 | -43.06499 | 2025-11-13 04:44:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 340e9f4f-b65c-3d59-acb2-618feeba2ce3 | -9.64192 | -44.55083 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 707733d0-c5bd-393e-bbca-26314ab81974 | -9.35005 | -46.59518 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8554a686-bacb-32c8-bc87-8287ba5d653a | -12.0625 | -48.20979 | 2025-11-13 04:44:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfb16419-5274-3592-a95e-c53941c2a874 | -14.10026 | -43.4605 | 2025-11-13 04:44:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b660a7b7-a7b2-3d31-9e41-94c549b739fb | -9.34942 | -46.59954 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c668b6c9-86a2-31fa-96eb-6f90922bb6e2 | -8.31009 | -43.64175 | 2025-11-13 04:44:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9e10936-5bfb-359a-9bb2-7d3141ff0bb1 | -12.4119 | -45.79441 | 2025-11-13 04:44:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c9316bd-6598-3b43-b5c3-a96e3784d857 | -10.62483 | -45.24675 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4756c90-eb87-3ba4-829a-bb6b0c2c331d | -15.39485 | -43.07096 | 2025-11-13 04:44:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 473fa4ee-3d9c-3b70-96fd-68c3f9505e51 | -9.85807 | -44.57409 | 2025-11-13 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 524ebfe0-ea79-3ba8-8efd-6a960a491f57 | -8.53832 | -49.58471 | 2025-11-13 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da1a9a7f-75bc-301f-8e39-e083bc771b23 | -12.66584 | -46.74785 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 898b4d38-92c2-33e8-91fe-7f3aac245ca7 | -10.62505 | -45.24248 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f80c1793-7de3-3ff0-81a8-6cc151617c61 | -9.24658 | -47.83006 | 2025-11-13 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b601012f-37b4-3383-a2a8-838c5e2ef575 | -12.64804 | -46.74821 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 729d7ed9-b41f-367f-9d3a-4b6744b3bac2 | -11.09959 | -54.09288 | 2025-11-13 04:44:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80762a06-0ab3-37be-82a5-4c05f64956f0 | -15.29667 | -43.89706 | 2025-11-13 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fc21d42a-8f05-3abd-828b-ae79f2bdc52a | -9.34372 | -46.59615 | 2025-11-13 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 3e2b487b-68f3-3b83-8ddd-899349e6774f | -6.97161 | -52.87073 | 2025-11-13 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89c44b71-d5e3-3c10-a8c3-b33de7c60a88 | -14.99138 | -42.41513 | 2025-11-13 04:44:00 | NPP-375D | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9656a425-cadc-3e75-b8cd-f9ca4d2a3b0e | -10.93017 | -44.60949 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65488ca7-69cb-3c1d-96af-a02293a428c2 | -8.72899 | -49.59736 | 2025-11-13 04:44:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85dae0b6-ad0a-3474-a052-f8e544a87328 | -10.92709 | -44.60952 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 557f2c1a-2a69-339b-83c9-a7e70edfae58 | -9.10657 | -50.05776 | 2025-11-13 04:44:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 469d9e6d-826d-37da-aed5-7d9846875f28 | -10.9248 | -44.6256 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6e04820-871b-3738-b4a0-e9d2e317e76c | -8.94106 | -49.82045 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7316a211-8323-33f3-ae21-6e5a84eb1137 | -9.62823 | -44.55651 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fcb7df79-34de-3023-a0ef-fa57dfefcce5 | -9.94249 | -44.49445 | 2025-11-13 04:44:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91c943f1-1ed3-35f2-8298-a35c94fb2adf | -9.63353 | -44.54948 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b00daeb0-d017-3ad2-a96e-90160243851f | -9.64295 | -44.54588 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ade67ef3-69c7-3350-b5c2-ea9d4ae5d859 | -12.6588 | -46.75466 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 4d2889a7-1538-3c88-81ca-df701066b575 | -8.27076 | -48.00717 | 2025-11-13 04:44:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eadf0eee-f604-3e2c-afae-5c12b15bf4e0 | -12.6633 | -46.75047 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 86841744-71a9-39fc-9c9e-675ea11771b4 | -10.88629 | -44.39943 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c654e41d-d0ab-31cd-a054-1142eebd065d | -12.41771 | -54.48125 | 2025-11-13 04:44:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b851cb53-7238-3abb-9f76-90f4a7e889a2 | -9.64242 | -44.54979 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6297efc-56ac-36b3-88f9-5d56f5273e2c | -9.22666 | -45.22104 | 2025-11-13 04:44:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d748f1e2-b563-39a2-be62-8a3cad61f7b0 | -12.66781 | -46.74628 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4f9507be-cd27-3542-bac2-8836b9f45bf5 | -13.0023 | -49.79391 | 2025-11-13 04:44:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0401303-10f8-30d3-93ce-0d558b34e05f | -12.99949 | -49.78973 | 2025-11-13 04:44:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73b4b51a-8cad-34f0-b4d8-1060bb0276fc | -15.29605 | -43.89975 | 2025-11-13 04:44:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9509c6d-2134-3747-92b6-0dd99cd90462 | -9.85768 | -44.57503 | 2025-11-13 04:44:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 393a4e6d-197a-38b0-affc-ae1cbcc2ea22 | -12.64873 | -46.74343 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0e911c6a-a271-3567-835c-304cc0281d34 | -9.63298 | -44.55335 | 2025-11-13 04:44:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9b8788ce-5b28-34eb-ae0c-7290fec6bdec | -10.29051 | -44.95053 | 2025-11-13 04:44:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30162113-f09a-3c21-b485-4b95a5778056 | -8.86756 | -49.94105 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 72a1ef2f-ee58-35ca-ac7d-f16d7887746e | -12.1101 | -43.64354 | 2025-11-13 04:44:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 14f76478-80e3-3b91-bcdb-2d000c310f02 | -10.68772 | -45.00129 | 2025-11-13 04:44:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a2be5459-d7a9-37e9-bfc3-6a11f8507cec | -12.5987 | -48.33164 | 2025-11-13 04:44:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49af1f2c-8b37-3941-aa26-f28d736c33f8 | -11.9087 | -43.8273 | 2025-11-13 04:44:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b2a738ba-a382-3657-a7fe-7ed20c4aeed0 | -10.9421 | -48.00091 | 2025-11-13 04:44:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f9630a2-6c60-38c6-a7cf-f25dfccf62f2 | -9.32779 | -47.84135 | 2025-11-13 04:44:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d08ac016-acbf-3daa-8df5-aadf55439aae | -12.664 | -46.7457 | 2025-11-13 04:44:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 53cc619a-5258-3b28-84ae-4d0c6f5be367 | -11.00648 | -49.04453 | 2025-11-13 04:44:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ed6645d-31da-3400-8326-bed86d40114c | -10.17601 | -44.78732 | 2025-11-13 04:44:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d775f41d-633f-38de-81d2-958a33e30108 | -8.25318 | -44.37228 | 2025-11-13 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2fdeb13-1e0c-337b-81c9-f94b6e7dd97b | -12.43815 | -43.75605 | 2025-11-13 04:44:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d17ab68f-fdce-3b71-9ef7-438fe645c230 | -13.13105 | -43.79205 | 2025-11-13 04:44:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa2cc480-f052-3e72-b6ec-736da48b6e22 | -8.86424 | -49.94052 | 2025-11-13 04:44:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
