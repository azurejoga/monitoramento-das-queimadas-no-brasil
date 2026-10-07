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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a67b67af-f4cd-36a8-b2ec-294e5c2b3657 | 1.76885 | -55.56252 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a17ff7fc-d529-386c-81d6-d7fc4d4d1c3c | 1.73144 | -55.60166 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69fb46bc-01f9-3f6b-ae5d-663bd149ed2b | 1.70231 | -55.63535 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e064f00c-9730-38cb-9326-2a0bc33f9913 | 1.90361 | -55.7071 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 042af00c-90f8-3d2c-95a2-919124c30813 | 1.64302 | -55.79856 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 566b7cca-0f85-3d2a-85c9-9243fc0936c9 | 1.76995 | -55.56964 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 340c1f5f-a786-3a2c-86d4-8b2669ed25cc | 1.52607 | -56.0131 | 2026-10-07 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97d3ae46-61ea-3529-ae0a-45c4220900db | 4.28014 | -60.14872 | 2026-10-07 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| adca3c13-ced5-38cf-b289-e750bbc497db | 1.76605 | -55.56659 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0c9d38c-3e2f-34f1-823e-14ad6ec36082 | 3.21303 | -51.32443 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20945701-37a5-3423-9538-dd4fd0463015 | 2.56394 | -60.1818 | 2026-10-07 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7aedafde-8358-30cf-8173-fd9e0eee80e3 | 3.1512 | -60.59407 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b071c29d-053b-330b-b04b-aa902fbb8c83 | 2.43778 | -50.85086 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b417bdc-3a82-3d9e-b3d5-a017cb439926 | 2.1267 | -50.83189 | 2026-10-07 05:01:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2174fb72-5e03-3a47-bd7d-da7ece1a1f91 | 2.43353 | -50.84731 | 2026-10-07 05:01:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23646da5-b034-39c0-9e8c-80b0beeca161 | 3.98212 | -59.7293 | 2026-10-07 05:01:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fb15d15-3a35-3fa2-b2cb-164a1cebf3f7 | 1.82312 | -55.536 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa10d69a-0bbe-3f9e-9a4d-254bdfff8901 | 3.15409 | -60.59298 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a178668-0809-3625-beeb-9453cd5820dd | 3.14215 | -60.59541 | 2026-10-07 05:01:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd23260d-3aae-3da7-99d3-40115f46c58f | 1.7666 | -55.57016 | 2026-10-07 05:01:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3d5bc63-5f58-308c-9bf8-aee2de1961d8 | 3.52435 | -51.27338 | 2026-10-07 05:01:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc14a4f5-034e-3aea-aab3-9f098063b77b | 0.72352 | -51.38458 | 2026-10-07 05:01:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc7f714b-3791-34c6-8daf-a4b95174f691 | 2.75356 | -60.00231 | 2026-10-07 05:01:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 847b36e6-4e7f-32bd-bd9d-8e6a0afd2c7a | 1.5255 | -56.00945 | 2026-10-07 05:01:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e086c9f7-b197-3f90-925c-6ec25a118eee | -3.51342 | -54.63858 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a9439dc-8b73-32a9-99bd-9a1b3c6e1a49 | -3.27653 | -50.1437 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| affcb3d3-f55f-314f-9212-351c661ebdb1 | -3.6926 | -55.95565 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4dde9e7f-26d1-383a-b155-9882e3794f7b | -3.52119 | -54.65397 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 93ffe433-84c5-35e7-ac83-998a18321a0b | -1.50679 | -54.82817 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6dff8ac-93f6-30af-b166-176f17f71216 | -3.24228 | -56.80616 | 2026-10-07 05:04:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7cac8f1c-322a-3532-bb8c-a8a4de60277e | -2.44102 | -58.01789 | 2026-10-07 05:04:00 | NOAA-21 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2976fe8-c3c7-301e-ab3b-3ccde4d7af0e | -3.32897 | -58.15806 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6e6d3c6-0720-32d5-8b8b-35545ff92198 | -3.59964 | -54.56649 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7cbfc301-a9d1-3d89-9677-70a5c3f1ba78 | -2.91955 | -54.10393 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86370be5-c974-37e7-9bfb-5cf51962b886 | -3.74637 | -59.44646 | 2026-10-07 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0133ac7-f44f-314d-82a2-b40d9ed5c5bf | -3.98039 | -51.93781 | 2026-10-07 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0048aaf1-fc6d-3bf7-8c94-9c9585e384a7 | -3.08073 | -54.18242 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f60411ff-4b88-3eb2-a2e6-8947f77b346a | -3.05389 | -53.94014 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54d57545-0694-3020-9977-da0a6858e532 | -1.08992 | -54.11944 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95df53d7-5ace-33d3-8485-83fd62098da2 | -3.07486 | -54.24246 | 2026-10-07 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe71227-22b7-3069-847b-f02fbe3cee68 | -1.51009 | -54.82868 | 2026-10-07 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ded79754-d9ee-359c-b86c-ae852d92701e | -3.2715 | -50.42286 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04d5a985-6efa-3edb-af6b-58e2badf94ac | -3.67652 | -54.18072 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96f7ff8b-7a6c-3a1a-991e-13f2a283dbf7 | -3.27886 | -54.02572 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 33a7b1c3-d970-3671-ad76-8c96f67b9909 | -3.24778 | -53.87177 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a2423ca5-705a-3e1a-ae83-e22977a9200c | -2.87854 | -54.12636 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d005fffb-3ade-314f-8e6b-ae80a167c5dd | -2.98216 | -54.13849 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f53442ff-91d4-31d2-92c9-cc5b85ac88d1 | -2.03802 | -54.30223 | 2026-10-07 05:04:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3cde873-44f1-3225-8dab-9cc9455d46e1 | -3.00359 | -54.2422 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3de6fca4-8b37-3b12-b5ad-d38e8204e34a | -2.99184 | -54.05359 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9a8fbb4-a706-34ba-a753-2e3bca4cbb7b | -3.59247 | -54.56893 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b39ab036-2c46-3670-b879-6949b40ec7b7 | -3.29605 | -54.06439 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| def644ac-7db2-3bfb-b51f-1ddd9e2103c8 | -6.00846 | -53.50177 | 2026-10-07 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7ddeff0-d449-3315-b89a-f906ba924b77 | -3.49856 | -54.64691 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f5927ed-ef82-381e-ac55-8c173d4148b5 | -3.02112 | -54.17324 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0f9d383-fe54-3f79-95c1-a6641e568989 | -3.1765 | -58.63814 | 2026-10-07 05:04:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ddb6e388-30a3-3884-8d79-698006da6bed | -4.77411 | -50.81159 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de9504a2-4768-37ab-855a-1f7886400f67 | -1.44665 | -52.68967 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ff3ea71-dbf2-39ee-a4e6-6f3dcf808709 | -2.80677 | -52.08919 | 2026-10-07 05:04:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63b60cca-5436-3be7-b5dc-16e61752decc | -3.09775 | -53.74612 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95ac1af3-6d6f-33a7-8133-5cbdeffb5fa1 | -3.28555 | -54.02674 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bfdb3390-8ad2-3533-8e95-22f42c6137ec | -0.04788 | -53.24971 | 2026-10-07 05:04:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f788e1d-cf76-3660-9dac-f6f7fcd5892e | -4.29116 | -54.80197 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be949716-8cbc-30f6-b64b-1e86997dadf1 | -3.03033 | -53.89288 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 356886f3-4e0e-3422-a1a4-5041bd9253db | -3.28779 | -54.03433 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| a1c08bc8-e100-3d44-bb7b-42219a97b4ad | -3.50626 | -54.64101 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e1ce8d5-1b8c-3014-b676-7e421ab27ce7 | -3.04099 | -53.9127 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cb6a49a-f57d-32d8-b17b-50b68d20183a | -1.2046 | -55.69631 | 2026-10-07 05:04:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 586407dc-6520-348a-bef4-0e67bab438b6 | -2.92591 | -54.1946 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c3182ca-8819-3bf4-a767-b035ecb22903 | -3.05109 | -53.93607 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e75148c-fd0d-33e4-82cf-b8a7af2f443a | -3.83646 | -55.97077 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8c79728-b27b-30b3-916d-10ca7b38fec0 | -3.50349 | -54.63704 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e82241d-bc7a-3a63-951b-fea5d6a778d5 | -2.94792 | -54.11905 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 387fc906-5327-3f5f-9a9f-90274f33482f | -3.68214 | -55.95756 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c1d8d76-9ade-350c-9bdf-5d78a71dd589 | -6.94061 | -43.6779 | 2026-10-07 05:04:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7954659d-814d-3c66-96e8-fb62de0f523d | -2.87816 | -54.17291 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10f63d1b-0a0a-3274-97cc-bc78a1812bc8 | -2.77957 | -54.10704 | 2026-10-07 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ab24e70-c133-3c9c-a857-9a51991e0b1f | -3.17171 | -57.54345 | 2026-10-07 05:04:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c3baf8e-90fd-3743-a2d5-210e06b2a500 | -2.99627 | -54.04706 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fd6371d-7f5b-339a-a9a3-35b20ed0f5d2 | -3.51656 | -56.89689 | 2026-10-07 05:04:00 | NOAA-21 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d43efa59-bc69-32e3-b465-8a54759d52ac | -2.75184 | -57.66004 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 255a559b-6375-30ca-8f5d-56f305b19e1b | -3.09897 | -51.37855 | 2026-10-07 05:04:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a53f47f0-7b3f-3ffd-8f20-f6831af57009 | -3.10392 | -53.75075 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95a92cd6-3596-3c89-8fc2-fa8578ef6b61 | -3.72905 | -55.98247 | 2026-10-07 05:04:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86e57690-746e-332f-a833-31dd08e4d402 | -8.70155 | -45.20906 | 2026-10-07 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 6f56eeaf-5dc6-3350-91ab-e229241229fd | -3.28385 | -54.01561 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 810aced8-d1b2-325f-955a-a8a37be80338 | -3.10506 | -53.76559 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 38916105-ce8b-3107-a98b-77715c30baad | -3.18314 | -50.55648 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c977c734-a957-3ae9-b44f-41fd57368dd2 | -3.72833 | -54.21745 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 265b1540-d302-3857-8eba-704e57405135 | -3.52342 | -54.6614 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ac240112-f12b-3723-98b9-207db418d6a4 | -3.27254 | -50.41601 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 391a565d-3be5-3ac3-b8d2-c734ce507dea | -3.29117 | -54.05658 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ae879681-7e61-3597-962b-e3bcb81be836 | -6.40586 | -52.71196 | 2026-10-07 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 658049f8-519b-3a68-9c43-210655b9a767 | -2.95872 | -51.05133 | 2026-10-07 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f53aac2-693e-39c9-ba9b-c574062768b7 | -4.32187 | -50.78026 | 2026-10-07 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcf8b514-78a4-3370-8a86-60aaceec1c10 | -4.26827 | -54.86227 | 2026-10-07 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 863fae94-aed9-3213-be42-22c5fef05417 | -3.09731 | -54.16338 | 2026-10-07 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 731f6b65-b760-3ab0-be2f-fd5cdc9154f1 | -2.71935 | -57.47076 | 2026-10-07 05:04:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa453a30-eaa9-352b-89b8-70b810e223eb | -3.59023 | -54.56148 | 2026-10-07 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 330405e6-3853-3898-925c-13ed8b337610 | -3.10617 | -53.75843 | 2026-10-07 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README66.md)
