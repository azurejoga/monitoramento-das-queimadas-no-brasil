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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7d120d2-64e4-36fe-8d54-33aef0bff506 | -10.92519 | -47.90786 | 2026-09-15 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27f8e8a3-3fb2-3aa7-bf12-4db5ede991e8 | -13.6274 | -47.91667 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4abb56f8-72b5-3dae-912a-5047199c3015 | -10.93786 | -54.08742 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77bf4f2d-9389-398c-949a-7ce2f2b26eba | -8.46972 | -50.7732 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e957a548-ec90-311f-b134-393266035fd4 | -12.04932 | -49.40884 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b8b66cb-77e6-3cb1-8952-a92352368284 | -10.38369 | -46.64873 | 2026-09-15 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37e029dc-8f45-3f66-b02e-fd17c4ae2778 | -10.3036 | -45.30345 | 2026-09-15 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 188f1b91-4b2e-32f6-a073-3e0591bfe28c | -10.67328 | -54.14862 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bae49fa0-be8f-3649-b9a3-09bd928a1e45 | -13.40438 | -57.02423 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 974aed1f-ab72-3f8a-999e-a39f28737ee3 | -9.88539 | -47.78179 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1ace1f8-4c28-3d97-b71a-6a2e27be923a | -8.46822 | -46.86697 | 2026-09-15 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b3fb111-9981-3c57-b4de-f862f7576c6f | -9.8832 | -47.77424 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 91cf8148-69d1-3ec4-a5f5-f960b4a20ee2 | -7.93299 | -49.73394 | 2026-09-15 04:34:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a8196c7-6d09-3c0d-aecc-0c5112ac230a | -10.93694 | -54.08514 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e113fb38-9341-3040-bedf-60deebb9108e | -10.29702 | -54.17213 | 2026-09-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d45f3430-d059-3cf8-b5fd-a0c81b7f7b20 | -10.38647 | -46.65273 | 2026-09-15 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa9c5521-7ce9-3da6-9941-be4f74e437c8 | -13.56835 | -47.90315 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12009645-9a0b-3648-a25e-afbb164adcfa | -8.45664 | -46.87581 | 2026-09-15 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b70a32c0-d76e-3023-b725-37d871d90b39 | -8.50243 | -50.1445 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9c9e1de-6315-3357-95c4-46b0afd95b10 | -9.35995 | -50.19765 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f542da2-ab63-33b3-8667-90744ea2e09f | -13.57334 | -47.89308 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85eeb16a-3239-34e5-abf4-85ea1bd7b05d | -9.4207 | -47.86131 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae1916f2-a047-3dc3-afe8-f7003627ff74 | -9.35856 | -50.20593 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36625760-7614-30c1-b16e-2f8429a0d79c | -15.03187 | -48.52691 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed463c1b-8ccb-3bcc-9ad3-e18b4cf1904f | -9.87927 | -47.79878 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 388968f9-a1f7-31c7-a967-2ecbb1624a28 | -7.93232 | -49.738 | 2026-09-15 04:34:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b24a8f2-7aaa-394a-bcf8-1ed658b34c17 | -8.55859 | -44.49233 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab1b5e24-196a-3410-b555-7b99e94a3c11 | -9.35396 | -50.14573 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 078bed58-b344-3858-bba2-f7e6be84e49b | -12.72708 | -40.27898 | 2026-09-15 04:34:00 | NOAA-20 | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd49f91b-1422-315f-9635-d95a4fc3253e | -9.43455 | -49.54829 | 2026-09-15 04:34:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8185b5b6-ad87-350e-a428-aef953759d77 | -10.25481 | -57.70283 | 2026-09-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f796373-d32e-3116-a682-cf6fe6607283 | -11.333 | -46.78511 | 2026-09-15 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8504b086-4094-35f5-bb9d-47a1339acdd1 | -15.3508 | -48.09715 | 2026-09-15 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85f58d0f-8544-37d6-80bc-b51ee1d38855 | -12.47893 | -41.4049 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0ad48252-3755-3900-ad6e-1dce0d0ad202 | -8.46818 | -50.78259 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a55b0cc-5851-3df9-bd57-0a9499cc113c | -10.80244 | -46.20346 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c5dd1db-ee6a-35b4-a61d-2e373db93ddc | -11.26805 | -54.13271 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95b6087d-5f3e-3330-9a2d-a2b2d7b808a5 | -15.25142 | -40.99304 | 2026-09-15 04:34:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a737321c-b4d9-3f44-93dc-8d69521fc135 | -11.24053 | -43.46701 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04e0948a-0666-3791-9fc5-ee956efad45e | -9.876 | -47.77667 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 96a7a5dc-721a-39ac-807b-c58372c872a1 | -10.97716 | -48.32563 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7c8d5eaf-8e41-35ba-964f-831ea67ae83d | -14.17372 | -47.41743 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d378057-70a7-3369-a1ba-8713e8069a2b | -13.56947 | -47.89606 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5aa3008b-4d13-333b-aeaf-af44f03bdd95 | -8.59303 | -44.47771 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0de04376-335d-3575-a187-81f5c9a745c8 | -9.28409 | -49.783 | 2026-09-15 04:34:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7e3f0f9-6ce2-3307-bfda-475981f1209b | -8.40442 | -54.71947 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd1a23c4-e515-3a19-93c3-1d67c7723233 | -14.91285 | -44.67035 | 2026-09-15 04:34:00 | NOAA-20 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fc672d4-6b30-3a40-b09f-4081758ad8db | -8.50534 | -50.1493 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7171af3e-c107-37dd-b6b3-012558a2be4e | -8.08805 | -50.96957 | 2026-09-15 04:34:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a491f2d4-f443-3bc1-9937-7ad1bfbd9fa2 | -8.79576 | -45.90606 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c28a0d30-393e-30d5-a88d-95a0d08f5af6 | -11.24994 | -43.45179 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| feb2fedc-46c2-37dc-9c50-7f12f5e71a6b | -13.76468 | -48.80476 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9837ee63-72b6-3ca1-a4d1-e580275b33d9 | -13.29574 | -51.28348 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f151c38-4c97-39ea-b946-daf9af26550f | -10.50535 | -53.57077 | 2026-09-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5ff0492-86fa-3a03-ad42-8aa59b4d0103 | -13.77566 | -48.82147 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cadeece7-4414-3ff7-8c65-d32b737287b1 | -12.12116 | -57.18612 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4385ec84-e5d0-37cb-84f3-77d4b58ae309 | -11.24882 | -43.46341 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 42c2afde-7390-3c4a-90aa-c42c4bc9ec52 | -10.30072 | -45.29926 | 2026-09-15 04:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec575d5d-c6d3-32f1-b028-7bf2e7fe2491 | -11.19138 | -42.81656 | 2026-09-15 04:34:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8831d0b3-f095-32b5-81d9-8bc5fe7687ce | -11.24362 | -47.5501 | 2026-09-15 04:34:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2f5f7b3-c2a4-3d52-8996-d545560348f9 | -12.12545 | -44.21616 | 2026-09-15 04:34:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78e82c2b-44e1-3fcf-9e49-3a1c2929ea16 | -14.85685 | -48.15141 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02bd97ec-cf35-3c90-9e65-57ef683efa6a | -10.66152 | -54.13696 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8803e616-0688-3765-a7ef-5a632b5f95d6 | -13.29715 | -51.29686 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 692748d9-329a-375d-9806-e6535756677f | -13.29501 | -51.28773 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4e822996-ba68-36fc-9ab1-992763a454ed | -13.38533 | -57.03969 | 2026-09-15 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bda3f997-c8ff-39d2-9421-5b97128fdec9 | -6.68555 | -58.69361 | 2026-09-15 04:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb8e6f5a-e318-3668-bb6d-915303d95788 | -8.46578 | -50.77993 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a246ecb6-d620-3dd4-bdca-a907293b5a1b | -14.86185 | -48.14125 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8aaae547-aaf5-3627-a4c7-805f4ae6a89c | -8.79184 | -45.88718 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0346731b-7211-3821-88e6-a107238a6111 | -12.49382 | -41.42397 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ba6bb03a-5332-310c-acc7-c417bd9ec682 | -8.47263 | -46.86055 | 2026-09-15 04:34:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a107e1e-7c8f-3bb0-973f-876ba218e8fc | -13.29935 | -51.28412 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dab2ccd-b9d0-3f69-99c4-d639854a149e | -8.32793 | -49.99757 | 2026-09-15 04:34:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29d40d0b-ed2c-3a03-956f-b55075478dbe | -9.02131 | -47.7461 | 2026-09-15 04:34:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee0afe7f-10f4-36b2-bc0d-5ea18b859505 | -10.03325 | -52.10316 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96d12908-691d-33c6-ba3d-ef006a54d30f | -6.87914 | -59.63786 | 2026-09-15 04:34:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4192d535-c22d-3e83-b911-c2a693101e4b | -10.30234 | -54.16843 | 2026-09-15 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9adb7f24-d099-313d-b537-251868e8aaf3 | -10.9415 | -54.09277 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdce0c02-5792-344c-9cb5-a8e085cc486e | -10.65843 | -58.76918 | 2026-09-15 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 149ee48c-2510-34f9-958d-e801895e9353 | -8.35937 | -44.83194 | 2026-09-15 04:34:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ddd957b-bf31-3ac7-aef4-9bcc2361e125 | -12.49444 | -41.41918 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 00675903-c844-3a3b-9239-c0deb6d38268 | -13.78013 | -48.81483 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7359c61a-eaa8-318d-a695-c6e220b1c29a | -10.66597 | -54.13786 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 91a58b5e-642a-3d00-ae67-aa05b69ea90a | -15.06982 | -48.56634 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5eeada6f-4015-31d3-bee5-0b4714a2da6d | -10.42291 | -48.64519 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cffbb68-ecda-3365-a5cd-5ab07d880b74 | -10.42405 | -48.63817 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ecde74a-b54c-30c4-997c-34bdbfc9c135 | -9.88595 | -47.77828 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4023d67a-83e1-3747-8abf-e974eee18667 | -8.5405 | -54.69698 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 088b4f24-819c-3d0a-ab2a-895fe9ca0351 | -13.06631 | -48.60491 | 2026-09-15 04:34:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 842e0368-1a46-3eba-b203-3b232a2ab35e | -12.36508 | -46.93364 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a5640e4-9570-3217-ad57-1d53d627ef70 | -8.48458 | -44.5696 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2cb1ea0-2988-381f-b9a4-9bf003a6fb97 | -12.37043 | -48.13393 | 2026-09-15 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2f43f59-4ae0-3a48-807c-7d2c482d1787 | -11.50337 | -45.78838 | 2026-09-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45daf837-60e5-33d5-b3d8-f35c3865caa1 | -13.77623 | -48.81786 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b3b569f-0c06-300a-9fd6-13ddf4dcc03f | -8.48338 | -44.57734 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f439ac7a-f691-320e-8906-9d9274c7a3bf | -15.14701 | -49.58644 | 2026-09-15 04:34:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2e2c4d7-428c-32f8-84df-532bf1fb0e48 | -10.94055 | -54.09042 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 058051b3-d01b-3765-b7e7-3af56e950ace | -8.53507 | -54.70456 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af49e5c0-49ea-343d-956e-d7e7dd41347a | -11.80237 | -46.60285 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README43.md)
