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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 675973b5-0b7d-3fc1-b330-4f2363a212f7 | -3.6649 | -50.7997 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 4fa79e87-71af-35c0-bbb4-2298e9e1c40f | -4.25626 | -48.63116 | 2025-11-09 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5df264fc-ce84-32bf-9614-d15781d4bc12 | -4.29052 | -50.65986 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| c51c551d-60cd-3197-9b77-7b3c39b635cf | -7.95216 | -46.8499 | 2025-11-09 00:34:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8ed07f92-71a8-38a8-b2c9-0a95070d4844 | -3.08172 | -52.92367 | 2025-11-09 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 8e23d46c-9955-395a-949b-09919487b6ca | -5.34898 | -49.59108 | 2025-11-09 00:34:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5156fc74-8078-3995-9356-6948556f3b71 | -2.93831 | -49.34964 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| f36fb9f8-272a-30a7-81cd-60f35a4b3c80 | -3.4065 | -50.26424 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 95bceb3d-9269-3dc5-800e-2debe3fcc74e | -6.88608 | -49.24271 | 2025-11-09 00:34:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 7648eb69-44a3-3e33-888a-840b8146f7d4 | -4.40073 | -49.65884 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 7f1498b9-e175-3ac3-825c-12d7a332b353 | -5.36772 | -44.62714 | 2025-11-09 00:34:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 59a79ea3-c45c-3a76-a4b9-427fe68e16fa | -2.74796 | -45.17721 | 2025-11-09 00:34:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 44.7 |
| b0dc0bb3-13dc-3578-81ed-eef54ed19c4e | -3.36653 | -49.51061 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| d121b0ca-2b44-3a9a-8847-55fcc41dd225 | -3.29586 | -50.19539 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8384a45f-525d-3f68-985a-10b2ba200925 | -2.94873 | -49.35772 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 5a9c19a8-e37c-3ea0-aa38-bcc8ccfd2254 | -3.64598 | -49.86653 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83d3dc9d-7924-3c49-8064-1d32ae9732e4 | -3.66847 | -51.75647 | 2025-11-09 00:34:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| abbc40f3-3c00-30ab-bdd3-207c5195e2ac | -3.73742 | -52.66026 | 2025-11-09 00:34:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| c34d1d3f-d612-32c6-8d6c-380f7c9df945 | -5.6588 | -45.99176 | 2025-11-09 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| a1bf6a5c-8f74-3e33-a9a3-5334518bc4dd | -3.46314 | -48.81916 | 2025-11-09 00:34:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 3eb6c948-1672-34e9-97e2-89c4ca9f3bfc | -7.17405 | -44.96465 | 2025-11-09 00:34:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 53bf0a87-c773-30f5-9ba1-130e4f8766b6 | -9.51624 | -47.26294 | 2025-11-09 00:34:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8e05340f-16a3-35aa-a7a0-c005315b5932 | -4.39073 | -45.96091 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e1607c35-5972-323e-bc0d-f3cbd07938be | -3.07073 | -49.37266 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 2b2c6cea-0e0a-383e-9345-064678dede9f | -1.59253 | -54.30818 | 2025-11-09 00:34:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 35185770-d121-319a-b3a7-b4810f22e3e8 | -2.87517 | -53.15349 | 2025-11-09 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 70497325-c867-3044-87d6-8b0245849c9e | -4.91267 | -44.65388 | 2025-11-09 00:34:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 26989c99-e556-35d1-91c4-fafe04893bee | -4.68425 | -45.69096 | 2025-11-09 00:34:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 99e00f37-1d6a-3802-b2ba-1033e4f96d8a | -3.41485 | -52.18988 | 2025-11-09 00:34:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7feab51f-aeea-311c-8805-e021b403c86b | -3.32268 | -44.35759 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2c29cdba-ebb8-35de-a4ce-9a6d02a067cf | -4.39798 | -49.76925 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 42593318-0b39-35d6-87f8-ee708f987f80 | -3.61687 | -49.32492 | 2025-11-09 00:34:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 806ca609-8f2d-3aab-8975-905e72799158 | -4.52484 | -48.83992 | 2025-11-09 00:34:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 93890a74-da34-301d-95c2-20c889bac6cc | -3.32216 | -50.11315 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c652aa88-d4de-3962-887a-186086f62bd7 | -3.83199 | -51.13248 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |
| 40b0c6c1-7b2c-39a0-b388-23a1267d304a | -4.11651 | -47.2921 | 2025-11-09 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 71322179-36fb-3b46-8fab-0320442dbcc5 | -4.39923 | -49.77819 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f91f383c-d5f6-392b-8815-d2a1a0ad4ce8 | -6.87387 | -47.24171 | 2025-11-09 00:34:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f5fb3742-1df0-30d4-906c-1b0d85d946a0 | -8.44792 | -48.1037 | 2025-11-09 00:34:00 | TERRA_M-M | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 72525e04-9530-37a3-9983-e566d881b2f4 | -4.58422 | -45.63604 | 2025-11-09 00:34:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 123c77f4-c233-306e-a19f-e05333a13b39 | -3.45016 | -49.97953 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 2d3fd472-1d3d-3048-9be0-fef881ee8c29 | -3.08113 | -49.38073 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e6889bef-3581-3b7b-8812-75fc6dda05f4 | -3.48122 | -46.11736 | 2025-11-09 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 661aba28-719a-3d03-be66-a6263565f631 | -3.32202 | -49.12637 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 69e87dbc-e118-362b-9481-1629b5196688 | -4.29174 | -50.66866 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b37049bd-073d-3157-a459-94d44711f772 | -3.77307 | -44.30038 | 2025-11-09 00:34:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 0895d8d6-c9a5-3998-978f-3f0d85801664 | -4.56661 | -45.43376 | 2025-11-09 00:34:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 84eeefb7-4a17-3bf1-a482-3efcb95deb6a | -4.18434 | -45.7336 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6d3323d7-c734-3a96-b635-2bd31ef21313 | -3.32664 | -44.38379 | 2025-11-09 00:34:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| f14d1a41-fd99-3e2b-b1a5-9bc5f3db323d | -3.86187 | -51.21862 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5693b50d-929c-35d7-bb3d-7ba2ea781618 | -4.6348 | -46.39605 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 102.3 |
| fcf2497a-8296-3150-9707-27dac6fb0ba8 | -2.51808 | -49.43999 | 2025-11-09 00:34:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8f7026a-6637-3b79-91e1-6f22b9cb8c02 | -3.42642 | -52.89178 | 2025-11-09 00:34:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 26abac1e-5a7e-3245-a651-f518683180d8 | -3.45906 | -49.97827 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.8 |
| adbe26e1-532a-31dd-81a5-72f9b0978a8b | -2.5981 | -49.21981 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 3bf3ed1f-4a2f-3053-a9c2-4b97c34b4a5a | -2.83168 | -48.98204 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1899d0cb-2975-3206-93ed-2e0ce552dfcc | -4.80133 | -46.02021 | 2025-11-09 00:34:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5a7e348c-a669-3aa7-81e4-576a05bc5621 | -3.36399 | -51.28862 | 2025-11-09 00:34:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0fdc3a5-e161-3ace-b2a7-b1302a027f98 | -2.48665 | -54.19358 | 2025-11-09 00:34:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 241138c6-3b45-3191-8500-8c2c6702617c | -4.11609 | -47.28664 | 2025-11-09 00:34:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7f9ac7fb-c4f5-32fc-971d-bc969e2d8349 | -4.41287 | -45.95751 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 5b4d32c2-df30-387f-a79c-c8cd4f5f2c92 | -3.10297 | -50.19855 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 0a871eff-c566-39df-a666-a3f23edfd650 | -3.75173 | -46.00027 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 3b7f228b-927f-3e54-bd80-3d9da391227e | -3.46451 | -48.8289 | 2025-11-09 00:34:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 154c0fba-5619-3909-b325-45c6996ff7f7 | -4.70331 | -46.46022 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 09808333-8c0e-3995-9392-b42c955c2f51 | -4.39289 | -45.97538 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.7 |
| c3baf610-fc53-327c-9e9d-16fe2b92d4c0 | -3.26078 | -50.07325 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| ad85cdb4-6288-345f-8515-e7bc344bc013 | -3.45782 | -49.96931 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f2e731a4-5070-3170-81c9-8411a587268b | -3.14932 | -50.59762 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f71f50e4-45c3-324e-bb39-30efce01a19e | -6.0445 | -57.96685 | 2025-11-09 00:34:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d2a42491-748b-3d65-9c64-9b65e3af207e | -8.01209 | -46.98726 | 2025-11-09 00:34:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2e24c8f-9fd4-3206-b7b7-cacc02c24aec | -2.61779 | -49.22677 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d1bce931-2734-399c-8eba-ed62944ea8f9 | -4.4577 | -44.65503 | 2025-11-09 00:34:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 126b608f-c8eb-3f83-ac7b-8b4f2a4eca81 | -4.40182 | -45.95935 | 2025-11-09 00:34:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 5f8e654f-d7cb-3a5b-b232-9d5b1e6acfc6 | -3.13506 | -49.1069 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 9166ab4b-1f86-3dbe-84e6-814f65a721be | -3.09535 | -49.67972 | 2025-11-09 00:34:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3efa4b27-a525-33fe-9d16-8f6be6187c34 | -7.54874 | -45.84999 | 2025-11-09 00:34:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 1812208d-1d15-3d9e-9dff-4372364e115d | -3.12468 | -50.15919 | 2025-11-09 00:34:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4b8cd5c6-bc5e-303c-9377-4818295058c5 | -3.48146 | -46.11158 | 2025-11-09 00:34:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0204c2db-e286-3d60-82db-d79c927fff0e | -4.14783 | -46.25805 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0cbd9036-d311-3bac-8d37-b042be8c7cc9 | -5.65682 | -45.97809 | 2025-11-09 00:34:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b4910e4c-f27f-398d-871b-541d48762102 | -4.32798 | -45.6909 | 2025-11-09 00:34:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| c4da0719-f5ba-3697-b127-5c0e4ff63f4c | -2.60728 | -49.21853 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5c4b42ba-6a23-3b8e-bf38-11ca6efcff7f | -4.71393 | -46.45876 | 2025-11-09 00:34:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 2d254ab4-340a-3119-8552-2e9d9e48ddad | -4.45474 | -44.66205 | 2025-11-09 00:34:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 88fdb289-fb61-385a-8633-368c47a95d28 | -3.79678 | -48.90511 | 2025-11-09 00:34:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| e75136ed-a8d6-34aa-9b55-1ab9dfadf324 | -6.87195 | -47.24844 | 2025-11-09 00:34:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| be2444c4-fdf1-3518-b7bd-9cf8ca8ec9bd | -2.60861 | -49.22807 | 2025-11-09 00:34:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f96352ce-7b90-3a33-9cc9-ac0e19a87858 | -9.37816 | -47.08013 | 2025-11-09 00:34:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d2792b01-b6f1-3235-b9bb-a53302cc0d0e | -5.25702 | -47.1823 | 2025-11-09 00:34:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2bd0602c-96fb-3370-94f2-c398a570bfa4 | -4.21618 | -50.65873 | 2025-11-09 00:34:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f1d47252-3193-3cd1-920f-9b38117a1e02 | -7.87804 | -42.01072 | 2025-11-09 00:34:00 | TERRA_M-M | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 8fa5c08f-7d23-37e8-accc-eb485e34db45 | -3.3207 | -50.3094 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9cf17b2a-4a14-3aaf-a347-fae2ac5faed0 | -7.49571 | -46.60123 | 2025-11-09 00:34:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8faa7149-6e96-39bc-baab-3fa4583ceb90 | -4.75321 | -47.52229 | 2025-11-09 00:34:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3cc8bb3e-3dcb-39f9-a5f8-fd87c9258576 | -3.80942 | -46.00017 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 81389431-59b4-3a48-b6e4-9645f372c91c | -3.66113 | -50.23705 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 67db8733-2892-3474-b64f-583259ddbaf6 | -3.75147 | -45.99382 | 2025-11-09 00:34:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 34.0 |
| ad2d4db4-eea9-3e7c-94ee-4fe06f400094 | -3.84157 | -50.74478 | 2025-11-09 00:34:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5f823e2e-f800-3813-9e75-90d9d3681498 | 0.77567 | -51.33563 | 2025-11-09 00:37:00 | TERRA_M-M | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |


[Clique aqui para ver as próximas entradas](README6.md)
