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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e6da2ec-83ec-31d1-ae70-b54667e10ede | -9.1711 | -49.9835 | 2026-08-28 19:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| cb7f8e54-c623-3b41-8300-43496fe9809f | -9.02 | -57.5377 | 2026-08-28 19:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 96.4 |
| aef3bbaf-0f5b-3e64-979f-b4210e2af31a | -9.4329 | -51.6926 | 2026-08-28 19:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| ce42d630-8afe-3074-b6ea-bf6529aac861 | -9.9708 | -53.9419 | 2026-08-28 19:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 154.1 |
| c3af8a03-094b-3161-8e2b-d4401c097f4c | -6.8019 | -59.4008 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| f6d8ef21-2bf4-357a-83c5-cacd382d66d3 | -11.2493 | -45.0501 | 2026-08-28 19:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| e3f6cda2-d33a-320f-8793-f458adeaec53 | -6.1102 | -57.8205 | 2026-08-28 19:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| ceb3801a-40cf-3b61-adba-5e15ae2c74d5 | -11.7167 | -54.5244 | 2026-08-28 19:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 9341bcb7-39f0-3692-8e80-45190dca474f | -6.5865 | -55.4346 | 2026-08-28 19:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| d882dd27-1301-3173-836c-6ff9673557f9 | -14.9193 | -56.3237 | 2026-08-28 19:50:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 1f8ca095-4506-3481-9b34-df774407628e | -11.6212 | -54.5947 | 2026-08-28 19:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 614d559a-5426-3815-92ea-c520ddce17d2 | -11.7165 | -54.5449 | 2026-08-28 19:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 123.4 |
| d8344daa-7b80-3ff3-8b49-fcf11681628c | -7.4953 | -55.2862 | 2026-08-28 19:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| d3a7f64c-cfab-3d92-8f39-55edbba77763 | -6.9336 | -58.9514 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 5301ee0c-e347-3e30-bcd4-ebcad1aa8932 | -14.3759 | -51.7183 | 2026-08-28 19:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 262.2 |
| 1326be9f-a5ee-37c8-9925-3546aaedf1cf | -14.8817 | -52.6293 | 2026-08-28 19:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 4f1c751d-bf64-3a8b-b822-cd9f8ee0e9fe | -14.1784 | -48.7703 | 2026-08-28 19:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 74c9e185-6718-32a9-a546-7e3d7ff5e7c2 | -14.8821 | -52.608 | 2026-08-28 19:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 2f66f64e-08be-392a-a59e-8c31a37523aa | -4.924 | -55.7645 | 2026-08-28 19:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 9c453c41-30df-3389-998a-0187663f9180 | -6.5323 | -55.2378 | 2026-08-28 19:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 6f3d7717-3320-38c1-95e3-53d1f65e8a29 | -6.7833 | -59.4208 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 8176aa52-c37b-31c4-8c82-4927b317aa30 | -6.7698 | -55.6844 | 2026-08-28 19:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 115.4 |
| c4156716-97ee-3de8-80c6-2526d9f6dae3 | -6.9335 | -58.9707 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 57460d96-8a65-3692-b37e-c34f30b5d233 | -13.5991 | -45.772 | 2026-08-28 19:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 2dddc600-bfff-37b6-a5db-5880e5fbe8d7 | -4.3021 | -59.4826 | 2026-08-28 19:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3cdbaa4b-ec2a-3bbe-a630-60d04a666885 | -6.7831 | -59.4594 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7c8bb808-0ce7-37f4-83ad-a2416fe06992 | -11.4972 | -45.084 | 2026-08-28 19:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 51fed40a-214d-3986-9d9c-8469586cb6b0 | -11.2128 | -53.9976 | 2026-08-28 19:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| f6f0a1e6-b1da-3ca6-bdf5-925864977d0f | -6.0005 | -57.6689 | 2026-08-28 19:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| fddbedda-4ade-3bfc-a2ca-135a046c10db | -6.1656 | -57.7988 | 2026-08-28 19:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 35f1cb91-1182-3267-94c5-a49081d1b651 | -6.8357 | -59.9571 | 2026-08-28 19:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 15df77b9-0df0-3a40-a906-4710d7cfc503 | -7.9169 | -61.3671 | 2026-08-28 19:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 116.1 |
| c1913307-8e63-377b-b876-060beac56fca | -6.7832 | -59.4401 | 2026-08-28 19:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| b25063cf-0685-351d-8ea8-d6342e861d18 | -6.7513 | -55.6853 | 2026-08-28 19:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| f5eb0819-8a4a-32d1-be57-a7b4a0a2f93e | -12.7603 | -44.2608 | 2026-08-28 19:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 229.6 |
| b5c93bcf-a2ec-332f-9915-4451791f30be | -11.2317 | -53.9958 | 2026-08-28 19:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 936d04ec-6d5a-3657-92ba-3cae9f16273a | -9.0012 | -57.5585 | 2026-08-28 19:50:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 0f94a2b7-5b0e-37d1-ae3e-d72ffff3fb43 | -10.7407 | -54.0401 | 2026-08-28 19:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 40870381-44b5-3f8b-9d90-2e117f649b99 | -6.7514 | -55.6654 | 2026-08-28 19:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 121.3 |
| 3cad5c3f-8a3f-3d0d-9cc7-a5eabfe37e7c | -8.5781 | -54.797 | 2026-08-28 19:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e7188dc8-8b09-3fbe-92ce-bc334e2a04c3 | -16.177 | -45.6265 | 2026-08-28 19:50:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 6580ee02-5854-3ebd-8f37-454b510bbec1 | -8.5971 | -54.7553 | 2026-08-28 19:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 97249ded-ed15-3236-944c-90686ccf9b67 | -12.7797 | -44.2576 | 2026-08-28 19:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 48dfee21-7188-39bd-b2df-c802973c1e06 | -13.471 | -57.0373 | 2026-08-28 19:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 5f559b50-0db6-3702-ae41-d4dcb1958716 | -14.3569 | -51.6995 | 2026-08-28 19:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 448.6 |
| 6e2d3bd2-e4ed-37a9-9398-0db187aead9a | -7.3663 | -55.1734 | 2026-08-28 19:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7bec747d-7e69-398b-9868-b5ea5125154a | -3.1815 | -61.1613 | 2026-08-28 19:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 06722c94-cf58-3e2f-ba90-65a381afcedc | -9.1525 | -49.9639 | 2026-08-28 19:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 3526da51-8bd3-3893-9dd6-979c60a6d904 | -8.0301 | -48.0145 | 2026-08-28 19:50:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| b133ad5d-adad-3cb1-bdd7-791f376cb5c1 | -8.5969 | -54.7755 | 2026-08-28 19:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 5fcd8c3c-5c81-3311-989d-3e10f3a2c413 | -8.5783 | -54.7768 | 2026-08-28 19:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| bc887378-2876-3ed8-bbe1-d6ad46f2e375 | -8.5365 | -55.2826 | 2026-08-28 19:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 9ebe1d0a-cca2-35db-a82b-2bce41fd2d84 | -6.1841 | -57.7786 | 2026-08-28 19:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| d3660926-5add-3a18-bd6f-e2abd54fc214 | -4.1699 | -60.6874 | 2026-08-28 19:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 021412d6-f9dd-342d-916f-3f6ae0b07ce4 | -4.9765 | -56.2961 | 2026-08-28 20:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 3fcd91e6-c36a-3874-b0e0-cda723f957a1 | -6.7699 | -55.6644 | 2026-08-28 20:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 201.1 |
| 2f2df0be-1f37-3221-9dbb-ac229a5ccb6c | 0.1549 | -60.412 | 2026-08-28 20:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 98e3c64b-d078-3d17-8fca-ef8cef4b5677 | -14.3565 | -51.7208 | 2026-08-28 20:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 140.8 |
| f1a2490a-bdb1-3d06-8dd7-fd7c5324f5cc | -6.7248 | -59.9998 | 2026-08-28 20:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 565f8810-8f9f-3c8a-bb5e-431cc2a11ca4 | -14.1978 | -48.7673 | 2026-08-28 20:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 63ed5926-b329-38f0-a635-40830a4dacd3 | -11.0439 | -57.262 | 2026-08-28 20:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 64e92850-6093-31db-8171-1e7f4998e122 | -15.5773 | -56.271 | 2026-08-28 20:00:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| a2df28ea-eab1-3931-b3e9-ce086f0e1d7c | -3.6034 | -60.5284 | 2026-08-28 20:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 81b925c4-b315-3d6d-9b44-65cd9936268b | -9.2477 | -57.0697 | 2026-08-28 20:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 6041ed08-a50a-394a-b60a-b7397d30343a | -5.6406 | -43.4153 | 2026-08-28 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8cb8f91b-a98c-334a-9b4c-ac37d59f7d16 | -4.3021 | -59.4826 | 2026-08-28 20:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 29d34edd-3a3c-37ea-8423-086b286dd65d | -5.871 | -57.7715 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 43f2ea8e-b188-33f4-bbf6-19c49ccb69aa | -5.9078 | -57.77 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 6c78c07e-5d05-397c-b2c7-f0a2494b6ea9 | -12.7608 | -44.2373 | 2026-08-28 20:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| f8c7f595-c061-316e-bce2-3ed1b2c82688 | -2.533 | -45.3168 | 2026-08-28 20:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 8c4a813c-5d19-376d-ab4a-1e53b1b45a7c | -14.1835 | -52.8456 | 2026-08-28 20:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 15af8bae-b8e4-3bc4-9330-752c9d421ad9 | -6.3137 | -54.7482 | 2026-08-28 20:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 99f365d5-07f7-3a02-9836-f390d4be041f | -6.7247 | -60.0189 | 2026-08-28 20:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| ffda6ea8-7912-3223-a077-e5eb49d3f3b3 | -7.5478 | -61.3056 | 2026-08-28 20:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 434.3 |
| abfd3484-d5c4-3fdc-9fc1-c32e75e33d72 | -8.8219 | -70.638 | 2026-08-28 20:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6617c09c-480f-37b0-9488-5bddf326f001 | -7.5663 | -61.2858 | 2026-08-28 20:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| 0ae69868-102c-3faf-bdcd-b2682f996eaf | -7.5662 | -61.3049 | 2026-08-28 20:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 537.2 |
| 2e1eb236-4373-3f2c-a03c-671aee7fc6a8 | -14.1597 | -53.1219 | 2026-08-28 20:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 67846bfb-dd6e-3483-b65f-fe2ec8a6c5d0 | -14.1784 | -48.7703 | 2026-08-28 20:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 113.3 |
| a97bd92d-efd7-3ae1-82df-c477939bc7f8 | -9.971 | -53.9214 | 2026-08-28 20:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 79329c06-6c6e-34a6-b098-403182cded95 | -14.3762 | -51.6969 | 2026-08-28 20:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| dfa00bb4-0d6b-3208-a4be-dc9d85767348 | -9.1739 | -56.9754 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 67355fcb-833a-31dd-9030-08ad11d5375e | -5.6219 | -43.4167 | 2026-08-28 20:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 77.7 |
| ec4d6fa2-3401-3be1-bcd0-77f0b54151bc | 1.2055 | -51.0182 | 2026-08-28 20:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c6847a68-9e58-36cb-9413-cbe100496226 | -3.1998 | -61.161 | 2026-08-28 20:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 4d8b151e-72e9-3c3a-9747-e4ba9b101aae | -7.0474 | -55.69 | 2026-08-28 20:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| da3833d0-bd48-3888-97de-02749a0afae5 | -3.8947 | -60.9399 | 2026-08-28 20:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d03c4b88-45ff-3c84-9e4a-d78224ba845b | -9.8739 | -60.2955 | 2026-08-28 20:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 262.6 |
| e97e75cf-7364-3008-bd34-2d67e3ae8a70 | -14.9386 | -56.3216 | 2026-08-28 20:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 6f1df82b-ce3e-3e91-9969-98e8f0335db4 | -9.1978 | -61.0809 | 2026-08-28 20:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 635e2bac-3b4f-3c8a-95a4-491d65f20cf5 | -6.425 | -43.7478 | 2026-08-28 20:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| eb99f474-1e91-3f78-9fa0-d4a620df907b | -3.913 | -60.9395 | 2026-08-28 20:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 57b04798-f7a6-373b-a502-58b78f43016d | -6.8358 | -59.9379 | 2026-08-28 20:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 2eb9b52c-02eb-313d-b189-48cff82c1d7d | -6.1657 | -57.7793 | 2026-08-28 20:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 147.4 |
| 4f62d893-872c-3dc9-ad61-8e156b0613c0 | -10.5149 | -59.6184 | 2026-08-28 20:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 5b093633-8d5c-3b78-8c98-55c1281ce698 | -6.77 | -55.6445 | 2026-08-28 20:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| e3d96869-2ff2-3742-a997-a2ba789c755c | -6.7652 | -63.054 | 2026-08-28 20:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 2f5a2031-7410-3a4c-9455-4d6234b35075 | -14.1788 | -48.7481 | 2026-08-28 20:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 89.4 |
| c255aebb-db43-372e-92f8-dec611da55e7 | -17.5789 | -51.6498 | 2026-08-28 20:00:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 2ee331e2-5bee-3fc3-960f-2cfdc277197e | -21.4947 | -55.4019 | 2026-08-28 20:00:00 | GOES-19 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 122.5 |


[Clique aqui para ver as próximas entradas](README176.md)
