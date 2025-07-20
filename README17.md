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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5cb1978-c367-384d-bad6-468407e86e0b | -20.09763 | -43.91212 | 2025-07-20 04:42:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3bc47196-4c49-3f46-ab8d-079c2949e625 | -22.91055 | -47.01957 | 2025-07-20 04:42:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7ae72145-f138-3441-91d2-60798fc51794 | -22.13668 | -43.19321 | 2025-07-20 04:42:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a1881086-a7c0-3543-8977-ad51fa318f4d | -19.39701 | -43.248 | 2025-07-20 04:42:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c47bd91d-d551-3b1b-b765-90505e853434 | -22.43465 | -45.47418 | 2025-07-20 04:42:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 60006bc8-2c27-305c-bc00-0abd9a97f692 | -23.09943 | -50.10335 | 2025-07-20 04:42:00 | NOAA-20 | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| becf3513-7304-357f-88dd-c7e3ff6126e3 | -22.13703 | -43.18965 | 2025-07-20 04:42:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| ae81fee2-4517-3024-9909-b72757317b87 | -19.39735 | -43.24474 | 2025-07-20 04:42:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| feac9da4-2fec-370f-9829-85f0fb189fab | -28.22764 | -50.66601 | 2025-07-20 04:44:00 | NOAA-20 | CAPÃO ALTO | SANTA CATARINA | Brasil | 4203253 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 18bc3f64-babf-3669-b880-8ed2d0d08cb5 | -23.33769 | -51.90498 | 2025-07-20 04:44:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| 01f09f49-7978-3751-b474-a6f0d55404c2 | -23.33827 | -51.90104 | 2025-07-20 04:44:00 | NOAA-20 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.8 |
| c7147799-5400-3386-b1c9-4d4d63487b02 | -10.688 | -46.7829 | 2025-07-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| a2833e0a-9d1c-38e3-ba99-2089d4ee8310 | -10.6496 | -46.8101 | 2025-07-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b2f101d7-fff4-3b45-9535-8fc0c118440c | -10.6499 | -46.7876 | 2025-07-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f7de5f9d-d38e-31c1-af00-97110afcf0f9 | -10.6686 | -46.8077 | 2025-07-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| b7f7d536-4213-3e9c-944f-0692d2d26d24 | -10.6689 | -46.7853 | 2025-07-20 04:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| a24dcb8e-87a2-375b-86c2-28d8e82c7bfc | -4.07406 | -48.03534 | 2025-07-20 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a3329742-511f-3ebb-9824-bf64eb503f0d | -4.07794 | -48.03458 | 2025-07-20 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9c7e81a-340d-3fc5-b950-a7f276805313 | -3.31466 | -49.0458 | 2025-07-20 05:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d744769d-4815-306e-aafd-c6ef1cf48614 | -2.90718 | -48.24555 | 2025-07-20 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4b818a0d-fe57-3a76-b382-5f9bba435641 | -4.07703 | -48.04114 | 2025-07-20 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd9132e5-879b-3bb8-90e1-dab8ed796a3b | -3.034 | -47.86957 | 2025-07-20 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5d03b219-1e1b-3899-a0d6-c2a0cbbff13c | -3.03886 | -47.8648 | 2025-07-20 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| ac2267ae-9ee6-3d87-8d10-c180e4cc4af5 | -2.91503 | -48.24026 | 2025-07-20 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6b64b3f5-e850-3c44-9a5b-142f8deabd52 | -4.07609 | -48.04797 | 2025-07-20 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1b7b103c-2c4c-322b-86f1-583b4a1b6bc1 | -3.03496 | -47.86313 | 2025-07-20 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c74404be-10fc-33c6-8ac6-4321ea042282 | -4.08017 | -48.04328 | 2025-07-20 05:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| f7f7a415-e538-33e3-811a-6766f6d0a854 | -4.25353 | -48.54742 | 2025-07-20 05:27:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 91614312-589b-3172-a755-fc34ca9b78b6 | -3.04203 | -47.86432 | 2025-07-20 05:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| dfa3544d-b2b7-38c4-8649-6de2c5c25050 | -2.9141 | -48.24668 | 2025-07-20 05:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| dc67a87b-4335-3284-8242-b1cab849365c | -9.02252 | -59.76407 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eeba187f-94a9-36b4-8178-138b9bb2c348 | -9.34493 | -58.83427 | 2025-07-20 05:29:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d38203b4-52ae-39eb-90f7-07a080a43f43 | -9.01411 | -59.77117 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07f90e81-cf16-30a7-964b-529746a65474 | -9.19524 | -59.68814 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 693b0862-36b0-30ba-99d3-9223bc3b504a | -5.68553 | -57.95482 | 2025-07-20 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4268faf2-4c7d-3faa-a7ea-2c08471be5ab | -10.67966 | -49.675 | 2025-07-20 05:29:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7d993f3b-3a1b-3830-8383-2a752062bb17 | -8.97627 | -61.51207 | 2025-07-20 05:29:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4020b7e9-3dab-3ad0-b604-6c3538893734 | -9.91357 | -55.52665 | 2025-07-20 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0a295bb-097d-3eaa-b9ae-3856fd80bfc1 | -9.01444 | -59.54234 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38136c5f-6633-3798-a299-8be280fd2e15 | -7.26796 | -60.11676 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 27269608-1cca-3a6b-86a2-4ba62c409b61 | -10.68073 | -49.67848 | 2025-07-20 05:29:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07f9462d-9938-30d0-8141-948734111637 | -7.26448 | -60.11625 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cbbb71a6-a3a9-3b93-a9ec-147f0bd441e2 | -9.02191 | -59.76821 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e198e43-7003-31dc-ad9c-31c98b843de5 | -7.26987 | -60.11605 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75614c79-7bb1-391a-b0e8-f77f84dc10ce | -5.08963 | -48.42178 | 2025-07-20 05:29:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 999aba10-d6fc-3a7e-987d-9072e246b466 | -6.78589 | -58.62909 | 2025-07-20 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec352215-cb78-396d-a65f-4062e2b01847 | -5.00343 | -56.29321 | 2025-07-20 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c593d0e1-29bc-3e83-972f-c877810e1b9f | -7.26041 | -60.11959 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e296634-2ac4-3a60-9c55-85e3d41544ab | -8.30862 | -55.11338 | 2025-07-20 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c66a774c-ff16-364b-90ef-b9229f49dc59 | -9.0187 | -59.53862 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cb1eed3-2fc0-37f7-a521-82db7fe08578 | -7.261 | -60.11574 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 201f8d01-da91-323e-a9bb-38a08102dc71 | -9.01569 | -59.53379 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 93f050df-3b2a-37db-b909-9fccb27e0f67 | -8.31001 | -55.10286 | 2025-07-20 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b74e2b4-84a6-396e-acf9-b901dbaf7f18 | -9.02067 | -61.2211 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4f5150a-d1a3-38f3-842c-2acd269b4b89 | -5.32671 | -55.94446 | 2025-07-20 05:29:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a2981d5-384c-38f7-9d12-0a2565fb5124 | -7.26389 | -60.12011 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| edbbc77c-3431-3cd9-a4f1-0220eb507dd6 | -9.01472 | -59.76709 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20bf713d-858c-35ce-b361-6c61b15c447e | -7.25925 | -60.12719 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b61d1a4-c4f3-3450-9f40-0be751ada4e0 | -7.26639 | -60.11554 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bb11f28-bf42-3f37-b507-bc306f346ee9 | -7.84265 | -63.2484 | 2025-07-20 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1225f6a8-8804-3d69-9c5f-5e0458c3a132 | -9.91289 | -55.53184 | 2025-07-20 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1dc82b1-fc0f-3766-89d1-3471ace81465 | -7.2693 | -60.11993 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d97f0eab-3036-3700-ba70-45506f5baeff | -8.94777 | -62.22686 | 2025-07-20 05:29:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36dcfefe-ea3c-3929-9bc6-049355f1f9f7 | -9.47428 | -57.83494 | 2025-07-20 05:29:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| af992040-fbc9-39e3-9bc7-fe62a5c49a10 | -8.97346 | -61.50795 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4e2cc512-d98a-33d3-8c1f-ceb177d1c3ed | -9.19463 | -59.69236 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7f05c1e2-387a-398c-8368-8bccf8d2c540 | -5.09462 | -48.42033 | 2025-07-20 05:29:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60528bbf-712c-3fdf-89e9-99d7fd88ab93 | -7.26272 | -60.12773 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70133987-0805-355f-8416-1a30a8959632 | -8.07792 | -50.10236 | 2025-07-20 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ee15b9b-f388-3144-aa05-d36947b91f40 | -8.08794 | -50.11419 | 2025-07-20 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15b35b0c-cd5f-3efc-9963-d972dbca72d8 | -8.97291 | -61.51155 | 2025-07-20 05:29:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cf850a43-4008-3e2e-a834-e0e7b1cda20d | -7.26737 | -60.12062 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cc447c4b-d0e7-3cb1-941a-1c13213a1828 | -7.26855 | -60.11288 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bcd09ed4-dba9-3a8b-a326-17a8f9ab2fbd | -5.08868 | -48.42852 | 2025-07-20 05:29:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 4abea215-8a3e-33aa-80db-327a246818ce | -5.91895 | -61.30166 | 2025-07-20 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 388cedb9-b244-36a1-b5d2-55a42369b502 | -8.30868 | -55.11276 | 2025-07-20 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5fbef836-f3eb-37c7-b47c-7bdf0e02cd72 | -8.97236 | -61.51514 | 2025-07-20 05:29:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03375af4-2b5c-37fe-af45-85eb2c739f4c | -7.25983 | -60.1234 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7a7b393b-8ae1-3684-beb2-21d3c596da62 | -8.0887 | -50.10783 | 2025-07-20 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0038e750-fec9-33c2-885c-bb326fa7e89b | -7.26582 | -60.11942 | 2025-07-20 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e63d1567-8662-3bee-88c4-4dc32222a159 | -9.01204 | -59.53324 | 2025-07-20 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f73f6cb1-faec-30cb-bc16-83b24dcb23fb | -5.0937 | -48.42714 | 2025-07-20 05:29:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d28b70a3-daeb-32e8-abf4-4cc70d7e18b5 | -8.31015 | -55.10225 | 2025-07-20 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 25c338ab-5d6d-3830-9530-14eb005c1c70 | -9.33598 | -58.84249 | 2025-07-20 05:29:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d39c4201-7457-3665-b82e-e795f7ea6d5b | -8.07862 | -50.09687 | 2025-07-20 05:29:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c47b259e-4333-3db9-b48e-6d014395354f | -6.896 | -45.38 | 2025-07-20 05:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 370d6d84-5550-387b-abb9-2241ac9b4678 | -6.9148 | -45.3784 | 2025-07-20 05:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 061cd3df-fe4e-3d91-98e8-c75785f7ff13 | -10.04207 | -64.90015 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d6dae55d-57dc-3754-8698-b1f8ba2475e6 | -12.02219 | -63.75139 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe993087-d765-3e9e-ac43-47a4cb3d45ae | -12.03522 | -63.7786 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92e29738-4d68-3d0c-ac17-cc177dead238 | -8.17078 | -70.03201 | 2025-07-20 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 896ac9ac-1eb6-33b4-864e-07765bb2e9c9 | -10.87689 | -56.09356 | 2025-07-20 05:31:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 83e2a7b5-5d9c-39c5-bf2b-65e755da3df8 | -10.38011 | -62.76928 | 2025-07-20 05:31:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 53409dd7-3bda-3483-b9d0-51f2758d7dcb | -14.16949 | -58.17702 | 2025-07-20 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74998589-22a3-33d0-8417-05f9675b1eb7 | -12.04184 | -63.77967 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4cd7b4b6-aa87-3a04-a13e-03754668fd6e | -12.36062 | -50.32237 | 2025-07-20 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb5d278a-e03c-35a5-9903-09f3582a3c57 | -12.02384 | -63.74086 | 2025-07-20 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ff6478e-9ce3-37bf-b3b9-86640346f929 | -14.14892 | -58.20301 | 2025-07-20 05:31:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 547ade08-f1ba-36c4-8633-52bb83ee8bc1 | -10.05767 | -64.9981 | 2025-07-20 05:31:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eafa94ba-7033-3bb4-b16d-b842afe4f0e1 | -9.78447 | -62.48814 | 2025-07-20 05:31:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README18.md)
