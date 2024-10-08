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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c25b038c-e6c4-30be-b6dd-a7ede2d92e6c | -20.4081 | -48.790699 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 23d9fc7c-0635-3079-b035-7287d6c6b5c6 | -20.4097 | -48.798 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3c0250f5-132b-38b9-8244-c3fba871cda5 | -20.411301 | -48.805302 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| fb2625c2-bc81-39b2-ba41-423b751acb21 | -20.412901 | -48.812599 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| be9753ac-e4b3-39cc-872b-01ea4afd345d | -20.414499 | -48.819901 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 95a1cf32-135b-3199-a335-dbb5317cf3af | -20.3951 | -48.7785 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f101f555-2f18-3983-b3d7-a542f42da6e8 | -20.3967 | -48.785801 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| eaa66123-9617-38b5-be36-4fcf09e42edd | -20.3983 | -48.793098 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4a011ebe-89e6-3746-bf6b-85a8a231e608 | -20.3999 | -48.8004 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0208efe5-18ff-37a9-b803-057ae0c50a0d | -20.401501 | -48.807701 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 072e4953-01db-3265-b4de-9e5ef869b016 | -20.403099 | -48.814999 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 77d59f89-d457-35f7-8fff-252fd76bbe2c | -20.404699 | -48.8223 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 53d64108-933e-33a7-a09c-de51169bb29b | -20.3853 | -48.780899 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6c745644-75dd-3268-87b7-b390278415fa | -20.3869 | -48.7882 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 891146a8-2841-38cf-8ac4-7cd9c7138653 | -20.3885 | -48.795502 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 74ef2819-d132-3bed-b16f-323c75da6cf6 | -20.3901 | -48.802799 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9898bbab-4669-3c4c-999b-edeada6ba5ac | -20.391701 | -48.810101 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cb26e72a-2cf2-31b2-96ab-c4049cb17fb9 | -20.393299 | -48.817299 | 2024-10-08 00:58:10 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7c03e94b-3f06-377c-90a6-075e3f4a2e4d | -20.3755 | -48.783298 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 90b0ab86-6295-3cc3-8579-15b2f54b7cb1 | -20.3771 | -48.7906 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d58fc9f4-6f36-36d7-93e4-2f627bf2ef36 | -20.3787 | -48.797901 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 54a9f68b-2f73-3979-a917-74a1fa2e6464 | -20.380301 | -48.805199 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9c56b5-f5a0-3d26-89eb-f129fe795adb | -20.381901 | -48.8125 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2d5c9729-dcd1-37c3-8b0f-911eac6187c9 | -20.383499 | -48.819698 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b385c6d7-01bd-3ac4-8885-5686168fa9f3 | -20.365801 | -48.785599 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 801f8356-a6f8-3480-8030-d5439e1eeaa8 | -20.367399 | -48.7929 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9d8da64f-79f5-39f5-8cbc-34287ed04f0e | -20.368999 | -48.800201 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 274d97dc-42cd-389c-9b7e-67d02f1c0e07 | -20.3706 | -48.807499 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 02beaaaf-c0b6-3790-9504-63918b13b238 | -20.3722 | -48.8148 | 2024-10-08 00:58:10 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 31df2787-a2ac-34ba-82f8-64317aeed13b | -20.357599 | -48.7953 | 2024-10-08 00:58:11 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d10270b3-6b70-397f-8108-aa33e6a6a82c | -20.3592 | -48.802601 | 2024-10-08 00:58:11 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 75c42bac-4882-3021-9534-c419dc232060 | -20.3608 | -48.809898 | 2024-10-08 00:58:11 | METOP-C | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bc01bba3-5be2-333f-a4bb-38db7276d3a9 | -21.341801 | -54.6301 | 2024-10-08 00:58:14 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 66371c74-3d36-3e0f-a084-385316846c90 | -21.332001 | -54.632 | 2024-10-08 00:58:14 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1b4eaa9a-2042-3903-b544-f8c199bc4911 | -19.813 | -47.384499 | 2024-10-08 00:58:14 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a97f5060-22ff-3b0a-9cc0-633955d55c0d | -21.3969 | -55.6637 | 2024-10-08 00:58:16 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 58c7b6cb-3851-3f24-9bdc-02a83c5b37f4 | -21.387199 | -55.665501 | 2024-10-08 00:58:16 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a1a8e222-29b4-30e9-80aa-842c7a84a040 | -21.389799 | -55.680302 | 2024-10-08 00:58:16 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f9ab3ad3-1256-368b-b2d8-5fe84f3ad6ec | -19.267599 | -46.1147 | 2024-10-08 00:58:18 | METOP-C | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 220eede0-002d-348d-bd08-3e79e455ebac | -19.2696 | -46.123001 | 2024-10-08 00:58:18 | METOP-C | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5e8f5057-e4e6-328f-981c-69a5c950b34a | -21.4261 | -57.228699 | 2024-10-08 00:58:20 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2f69bb3a-51fa-30ed-a009-b29b1fc55fb6 | -21.3969 | -57.234001 | 2024-10-08 00:58:20 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cb809510-3ce1-3676-9814-adccbbfa59f3 | -20.1355 | -50.970299 | 2024-10-08 00:58:22 | METOP-C | RUBINÉIA | SÃO PAULO | Brasil | 3544509 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f957ebc1-8d80-344e-b752-d938b3212d9f | -20.7899 | -54.820999 | 2024-10-08 00:58:23 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b0584d2c-098f-342c-8fac-ad0f1929fc28 | -20.7922 | -54.833698 | 2024-10-08 00:58:23 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e688c066-5d21-3b58-8780-22e9d05bdc6d | -20.780199 | -54.823002 | 2024-10-08 00:58:24 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc62877-c034-3ab3-8232-953df046ea61 | -20.782499 | -54.835701 | 2024-10-08 00:58:24 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b1ed6e0d-b3a2-3ceb-9aa8-e422ae4b5912 | -19.5509 | -49.4814 | 2024-10-08 00:58:26 | METOP-C | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5d0991af-b0fe-3fe3-b278-7f484765e2d0 | -19.5525 | -49.488701 | 2024-10-08 00:58:26 | METOP-C | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| da9f00f0-2c3c-3759-a21b-8c2302a00f75 | -19.5541 | -49.495998 | 2024-10-08 00:58:26 | METOP-C | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 746c6080-b2bc-3c8b-941e-eeb3aa8bd444 | -18.099501 | -45.055 | 2024-10-08 00:58:33 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ab5aab4b-7fec-3b59-8f5b-3fbfc54dde01 | -18.101801 | -45.064602 | 2024-10-08 00:58:33 | METOP-C | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 14cfc5a6-f3c3-37b5-a432-ae651ab28cc3 | -17.652201 | -43.8853 | 2024-10-08 00:58:35 | METOP-C | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1ae86295-341f-382b-bf78-0de526365892 | -19.4018 | -51.679298 | 2024-10-08 00:58:36 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ee403b7b-4e8e-3371-83ab-e26de5d3a5ec | -19.3937 | -51.6898 | 2024-10-08 00:58:36 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 496a5ce7-2d3d-32d6-83af-c9f820571d19 | -19.395399 | -51.698101 | 2024-10-08 00:58:36 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a2f45f0f-6d88-3470-b913-a712f29671a9 | -19.384001 | -51.692001 | 2024-10-08 00:58:36 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cffa77ae-d29c-3329-b2a0-19bdcbb478d3 | -19.3857 | -51.700298 | 2024-10-08 00:58:36 | METOP-C | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 293016e4-9e06-354a-9dec-32d2b237a603 | -19.005199 | -50.236401 | 2024-10-08 00:58:38 | METOP-C | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ed28743a-55e4-3bee-a80c-5498287b6de5 | -19.0068 | -50.243801 | 2024-10-08 00:58:38 | METOP-C | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 172cfd26-0ae3-3bf6-a04d-ac1f0d1aef36 | -20.067101 | -55.9548 | 2024-10-08 00:58:39 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0a036259-7d26-3316-895f-893387505845 | -18.1709 | -48.511101 | 2024-10-08 00:58:45 | METOP-C | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3f115685-45c0-30bb-9c5f-20f2d564d3a7 | -18.172501 | -48.518398 | 2024-10-08 00:58:45 | METOP-C | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa8f444c-7fcf-3746-b445-ce3ebca9f830 | -18.1742 | -48.5256 | 2024-10-08 00:58:45 | METOP-C | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fc136e3e-98cb-3c0f-abbd-7b43936452cf | -19.5839 | -56.519299 | 2024-10-08 00:58:48 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 93007f60-98b7-3817-9c5c-13568069aed3 | -18.553101 | -52.627701 | 2024-10-08 00:58:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7af66533-645e-3a0f-a826-23f681f05737 | -18.554899 | -52.6366 | 2024-10-08 00:58:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 390482f6-d9b8-31d3-8dff-ed29de49932e | -18.5434 | -52.629902 | 2024-10-08 00:58:53 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a094b075-4ab6-3817-9469-697c1a1e343f | -18.9219 | -54.539799 | 2024-10-08 00:58:53 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| aff5b12a-4878-3483-ae2d-3b98416bf301 | -18.924101 | -54.551201 | 2024-10-08 00:58:53 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e559caff-0b42-3e08-b6af-9dec820071fb | -18.8946 | -54.450901 | 2024-10-08 00:58:53 | METOP-C | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c1482bbb-0265-3dab-9fa6-ed28899e676f | -18.896799 | -54.4622 | 2024-10-08 00:58:53 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2ed10c58-26ba-3e7f-9328-fb40152e04bd | -18.899 | -54.473499 | 2024-10-08 00:58:53 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| beb047e8-29cd-31ac-b027-6e674b6aa391 | -18.914301 | -54.553299 | 2024-10-08 00:58:53 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 393f5753-7876-32c4-9e15-701df06f8f4e | -18.8892 | -54.475498 | 2024-10-08 00:58:54 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c12386ae-ccf1-3df9-873e-0e4f937aacbe | -18.9023 | -54.5438 | 2024-10-08 00:58:54 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| be0ec92d-821f-3cda-8d09-6d8f6f4631c7 | -18.904499 | -54.555302 | 2024-10-08 00:58:54 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f95ec789-4190-3025-9c12-c9ee2a604cb7 | -18.9067 | -54.566799 | 2024-10-08 00:58:54 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 16c3ab28-9ec4-3a3c-a0cf-77e17b1e252d | -18.896999 | -54.568802 | 2024-10-08 00:58:54 | METOP-C | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ff89e358-2961-3338-b27c-3af671dc439e | -18.4916 | -53.4356 | 2024-10-08 00:58:57 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 173d169b-09b8-3b25-ae59-3fa962fe5d80 | -18.4818 | -53.437599 | 2024-10-08 00:58:57 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3f0061dc-67f2-3491-aa17-f50e86a4679b | -18.4837 | -53.4473 | 2024-10-08 00:58:57 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2339a54a-840d-3b54-baf4-20eae9134cbc | -18.479799 | -53.478699 | 2024-10-08 00:58:57 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 10db08cd-e8e5-363b-991f-b38aa27d9c1a | -18.481701 | -53.488499 | 2024-10-08 00:58:57 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 334b8844-cbd3-32d3-bc04-f3e19480bcf9 | -18.4837 | -53.498299 | 2024-10-08 00:58:57 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 709846df-0eec-3255-b61a-d0c9934bf5c9 | -17.5823 | -50.452202 | 2024-10-08 00:59:01 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c8cf77e7-9beb-3237-832b-2c3c18f63056 | -17.5839 | -50.459599 | 2024-10-08 00:59:01 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 312d8f49-f763-3ced-ad92-249ef6ab3b96 | -17.585501 | -50.4669 | 2024-10-08 00:59:01 | METOP-C | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ee8c992e-c97c-3d13-81d9-cc46a102472e | -16.5889 | -46.469101 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 03c4d2e9-dc93-3846-9ca9-9308321d416a | -16.5909 | -46.4776 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f7ebfa7e-9275-3156-b54a-4dd8c329ae57 | -16.592899 | -46.486 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1ee9db9-9d9f-3cb3-a99f-2de15f3b96d4 | -16.594999 | -46.4944 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e5c35fd2-e844-3287-ab3e-5cfb735d2cbc | -16.5811 | -46.480099 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7e15c27-f2d2-30f6-b8ca-353d30fd2373 | -16.583099 | -46.488499 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1c9d170f-5b6e-3d15-b503-12a90fb7510f | -16.5494 | -46.434299 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 21c63a8b-c948-300f-9154-383f30411362 | -16.5515 | -46.442699 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 849cb62a-b6f1-3b53-9da6-1df15360ba0a | -16.5555 | -46.459702 | 2024-10-08 00:59:03 | METOP-C | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07b0d05b-7600-336e-b0d6-b1222465d445 | -18.211901 | -54.4422 | 2024-10-08 00:59:05 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4e56ed7e-306a-3323-9002-bcf35d00b700 | -18.2141 | -54.4533 | 2024-10-08 00:59:05 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a7643039-b270-30fa-9193-3d8be634dd30 | -18.202101 | -54.444302 | 2024-10-08 00:59:05 | METOP-C | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README16.md)
