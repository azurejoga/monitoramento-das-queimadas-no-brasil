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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 326b2834-1e43-3c66-8a4b-55257d9c4a72 | -3.33868 | -50.12728 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 27514166-fcc6-352e-b59f-225e3bf086de | -3.33471 | -50.1212 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 069abb67-cdf8-39b5-b650-5de0c9c07b4b | -3.33385 | -50.12647 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 34a86b75-7660-3cbc-b514-d18bb06bea4f | -3.11281 | -50.38399 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2479ba6-a743-3e74-9676-f215ff104350 | -3.11144 | -50.38215 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a4e96ce1-06e5-35e2-90ff-0a5c6bcd4d07 | -3.1105 | -50.38802 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ef6b0c4-0d91-3a3d-92a5-84b9f1601ed7 | -3.10789 | -50.38309 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| efd21f4f-a1b1-3aef-916d-7b3ab7fe4813 | -3.10691 | -50.38889 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 739dff46-fe45-3bde-b6a2-901132ef1539 | -3.10652 | -50.38129 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa62f22d-e358-396e-8d63-94feca2e52da | -3.10559 | -50.38706 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 637fa505-bdab-3e0a-ac08-cea6673db124 | -3.10297 | -50.38221 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8a5dc693-afc3-304d-a059-f39c6b9afe22 | -3.09464 | -50.46152 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 75168da2-729d-3ba2-8fec-da22c4e1fb34 | -3.07459 | -50.48442 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2cc2dce-4a6d-38dc-a659-52161a9f79dc | -3.04441 | -50.29737 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94fc08c8-2d5b-31e9-a735-0b91f92615ed | -2.89426 | -50.39732 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ea5365f-1b0f-3cba-a92e-f7f4a976e7b7 | -2.89351 | -50.39424 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6312c13b-0d4d-3308-95f1-c5c12416de93 | -2.89331 | -50.403 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cce03856-c5ac-34d5-a959-ec071aa76708 | -2.8926 | -50.39992 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a07642d-96c4-3ebe-8a45-eab2b1d6de25 | -2.4765 | -50.24794 | 2024-10-09 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6cbf820a-046b-3764-bc1f-f64b89e9cafa | -2.47556 | -50.25354 | 2024-10-09 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4958ad28-1044-3fb7-8625-9a1ab2e5265a | -2.47543 | -50.24463 | 2024-10-09 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be6f77fd-0ea9-3292-829d-7a8adcde50b5 | -2.47453 | -50.25023 | 2024-10-09 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 25544201-19f7-3959-ab65-93a39481de5c | -2.47155 | -50.24717 | 2024-10-09 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b1711ded-9142-301b-b612-f79979f4adbb | -2.45294 | -50.25829 | 2024-10-09 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5b86c69e-0acc-3307-899b-8d0b878337ef | -3.45913 | -49.15949 | 2024-10-09 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 370018f8-a198-32a0-9ced-d196111b9532 | -3.27082 | -49.09929 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fff81000-119e-3ed5-83fc-0ae8182bcda8 | -3.05829 | -49.39334 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37009545-4bb9-3996-b19a-ef1d61a6520a | -3.05752 | -49.39816 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d19b9f6f-a2d4-319d-a93a-c484a2881d98 | -3.05715 | -49.39682 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6830bdd0-dc2e-3907-9594-2ab11f97896d | -2.98382 | -49.53045 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 06cd2f65-e100-3995-8f92-542053a29239 | -2.97915 | -49.52972 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0d829964-603f-32b9-ae73-695887fab1f5 | -2.87622 | -49.15394 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0423e2be-8287-341d-bb85-213390ef8510 | -2.6073 | -49.78919 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 3cd1669f-756e-3a07-9f2e-ae7e2712e361 | -2.60646 | -49.79433 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 34dbbb83-ad0f-3a2e-8db2-018ea17f6eb2 | -2.60252 | -49.78842 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65de226e-065f-3602-ad7d-19da6b8769bc | -2.60169 | -49.79354 | 2024-10-09 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5dfe1aef-ddd3-3c53-9746-3c19cd90caac | -2.40825 | -49.1327 | 2024-10-09 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5defa2d-bd51-305f-badb-f568f67bf2ec | -4.92316 | -50.56893 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ba47db1-8309-3900-822f-c25618e1c069 | -4.9222 | -50.56528 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fe150636-cb9c-33b2-9976-90992db78d59 | -4.72878 | -50.87562 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6749be4a-e748-3af9-9e3c-002b46f65bae | -4.7283 | -50.87846 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f5722a0-457c-33f6-9f65-4b34853f5c4f | -4.72427 | -50.87201 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0794cd2-96bd-383d-85e6-399884a183f7 | -4.72379 | -50.87486 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4cac697-5a77-33d7-8af0-31d54e3f233e | -4.72332 | -50.87771 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bd98aceb-9697-3474-bcaf-96ab9457545d | -4.69987 | -50.40067 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10479b78-2534-31d1-852d-86da68227d61 | -3.70426 | -50.17364 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 98eec0c6-b853-308c-9ebf-f3934ecae930 | -3.70336 | -50.17899 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c9f53833-2fbf-3cd4-9f59-f4f10b6b7241 | -3.69463 | -50.17204 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4aff4c0c-57be-3420-9b14-80cfb6eebb42 | -3.69377 | -50.12105 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 69a4e3e5-3d6f-36d6-853b-676d5047d9cc | -3.69372 | -50.17745 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74aa3d73-b747-337b-be9f-c2acd0f7afe3 | -3.69307 | -50.12292 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 731e8e8f-4ff3-3229-b325-2ef0d1a0b353 | -3.69292 | -50.12627 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58b3ccb9-c883-3587-85bd-05c9853f895a | -3.68896 | -50.12027 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d89822ff-6f6f-3496-8ad2-3901f077e505 | -3.68826 | -50.12215 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 59059dcc-ea0e-3842-9705-daa02528c14c | -3.68811 | -50.12552 | 2024-10-09 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ae3b980e-bf94-3e26-9d29-7c476afcddf2 | -5.09416 | -49.59101 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07e55f89-1b5d-35ff-a5bc-001235d2061b | -4.95298 | -49.64588 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7897866a-83c7-3c24-94a9-6c452de06627 | -4.95201 | -49.76107 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 65da137f-3ced-38c3-b3fd-839b47e1fb3b | -4.95192 | -49.64679 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4752fc6-3920-3418-9106-45bfc9bee322 | -4.94742 | -49.76036 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ed7da753-e847-39ed-bc23-138b548b59f0 | -4.94721 | -49.76154 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 83f3bd8a-0f8f-3687-818c-fb1d38c8aee1 | -4.94661 | -49.76506 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 42916ac5-7b55-376e-8912-29ae212e88ab | -4.94644 | -49.76627 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 94df962c-312f-3c95-9e9a-1ed1d1b45b6d | -4.94281 | -49.75974 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 294a3133-a3a6-3e02-b558-9ab0136f81bf | -4.93819 | -49.75913 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5fe8e47-45d0-39e0-ad9a-af1307a4859e | -4.90608 | -49.86788 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ae1aec9-ddc2-3ce5-b333-8d792a46c92c | -4.90498 | -49.93234 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01e7e572-526d-397c-bbdb-7f4dbd635e6f | -4.90417 | -49.93723 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 206b8ddf-3f7b-3ac4-a7ff-659d1f751dc3 | -4.90303 | -49.93558 | 2024-10-09 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e838cc86-32ab-371a-b623-538cd4815b89 | -4.80808 | -49.94006 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14bdd39e-487a-38c6-a135-3108cfba42e7 | -2.14776 | -50.8876 | 2024-10-09 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a89d2d33-c384-39a4-b0ff-0c2cb20fd212 | -4.80551 | -49.93724 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8b855325-ba06-3c52-9154-2399ee420b99 | -4.80343 | -49.93929 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3275a9cf-74c4-38b2-b95d-28cb7865ace1 | -4.38237 | -49.78864 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 4fd40fae-16f0-3b33-8008-744d16221b43 | -4.38147 | -49.78597 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6de29712-3d78-3ed7-83df-384c5dedd942 | -4.38063 | -49.79086 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5cd2e3f9-2898-3bad-a473-cbc9a7237e8a | -4.18348 | -49.39582 | 2024-10-09 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f5ec218-1814-312b-882a-b4c22f1fab33 | -4.18272 | -49.40038 | 2024-10-09 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a3bea26-3278-31e4-8c40-3af73c68099b | -3.88707 | -49.99199 | 2024-10-09 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 53819085-61dc-396f-89eb-75ac56421c30 | -3.88231 | -49.99128 | 2024-10-09 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 11de924b-bc95-3f9a-ab36-a5102ee88788 | -3.84818 | -49.4565 | 2024-10-09 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab6e1330-cadf-3923-af6c-961d3cc110d6 | -3.84438 | -49.45107 | 2024-10-09 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b0c8c49b-4b93-3ed1-a06d-871399e10312 | -3.8436 | -49.45575 | 2024-10-09 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68677036-747c-317d-9d1b-eb8425b4dfd4 | -3.80981 | -49.48898 | 2024-10-09 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 327aa3dd-b311-34ff-ad59-dc8d6d3be9f7 | -5.99582 | -51.05897 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8d798c1-0526-37c6-ae71-91a2c9c7dfb2 | -5.73057 | -51.10572 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb0290f0-dcc9-374f-b4f6-04aba362d15f | -6.48701 | -49.91415 | 2024-10-09 04:14:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9019689e-324f-3a32-b023-9e7fecba464d | -6.43658 | -50.12631 | 2024-10-09 04:14:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dcd5ddd5-fd17-377d-905b-2e90e6bbe9c1 | -5.84992 | -49.83242 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fa32c7e9-acc4-3b97-927b-9e85b1543b73 | -5.78131 | -50.20807 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e03cb32e-b924-3e85-abe7-b27864ce2768 | -5.71916 | -49.99125 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 121cba7a-b787-38eb-a04b-80e51808e36c | -5.62015 | -49.99204 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee0519a0-6214-3151-a5c8-616659c62dd1 | -5.44719 | -49.5654 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 73ce5259-7fd2-3952-8108-4ece8ceac6c6 | -5.44347 | -49.56013 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2dbdfa12-19e1-338e-a2ce-0b52849f71d8 | -5.44271 | -49.56465 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 89a6c7a4-0b04-35fe-be38-33a71ef8cc48 | -5.44193 | -49.5692 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e634b3e9-4d39-3c5b-8f3d-6631505bfea7 | -5.27034 | -50.90046 | 2024-10-09 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c8c9c1d-81d0-3a8f-a30a-ee26e6ec706f | -5.20647 | -50.60631 | 2024-10-09 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cde1cc87-390b-3a8b-b11e-bbc66a93e411 | -5.06395 | -50.66242 | 2024-10-09 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae08be32-59a9-3f28-afbb-1d1e97edde87 | -6.91047 | -51.25869 | 2024-10-09 04:14:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README80.md)
