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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f311452-61c4-3d4b-8856-b3b62241c848 | -3.90323 | -46.66848 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 387479c6-1532-3c47-ba84-c4ce10b15d53 | -3.25289 | -50.61492 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26dca037-727b-3152-b664-8b03c12b2585 | -3.25695 | -53.6241 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6b8a43d-571e-3213-b412-7925ecc0811f | -0.25673 | -51.5003 | 2024-12-04 04:10:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 777e1466-6c5e-3242-890a-76630d3214b1 | -2.63128 | -48.06472 | 2024-12-04 04:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6e2bfae-40f4-3abf-adca-49dced39bc00 | -3.10798 | -54.6796 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9193e01d-bd09-3370-9826-894e6d799694 | -3.37674 | -52.79223 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df416683-df62-39a3-8f14-808a8b4d9190 | -3.1889 | -54.51699 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0123754c-51bf-3d6d-9ea8-55e22b797d96 | -3.93138 | -46.89322 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d20fcd7-21c0-3a6d-8cbe-1d2a891d42ee | -3.72919 | -50.05797 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed372cc7-c85c-36bc-9f14-79d98ca9f048 | -1.2265 | -49.15289 | 2024-12-04 04:10:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc3675fd-8573-32f7-8c83-a637f230ee02 | -3.24853 | -46.2838 | 2024-12-04 04:10:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd5eba11-d3ac-343e-910f-5d23e469ae0c | -1.48028 | -53.81143 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 992869b5-a36f-38e6-ac06-8e307c464931 | -2.65522 | -46.5795 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad43d045-1224-39c1-a7c4-07067641dd5b | -3.98874 | -46.66577 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b34126f-77e0-3b24-b41e-b57edc916f70 | -3.26374 | -53.62418 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c753d015-97f1-39ca-9457-bdf59b9f5808 | -1.7539 | -52.63335 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8eb3b0cc-9033-3dd6-8ecf-c8e68a3f0bf1 | -1.8148 | -46.30882 | 2024-12-04 04:10:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a456ef15-74fd-3a80-a462-ed04ad652fd2 | -3.48921 | -51.56235 | 2024-12-04 04:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0038d1f1-8b6c-3b72-a1a4-3ac174848efd | -2.82211 | -53.05727 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80e8f91b-5222-318b-a222-d4b90276a8c2 | -3.89403 | -46.67664 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3097e80-183f-3aab-b05a-aff70ce5a61e | -2.80871 | -53.06407 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 559c70d0-7d16-337e-a949-dc43893776b6 | -3.58473 | -50.53556 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28063659-7847-32d2-985d-70d6ba621932 | -3.07094 | -54.06744 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ba29288-0aca-30a9-b3e7-b6a4224ee309 | -1.71005 | -46.21143 | 2024-12-04 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 514d96ad-531c-3153-a5ad-aacaeacd111a | -3.85035 | -46.51864 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f0c4438-79a8-3bd2-80e7-2f0ca100c0a6 | -3.20695 | -50.65046 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 471d4113-ee99-3de0-9b4a-b118190ed7ca | -3.34189 | -51.21031 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 913cd985-a50a-3303-b920-7dce8432bbad | -3.62552 | -52.03866 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d82fb51-3e55-320d-aadb-f727d77dbfee | -1.50943 | -46.7646 | 2024-12-04 04:10:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46744a0e-9341-3f6d-9b61-1117adbe5ad9 | -3.71773 | -51.0904 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45ba8230-785f-35c9-a2d3-9733e88600de | -3.20187 | -50.64968 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f46461d8-7d99-3e49-9433-6f124b7995ee | -3.47807 | -50.24473 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aa92adaf-a590-3d9c-97ba-59edebab429e | -3.26973 | -53.66035 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7bee845b-0e4d-3a7d-873d-c99d36d62ce5 | -3.25746 | -53.66227 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31091f5d-d23f-3591-af7e-2f1cf4219c19 | -3.09151 | -46.61358 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d8558ee-a5ed-3368-93d5-bcacf9bbe970 | -2.1956 | -47.24382 | 2024-12-04 04:10:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cdecc04e-25b5-3856-b626-fdec334bbed7 | -5.6224 | -44.84239 | 2024-12-04 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 601d8c0f-2851-39e6-9528-b2b1ed6b8ee6 | -3.2513 | -53.66119 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5b29ec9-e748-3dab-b91f-ea47e24781ea | -2.82561 | -54.14977 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34ee3184-4588-366c-bb3f-ea1d7f2b7c39 | -3.87339 | -48.36282 | 2024-12-04 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f2221cc-b959-3e8f-9b38-6a2cf01bb682 | -3.80585 | -46.94535 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7a5d0202-7131-341e-8030-71216e13fa11 | -2.91316 | -52.21143 | 2024-12-04 04:10:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 564efdb6-771e-3672-9931-86e3be1aeefd | -2.89882 | -51.81887 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0aeac565-10a7-328b-86ce-d442d98a0a4c | -3.26845 | -53.63089 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 69a0effc-7930-3e07-842c-1521a665669f | -4.98735 | -40.90478 | 2024-12-04 04:10:00 | NOAA-20 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e98944a9-4b24-316c-bf80-013fbc571a10 | -2.89558 | -48.0602 | 2024-12-04 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 003182b1-4d65-337b-a601-6ceb5bbb83a2 | -0.96345 | -46.84342 | 2024-12-04 04:10:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9997ab4a-156c-38aa-804b-44ae859d3dbc | -1.55699 | -53.79459 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7dbd63d6-4fa3-3d23-89a4-bd4fc6f5e237 | -3.10236 | -54.6729 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d014f70b-bad3-312b-ae84-ac7369ddb719 | -1.48112 | -53.80625 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f470b3ca-e69f-3ce8-b83a-7f10c04ffc85 | -4.19178 | -50.68435 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 744e6993-dad5-32c4-b950-c1c13a5e37d9 | -4.39995 | -46.01117 | 2024-12-04 04:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67737479-a761-3fa5-a617-818af41f7378 | -1.7612 | -52.62579 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| a52b2508-81ff-3b3d-a36f-8d94f7f7dcd6 | -2.8989 | -51.81829 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8eee8750-19ba-3c7f-847c-31908effc0a7 | -2.47222 | -46.54801 | 2024-12-04 04:10:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 715a12fd-e583-3803-ac60-b944c0c90ece | -2.62364 | -45.73632 | 2024-12-04 04:10:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 03df305c-1afb-30c7-84a6-0d65f8507d99 | -3.77217 | -52.21218 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d40014fa-b3dd-34aa-8f54-99c8ec1c846d | -2.61133 | -46.27153 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a29b0b17-ca57-35eb-8f93-85ab2a972e12 | -4.09645 | -46.6468 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c06145e-b46f-38fa-a990-744740cecead | -1.61922 | -53.53383 | 2024-12-04 04:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61a45393-15b5-3f9b-825c-f4bbfa92d56d | -2.80273 | -53.06306 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff584c80-205f-3446-bd7d-c23106efe0d4 | -2.9043 | -51.81994 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 657d5420-d272-3b4f-9e40-8adff190cef0 | -1.05233 | -46.59055 | 2024-12-04 04:10:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8018fa71-d3a5-3726-be99-a9e49cbaa8ac | -2.56314 | -46.57754 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7cab39e3-6d87-3fc1-b537-33a9838a0a0c | -2.79811 | -54.14864 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30154c51-7d7d-3832-a1c3-67c581f0de9b | -3.20089 | -50.64584 | 2024-12-04 04:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d280280a-c9d7-36f8-9ed7-2879b627d16b | -5.12254 | -43.20254 | 2024-12-04 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4746b6e9-7f1f-314d-b4ba-05704683bdf9 | -2.82465 | -54.15534 | 2024-12-04 04:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b8839433-fb64-37fc-8658-4cdd3b470deb | -3.80817 | -46.95597 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a51460f-7861-35dc-9cd5-39f4c5ccfb5c | -3.10603 | -54.69092 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a815066f-ea22-3a38-ad4f-1c2e95cc46c5 | -2.61964 | -46.95788 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4565ad8b-1d67-3c31-8deb-ae3606cf06f8 | -3.18217 | -54.52039 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feb53e04-16df-3cef-8e8a-e1d7c06fa8de | -3.71652 | -51.80195 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eea6d37d-b8ac-33cc-a5f3-ed72646ee923 | -3.82687 | -46.61602 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 322facb8-764b-392b-b5bc-9ee7a8a121fe | -3.734 | -50.05886 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c860210-ead2-3241-9e04-36bff9d55d97 | -3.93089 | -46.89063 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4074aeec-9f04-3297-b30f-dafd8fd7f954 | -3.85031 | -40.98508 | 2024-12-04 04:10:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fda5bffd-2253-3338-8f07-a638fba5773d | -2.81861 | -53.05654 | 2024-12-04 04:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc8c005f-a33d-33ea-b543-4944e5e3f979 | -3.86031 | -46.5296 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f474152b-f979-3d9a-a94a-5e6a64c1b853 | -3.57559 | -50.30753 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 673c828e-07d6-3150-9b9a-fe506a307424 | -3.70152 | -51.82454 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6bf67e4f-6a6b-346e-bca9-6617d183492a | -2.5946 | -46.27844 | 2024-12-04 04:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bca0e7af-3239-3cd6-af05-597df1d68c24 | -1.73758 | -52.6218 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9ef30ff5-ab69-32cd-a610-1cdda898f695 | -3.37239 | -51.06203 | 2024-12-04 04:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e707cfa1-0675-3cc4-8acc-b3d7d07988d6 | -1.73828 | -52.61752 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 25ea1eb8-b73e-38c1-8793-6279cfb7a7c2 | -3.81438 | -51.66359 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 35da68b7-b7e8-37a7-8b00-c59f2dee3e64 | -3.96757 | -46.65965 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea226dc5-5d2b-33d0-97ea-2e91cf20328c | -3.44201 | -54.09126 | 2024-12-04 04:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11d3981f-de69-31a8-9c1f-a629d3dd8e08 | -3.8096 | -51.65924 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a7bb55d-85ac-31c2-9fec-9343ce438995 | -1.83607 | -52.31271 | 2024-12-04 04:10:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9db006d4-d1a2-3b75-b63b-539aaac6f8f7 | -5.37977 | -42.88595 | 2024-12-04 04:10:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6073f324-6ab4-33dc-8e7b-e740ec38b19d | -2.97728 | -46.94984 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3091231-ace2-388c-ba7b-8d7478bf54ee | -4.32581 | -45.81715 | 2024-12-04 04:10:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18d7b629-b63e-34fa-94ad-52660298fc86 | -4.05099 | -46.81781 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b24e05eb-1092-318d-bca2-bd5893b56bba | -3.10509 | -54.69644 | 2024-12-04 04:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd579b09-1555-361e-8c5d-38e4640aa437 | -4.04155 | -47.00396 | 2024-12-04 04:10:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6201614-bb83-3149-bcce-a18a843d2ab3 | -3.89782 | -52.17115 | 2024-12-04 04:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7390218-f05c-3660-aa73-ed5aebee2958 | -3.81698 | -46.67739 | 2024-12-04 04:10:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8d9b477-6f67-34ac-aa93-efb8742d35d5 | -2.56822 | -46.57539 | 2024-12-04 04:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README25.md)
