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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d470c6b5-930d-303c-afb5-72a63404aa66 | -3.77667 | -49.9832 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79c971d3-8336-34d9-b605-93ced3d99e8d | -3.52558 | -52.15911 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c5f7f76-5384-3522-bc80-9080ed50b5df | -3.23644 | -53.63297 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04cdc383-decb-381c-bb4c-38811fe24061 | -1.80212 | -46.63274 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee8b7f27-3eff-36ee-a029-d4cb5e3df318 | -3.78506 | -46.69672 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 37094988-a69a-3447-9c23-5c26c0375eb3 | -1.33009 | -55.84932 | 2024-12-01 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7df11be6-fda3-3c89-933d-61b207a6fc3e | -2.70087 | -52.44798 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1e335fd-599a-304c-8334-149514e79a68 | -1.1876 | -51.77422 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6809ce60-2713-36f9-96e2-37750feb6e72 | -1.35743 | -55.15643 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 46df9e5c-0036-3f50-8dc9-73f8805dc798 | -1.64197 | -53.87031 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c9ac0a5-ced5-3aba-abc3-9ecb84501b22 | -3.25041 | -53.63955 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc5f8b32-5c57-369a-8bc0-f498721be04f | -4.11257 | -49.07409 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcfe89da-9af4-39bf-bd41-162d19c27108 | -1.33072 | -55.84523 | 2024-12-01 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c97877e-930c-33bd-aa4d-d94d695d6d38 | -3.70897 | -51.68169 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 015f117e-d3c3-3ed1-a04f-25066449a5a0 | -2.8746 | -45.26387 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 946d4ab8-889b-3043-830b-3ef6cf37112e | -1.72396 | -45.76482 | 2024-12-01 04:44:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a200372-7d30-388d-bd76-1d07ad4788a2 | -3.46441 | -50.27023 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| de1a2532-5727-3187-ac5c-be33c10510dd | -2.76525 | -51.68931 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6bece8b8-0c77-3c0e-9a12-f4109a8475c2 | -1.70672 | -52.4411 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6295bdc-754a-3341-b439-554c6cd026fd | -3.10306 | -54.02667 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d0377b1-102d-35b4-aae6-6818a0eb8ac2 | -2.32825 | -50.67287 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e21d854-66e7-37cc-b5eb-2b373c1f78e0 | -3.34618 | -50.8253 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a85a8b6e-addf-372b-bff1-7c881f44a72c | -4.9019 | -41.32181 | 2024-12-01 04:44:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 20078ce0-8d47-3815-8744-6ac00512f166 | -3.41507 | -50.17786 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9245c8a2-266b-38a9-af6c-ce1f4ec543e4 | -2.98687 | -51.45619 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc9e6a50-eb15-38bf-be70-055cdfa48039 | -3.41535 | -50.32265 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 691ba2af-1a15-34f7-98c9-52cb9acb0df3 | -1.21807 | -51.73708 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b6036f1-39d9-3035-a95a-4bd3f3e2bcfb | -3.05245 | -51.06164 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08d60158-24d3-3943-a437-564a5360f262 | -3.01901 | -51.3699 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1baed0c9-4730-357a-bc31-a4a8e042ef2d | -3.10769 | -53.27213 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a5f83f4-5d7e-3b5a-9743-e86750edf906 | -4.34702 | -48.12992 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9d4edbe-1664-36ad-b09b-f41d2a3e6364 | -3.27444 | -50.78937 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee10abc6-eafb-3fc7-ae60-59a350698267 | -2.62708 | -54.22731 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a30981c2-7d13-39c6-8b9a-c2d3aa6e1066 | -1.2541 | -51.79156 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9efe384-808a-3260-9482-b85e5b8cc963 | -2.4816 | -50.36712 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d12b7cc4-0f1e-3659-a57b-1e6fccc18d51 | -3.11536 | -53.80613 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e24d45ea-64a3-3f9d-a2b2-8c622a96df3e | -4.07164 | -46.68568 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a8d4c40-74f3-3e87-b0a1-5b5281b65e73 | -3.055 | -52.76277 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e8127b4-2d9c-3aac-a702-377902a9c641 | -2.47187 | -46.56291 | 2024-12-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b81ca301-73fd-30a2-aacd-70368b6335d0 | -3.8518 | -46.53693 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 93887938-faa4-348f-9223-05d61d8b4530 | -4.34872 | -45.93073 | 2024-12-01 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d93b6531-4372-3a1a-9309-abc04047d8e6 | -2.96668 | -51.01955 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15166ce2-cb66-3886-8b0f-a9acfa323dcc | -2.53216 | -54.07272 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e9fc974-be85-3224-acdb-2c21ee6e008f | -3.6366 | -51.45555 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b232086-7143-3a2a-8ad7-2dbee768d025 | -4.31739 | -48.08978 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a867719-2aa8-336b-90a5-6d77b3581abc | -2.1466 | -54.87567 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bf5798ba-9ba1-342b-8db5-d901b41e938d | -3.22422 | -54.23254 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2204992-e1f4-3670-a059-faf5a4c58e65 | -3.25083 | -50.61539 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ef478d6-7cc8-34a1-9491-c8f19a561184 | -1.44099 | -55.22995 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52ca7d2c-6ed5-3950-9c7d-ea16b1f61374 | -1.77873 | -55.27391 | 2024-12-01 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9feb1661-d3e8-3800-9fc5-e54d53062a10 | -3.29657 | -53.83531 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e799972-cbce-3f62-93d1-512d5cd0784c | -1.5299 | -52.66531 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b7965abe-0ce8-3d02-b2de-1eef2b44e592 | -3.48046 | -51.25781 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92d92819-9bfb-3456-bdd7-a957d52f7bc6 | -2.83049 | -54.08888 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3f8f1357-a608-30b3-a762-d525d068e36d | -4.31389 | -48.08925 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7eefd88-fdf2-318c-a115-608cb3f5bf8d | -1.0787 | -53.228 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b757334-13fc-315b-86f5-1ab80d549f89 | -3.30037 | -50.49572 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78b674a4-e4b0-3113-957f-05d6db892b88 | -1.5257 | -52.66876 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17d6c6db-a948-3ef1-ab12-4ccba7d8d071 | -1.99351 | -53.2888 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b9eecb6-23a9-3854-985a-57202c37384c | -3.30964 | -54.11098 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a72c3e01-7f94-3b20-8086-dcd35ab7110d | -3.12279 | -53.80719 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| a56e7ef5-a36e-351b-91e7-d5a48c1872ae | -3.62818 | -49.85376 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 817ef171-1bfc-3777-800d-c4eafbbdc4e0 | -0.72388 | -51.69968 | 2024-12-01 04:44:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1ccf9b5-81d3-38d9-922a-e328308efedb | -2.95969 | -50.57295 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47b00341-cc85-3aeb-b94e-b922632f194e | -1.28186 | -51.7274 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fcda16c-9569-38bd-9cfa-add7cf6f50de | -1.2082 | -54.16948 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c883f0c3-1183-33a4-8e5d-53ceba6ab21b | -2.60821 | -46.57751 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08f3d62b-9075-3737-a4c6-c7fb61374105 | -3.21809 | -54.17507 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b21e9762-56d8-3403-a8b0-69872a0fbd44 | -2.56442 | -46.40624 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c2346f9-45b5-3c5c-9227-3b537ce1d9f3 | -2.77374 | -55.33823 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d9dc376-c109-3bd3-b34f-611261daaa77 | -3.24308 | -53.63839 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e449aa1-25c4-3289-b8b4-7e9dbbff5982 | -3.28684 | -50.62456 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b82bbfa-524f-35ea-90ee-754417b0a824 | -3.59146 | -50.36841 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d1f06e9-46c3-36f1-8712-119e68e8d053 | -3.21058 | -53.12001 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 927f8ace-eb98-3f1e-a07b-68b1e5041bb5 | -2.6795 | -46.6062 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4dc5e601-49b2-3dfa-9ac5-e791305cc5e1 | -3.8011 | -58.97403 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e55a1e90-6458-3454-89a2-46299c114d60 | -3.86866 | -51.0105 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8be2d520-750e-3441-b46b-ab9009ccba08 | -4.16608 | -48.62015 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 657b81f6-5600-3866-b7cc-131683ec5d8a | -3.207 | -53.11946 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bb3112c1-d984-3570-bb25-66cbef1a344f | -3.41999 | -54.02552 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76c797df-5606-3f86-a3c0-0bb14c00b6b4 | -3.5091 | -53.83523 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 507eb234-67d6-38d6-9002-cb6045865719 | -7.02883 | -44.84368 | 2024-12-01 04:44:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d33f2197-6ea8-335d-825a-d635811a6bdc | -3.64553 | -51.42075 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5351252b-f9f0-315b-937c-b8c7d6721651 | -1.18948 | -54.03911 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30dad5e8-35a7-389f-82c2-869866da9b44 | -0.99709 | -51.77932 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7295c189-f1bc-31f1-b71f-ccaf970d4252 | -1.23886 | -51.62236 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 89424599-4a99-3d03-a74b-a0e9780c11a1 | -3.27164 | -53.41438 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e49830f-8805-3505-a90e-293812e9fda7 | -2.97071 | -53.45179 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 700e064d-4438-3860-a9ee-1094e0c2a03c | -3.35902 | -49.75827 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 085212af-7541-3451-bcd9-196a5a1dc1f4 | -4.40905 | -50.82238 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95941733-6885-38e6-92e5-a28e5b80d230 | -1.95209 | -50.63178 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d61e19d-eee3-3fe3-9e18-6f633c5c5c04 | -2.60422 | -54.22323 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67695324-8087-370a-8f60-436ceb48255d | -0.18797 | -60.68009 | 2024-12-01 04:44:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a5e4d6c-a3a0-3d44-9a4f-439246219ed4 | -2.36115 | -53.86265 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b42f23d5-480a-3ef3-ad4f-2e685e71270c | -3.30097 | -53.83154 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50a9bd54-ba6c-3634-86d3-7e0d058a649f | -2.22423 | -53.62687 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f891ea30-cefa-3838-b500-3e7667bec361 | -3.17178 | -46.31993 | 2024-12-01 04:44:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b4988b6-84e6-38b9-9bb3-5e4b39c9c5fc | -3.097 | -54.01648 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4849ea38-dfd9-39e4-a296-8ed04ccdd07a | -3.82152 | -52.25031 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c80d6fe6-bf6d-3a9b-a39f-c378dd974071 | -3.33058 | -50.21771 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README60.md)
