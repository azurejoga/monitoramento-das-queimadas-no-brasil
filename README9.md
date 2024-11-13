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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07956679-82b8-3976-b7fd-939ec542b8f1 | -5.3587 | -43.529 | 2024-11-13 01:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| bd90e46f-df30-3935-b0f9-573b3f197910 | -3.1096 | -54.3066 | 2024-11-13 01:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 54e253bf-e1f2-3d99-a5f5-ec37d330c1f2 | -3.0504 | -50.3332 | 2024-11-13 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| dfa9500d-f7ca-3f93-af42-23cf384323c4 | -2.2479 | -53.7627 | 2024-11-13 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f76285b1-0ff6-3af7-bb88-fd64bca4cb11 | -2.2112 | -53.7432 | 2024-11-13 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| f2d5f07a-fc27-3876-8ffb-c328ce88cb80 | -10.7425 | -49.5244 | 2024-11-13 01:30:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 90c5d184-559b-3164-bf34-c85f9bc1d32e | -2.2663 | -53.7422 | 2024-11-13 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 8b56f2c8-9b8b-3a25-93e2-5b4882ab2220 | -3.7666 | -47.4855 | 2024-11-13 01:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| ffa1408d-6a18-354b-b2e2-b72f4b443eea | -2.7033 | -49.3513 | 2024-11-13 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 29fe217a-8db0-3b70-a5eb-e97cee8b595c | -3.1501 | -53.2371 | 2024-11-13 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 84116731-43f5-337e-b003-69cd52685906 | -2.1395 | -46.4206 | 2024-11-13 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9c44a205-8957-35d4-a398-628063992464 | -4.6776 | -44.5861 | 2024-11-13 01:30:00 | GOES-16 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8a42f401-c793-3de0-bf9b-6e18eed02abf | -2.5319 | -45.6086 | 2024-11-13 01:30:00 | GOES-16 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 6a87900c-6700-31a5-ad12-ed42fa005807 | -4.6778 | -44.5633 | 2024-11-13 01:30:00 | GOES-16 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| ea7dc41a-a5df-3628-83aa-7d0b39afc98e | -2.1396 | -46.3984 | 2024-11-13 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| dbe75714-a704-3e79-92b1-4c600441917c | -1.6444 | -52.536 | 2024-11-13 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 2828130d-a954-368d-aa99-d426ef5f6f01 | -2.7033 | -49.33 | 2024-11-13 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 27b16023-a36d-3517-b423-20da4fccf7a8 | -3.9483 | -48.1724 | 2024-11-13 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| eabf783f-4ad5-3c3c-904c-6e0eaddeb886 | -2.158 | -46.4201 | 2024-11-13 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 289bd065-4c41-3b30-8a08-5f58b8c52df5 | -4.6581 | -47.4216 | 2024-11-13 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 1e34392f-2122-3394-a349-eefb34ae8abf | -1.6627 | -52.5357 | 2024-11-13 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 21530c29-7532-31fa-ae4b-a2de7ff8e0b7 | -2.2479 | -53.7627 | 2024-11-13 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| bdeba926-8cfa-3b8a-a637-98b71f0b4294 | -3.0504 | -50.3332 | 2024-11-13 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 005a7c07-e2e4-3fd0-8df2-493fd5356415 | 1.0663 | -60.5985 | 2024-11-13 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 86837312-f8ec-3a50-86bb-2d8b7719d725 | -2.2296 | -53.7429 | 2024-11-13 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 9ced00ee-c750-3b89-b524-c5c0357c98e6 | -1.6627 | -52.5561 | 2024-11-13 01:30:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| fabb0852-9e95-3d49-a4f3-9958fd5710d7 | -17.3873 | -40.4343 | 2024-11-13 01:30:00 | GOES-16 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 148.0 |
| 831c9b69-0329-3712-9173-37123394d3ff | -4.6767 | -47.4206 | 2024-11-13 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 274d9f50-6b31-3e6e-8d1d-5c4933bef911 | 1.048 | -60.5986 | 2024-11-13 01:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 185a1330-88d6-3f7b-a52b-7eb18b00cc8d | -2.6848 | -49.3518 | 2024-11-13 01:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5c4a3a22-cc8f-391e-994f-453227b313bb | -5.9398 | -39.6854 | 2024-11-13 01:30:00 | GOES-16 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 7a9ed395-95a5-3a56-9e40-4e92acb8e024 | -4.658 | -47.4434 | 2024-11-13 01:30:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 91346116-5b7b-34a2-ab5e-56ae14011dcc | -2.248 | -53.7426 | 2024-11-13 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| b2a5d4a9-09b2-32bb-90ad-3c4e2e7da47d | -2.1581 | -46.398 | 2024-11-13 01:30:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 112.4 |
| d941fbfa-345c-39ad-979b-93f74f70362d | -29.52694 | -49.89632 | 2024-11-13 01:34:00 | TERRA_M-M | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 21.8 |
| a650715c-78ba-3754-9797-9942c8299216 | -29.52434 | -49.88158 | 2024-11-13 01:34:00 | TERRA_M-M | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 13.0 |
| aa02c6b7-b0c0-3b4b-b17e-5d241443363c | -21.20255 | -47.11952 | 2024-11-13 01:34:00 | TERRA_M-M | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 238eff2f-ac12-3576-8167-2981285dbe9c | -17.71726 | -57.49939 | 2024-11-13 01:36:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 96cf57ca-0f1a-32d1-bbeb-5aa6efddfbca | -10.95006 | -55.4539 | 2024-11-13 01:38:00 | TERRA_M-M | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0d3e462e-bba4-3cb7-af6f-34735e82f9c3 | 1.0663 | -60.5985 | 2024-11-13 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 110.7 |
| ff70b2df-d857-37b7-b478-e46571d8c428 | -10.7235 | -49.5265 | 2024-11-13 01:40:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 117fa2ae-cdb9-39a0-bd25-69e2c0bea3b2 | -3.7666 | -47.4855 | 2024-11-13 01:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| b50dfa4f-618b-3013-8fdf-fae9c87ed0f7 | -5.3587 | -43.529 | 2024-11-13 01:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 41a43401-8dda-354e-bfa8-2623e5cff75f | -2.9924 | -51.045 | 2024-11-13 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| e1ca7cbd-f5a0-3dff-9f24-7b384edf9fe6 | -2.1395 | -46.4206 | 2024-11-13 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 5d83c7f1-f948-3c75-a3a6-e2c4de5fc16c | -2.2479 | -53.7627 | 2024-11-13 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 41aac306-45cf-34be-8b35-64fdd6be3851 | -2.158 | -46.4201 | 2024-11-13 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| a2bcc3e6-d1e8-376d-9fee-2d0f0bd2d735 | -2.2296 | -53.7429 | 2024-11-13 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| bcdba8c0-f726-31c7-811f-932f8b499864 | -10.7425 | -49.5244 | 2024-11-13 01:40:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| a78d680b-4754-3de6-bff8-1b71ff181aeb | -3.3519 | -48.9475 | 2024-11-13 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 9cde7816-2b27-31c6-bfc0-cfed9a47b8d2 | -3.1096 | -54.3066 | 2024-11-13 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 9b234de2-031f-35f8-8e3f-1475cb9944de | -2.248 | -53.7426 | 2024-11-13 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| da1fe691-6712-33f0-a6ee-48e7f4a68c3d | -2.7033 | -49.3513 | 2024-11-13 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| f3983ed2-c742-3d8a-9a1c-697a3dd7b34d | 1.048 | -60.5986 | 2024-11-13 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 7d55c885-7089-372f-b6dd-5418b199269a | -3.3518 | -48.9689 | 2024-11-13 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 41931ee3-8c74-3cc6-96f1-234af3d0e1ef | -2.1396 | -46.3984 | 2024-11-13 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 78667a91-58be-3230-81e8-e3841bb873c7 | -2.2112 | -53.7432 | 2024-11-13 01:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 5ddb935f-2418-3d54-bf89-1c704bdd3a2e | -2.9925 | -51.0242 | 2024-11-13 01:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 6f04dd34-5fb8-39e4-a121-0c1e6cdbbb67 | -1.6444 | -52.536 | 2024-11-13 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 4f046924-8c5b-34f1-a205-07ea2986a61a | -2.1581 | -46.398 | 2024-11-13 01:40:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 04f2e32b-b360-3950-8496-791eae6bd52f | -4.6581 | -47.4216 | 2024-11-13 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 2e98dc7e-6ca4-3b5f-b4d6-65d6249c5949 | -4.658 | -47.4434 | 2024-11-13 01:40:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 45ec42e5-2a8a-310f-aba3-f540a81b8fc6 | -1.6627 | -52.5357 | 2024-11-13 01:40:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 164de162-a8d7-3036-b673-f1d9fb85e117 | 1.0663 | -60.6174 | 2024-11-13 01:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e689bcd8-da47-3660-a304-0eb3c89b5540 | -2.7033 | -49.33 | 2024-11-13 01:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 26c2c7e0-41c0-319c-ad5d-c221d5351c18 | -2.98582 | -51.34602 | 2024-11-13 01:41:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 54afb593-5d45-301b-b487-e66cd84c28a4 | -3.8546 | -51.91735 | 2024-11-13 01:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 163965a6-f1fb-328e-9053-d67fe907dddd | -3.15161 | -53.22895 | 2024-11-13 01:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 699d5735-0b3f-3134-8450-a5f7dc5b3f6f | -3.102 | -54.31522 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 195062bc-1094-3043-a442-744d43f5b5e0 | -3.66946 | -50.16545 | 2024-11-13 01:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 6e0eab5a-7d3c-3e68-b499-5ce7187a00d8 | -3.5367 | -54.50084 | 2024-11-13 01:41:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7da8c5bc-7fa6-3507-94ff-3a90a7443a85 | -2.98747 | -53.97439 | 2024-11-13 01:41:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 5f82fa53-a570-304c-a1b2-de9db15f7f1c | -4.10892 | -51.10039 | 2024-11-13 01:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 51037e53-a5c9-3cd9-a423-d3519d633c6c | -3.15534 | -54.49047 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 3bf136f4-f254-31ea-b708-05cab085715c | -3.00364 | -51.03436 | 2024-11-13 01:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 9873ba30-8a5d-3cf4-bff8-53811914de80 | -2.62563 | -54.2806 | 2024-11-13 01:41:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4ae84e24-0f75-3cb3-bd94-5f01f54ef759 | -2.76814 | -54.72445 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5e8ac7cb-5763-3df6-b74d-757823e00ba4 | -4.3962 | -59.92018 | 2024-11-13 01:41:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 336b391b-9f27-3cd0-a3f6-265eff2e88bd | -3.17348 | -50.47029 | 2024-11-13 01:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 08f80b09-f5b4-3ae0-9c6a-4fc080cd4dfc | -2.99693 | -51.04047 | 2024-11-13 01:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 53956297-4523-3a3c-b06c-6695e0d769a8 | -3.53406 | -54.48292 | 2024-11-13 01:41:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 1ee4aee7-f3c1-3ed1-8c66-d196788bc3ee | -4.33182 | -50.444 | 2024-11-13 01:41:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 0f6b233a-2ae2-3d7e-b31c-1cfbf2d68fd0 | -3.57782 | -53.01575 | 2024-11-13 01:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 51332563-4180-331d-8e73-61fb6ed0c111 | -3.09937 | -54.29672 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5139f6dd-495e-323a-803d-836b7dca754d | -3.10298 | -54.30957 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2424f5ca-dfe6-34df-9167-27e7d96716be | -4.33662 | -50.43816 | 2024-11-13 01:41:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| f71a3109-afb6-3799-9add-3b27444f993e | -2.98733 | -51.03686 | 2024-11-13 01:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| d5649829-f9fa-35cd-af7a-bbb7052c84f5 | -3.15509 | -53.25222 | 2024-11-13 01:41:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| b4b46c29-764d-3521-ba32-af8f793bb1be | -2.77074 | -54.7426 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 6d68f263-91c7-301a-b4f8-cf7ba634b6de | -2.62567 | -54.27407 | 2024-11-13 01:41:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4edff9a5-f486-34cc-ae79-cab80fefa7c2 | -3.52175 | -54.48464 | 2024-11-13 01:41:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 603dd013-872b-364d-ab63-cc5f316f684e | -3.76733 | -54.65296 | 2024-11-13 01:41:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 0e2ba305-ad21-3e2c-af64-fb47d7342e9a | -3.81805 | -51.26909 | 2024-11-13 01:41:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 43ad85fc-fad0-3f31-95b9-c58f7fd6c82c | -3.15732 | -50.58815 | 2024-11-13 01:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| a0e66bf2-628f-3648-968f-de294eddb85f | -6.7898 | -58.78716 | 2024-11-13 01:41:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 58000451-3f62-36f8-9f72-106327e4a3a4 | -2.74823 | -54.67297 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| c7bdbfd6-0e4b-3df4-847a-79689d61f131 | -2.77424 | -54.73631 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| e14b5755-7602-37b6-b27d-f4107424a742 | -3.25488 | -54.54282 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 44e4b99f-fa2c-3479-a09d-2a4cb533a579 | -3.66382 | -54.65608 | 2024-11-13 01:41:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| debb69eb-b2d5-3653-9a25-78747b76d8ae | -3.14296 | -54.4922 | 2024-11-13 01:41:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |


[Clique aqui para ver as próximas entradas](README10.md)
