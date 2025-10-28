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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a79286fa-5fe0-3ddb-a254-2d4673b4d04d | -7.35961 | -47.63908 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09eec1a0-a887-3a4c-a1fe-45f959e50c7d | -7.27277 | -45.01107 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e6a8000-681c-3ce5-b8cd-787b045f3b94 | -1.55427 | -55.42084 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 14c965d5-a937-35ee-9713-cc6a9cbdeac6 | -7.12559 | -47.02145 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db4f304b-2ec6-3750-af9b-f7a7a0ef77fa | -5.86309 | -43.20512 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| feaa0df5-bd88-3091-adbb-2bb0d7145890 | -7.8127 | -46.45234 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 6ee9c6c3-3d6e-387e-9681-e9ae061a8ffc | -5.60881 | -47.09411 | 2025-10-28 04:42:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0aa6ab56-f8b5-341d-9c89-8b5134c961fd | -5.65939 | -41.11436 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fe1f569e-85b2-3607-ab36-b377233191f8 | -4.87734 | -47.5445 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95cdcfe2-26a7-3c95-bd9e-443778c14f76 | -7.47648 | -47.15073 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7e1e693-6ee1-3c80-8ee1-053796b92b4f | -3.58183 | -43.60141 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b7995837-16b2-330f-8830-59f25a4bbba7 | -3.52979 | -53.00157 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 014a0b1a-750f-341f-a840-b74210c7ecfd | -5.79833 | -35.60139 | 2025-10-28 04:42:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f47e72cf-a562-3841-a226-077617d857fd | -5.44139 | -47.39587 | 2025-10-28 04:42:00 | NPP-375D | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cee6102e-633b-3dc7-a149-8646cfbe3199 | -5.83751 | -47.65194 | 2025-10-28 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1d0e905d-eae1-38c3-9e09-bb62e81db7c8 | -8.15374 | -47.00602 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6862b27d-d1de-3879-b77f-8c96b399cdc3 | -7.85484 | -46.397 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7398f6e-4717-371a-9844-2a7e234f7538 | -3.58896 | -43.60984 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0b45f32-87ec-3ec7-8d7e-8b244c237ed5 | -6.44512 | -42.36213 | 2025-10-28 04:42:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| edcf2718-2512-38bd-bcdc-5bbdd48fd241 | -3.89466 | -47.33194 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 575721bf-d856-3eee-8d0d-77c645060b43 | -3.7961 | -43.32288 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 476d9a5d-5ac7-36cd-9ed7-df4c1b435755 | -6.70448 | -42.04309 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| f394116f-18ee-31bb-8385-b5943900c3a1 | -4.32718 | -48.0927 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e2a4d15c-6916-3432-81f9-f8bdc9d494f4 | -7.97421 | -45.52881 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fb175a2-f6fe-3847-a90d-a551f93b83a0 | -7.95387 | -45.50588 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ac1dc160-26f4-3ca8-bdda-b89060f37b31 | -6.36682 | -48.06344 | 2025-10-28 04:42:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c077a5e4-d7af-33fc-9cc2-eb26683fa104 | -6.99978 | -46.99411 | 2025-10-28 04:42:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cac96d6-08bd-3b94-9deb-1464dd60ceb6 | -7.64567 | -45.23902 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3612d36d-528f-3d10-89f2-322a88310472 | -5.65575 | -41.10375 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b1bf2276-6718-3094-b74c-641c92fc288f | -3.83789 | -50.19422 | 2025-10-28 04:42:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e061593-3051-339c-aaa7-eb2b9f391ae1 | -4.92737 | -48.55844 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0439842b-2a87-3277-8f48-bb7b5664c86e | -7.35322 | -47.6427 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bd87bbe-1d94-33bd-b2e1-03d9722ff509 | -7.94296 | -45.49932 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 5e84e191-2c9e-3b06-8f79-dc52c08b2f3a | -7.94824 | -45.49039 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97db317d-9e9d-379c-ae3a-b747b830146c | -8.14783 | -46.99665 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbf47993-655d-35ba-8b5f-2422002c5d81 | -7.55001 | -46.24464 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c5ca9f6-67af-3588-8cbc-1243adee398f | -8.03962 | -45.14423 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca56ca75-a77c-3f81-bf70-bf4e6b314327 | -6.58425 | -42.69296 | 2025-10-28 04:42:00 | NPP-375D | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 22c6827b-7f1e-3d08-8cd0-bbd84a954e63 | -5.61669 | -45.98305 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10d9bd66-ee42-3f80-b090-e377d71361d5 | -3.57387 | -43.62625 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca6c202c-3a50-33c9-b233-c4aa948b8a0f | -7.46763 | -47.1615 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f415c645-df60-388d-9a4e-87fc448c79a5 | -5.48771 | -42.16571 | 2025-10-28 04:42:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b39f4fbb-a1fc-3a7b-8599-dd0d7f5c1cc9 | -3.15572 | -50.33115 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ecfab42-7dab-3f19-a71d-b5d1c92e501c | -3.59341 | -48.98773 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 845095e4-fbfc-34dd-9849-b70b47681d62 | -5.60783 | -46.53387 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4b4e79e-02ea-3b48-80c3-5728e5b86b8f | -4.32997 | -48.09674 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5abb3856-e3d9-32f3-9ac2-ba3fb799787d | -2.30607 | -48.14172 | 2025-10-28 04:42:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 794ba2b4-a64a-39af-b67d-9a16d5a0b47e | -5.47199 | -50.15762 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23af80fb-3d10-310b-b531-16f7c757ebd9 | -6.13367 | -41.71501 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1a6add29-a58f-39a1-ba38-fb4d85fd859a | -3.79664 | -51.64156 | 2025-10-28 04:42:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3193dfac-7f62-33a4-bc38-82b29e95f7c1 | -7.96576 | -45.53244 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b05920e4-f0c2-3a6f-a47d-11c9de1b40ca | -4.18904 | -46.23012 | 2025-10-28 04:42:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5a3193fb-2e83-319e-8d99-0b18b9c45762 | -6.74046 | -48.1758 | 2025-10-28 04:42:00 | NPP-375D | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a077352-e148-3748-9a53-5a2dc68a03ed | -3.1384 | -52.99962 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 618f6bc3-fb2c-33a0-9799-a77a825388ee | -1.86767 | -54.52044 | 2025-10-28 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bec9651d-6ac0-301d-be43-8258c5375e10 | -6.48912 | -42.22219 | 2025-10-28 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 02b3d05c-9a24-3c05-9c1f-865491437e56 | -5.66033 | -41.14375 | 2025-10-28 04:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9789164b-2023-3e46-b2aa-67a680c79f63 | -4.96411 | -47.59095 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 428cb5c7-d96b-3d3d-8617-5b645c102e9f | -3.08591 | -44.44442 | 2025-10-28 04:42:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1486689d-9cda-3d16-99d1-e1957c437a25 | -1.69916 | -53.69127 | 2025-10-28 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a5fd52da-b3d3-354f-b7e2-dee8ea452997 | -4.84924 | -46.73549 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ecd6b9c1-3bdf-3dd0-841e-e58c77b98ce7 | -5.65123 | -47.63892 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e0301c3-a90c-3af7-8ae4-0116b5dfc263 | -4.3048 | -48.06038 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a41fb017-caa2-3c51-b080-d141ae850dba | -3.97436 | -44.31038 | 2025-10-28 04:42:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5a519fa-b1c8-3085-b853-409b87fe5344 | -6.48777 | -42.2316 | 2025-10-28 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5c6cf644-bed5-37cc-b01f-e966a8ff8513 | -3.58207 | -43.6276 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 821d0d82-2fa5-3813-b507-37e84023c0fe | -5.6262 | -47.61999 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 999969b0-1787-34d6-bedf-61bebd960a19 | -8.00101 | -46.19347 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4a93340d-8a3c-33f0-ae88-d709dca3c2b4 | -7.36951 | -47.80548 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e18ffde-0fcd-3eab-96bd-69470d809c7f | -2.95098 | -49.35159 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b06fac43-fa83-3b4d-855e-f84c1e41ec01 | -3.07903 | -49.47861 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3eeb195c-dcd6-3ef8-8e47-636c6fb5e202 | -1.70327 | -53.69193 | 2025-10-28 04:42:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70005342-2710-3c2e-b2f8-1a36371ffabb | -7.72759 | -44.05189 | 2025-10-28 04:42:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a2a8a36-f175-393f-b2c9-89953ff82739 | -6.98074 | -47.33446 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc793c59-a3d4-35eb-9cbe-7a21f1eb1d28 | -7.25769 | -45.00357 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 44219cf2-bc67-3f1b-bc99-118f7e421258 | -3.57079 | -49.02311 | 2025-10-28 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc4bf2be-47bd-300b-82cb-a47d8e9340ec | -3.58018 | -43.61231 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48b35b91-e199-35fd-99d1-685930b2b94a | -6.13568 | -41.83801 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e69cce47-aa0b-32e8-91af-86f84d1cbdfd | -4.75723 | -46.42121 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f62450e-282f-3f48-b133-c96664ec5afe | -6.1842 | -44.87079 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 533a5588-6eee-362d-ad83-803bba8c64bc | -7.35379 | -47.63906 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2e4fe8b1-d50e-35a9-8cae-2cc18e836978 | -7.5152 | -46.27522 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b6999bb-3b42-387d-be83-d226a281348c | -4.89578 | -48.58561 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0369e54-e394-34c0-8137-3cd88ff27774 | -4.88333 | -45.73972 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d21304c-7c1b-35df-9eec-4339e1d5545c | -2.75098 | -45.41375 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a0f5589d-88ae-3346-86e5-ad892a2c13b0 | -8.19086 | -44.44631 | 2025-10-28 04:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 69818146-5e2f-3ee8-abe5-ad242b0805b6 | -6.1587 | -41.67951 | 2025-10-28 04:42:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9f6e2c64-0407-3df4-adad-5613c0a52b2c | -5.84107 | -47.56205 | 2025-10-28 04:42:00 | NPP-375D | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f2245709-eb23-3cd8-bd93-5720b22d6f90 | -3.70705 | -47.6421 | 2025-10-28 04:42:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5ba73605-ebfe-319a-9c76-784039bf60f6 | -7.42033 | -41.87067 | 2025-10-28 04:42:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0c26f189-3ea7-38ef-863d-1a4669afac91 | -3.09926 | -54.6205 | 2025-10-28 04:42:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3906b13f-23c3-3baf-aa3a-a5f348c871d9 | -2.63943 | -47.29874 | 2025-10-28 04:42:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0945a2f-ebac-34ab-8663-d8d19a836ac1 | -5.92171 | -45.39592 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84ea64e4-9b9c-35b3-85a8-56b314228f92 | -3.12493 | -50.15234 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 514e15ef-f25d-3dec-a70b-88065c6885ba | -7.99782 | -46.19966 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16d7d305-b0e4-393e-9cf9-1be922da9ece | -7.9892 | -46.19606 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 4d250620-7369-3eb6-9645-a0c1bb95ed26 | -8.16446 | -47.00768 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e03cdc4f-51ef-3b44-acba-06cd16724d23 | -5.84364 | -43.27507 | 2025-10-28 04:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8529c150-b505-397a-84cd-bf88c30daba5 | -6.82161 | -41.20646 | 2025-10-28 04:42:00 | NPP-375D | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e529d5f0-dc3b-355d-9d0d-87d058679e30 | -5.80412 | -40.81219 | 2025-10-28 04:42:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README55.md)
