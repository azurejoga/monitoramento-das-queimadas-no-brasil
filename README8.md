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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e75a19c-df77-35a5-85b2-c73bf9a57598 | -3.0154 | -45.4577 | 2024-11-27 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 32ad313d-5d64-3ab4-949d-3824d61c178b | -6.5407 | -35.1917 | 2024-11-27 00:40:00 | GOES-16 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 0bd4d0b8-eaee-34ba-ba64-7f62627f1d57 | 0.6535 | -50.8359 | 2024-11-27 00:40:00 | GOES-16 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 41.0 |
| c323cdfc-d26e-3672-b53a-a01f0aecc1d3 | -1.9562 | -45.7137 | 2024-11-27 00:40:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 7810fa29-f988-3793-848e-7134363da682 | -4.2115 | -50.8782 | 2024-11-27 00:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 09c70f6f-3914-3d8c-b9a6-dc60643b5b72 | -1.791 | -52.7376 | 2024-11-27 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5b66c62f-c61a-30fc-9944-1963a7493623 | -4.7381 | -46.5816 | 2024-11-27 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 657428af-2c5e-3880-87ba-d048d07b2ad4 | -5.9975 | -45.3607 | 2024-11-27 00:40:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 399c4db8-e3d7-3390-a56b-6a8eb9fb0091 | -3.5226 | -52.1448 | 2024-11-27 00:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.1 |
| c36c94be-d0a3-3270-a2e8-42ea725b30a6 | -4.7195 | -46.5827 | 2024-11-27 00:40:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 8f925d19-20f8-3a02-842b-7e73b0ac4647 | -1.6444 | -52.4951 | 2024-11-27 00:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| cf926bd1-be0a-3647-911d-6e7d4df468c7 | -2.9967 | -45.4809 | 2024-11-27 00:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 4e7263e4-2bab-3574-941f-d04027039118 | -2.824 | -46.8199 | 2024-11-27 00:40:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 8e9f9a89-2519-3435-a030-534e065f2dd6 | -2.1928 | -53.7839 | 2024-11-27 00:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 4ebd5b80-865a-34da-9fba-c972eca00351 | -2.8346 | -54.1326 | 2024-11-27 00:40:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| c9892689-54cd-36a2-b383-cfdc2d911710 | -5.9788 | -45.3621 | 2024-11-27 00:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| f5102ac0-5934-30c7-8c7c-69ee649a695a | -1.6629 | -52.4336 | 2024-11-27 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 08a754a0-6a8a-397a-89fd-06e990dd76b2 | -3.0154 | -45.4577 | 2024-11-27 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 109.1 |
| ebbb9d80-bb0e-3dd5-80dc-908f13b1b9f9 | -2.8346 | -54.1326 | 2024-11-27 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| e64b6315-732c-36a3-9f9b-4df2d5cd4491 | -1.6444 | -52.4951 | 2024-11-27 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| affdee83-082a-32e5-8cf2-fbd78532306f | -2.824 | -46.8199 | 2024-11-27 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 018bf5ae-7256-3f1f-a1c6-f8160c612bcf | -4.7195 | -46.5827 | 2024-11-27 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 72f00a70-bbe6-3ca8-923d-ab15f6f5d7c5 | -4.2114 | -50.899 | 2024-11-27 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 5e1b8fbf-bdfb-3a95-beeb-9e8876c56372 | -3.1691 | -48.4394 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 440.1 |
| ab6cad51-c324-33d6-8cd2-58975a660f6c | -2.8163 | -54.1129 | 2024-11-27 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| dbe9f511-2301-3e50-9910-68910fd2d3eb | -1.9561 | -45.7361 | 2024-11-27 00:50:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 85d3ef4e-4c12-34ad-a76c-93d821d005f8 | -2.9967 | -45.4809 | 2024-11-27 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 78.2 |
| e61c507d-ffc4-39a4-9f3b-a358f18b92a9 | -3.1876 | -48.4387 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 204.8 |
| 1061030b-def3-32dc-91e5-0f6c4d9129c4 | -3.5411 | -52.1442 | 2024-11-27 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 32506e48-8ebf-3ccb-8051-17dd9abdc1ae | -3.0578 | -48.5076 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 16ebe79a-8fd0-353d-8018-f1993a616321 | -3.169 | -48.4609 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 792832d5-000e-3603-9c92-8ecbd2ed0768 | -1.9376 | -45.7365 | 2024-11-27 00:50:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| a2bd3832-845d-3258-abae-1cdd7fced5bf | -3.9675 | -48.0634 | 2024-11-27 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| efdfd991-8fd5-3a07-b2d6-9d2d4d27ab0d | -2.9968 | -45.4584 | 2024-11-27 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 124.9 |
| cdb15881-dc18-3d9b-a0ee-10cd0db7c243 | -1.9376 | -45.7141 | 2024-11-27 00:50:00 | GOES-16 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 98.9 |
| 5cb51420-31bc-3eb3-8ec6-33afe134279b | -3.5226 | -52.1653 | 2024-11-27 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| b9df228a-a9ef-37f1-930f-dcb54be221b5 | -3.1692 | -48.4179 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 198.1 |
| bc46b1cb-4f40-3b9c-8e16-e46c19ea3d92 | -2.6987 | -45.6705 | 2024-11-27 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 93.0 |
| b37c1430-3d19-3887-b849-542092819a3b | -3.0393 | -48.5082 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 359e3b0e-dc62-364a-9ceb-f6c0ca2a6727 | -3.1506 | -48.44 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7602a347-6b68-3ea2-aa3a-f43fbaa4aee4 | -2.8163 | -54.133 | 2024-11-27 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1d17e26e-6fcb-34fe-8645-2cf9a14df153 | -4.2115 | -50.8782 | 2024-11-27 00:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 46036add-6ea9-3b02-9d8b-e5a409b9462b | -3.0153 | -45.4802 | 2024-11-27 00:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0f9acb7a-bce9-37a0-80d9-4d9c38f463db | -4.7381 | -46.5816 | 2024-11-27 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 624c9ce3-01d5-3704-a170-2eb620ae1349 | -1.6813 | -52.4333 | 2024-11-27 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 540be144-16cc-3594-8366-099f85c61f42 | -4.7383 | -46.5595 | 2024-11-27 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 45.8 |
| f4b232fd-0d49-3a03-b0e4-ede1a1cfab07 | -3.541 | -52.1647 | 2024-11-27 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 94acc3ea-28d0-3268-b910-0b232a335e61 | -2.8239 | -46.8419 | 2024-11-27 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0c984b65-b0b2-31be-9bf9-46efa98db512 | -2.6988 | -45.6481 | 2024-11-27 00:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 5e4bfd83-5f20-3c8a-a17f-bd20b428e911 | -3.1877 | -48.4172 | 2024-11-27 00:50:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 003b153d-31c0-3f49-9282-043789d8f989 | -4.1417 | -43.8135 | 2024-11-27 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 808f8e91-9d21-3d93-801d-9f971d238fd7 | -1.6813 | -52.4537 | 2024-11-27 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 82598fcb-3c24-3ead-8fdc-2d838acad4e3 | -2.1928 | -53.7839 | 2024-11-27 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 458b409a-d195-34ff-ab4e-b22642a5243f | -2.8424 | -46.8413 | 2024-11-27 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| d6210eb9-533f-3efb-834e-dc38ef7a487b | -1.6629 | -52.454 | 2024-11-27 00:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| cf8b78d1-dd7a-3eae-92d3-53c302a0a813 | -3.5226 | -52.1448 | 2024-11-27 00:50:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.9 |
| 4ddd97fb-a460-3be9-8409-a53bcf470033 | -1.9562 | -45.7137 | 2024-11-27 00:50:00 | GOES-16 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 5f1a8e73-1255-380e-b52f-e09aa6cced85 | -2.8347 | -54.1125 | 2024-11-27 00:50:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 571ff224-d8cd-353a-b9de-f3e3128a39f1 | -3.0392 | -48.5297 | 2024-11-27 00:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| fb709d5f-937c-348d-bf70-e045e50edc05 | -3.9674 | -48.0851 | 2024-11-27 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 5010b711-19c5-306d-aec4-e6eb85ad4b7b | -4.1604 | -43.8125 | 2024-11-27 00:50:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 63026ea5-7902-390a-8017-9718be429052 | -2.8425 | -46.8193 | 2024-11-27 00:50:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 64def449-36d4-30b2-9ebc-7134be488bf0 | -3.058 | -53.28 | 2024-11-27 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 6fc258bb-9b9b-3d8f-b5e6-9c212a437e26 | -4.7197 | -46.5605 | 2024-11-27 00:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 73.0 |
| bc8fdf73-a16f-3cb2-8eb7-5b37f2c624c7 | -15.3015 | -56.522099 | 2024-11-27 00:59:00 | METOP-B | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50e43552-9bfe-31d5-84b5-c4ed7e8b1ec7 | -3.3932 | -50.313702 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68e9e390-8f98-3457-abc8-473b3fb76239 | -3.6902 | -50.226101 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4bb61f8a-7754-3df9-be0e-1ca6882c5e70 | -3.8994 | -50.589401 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88900391-c835-3c1b-b3af-96d1618d377c | -3.0404 | -48.484299 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 029b0b24-c52e-305b-947d-eebea86b63ef | -17.7071 | -54.074299 | 2024-11-27 00:59:00 | METOP-B | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5ece4357-8a99-3768-952e-8fa968ba4761 | -3.1756 | -48.452202 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 474e987c-405c-3938-a0fe-ac0b262c32f4 | -5.9779 | -45.378601 | 2024-11-27 00:59:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ccc09a70-c8bd-38bf-bc8e-e88ac9069f52 | -3.4945 | -50.481701 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5009656f-1de4-3d43-ac01-7f6ce13b23ee | -20.391199 | -47.470501 | 2024-11-27 00:59:00 | METOP-B | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 77df0218-8058-3667-a16f-3d9cfed39a6d | -3.0939 | -50.348202 | 2024-11-27 00:59:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15fb46df-915b-3219-bc2b-526a087fe328 | -2.8172 | -46.831501 | 2024-11-27 00:59:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a2a3eae-831f-31fc-bac8-b6c6618a2d5d | -5.9694 | -45.3452 | 2024-11-27 00:59:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 456b7044-2f0b-390b-b62c-cda34011a689 | -3.0308 | -48.486599 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb503672-3103-389f-941c-f9bd5ca2c975 | -5.9789 | -45.3428 | 2024-11-27 00:59:00 | METOP-B | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7865b2db-3ed8-3dd0-9fdb-044397c84d37 | -11.7785 | -54.681801 | 2024-11-27 00:59:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f44704ac-be29-3ffe-8759-d96862b0c327 | -22.1451 | -50.855999 | 2024-11-27 00:59:00 | METOP-B | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb4407eb-004d-3b87-99af-716dcd982ced | -4.2099 | -50.9034 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f7ffbd3-3182-3c1c-84ee-bfb0cd7bfc57 | -14.9209 | -52.8675 | 2024-11-27 00:59:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1135e2b3-0461-32d0-9541-9178aa9390cb | -3.0458 | -48.507 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae4cbb9d-a559-3f62-ad61-fa00fba0ce34 | -3.3739 | -50.102001 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91a8da5e-a3fa-3fa5-a63b-d241d7edab4e | -3.5276 | -52.151699 | 2024-11-27 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43d276de-a67b-3d34-8c56-9af7ac6a46c5 | -3.7391 | -54.259201 | 2024-11-27 00:59:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10f46cd8-21ec-3107-96d0-a8a7605ae14b | -21.3293 | -55.9431 | 2024-11-27 00:59:00 | METOP-B | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 959f7999-c169-337e-8365-9b0609c6c957 | -3.9031 | -50.605099 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6eaa7b4f-646d-3dce-93f8-c42b4fefa7f4 | -14.9189 | -52.859299 | 2024-11-27 00:59:00 | METOP-B | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb8e732-bf54-3cc4-8ab9-2a7de7007084 | -3.7715 | -52.403801 | 2024-11-27 00:59:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 277d745a-ddbd-326e-9185-ea0815d9b316 | -3.1606 | -48.431702 | 2024-11-27 00:59:00 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81657668-04ca-308c-acf6-b1e014d6c080 | -3.5903 | -53.260101 | 2024-11-27 00:59:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7413e691-834a-3a7d-bc71-ca9e0830d706 | -11.79 | -54.686798 | 2024-11-27 00:59:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fb9ac9fc-bb2d-39cf-875d-e52667f3efd3 | -3.9129 | -50.602798 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 760dd304-9e7f-32db-acd9-d9181c8a48fa | -3.378 | -50.119301 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99db2f6c-6c55-3aa1-8ddf-d618427c04b1 | -3.6792 | -53.554798 | 2024-11-27 00:59:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21c7eb82-b56d-37ed-85ad-e80a0c15a2f0 | -3.4475 | -50.283199 | 2024-11-27 00:59:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3184df02-b718-35e3-b9f4-0f76041dfc0c | -3.0416 | -48.532001 | 2024-11-27 00:59:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e14f429a-baa1-315d-85ca-5017f17d77b1 | -2.8268 | -46.829201 | 2024-11-27 00:59:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
