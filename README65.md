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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 424f981d-a3d5-348b-b73f-fa3bf8ec19d7 | -6.0781 | -57.81467 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08ea9a18-6188-3ade-85de-74f955b21cb9 | -6.0812 | -57.79438 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d8540d72-6c84-3d39-aec8-37f32da953be | -8.83729 | -62.39179 | 2026-09-28 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3ee8b81-b9a7-38fb-8173-67a716e9d228 | -3.75696 | -61.74343 | 2026-09-28 05:29:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac633247-e734-303f-8cd5-1c4afbecbea0 | -10.25374 | -68.62412 | 2026-09-28 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d9f475e-5346-3f45-a11e-a8cc293266ae | -13.71837 | -48.81874 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6e8b4b9a-2623-3998-85e2-3e0619425366 | -13.71074 | -48.82444 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e0c7716-a788-361c-8874-144e19248a7f | -10.17455 | -63.55324 | 2026-09-28 05:31:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bf937b1-7b3a-3e81-95d2-282038101469 | -11.78647 | -51.05534 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95133a7a-a4c0-3ce1-b9fd-6468682b5f0f | -10.59664 | -60.78506 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c274badd-9cbb-3b9b-b5bc-2ad6104b572b | -11.77997 | -51.05902 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ff1106f-90cd-367b-a7a3-f05ba2bb52c7 | -10.81418 | -60.7386 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6708ad99-ce93-32e1-8017-cb051aa53421 | -15.1173 | -53.88753 | 2026-09-28 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9938dae0-466d-3fcc-99f4-98d1ac8fd517 | -12.14678 | -61.13952 | 2026-09-28 05:31:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1d48a76-acdd-3261-88ab-bb1ad1cf787d | -12.1286 | -61.15114 | 2026-09-28 05:31:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c090a50-14ea-3a2d-ae2e-c9d5af8d4b1b | -11.04053 | -54.04184 | 2026-09-28 05:31:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f450615f-b6ff-38d9-89df-a8f521ca939d | -10.82165 | -61.40992 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f4d50687-8458-35f3-983c-3a50c953ca5e | -10.82411 | -57.23135 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b7c431dc-5df7-33a3-b568-14c8309006e7 | -10.03695 | -62.45594 | 2026-09-28 05:31:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea6503b8-d10f-3c41-b5d4-6f32ce2a0f5b | -9.22211 | -67.59312 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3532547-85f6-325f-94ff-ecef7183ec63 | -9.68475 | -62.48905 | 2026-09-28 05:31:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b4ce372e-1b72-3957-9c06-445c07a31cdf | -12.29006 | -50.26808 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74cd1caf-2674-316e-a584-c601dcac8cdd | -9.19999 | -67.74197 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f30780e6-8f59-307e-9864-ea0f2b8366e0 | -11.78593 | -51.05976 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30700ec3-4b09-3406-9003-23c089e52139 | -12.16878 | -59.84234 | 2026-09-28 05:31:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8964a76-1677-3618-a5d8-0b7eb210c64a | -9.13554 | -67.93135 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2def1869-13e3-327f-a297-4cc621e0fdba | -10.57477 | -68.27845 | 2026-09-28 05:31:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0c07b2f8-7211-3cee-a4ce-7f25bca14693 | -13.50722 | -61.14325 | 2026-09-28 05:31:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7a4863f-a04a-3a56-a44d-03ee642778c6 | -10.82482 | -57.22644 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe953e0b-ee89-3fdb-ae42-ef58ce719af6 | -12.16157 | -50.37819 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6a5b237-8720-30a1-be53-6e251f215ba2 | -11.60975 | -62.39381 | 2026-09-28 05:31:00 | NOAA-20 | NOVA BRASILÂNDIA D'OESTE | RONDÔNIA | Brasil | 1100148 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e40c856-a70d-328e-9291-2e2e0bcc54f7 | -12.09718 | -50.29623 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2439729-87fb-3d99-b64e-fe8fd1d01676 | -11.84257 | -50.49546 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cf418ef2-aebb-3ccf-a99f-94bc785b8821 | -11.77401 | -51.05827 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27f2668c-dcce-370a-92cf-b541e6ca4928 | -13.46844 | -48.60532 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b69821db-318a-309c-9d0f-f56b5ad2d051 | -10.82442 | -61.41396 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f36aaed4-d0c0-38c4-9310-65cddfad9ebd | -10.82552 | -61.40694 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c104bfff-15da-30e6-a490-7ca998395e5c | -12.13968 | -60.76966 | 2026-09-28 05:31:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dce13965-c83c-34db-888b-ece05c48cc84 | -15.11768 | -53.88432 | 2026-09-28 05:31:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77cddda2-71eb-3cf6-bf6c-db10635c4a80 | -11.78993 | -51.05452 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e64ccccd-e793-3504-af5a-ad9717362242 | -10.81642 | -60.74628 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2f4bdfd5-a740-38aa-bfd5-2adba7a19a92 | -9.92843 | -60.71589 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fa60b301-8850-30ce-a8e3-9fa2259eabce | -13.46908 | -48.59911 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f2f8f91c-db10-3afe-8eeb-ad5533aa9e24 | -9.93066 | -60.7235 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85945836-9906-3af3-ae87-db00791ce486 | -12.21519 | -50.3543 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9428990b-0b20-358b-b7c9-f9742a81928a | -10.80356 | -57.20819 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a261c87d-2d94-3645-b338-183ee24b6c9b | -13.69725 | -48.82714 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1c32e524-6f10-39cd-be3e-7558e58ab5d5 | -10.55718 | -68.56044 | 2026-09-28 05:31:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 461f007e-e4e2-351d-9cb2-43db42d23c0d | -11.54731 | -50.5149 | 2026-09-28 05:31:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 471b5200-f51a-38fb-814e-0d3855cc3ee7 | -10.17415 | -63.06017 | 2026-09-28 05:31:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4ec59c0b-8665-3105-b172-94faece71bbc | -11.77973 | -48.32331 | 2026-09-28 05:31:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92e40acf-c28c-320e-8c4f-f16a277c7abe | -10.1674 | -63.05907 | 2026-09-28 05:31:00 | NOAA-20 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b310c873-fb54-3ec0-9a20-9e5ca7c8bbe7 | -10.82522 | -57.19597 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4491894b-0c20-3b53-b828-9061ebc52065 | -10.65087 | -58.77918 | 2026-09-28 05:31:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e397cac-1c85-341c-8233-bcc241c0bf41 | -12.22485 | -50.35978 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 387ca75d-e519-3353-9b29-082bc16cf2b8 | -11.30855 | -55.11045 | 2026-09-28 05:31:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a3d1e52-e506-3fa2-a34b-456112054f78 | -12.16216 | -50.3732 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 29747c4f-00ce-30e3-ac50-f458119ea17d | -10.24917 | -68.62328 | 2026-09-28 05:31:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9d952af-a7ca-3743-91dd-90e1be0ee896 | -14.48129 | -53.63352 | 2026-09-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f100cc58-6b54-3ba6-b2e6-3bc0d1be61f8 | -13.68395 | -48.81938 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1c3b413e-6f11-32a9-be6f-e34cc7d0a6b7 | -10.81632 | -57.23028 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e84d6d78-718f-36a7-95f8-d0d796e75b7c | -11.77943 | -51.06342 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a63bb71d-730c-3a47-9cfd-d29324420f3b | -10.82131 | -57.1954 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89301cc8-737a-35d4-acea-e670b37460f9 | -12.16605 | -50.39385 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7cf0fdec-3b05-35e3-8c9d-775ea00f1f11 | -9.53463 | -63.56206 | 2026-09-28 05:31:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e676f761-937f-359e-b9e0-2ba526dda81b | -11.54733 | -50.5178 | 2026-09-28 05:31:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8ed3239b-11a8-3fa7-8104-b2595cfaf334 | -11.77347 | -51.06268 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 905f31f6-6b21-371f-999b-68d3b99574da | -11.79045 | -51.05011 | 2026-09-28 05:31:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abe257a0-1cc6-3972-852d-a168335314d7 | -11.84199 | -50.50029 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 474897e4-f059-3379-8496-11bd1ca86792 | -13.45499 | -48.59745 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b68105d9-4f89-38f8-a771-9c57359b1517 | -10.81921 | -60.75037 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 22d6c330-0841-34fd-87ab-b8c5425648a6 | -12.14623 | -61.1431 | 2026-09-28 05:31:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae447b6a-869a-375c-97fd-6d05727bf1d5 | -12.13178 | -61.14809 | 2026-09-28 05:31:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd9d2ce9-13b5-301c-9062-ae3d9176f1dd | -10.54274 | -57.43929 | 2026-09-28 05:31:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd8b59c0-58bc-3f09-8b16-40b457a44063 | -12.79866 | -54.01295 | 2026-09-28 05:31:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99486fb0-414b-3f0e-9145-64c54bb568ef | -9.93176 | -60.71641 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63212189-1aef-32a3-b5e9-7aa3ebf13d1b | -12.59575 | -51.96511 | 2026-09-28 05:31:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcd8b66a-9522-3738-bb11-aad59b9c5109 | -10.81473 | -60.73503 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01176b37-2fca-33f6-b940-436183a6b0b1 | -9.92788 | -60.71943 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e983a7a7-b773-35a7-89f1-1bded96df8f5 | -9.16615 | -67.677 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cf20ddb-2fb7-3fa6-b2d4-d982c435b693 | -11.90888 | -50.61832 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5db01040-c7ff-35cf-8127-356b1c18c994 | -10.65446 | -58.77958 | 2026-09-28 05:31:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ba2c0d0-ad6e-3145-8bac-7c491fe11fc9 | -10.82331 | -61.42097 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4cb0da8-c977-3621-86ed-0a78ee3d9dbd | -12.136 | -57.1752 | 2026-09-28 05:31:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1b33fa74-8e50-3749-9d5a-7fc9cc9edfff | -13.04234 | -60.52075 | 2026-09-28 05:31:00 | NOAA-20 | COLORADO DO OESTE | RONDÔNIA | Brasil | 1100064 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e728af38-d14f-305d-99be-d0b6cc5d49af | -11.03568 | -54.04126 | 2026-09-28 05:31:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51362c2c-0a09-3e9a-a4b7-bb146395888a | -13.47046 | -48.6085 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d089153f-4f58-3f8c-8c2b-edb779b0a303 | -9.56217 | -63.13673 | 2026-09-28 05:31:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52949d38-e102-31da-b2b7-a399d438f003 | -9.16016 | -68.25058 | 2026-09-28 05:31:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baa80e91-c3a7-3ea5-9476-9e2f919cc1ec | -10.05235 | -67.54825 | 2026-09-28 05:31:00 | NOAA-20 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f3be7f9-89a6-3738-b9cb-0b3fef2f5eba | -10.8231 | -60.74733 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b8309eed-330c-32b8-bc3d-13a016863f05 | -13.71247 | -48.8167 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b58e952-66c8-3bab-87eb-faed195885e7 | -10.59331 | -60.78452 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c0ce5db-f294-37af-91e5-5cd2698e1f0d | -14.90167 | -49.49378 | 2026-09-28 05:31:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 82be5f3f-c41c-3b70-bd04-f522b172e453 | -11.0364 | -54.03586 | 2026-09-28 05:31:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e8cfc91-d601-37ea-9d4a-063d98e83e76 | -11.30405 | -55.10977 | 2026-09-28 05:31:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7066260-453e-3d23-9e3b-89d4eb5e4987 | -12.21859 | -50.35902 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2dbe117c-0a36-34b8-a3f4-c1afe49adff6 | -13.45767 | -48.59513 | 2026-09-28 05:31:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9bf52eff-1461-3d70-9376-1fb735f6a264 | -10.81363 | -60.74217 | 2026-09-28 05:31:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9acb5657-7ba4-37d3-8e25-1e9a19e14809 | -12.09657 | -50.30125 | 2026-09-28 05:31:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README66.md)
