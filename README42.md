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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 042ab52a-fe3b-3fac-95fe-e4d0cbdecbc7 | -13.70792 | -48.81537 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9513d902-f52e-32fc-842d-d1e2583fd747 | -12.90164 | -52.06263 | 2026-09-28 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0031993-1924-3ee2-bfdd-70066c3cc46d | -14.72139 | -45.57152 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 844cfc5c-06fd-331b-8797-1ae0e9f7cab6 | -17.68322 | -47.98124 | 2026-09-28 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08f42e6e-a067-3d2e-ab92-0a1c3d347478 | -16.39219 | -42.56931 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c47de31-2c64-3f0c-91d8-4f9d2c11e66b | -14.51903 | -48.3079 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c1017047-b50f-39b7-8154-b4502845edf2 | -15.05509 | -47.22983 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 48f4caed-9de8-36d3-b1b5-4ce38e43aa9a | -19.10454 | -43.9579 | 2026-09-28 04:36:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b041ebf-ffde-31ce-97b4-f9dbb79ec0ab | -15.15382 | -43.61122 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 26238736-d1f8-3745-8a9d-f9ac06986835 | -15.2237 | -46.35318 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b874c090-570e-3878-9e6c-47820bff8b36 | -14.52578 | -48.30897 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 404b2848-90d9-350c-b5f1-bbb0304a746c | -15.74061 | -51.10962 | 2026-09-28 04:36:00 | NOAA-21 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b42c937-aa39-3cba-a58a-7789a7b06c28 | -15.22308 | -46.35756 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f88857d7-c797-37ec-aff5-d278c70a8429 | -18.10153 | -44.37252 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e589906-c5d0-3c49-a89f-1a1cb9f562e0 | -14.53299 | -48.31698 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de963387-971b-38cc-94d1-63d56e3def9b | -13.69407 | -48.81681 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7279614c-c1d8-3b11-a18b-824af67ff245 | -13.69685 | -48.82092 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 91f47ef8-d658-3463-8bcf-1aaaae02cef9 | -18.11356 | -44.38258 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d99b0cac-8841-3d24-a579-8e26f1eaa9c9 | -15.19544 | -48.43086 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de65030b-0853-3096-8000-968045e18d8d | -13.37829 | -51.32073 | 2026-09-28 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac4f4d0b-7f04-3035-af2e-3c2fd66234a3 | -14.59438 | -45.59573 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78d9e25c-9787-3f5b-b7d1-f606a9b7edc0 | -14.52523 | -48.31264 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 03afe0c5-5a98-3989-bbe7-784ed83e1917 | -16.22106 | -42.87342 | 2026-09-28 04:36:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b07152ef-e914-3357-9527-1698875de29a | -18.11407 | -44.37827 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cf1d0ebb-d4e7-3229-bfb9-8f5173bd7b8d | -15.16618 | -46.15545 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bccd13d-1c12-32ee-b022-454ee24f2f19 | -14.90308 | -49.49073 | 2026-09-28 04:36:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3363db09-f692-37ce-9e0e-6e727ab4ef14 | -15.14832 | -43.61932 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3b14d590-96f8-315c-a01a-5fbde30c8320 | -15.18304 | -49.39334 | 2026-09-28 04:36:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f867858c-1860-3992-8a73-8241f2853cc6 | -16.39013 | -48.97843 | 2026-09-28 04:36:00 | NOAA-21 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1035157-5837-35f6-98a4-552946f03d68 | -12.13384 | -61.14697 | 2026-09-28 04:36:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 93708838-e553-364c-bd0a-356a60c9a0b9 | -15.10465 | -53.8828 | 2026-09-28 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ed2996f-b5bc-3fc5-9623-c9fa62945540 | -16.46664 | -55.07784 | 2026-09-28 04:36:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 60f7a9c9-902a-3b39-a12b-8f437df83475 | -15.19488 | -48.43466 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d96b9dd6-4198-37e3-9d77-9febb89830e3 | -14.73673 | -45.574 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4a4b630-8cfe-3a59-9f6a-e75457ad49ea | -13.89285 | -53.66606 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63850d3a-54d7-38cf-9423-90fc952a4351 | -15.55782 | -47.92079 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0d711fd-bf63-3693-a571-fbbbb7fdf809 | -19.0842 | -46.65087 | 2026-09-28 04:36:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bc43caa1-058b-3a91-bcd7-53333238e023 | -16.35788 | -42.56934 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1c981b6c-ae8c-3864-a328-ade5c4a43b1b | -17.25175 | -42.83475 | 2026-09-28 04:36:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9eedcd36-297d-302f-9ebd-ef55426c7b8c | -14.49039 | -48.33743 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86e5e9d1-61df-322d-bcdb-9831c76225a3 | -18.10537 | -44.37727 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74949f55-26af-3644-a1a8-284b73612564 | -17.68673 | -47.9818 | 2026-09-28 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b7889a1-04b2-31a2-8d46-56b33f7f541a | -15.15821 | -43.61183 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 10b43041-44bf-3019-9822-1cc089f51f93 | -14.48507 | -53.63729 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74c29bf9-e4b9-3710-ba0c-4f2080657c9d | -13.71016 | -48.82306 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fe40048e-eb8a-30f5-96dd-a85f9b855510 | -15.82772 | -42.56234 | 2026-09-28 04:36:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 663cf97e-f1f4-33e7-9d05-f1b0660cf3a1 | -15.40956 | -47.9024 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd25b646-e0dd-335c-892d-f993bd1df921 | -14.7972 | -45.95166 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25345b23-4fa8-3f4e-9e21-ad134b14350a | -12.80093 | -54.01201 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60e825a5-b7e4-3f38-8524-c958482b2786 | -14.11465 | -46.29885 | 2026-09-28 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d8657d0-fda6-3452-ba40-e5af8bfd5116 | -14.0926 | -46.32299 | 2026-09-28 04:36:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 627dc464-f7d0-3070-98b8-feef4c728a7a | -16.35313 | -42.56847 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a4362d4-60dc-3d9c-8926-334ff05ac16a | -16.36346 | -52.41388 | 2026-09-28 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 698a22d2-f30e-3afe-9d59-22388dc423cf | -12.9073 | -52.0718 | 2026-09-28 04:36:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8eb4c7b2-2722-3a01-8c13-eb4354404de3 | -14.90585 | -49.49483 | 2026-09-28 04:36:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aa32aa15-ed41-36e1-83fd-d3923517f47c | -16.3873 | -42.56715 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7b125218-c4fa-3897-b06a-0e12300518c8 | -16.35247 | -42.57389 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48b7fe91-8db1-3fdf-907a-2e0e249d6ccd | -14.52634 | -48.30529 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e4c14377-1116-3bbf-9f90-0de23b260ae3 | -16.36068 | -52.40939 | 2026-09-28 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0b3f1db-4401-39df-a040-f760db27411d | -13.70018 | -48.82145 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 96437b5b-921f-350f-b96f-f6a20be5419c | -18.11304 | -44.3869 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4f9623bf-9fb8-372e-8537-4e7c735bfd86 | -14.73608 | -45.57879 | 2026-09-28 04:36:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf66f152-f2b3-38b1-affc-0c45b23193b6 | -15.41302 | -47.92693 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6616f7d3-38a6-3608-885e-e5bec026d23d | -14.49169 | -53.64301 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb8f7a8c-3beb-3478-bb3b-76c666f9c062 | -18.11791 | -44.38308 | 2026-09-28 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c7bd8e2-d45d-3106-b83c-996dd3830fd4 | -17.68963 | -47.98656 | 2026-09-28 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0a322d0c-2758-3069-8ec4-f3718e314072 | -14.49937 | -48.32367 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de0c0743-9193-3faf-9918-d49e9320fde7 | -15.1675 | -46.14615 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 094ff146-7a75-3132-8b81-e61b62eae9a7 | -12.79708 | -54.01131 | 2026-09-28 04:36:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3958fb57-1a80-3db5-9899-004a0f881550 | -15.1977 | -48.43897 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c185e683-0b1e-3bfe-a1ac-c9394c7a56b8 | -14.79657 | -45.95632 | 2026-09-28 04:36:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e54c31ef-e222-33e9-ac3d-5a71ad8df23d | -14.53354 | -48.31327 | 2026-09-28 04:36:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7583c18b-c6cc-3778-ac5d-6baad03285f1 | -15.16684 | -46.15082 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a965b05-870e-3d8c-b967-5ca58ae8c06d | -15.13463 | -43.62173 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e8f74c04-3fd8-35f7-a892-1085f57dbd57 | -13.38784 | -51.32616 | 2026-09-28 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62807f19-7cd7-3093-a333-087fd0561463 | -15.16486 | -43.5949 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7267fb5f-18ff-3abc-b242-94039a7e0bb7 | -13.4517 | -48.60204 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f222a8bc-55ab-3fb1-abc1-fe18ea9577ce | -15.46872 | -46.14962 | 2026-09-28 04:36:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4859026b-c62a-3cd9-bc26-d132fd6458e8 | -14.90254 | -49.4943 | 2026-09-28 04:36:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| daa148b6-034f-3629-a29b-f8e1969ff4ac | -15.11947 | -53.88549 | 2026-09-28 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d00f1ff-d2ef-3255-8504-3ac96476046e | -13.47227 | -48.60162 | 2026-09-28 04:36:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc91e464-a3aa-3587-a33c-3044053ef0a5 | -15.5624 | -47.91364 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dc81af0-5ced-3a7f-bff4-b66d82bbc0ad | -15.34372 | -42.16911 | 2026-09-28 04:36:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 8192bfcd-a51a-3856-8ea5-869e880d6874 | -15.17474 | -46.15894 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2606cbff-d268-3801-9193-0cbdbaadb9d0 | -13.58204 | -51.45089 | 2026-09-28 04:36:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65d12d8f-07e9-3e4b-99c8-37e5c24d21fa | -16.38737 | -42.56898 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ad04af14-8860-3628-982a-e0aa577630d2 | -18.51644 | -42.41808 | 2026-09-28 04:36:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d742b496-9148-35f2-9c68-575a94d20fcb | -15.9333 | -56.25557 | 2026-09-28 04:36:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 70a60c85-e090-3733-9aa9-c67f0e948809 | -15.10387 | -53.88735 | 2026-09-28 04:36:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7ecd8c3-5278-338f-b73f-89ef0061e0a9 | -15.14888 | -43.61497 | 2026-09-28 04:36:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 99de8c2c-27f0-3b75-9ca9-f8ef687ef8db | -15.17039 | -46.1629 | 2026-09-28 04:36:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e2f5a289-3380-3faa-a8be-55caff071dad | -15.34594 | -48.12163 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41fb5442-3900-3673-a365-8f7562743cb1 | -15.41241 | -47.90702 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9251627a-8e79-308d-9b2c-a297ca5e80cb | -15.76347 | -52.46736 | 2026-09-28 04:36:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd67946c-f486-371f-9cbf-3138279eeaf5 | -16.36005 | -52.41323 | 2026-09-28 04:36:00 | NOAA-21 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2438ae50-f623-3b46-b077-3586967f6c56 | -15.41069 | -47.91882 | 2026-09-28 04:36:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 26ca8006-a02c-3543-9046-739a18e9a747 | -17.83342 | -44.39593 | 2026-09-28 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfa6845a-45b4-38bd-84f8-cf6c21d9c186 | -15.18529 | -48.42928 | 2026-09-28 04:36:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e287471-d79b-398e-91fa-8e83eeb582f2 | -15.55839 | -47.91693 | 2026-09-28 04:36:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dee3510c-d1c2-3aeb-b708-789eb10a30ac | -16.38799 | -42.56357 | 2026-09-28 04:36:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README43.md)
