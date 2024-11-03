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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee662607-e98f-3bae-96eb-161063b4a66d | -2.7602 | -54.4349 | 2024-11-03 04:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| a58a0b86-60b7-3fff-aba6-1c5ccb3ede6d | -2.7603 | -54.4149 | 2024-11-03 04:45:22 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 36bd8d82-c93e-3727-b3ed-49e9d3fc236f | -3.055 | -54.1474 | 2024-11-03 04:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 5d892cee-19f1-3aa1-b077-aa3a64a22881 | -3.0734 | -54.167 | 2024-11-03 04:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 05db58c6-4333-39d1-9c6f-f1df98b69694 | -3.0734 | -54.147 | 2024-11-03 04:45:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4cfc3a7a-a55f-3d67-8f0f-e6d2e15c19f8 | -3.1059 | -50.3105 | 2024-11-03 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 9e17f0bf-95ae-3a45-902f-7a51eb27fa7c | -3.106 | -50.2896 | 2024-11-03 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| 43015952-7d8e-3662-9f04-32c3d815a0ed | -3.1061 | -50.2686 | 2024-11-03 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 0350858d-8e8a-3517-ab9a-39a493563e1b | -3.1245 | -50.289 | 2024-11-03 04:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| d3954f21-7303-3ac8-a4dd-7916016bf93d | -3.2047 | -53.4179 | 2024-11-03 04:45:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| b696176c-f552-311a-9dfe-4953abc1b199 | -3.2415 | -53.3967 | 2024-11-03 04:45:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| afde3b9e-2a39-3d26-99a6-ae0a02d0d4f3 | -3.4749 | -50.3826 | 2024-11-03 04:45:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e0fafd08-e1cf-3e88-a8ab-f92ca7d17776 | -6.5241 | -41.4688 | 2024-11-03 04:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| d732f9ed-f50a-3bb0-9b34-7b41968d99fe | -6.5239 | -41.4929 | 2024-11-03 04:45:43 | GOES-16 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 93.9 |
| 7f9aebc6-bde7-36e8-8e3c-c93400f6dae3 | -2.66441 | -46.76094 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ea94839-9bca-36bd-ada8-9071bab18d1b | -2.66376 | -46.76522 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1952e387-3b2c-3eb0-9e91-8606e01883d6 | -2.66204 | -46.75182 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6e71fa3-c02e-394d-9ee0-72824e7a8545 | -2.6614 | -46.75609 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 805d7a85-4767-348e-9e16-72e25558e37e | -2.66075 | -46.76037 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3b15b17f-028f-312d-98ca-a942068008a3 | -2.66011 | -46.76465 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a293e20-db67-3653-a67a-36f04e887aed | -2.65838 | -46.75124 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3d5e34a-423e-3091-800c-e2c371cf979c | -2.65774 | -46.75552 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a1e1758-d923-337f-854a-c59d17fffe29 | -2.6571 | -46.7598 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 84cd281d-8972-3826-ad8d-0ecce6a3b514 | -2.65408 | -46.75495 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08bcee18-edf0-341a-9c88-ebb8ee77f40f | -2.65344 | -46.75923 | 2024-11-03 04:46:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40abe4d8-70d2-3668-b46d-0772a8f2a2ba | -2.57503 | -47.30338 | 2024-11-03 04:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86c82261-a2c5-3bd9-b8ef-710f92268160 | -2.57442 | -47.30741 | 2024-11-03 04:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45604ab6-a780-3589-8a3b-16dfa6b70ff3 | -2.57381 | -47.31144 | 2024-11-03 04:46:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a8011883-ba6d-32d6-9f41-a041d3f6a6f9 | -2.57148 | -47.30284 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f3a3399-6485-3945-af23-c1af46f801c1 | -2.57087 | -47.30686 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7d2038e-3cc3-3260-bcb5-b243aba2a535 | -2.57026 | -47.31089 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e0e6b83-89a7-36d0-b344-46e65e1ef3c7 | -2.56965 | -47.31491 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4b6ed3d3-6c18-3d08-b5f1-7aa9bddd7304 | -2.5661 | -47.31433 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f8c2dd1-7411-3b63-8cad-6bcfe27a19c8 | -2.56128 | -47.27733 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 194d244d-ca72-3a36-accc-49571b41c165 | -2.5609 | -47.27651 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4e7567a8-72bc-3e4b-ba6d-d68a360be5b5 | -2.56029 | -47.28053 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a8758372-810f-3cab-8362-788aa62da6db | -2.55962 | -47.26466 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 614e1f92-a945-3823-824e-197847fc98bf | -2.55839 | -47.31726 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96371153-8dbc-38c4-837a-f29a907bfcea | -2.55543 | -47.26814 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 318a41a0-c03e-32e1-bbbb-e8ecde76f3c6 | -2.54761 | -47.36476 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f79916f1-bbb9-3665-9fce-1c3100076d42 | -2.54754 | -47.36543 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 15059f60-174f-36d3-a164-fdfbdda3f3e8 | -2.53169 | -47.18567 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b975fcf4-9b9a-37c3-b6ce-8faa4b9fe6fb | -2.52963 | -47.22281 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 258c6af7-8153-3a4d-a283-36fec0e2ee91 | -2.52815 | -47.35013 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d643ea2e-2aaa-3542-8300-5829b5dd0b8b | -2.52461 | -47.3496 | 2024-11-03 04:46:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e127cfd-d6ce-350f-bb7f-b4ed10d55637 | -4.76044 | -46.40446 | 2024-11-03 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 077dacb5-c017-39df-9f11-89309a180b2d | -4.66209 | -46.37993 | 2024-11-03 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7c3b5b2-0223-369a-bf82-6ea4449d059a | -4.6598 | -46.37789 | 2024-11-03 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ccfa67cd-1ac0-398c-8573-b58fca050807 | -4.64933 | -46.31767 | 2024-11-03 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebc46f53-028a-35f3-bbb1-d1a990c4a403 | -4.56908 | -46.46051 | 2024-11-03 04:46:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23cd362c-0310-3909-a38e-a431417fa396 | -4.51023 | -46.62279 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f136c04d-9783-3250-9c9d-fa054bd5a6ad | -4.51019 | -46.62074 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| e372468d-1901-3132-babd-eb2b4fe25cd4 | -4.50646 | -46.62218 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c26b88c-51f0-32af-8bff-4185e691d05d | -4.5057 | -46.62482 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 112883ab-db92-3f47-8044-f21a762f25b9 | -4.23202 | -46.48796 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d1d16b0-4ec0-3b9b-999b-3cbc4bf636e7 | -4.22823 | -46.48735 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb10e1df-0918-3cfa-b5dd-83f1a81c1bb3 | -4.22444 | -46.48681 | 2024-11-03 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 468bb99f-3c78-34db-b633-b95b0d914606 | -4.13827 | -46.84653 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bded39f-214c-3c4d-8def-04bc820335d9 | -4.12041 | -46.88896 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62f34f2a-4390-3dfa-846c-3dfeed07dbe1 | -4.11476 | -46.16288 | 2024-11-03 04:46:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14a629af-e7ac-3b2b-8626-b1883d270952 | -4.11403 | -46.16769 | 2024-11-03 04:46:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e883dfbb-0739-3d19-a597-8ab62d80135a | -4.11091 | -46.1622 | 2024-11-03 04:46:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1480d544-d9b5-33f9-ad94-07618454671f | -4.11018 | -46.16703 | 2024-11-03 04:46:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 740e4bac-eebb-3bb1-a303-df447b08dd46 | -4.0564 | -46.93764 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d429862-57bc-3101-822c-0c2b2ff30fa2 | -4.05272 | -46.93709 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7d0e4ca-7bc8-36eb-874e-e0140bf6eb8b | -3.98903 | -46.4288 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f9b1995e-6466-3d6f-9e38-ff4819abd82d | -3.98875 | -46.4308 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c3694fe-2c3d-303d-8510-5436b3e38eaf | -3.98566 | -46.42566 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 619e085f-1182-3326-813d-99b703eb8f77 | -3.95453 | -46.47742 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6f6c051-1980-3143-814c-f620f9668890 | -3.90455 | -46.34888 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bbc59ea-01cf-3ef7-81aa-d906b7286252 | -3.90365 | -46.35089 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| abf7afa3-41b5-308b-b595-cc7b36cc88a8 | -3.84263 | -46.44931 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f11109cb-1c26-3ad6-94a9-7790edd69f1f | -4.12443 | -47.10882 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dfabed46-2a26-3a86-9d43-809ae108490f | -4.11283 | -47.11141 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d733397-eeb9-3c6f-ac2f-5c205cf18019 | -4.11224 | -47.11337 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83912aa0-265d-3e74-9e1a-74781e023865 | -4.10918 | -47.11086 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75d97a7b-8834-3d75-834c-32e5330a76e4 | -4.10859 | -47.11282 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb7c46fa-73b6-3b77-8d92-a1c3a99a7fed | -4.06119 | -47.37202 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cda9face-31b6-3af3-9684-cc98b3f5bfa0 | -4.04075 | -47.14158 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9889b27d-4b76-384a-bdf0-ee090e21c91c | -4.03774 | -47.13676 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2107cba9-1cff-3b92-95e7-76565587bdbe | -4.0371 | -47.14101 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 530457da-949b-3df3-86b2-62e28332eaf8 | -3.98198 | -47.23614 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00c36e1c-ae00-324a-837f-81a7b0ebe64a | -3.98136 | -47.24035 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a75b2cc-6ee2-3cdd-8570-4af07e577f64 | -3.9807 | -47.23779 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a710fb35-1a4f-3510-98c8-7375e1a464a4 | -3.97836 | -47.23558 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bec080e-8a6a-3852-83dd-11f0219a7656 | -3.94256 | -47.09803 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c830ed7-e13b-38cb-8022-253c43e38595 | -3.63205 | -47.31219 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3f11376d-4f32-36a0-8199-3cdd076007b8 | -3.62126 | -47.31058 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 60daf1c6-648e-316a-b24c-2aaefdca95d5 | -3.621 | -47.52202 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb83561f-42d3-3049-8a96-0e09cd6dc3bb | -3.6204 | -47.52601 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af09fda7-db7b-3544-9d31-1626679ff44c | -3.61684 | -47.52549 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff72c083-1a72-35e5-9cf8-b0e347fe0408 | -3.59311 | -47.30227 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 966e37f5-b701-396e-8b4c-ed52589644ff | -3.59249 | -47.30637 | 2024-11-03 04:46:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dee73943-6ac7-3338-9e51-e7d16a94e058 | -4.42391 | -47.25861 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6a2d7921-4f39-39b0-bb07-2ea60b5e7d05 | -4.42326 | -47.26295 | 2024-11-03 04:46:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6fcd719b-e915-3d36-94e0-8d0060d68fbb | -4.27017 | -47.06 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af8b83e7-a8b7-3bd1-b37f-1fcfbb9cd9a3 | -4.26953 | -47.06425 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4640afa3-ad58-3ed6-9987-cccfb4f3b2b4 | -4.26649 | -47.05947 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2721ccff-4ad8-384e-a004-74a457adab33 | -4.26585 | -47.06376 | 2024-11-03 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b251bc0f-1be3-3370-9a77-f1f09c5f8070 | -5.22564 | -47.45097 | 2024-11-03 04:46:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README37.md)
