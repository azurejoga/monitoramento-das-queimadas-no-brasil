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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6291596e-76de-3dd6-afb4-a9588ad7cb91 | -19.20632 | -45.37923 | 2024-11-28 03:42:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb23ea87-ad93-347a-89b8-c2c76c4a0247 | -20.46087 | -46.14592 | 2024-11-28 03:42:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a6d451b-7577-392e-ba02-f10d419f5ea2 | -20.35596 | -47.45487 | 2024-11-28 03:42:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ac3136c3-2868-3345-89e8-678bcabb759b | -22.90323 | -43.66051 | 2024-11-28 03:42:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 347affd4-5eb7-30c0-900e-b737ab47c2a2 | -23.71313 | -50.56396 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.3 |
| ca2192df-0d16-36cf-8cd6-8b98dab89af6 | -19.52225 | -47.3301 | 2024-11-28 03:42:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2930af0f-f798-3d6a-974d-38e2dd1b346c | -23.71453 | -50.55812 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 497d726a-19a5-34b7-8889-5bcaa89388fb | -21.83002 | -44.18899 | 2024-11-28 03:42:00 | NOAA-21 | ARANTINA | MINAS GERAIS | Brasil | 3103603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ae111d96-f8c6-3bea-99f0-67954ffaa61f | -23.71438 | -50.55463 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 2fcc7b3c-5023-33d9-a407-84183ddedd27 | -19.52618 | -47.33461 | 2024-11-28 03:42:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74c308a4-8625-3c28-815f-04cc7bd75cc2 | -20.89928 | -43.82125 | 2024-11-28 03:42:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baf5315b-a839-3566-b34c-b551f5d4d50a | -19.3322 | -45.62631 | 2024-11-28 03:42:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52b02e2c-4826-3226-a4ed-410d18eb3601 | -19.30343 | -45.53826 | 2024-11-28 03:42:00 | NOAA-21 | QUARTEL GERAL | MINAS GERAIS | Brasil | 3153707 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a711608-d293-3d27-85ef-0d3ca840a1ef | -23.713 | -50.56025 | 2024-11-28 03:42:00 | NOAA-21 | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 19b98a54-1ecd-3b85-9593-f2429f85c03e | -21.12362 | -48.6449 | 2024-11-28 03:42:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1918773e-e53f-34eb-831b-027bf9a14204 | -19.52141 | -47.33404 | 2024-11-28 03:42:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9126a099-9dee-3932-ad41-aa176a87fd68 | -21.06181 | -41.81269 | 2024-11-28 03:42:00 | NOAA-21 | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74b70417-0236-3b85-8e0a-d51f68f1891e | -22.46717 | -47.13556 | 2024-11-28 03:42:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ed0296f-dfbc-30c3-b80b-d3bbed96d9dd | -22.0585 | -49.73626 | 2024-11-28 03:42:00 | NOAA-21 | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 45553aa1-1065-3bd3-be4d-7393b9ebdf77 | -20.35048 | -47.45365 | 2024-11-28 03:42:00 | NOAA-21 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e1278d7f-a30b-3568-b05e-2853f7e72424 | -21.49591 | -45.11016 | 2024-11-28 03:42:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| da6553bc-8ed5-30e3-aa06-d99bc883e954 | -19.5216 | -47.32915 | 2024-11-28 03:42:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37a0a7dc-ac55-3567-8a50-293393d47d98 | -22.46643 | -47.13892 | 2024-11-28 03:42:00 | NOAA-21 | CONCHAL | SÃO PAULO | Brasil | 3512209 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f5fcd2b3-93e6-3a1c-94a2-57adeb317750 | -22.0573 | -49.74129 | 2024-11-28 03:42:00 | NOAA-21 | ÁLVARO DE CARVALHO | SÃO PAULO | Brasil | 3501400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6f881c17-a9e3-3529-a230-7e40b7038cc8 | -20.44409 | -42.36273 | 2024-11-28 03:42:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d16488f6-10b9-32d7-96c4-d353057693ae | -6.1737 | -42.5985 | 2024-11-28 03:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 44.4 |
| a795d76d-ab00-3702-8dd1-0c4944164655 | -6.1041 | -43.9593 | 2024-11-28 03:50:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| da4d3261-4f7e-369b-8e14-e8335d0a66c5 | -3.3837 | -50.1125 | 2024-11-28 03:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| fc38aee5-ad50-349e-ae4f-07bdd052cc6c | 1.2537 | -55.9467 | 2024-11-28 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 0590e932-475d-3bae-8a9b-58110f451413 | -1.5897 | -52.271 | 2024-11-28 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| fff6c5a0-26e0-36c8-af9f-88dc1f676f98 | -6.1735 | -42.6221 | 2024-11-28 03:50:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| ead0d113-0220-3953-8eac-2878c0e1da36 | -3.1113 | -53.8242 | 2024-11-28 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d81d67f7-1938-3497-b2a9-2548d2d83f19 | 1.2538 | -55.927 | 2024-11-28 03:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 1596fdbf-bf92-380a-9c93-6c1ba302f3d1 | -5.9788 | -45.3621 | 2024-11-28 03:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1741f3fd-1369-3c22-bb63-84b145e076f8 | -1.53807 | -46.06326 | 2024-11-28 03:57:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78cc0072-bc96-3248-a0bd-cade2cd76498 | 0.98204 | -50.12415 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 041cb327-e873-36c8-a219-676c0604d778 | 0.98275 | -50.12973 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 03fdc707-8d6f-3e46-895c-5beff10333d8 | -1.55073 | -46.0447 | 2024-11-28 03:57:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1957fb6f-a5e0-3ca5-a5cc-10a4c8eb41cc | -1.08806 | -48.20871 | 2024-11-28 03:57:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5ec302e-c03e-3e59-b8fa-93487acc4bb1 | -1.53728 | -46.06825 | 2024-11-28 03:57:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ef6b8da-d4d3-3c2a-b8eb-e388aa957ee7 | -0.58534 | -51.7065 | 2024-11-28 03:57:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e254d97-dff0-37ee-b94f-977cd3bfe007 | -1.08749 | -48.21229 | 2024-11-28 03:57:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 85aceaab-b871-3d0e-bdf0-e7c5873cd985 | -1.5444 | -46.05399 | 2024-11-28 03:57:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dce72020-e615-3d5d-bc66-c735c3946ca8 | -1.74427 | -46.21038 | 2024-11-28 03:57:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49891a1c-73c3-3f20-bfd3-9cd111a83967 | -1.52853 | -47.30005 | 2024-11-28 03:57:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 865b2e6f-b829-38f4-8e8a-8508e9d009d4 | 0.98284 | -50.12942 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 201f0bd9-a348-3b1c-bb9d-5a168cfa38c1 | -1.4455 | -47.11652 | 2024-11-28 03:57:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49a3085b-485e-3799-819d-4cf3c17796bf | 0.9756 | -50.12514 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 05b2ab61-c1ae-307f-a220-6078e0b10564 | -1.43725 | -47.9645 | 2024-11-28 03:57:00 | NPP-375D | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 67bce00f-fc15-3f09-89df-424578f5c0ba | -1.89545 | -45.46328 | 2024-11-28 03:57:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b391df6-d667-362b-812c-926572b49ee6 | -1.89226 | -45.4603 | 2024-11-28 03:57:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6415a5d4-fc46-3803-8f64-9ce5030410a7 | -1.093 | -48.21322 | 2024-11-28 03:57:00 | NPP-375D | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32bf61ad-2de8-379b-85fa-d601f43f42ea | -1.4506 | -47.11738 | 2024-11-28 03:57:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5487dd22-7fab-357a-a092-29755e027251 | -0.93477 | -47.55599 | 2024-11-28 03:57:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2db600d-e402-30d5-9d1e-1ba41df3c2eb | -0.58435 | -51.71285 | 2024-11-28 03:57:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 723f0e23-9522-37d4-81ac-d1fec7338ee4 | -1.52903 | -47.297 | 2024-11-28 03:57:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc9c7d31-2e5e-3ca2-b752-60935991ea92 | 0.699 | -51.45169 | 2024-11-28 03:57:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ce708282-494b-37b2-ace4-7509b4b0b0f0 | 0.97639 | -50.13041 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71c1e5db-508e-3e9d-9735-4d158786ebd8 | -1.51889 | -46.12234 | 2024-11-28 03:57:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1c0aa34-2604-3339-9338-4620a5caf18d | -1.64731 | -45.23503 | 2024-11-28 03:57:00 | NPP-375D | BACURI | MARANHÃO | Brasil | 2101301 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f1112a0-6ac8-3e15-a542-d1b87f98d469 | 0.97548 | -50.12544 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c25196c-bb9e-36cd-8d17-f6af3bbe6bd9 | -0.58479 | -51.70617 | 2024-11-28 03:57:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8bd969c3-5c94-3bd9-bde9-d0fecac26cf9 | -0.58375 | -51.71251 | 2024-11-28 03:57:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d33bc2e-f83b-3e73-8404-6f073bbb90b4 | 0.6976 | -51.44813 | 2024-11-28 03:57:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 90b35f33-1376-381e-9a34-fb2939707146 | -1.44502 | -47.11953 | 2024-11-28 03:57:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a86f9dd-20bd-3573-93dd-243fb5cf0fa7 | -1.89094 | -45.46255 | 2024-11-28 03:57:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13bd01ee-c56a-393b-8ffd-ab6a3c3e76e0 | -1.89152 | -45.4648 | 2024-11-28 03:57:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab811a7b-8782-3a60-a57b-6616f305c8db | 2.08551 | -50.63222 | 2024-11-28 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50478db7-ba8b-3a46-8389-453c79950d8e | 0.9763 | -50.1307 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af1417a5-2e6c-3b11-ba33-f3db43d53459 | -1.53334 | -46.0625 | 2024-11-28 03:57:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81732683-95e1-3036-a9ee-54b39468bc78 | -0.5917 | -51.70734 | 2024-11-28 03:57:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa544e41-9dd6-33ee-9c16-c68b04f6ecbb | -0.93425 | -47.55919 | 2024-11-28 03:57:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0af05f02-c5f1-3f55-a9e6-7082abf06811 | 2.09224 | -50.63112 | 2024-11-28 03:57:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f4fdb5d-2209-3588-b023-ae71fd733af7 | 0.98191 | -50.12446 | 2024-11-28 03:57:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06fb1d10-aa0f-369a-b3ae-eb63acbf90b2 | -1.4378 | -47.9611 | 2024-11-28 03:57:00 | NPP-375D | INHANGAPI | PARÁ | Brasil | 1503408 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a33d78c1-d4cd-3fc7-b371-4d0f0da05ef1 | -1.40311 | -46.62349 | 2024-11-28 03:57:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25709936-73e2-3c2e-9008-3eef621fce86 | -4.8044 | -43.29818 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d56dd8d0-db5a-3d50-99f3-0e6e76960150 | -1.642 | -52.47066 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61ce5aab-b100-3639-8ba3-b2f07a53d13f | -1.35937 | -51.96688 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cd97526a-a93b-3fc5-98ec-d3aa9307da73 | -2.86638 | -46.84564 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 54e6f18d-5f69-39b5-8150-f997b8d8b000 | -2.74297 | -48.66099 | 2024-11-28 03:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d72fb750-740a-347a-b40e-617ddc8293fa | -3.84588 | -50.09032 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50b594e6-d403-3530-993c-3db85842664c | -3.46205 | -43.52954 | 2024-11-28 03:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4933e522-ab25-3ce0-bc64-42a1bf0778c3 | -3.25097 | -50.76929 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a673c4e8-5972-310c-b36c-d280d92e54d6 | -5.19081 | -44.24839 | 2024-11-28 03:59:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43d72ac6-269e-3dae-97b2-e9d26e2e8aa1 | -3.38478 | -50.10877 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 27932618-b3bf-36b6-98d3-8f90b4384982 | -3.2484 | -50.61247 | 2024-11-28 03:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e97dc81-d3e7-3828-8294-c8eb003de8de | -4.72679 | -43.25075 | 2024-11-28 03:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3259f110-a9e8-3d93-b0d8-98f66c8824f5 | -2.87037 | -46.85188 | 2024-11-28 03:59:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 80364443-cc95-35d7-9b77-2beff55b5ebf | -6.08738 | -41.93842 | 2024-11-28 03:59:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 530f445c-e41c-3593-9cd3-65164fb66964 | -3.44577 | -50.00505 | 2024-11-28 03:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f820b22-e685-32e8-925c-b917c6f8a576 | -1.68805 | -52.4784 | 2024-11-28 03:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b623b612-9b99-3c46-b603-6ffaa551dbf2 | -5.97726 | -45.35551 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1a7ff8b2-949a-3bb1-b171-ee9e614c4819 | -5.75979 | -47.90719 | 2024-11-28 03:59:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1020e991-27d3-38fd-9b07-72ed967db5c4 | -4.10661 | -48.24826 | 2024-11-28 03:59:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5d5b91eb-6e20-3910-8617-81944b7b20f7 | -3.0875 | -49.21254 | 2024-11-28 03:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6054f3ab-e0c2-333c-8019-08eb2c12436d | -1.3338 | -51.94933 | 2024-11-28 03:59:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 02f4c273-5e15-3132-bcd3-fd08de41eff0 | -4.65601 | -44.04213 | 2024-11-28 03:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 704da505-6a64-3add-b60a-84f401da30cf | -3.74225 | -51.83733 | 2024-11-28 03:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff4cd531-26a6-32a4-aae5-b1a92ab30a93 | -5.9779 | -45.3517 | 2024-11-28 03:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README30.md)
