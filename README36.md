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
| e5bbb977-dfb6-3ccc-8317-1e08cb2f778b | -8.8346 | -62.30581 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 940254c3-910d-3176-b9be-713fe8f5b13a | -8.81848 | -68.6768 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f097bfd2-8ef2-3ea7-a8bb-0cc77d7e9ded | -8.76791 | -71.09609 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fecefea4-9d3d-3756-9160-c33e5176625c | -9.04377 | -65.74106 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cffc3158-2672-30d0-8da6-5e210464eeff | -9.43827 | -67.42348 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 744d170f-26ed-3f37-8d6e-eb09b20cfe4a | -10.54441 | -69.02736 | 2026-09-04 06:01:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbb6d752-c3ad-3d57-9e38-1fc65aaf2e9e | -8.52587 | -67.15987 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a83f9b49-bdd5-3744-b931-b0790839c5c9 | -7.88023 | -71.75822 | 2026-09-04 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cfb99cf6-1aca-3547-9459-2f87ce3678ce | -8.56157 | -63.1914 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df8e7672-c261-3e85-9e8d-1827b7ab3941 | -9.74391 | -69.06718 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5005e7e4-3bc0-3cca-b136-716334d26879 | -8.6953 | -62.92801 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 363212b2-99a7-36d2-8781-b887792beff0 | -9.5357 | -68.63184 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf6332cf-81b9-32a6-b608-8d9b77e702d9 | -9.04035 | -65.74052 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b6505b-fbc9-3944-bb87-c435421eb842 | -10.28588 | -68.85262 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 664f77b2-5eaa-3962-99c1-a6a228048238 | -9.03749 | -65.73624 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48ce1ebe-781c-3d0f-af57-455aa1298dcc | -10.20116 | -69.08979 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0217e333-71d0-34e2-9db1-28a994a6d2d3 | -9.02198 | -65.45246 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0810687-79c8-3717-90c1-943ebe12eb8c | -8.52532 | -67.16336 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ea2d7ba-1282-3fea-aff4-50b0ad510dec | -7.87633 | -71.75755 | 2026-09-04 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3f38e11d-fadd-3d68-9587-36847484dd90 | -10.20058 | -69.09341 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10ada47b-bd2a-3c54-a95a-a44c4ccdaca7 | -8.55771 | -63.19082 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 12c9de89-60fc-37c1-be0f-98d52816cd6d | -7.79016 | -66.95685 | 2026-09-04 06:01:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a569641-1b12-3dd5-8196-14a7aeb2aea5 | -9.03806 | -65.73251 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fd470b5-66ff-3a23-84d6-2d01d766e18a | -10.29096 | -68.84247 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c7a4ed3-8259-320c-96e6-612d36721c3b | -8.9206 | -62.36993 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a07ef16-c8fb-3eaa-a6f4-a9f1d20f7a05 | -8.87265 | -66.67141 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0af1ddcf-89ae-3d36-8103-9090fa1c23a8 | -8.60511 | -67.17236 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 160adbf2-17d1-35a7-ae0f-e8197fe8d363 | -9.03463 | -65.73197 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f0aa645-1072-3352-ad3f-87f2e7fb9b82 | -10.28761 | -68.8419 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 565d4959-a651-34c4-bc78-565afc801d9d | -9.57371 | -64.29353 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2f5aeb8-19de-3b21-ba88-49a19baccb3d | -9.04434 | -65.73734 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 28f7f1ac-6c13-3185-a293-c235ac876cc3 | -8.47854 | -70.61398 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54d3c0f9-28d3-357e-861f-054b9e31094d | -7.56784 | -67.39604 | 2026-09-04 06:01:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75131395-2dce-3b91-9273-f654ebac8e42 | -9.1093 | -65.49706 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a2a20cf-89fb-37f7-a438-b55ff36748b9 | -13.30951 | -61.09993 | 2026-09-04 06:01:00 | NPP-375D | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 617f2bde-62a5-3b54-8ead-03bbf715e748 | -10.20174 | -69.08617 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dfc30a7-97fa-351d-8c0b-c37067109f82 | -9.65111 | -68.61039 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ce1f8e5-6ba9-37ad-a3fa-1c40e659ba8d | -8.56543 | -63.19198 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60c19663-aa60-32f2-81f8-f7c04fac4c2f | -7.88741 | -71.7393 | 2026-09-04 06:01:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9020bf87-0553-39dc-8268-728e255a9820 | -7.74209 | -67.06708 | 2026-09-04 06:01:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 67b74713-9b72-3a30-aa35-7ab811a930df | -10.64172 | -68.95875 | 2026-09-04 06:01:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1ed4a88a-77fc-370e-aeab-3041b9ce5af9 | -8.86518 | -68.49385 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54aec972-8f48-3f84-93a4-e5f4ebb473c5 | -10.292 | -68.8573 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a37647fa-5421-394f-a8bd-d94399cf6670 | -8.21179 | -70.15406 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29d7bdce-2108-377f-a7c2-14f48fb503e8 | -9.66558 | -67.39851 | 2026-09-04 06:01:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b7075d-1c4e-321c-8285-d0f3d6002613 | -8.87369 | -68.61234 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b1bda7e8-040f-3863-b567-182b1a93feaf | -8.60068 | -67.17882 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 98afd990-e210-3701-8226-6eae122100c1 | -9.0432 | -65.74478 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 100341d6-b561-3ce2-bc0d-264d7c1ba0e1 | -10.18969 | -69.0323 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e28be1b-1b2c-3d3b-94fc-4036554097a7 | -8.80148 | -62.88404 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 762a5cfd-9203-38d4-87a3-00baecbb34b3 | -7.78739 | -66.95284 | 2026-09-04 06:01:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47a7b65e-4a32-358a-b42e-6e276f010f4f | -9.03121 | -65.73142 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cd44622a-23d2-35c2-85fa-5da95352f969 | -10.28646 | -68.84905 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31e9bc41-d95f-399b-ae57-75f3db7ec3d4 | -8.60678 | -67.18337 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0a79a5b6-705e-33bd-8b25-8832f612aa13 | -10.29143 | -68.86087 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0ea70c1-6aa2-3d29-a213-2c3e81b56ff7 | -9.74332 | -69.0708 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e4d9b1ac-9d33-312f-9aab-b94c74e5c172 | -9.57738 | -64.29408 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35eb4550-573b-3199-adfa-62f14e44cba1 | -8.60568 | -67.19036 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9d0791b2-6f9f-3f11-a61d-9d0a2142e3c7 | -9.89672 | -64.82062 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b0c3908-e731-3d4f-9b4f-a2e45f81c294 | -8.92113 | -62.36629 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2355f8db-2b73-3b1f-ae73-94cf1ff31111 | -8.60178 | -67.17183 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 03c72721-9818-3e1a-bec9-d1e7c8ab8168 | -9.71368 | -65.00175 | 2026-09-04 06:01:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7032325f-e381-31f1-b4bd-fc955f0f7473 | -8.8691 | -68.49085 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c39ccca-8811-32d8-84df-06518c061f39 | -10.45698 | -61.20728 | 2026-09-04 06:01:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77bd8a3d-e414-3b30-a287-3426a0fcf691 | -8.63653 | -67.01614 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a83cd985-466c-349a-b31c-f363a45af8df | -8.8693 | -66.67088 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c705822-554d-3b5e-af85-c3a912d031c7 | -8.70705 | -69.99992 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a08c4e11-0e3e-361b-a48d-b35bc0140953 | -9.00573 | -70.56754 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63b8d8ef-61b7-3e1d-96b5-2e1d5fb1d6ac | -9.17534 | -68.26448 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e253f5da-06d0-3a3f-a93d-43e1584d3357 | -8.60013 | -67.18231 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 26.3 |
| d26a7f77-7f35-3744-ad99-978420f0a422 | -7.38761 | -72.80025 | 2026-09-04 06:01:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cd5f337-f9fa-3e1a-a2f4-b2ae7ffe2824 | -9.24717 | -68.22198 | 2026-09-04 06:01:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b577edd5-faa1-3168-b591-38d12de9edc3 | -9.10065 | -65.50736 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df35ab53-e1ed-3574-9435-5db9f36b0865 | -8.70655 | -66.54705 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9eda0a5-e14d-3093-9552-2dce843f8c5e | -8.87801 | -68.49959 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e8d65f2-9ad0-37b4-a1d4-ae83246588f2 | -9.04834 | -65.73414 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11d7333e-255b-3fee-8e81-f685844e6cfc | -8.87599 | -66.67196 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24a627fc-b9e7-3e6c-a144-99faa7497b17 | -7.79464 | -70.05648 | 2026-09-04 06:01:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a89adaf5-2ec5-3ba6-8445-afac1ace47ea | -8.91454 | -62.35416 | 2026-09-04 06:01:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81827d99-1366-3398-a71b-f5200b98dd87 | -10.28981 | -68.84961 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3922db2e-7330-39cc-a844-3f59956d065f | -8.522 | -67.16283 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f82ff304-add2-35c6-8811-e62748a4625a | -10.28819 | -68.83834 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2adebca-e57f-331d-b419-662f6b9494bc | -10.2853 | -68.8562 | 2026-09-04 06:01:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d2259c2-38b2-3e4e-83a4-e4ac03710ce4 | -11.51544 | -58.50712 | 2026-09-04 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf2d675d-ad70-34f0-8a0c-2ff12e73fe45 | -8.71056 | -70.0005 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d210ea27-c4f9-3698-b7f0-51634f8ad44c | -9.74274 | -69.07442 | 2026-09-04 06:01:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57a6ded0-311a-37ab-9cf5-be13df9567ba | -8.87523 | -68.49548 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64fa3efe-e1b2-373b-adb6-aa9f7459c99c | -9.01744 | -70.8981 | 2026-09-04 06:01:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f9517c9-f081-3323-b990-f46119509fb8 | -8.52255 | -67.15934 | 2026-09-04 06:01:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09336421-5349-3bc1-a0c1-c43066692dc5 | -8.71203 | -62.95087 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 441f3a02-9cb0-37a9-afb6-8585c231a423 | -9.10989 | -65.49324 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7115fb1-284d-3a50-9264-f837fe6edc26 | -8.68424 | -62.92126 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37dcca7f-f7dc-3ebe-982f-e4f4765af184 | -9.25911 | -65.90631 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a3d8207-e078-3956-bb31-0c4ca8034f1a | -9.03978 | -65.74424 | 2026-09-04 06:01:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c83cd6a5-10ca-3391-b355-bac6dfccd132 | -8.69458 | -62.93299 | 2026-09-04 06:01:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5458f76d-9711-3998-a1e8-8cc5d7964698 | -17.10389 | -56.85089 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3c6973cc-0151-3495-89b6-881bc9e92ea1 | -17.09954 | -56.8448 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| df16c52b-1b2c-3760-8690-c58d58c617de | -17.09782 | -56.86177 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 11fc4736-ba57-3eda-8fcb-da9cb5d968d4 | -17.0984 | -56.8561 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4871280f-bf3e-397d-972a-03b473f0ab1b | -17.09788 | -56.84449 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |


[Clique aqui para ver as próximas entradas](README37.md)
