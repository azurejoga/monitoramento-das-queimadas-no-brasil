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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33ca6b5f-c793-3435-9e42-368e9b4acff5 | -1.95534 | -48.56406 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a077da3-1925-3147-be15-b109136447b1 | -2.56112 | -48.94563 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b0317029-3870-382b-9cb9-4406e47954d3 | -3.91995 | -53.66257 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 705be662-7bcc-3c9e-b84a-f4a1c3434830 | -1.58292 | -52.28325 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 6c862059-ea4b-30f7-a8c5-6266e11c5be4 | -3.89503 | -46.49537 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a6de859a-f41b-3141-bb38-592395473249 | -3.18494 | -54.33087 | 2024-11-29 00:52:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| b031e0ff-e498-385e-a227-7cef24d878ea | -2.62062 | -51.81284 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f6a6ef42-b4d5-33e1-9bb8-42097e73044a | -1.53254 | -51.62891 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 895acbe3-1cc4-33db-9a63-5d22da9c8fad | 1.32412 | -50.67697 | 2024-11-29 00:52:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9bceb1b3-5afe-3266-9e5e-05fa92a84339 | -1.96339 | -46.44093 | 2024-11-29 00:52:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| d8125d93-6dc4-3925-a8e7-2c19270ffc1e | -1.36021 | -54.6605 | 2024-11-29 00:52:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| e95bd8a8-fa7a-3c08-b196-51d417f60a07 | -2.01529 | -51.19739 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 657ebf41-dc71-3dcf-94ff-a574e3205703 | -2.7753 | -48.56432 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 161878a2-4035-34d7-9247-a9db55ac7879 | -3.22391 | -46.30703 | 2024-11-29 00:52:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 326adf4f-9789-347e-983a-34bbdb753a04 | -4.11949 | -48.48997 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 96b4aa1d-eb99-344f-97be-9fc80d529b15 | -1.62568 | -52.38336 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| de6022e8-5a48-39d3-bfa2-13a342b66060 | -1.95412 | -48.55526 | 2024-11-29 00:52:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cdac5e2c-3338-394d-901f-8da44478e459 | -4.25331 | -48.06265 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9485f21e-5717-3b38-9676-6be29f087db9 | -2.64741 | -48.77435 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c88838ae-5537-3f88-8b51-f78d9c36d67a | -3.73831 | -51.83944 | 2024-11-29 00:52:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| a3c6509f-19b7-349b-b9cf-e523969fdcb5 | -2.6077 | -46.843 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 78c72f7a-539c-3193-b4f6-ec16acd54073 | -1.52003 | -52.20644 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| acf5b1d5-cf5a-3ea1-b618-e9a7a9479622 | -3.30207 | -50.76388 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| fd449da1-414c-38ce-979f-593b673a7fa6 | -5.17266 | -46.16061 | 2024-11-29 00:52:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c04c74bc-aa20-3204-a817-01c511fb2168 | -2.26652 | -53.46577 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| c07c7e51-884f-3dfe-8f91-5de5977eb3e7 | -3.18496 | -45.65633 | 2024-11-29 00:52:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| c921229e-122b-31d5-be2e-66104d287fa5 | -3.98279 | -46.98974 | 2024-11-29 00:52:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b177921a-3ae8-3970-9029-a2dc349f9362 | -3.73649 | -50.78917 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b1685a01-d361-386c-bb27-bc5089a1abc1 | -1.21277 | -53.56186 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 522f3b02-98e5-3dad-aad3-d2437f52714d | -3.96901 | -47.94133 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 1e622e66-b841-3aff-a546-7a957c3a718f | -4.08955 | -48.48242 | 2024-11-29 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d40ee0c5-f29f-3cc8-bdf1-21456380d979 | -4.25454 | -48.07147 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f3d068cf-b63c-3b38-a672-89f1e4ab386c | -2.56578 | -46.41357 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 887fe174-a173-3208-9ad5-67962691adb3 | -1.50333 | -48.02981 | 2024-11-29 00:52:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a344b03c-93c7-3345-9889-6fa0dc9b18b2 | -2.44247 | -50.42324 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e9212d25-145b-3bdf-af24-4f34343de738 | -4.34849 | -45.86081 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d86a8db1-a333-3356-a9d2-9280a45eb331 | -2.65873 | -48.79076 | 2024-11-29 00:52:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 347.8 |
| 1a7bca67-0dba-3495-bb6d-28330230cdc2 | -3.2649 | -49.90261 | 2024-11-29 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| afd9303b-b1a6-3fe1-9466-40d19d0c1c18 | -1.68613 | -52.43788 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a39da818-b918-3581-8421-f9f731da999b | -3.26634 | -45.37172 | 2024-11-29 00:52:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b9cb02f4-2ae4-382e-9938-a816c6039145 | -0.95162 | -51.65252 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| decbf9c9-005c-34d8-925e-75d8906f0be8 | -4.07427 | -50.03683 | 2024-11-29 00:52:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 2eea7369-8f09-3787-ba1c-3124ed6e4b12 | -2.8966 | -51.37024 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a84f24b5-7e91-35f6-948e-f424bd004f6f | -2.62022 | -46.21605 | 2024-11-29 00:52:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6be5ad3a-e4af-3db8-bc09-d0e965f7216f | -2.83855 | -54.11192 | 2024-11-29 00:52:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| a2793dc6-49ae-3321-937a-4e587a69bb9c | -5.76025 | -46.27248 | 2024-11-29 00:52:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 47c5c1f6-cb64-3ba7-8bc6-44963aaba9bd | -4.20147 | -50.68399 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8bf5c09b-17c5-369b-b3c1-da09bea4d0f0 | -2.63969 | -49.90877 | 2024-11-29 00:52:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79dc0a86-4ab2-375f-a2b4-c7c82c871014 | -1.16598 | -51.93713 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bb40388e-0d08-3518-bcac-b1679a25ae88 | -2.54441 | -47.96991 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5dfccfc7-7993-35b2-8b63-6d9661545361 | -1.34695 | -52.13438 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ada7a2e3-4dd6-3c3b-a18b-e3ef180f6093 | -4.34057 | -47.5747 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 78836f67-4d80-3adf-a029-e98d3be41c4b | -1.24698 | -51.63105 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 780f741c-2132-35b6-9bfc-7fafbccae17e | -2.73726 | -54.1315 | 2024-11-29 00:52:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a91365ef-9980-309a-a899-fd6a61bac44a | -4.92363 | -44.52579 | 2024-11-29 00:52:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| dc610b53-4348-3ef3-b830-3fefe68e3d3d | -3.61765 | -49.85785 | 2024-11-29 00:52:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b46c027f-6864-3318-bc38-f965d6a2e5ab | -3.01934 | -47.80247 | 2024-11-29 00:52:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21350bdd-907e-3865-ad33-b16cb53524b3 | -3.62959 | -51.42501 | 2024-11-29 00:52:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6c862961-48ce-3434-b53c-2d22b51b9e87 | -3.98257 | -46.72841 | 2024-11-29 00:52:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 79165650-037f-358d-aa8d-05f6c75031c0 | -3.28213 | -50.16229 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 79b08b6f-4cce-3e6b-a7a9-6174be92821d | -1.0947 | -53.37847 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 83c8c83f-81a0-3c27-93c7-a8e5a62b6a5e | -1.78823 | -52.74199 | 2024-11-29 00:52:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| ce2bc1ab-cc6d-3b78-9a69-3ba2ff1b4f82 | -1.24187 | -53.36009 | 2024-11-29 00:52:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 01994518-5b3a-3684-ba0a-532e70188efe | -3.34652 | -50.23627 | 2024-11-29 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| be5acb97-dfe6-35d0-b708-d2aa021d1f97 | -1.15373 | -51.69494 | 2024-11-29 00:52:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b5d87b28-466b-3403-8827-91be052d3228 | -3.25463 | -53.63346 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 75fbd6d2-15b0-3a62-9527-33394e50dc24 | -3.25293 | -50.41124 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2493513d-488a-3c6b-b9db-a0b6d3ac1397 | -2.55874 | -48.20263 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5506495b-0025-3db4-8b1b-4dcc46b56fc5 | -3.50432 | -53.79887 | 2024-11-29 00:52:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 07eea4fd-0dfb-36b5-b6d4-60e9f2406ddc | -3.96217 | -48.08642 | 2024-11-29 00:52:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 582f4f44-ccd2-3d1a-b92a-89b08b1af34b | -3.035 | -48.50911 | 2024-11-29 00:52:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 95736f43-298f-3e33-abf6-96a3ef20eb3b | -4.78907 | -46.12193 | 2024-11-29 00:52:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 4b5e450f-4324-3c03-ab16-2fa1a813a507 | -3.28076 | -50.61095 | 2024-11-29 00:52:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 136a19ec-431e-3e69-81c2-b7472dcc20de | 2.09298 | -50.647 | 2024-11-29 00:54:00 | TERRA_M-M | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f3d33c9-cc42-388d-9b0e-1f7fb7dbd829 | 1.21953 | -55.96266 | 2024-11-29 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 05d5c5f0-e901-3557-a7ee-a610976725ae | 1.85853 | -55.80258 | 2024-11-29 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b9f94cf7-7c90-3dd1-b019-955e95978cd7 | 1.86075 | -55.78939 | 2024-11-29 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| f0efcfd8-8f97-3da9-926c-225be2ef1a0b | 1.8613 | -55.78293 | 2024-11-29 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ef0f2811-ca8b-3e70-9a36-8fe8f9696e2b | 1.85573 | -55.82238 | 2024-11-29 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 638fa3e6-acf0-34a8-be07-f82c5b499d6e | 1.67572 | -50.66632 | 2024-11-29 00:54:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 21797214-f792-3cb8-a8d5-af813f122636 | 1.85781 | -55.80907 | 2024-11-29 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fbc200d5-b7b9-3832-b190-3ec209bd9aeb | 1.89495 | -55.73446 | 2024-11-29 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 67432143-82bc-3f07-9cc1-9b74aa8dddc4 | -2.6498 | -48.7986 | 2024-11-29 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 0645522a-a019-3591-bd04-f397e020c94a | -5.0399 | -43.6205 | 2024-11-29 01:00:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3253e2e9-7d73-31ba-a9d5-80f280d54620 | 1.8583 | -55.8018 | 2024-11-29 01:00:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e20f389e-a937-3019-b6a5-d75d7f557ee9 | -4.4405 | -46.5754 | 2024-11-29 01:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 98.1 |
| afea7b02-d577-332c-af07-e0530038502d | -4.8529 | -41.2445 | 2024-11-29 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 52fbcc58-ae42-3da6-bf84-7105c16d8801 | -2.6684 | -48.7767 | 2024-11-29 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2295efd5-d729-36f6-8d37-31bcb274ca15 | -2.1351 | -54.8861 | 2024-11-29 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| da7fd9be-b6e1-3305-9539-de7fab64b686 | -1.5897 | -52.2915 | 2024-11-29 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 536a8cca-2fec-35d0-a7f7-4c7adf2013d4 | -2.8664 | -45.5528 | 2024-11-29 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 134.1 |
| eb5828de-9fe3-30c7-9f96-d5eb4795fd66 | -3.259 | -53.6388 | 2024-11-29 01:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 94261e5c-b9a5-35d5-af7c-86110fe99c85 | -2.6683 | -48.7981 | 2024-11-29 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 69e18107-eacd-3500-a689-b8a109ef08a9 | -4.8527 | -41.2687 | 2024-11-29 01:00:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 49371712-d347-3734-9314-4ac19e12c0bd | -1.5897 | -52.271 | 2024-11-29 01:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7031ceec-5593-31c6-b68c-a88021317276 | -2.8665 | -45.5304 | 2024-11-29 01:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 92eb4953-1635-35da-bc40-55be1f4afc3e | -1.5869 | -53.8336 | 2024-11-29 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 5d89a22c-a73d-3600-9c8b-3ca3ea820e7d | -2.6499 | -48.7772 | 2024-11-29 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 100ae7c7-b635-34fe-bcee-257087001cb5 | -1.092 | -53.3954 | 2024-11-29 01:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4097e396-a294-3887-bf5f-257c69b85682 | -2.8425 | -46.8193 | 2024-11-29 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |


[Clique aqui para ver as próximas entradas](README12.md)
