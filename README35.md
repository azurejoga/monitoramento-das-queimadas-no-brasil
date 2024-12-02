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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f808cc92-d0f8-3f42-a12f-47fe7fcc72c3 | -3.25948 | -53.63852 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecd1fc31-72b2-322b-9040-372c764acd8a | -6.3692 | -47.36059 | 2024-12-02 04:25:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8c4700f3-7779-3cc0-b988-84f6f5120c51 | -2.349 | -54.37446 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f7817e7-848b-3661-81c0-c56a2f3bdb3d | -3.26794 | -51.10928 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f591a5a-9c79-3397-a183-d3d579168ea0 | -4.04215 | -50.73251 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c8be143-cc50-3a4a-984a-c63d585ac7fb | -6.00138 | -45.42189 | 2024-12-02 04:25:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2293b692-7446-36e4-adca-3bfeb589965d | -3.26042 | -53.63284 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6affd166-e79b-39ad-8751-b2bdb5f27f88 | -4.00541 | -46.94054 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74942828-ff1d-3e66-b607-499ec4456ac9 | -3.80456 | -46.53936 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf6cae99-870b-3ff9-9155-a28e28a409d1 | -3.7466 | -52.27275 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70f21785-6fe5-3d5d-a88e-fb601ae30ce0 | -2.69051 | -51.87997 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 125a2db6-deb2-3576-bac2-7afd49572d78 | -4.58492 | -43.35367 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 31354717-421d-3ca5-a97f-f228154523ee | -4.32279 | -45.9231 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bd26153-882e-309c-8b22-c9828432d054 | -11.07775 | -44.30901 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aa54189-7d0f-3511-9247-da21a1957427 | -10.65281 | -44.48862 | 2024-12-02 04:25:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cfa21c85-6497-34f6-9f4f-c64feb7cdd72 | -4.74955 | -41.1051 | 2024-12-02 04:25:00 | NPP-375D | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7c00c91a-c973-3783-8e8a-88da577b885c | -4.17557 | -48.20156 | 2024-12-02 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4c6dec9-71dd-330b-b920-61fc94b4a190 | -3.86247 | -47.05058 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da44f9d7-392e-36ce-81dd-27fdcfd3f4ae | -4.4217 | -46.15098 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 24451444-c40e-36d3-9681-40ca7c63984b | -3.84805 | -46.52451 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75b0ee02-74ec-3156-816c-78be393e8ca5 | -2.31024 | -53.89904 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d62c238-4a69-33ff-a0ce-b773f01da625 | -2.8198 | -53.95786 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc2fb43c-2f1b-3439-8563-8a9fdf9c1dad | -2.70706 | -52.00661 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcb1e582-c414-3a47-938d-c62098815435 | -3.82908 | -46.60074 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b657d55-51ed-34fe-84f9-a4d7d1bb940d | -3.8015 | -48.91278 | 2024-12-02 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee379285-206e-39fc-804b-e2162cb0021c | -3.54921 | -51.45342 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d1a5c7f-2412-3f18-b102-be141625e617 | -3.45771 | -51.42194 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce4df5b1-d343-39f2-876e-7516675a8597 | -4.03405 | -46.9341 | 2024-12-02 04:25:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5329367d-6e12-356b-b6dd-3c56fe6ad0fa | -3.98235 | -46.72997 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ac7f7f5-7578-3cf6-8f46-8c25ab694bf9 | -3.15892 | -51.11508 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2cb14ca-d914-3b33-8ef0-bac9cee423b2 | -4.48738 | -46.05849 | 2024-12-02 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fbed04bc-4a23-3a01-880d-854f0b25e1d8 | -3.81736 | -46.58812 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9df1ab00-61eb-3fdb-8916-e410878a0c63 | -3.06868 | -53.68151 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd1c0e0f-0638-3c25-bf8a-2a99bc3032ec | -4.57932 | -48.02636 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f7dd356-9c82-3a2e-8a25-f980d30fd735 | -3.27477 | -50.21268 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cfc752e-99f9-35d2-8147-255d445d96de | -3.73199 | -49.93604 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ec56437a-6c52-327a-ac5b-b98793a436a6 | -3.96327 | -46.50377 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49edb3fe-70fe-327f-840c-0eb08185370f | -4.18842 | -50.67695 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 797a275c-07ca-3131-9518-dbcc15cad288 | -3.65041 | -51.12089 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07cea2bb-b330-37b3-bc4d-63e053cb72f0 | -3.25096 | -53.92655 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e777c4c7-649a-3913-a8b0-d2e9353a72e9 | -3.09702 | -54.29641 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c07b5319-ecb6-3b3c-9a5e-039c404e6577 | -4.95421 | -42.7984 | 2024-12-02 04:25:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| acc45446-915b-3186-b643-22387206023a | -3.78937 | -46.69912 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc84f921-3382-3f97-83ef-887380d29f01 | 1.88734 | -55.70166 | 2024-12-02 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e3bfcbe-2065-303d-9b71-669c5d5ffb0f | -3.79033 | -52.40161 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e44c74e-224b-392c-a556-408430a40bbc | -3.80409 | -49.73402 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 374b68f7-4d6b-3dc7-95b0-8cad5955d919 | -3.8235 | -46.59266 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f997f2f5-48f9-38d4-bf7c-b8a394d1c904 | -3.25854 | -53.64423 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 896b020b-c48a-3251-8897-95003a86696b | -4.03465 | -48.87804 | 2024-12-02 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21466300-c29e-341b-b943-b15f18065e36 | -4.58552 | -43.34978 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7c67e08-9281-3f83-9b6f-9f51ea7c6754 | -4.28375 | -47.06051 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c7fbe94-535e-34ca-bb75-12d8ea5d1622 | -3.97349 | -46.90265 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30306f7c-54c2-304b-abcf-be2c4a9b5088 | 1.94393 | -55.71165 | 2024-12-02 04:25:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c876ac3e-4902-34f8-9a76-f08ff1c69ccc | -3.72734 | -49.94019 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bc7d8da6-1196-3eb9-87ee-851067c5c8ae | -5.2918 | -44.78513 | 2024-12-02 04:25:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 506ee711-eebf-35f4-ba0b-e41fdfd775eb | -2.81413 | -53.96028 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3625ba23-8a8f-3cec-92e7-237b654cb8b1 | -3.83187 | -46.56161 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 317c4ed2-20d2-32a3-aa35-cffdfef9beb3 | -4.17858 | -50.66121 | 2024-12-02 04:25:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8e3d148-b6f0-3147-8925-eaca85bc256c | -4.01436 | -49.94261 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5bed9a4f-1c09-3238-9464-83f5ed628cde | -2.34955 | -54.37116 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d319bb2d-765f-3097-b1eb-426c423f9589 | -2.57746 | -53.67813 | 2024-12-02 04:25:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4509c860-c119-367e-b722-0fde18ff5211 | -3.98291 | -46.72643 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfb9f7d6-bfe0-3b40-82aa-3cf184efc105 | -3.8263 | -46.59669 | 2024-12-02 04:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 488dd953-d0c9-325b-b0ae-796783daa76b | -3.04343 | -49.37273 | 2024-12-02 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fb062a81-4efe-3ec5-9998-62463220aaa7 | -4.02942 | -49.93276 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1fb696e8-7125-3348-ad15-142b23c6fcb4 | -4.31096 | -48.21386 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afd9ee65-9c76-37d0-9010-e38bbfc66baf | -3.86199 | -50.89908 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4dba506a-aa8b-3408-9ead-3c3141cc4d0c | -3.26767 | -50.20631 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e0dd6dc-8b37-3130-84cc-9e245d0610db | -3.25759 | -49.89802 | 2024-12-02 04:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f478fe44-2da5-358d-9b1e-de0bd4d7767e | -3.8572 | -52.31264 | 2024-12-02 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a18e9ad-768f-399c-89e8-6dbeacb21450 | -4.58201 | -43.34925 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 165b674b-4c86-359e-ab02-215b38d139db | -3.18642 | -54.33694 | 2024-12-02 04:25:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 34a07c3a-3706-31e2-8d5f-71519262ce53 | -3.25449 | -53.6377 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 009f0279-a645-32fb-ab63-bde49ef017d3 | -3.74566 | -51.3021 | 2024-12-02 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d64d2c46-cf6d-36fa-a623-a0c84b70caf7 | -4.31295 | -48.09131 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 487e9f74-945f-3a5e-b99d-0682a384f3d5 | -3.95605 | -46.91857 | 2024-12-02 04:25:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d509a273-86db-384b-9507-65942dad591c | -6.45996 | -47.54289 | 2024-12-02 04:25:00 | NPP-375D | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fb386935-a643-3a33-8ffc-d5f98554f1f7 | -3.77987 | -52.03149 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 514f568b-7a48-35e6-b3a8-0167f9478579 | -4.84627 | -41.32982 | 2024-12-02 04:25:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 0d48983a-b6d8-3fa7-986e-e73ec510b87f | -4.53683 | -45.70158 | 2024-12-02 04:25:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46b6aa7e-2dfc-37ee-aed0-7782a3ecfc73 | -2.85082 | -54.19615 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 777aa417-0991-3acb-b81b-e0c391cca299 | -2.91747 | -54.12034 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a47a128d-68ed-3d1e-ae4e-d6f011d56fdb | -4.29631 | -48.2155 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 782d9f31-9516-379d-afd6-c4448b1fe483 | -11.0601 | -45.37772 | 2024-12-02 04:25:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a02943d-c10c-33ba-872f-a7be2fd716dd | -3.64622 | -50.21375 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68af1aeb-53c4-394d-9c7f-0de75660a97d | -4.32279 | -48.09685 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2225d0c7-d930-3e40-b88c-941a005cebdd | -3.95946 | -46.01451 | 2024-12-02 04:25:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7fa4479f-74b2-3a61-a489-0e3bbc9b6bd4 | -4.63151 | -45.46161 | 2024-12-02 04:25:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 67440f06-50ba-3fd6-af03-8329f240cfc6 | -4.31644 | -48.09188 | 2024-12-02 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e77fd203-38e0-3161-9547-bc8f260c831b | -3.2499 | -53.93277 | 2024-12-02 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 389b687a-1977-3f83-a6e1-25ad3fa302a7 | -4.57731 | -43.35647 | 2024-12-02 04:25:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9dcb69cc-02ff-32fd-95be-c331beea158c | -3.27789 | -48.77995 | 2024-12-02 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff4f9415-b5f4-3226-9989-44f9d0049d23 | -3.43732 | -54.6062 | 2024-12-02 04:25:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f613086-bc62-3f17-ad5a-0cb160c0b7ff | -2.3501 | -54.36785 | 2024-12-02 04:25:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 118b36cd-f4ef-3c08-b176-c0b7687356bc | -4.50859 | -42.07097 | 2024-12-02 04:25:00 | NPP-375D | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8eaa8ef0-3210-3696-a6e8-706e02edc022 | -2.89799 | -51.37057 | 2024-12-02 04:25:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 12113438-b441-3ca9-a76e-4ac5d4863bdf | -3.85847 | -50.89475 | 2024-12-02 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94e42aa3-dae6-393e-a98d-f53b35a9b8eb | -3.74977 | -52.276 | 2024-12-02 04:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 446f787b-d5c2-39e7-a7e4-1f0268373ed1 | -6.08081 | -48.05177 | 2024-12-02 04:25:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fca80848-71c9-3d92-9f0e-1da8b110de23 | -3.90691 | -49.74355 | 2024-12-02 04:25:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README36.md)
