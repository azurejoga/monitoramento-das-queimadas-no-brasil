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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5fc730a0-2b2a-3a0b-b60f-bded82589692 | -10.33362 | -57.4915 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83455233-11d1-3945-b47b-e028c8a67386 | -7.019 | -44.60709 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0dd8047a-d2a0-31e0-87d0-3030dde77402 | -9.57324 | -48.57005 | 2025-06-05 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cc43a3b-0e81-372a-af2c-ed1000bee9b8 | -7.70065 | -45.77624 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d5cadea-12bd-3c3d-b273-dde2f0e2dfcf | -7.19325 | -43.13719 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f625e029-99fb-3d1c-8fbf-fed9e92bea71 | -11.99543 | -52.47044 | 2025-06-05 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f29047a2-12ea-37de-bb04-e4d957173c86 | -10.70922 | -48.78139 | 2025-06-05 04:59:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7321cd32-bcdf-37c7-98be-32c3e92b5865 | -9.4985 | -57.14812 | 2025-06-05 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e83638d-1379-38b7-a69c-f3413d04971f | -11.42976 | -45.10312 | 2025-06-05 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 14554eb0-da55-3f64-b999-91744215e44f | -10.67121 | -44.38514 | 2025-06-05 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02db426b-d535-3999-947c-3b47256248df | -10.67177 | -44.38054 | 2025-06-05 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5dcaf25-ddf1-3293-8dbd-f65948124286 | -11.71643 | -49.09245 | 2025-06-05 04:59:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3722616-210b-363f-b67e-ea8a2730f355 | -10.68158 | -57.59525 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5ebc495-1038-3bd9-8a4e-779e9b3c2044 | -7.01181 | -44.61761 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9a72b531-481a-34f4-b199-137f2cc898d9 | -7.69453 | -45.78178 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4e942b8-6941-3b2d-91d0-6c524b76594e | -10.81209 | -56.95717 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1eed6a72-1608-3d5d-9a58-b346e1e168cb | -7.01147 | -44.60697 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5d14269d-d80e-359a-8c81-dd92a0311d8d | -10.49636 | -53.65432 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 799f4c8f-a118-3ec0-8cb5-a670253cb83d | -10.68572 | -57.59194 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 968568db-13ad-3bbd-a3df-ca7afcae75d1 | -10.6658 | -44.37965 | 2025-06-05 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 224c34f2-1e8c-32e9-b279-f8892e9e83ad | -10.12464 | -48.68847 | 2025-06-05 04:59:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b10a440c-8edf-3baf-9ccb-1d25fb9d3028 | -9.35404 | -47.69639 | 2025-06-05 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e67a5bc0-49ad-36b4-8ddc-e3c23ddeb45c | -9.49913 | -57.14427 | 2025-06-05 04:59:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9db4e1a-0003-3586-b072-fdfd717136e6 | -12.28996 | -43.54688 | 2025-06-05 04:59:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 324f6dbe-1326-3da5-8a50-01a14494fb4b | -6.90833 | -47.76248 | 2025-06-05 04:59:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dab2b766-9fc4-38fd-9167-eca5c28fb435 | -9.26653 | -56.29958 | 2025-06-05 04:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c01ac4-ee7c-31c0-aa6f-29c8f15f7784 | -10.85238 | -46.86248 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 856ed331-1dce-3f08-af8d-bd7bc64f82f6 | -10.65328 | -49.42569 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 249101dc-226b-3f58-94b8-3267d4dbb90c | -11.13806 | -53.94802 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11d90aff-52b5-33ae-a2c9-7531a32ef842 | -11.14144 | -53.94855 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1515f0d-a6bb-38ba-9676-1b8e49f1a4c2 | -9.45712 | -55.94266 | 2025-06-05 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5946f92-b7a2-3f62-a8a2-cdac54bbbbe1 | -11.13523 | -53.94383 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f4774c69-d8b7-36ba-8fd5-3c860f183261 | -8.94242 | -47.30173 | 2025-06-05 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22b41ecf-be78-3233-913d-7ff773157cc3 | -9.82199 | -48.04471 | 2025-06-05 04:59:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12f66a56-9ead-3db3-923f-ee2cba5387b8 | -10.49863 | -53.66222 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e1b38af8-3e71-3bd5-8944-2a69274a58de | -10.93806 | -55.3311 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c8cd60f-dd50-3d26-9f33-1af5866f9677 | -9.35176 | -47.69244 | 2025-06-05 04:59:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69420440-cc34-33cd-a365-1e97cc1ee673 | -8.74333 | -48.03287 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 137de49e-1080-3bca-bc0c-8eecd26e70cc | -10.70477 | -48.78073 | 2025-06-05 04:59:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 704665da-849e-3fd5-8ca8-42dbb303698b | -11.44031 | -45.11263 | 2025-06-05 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a106e0c-1540-37d5-a36b-21b23dad614f | -11.13862 | -53.94437 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28d72570-b722-3c3c-91fb-817de302f507 | -11.13132 | -54.22129 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67c57d29-7d9b-3c3a-97df-e10bc3726b3f | -10.65272 | -49.42973 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3098fc3c-a57a-3184-b754-cc4ef2829c45 | -10.69537 | -57.64177 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d2e57b6-121b-33cd-b593-dd17271af30d | -11.55991 | -47.62024 | 2025-06-05 04:59:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8ca0c06d-d214-3117-9eb6-24c9d30c36d5 | -11.84017 | -51.29455 | 2025-06-05 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7234209b-6ad9-3978-a765-ac3ff50908b9 | -10.30324 | -57.14407 | 2025-06-05 04:59:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13f8bea8-28a2-39b6-ba2b-270f9d693c9e | -7.62404 | -45.75172 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f47baca-a697-36a7-8a2b-21e40bf32aeb | -7.61883 | -45.75082 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8fecccbf-3164-3506-a330-b9ca330dcc8b | -7.01247 | -44.59948 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 524d9dd1-e974-37e4-bb38-1a33927f7d0f | -10.54094 | -56.38706 | 2025-06-05 04:59:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2e833e11-48f4-3cb2-a61e-b5ae09aff60d | -11.83633 | -51.29396 | 2025-06-05 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f140c7e8-5a1d-30ac-9b6b-a00463dbcb42 | -10.67231 | -44.37608 | 2025-06-05 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6825f097-28a6-34fa-bf94-29a8b2ec300a | -9.22145 | -48.85844 | 2025-06-05 04:59:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92f2e90e-85ea-32fe-939e-fd4904f3c959 | -7.01 | -44.61798 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aa4e5ac6-bbc9-306d-8d50-eb2c70c6a10c | -12.0769 | -48.45626 | 2025-06-05 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad31da80-9c14-35fc-aab4-d88f670beb4a | -7.01233 | -44.61393 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3554dc54-92ff-34ec-b515-b2204def6d1e | -12.15434 | -46.59551 | 2025-06-05 04:59:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0be519a0-5839-3c5a-ad42-ba0b3e58a5f5 | -10.65642 | -49.43436 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0bb42ac3-63a0-33c3-b4ca-31f57f7d32ea | -10.68027 | -57.60303 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f846cf06-9080-38c2-9a01-bfb72ea3d8a2 | -8.74787 | -48.03356 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad1dc0d8-8e8a-3aa6-93c7-aa3a0aa5f41f | -10.8183 | -56.96202 | 2025-06-05 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3fb6fc1d-7948-3282-bb43-7e80e828d0b1 | -10.68846 | -48.97011 | 2025-06-05 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0461393-cbd4-3467-a92e-e99d7958db48 | -11.142 | -53.94491 | 2025-06-05 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d56acbac-2ebe-32b5-a28c-ee4980b9ef18 | -10.5026 | -53.65906 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4eaa60c-6af0-3f90-ba24-ff0a15ef50c0 | -7.90028 | -50.36063 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c0a538d-166e-3880-a672-575a0970399c | -11.56967 | -54.56218 | 2025-06-05 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2b75f8f-88da-3584-a75e-8a7ec21632c2 | -7.7002 | -45.7794 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8783a18-2355-3c9f-8ac4-23c48f786369 | -8.71795 | -48.01529 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04b63f97-5654-3217-aa2c-1724f0c23fe2 | -10.94139 | -55.33164 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 193aced1-d66e-3744-b6b0-e3592563e968 | -10.85128 | -46.83185 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebca8eb2-95b3-346d-8cca-1e152ffcc2a3 | -11.83319 | -51.28858 | 2025-06-05 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bf25602-3e52-30d5-815a-74cd19b63abc | -9.38616 | -48.40385 | 2025-06-05 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eda54549-a2fb-3213-8b4b-6dbf2df196bd | -11.3796 | -55.11017 | 2025-06-05 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba763647-91c5-3b1b-a8e1-db282cde82a1 | -11.82936 | -51.28796 | 2025-06-05 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f5e36151-34b7-318c-9071-0d58035703a2 | -8.04639 | -46.89794 | 2025-06-05 04:59:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc1c5026-e99d-36be-a9ca-137d3ecd9d03 | -7.90167 | -50.3628 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 6d82f28a-6f54-387b-abcd-51582b29b7c0 | -8.96107 | -47.97478 | 2025-06-05 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5947e880-8558-354d-a3a8-96995e367585 | -11.83388 | -51.28379 | 2025-06-05 04:59:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 013f613d-d235-3d56-9dbe-5c8de593f2b3 | -7.01857 | -44.59658 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c8e0aed-b357-3a8b-b28c-f374b6784586 | -10.87581 | -46.86261 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2416f60b-a2e8-351d-b9be-102cb94cc3fd | -8.99666 | -47.58139 | 2025-06-05 04:59:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 92dace02-ba20-3133-8762-f9754f83aa40 | -11.9009 | -47.45534 | 2025-06-05 04:59:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c6971ef-fc1d-3f89-9a32-2f693122bdc3 | -9.24378 | -63.28999 | 2025-06-05 04:59:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3668afe1-51e2-3755-bbf4-3cfbac200cef | -8.455 | -46.48326 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 426d937d-812d-3c9f-a5b1-cf61b7c0fcd3 | -7.54387 | -45.83277 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8c8b121f-4678-379e-b28b-ed46410a4544 | -10.4992 | -53.65853 | 2025-06-05 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c02b11e1-c187-35c8-be03-659e1d69375b | -10.87659 | -46.85645 | 2025-06-05 04:59:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c62abb03-7b37-3e63-8e78-7d6559a3e564 | -7.00733 | -44.60888 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 22a2d1c0-5c74-3524-8c80-2702c890a440 | -7.01049 | -44.61431 | 2025-06-05 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f388ca2d-2340-3e7a-8d9a-52016f620f74 | -7.90552 | -50.3634 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 14a4f6b0-11bf-34f2-b00c-e9c98a01357d | -7.90485 | -50.35644 | 2025-06-05 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 71365a89-ed94-3c3e-b3d2-5e37efa96656 | -7.69497 | -45.78166 | 2025-06-05 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eda9109-b452-3ea7-b3b8-16144382702f | -11.0722 | -55.04256 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14fd8f2d-e2a5-35e7-8602-90e43c4f07f5 | -8.71858 | -48.0107 | 2025-06-05 04:59:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77f91b77-cbea-35ac-b788-0b668bd24a9e | -10.05742 | -49.66081 | 2025-06-05 04:59:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ca1a9be-9f65-3ade-9806-c7d0e1793ca9 | -7.58749 | -45.86165 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2f932a3-2d27-3303-80ca-cddb2f2508d2 | -7.21168 | -43.13428 | 2025-06-05 04:59:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e479033d-5161-3335-8811-65c5a2009f09 | -10.94583 | -55.32514 | 2025-06-05 04:59:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3373a17-b954-3cc1-a1d2-2de0a857300a | -8.45925 | -46.48445 | 2025-06-05 04:59:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README15.md)
