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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92f06e59-2697-3b44-a643-e52a81af08b6 | -9.18427 | -59.45044 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbd5010f-3251-3789-9567-54b26decd873 | -10.58369 | -51.36624 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9f5b6886-397a-3409-8932-9d38a320a7dd | -10.53203 | -51.30265 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a5fbbd5-eef4-3114-8719-fc22fe081e38 | -8.03963 | -54.85314 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44cf6eee-7ba1-3d62-8bbd-be32eb3a0f08 | -10.62986 | -46.10241 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f59cb5b-5ae1-37c3-b7ae-a56555e69a92 | -13.38122 | -48.00852 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba8dc2d2-5e3d-3afa-8c94-c0710523861d | -9.18678 | -59.44933 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37239e7a-0442-3a79-ba7d-f8d75ef4fee3 | -7.87004 | -54.72979 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4db5eeb3-dadf-3368-8740-6ef721f05bb3 | -9.88103 | -47.5883 | 2026-09-13 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18d721aa-8554-3eda-85b5-b97dfb03ca18 | -6.60226 | -58.85073 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a690cc9-b1d3-3a8c-8c93-61aaa52219e4 | -8.28331 | -39.97226 | 2026-09-13 04:51:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b1c56b8-36a0-3ab8-88d3-3c5984763e4a | -6.27999 | -59.93221 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4db60d0a-bbff-3074-9f21-c01e5c70e770 | -5.96804 | -57.76611 | 2026-09-13 04:51:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aa8a6667-3300-3ebd-a56e-16f391bbde88 | -7.18624 | -50.83785 | 2026-09-13 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5acc468d-1131-3327-9c8d-2ba8a679edd1 | -10.6858 | -54.1733 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ed866ddd-c014-3e92-856c-8ea1ad58d4f0 | -11.18751 | -42.79586 | 2026-09-13 04:51:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 6da0cef4-10f0-3f4b-a555-7e58e66c0495 | -8.04769 | -54.85454 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 365cdc50-5fc0-3d76-943b-147bdd594a19 | -13.31527 | -51.71802 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 14afad1e-5560-3cac-9141-9a7483ab203f | -7.50801 | -49.43464 | 2026-09-13 04:51:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9585b2fa-453d-3762-b2a1-3505593abbe2 | -13.45184 | -48.49065 | 2026-09-13 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b27f2aa4-efdc-3123-90c7-ab6946357d96 | -12.65096 | -54.69718 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 14c4b1fb-eb7c-37bd-b4b5-ac0cece261a1 | -9.1814 | -59.44837 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4ca29b7-ae79-33eb-8657-73ab79d3f46f | -6.61655 | -58.86409 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 156ed5c9-9487-3913-974b-7a66b3331888 | -8.05617 | -54.85688 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8613850-a27f-35d3-9aec-367a077da4db | -11.80551 | -46.38453 | 2026-09-13 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c3a00b4e-91e8-3dc6-9bf1-211e4e08b160 | -7.18681 | -50.83431 | 2026-09-13 04:51:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4588f965-e09a-3c39-a920-d82835479a92 | -7.52557 | -47.3344 | 2026-09-13 04:51:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 892148e5-dcc7-3473-a001-25c95b0c5a6b | -7.86356 | -54.69583 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45995e1c-24db-3928-86b3-08bde5967f8c | -6.31534 | -59.9648 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ab5c1db-caf1-3892-b0b2-2f88aeba30df | -7.46915 | -46.14886 | 2026-09-13 04:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a38029c-5dd8-35b0-b4a5-0163384a6995 | -8.11249 | -54.79426 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 713c42f1-f784-369a-93a0-dc9ee8fd8a10 | -6.5921 | -58.84535 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e125ffc3-e538-3cba-8a04-e86d76420d7d | -10.29089 | -49.99221 | 2026-09-13 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da72cb8a-a18b-3287-b4bc-7be01f43b774 | -13.8135 | -49.08146 | 2026-09-13 04:51:00 | NPP-375D | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9efb9e93-48cd-3c8a-b4ec-3e27e4a41fc5 | -12.66805 | -54.7095 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d19ef613-e47b-3657-8d8b-4eed7a6f62f6 | -8.11992 | -54.79911 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07ace92c-8001-3648-a3c9-3322b423a4b8 | -12.66312 | -54.67149 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36281331-744a-302b-b307-20d832ef95e0 | -6.60288 | -58.84728 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5423c94-604e-33a3-b351-3fc48eff4c63 | -10.62068 | -46.11108 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 98aafd78-2b5e-3ffb-8821-51b6defbfa4b | -11.43237 | -45.14511 | 2026-09-13 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11732780-e1c5-3d00-8c45-e2cb4d93dbd3 | -13.39264 | -48.00605 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 81bde7a8-23f2-34f1-90d3-8ac1f8309094 | -13.61865 | -47.88104 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| becc2383-40e4-331f-9379-08297ea10b1b | -11.24292 | -54.15202 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9296e590-d6e7-3a29-afcf-cd29eabdc578 | -10.53285 | -51.36144 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 14d693e6-2889-3867-b1ab-f3d9a868173e | -12.68623 | -54.67109 | 2026-09-13 04:51:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6c8b15ed-2712-3499-a3e8-531d6b25fbe7 | -10.53874 | -51.3037 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1a6e427-bb45-3f15-ae67-18be9fc80a0f | -10.94624 | -57.18497 | 2026-09-13 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 97297f30-dd19-303a-9af8-5fdb554a5113 | -13.75676 | -42.59706 | 2026-09-13 04:51:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 42bd2bf9-8ff7-34fc-945e-662ed42b2e14 | -6.81845 | -58.9974 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a01e6c6c-7549-3305-8552-4ae278923deb | -10.3569 | -46.67336 | 2026-09-13 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 347255b3-da09-3fd9-8df7-e646f418a8e3 | -8.02293 | -54.85386 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7317e938-9004-3820-af21-8e700579ff23 | -10.46956 | -48.63823 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aed50848-6ef1-33b9-a3e5-68c0b5389ff8 | -10.56646 | -51.34497 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24cbefda-1d2d-39cf-8f3c-db07bb949815 | -6.27488 | -59.9272 | 2026-09-13 04:51:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7dfcd10-55eb-319e-9a29-ec9c53cfef52 | -10.47231 | -48.63787 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9f94fb4-6340-34ca-99d1-807151652e50 | -10.54525 | -45.20057 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb4b6c1b-5d9b-3329-ae5b-7dd0e6ddb6bb | -10.46096 | -48.64849 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1933255c-47c3-33fe-8831-1878f6168f82 | -7.42862 | -55.52559 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3cb0b6d-3a20-35e8-a036-279189bb8d5b | -8.0574 | -54.84982 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea4a719c-8dd2-3a23-aa23-d43079a817ae | -6.73745 | -55.63923 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a37586e-aa52-3a10-a2ba-2fa1edc28328 | -9.59486 | -55.15139 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a265157-4e60-3b11-b4a7-dbf792123760 | -10.4712 | -48.65022 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3b24893-6ec1-32fa-85e2-aafd5f985efe | -13.30088 | -51.70096 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0c5528b-9b20-31b3-a5b3-29e9f3bc1e63 | -10.69184 | -54.1605 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| cff1a607-d2c2-37f8-b026-31d6bc9d60bd | -8.60851 | -55.22548 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be4efb9-3c7b-36b9-8e7c-f9d28f729a88 | -7.86321 | -54.72159 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b273d47-4c9b-34da-8c29-23a76f8f543a | -6.60086 | -58.8509 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a983f182-04d0-3272-98d1-7e3cef9bf1f1 | -10.93881 | -48.35213 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 248529cd-e19e-3ba1-966f-2643d3cc18f4 | -10.68952 | -54.17396 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 89f90893-509a-3615-a2d3-ba4b06138bd3 | -8.8497 | -50.71337 | 2026-09-13 04:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7786170d-4cae-39c9-bc16-353ca1badaa4 | -10.09938 | -48.86569 | 2026-09-13 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 760b7e2e-a590-3fc1-8e93-f4da72809a20 | -13.61749 | -47.88917 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edee6bf5-575a-3cea-b602-2a5e3d0d1a0f | -13.79095 | -48.79602 | 2026-09-13 04:51:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86f3d4b6-c983-3fdf-9d37-48574684dc2d | -10.56532 | -51.35207 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72a6f60d-0c3f-3321-b629-7ce6d09d3f53 | -8.06143 | -54.85048 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 283e9045-f728-3d32-b93b-ed130f3e56ed | -13.61322 | -47.893 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc79230e-3490-3718-8075-fc736169da6f | -12.76443 | -48.80673 | 2026-09-13 04:51:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9eeea1bd-73c5-37c8-9538-ecd9e0a5b96e | -10.47356 | -48.63505 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d5f7779-a5fb-327d-b7f6-87f514fdbe93 | -10.56589 | -51.34852 | 2026-09-13 04:51:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d22b5af-ec04-3f0f-b4dd-fb3dcfcb6e34 | -13.61381 | -47.88891 | 2026-09-13 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd611de4-79fd-380f-9909-452979679aca | -10.21612 | -45.19574 | 2026-09-13 04:51:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 425aacc5-b89a-3042-8a71-204283bf82d5 | -10.62625 | -46.1037 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 08ec0d23-58ae-38cd-b5ad-6461d3d94e3d | -13.2995 | -51.64565 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef19df6a-fabc-3a91-8338-928d319aa4e6 | -6.75641 | -58.96476 | 2026-09-13 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 338e3718-6192-386c-a1d3-523325875771 | -8.12051 | -54.79561 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdb1a3b4-8e31-39f4-905f-02ce22494e8e | -9.58165 | -55.15616 | 2026-09-13 04:51:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7afd7bc7-c68f-3a8e-af3a-e519f965bf0b | -10.47574 | -48.63842 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 330b72e9-d4b1-3409-bb94-43feb7a88e76 | -8.12333 | -54.80333 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4819a19c-0d40-37a3-b542-b76ac6d145ff | -9.17644 | -59.62293 | 2026-09-13 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| fdfacf55-7cb3-397e-941e-9d796a2a57c8 | -11.24595 | -54.13432 | 2026-09-13 04:51:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7ed367b-d366-3f7d-bf1e-8513af331a6b | -10.47401 | -48.64986 | 2026-09-13 04:51:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6fb6225-665b-3f1a-be96-6d0c34df7734 | -6.59606 | -58.84649 | 2026-09-13 04:51:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc858297-dd85-36b4-91ba-10b08170c8dc | -10.75691 | -46.24786 | 2026-09-13 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec614bdd-a480-3701-aa62-93e31fdd20f1 | -9.62506 | -49.02208 | 2026-09-13 04:51:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0787a89-b42a-3810-bb6f-de9e776fb875 | -10.09994 | -48.86206 | 2026-09-13 04:51:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95ae65be-9fac-343d-b45f-e07e80af2cc1 | -11.57748 | -46.98604 | 2026-09-13 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5b43e51f-0442-3c03-8591-bab895962236 | -8.02636 | -54.8581 | 2026-09-13 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aad072ad-0b8e-3529-9371-07453a8aeb71 | -7.34487 | -55.21254 | 2026-09-13 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d45cde46-8a41-3fa3-98be-40a4581d6583 | -9.71465 | -48.14366 | 2026-09-13 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0636c194-7033-3b77-9228-d5156c49cfbe | -13.3455 | -51.778 | 2026-09-13 04:51:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README36.md)
