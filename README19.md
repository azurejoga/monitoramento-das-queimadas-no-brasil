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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91fa4164-d3d8-3371-90af-e19f98c77ce0 | -11.06752 | -55.38038 | 2025-06-26 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5c8b98d7-8ab2-3810-b902-9e747ad78b14 | -11.1445 | -53.93639 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 807b5055-bf2d-3ab3-9bef-8a14b23dade1 | -11.91638 | -54.80991 | 2025-06-26 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d49a71f8-3a4e-357e-a265-7b78706a64c2 | -11.60963 | -46.50628 | 2025-06-26 05:08:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13febd23-4ce3-3af8-862c-b044b4d72619 | -11.83686 | -51.26106 | 2025-06-26 05:08:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ed7116d7-c24f-38cd-982a-16a51b90f1ac | -16.30191 | -53.82849 | 2025-06-26 05:08:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c99dcc20-4f8e-3299-9a43-f589080165e5 | -10.86712 | -53.78226 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8da67d3c-b32b-3a44-83a4-6e40b0669eaa | -10.82562 | -53.73055 | 2025-06-26 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3279507-724b-3544-b058-078bb51d847b | -10.06797 | -55.55292 | 2025-06-26 05:08:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c24895e-8951-3ff2-9f10-023593bb5c74 | -11.80282 | -47.54364 | 2025-06-26 05:08:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| debae84b-7332-3d20-be01-4a8c99cee243 | -11.56624 | -52.09698 | 2025-06-26 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90c5db89-6712-3e4b-bc5c-289c6af0a413 | -9.1213 | -49.4313 | 2025-06-26 05:10:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| bc0b4000-2103-35c7-8a0b-62537a41fe4e | -20.89662 | -56.4715 | 2025-06-26 05:10:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93909a7e-29cd-360a-9c01-6208c2f448a3 | -21.1883 | -48.68921 | 2025-06-26 05:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 98152250-1331-3575-b02f-82812bcf94c8 | -20.78348 | -54.48602 | 2025-06-26 05:10:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dbdea52-cc01-31b7-95bd-9ab23eb55543 | -18.09601 | -54.28346 | 2025-06-26 05:10:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e17c1753-1bb0-3f63-a957-5c21bb5a8717 | -21.18987 | -48.68639 | 2025-06-26 05:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2de4f1e3-6611-3da8-a1f8-782982130de6 | -18.09335 | -54.28616 | 2025-06-26 05:10:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 810d2f11-7cdc-323d-b7a8-e9ca08a78e80 | -18.09284 | -54.27795 | 2025-06-26 05:10:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6156e01-d692-3592-b5be-52310c5fabd9 | -18.09403 | -54.2812 | 2025-06-26 05:10:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dedef04a-d9f7-3840-b503-2a57a72f6aed | -20.95044 | -56.59464 | 2025-06-26 05:10:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3018226-d614-3326-8890-2f765ee5b13d | -21.19403 | -48.68962 | 2025-06-26 05:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3a215fa2-b307-3add-85e5-4fff87339381 | -21.18949 | -48.69056 | 2025-06-26 05:10:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 4ba2de58-fc81-3db8-9f8a-3f7465de2308 | -19.0657 | -52.45717 | 2025-06-26 05:10:00 | NPP-375D | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2af89faa-0dc7-3e6a-9a2d-b7d873973503 | -9.1213 | -49.4313 | 2025-06-26 05:20:00 | GOES-19 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| d6ec7a43-5604-355b-b13b-0a3924c4308f | -4.71137 | -55.99161 | 2025-06-26 05:27:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7d69c97-cd61-3012-89c7-69b38f3ee65f | -9.50822 | -56.09642 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d3151f48-fb9c-31f3-beab-367dba67e9f0 | -3.88375 | -54.21342 | 2025-06-26 05:27:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 764edded-01d8-36a3-a534-81448d75da7a | -9.11343 | -49.43256 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c3a0bf3b-4f33-3cbf-8990-65c2dbbd5fa8 | -8.97066 | -49.86784 | 2025-06-26 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8913b670-27f7-316b-964a-a3d4d05b20cd | -9.11865 | -49.4537 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 9bdaa688-ca22-3fbe-9d50-0bef48cca96c | -7.89182 | -61.47378 | 2025-06-26 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79dc5d17-335d-35aa-8857-403a5be4908e | -9.49465 | -56.09438 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| cc10ce78-6184-3338-95a2-2422cb613ceb | -9.1211 | -49.43405 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 9b64fc41-3316-3cc4-844b-7fcff18330b2 | -9.29064 | -56.24474 | 2025-06-26 05:27:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f31b7222-c0ce-3bac-aa18-3e89d7d35871 | -9.11958 | -49.44024 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 50680f0b-7584-3d60-802a-18d94f6286c5 | -4.27732 | -48.18495 | 2025-06-26 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4fd5f15-0f69-3fc7-9b20-455b4ce8f7ac | -9.11336 | -49.43957 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a2830fd1-b412-3cd6-83df-ec2b6f385132 | -8.67527 | -49.95018 | 2025-06-26 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fc8f2186-ddfc-3dcd-a5e8-e7c1dfafa1b8 | -4.5291 | -48.04824 | 2025-06-26 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f2fad53-5b3f-32f2-ac92-35fe05b9f107 | -4.27028 | -48.184 | 2025-06-26 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9f4ad98-393b-35ac-8b40-408374efcc6c | -8.67449 | -49.95617 | 2025-06-26 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16651f68-a23a-373a-973f-8251d271a7f5 | -9.49981 | -56.09046 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 055ebae9-88de-3ee6-9523-e011dae74da7 | -9.11882 | -49.44672 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| aae3b8e1-d939-33d1-9fd8-df1d7651b1af | -9.47904 | -56.07351 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd3709bb-fd03-3f48-b2bc-9aa94899ff3a | -9.49918 | -56.09504 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2849b751-868c-37e3-8507-27e8cc4002ac | -9.12029 | -49.44057 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 70b9efdc-a071-3fd8-b789-47dda99c78d6 | -9.51212 | -56.10161 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a6200170-f4ce-34b6-a998-635a8908abcd | -7.90068 | -61.5215 | 2025-06-26 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8ce0832-5df2-3c4f-b4f6-1e94d61aa2f5 | -9.50307 | -56.10025 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba7bd0ae-09f3-3142-a1c1-7f2a1107bed8 | -9.51537 | -56.11139 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6a30a4fb-4807-36f3-8bf1-aa019cef2240 | -9.5037 | -56.09571 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2a16f0c5-4b46-3c2b-b5f5-f39408341f25 | -9.51601 | -56.10681 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7e298b0f-40d4-35b3-94ab-425782498a2c | -4.52804 | -48.00412 | 2025-06-26 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d96556af-cf61-3ecf-9dbe-22183d9d251d | -9.49855 | -56.09961 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1b851c72-189c-3905-bd67-270a2ef2bcca | -5.87054 | -50.15089 | 2025-06-26 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17c262e9-bba6-3a1e-9122-9ad94a7be7da | -7.92966 | -61.55497 | 2025-06-26 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ab6f0cd-55ce-3b97-9c85-8e105b7b3a4d | -9.51149 | -56.10612 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b9bbfe3d-efc6-3c91-a088-b6bfc9f6229f | -4.53508 | -48.00573 | 2025-06-26 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5dce2598-95a5-31d4-ba5f-f41b59e8e2a3 | -4.52817 | -48.05482 | 2025-06-26 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 861b7c0c-ec98-3d28-8071-ffe8c442d525 | -9.11418 | -49.43295 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ee31e9c8-38a0-362e-a3e3-07b9c59a03ef | -9.12035 | -49.4337 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 12a9da97-9a86-3e9d-bf94-0ef94f8d7884 | -9.5076 | -56.10093 | 2025-06-26 05:27:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d1001cb-ec45-3799-93c0-ad725d9dee13 | -9.11948 | -49.44703 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 562ef39c-7fb9-3a45-89bf-4e2ed6e7abb2 | -9.11265 | -49.43921 | 2025-06-26 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 420a6ea4-e824-3cd8-aa9b-16adb0304252 | -8.67163 | -49.95029 | 2025-06-26 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89fa25d0-1042-36ea-983c-fa7621ab14c4 | -8.67834 | -49.95108 | 2025-06-26 05:27:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f28583bd-767c-3236-9a3b-84cc69f77956 | -2.95379 | -60.01516 | 2025-06-26 05:27:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fadb425-84ec-3589-ba83-121a042f42b5 | -5.87541 | -50.15022 | 2025-06-26 05:27:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6a9a7c5-e19d-3cd7-8406-7e3b6922b91c | -4.52199 | -48.04722 | 2025-06-26 05:27:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2ab40d67-acc7-3415-b312-22550da86213 | -10.06614 | -55.54923 | 2025-06-26 05:29:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 610f182e-6533-376a-ba51-e49bf013b1de | -11.56567 | -52.09941 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 69385f19-57c6-3093-9ef9-48b04f112d8e | -10.82746 | -53.73673 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fae1df6-e317-36d3-847d-f4a5eb163ac1 | -12.58635 | -57.38349 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94ea314c-843b-3b27-8cd0-aeb87966247d | -11.13548 | -53.91993 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5b4e00a4-2151-3960-ba58-b1614eeea40c | -11.0748 | -55.37055 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ac5241a-5fd7-3d3d-993b-cd48bc48987b | -11.83315 | -51.25422 | 2025-06-26 05:29:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e80dc56b-c90a-3306-b1ec-cfa24eee130d | -11.5658 | -52.09257 | 2025-06-26 05:29:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9a831ef-3ecc-33fb-a887-54137cbe9218 | -10.71209 | -59.13309 | 2025-06-26 05:29:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f2259bb-6820-3014-bbb8-b8c19fe48b77 | -11.13849 | -53.91865 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7b6ed1f-e9c8-37d0-a552-de163381d2c8 | -9.25032 | -63.29064 | 2025-06-26 05:29:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6a8f435-eb26-3095-8b93-a3846642dfa4 | -13.29225 | -57.08929 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17604578-8580-375a-b5c2-0c76c9fc5beb | -11.05583 | -55.37691 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d39e7d92-b305-3b96-b257-e8d0f2bc69a7 | -9.17193 | -61.40355 | 2025-06-26 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4686ef79-7a92-322e-b2b1-d687afda5e3c | -10.50275 | -53.58729 | 2025-06-26 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8ee15a62-d01f-3112-a4df-03c6dde7a6ea | -10.82249 | -53.73233 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c4d72c7-392e-3119-97a0-ddd510d11e9c | -9.5766 | -63.20393 | 2025-06-26 05:29:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1d0a39e8-aa6d-3847-bc5d-046d96456b34 | -11.13588 | -58.61077 | 2025-06-26 05:29:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08564f03-80ed-3bfa-b835-0545a375b11d | -11.06852 | -55.38084 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a1e70aed-be10-312d-94b5-e09508a50045 | -11.13591 | -53.91645 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 20fef584-fe77-3165-97f8-30c74513f7e8 | -11.06435 | -55.37473 | 2025-06-26 05:29:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1b521b27-4e1f-3f22-8b4e-510b79bb3f94 | -10.82598 | -53.7322 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 32b81745-b8d8-3e59-8fc5-f0094b39c055 | -10.5082 | -53.58805 | 2025-06-26 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1835b9b8-c5a2-3824-b2fc-63df03753e7c | -13.09867 | -52.3003 | 2025-06-26 05:29:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a37e0a71-4032-33f6-b912-2dab8864cfe0 | -10.81916 | -53.74225 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| edd15cc8-2ee0-3fb5-add9-12a0771bbe7d | -10.29876 | -57.1287 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fb4c4511-7bb2-3c9e-99ac-b63025b1dcf6 | -10.8216 | -53.73958 | 2025-06-26 05:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa679ef6-9a13-3153-9753-9d7a9c216bc9 | -11.83637 | -57.8575 | 2025-06-26 05:29:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7ee74cc-e9e3-3101-9480-e06c7617fbd8 | -13.29366 | -57.09282 | 2025-06-26 05:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91e516b7-6e8e-3863-a883-d08979bf712a | -10.06685 | -55.55108 | 2025-06-26 05:29:00 | NOAA-20 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README20.md)
