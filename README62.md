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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efffcf82-5c6e-3879-ad91-e294c0db548b | -12.79091 | -50.87012 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 713f65df-4d2e-3982-bbc7-f3e4082480ef | -6.44845 | -54.99934 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 122bcb3e-028c-3e23-a9ea-551d045ec5e6 | -8.70437 | -47.03538 | 2026-09-23 04:27:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3abc226-bcea-3d75-994b-b402d15fbea4 | -12.79801 | -50.87135 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 976387de-cb0f-3683-a312-66447cb7aef3 | -11.93642 | -38.29168 | 2026-09-23 04:27:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 90f2d932-a362-3810-a7e5-2aaa5d434e12 | -8.37972 | -45.59249 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3c64a9a-fe00-3635-93ea-1b3bb1816476 | -6.93064 | -46.5659 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a4f42723-fce4-3652-9ba0-20327dc10d04 | -8.45454 | -48.69798 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50461eb6-9ae0-377c-8b64-9149d55f1fca | -14.62211 | -45.6498 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 33f1bb32-8905-3dc2-bf0f-bb6a9554df17 | -6.09612 | -57.68281 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1ed52341-e871-3568-99b8-2fa42c7d7ab5 | -12.12665 | -47.37938 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9cf3962c-f418-3603-9fe9-55f54abb1cfc | -7.41473 | -49.85441 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c364fc71-0c86-3d36-ba39-76edf7e38edb | -10.82832 | -48.47424 | 2026-09-23 04:27:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f53acb4-7889-3d86-aed4-7f4f45634319 | -14.62329 | -45.64169 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 8375d94a-12e7-31f8-babb-b544068e040b | -10.11731 | -46.07246 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eab69765-d968-3d28-abf5-33045c6f894f | -7.43554 | -49.83985 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d5beaed3-e5a1-32a4-a83d-60370463c011 | -8.0814 | -44.34503 | 2026-09-23 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab54b43c-892a-3f7c-bfb8-e9428c8986b0 | -12.81496 | -50.85733 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f3d4c56-f3e7-32db-b0d7-c8cb50e2f273 | -9.28581 | -50.32806 | 2026-09-23 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05705623-796e-31d6-b9de-f319ca960832 | -6.78098 | -48.66229 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1622c404-2688-3b10-a561-085485ac6c6d | -11.601 | -46.79688 | 2026-09-23 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8022a1fa-0ef6-3e40-a92a-58a77c7035a4 | -9.4909 | -51.90446 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44b3efcd-2f0a-39db-9c65-a7d2eaeb0550 | -13.29927 | -47.88585 | 2026-09-23 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d33c5ed-a441-3fac-8df6-f6c6c89e7060 | -10.51032 | -44.87796 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5de404d2-a28e-3adf-b120-9de437a6286c | -14.62681 | -45.64221 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| eaf59a57-78cc-3a58-a97b-e5fe9fbee040 | -11.65967 | -43.4118 | 2026-09-23 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f700f61-9b6e-3e6b-8cb4-639f8cf5f2c8 | -7.32938 | -55.59486 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4f39d8a-99f4-3c49-be1e-72f99a1021df | -14.60453 | -45.64713 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 2a0d91d4-42a5-3b89-b5be-bf21ef384287 | -6.67835 | -55.07265 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58970968-0d24-32f3-ab39-2317755bb27f | -8.73472 | -54.97917 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afde564e-933a-3aee-8ec6-2ec0214f1ee1 | -8.45912 | -48.69112 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 72040288-9bc7-3aac-a333-7fb667a9799d | -12.79826 | -50.91386 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9cf70a9f-08a2-30fa-b127-c97d90ee19ae | -9.87032 | -48.39899 | 2026-09-23 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20e12b8b-921e-344b-be6e-18af969c4363 | -10.45564 | -46.28586 | 2026-09-23 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eab13ab6-4be2-3e50-acb3-1a1bdec3ff63 | -14.60163 | -45.61756 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13356cdd-2cc0-3653-b963-70eeb7ee5a29 | -10.25426 | -49.97847 | 2026-09-23 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d864251-6541-3772-ab4d-edfacf8fc748 | -10.11904 | -46.08371 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b801d7a-3c0c-30fc-8cd5-36cce3523c50 | -9.56716 | -46.53809 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 880a5c31-e272-3978-a4e3-24273745b425 | -12.72203 | -50.88795 | 2026-09-23 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 104dc6a2-f762-3743-820f-9189a6756e01 | -14.62875 | -45.63326 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27990119-549a-37e8-aee4-5a6f52a875ef | -9.83738 | -48.30883 | 2026-09-23 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a87c9bec-e2d4-3c9d-9048-38959897bee3 | -10.14296 | -45.54789 | 2026-09-23 04:27:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03be1bb8-9ca9-325a-9391-3964095f9a46 | -12.12886 | -47.38695 | 2026-09-23 04:27:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c6c409c9-fdd3-39f3-8160-e4aa19d07db6 | -6.18491 | -52.79157 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 547cec3c-bd38-307a-a294-65aadc21bc42 | -11.78213 | -50.07974 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd46b71f-6871-3fbb-852d-40490f6ccf05 | -9.85797 | -48.30839 | 2026-09-23 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f26c921f-8011-339e-a28b-d1172074ded2 | -7.43482 | -49.84435 | 2026-09-23 04:27:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 91b169af-1ad2-3407-ba59-025b0c64a0e0 | -10.12184 | -46.0878 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bc63f905-ff10-3b40-9331-f56dcfd6f417 | -8.36305 | -45.61169 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d20c9dd6-963e-3c77-8ca8-f21e9968740f | -6.454 | -59.9719 | 2026-09-23 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 378f8584-0b73-3c9a-a8bd-a65861a7835d | -13.4583 | -46.27562 | 2026-09-23 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f32ba75-128d-3c36-a57f-a7c7afe5128d | -13.02497 | -50.60024 | 2026-09-23 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7f76fd5-2ff0-38bb-85d0-9bec000fef14 | -7.32872 | -55.59531 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7695493f-040a-31ba-9664-113644ca58a6 | -8.25105 | -54.7792 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| da295b72-f0f1-3a4b-9bcf-0741e66b6676 | -6.06708 | -57.80723 | 2026-09-23 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd59ecc1-ff4e-327f-97d3-eb5948bbb876 | -8.89836 | -45.91299 | 2026-09-23 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c1efd8ce-7fcb-3bd4-97b6-46e46ea77058 | -10.5057 | -44.86115 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac3d3320-3bb6-3e51-a8c6-0b9bc2b557af | -10.54451 | -57.44563 | 2026-09-23 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8b43011-6f33-3093-965c-bc3fddd4cbc5 | -7.63938 | -49.52034 | 2026-09-23 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 679a0252-c834-3b36-a660-09308850fdfe | -12.10619 | -50.0332 | 2026-09-23 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97284a28-03be-313f-b36d-3756862abfe0 | -14.64105 | -45.62255 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5fe8d0a-45ff-3c6f-83e5-2394b0fd037b | -10.66311 | -51.33038 | 2026-09-23 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84efd27b-23bd-3b7c-b8cb-0fdf92679258 | -6.66598 | -55.0718 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f804482-abba-3a40-9245-30f8903649a7 | -14.59282 | -45.62875 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 969eb17b-a409-334c-9086-02641d0eb499 | -10.11796 | -46.09079 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0ef8646-a634-33c1-912a-69201c73b96a | -7.97571 | -44.08784 | 2026-09-23 04:27:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a251e44-e7b8-3ce3-9874-72695779b5c2 | -6.68441 | -55.05667 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 81d7a0f9-44a2-338d-82a8-b138f07c0235 | -12.47837 | -47.01494 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c765444e-fc2b-3041-b261-fcd42cff7ec5 | -13.12737 | -48.57066 | 2026-09-23 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8aba00ae-2947-399f-9df3-622cd206fe48 | -6.63075 | -59.94083 | 2026-09-23 04:27:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 29e66b9e-2849-34fe-b24d-38a1c8ef41d4 | -6.67782 | -55.07581 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f5304c9-e7f0-3b43-b216-2bd17a1e40ad | -6.73344 | -59.42387 | 2026-09-23 04:27:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b00b7ab7-defa-3006-bd20-c5210aaea379 | -6.67019 | -55.05903 | 2026-09-23 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfb3c946-0743-3a62-a8a4-440b92427289 | -6.56711 | -55.41002 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dcc78f7b-2d1b-3d41-9717-c9b7604d144a | -7.98318 | -47.46848 | 2026-09-23 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| baedfe0c-ced6-3226-8d14-31d85d1b06d6 | -11.46069 | -47.37694 | 2026-09-23 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca097dc7-0b61-39b4-b647-e79eaa48c380 | -12.41129 | -46.96448 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 6b0fc268-75a0-3f88-8c5a-08f4fe9ee6d0 | -8.3636 | -45.60812 | 2026-09-23 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df99a11d-5e6a-314d-b04e-0357a5bf6aba | -7.33042 | -55.58912 | 2026-09-23 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66337742-a224-34b1-b924-09bd4dda50b8 | -12.04551 | -50.35328 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4a1f431e-709d-3d49-a665-cbc3dd5c995e | -12.06718 | -50.35286 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72173350-d630-3bfe-8700-a72a47738fa9 | -14.69212 | -45.59274 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d45de266-f7a6-39be-a484-ae901a2dde3c | -14.70035 | -45.58573 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6d54f9b7-75dd-330e-af8d-5ddae23c473d | -6.78037 | -48.66606 | 2026-09-23 04:27:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ccee446-85ab-31f4-92c1-bbd62eacab58 | -12.04735 | -50.3584 | 2026-09-23 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c89448e1-3384-335b-a342-21e615789594 | -11.45335 | -47.61951 | 2026-09-23 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4324df2e-0374-362d-b924-0b826ce8ad86 | -12.41244 | -46.97927 | 2026-09-23 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de0efea2-212e-3a8f-913c-5595e89faf1b | -6.90147 | -46.55781 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b83034e-5e79-3870-9ecd-e42234a41765 | -10.50043 | -44.87243 | 2026-09-23 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f0974cd-a1f2-3372-a1ee-4718671b9747 | -14.16917 | -47.84627 | 2026-09-23 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d13189a-4653-3fe0-8cb4-ce31e36d6436 | -6.46516 | -51.5212 | 2026-09-23 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ea80030-1022-3fa8-8470-679acde0b7ad | -14.62881 | -45.65823 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c8cd635e-dd56-3e38-8a21-d36d2770b3fe | -9.6227 | -46.75076 | 2026-09-23 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| da0a747b-4e86-3100-8970-e606b9afa75b | -14.63153 | -45.63457 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e2ddd729-103d-37cd-a06b-97c0fff79a8d | -11.08789 | -48.34131 | 2026-09-23 04:27:00 | NOAA-21 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6444f9b6-b971-3e50-9f9c-77baa63c306b | -8.45394 | -48.70166 | 2026-09-23 04:27:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c244477-e5cf-3628-b6e4-eadac21d1dc3 | -6.93833 | -46.56002 | 2026-09-23 04:27:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f4c899d4-730f-3b6b-bb8c-95aafd5e10b4 | -11.11827 | -51.05437 | 2026-09-23 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4211f5e-de2f-3958-abc7-aaef7a8917c8 | -14.69976 | -45.58981 | 2026-09-23 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.1 |
| ab5886f4-b1a4-31cc-a0a5-ae72ca4848e4 | -10.54399 | -43.97648 | 2026-09-23 04:27:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README63.md)
