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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cfa6d58-495f-36a9-86a3-ffdd596163b7 | -2.80767 | -54.13213 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d144fc7d-d0d5-3a3b-8b04-4edab6139781 | -2.94829 | -54.12415 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8bb8580d-fefc-361a-9299-1d6854ebb363 | 2.87465 | -60.55215 | 2026-10-04 04:55:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a2bfc514-0a4f-37b9-9c79-2fa599b364c6 | 1.83534 | -55.54013 | 2026-10-04 04:55:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e785d1a6-83ad-3f92-9a9b-7face1eee4a1 | -3.11231 | -50.28765 | 2026-10-04 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27595ce3-ea2f-3325-8a0d-27d96abfd17c | -2.77272 | -57.69207 | 2026-10-04 04:55:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b223480d-6a0e-3f53-9bed-bc2ddc00599e | -2.97377 | -54.08599 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b4b8a67-60aa-3722-a0af-3f071526c4c5 | -5.04416 | -44.46515 | 2026-10-04 04:55:00 | NPP-375D | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 94f04176-7fb7-32f8-9422-8a090ee88000 | -2.92798 | -54.1538 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7335a845-8f37-3531-8498-672d28d78db7 | -3.06782 | -49.53891 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 521f36a6-d936-3a98-aee3-75c09908cad7 | -3.30312 | -53.83536 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 125c6412-0c6b-3fd3-8e11-da58daacacff | -3.12902 | -53.75119 | 2026-10-04 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e573d001-a00b-3193-b1ac-d5ead020fea2 | -3.08008 | -49.54797 | 2026-10-04 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb5fc3a9-bb7a-3c39-877c-54056b8855cd | -3.47336 | -50.10032 | 2026-10-04 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1a7ce905-22e9-38de-8759-0cc35f053ff8 | -4.15381 | -47.54072 | 2026-10-04 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44b088c8-6d0d-3f8f-a765-8de22d74227c | -3.04508 | -54.23501 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff146939-db77-3e6a-a96a-0ca416694580 | -1.26149 | -54.56024 | 2026-10-04 04:55:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6766353-8b50-3b24-adf2-4695f48d54e8 | -2.96289 | -54.10055 | 2026-10-04 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abbd1416-224f-3ef8-a7a8-67902c6c6cf7 | -4.44531 | -54.96654 | 2026-10-04 04:57:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d18f1b4b-4ee8-3201-982c-4e4c7f29a219 | -6.00367 | -53.52341 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d8754c01-99ab-3079-a5cb-b95e480003c2 | -9.50803 | -54.63788 | 2026-10-04 04:57:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 906b9542-89d5-3f37-9030-b05df112bee1 | -5.88243 | -49.85904 | 2026-10-04 04:57:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e1a67ac0-1dba-35c7-83f1-9c78390d4c0b | -4.09711 | -54.32399 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0cc43d9a-606f-354f-9846-1549ea48b556 | -9.23518 | -46.68646 | 2026-10-04 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d21878d-b589-37ec-859c-a821f527ba76 | -8.52038 | -48.90903 | 2026-10-04 04:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1837d5a4-c0a2-328e-9ffd-3ee6aeb50edf | -6.20875 | -52.80362 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c938d978-1e9f-378c-b4b2-cba28ca9795a | -3.86669 | -55.82716 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c75bc2d8-1e67-3d80-9f5f-b275b58eff80 | -4.22121 | -53.48463 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e73ecc28-f4e0-3ff9-aed3-18d55e485cc8 | -9.48925 | -64.69331 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a5ae4de-8231-333b-8761-02e26e1ca3e9 | -6.4378 | -52.70668 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 800a265b-1069-385d-9ea2-2aa6742a5187 | -10.6007 | -53.9747 | 2026-10-04 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5475b23-5224-3768-a145-8c252666c24e | -6.01655 | -53.5335 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28588b64-b942-3362-9791-ec2065239563 | -3.79238 | -59.3774 | 2026-10-04 04:57:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f22f2e-7716-3fe1-8908-a8343202199f | -6.07987 | -53.4791 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e126b81c-2d75-3215-90fc-58efa58dfc85 | -10.83024 | -57.20972 | 2026-10-04 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1a03111-2fa0-3512-b0d3-4fa46fbb368b | -9.16658 | -61.40693 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6aaf8d00-3bb2-3709-9a50-b10a254e9d9e | -6.06991 | -53.47351 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7009a8c6-3098-3ffe-8f4f-45d3c6dc9d4d | -4.82135 | -49.87769 | 2026-10-04 04:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90c3277f-9345-37b4-862b-c9eba3fa3aa8 | -4.8172 | -49.28601 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b3d6d62-88c6-34a0-b1a5-17b3b69d6914 | -10.83901 | -57.20767 | 2026-10-04 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f16b79b5-42a3-37ce-b931-c58c17e37981 | -4.2124 | -53.47055 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7f407e2-97e3-3138-b3b3-afeff5878aea | -5.98477 | -53.66006 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 045712fc-c0f9-3b02-a613-9f78485e5db4 | -6.31819 | -43.34193 | 2026-10-04 04:57:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ff3b2d1-e683-3c83-a5bb-32334be0cba8 | -9.16726 | -61.40338 | 2026-10-04 04:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 63d64853-0650-31c6-bdb4-76fa29a7ce20 | -3.86253 | -55.82647 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9992261a-cb1c-35cf-a908-1bd0f5de0345 | -8.34575 | -62.82999 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dbf40a77-990e-375d-b104-5263669801cf | -6.06348 | -53.46844 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b467bb19-94f0-3286-9ce9-886e27554008 | -8.71225 | -61.39401 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 69f17a0b-4841-3811-b94d-b75009c3e948 | -4.5383 | -55.97353 | 2026-10-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f698278f-fe2d-3394-b69f-2f212c70c5fb | -4.81439 | -49.28189 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac9124cd-68c5-3b9c-80b4-5b8b7db22ae8 | -3.9616 | -55.77692 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0942cd47-1643-3447-9cef-a3e40c89382d | -10.59788 | -53.97033 | 2026-10-04 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44a8b465-42e9-35e6-a415-a2efb2603da6 | -5.56082 | -49.88464 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ac7879c-a69d-3a47-b2cc-bc465b270209 | -6.08051 | -53.47517 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e83c950-6360-370c-8b73-ed5305a796ff | -6.28392 | -45.84656 | 2026-10-04 04:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ecd577b8-7ed3-3ec9-848a-3dc6249ec7ab | -3.87053 | -55.81187 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| f72211ff-c439-3da5-9dd8-de23dc656460 | -9.36228 | -60.30744 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 775dc98c-2363-3370-a31f-1cc41c63a301 | -10.59725 | -53.97412 | 2026-10-04 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a645557-aa77-328d-9cb7-387c77b8a923 | -5.9988 | -53.53086 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 302bd1f2-cb8c-3421-9bcd-19315835f275 | -6.57408 | -44.14539 | 2026-10-04 04:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a7147f9-461e-305f-babe-8f24dbc0161b | -9.47512 | -64.33539 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44744b83-bf4e-3557-a1e7-41c5b990f9be | -6.00433 | -53.51942 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5cc69adb-03e8-3a91-924c-497d5f0a9bfc | -4.20653 | -53.46113 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61d34716-787f-3419-b4b3-0b03c96f0ce2 | -8.71088 | -61.40152 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 92715573-a729-37cb-8cc3-270b8865607e | -6.35925 | -45.61229 | 2026-10-04 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7792699b-a35e-374a-af49-0116a0dfebb3 | -6.20011 | -52.79903 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9e7d811-1f97-3826-b8fa-8c87d45799ca | -6.27805 | -53.15089 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dde0f8a6-c45c-3a6c-9590-b91685e07842 | -6.19668 | -52.79845 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3809bbc8-cd0d-35f1-9aab-30a9fe53b95e | -6.06284 | -53.47237 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 116eee44-b646-359b-9704-35ed626d2d29 | -8.51625 | -48.91241 | 2026-10-04 04:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c8a98a9-3c79-3669-8e60-1e040fecfe34 | -8.35006 | -62.84068 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d17d8033-b0c0-377f-ab12-b84edabc8cc8 | -9.3617 | -60.31055 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ba1ae786-2bf7-33e1-b830-8c12acbfd0a9 | -4.42294 | -55.74947 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07477913-dad1-3d83-bcc3-0d1581b19e21 | -5.99591 | -53.52637 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da9d00a5-3a13-3e04-aa10-be783339c45f | -5.5541 | -45.26505 | 2026-10-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f84ece53-6374-3d59-9d8b-7dbda40be10b | -6.35515 | -45.61145 | 2026-10-04 04:57:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21dd2ae8-a448-3722-8f34-43a2eef57454 | -5.99879 | -53.64162 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67ed7fda-7b16-3565-9c4f-22aeb6ad8e3b | -6.02074 | -53.53015 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4970c855-b6c3-3910-90bb-25d2f6a2e0d2 | -6.08319 | -53.30269 | 2026-10-04 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45f4d646-bfc0-3fa3-b882-dddad1fda134 | -8.51685 | -48.9085 | 2026-10-04 04:57:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b894744-1895-336e-ba2a-f5a6eaa444f8 | -6.44641 | -55.45466 | 2026-10-04 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e52b86ee-3a6c-33b7-9b22-a8d490be0921 | -5.80473 | -50.15681 | 2026-10-04 04:57:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 808432cc-0ba6-3c53-8d44-16787ca5f1f6 | -3.87388 | -55.80912 | 2026-10-04 04:57:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| db3205e1-778b-3068-99de-fa2154918e57 | -8.71157 | -61.39776 | 2026-10-04 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0441ebbb-e5f4-3e6b-b4d3-5719341c7e15 | -10.24228 | -49.65723 | 2026-10-04 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22fe2d6a-2af8-3211-baf6-424ab8b51ddd | -4.81837 | -49.28264 | 2026-10-04 04:57:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60a98693-97f3-3638-9192-238991f20b3e | -4.53892 | -55.96981 | 2026-10-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fcd6ffdd-048d-32f6-95d5-3307ca9e85b8 | -4.1131 | -54.4133 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f104a146-ad1c-3448-a372-44baeb613630 | -5.61418 | -47.43821 | 2026-10-04 04:57:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71a18c6c-30ac-3650-a28f-5f80ae1361b7 | -7.27811 | -49.25581 | 2026-10-04 04:57:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd088999-b16a-3162-8a7a-06f6d1d7a787 | -4.19867 | -53.46405 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63f9d886-326d-3228-9583-b6cb1de0a2e4 | -5.53065 | -44.95679 | 2026-10-04 04:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a971e56-f031-329e-bdbd-36f59e8c5f1a | -4.06011 | -54.31321 | 2026-10-04 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 4f8a6db4-6641-3c27-bad4-a2d06fb24598 | -4.2108 | -53.45762 | 2026-10-04 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab1c7150-e8b9-3e7b-8126-b9fecc82113c | -10.80209 | -57.24995 | 2026-10-04 04:57:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1bd7679-8b9a-349f-bdaa-a8d62bae6bc8 | -3.79292 | -59.37416 | 2026-10-04 04:57:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7518cb1e-a52e-3495-8dbc-06b1a4401880 | -9.46855 | -64.33395 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d1c1348-2ff1-320b-ac64-6291255fb08a | -8.54018 | -50.06833 | 2026-10-04 04:57:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1deee5fd-94cf-3dff-910d-5cd27dd1f9c3 | -9.48776 | -64.69339 | 2026-10-04 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5528c5c1-daa8-376e-a45c-cbbbe327eea7 | -9.78993 | -60.1396 | 2026-10-04 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README46.md)
