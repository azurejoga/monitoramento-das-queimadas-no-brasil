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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9cbfd75e-c264-3636-bdb0-27f35e79619a | -10.96112 | -57.19098 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1e1fd0f-f2b7-33ca-832c-6f4c722329e9 | -5.83166 | -53.51247 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64a1acde-3104-3eac-a56b-cbde25ac5a90 | -6.27771 | -62.71906 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c2c2aab-d4b5-3799-81b5-0d09ffeecc78 | -5.26039 | -55.925 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 071e6d21-8154-309a-ba78-4d6ca749ef72 | -6.74782 | -59.06448 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9869448-db1b-3c48-9753-6b6daefacaf4 | -5.81012 | -57.73718 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12ba3041-6e50-3b2e-b946-e846bd3c0b7a | -5.82095 | -53.51404 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d76a0694-82a2-35e9-bc33-cd1cdff06018 | -10.48798 | -50.99276 | 2026-09-21 05:42:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0e22531-1dd6-3fb8-b3b0-c00792a3c2d7 | -5.84236 | -53.51098 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b68dd7f7-bd5b-3fcf-980a-d4f9d3fd7182 | -10.80278 | -50.77505 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1617f0bc-c90e-3564-b57e-c323e6cfa296 | -6.33262 | -60.01346 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d807f70-41a7-3dac-890f-8c9390a299ca | -5.80981 | -53.51866 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 552bac30-7db8-3421-8ab6-88c23ee106e2 | -9.55144 | -66.00101 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3eb44bf-df17-36a5-b7c4-614fc4245443 | -11.12897 | -54.0111 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 221d687d-affa-3ed7-ab93-c95ec660176f | -8.0832 | -55.34439 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be8d5250-6a27-33a0-bdf2-7a7812f21e97 | -9.06107 | -60.39188 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a56b324-102b-3604-9cbc-f3baaba0c4b2 | -10.80944 | -50.83753 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 815a6e52-e19c-33cd-87c6-0c687dffd6a5 | -5.80549 | -57.74152 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a943b9b5-4fb8-3dcd-813f-c393dd886834 | -7.32987 | -55.20481 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfc60d24-2d44-3098-a2c1-6b83002351b1 | -7.9715 | -62.04192 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b57a6eb-26f5-3cbf-9383-4478ff2e56df | -10.46653 | -51.33164 | 2026-09-21 05:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c881f75f-4d66-3879-83b2-970c78cf4992 | -10.3894 | -50.2268 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac78f601-0ac6-3a4d-b042-8fe80db6b957 | -6.49344 | -58.37992 | 2026-09-21 05:42:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 730cdd31-f952-3f69-97f8-1d2105419532 | -5.98413 | -57.77717 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ff973185-8868-3581-beef-a4eefcdac5b5 | -5.88291 | -53.64341 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7951d046-0163-3f4a-b6db-8fd5fd3920d6 | -6.64594 | -59.95954 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4388489b-3a2c-36aa-8910-45676e9df1b2 | -9.12305 | -58.9239 | 2026-09-21 05:42:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9885bb09-fc94-39b6-b172-ea1cb7d19d82 | -8.79809 | -60.8038 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 842fe211-c3c1-3fa1-9564-dfe5dbf4343d | -7.59272 | -57.66901 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8622a212-ba06-3e38-8bb3-09902fea0205 | -6.79612 | -59.13854 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e2de006-4c86-376b-91f2-6fec55e3879f | -5.91968 | -57.67888 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20fcdde8-52c2-3abe-b7a3-abe3cfb6929b | -10.42535 | -51.86906 | 2026-09-21 05:42:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1826f50-2630-3f9d-bd91-4daecefc0e98 | -8.78138 | -68.84116 | 2026-09-21 05:42:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90b8cd96-f586-3f6a-a684-a8f348248105 | -7.58501 | -63.047 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5bd7b91-8448-3c44-8e79-58235724bca9 | -5.82653 | -53.51171 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3eacaebf-51ce-3569-a430-4e737f101e39 | -11.12318 | -54.01369 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04d844ab-9ad7-384e-999f-05a2a46512ec | -5.81452 | -53.5224 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5486128e-38e0-3af5-8f00-d7fbad603b7d | -10.96544 | -57.19147 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ae26e5c-0349-3cff-a80f-45cac998f1f2 | -9.9857 | -50.26389 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e551a0c8-1116-305c-a4bf-57ac31a86af5 | -6.72882 | -55.08008 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ce0e11d-7b4f-3c85-90a3-c3aede41253a | -6.75889 | -59.11325 | 2026-09-21 05:42:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebb16960-0fa7-3220-a819-86a60de5e63f | -9.55169 | -66.04434 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbb8909f-4093-3e78-b4aa-a0a152f9da0f | -7.32681 | -55.61124 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cea21945-418e-3b5f-9b24-594363ca5e29 | -9.57006 | -66.04574 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa2511c6-ce37-36c9-ad35-b44b54d9f83d | -10.85988 | -50.15725 | 2026-09-21 05:42:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e4a8392-7a73-3328-9392-71b25fc2ac3f | -10.82942 | -50.78376 | 2026-09-21 05:42:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2307a7ea-10bf-3e19-9a6b-b3ebf94aa6d6 | -10.94661 | -54.09249 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd2edb28-7219-3ed2-a695-54b0738802ec | -10.88276 | -53.97583 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d192230-f2ee-3e19-92d7-115a9c06288c | -10.91974 | -53.94306 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0bea6cd-9d6a-397a-bb94-9261cc3fdb5f | -10.87176 | -57.1591 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ca46344-7630-392f-b44c-8e9d0836df33 | -6.7285 | -55.09591 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd9c81bd-16fc-3bf4-ab24-0f6cbbdde736 | -10.95193 | -54.09315 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa1e04f2-a6c8-36f3-9c25-8773c3b8a5ba | -9.55754 | -66.05405 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34318ea0-c97a-3ef5-8a49-26199f92637e | -11.01636 | -54.12825 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d18cf812-df47-3626-8f3e-fd96ba60eaad | -10.42509 | -50.23662 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 544e00a7-586a-3d40-a59b-efba899accff | -7.25496 | -55.59349 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2e76b7bf-c22f-360b-99c8-18c1290b9225 | -6.73609 | -55.09542 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d5e8ad4-2cd2-3e03-8342-89c0260216ad | -11.01674 | -54.13529 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2f503e4-0202-33ef-b5dc-ef0bfe7adcc3 | -8.60561 | -54.61273 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc60844b-243d-3f33-b199-5d031cc1ae5f | -10.46306 | -61.31487 | 2026-09-21 05:42:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b2d0e8f-c058-3abf-8ee0-67cae013c325 | -8.18755 | -54.74031 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86efa157-2519-3fc9-93b8-bdd5bd66cf04 | -6.72351 | -55.08379 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9ae411d7-728c-3a2e-9fcb-2b6ee59dc4cc | -6.11952 | -57.75784 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed445827-a15e-3cb5-b20d-319d5b44ecd9 | -9.02966 | -60.3632 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68e7b02d-02aa-3a1f-ae7b-2a346f8a9c72 | -10.87288 | -54.05268 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b78d336-1c9c-3698-8a57-09aba705754e | -11.04574 | -54.15218 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b718938-d521-31e5-8f31-d96525e2a930 | -6.35198 | -57.77657 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a91f051b-5d9f-3346-a18c-69342ebca9a2 | -5.2121 | -56.07401 | 2026-09-21 05:42:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 863b8c1d-47dc-3d71-8e11-f4f30cb5fa51 | -5.66764 | -60.2347 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 236d7ef8-be1d-39a0-96a4-d3f1ffa152b2 | -11.01958 | -54.14566 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52152245-c5d2-39e8-abc2-d7839b5a27e5 | -11.03282 | -57.24281 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df50e597-a476-3725-a135-1baa8d5dd56d | -9.11371 | -60.95079 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cf5b289-2b79-3b26-a751-5af380659f37 | -5.9158 | -57.67826 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7647a661-abf5-362d-a11c-195c4b90c906 | -9.27751 | -60.6317 | 2026-09-21 05:42:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f921af1-98d1-32e1-b0e1-f75a443ea4fc | -6.19868 | -57.78442 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| ebff86b3-92de-37ac-a17c-27353a82fd32 | -8.17565 | -54.77082 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a06cb417-93d8-3d42-b850-949221a76732 | -6.72281 | -55.08854 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1339acd0-d4c8-3834-990b-e6fa12d6bd1e | -10.42371 | -50.24865 | 2026-09-21 05:42:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ff8bdde8-8609-34a7-a7d8-8e8d5d819462 | -6.30973 | -57.73853 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4046c6f7-7ae4-32c6-92a2-d0796b9a2013 | -7.58168 | -63.04646 | 2026-09-21 05:42:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d8a823d-62f9-3da1-a4c3-6d025c95ffe5 | -8.793 | -60.79595 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c7a979a7-81ab-38fc-a6bd-0c44ac1e4a8c | -11.03398 | -57.2347 | 2026-09-21 05:42:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2371d80c-0954-308c-9e5c-4c5e6d6cf357 | -6.02821 | -59.92928 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6bbb6d6-d99e-3810-abf2-6aae0704a28d | -6.9943 | -61.35216 | 2026-09-21 05:42:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffe58f35-7c05-32bc-8596-2fed183426ac | -5.76075 | -56.51965 | 2026-09-21 05:42:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1884a509-d4ef-30be-8372-e37b1887a21e | -9.24164 | -57.15189 | 2026-09-21 05:42:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| befecebe-a8a6-3019-a9e3-44ba4a445f99 | -10.91754 | -53.9599 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a856a645-3e99-383f-b218-c93bb5a3b134 | -9.55087 | -66.02685 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6cd04388-3c06-3807-a53a-09550ca44edb | -6.32051 | -60.02314 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 303cf48b-5a9a-371c-9e34-b0b0df996475 | -6.64881 | -59.96393 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a24b457e-4ac1-3d58-845b-2e122e703550 | -8.65644 | -62.48044 | 2026-09-21 05:42:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7570f0dc-0c90-39ec-8623-dde92c1da33d | -6.32802 | -59.95056 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 835cb76f-7b2a-3444-bbd5-ba35190ea910 | -11.05106 | -54.15276 | 2026-09-21 05:42:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df88075e-3b60-3ea2-86d7-394533b0817e | -5.85378 | -53.54074 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 266ddc2d-3e0f-3db9-aa69-4a60f1aca7c2 | -7.57458 | -57.68197 | 2026-09-21 05:42:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6d3db101-a38d-370a-b3d1-bc87c66004e6 | -6.20909 | -53.56677 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb766b97-7b9b-34fe-ae1f-e56c58f46890 | -6.31752 | -59.96128 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7dada380-fe8e-3e41-8faf-19e008d801fd | -6.45256 | -59.98059 | 2026-09-21 05:42:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65792ed3-49f1-3170-98aa-0cc4d289b83c | -7.25042 | -55.59284 | 2026-09-21 05:42:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 29747aa4-2e5f-3642-a254-d0831e11374e | -6.72958 | -55.07497 | 2026-09-21 05:42:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README93.md)
