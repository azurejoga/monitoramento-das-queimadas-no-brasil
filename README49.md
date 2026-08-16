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
| a5f87a8f-84e0-3a25-b5d6-f7f61965ced1 | -6.62007 | -59.0648 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16e003ee-4f53-3026-a286-815ed5370a21 | -10.62442 | -53.90162 | 2026-08-16 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7967e76-267e-3c8d-9e46-2e660df0219a | -7.46021 | -55.31023 | 2026-08-16 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5091c01f-bf65-3a11-805b-f69607417137 | -10.07157 | -60.50343 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7bc3c74b-9168-3c5b-972c-ce929f569b6d | -8.95382 | -60.59801 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04e66617-1207-37da-b144-a61e7a53eeb1 | -8.94709 | -60.52589 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 698d9a87-cdd2-3418-ac7d-074feb95848c | -9.2988 | -56.81982 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 419d7235-642e-385b-a767-d39ed41ec628 | -11.22067 | -54.82444 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72a1eb95-1ab4-359d-9a89-7dfba468ae4a | -6.62671 | -59.07014 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 3b7eb6a5-eab4-3d87-a7fe-1bf757f1c2fc | -8.61087 | -54.71116 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9adc210-cf1b-34a7-b338-9160c050a6b6 | -9.08344 | -61.39716 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc16334c-e780-3e80-9df1-9b252a9c5ab2 | -7.4621 | -55.31243 | 2026-08-16 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81947a37-0069-3e12-a0ce-ff707346a0cb | -6.88105 | -59.01867 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e54b1732-f250-3882-a643-cecdf1cfdc95 | -6.70749 | -58.95605 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34cd4a5a-2ffc-3549-a0c0-fd139c81c9f7 | -9.13178 | -68.18315 | 2026-08-16 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09c259cf-ee58-36bc-8c9c-e488c002c032 | -9.12989 | -66.97348 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9aebe03d-5f8d-35b6-ab85-1803d3805be2 | -8.94872 | -60.56178 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81f20bb6-d1ee-3d65-9814-6c192a41dc8e | -8.97374 | -60.53791 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa24c006-018c-37f7-96a7-5ce7261e44ac | -6.61754 | -58.98191 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbdad613-5d72-3a2c-919c-e299e4dba061 | -8.64292 | -54.69876 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3ce336e0-6ea8-31f5-8514-c916fd26ddc0 | -6.6207 | -59.06058 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96ac81bf-1083-347a-b49e-6d45562c2459 | -8.43543 | -62.68196 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 86e1fcdd-0988-3ac2-b00c-ab7362f0551f | -8.43708 | -62.67154 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5b951c3b-ad65-330a-b453-28687e9dc5f8 | -8.62199 | -63.72781 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f4a7b4c4-c9f4-3758-acfd-b4ba9e8e2676 | -8.61034 | -54.70995 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 573cf7d7-cd70-3432-b8b2-102fae814da2 | -6.71147 | -58.93017 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3eb96d98-882a-38e9-b830-8e950851f5ab | -6.87009 | -58.94216 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87250d3e-bc8e-3aff-ace2-8ff8ac75a3ed | -8.97957 | -60.51059 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| f275653c-d1eb-37fa-a6b9-f5f97cd6fd20 | -9.47457 | -60.50678 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d7c6b9b-4185-36b0-8d13-51fce933f4ce | -8.42882 | -62.6809 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 454ecd86-24ee-37ca-bc72-189b39ab92ea | -12.06047 | -58.04492 | 2026-08-16 05:36:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e58738e-55bc-30ed-9e52-76d07eb0f4af | -8.95457 | -60.5468 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be395f9e-e48d-3b88-8395-f7cf4d325063 | -9.4294 | -60.3264 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aefd6d8f-f349-303d-bbb5-79e17696c977 | -7.34649 | -59.59489 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| be47159a-2c3a-3859-921c-0273c8831dd4 | -6.78765 | -58.74355 | 2026-08-16 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6ccabcbb-c971-3a80-81b4-6cde15dbdbaf | -7.33516 | -59.59731 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 64d99ae9-7ae4-3a94-a394-b62a0f68589d | -6.85327 | -58.97933 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a4079e77-2b3f-36f1-bdfa-c067947dca83 | -6.62371 | -59.06535 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f4e537ed-6d96-3c7c-ab94-804806152b57 | -8.97214 | -60.50196 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bb59f5d0-c620-3605-8176-ff37131988d7 | -8.61866 | -63.72726 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b6ddc639-0e41-3baa-856e-3fd37ad8a63c | -6.6096 | -58.98508 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 222362c5-1df7-3b5d-9e30-cecdef5be7cf | -8.60696 | -54.69787 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ff749b8-5f25-3226-89bf-2316ab58f5fb | -8.97608 | -60.51005 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c13bceed-9edb-3d6f-bde9-f914be91fab7 | -6.85822 | -58.9713 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e210c2b9-b9ac-3b68-82a6-eec23febeee7 | -9.47107 | -60.50625 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42c7fc16-5302-355c-b949-1ea24ecfcdc2 | -6.69886 | -58.96354 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6215c732-9e21-3394-9050-41e427bf2c0f | -6.42905 | -60.07821 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cfbdbea-7b08-302f-a386-7cea861e9f2b | -6.96774 | -59.30696 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af4c4d02-c8ca-3eb6-aea3-52492ea6428d | -9.48343 | -60.47195 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc0a2d8d-6124-3f1d-bc31-28a9f7ba4f6a | -6.60342 | -59.00156 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc45727a-c89b-32b0-a588-9e8061313ed7 | -6.71579 | -58.92642 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4b27ad66-fee2-353e-9a47-374227631c90 | -8.44148 | -62.66513 | 2026-08-16 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6ba006f-d22d-33cb-8bd8-ed34c5eedf39 | -8.61237 | -54.69979 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43d4394c-daa7-396a-9179-7410d701b9e5 | -6.70121 | -58.9726 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81e3ad76-51b9-3156-ae98-11f105a9931c | -6.62988 | -59.04903 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cab9dcb3-e49f-36a9-a443-601e2489a262 | -6.71381 | -58.93932 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b11d553b-6c2b-32a4-9959-7b1dc48a2e1f | -8.64007 | -54.71466 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e9569f71-2b37-30f6-91a0-a5a0d9ad6814 | -8.97899 | -60.53828 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e961c786-4a8f-3f0f-ba7a-0a7b3d3d3856 | -11.80536 | -51.78779 | 2026-08-16 05:36:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35fe78f1-e543-3426-ab1d-a9c753df488a | -6.97274 | -59.00439 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| abd412f5-da68-35b6-b275-0d5d71c37933 | -6.61595 | -59.04263 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c41b5240-35f2-3fea-adef-971c694d2b0e | -6.85217 | -58.96159 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 28dca97b-fc2c-3bd1-9c27-948ffa8d01a0 | -11.21635 | -54.81755 | 2026-08-16 05:36:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdf4de71-c06d-355b-874d-2bd3b29893a1 | -7.35425 | -59.59188 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1ef1d90-9488-349f-b554-812cc7fdc507 | -8.95235 | -60.51481 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ead0c1ca-945c-3ea2-a150-03fb5f365749 | -8.97155 | -60.50584 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4bd99e6d-cc4d-3e0f-b8e4-2314dd5bf729 | -7.06842 | -56.65351 | 2026-08-16 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58b3b6bf-1e4c-30fd-ac47-33362922428f | -6.70252 | -58.96407 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4083bd4f-6820-37c4-96e0-4742b3550879 | -6.70514 | -58.94696 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f7ef4c1f-d981-3a27-b7b7-4bed7c21e983 | -8.60199 | -54.69713 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f2d1772-7711-3c9d-81c5-24d1b307ed80 | -6.5982 | -58.98526 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b80b9d1-cb7e-3b39-962d-976bc167d1ba | -6.70317 | -58.95982 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cde66f75-426a-392a-a9fa-c304b98e540a | -7.57777 | -61.23685 | 2026-08-16 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cb45e9a-d785-3f7c-9450-61dd0d6ed275 | -6.60119 | -58.99009 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c920fb8-b33b-3896-80f1-2ba34ef6e721 | -6.7188 | -58.9313 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9592eb25-537b-39d2-ac68-c4c4913cf983 | -8.61192 | -54.69862 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8adc206-14f9-3686-a5f9-52b1057a336f | -11.51141 | -54.63585 | 2026-08-16 05:36:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9df06f6-2e38-369f-b8be-b1f7f4df8ac7 | -6.6055 | -58.9864 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90b7115e-7960-31dd-a55c-748f0aed4d7b | -6.69348 | -58.9497 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| afdd5dfa-f987-3236-80e6-77c1e15661f8 | -9.30053 | -56.80716 | 2026-08-16 05:36:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cac52510-6046-3f0e-8a6f-5bf69fecaba6 | -8.9539 | -60.57437 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a599a247-7bb0-30f1-b6a8-ef54fdbf1f52 | -8.95346 | -60.53082 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bedc793e-0307-3420-9ea2-1ebd1aa07e35 | -6.61929 | -58.99527 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dacb2545-2ac3-3ec1-87e9-71dac153f650 | -9.47504 | -60.55095 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4f2d7b8-1d2e-30ed-8741-4ce9e93758cd | -8.54521 | -54.59165 | 2026-08-16 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 053e0cb3-e380-3586-be35-12aa52785a50 | -7.39279 | -60.00198 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30a8eca5-cd05-3574-8d2b-c8ddd2a6e327 | -6.70382 | -58.95554 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c083aefa-5050-3bd0-b516-f1608330c7a9 | -7.33873 | -59.59786 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecb8f20d-5d78-3a38-b580-e5282dc3aa27 | -9.47398 | -60.51073 | 2026-08-16 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff473b2c-95ea-3721-8934-404e97703f38 | -9.39832 | -65.96179 | 2026-08-16 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab4a31a4-095d-39c8-bd42-be0a1e13b1c9 | -6.85392 | -58.97504 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ea5c2b92-7cbb-3cf3-a955-ef6bf759c05f | -7.38056 | -59.98813 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4382314d-71ef-3d41-8218-e6202f933df1 | -8.9784 | -60.51837 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 06f30fed-fa1a-3843-969e-7c9eecf1d863 | -7.42661 | -60.01532 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c5862b20-ca68-301d-bcc8-e52b2baa8ee6 | -7.42635 | -60.02237 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf09ff93-556f-3bec-ae93-3486a7ba4a29 | -8.89307 | -60.60053 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3612e7f-abf6-3b9b-8e47-b27fdae2217a | -6.969 | -59.29867 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b83d7a81-4f54-32c9-88cb-90c892417d33 | -7.41731 | -60.00586 | 2026-08-16 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f9ba4e8f-f5a5-3ad6-b904-d6719603d234 | -8.9633 | -60.53631 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 37e93743-620e-319f-808d-d73219390bd0 | -8.9511 | -60.54626 | 2026-08-16 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README50.md)
