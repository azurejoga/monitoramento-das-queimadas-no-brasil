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
| 46a6eb3e-37b5-3f26-8e35-a46fc600aea4 | -8.90061 | -60.57562 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b5c725b6-61e7-3155-b4d2-1ddfeb507c2c | -8.95934 | -60.56306 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fae55bf-63c8-3e1a-9de2-cec57154f6c1 | -8.95972 | -60.60309 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2faf6608-ff3d-3964-94cb-626a99bc8475 | -3.75999 | -51.61069 | 2026-08-10 05:27:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f894c29-eb63-3e8e-86a6-1638a81344f8 | -7.55085 | -55.57174 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 41d69782-fbc0-32ec-84d8-89d4c1ef086d | -6.14566 | -57.71438 | 2026-08-10 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6acac5ae-9c0e-3354-8313-cdc3084ef96d | -6.85027 | -56.40453 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 189c39c6-f7d9-37a3-9040-fdcce45dd821 | -6.46666 | -47.85104 | 2026-08-10 05:27:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d16b51c-a96d-3181-9cb2-27d5343df860 | -6.81276 | -56.43584 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa0905fa-aeaf-3494-bb0b-fe3d8f4370ad | -2.74489 | -54.59282 | 2026-08-10 05:27:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 264a76f1-b048-361e-a486-6b6e06150edc | -6.45986 | -47.85482 | 2026-08-10 05:27:00 | NPP-375D | ANGICO | TOCANTINS | Brasil | 1701051 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01622254-7837-3166-a7ea-1ceebbd38d23 | -8.95819 | -60.57014 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 095a861d-55ab-3ef4-acef-2b74be509347 | -4.40138 | -54.78598 | 2026-08-10 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f4276046-382d-36b6-9f3f-c202101d1eb2 | -8.96039 | -60.57777 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c89faeb-b863-31cc-a667-e16840c31845 | -4.39763 | -54.78534 | 2026-08-10 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c265d76d-e8c5-313f-bc01-3a57d0db96bc | -7.68888 | -55.16257 | 2026-08-10 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98beb9f9-dfbb-3576-ae71-63d921ba1fe6 | -8.96088 | -60.54185 | 2026-08-10 05:27:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c37224b8-4584-3553-af5d-e5cf6ffae779 | -6.82881 | -56.42591 | 2026-08-10 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7cb0f28-1315-3eff-8caa-66a1fdaf116e | -8.67966 | -62.87837 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efef6bd9-fc29-341d-979d-bb56b0137c40 | -11.17997 | -54.80868 | 2026-08-10 05:29:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e62d49a7-f5d5-3e69-b155-ccb439311550 | -10.90712 | -56.36523 | 2026-08-10 05:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7b45253-6adb-3619-8fc3-3e6391721b94 | -14.30555 | -54.93197 | 2026-08-10 05:29:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9e8ee83-7ba0-3731-9f90-64a49bd36600 | -12.09058 | -47.20522 | 2026-08-10 05:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c1be72-2649-3886-a21b-1da766c8b54f | -11.17583 | -54.80812 | 2026-08-10 05:29:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e5d0926-8fb1-36cb-90ea-e69a98945d29 | -8.68381 | -62.87749 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 633b4e1c-0751-3660-9448-b597fa7ca9d8 | -11.22069 | -54.03274 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bb12c71-a76a-38e8-9ee2-e90c054cbb8b | -11.24428 | -54.87858 | 2026-08-10 05:29:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f3f465c-7f79-3ab9-a905-37a6e34eac61 | -11.22565 | -54.02907 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3babc225-4944-3441-ab41-6f1705bb8feb | -12.36045 | -53.15077 | 2026-08-10 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c281e94-1bd7-38eb-80e2-5dce1b2b57d9 | -8.90824 | -63.96912 | 2026-08-10 05:29:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f0bd7045-eee4-3525-b1fc-64db8bd1e1d7 | -13.84396 | -53.88992 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 317845b3-1c98-3c1f-8d2d-38acc4f10992 | -11.47533 | -50.55789 | 2026-08-10 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71dc1f79-f96a-36ae-9235-0a0e8a8820c0 | -12.10502 | -47.20071 | 2026-08-10 05:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0f783ef-c70a-3093-9637-07411dd175f1 | -13.86873 | -53.65779 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c4c9991-f94d-3e1a-8391-8100a2d9a965 | -15.13303 | -52.69741 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1efd7a8e-f13d-3921-b5ba-238351475207 | -13.85446 | -53.69619 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 34b66217-3994-35b2-9c7d-7f1fc04561ef | -13.85187 | -53.69419 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af523d28-5730-3efc-b9f2-9e017a9a7098 | -15.15246 | -52.70644 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0fc04b28-0ad2-3bcb-92e0-04fb6a296e9a | -14.30072 | -54.93535 | 2026-08-10 05:29:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b807be63-3409-3b88-8dad-b6707be7069c | -15.14741 | -52.70586 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e567e7f1-b6b7-38a8-bbfc-f2e2f4528842 | -14.3061 | -54.9279 | 2026-08-10 05:29:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaf0ab65-7b3e-311b-ba0b-2cae39d0bcdb | -11.62073 | -51.09604 | 2026-08-10 05:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c02de59-e004-3085-aca0-94332d9943a9 | -14.12672 | -53.96773 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3468243-3daf-30f7-a3be-776c00910e87 | -14.12608 | -53.97255 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adced9f6-7982-3776-8ac8-1c816ea5bde3 | -10.87711 | -60.73038 | 2026-08-10 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8eaf601a-9f40-34ae-af28-e9ece17f2909 | -15.84713 | -48.13748 | 2026-08-10 05:29:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dac23e12-f7b9-3450-886f-75837e035147 | -13.85884 | -53.66128 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ce611480-f832-3555-b3be-da71dc1c6772 | -15.97151 | -54.21544 | 2026-08-10 05:29:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87aeeb61-9d0f-3772-b8d8-0e885aa24fa6 | -15.15682 | -52.71285 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e12d8e19-ec36-39a2-a563-b1d5873d81fe | -10.87988 | -60.73446 | 2026-08-10 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b490f3dc-2bc2-3387-b198-84dae461abf3 | -14.12556 | -53.98014 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1cb6569d-b1ac-3214-aa65-c9c0a51c0af7 | -12.19891 | -52.86372 | 2026-08-10 05:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03ea1a14-a63a-396c-98e4-6e8b2c4bdb76 | -14.31523 | -54.92495 | 2026-08-10 05:29:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f689d49b-c407-3e44-87d9-0d2e0b0305d2 | -10.88044 | -60.73093 | 2026-08-10 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e67a760a-13e4-397d-8bb4-d8dea7a6ede5 | -15.15176 | -52.71235 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 826543e0-ee49-31bc-8a7b-ffa3b49a0180 | -11.22505 | -54.03331 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aea7fbbe-af47-3856-a939-ddb070a092d8 | -8.68035 | -62.87415 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b222fe8-3222-319a-8b80-baee831d57f9 | -12.09815 | -47.19976 | 2026-08-10 05:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b800fcb4-814f-3486-bfe8-c36fb884fc3c | -15.13876 | -52.69843 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ececeeb0-a05b-3bfc-9132-2735a26b740e | -13.84467 | -53.69915 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a84a0bcd-eaa5-37bd-bd82-a77312034f27 | -11.99856 | -60.51232 | 2026-08-10 05:29:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acad0c46-95f8-3747-81c0-96b8fbd8f9eb | -11.22129 | -54.02848 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26cfcd4c-88e2-3fa5-8eba-6b186669ffae | -14.14014 | -54.01163 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 46926096-1a3a-3b52-9bdd-7dc5e5f9fb82 | -12.09874 | -47.19768 | 2026-08-10 05:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5a19906-698a-3f4f-a5e3-675ec768a9fe | -11.22496 | -54.03657 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60a510ad-94d8-3154-9aba-a1c928571c15 | -14.00933 | -53.83704 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9cb95b22-83cf-3b72-ab85-f68bdf8b8099 | -12.3598 | -53.1558 | 2026-08-10 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f144cbce-cf10-3c4e-91eb-c84e6ca16637 | -13.86811 | -53.66268 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b0ea5792-1d84-3fc0-ae31-7eeaf5e630a5 | -10.05999 | -60.49918 | 2026-08-10 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6286640e-7109-3e91-a01a-6428ed37ee4f | -9.06166 | -60.39514 | 2026-08-10 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03ab1946-bf6f-3166-8a06-a8c407863abb | -13.85387 | -53.67918 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8fb75289-d64e-3506-86af-a3dbac24bb74 | -10.93305 | -57.115 | 2026-08-10 05:29:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58ee75ac-3b5a-3548-8f23-9b22423f791c | -12.19344 | -52.86831 | 2026-08-10 05:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 98c881a3-0bed-3870-9458-0c052ff7e32b | -8.68105 | -62.86991 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f38a6f5e-bac1-38ca-8cc3-1e9117b0d4ea | -13.84792 | -53.8953 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3427b2ba-e2c3-31ba-984f-bb2645136ff3 | -15.15743 | -52.71297 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5f30dcfd-6b02-31aa-b900-1e56a1c2d91e | -13.85173 | -53.68035 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54e3cc81-e3b8-3037-8653-8253ff6b1352 | -11.22609 | -54.02806 | 2026-08-10 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65e420c3-78f4-3bdd-979d-4bf7e01d0c1f | -14.13442 | -54.02024 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8bb8974e-6b98-3bf0-af55-aeb24e53182c | -13.85509 | -53.69113 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24e1a3d8-819f-3cb8-9434-51113ecfbcf3 | -13.84527 | -53.69437 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33650bfe-c8f3-3ce3-82c6-5c8fabe016dd | -8.68453 | -62.87326 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d14fa4fa-a7da-3327-b0b4-0255f990edf7 | -15.13373 | -52.69767 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 406ebe12-9702-3608-a0e8-f999e85cee1e | -11.46932 | -50.56084 | 2026-08-10 05:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e89654e6-4290-3ec5-944d-a7e430ce106f | -8.67672 | -62.87354 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d518da7-6f08-3111-8a0a-dfce2af19d00 | -14.12675 | -53.97066 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fe03b3e-b0ff-33d7-90ba-c87032afeb80 | -10.05943 | -60.5027 | 2026-08-10 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bbf9d05-5046-3673-b0b3-48c5ee0f2ff9 | -8.68831 | -62.87114 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3ecd01d3-199b-3d46-8ef4-543ac543aeb0 | -14.00475 | -53.83633 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 003a327f-5bcd-33cd-9ffd-c588ff9835f9 | -13.84986 | -53.69531 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1052e211-5759-3d74-be14-a66010356da8 | -14.13955 | -54.01629 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8f0c71f6-cc8f-3757-88e5-af90edd6b59d | -11.92537 | -55.90308 | 2026-08-10 05:29:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f89a6fa5-a37d-38c2-8ddc-142166fccce3 | -14.30017 | -54.93942 | 2026-08-10 05:29:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 356baaf4-87e5-34f2-88cc-1d74b81e1988 | -10.90721 | -56.36813 | 2026-08-10 05:29:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f18a25c0-ce4c-3e74-b8ce-49bb86356ed3 | -9.72171 | -60.20312 | 2026-08-10 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e2c22b6-2763-3b39-a54b-7ad2dc026775 | -8.67742 | -62.86931 | 2026-08-10 05:29:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da668fa5-d943-3136-becd-54e40ec1832f | -15.15168 | -52.71806 | 2026-08-10 05:29:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b7a152f8-8be4-3f9e-8b39-ef98478e14ab | -13.86047 | -53.66503 | 2026-08-10 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d16224cd-788a-35bb-9fae-a784ffd6984a | -12.19822 | -52.86897 | 2026-08-10 05:29:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 376adad1-a70b-39fa-9e5d-9fc17553809e | -12.10561 | -47.19861 | 2026-08-10 05:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README18.md)
