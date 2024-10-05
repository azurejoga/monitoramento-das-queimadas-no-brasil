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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0eb51bb-6b79-3788-aa5d-8e927536966f | -18.6785 | -57.2734 | 2024-10-05 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 578f22ab-fd14-3389-834c-17752243a98d | -18.6981 | -57.2915 | 2024-10-05 03:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.4 |
| d0f4535d-821d-3140-8021-fc332e02cae9 | -3.39947 | -45.28373 | 2024-10-05 03:47:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6699a13a-2e0e-3e30-9235-1fbe0c1257ad | -3.39891 | -45.28708 | 2024-10-05 03:47:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddd0875b-ba77-3644-81b4-1b46658235e7 | -3.39411 | -45.28289 | 2024-10-05 03:47:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 745831be-a84d-394e-a4bb-2effac4135d7 | -5.061 | -45.37988 | 2024-10-05 03:47:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdadfef4-8584-30d1-9686-c21b6ab838f4 | -5.06047 | -45.38292 | 2024-10-05 03:47:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a2964a9-b8b2-3564-9d50-0fb2f7a406c7 | -4.78967 | -45.26154 | 2024-10-05 03:47:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdafc290-729a-384a-a887-713d2f07f853 | -4.41873 | -45.37774 | 2024-10-05 03:47:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0a8c2de-7181-3a79-ad47-46b7fda2843e | -4.41817 | -45.381 | 2024-10-05 03:47:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3b4966b-2690-3e77-94a6-d7058ea204ee | -4.41346 | -45.37675 | 2024-10-05 03:47:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57e45988-1f1e-31f4-b463-b0badbf3a6a7 | -4.92335 | -45.67758 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f3070d2-2623-37cf-891b-8654e3abe642 | -4.9228 | -45.68076 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6df2c41-a2b7-3614-a0e9-072e2c2490ae | -4.86555 | -45.85085 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af24a8b6-e248-350f-b131-6a4d28566bbe | -4.86079 | -45.84619 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ecf4b564-cd64-3a81-99a2-010339464757 | -4.85957 | -45.85314 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da1bc0fd-acae-3415-8fed-2d54b01464d0 | -4.69083 | -45.8725 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 36f6daff-fdde-33df-9dbd-70c0f453fe4e | -4.69025 | -45.87589 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6c9a271f-f532-3243-8c4c-52c4cf64de6d | -4.68421 | -45.87842 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 803cfe17-99df-3f84-a7de-ec1841a391d7 | -4.68361 | -45.88194 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 037df4f3-5389-38fd-ab4d-fde8feafc16a | -4.67874 | -45.87763 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0c6289f-4256-328a-a85d-4d7ea57f5cc5 | -4.67378 | -45.87387 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71a603a3-3c10-36db-9fb3-a08bd2458cf8 | -4.6732 | -45.87722 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e4bc042-1a2b-30ad-a10d-f3bb3a8bd8f1 | -4.59559 | -45.60462 | 2024-10-05 03:47:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bfa5ac7d-4ae2-3698-b6dc-b7fe5b5d9bb5 | -4.36376 | -45.63289 | 2024-10-05 03:47:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d6971468-6a33-39d5-ba97-07cba8d8a7be | -4.36318 | -45.63624 | 2024-10-05 03:47:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c47c6785-a4d1-35c9-9f7a-596866fcd74d | -5.3887 | -46.42717 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5d76bb3-a3cb-3c44-8034-d1eeac4573c4 | -5.38435 | -46.42666 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5b72f47c-c318-3348-abb1-3b6ff384d8b9 | -5.38317 | -46.42593 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0c7ce5b-69d8-33a4-a050-77a3e9c9ec43 | -5.13001 | -46.12452 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e8ea1c4-7394-3237-8362-3bb7b66fcec4 | -5.12976 | -46.12454 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cd3af75-12a9-37eb-812f-2453ec3f8bd3 | -5.09121 | -46.11831 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60bafc3d-1253-3e43-8967-c17a45f073ab | -5.09055 | -46.12216 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dfd4a26-fa03-3c22-9980-9ca52951dd08 | -5.08567 | -46.11763 | 2024-10-05 03:47:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd76c4fc-424d-3ee9-ad72-41ca356a5046 | -5.15618 | -45.23991 | 2024-10-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24fbad9e-dc02-336a-85ca-c8260a1440f4 | -5.15561 | -45.24314 | 2024-10-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07325add-df40-3b09-bcf8-8e373ea950d3 | -5.15429 | -45.24193 | 2024-10-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 679330a6-37a3-3c27-af11-aab724609aaf | -5.15374 | -45.2452 | 2024-10-05 03:47:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79c92751-b981-3811-b7a9-fd3bffd6dd79 | -3.31779 | -46.98662 | 2024-10-05 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f39650c0-f083-36fd-a1dd-84bb8bfc3cbb | -3.31703 | -46.99111 | 2024-10-05 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c86eadbb-ecf6-33c0-985b-fcf68dc98d37 | -2.62523 | -46.90985 | 2024-10-05 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4255da6c-2f0a-3dd9-a412-3fea1d3572be | -2.62446 | -46.91436 | 2024-10-05 03:47:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8025edd3-7157-381c-98f7-d3b2225cb670 | -5.04932 | -47.16005 | 2024-10-05 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a567d66-fee0-31ab-8f54-839a05085c59 | -5.0478 | -47.16019 | 2024-10-05 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45de3e30-405e-30fc-9059-d124a66c5ed3 | -5.04342 | -47.15909 | 2024-10-05 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b7cfd35-60ca-3810-b0c2-0ed5984d282c | -5.0419 | -47.15925 | 2024-10-05 03:47:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81fe4872-bc0b-3bfb-829f-fcf8cd8bc33d | -4.84972 | -46.52268 | 2024-10-05 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ffeb5207-dd3a-36e7-94ce-2349cf7ebc9c | -4.84683 | -46.52462 | 2024-10-05 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ed0a3b0d-0ce3-3ccf-863c-31e682eb3cfb | -4.84404 | -46.52179 | 2024-10-05 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a04bbc74-4f16-38f2-ba36-d93e49aba199 | -4.76874 | -46.67268 | 2024-10-05 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 042287d1-dd7a-3f86-8310-e5a9bbe651e6 | -4.76806 | -46.67657 | 2024-10-05 03:47:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 137f58b4-b074-31c8-aa2a-4ad389cd9c88 | -4.32559 | -46.71267 | 2024-10-05 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c1ba96c-5d07-30f5-a2bc-012880531167 | -4.32491 | -46.7166 | 2024-10-05 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f83a1c84-3f9e-36fd-bfed-ad4a87258ccc | -4.31165 | -47.7086 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bc605625-8714-35a4-8e90-7ff8d96c7083 | -4.3111 | -47.70832 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35ee258a-fbda-3ba9-910c-43959c1ae63c | -4.16688 | -46.83495 | 2024-10-05 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63006974-9e19-343d-88c1-38ae43087c0b | -4.1618 | -46.82958 | 2024-10-05 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a00c297c-dbc7-35cf-8849-01b7b6bb4729 | -4.15668 | -46.82446 | 2024-10-05 03:47:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 172e8777-d4c0-3d65-99c9-d53490505beb | -3.61826 | -47.5199 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| fe67fc14-a657-38a8-8dba-86c87b1176b1 | -3.61741 | -47.52479 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 5ae1d9c2-adae-3c3a-a1cf-5f38927be90c | -3.61656 | -47.52967 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 59a6732d-7835-36db-887a-d79cbe7945e2 | -3.61209 | -47.51889 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3de8f26d-e660-35e9-8d3c-de5b2629ed71 | -3.61126 | -47.52367 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| ffc52796-49b2-3067-85de-4bde1b7f3d86 | -3.61043 | -47.52848 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 65d5bc3f-8a4a-3ed7-9233-1e650b1ba58c | -3.60608 | -47.52045 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76be55df-7fc9-3f98-97e2-0354a4821289 | -3.60528 | -47.52521 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 940e6bcf-49c6-3db4-8606-cb653413d07d | -3.6051 | -47.52266 | 2024-10-05 03:47:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 84d33190-b412-350d-8217-e1f846a64be9 | -5.39679 | -46.57682 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52aa26ba-6aa9-3c42-ba6a-a336cb38222f | -5.388 | -46.43106 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cc6ebbc-fccf-3e68-bddb-b4171c374d26 | -5.38369 | -46.43053 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea270470-6a24-3ff1-8f0d-4fb2d98601a0 | -5.38248 | -46.42979 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc5deeb4-fa23-333b-863d-b758c3439930 | -5.37814 | -46.42933 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0fc8e00-9e67-3b95-aa4d-525b01a238ad | -5.37692 | -46.4287 | 2024-10-05 03:47:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 87e71e77-019d-39e2-8c84-f30362effd20 | -2.01885 | -47.9907 | 2024-10-05 03:47:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78fb43c2-072b-3c71-b49b-84aadf6ea6f3 | -2.01846 | -47.99271 | 2024-10-05 03:47:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f833b2d-0b21-3684-9261-d6670dfa0704 | -2.01796 | -47.99614 | 2024-10-05 03:47:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56e79eeb-159a-32ea-9ef9-6577e81ca16f | -2.01235 | -47.98965 | 2024-10-05 03:47:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3666ac70-4305-3c7a-aa0f-ae3d71422d11 | -2.01196 | -47.99173 | 2024-10-05 03:47:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 847f1cd7-902c-3c4b-b517-f3ee2ab661e1 | -3.45008 | -48.82293 | 2024-10-05 03:47:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 95b93edc-4df3-3c2e-ba3f-4dffa5d3bfca | -3.27484 | -48.79977 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bdaa6ba7-7592-3d59-9827-a1b2e4bc58c5 | -2.91172 | -48.91233 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78fe7ce5-0c03-3ad5-a25c-708a14f2ce6a | -2.90682 | -48.9129 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1c04e81d-146a-33f8-849c-4048b860575f | -2.90492 | -48.91135 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b27fbff1-7110-33b8-9a48-adff3cd4857d | -2.90389 | -48.91746 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 32df739f-9d69-36d0-a452-9aec63c971a3 | -2.87784 | -48.90683 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d2d92005-4dc9-3135-8dfe-923e6df28656 | -2.87678 | -48.91298 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 39ede91a-0362-3f4a-89ce-311c251a2854 | -2.77909 | -48.57948 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50b7e1da-cc52-3072-ac47-875f9d0e237e | -2.77807 | -48.58541 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 59d85c34-ab23-3911-8165-f51e9daccd05 | -2.7361 | -48.89734 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cad4b7cb-0bed-384c-96c4-5aa8bd819d08 | -2.72118 | -48.83341 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e7ff991-dbf7-3d0a-a3e8-1e1c037c5302 | -2.72011 | -48.83951 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97fdfb7f-d433-3477-b8db-55ab0fb8e5ba | -2.71815 | -48.838 | 2024-10-05 03:47:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aff7866a-2c34-309b-b5b3-76d5eac68d96 | -4.48061 | -48.10683 | 2024-10-05 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b60f7ecc-44be-356d-9a40-8ac0a87d76a9 | -4.47974 | -48.11177 | 2024-10-05 03:47:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23f1bc6a-d61d-3f36-af54-d857a104dd44 | -4.28582 | -48.06948 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d23db7a0-6996-3299-9dea-1a727b99bcca | -4.28042 | -48.06325 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a155d9c-a3a0-3f51-bf4a-b1b340786016 | -4.27953 | -48.0683 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38b320de-65fb-37f4-a03d-0fb21443be94 | -4.08463 | -47.95752 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a265f0da-14ed-315f-834b-d1056487621d | -4.08011 | -47.94643 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| a3e35cc7-752f-3319-bd58-fb777a30d8ae | -4.07921 | -47.95155 | 2024-10-05 03:47:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |


[Clique aqui para ver as próximas entradas](README40.md)
