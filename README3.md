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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08a7abdc-671e-38e4-8179-c8f0d7f6de66 | -2.907 | -54.4916 | 2024-12-19 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 54b3c41f-2da4-3590-81ac-9e235b4becb1 | -6.1229 | -43.9578 | 2024-12-19 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| e43263c7-b7f6-3b78-81a1-79ae079de6db | -3.5968 | -44.5289 | 2024-12-19 00:10:00 | GOES-16 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| ca5fa136-32bc-3a79-8aa2-288ca5d78bca | -5.2108 | -43.3067 | 2024-12-19 00:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e18d6101-d0e0-3d56-866e-b65bee1ffe67 | -1.7518 | -45.8299 | 2024-12-19 00:10:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 14151fb4-1787-3a66-be3c-265810e434b4 | -5.211 | -43.2833 | 2024-12-19 00:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| c1b89d71-7996-3d5e-af9f-9cf50c6ab1b1 | -3.2321 | -46.7836 | 2024-12-19 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| 6164b6b1-1ee7-3af3-b830-be81e3ccc48d | -6.1229 | -43.9578 | 2024-12-19 00:20:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 39e42a40-29ed-3a19-8f2b-69ffe83267e8 | -1.7518 | -45.8299 | 2024-12-19 00:20:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 6bcbb42c-24bc-3d98-8818-806507ac7b2e | -2.907 | -54.4916 | 2024-12-19 00:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| db5d0e2d-5cfa-31bf-a835-95575755296c | -3.2135 | -46.8063 | 2024-12-19 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| b1be7c83-f367-3931-a3d6-327f4a613972 | -3.232 | -46.8056 | 2024-12-19 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 667d558d-7816-3846-aabc-264681af6a99 | -3.2136 | -46.7843 | 2024-12-19 00:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 8815d3fa-ce68-30c5-a787-24e4ca1fc17d | -3.2507 | -46.7829 | 2024-12-19 00:30:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c52f304d-37d5-3dda-b7db-570ca90c6ea4 | -3.232 | -46.8056 | 2024-12-19 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 227.7 |
| a6470845-2876-3489-b164-86a976d65833 | -3.2506 | -46.8049 | 2024-12-19 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| fde33f9f-8440-3a51-934c-0d7e34924a8c | -3.2135 | -46.8063 | 2024-12-19 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 221.6 |
| 7756f988-a22a-32e6-a1c9-d5fab86289e1 | -3.2321 | -46.7836 | 2024-12-19 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 237.6 |
| 8553809f-162c-3cd5-a798-c478c8f3faef | -4.4854 | -45.4128 | 2024-12-19 00:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 06e649d6-7638-3e9b-8725-3aacd74ff096 | -3.2136 | -46.7843 | 2024-12-19 00:30:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 220.5 |
| 2e81b31d-9879-3e37-bd79-9afd6459e59b | -4.4853 | -45.4353 | 2024-12-19 00:30:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 64b65f45-bac6-315c-9f8a-b8776438feb7 | -2.907 | -54.4916 | 2024-12-19 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 52aaeca5-0604-31e5-b58f-101eb9b32e3f | -6.1229 | -43.9578 | 2024-12-19 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| fefe66d4-2a8c-3c6b-9dd8-480c1aad79b1 | -1.7518 | -45.8299 | 2024-12-19 00:30:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| f245b6ed-56d0-3484-bd18-46288e099527 | -8.0122 | -35.1029 | 2024-12-19 00:40:00 | GOES-16 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 65.3 |
| b4bc5505-ce54-3f7d-97a3-ad13cc96a952 | -3.2135 | -46.8063 | 2024-12-19 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 78748b89-4a9c-3a25-a175-8b9d7b0c0761 | -4.4854 | -45.4128 | 2024-12-19 00:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 8e08cb03-8484-3cef-800a-89b36e881d87 | -3.232 | -46.8056 | 2024-12-19 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 267.9 |
| 09005bdf-2671-38cf-833a-648d52931c64 | -6.1229 | -43.9578 | 2024-12-19 00:40:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 818024bb-6bd4-3f69-9232-19ef91b870e9 | -8.0118 | -35.1305 | 2024-12-19 00:40:00 | GOES-16 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 75.1 |
| 787547c2-7dd9-396e-a6a9-12d17e9b33fb | -7.993 | -35.1058 | 2024-12-19 00:40:00 | GOES-16 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 78.1 |
| a5ece57e-2cb9-3d5f-9be0-45260de64e35 | -3.2319 | -46.8276 | 2024-12-19 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 300bd2fc-e3dd-32c9-9fbf-172ab565724d | -3.2136 | -46.7843 | 2024-12-19 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 3db3e239-47b3-3d7d-9fef-257b192d47fb | -6.3878 | -35.2373 | 2024-12-19 00:40:00 | GOES-16 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 219db45a-d38b-36b4-b8cd-fc154f64955e | -4.4853 | -45.4353 | 2024-12-19 00:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 03124cc3-7abd-3b5b-88d2-5bced73d8da3 | -1.7518 | -45.8299 | 2024-12-19 00:40:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d0f38c62-8c5b-3cee-b096-b583ad43960a | -7.9926 | -35.1333 | 2024-12-19 00:40:00 | GOES-16 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 113.9 |
| fd709f10-622e-3a9e-8af8-267c765c17af | -3.2321 | -46.7836 | 2024-12-19 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 272.4 |
| b18d7f33-ab5e-3cbd-8a84-d1f7c5062043 | -7.4737 | -35.3172 | 2024-12-19 00:50:00 | GOES-16 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 71.0 |
| 9556e620-82d8-3e25-a6a0-f01d783182e1 | -1.7704 | -45.8295 | 2024-12-19 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| f0b76bab-3ecf-37f5-bdfc-4e130319c1ac | -6.1229 | -43.9578 | 2024-12-19 00:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 76a977bd-d6cc-34b1-870d-2e15de08266a | -1.7518 | -45.8299 | 2024-12-19 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 73a10164-7f04-3791-8a26-8605df5b2152 | -22.20312 | -53.1576 | 2024-12-19 00:56:00 | TERRA_M-M | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 15.4 |
| ae00dfc2-3c49-3265-8c35-0ced15222b1d | -22.55135 | -48.36703 | 2024-12-19 00:56:00 | TERRA_M-M | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 07825b06-9036-3ac4-8cb7-5ef61225f22a | -19.06345 | -52.88092 | 2024-12-19 00:58:00 | TERRA_M-M | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 9ed352eb-d446-3468-856d-bfa9d58c2af3 | -17.97924 | -54.0093 | 2024-12-19 00:58:00 | TERRA_M-M | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 20a04809-a00b-388d-bf83-a59c183e5feb | -19.06513 | -52.89584 | 2024-12-19 00:58:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 727025ed-705c-3a1f-8db1-0f3036e015e3 | -19.12788 | -53.46115 | 2024-12-19 00:58:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e096eaf2-a894-3330-b48f-da48d8402041 | -20.78193 | -49.85349 | 2024-12-19 00:58:00 | TERRA_M-M | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| 83a36c29-ae6d-36a9-a2dd-782adf7cdc23 | -6.1229 | -43.9578 | 2024-12-19 01:00:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 8df71262-8624-32ac-8722-620b1f8fed76 | -3.2321 | -46.7836 | 2024-12-19 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 270.9 |
| 266e6b72-ca27-3544-a949-690b7e743866 | -1.7518 | -45.8299 | 2024-12-19 01:00:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 65e37e3e-e74e-3fea-8e86-ea5484ad5d81 | -3.2135 | -46.8063 | 2024-12-19 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 119.7 |
| 67c6c962-1f1e-3ee1-96f8-29b022663942 | -3.2136 | -46.7843 | 2024-12-19 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 3d3e6ebb-87d4-3bea-a561-d17b42464aa5 | -3.232 | -46.8056 | 2024-12-19 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 295.2 |
| c74d60c8-d40e-319e-948c-8fd8f727c3f4 | -13.30621 | -52.43536 | 2024-12-19 01:00:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 56c16733-3f87-3bbc-9ba3-018fed6983f0 | -13.49376 | -52.95029 | 2024-12-19 01:00:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 96ccbb0b-be2f-3bad-89ee-84b2f857cc96 | -13.30768 | -52.44666 | 2024-12-19 01:00:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 829fa8a2-17ee-35cd-8642-bb5e81730388 | -13.92252 | -54.59968 | 2024-12-19 01:00:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 53a7bd26-6583-3897-9b20-e68cd0b83d09 | -13.88937 | -54.62022 | 2024-12-19 01:00:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| f9933cbe-df57-3ef6-abd3-81ca4b3a68e3 | -13.92445 | -54.6157 | 2024-12-19 01:00:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.8 |
| f05a41f1-fd23-35ab-b5f1-87ea2bd3fb06 | -12.23012 | -54.31285 | 2024-12-19 01:00:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 29.4 |
| b1537f0d-60ab-31a6-9812-a3272816c290 | -13.48351 | -52.95164 | 2024-12-19 01:00:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 8751ad9e-5dee-3c2e-953e-c84a3c309fc3 | -4.87536 | -41.37976 | 2024-12-19 01:02:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 78addc3b-0178-309f-86b6-d76e5996dbc3 | -3.22812 | -46.79225 | 2024-12-19 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 544.7 |
| 2a2a3a63-38be-3301-9374-9468f0c51763 | -4.47553 | -45.42391 | 2024-12-19 01:02:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1cafa320-2eb5-3a85-9601-7af9db371aad | -4.881 | -41.41452 | 2024-12-19 01:02:00 | TERRA_M-M | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 49.4 |
| 5af82232-6594-355b-b8d6-d48cb9d84cb5 | -10.51001 | -49.12427 | 2024-12-19 01:02:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37f632f6-dcf0-3c7d-91d9-32d31a7311b8 | -3.22881 | -46.79775 | 2024-12-19 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 498.1 |
| dc7ce22d-124c-3e83-871c-6b33f7de2f02 | -4.04141 | -49.76514 | 2024-12-19 01:02:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 42042a90-de0e-3051-843f-7366eaca2270 | -4.87083 | -41.38669 | 2024-12-19 01:02:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 31.7 |
| f185bb51-1614-3417-8332-529dc4e2803e | -4.8058 | -44.0397 | 2024-12-19 01:02:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 9f976337-7ca4-32a9-bfa6-db51602a0182 | -6.1259 | -43.94771 | 2024-12-19 01:02:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| a9b2a2a8-5a5f-3679-b524-b8a62eadf086 | -4.48009 | -47.98554 | 2024-12-19 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a5b97937-3fb5-30be-82c1-61719a4d6479 | -3.23091 | -46.81253 | 2024-12-19 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 43d6c2cd-3d35-3bea-a85b-521334d22df1 | -3.68381 | -49.57703 | 2024-12-19 01:02:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 08e67be0-ee5f-304e-bc3e-d214e14253f1 | -4.33064 | -48.29815 | 2024-12-19 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 04a82eb7-57d4-3c7f-b9ec-0c5dbc1747b8 | -4.3445 | -48.46444 | 2024-12-19 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8e14e3e7-401f-3344-b4a8-4513f1174c33 | -4.04277 | -49.77464 | 2024-12-19 01:02:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8dc40e04-32a7-35d1-88ca-a5a66131f0d0 | -2.92669 | -49.43303 | 2024-12-19 01:02:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 132c6be1-8fd3-372e-b6a4-49153d44c56f | -4.96836 | -43.71486 | 2024-12-19 01:02:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| f25895c0-2a2d-3048-811e-9da9089bdfa1 | -4.35729 | -48.19654 | 2024-12-19 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9f5f83fe-0e26-3b93-8156-c726b75c3295 | -4.97311 | -43.7084 | 2024-12-19 01:02:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 7642e076-9153-3f55-af9e-03a69ef97065 | -6.12943 | -43.97012 | 2024-12-19 01:02:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| ef27b426-7544-32bd-bc9b-20c558efd8a9 | -3.61107 | -48.99476 | 2024-12-19 01:02:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7901fae0-c9bd-3c76-840d-67a169e03697 | -3.99417 | -46.36888 | 2024-12-19 01:02:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 45179b8a-a601-32cc-92a7-f8e7bc6955d2 | -4.34607 | -48.47536 | 2024-12-19 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2aea5daa-7728-3fa0-9ea1-ffa927d251c7 | -3.99397 | -46.37806 | 2024-12-19 01:02:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 1a91ec5d-204e-3cf0-9487-47243467de95 | -4.79058 | -46.39628 | 2024-12-19 01:02:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 85731359-1d38-38bd-9a09-c155c43d2def | -4.35584 | -48.474 | 2024-12-19 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 2f6083e4-aafb-3637-a6c9-98af123b4d78 | -3.21759 | -46.7994 | 2024-12-19 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| d4184cbb-6d80-3e23-876d-4f78fd15e5b5 | -4.98671 | -44.20456 | 2024-12-19 01:02:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| ba409ca3-dc61-31ec-9635-cd010920bab2 | -3.60151 | -48.99614 | 2024-12-19 01:02:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 607ace42-1736-3e69-8b71-b0e89397dc2a | -4.33221 | -48.30909 | 2024-12-19 01:02:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 48f8c1d3-68e0-330a-a008-b762b95263ff | -4.11197 | -49.41502 | 2024-12-19 01:02:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 0ef72795-1580-36de-831d-c12ee409a600 | -4.88769 | -41.38491 | 2024-12-19 01:02:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| ffaa8b34-17da-397c-9502-81d2ab5c749f | -10.50106 | -49.12556 | 2024-12-19 01:02:00 | TERRA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f82b12dc-cfec-31c5-81a6-124874bbc629 | -3.22672 | -46.78301 | 2024-12-19 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 1afd59d4-091d-3029-85e0-b98acc0b5ef8 | -3.21548 | -46.78465 | 2024-12-19 01:02:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 8f7faf81-86b0-38ae-91f9-f1ac8540dc48 | -3.68243 | -49.56731 | 2024-12-19 01:02:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |


[Clique aqui para ver as próximas entradas](README4.md)
