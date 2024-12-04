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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04b99efe-53a2-3395-9e65-144052a1e91c | -2.88671 | -51.8236 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 328b6303-d37a-344c-9fd9-d84d6f5cc7a8 | -1.47475 | -53.80511 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92716ee3-d35c-36a8-ab63-aba7ec470df8 | -2.00435 | -54.11215 | 2024-12-04 04:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53548d46-0f4d-3386-9997-c56c3a4c94b0 | -5.11813 | -43.20895 | 2024-12-04 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50670f00-98ec-3371-b873-ce5dd1a22c69 | -2.62734 | -45.7369 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 34bab4e0-a8de-33a8-a7dd-309c1f3fa9a2 | -3.05887 | -52.76461 | 2024-12-04 04:10:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d280b27a-4ea5-366c-a547-0882b0fa82d7 | -3.87273 | -48.36691 | 2024-12-04 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a3e207d1-979f-37ea-9be1-b03c1e127310 | -4.05179 | -46.9905 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b4b5047-c08c-352b-9a29-7d537a3b847f | -3.10706 | -53.76049 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ae99e95-d012-337d-b172-05d1040d7bb1 | -2.95686 | -53.72458 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d615684a-d9e6-3443-9f9e-49758fa52ed3 | -3.37132 | -51.06833 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3755326e-751c-3630-ad1f-0bdd7b6726a3 | -3.47405 | -50.23845 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 624f49e8-f08a-3e4e-87f1-bedbe1d59e98 | -4.04713 | -46.81717 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d29333cc-5137-3e4d-bda1-6982a00f9819 | -3.98315 | -50.52146 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bbc06cc8-988e-3dcc-8c4e-c77ec69b206c | -3.20283 | -50.64372 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2afb6b0-8bce-3a22-b9db-8da9701fa2f7 | -2.67626 | -46.62299 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57ac9ac0-3898-3c76-a787-ab6f066b8227 | -3.46353 | -42.00272 | 2024-12-04 04:10:00 | NOAA-20 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8aaf0ec4-79d8-3b43-bce6-ce82051ee95d | -1.69536 | -52.33546 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec24a48a-f390-3eaf-bc2b-499754819c1e | -3.25658 | -53.66299 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86061454-9034-3db5-87dc-b3d358e4d49d | -1.226 | -46.52818 | 2024-12-04 04:10:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4a5ad5b7-416b-3b5c-a5c1-921b57617da4 | -2.0265 | -46.34148 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| df14ead4-1cb5-378b-a9f3-7cd14f5b345c | -3.86843 | -48.36627 | 2024-12-04 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 524dcb69-fbb1-30ed-88ac-bab68c454ad8 | -2.80563 | -53.04539 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27043a5a-8b50-36d7-83e3-d3e59ad4a609 | -1.69551 | -52.61914 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 666b98bf-b57a-31f9-9c88-d9df4360155a | -3.66454 | -47.12591 | 2024-12-04 04:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 867ad4d6-d1a5-3fb2-89c7-83a62aabc3e6 | -5.12632 | -44.28527 | 2024-12-04 04:10:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2dc5b1a4-e9a2-3af2-829e-e4f48aa42663 | -3.74528 | -52.44159 | 2024-12-04 04:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f72575a0-15e2-3698-a3e8-99a4b0d9702a | -3.71054 | -51.0699 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 94783b25-468b-3aa8-b09c-02e4d34944c0 | -3.08546 | -53.37618 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69310bb5-b271-33c5-b3cf-a5f8c7d7e6a2 | -1.91775 | -47.05205 | 2024-12-04 04:10:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cfbb5361-7d02-31e1-b98c-fe3b18aaf208 | -1.69748 | -52.62012 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f445216-4714-3efd-b5b2-8c73d7f12ca4 | -1.55059 | -53.79367 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cc77c30-457f-3c7c-97f0-89cf957d5df1 | -5.4203 | -44.85688 | 2024-12-04 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bf223ce-69cd-3a2b-b93c-89c94f004571 | -2.75886 | -45.19466 | 2024-12-04 04:10:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b9a2eef3-0677-3d0a-8be6-4e05bd7b14fc | -2.47142 | -46.5529 | 2024-12-04 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c15a54de-686a-3f09-9315-28b3165f1e7c | -3.8128 | -46.95281 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8d543f55-b729-306a-9d21-330749303275 | -3.25825 | -53.65748 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2a1c0fc6-66e7-3b1c-b82e-bfcda97b10d5 | -2.47302 | -46.54314 | 2024-12-04 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 378d4964-7cc1-3768-b8d6-0e641c5e9813 | -3.20091 | -50.65557 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 038f0010-6257-36b6-9d42-c61844fb5c9a | -3.37068 | -51.1038 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8334c6a6-584a-3779-aa8c-22eb362fbdf5 | -3.85722 | -46.52454 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b555875a-15a8-3b76-8cd9-4e0029aab049 | -3.08434 | -53.37722 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2ade2a4-cf8e-3437-aa68-67cb008d1636 | -3.8533 | -52.16435 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 18e584f2-37f1-372f-9a47-ad6160c578e8 | -4.08185 | -46.68773 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77af6e13-3c08-3eea-904c-1a8119f78c08 | -3.06639 | -54.05561 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36eec7ea-36d8-3b8a-a56d-bbf854b74593 | -3.84657 | -46.5179 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b4f3b703-e955-3824-a82d-ce3afcd78eda | -1.75009 | -52.61951 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4e79ac02-fd0f-3faa-93db-a431d43393d7 | -2.67237 | -46.62237 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 685fae5e-2d1b-3abe-a253-ec9ad7d15bd5 | -3.69702 | -51.08691 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 854eeced-401a-3de8-85c4-754779fe3196 | -2.07024 | -46.32654 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db5764cb-d7b6-362b-87e7-19a38c41bd46 | -2.67278 | -46.12698 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67b9f990-cb44-3301-addf-a5f5503d1ea1 | -3.57468 | -50.31314 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6d16b38c-1ce3-327d-8bde-cba9ba7836ba | -2.63174 | -45.73312 | 2024-12-04 04:10:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 58e2a775-ca96-3bb1-87b2-f323bdcd7027 | -3.20547 | -50.64957 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d43d51c4-223e-37e0-94c1-5392f7c41833 | -3.37186 | -51.06517 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ce19a15-216e-3fd0-8b1c-0ee4606f47a4 | -2.68131 | -46.62127 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81fcb408-496f-3c0e-be29-633c858f3abf | -3.9782 | -50.52056 | 2024-12-04 04:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae5edf9d-ff10-3acd-bd12-bf83ea4bc947 | -3.19679 | -50.64887 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f11fa31c-128b-356d-ab17-b5e797088873 | -2.82451 | -54.14811 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 42222d53-d8c6-3599-b633-3032def749ad | -2.82383 | -53.06196 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ec29a66-618b-334b-8e41-928b0c40d3d8 | -3.55596 | -50.40354 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84516482-43ef-3e41-9300-e1ad2ed1f005 | -2.94926 | -51.40753 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d49acf4-0da8-3fb7-b66d-bcf290b52406 | -2.79263 | -54.1421 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 93b95dd0-d942-39df-9499-7ded7eca8463 | -2.97334 | -46.94909 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df764248-dd90-3e66-9dfd-8ad2041de7ba | -3.25231 | -46.28441 | 2024-12-04 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78eaa6d7-1833-33df-8208-fd44abd6b9ee | -3.68846 | -42.04109 | 2024-12-04 04:10:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 79b83e4f-b4fe-3c15-b069-3c0b63c0a95d | -3.80719 | -51.01008 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 581ef984-0276-303c-a1e3-07799c0b1e75 | -3.81379 | -51.66705 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c297f80e-6357-3667-b928-7919b973fc89 | -1.99908 | -53.2857 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f02ecc45-1e76-336a-b20f-4f1759594800 | -2.80891 | -53.04135 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57a0f9da-cf6b-3142-873b-9f568ce5004a | -3.72436 | -50.05722 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0589484-09e1-3772-85b2-f60823c4aaff | -3.80998 | -46.55086 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9432bfa-32ce-337b-ab3d-bcf96ee61155 | -4.90178 | -40.5536 | 2024-12-04 04:10:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3bf10804-729b-3b4d-acac-234422ca76ee | -3.23888 | -50.42117 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d40c9fcb-46b6-3c70-b7aa-bfed13c9b87f | -1.65031 | -52.39136 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bdad2596-d08d-3c56-a10e-7787d498fdec | -3.52482 | -50.86108 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 40cec2dd-6129-31e1-b254-ab9bac30f2ff | -1.651 | -52.38723 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| bbc7d191-6fc7-365b-815d-1a9f42531139 | -4.06923 | -46.70307 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c329fac6-7f2c-3673-b940-c3c67b1129a6 | -1.65733 | -52.75603 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e2c8cdf6-8e4b-3f57-8095-80f12c1f6836 | -2.57168 | -46.57393 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51e8ea6e-6e97-3400-b490-58d3aeb69683 | -1.22178 | -49.15213 | 2024-12-04 04:10:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5a274ac6-262d-3501-adec-6c64b6e69c85 | -3.2478 | -46.28839 | 2024-12-04 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9b9c7dd-3b32-3e87-ab85-81b8bfd47a7e | -4.19339 | -48.42019 | 2024-12-04 04:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb72573c-c26f-3cd1-9c98-93b5f9f02d76 | -2.81686 | -53.05181 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a59b9e28-24c1-3150-a4c7-527f3592c555 | -2.81188 | -53.05994 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61f94a1e-40a4-39e0-a659-6bba2f735344 | -3.11263 | -54.69197 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38ddc4a5-ca3b-3000-bcca-347056921664 | -1.70621 | -46.21081 | 2024-12-04 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 704e57c3-3c6e-3789-b1f4-e9f0caf910db | -3.10993 | -54.66822 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5cf6be7c-86cf-3d47-8042-30e4d50978d9 | -3.4807 | -50.24081 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f87be377-788e-3b66-b906-e211b86060c4 | -4.07276 | -46.60701 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6771a407-be07-3057-978b-f320fa38dd0f | -3.18147 | -54.52114 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8fdfb2d2-ed41-3720-8f9c-247f06d8bb76 | -2.55925 | -46.57692 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79a685ed-f35d-3b8e-967c-40b36908ee73 | -3.02574 | -45.5179 | 2024-12-04 04:10:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fa0ca92-7ac6-3a69-be72-d18a49b7d484 | -2.90369 | -51.82356 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 103e3915-5559-3db9-a568-5fb9c20a0225 | -2.55042 | -53.41327 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10209a3b-1529-3082-824d-596d4595c625 | -2.99574 | -53.8231 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9234fb84-862a-3a45-a458-0447937b8973 | -1.7591 | -52.63865 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ff98595d-82e8-3599-88c2-eeead6001ecb | -2.57225 | -46.19831 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 278f4594-7b20-34a5-a236-1a7c1e6391e4 | -2.79916 | -53.06241 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1afe20c-7180-3208-b62a-17bccf98d2a7 | -3.83493 | -50.90895 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README27.md)
