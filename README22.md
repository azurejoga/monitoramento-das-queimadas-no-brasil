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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7dc7dc40-d19c-37ca-b770-b2dfa92d13c7 | -15.617 | -59.9809 | 2024-10-14 01:21:35 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87e9b825-c062-31b1-870d-65ac9fb47560 | -15.6186 | -59.988201 | 2024-10-14 01:21:35 | METOP-B | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cfef9b2e-ad8b-377b-ac9c-327cd8fe2a84 | -14.8671 | -57.470001 | 2024-10-14 01:21:38 | METOP-B | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b876568-bcad-3f5e-ab0f-e73f93ba8dc7 | -12.3124 | -50.224602 | 2024-10-14 01:21:51 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ceaa77c-b22d-32e9-ba8b-95d030dab34c | -12.3028 | -50.2272 | 2024-10-14 01:21:51 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3a88232d-64c8-3dc4-98f2-9525336ccb16 | -12.3079 | -50.246799 | 2024-10-14 01:21:51 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6d0a130-0817-359f-9bdc-18267cc2af25 | -12.8758 | -53.511501 | 2024-10-14 01:21:55 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1d6e5a8-e5d2-3ac8-ae1a-5740522ff7b9 | -12.8787 | -53.523201 | 2024-10-14 01:21:55 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db7717af-b57a-30f5-941e-55eff76466d4 | -12.8815 | -53.534801 | 2024-10-14 01:21:55 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33858d81-ee26-3476-95fd-8ac3bf319df5 | -12.1457 | -50.656399 | 2024-10-14 01:21:55 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8665f83-e0ed-397a-96fc-a0efdf93a48d | -12.1504 | -50.674801 | 2024-10-14 01:21:55 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 86dde68e-1d02-3d85-98f2-476a49269ce5 | -12.1552 | -50.693199 | 2024-10-14 01:21:55 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 747c9363-2f1e-3d49-84a4-8b995a7d7220 | -12.866 | -53.514 | 2024-10-14 01:21:55 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c8447dea-fb90-34d9-bd29-6c6ad1c22412 | -12.8689 | -53.5257 | 2024-10-14 01:21:55 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 13dd0ed0-997b-3484-985e-fdfa2130201f | -12.1408 | -50.677399 | 2024-10-14 01:21:55 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 11abb4ea-f763-3f92-bd3c-55b83eea7525 | -12.1455 | -50.695702 | 2024-10-14 01:21:55 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0b5f60f3-9779-3ce1-842f-4c2b4a686082 | -12.1215 | -50.682598 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 582590be-81fd-3ad9-9548-9df5c776aa36 | -12.1262 | -50.701 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e919acf-a945-3796-8cf5-12f477187977 | -12.1119 | -50.6852 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 969dafd8-d217-3b6f-8ebf-597a7850dd3d | -12.1166 | -50.703602 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e26e9de-5f3e-3f2c-87a3-09befe280e37 | -12.0877 | -50.672001 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c8fca8f-cb70-3973-aab4-ea4347325b54 | -12.0925 | -50.690399 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48b48d55-a8a7-39b8-b364-eae4f26fbfec | -12.0781 | -50.674599 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 780ad559-f529-32e4-ab28-9f281521ff79 | -12.0829 | -50.693001 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50a38354-cb4b-37f3-b0e9-3dda58925a59 | -12.0923 | -50.729698 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c8b05982-c25f-316a-a709-be55e593b8e2 | -12.097 | -50.747898 | 2024-10-14 01:21:56 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07063bde-cc3f-32d8-9f3d-6f6c8f09a2e2 | -12.0873 | -50.750401 | 2024-10-14 01:21:57 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ecfda01f-dc6a-3ede-8f1c-34d1b970ea26 | -12.092 | -50.7687 | 2024-10-14 01:21:57 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d51507bc-d367-3683-ba6c-f13f1a0a8c83 | -11.5526 | -53.847599 | 2024-10-14 01:22:10 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8467a13b-0a6f-331c-ae6d-0000ecbc7bb3 | -10.5127 | -49.7644 | 2024-10-14 01:22:10 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ea497c8-80e0-331d-b940-6ddef748436b | -10.5185 | -49.7869 | 2024-10-14 01:22:10 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 100fd257-9409-3f16-a592-b0f60300785d | -10.503 | -49.766899 | 2024-10-14 01:22:10 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89681ad3-ec9e-3756-9769-bb1c1183827d | -10.5089 | -49.789501 | 2024-10-14 01:22:10 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da269a64-fb31-3e07-a7c2-04f08d87a0d0 | -13.1431 | -62.2929 | 2024-10-14 01:22:15 | METOP-B | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9faa7f2c-8d4d-3b1a-bbea-61b00a296a5f | -13.1449 | -62.3013 | 2024-10-14 01:22:15 | METOP-B | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1127be0c-1834-3a86-ad58-06f8c078cac7 | -10.0008 | -47.283501 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dbd39b23-f60c-3cf5-8ae2-736c4c28ebb2 | -10.0098 | -47.3172 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7d7a180d-97be-3e79-87bb-a66991dad0bd | -9.9912 | -47.286098 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f1fddd05-6333-3a04-9ffd-cfc955b05429 | -10.0002 | -47.319801 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b46c0ec6-1627-3e9e-8ec3-c5e0d768bcb5 | -9.9817 | -47.288799 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c174917d-21bd-3a72-b367-fbfa748aa4cd | -9.9907 | -47.322498 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42631a49-c11a-3bcc-b8cd-84fb607bf50c | -9.9722 | -47.291401 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1048d937-6756-3334-86a4-5ab75a16a7c3 | -9.9626 | -47.293999 | 2024-10-14 01:22:16 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 704974c5-1623-33e2-8e37-814395354944 | -10.6201 | -54.6008 | 2024-10-14 01:22:28 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d0640528-b7ea-32c9-93d8-215aa7c59b0c | -12.5124 | -62.995899 | 2024-10-14 01:22:28 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 261e4709-034d-3496-a40d-15dd2e2b87ae | -12.491 | -62.991199 | 2024-10-14 01:22:28 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9cba1b55-9466-3d18-b2cf-4b9abd14a69a | -12.4928 | -63.000099 | 2024-10-14 01:22:28 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 794c6adb-b0d0-3d22-8fda-e650c872bc30 | -9.0853 | -47.9212 | 2024-10-14 01:22:33 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bd328373-cbcf-3682-96f8-586e44a794fe | -9.0757 | -47.923801 | 2024-10-14 01:22:33 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4756a561-f620-338a-bdfc-f145fb0f7007 | -12.5008 | -62.989101 | 2024-10-14 01:22:36 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c1f67c35-66b8-3752-b03e-22d43276300b | -12.5027 | -62.997898 | 2024-10-14 01:22:36 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 95d4e3d0-cea3-37fb-b52c-64b1fe683163 | -12.5045 | -63.252102 | 2024-10-14 01:22:37 | METOP-B | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0a7f9132-03e2-377a-a3da-9ee5258ee2c7 | -8.4671 | -48.609299 | 2024-10-14 01:22:46 | METOP-B | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 9704798b-cce8-3a92-9353-7fd6462a122f | -9.323 | -52.837399 | 2024-10-14 01:22:50 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 987f3ff3-b859-3ec4-8455-c50567350bce | -10.4324 | -60.999599 | 2024-10-14 01:22:54 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8301ec67-047f-3c61-891e-a98a3c07a9b1 | -10.421 | -60.994598 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9565e3f7-0a2f-3f94-8851-149994cfd09e | -10.4226 | -61.001701 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb6e448b-0965-3631-9ce6-c9b772970324 | -10.4241 | -61.0089 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 351a0ad2-6784-345a-be07-d053e6011774 | -10.4096 | -60.9897 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a8c3947-fc88-3816-b8e4-fcfdbedf90d3 | -10.4112 | -60.996799 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f248cf9-d7c6-3edb-b343-7d587d8522d9 | -10.4128 | -61.003899 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c49c834-e8f9-3076-8276-138d8dcabcc5 | -10.4466 | -61.252399 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a8041cb-e065-32d9-a6b7-2d1d9e3a3e68 | -10.4482 | -61.259602 | 2024-10-14 01:22:55 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b7b6ddef-dde0-3a3e-b779-4358ab8285fe | -7.9396 | -49.023602 | 2024-10-14 01:22:57 | METOP-B | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 923b5f7f-1c50-3a23-a7ad-c499c4e5279e | -7.9468 | -49.051498 | 2024-10-14 01:22:57 | METOP-B | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| cc5be210-3ba6-391c-beb3-97370bdd34aa | -7.9539 | -49.0793 | 2024-10-14 01:22:57 | METOP-B | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6523e644-be0b-3b51-b87c-a67459ce7e6b | -7.9372 | -49.054001 | 2024-10-14 01:22:57 | METOP-B | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f3164267-983f-36b5-b6fb-e8b2c33d9196 | -10.1613 | -58.635399 | 2024-10-14 01:22:58 | METOP-B | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 67fde35e-3369-3b5c-8e5b-1184c3d330cd | -10.1629 | -58.642502 | 2024-10-14 01:22:58 | METOP-B | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b34d438f-4540-340d-90fc-d30a6ca395e9 | -9.8903 | -58.1259 | 2024-10-14 01:23:01 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5224d10-0f1e-3eed-913a-aa3a8a0ed125 | -10.0573 | -58.994701 | 2024-10-14 01:23:01 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f47b8ba-3329-381a-b352-4f703d858c12 | -10.372 | -60.678799 | 2024-10-14 01:23:02 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62776a58-2f82-3670-bda9-7f0b66e0a7a3 | -10.3674 | -61.1717 | 2024-10-14 01:23:04 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a948afc-b898-34f8-84c9-b8750df0385b | -10.3689 | -61.178902 | 2024-10-14 01:23:04 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d36b3e1f-283d-361c-b6ac-1fcb60c82b04 | -10.3705 | -61.1861 | 2024-10-14 01:23:04 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d059497-a6e8-37cb-9834-62549cd09e87 | -10.3721 | -61.193298 | 2024-10-14 01:23:04 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 980b9dc6-24ca-34af-9cd3-f167c4350a04 | -10.1906 | -60.882099 | 2024-10-14 01:23:06 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 38e06b90-72d1-391e-a8ee-22a8c3dbb4dc | -10.1921 | -60.889198 | 2024-10-14 01:23:06 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bf4d0bf4-fc5c-31d9-9cc4-a28f97a96ef1 | -10.1937 | -60.896301 | 2024-10-14 01:23:06 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79ec7c63-fc77-38e5-a778-820191259522 | -10.1839 | -60.898399 | 2024-10-14 01:23:06 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a9f657f-af2d-3a86-bb1d-e04784827699 | -10.1855 | -60.905499 | 2024-10-14 01:23:06 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1d94d0d-f863-3989-9b19-f88a03f64430 | -10.0677 | -61.118099 | 2024-10-14 01:23:09 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 618055a1-69ba-3e78-b8c0-2ae23ffd712a | -10.0563 | -61.113098 | 2024-10-14 01:23:09 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 233848ed-e0be-373a-b7ce-ad18527fe61f | -9.8489 | -60.268799 | 2024-10-14 01:23:09 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2edb2898-df61-3865-9ad4-489827232f2e | -9.7658 | -60.404099 | 2024-10-14 01:23:11 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b99ed6b1-b64b-32e0-bbc5-91685e0b4efb | -9.1142 | -60.390499 | 2024-10-14 01:23:22 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6b2e6db5-44ad-3d58-8592-236ac77d6879 | -9.4237 | -61.791401 | 2024-10-14 01:23:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd965e1-393d-3c6d-a6a8-518bf5c1e031 | -9.4253 | -61.798698 | 2024-10-14 01:23:22 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1b342d36-2fcc-308e-befb-6190c775da4f | -9.1167 | -61.143398 | 2024-10-14 01:23:24 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93405a9d-eff2-317b-8fb6-007d310a05a4 | -9.1182 | -61.150501 | 2024-10-14 01:23:24 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ae03dd9-d48c-3efc-8c5b-d9c68d2f8980 | -9.1053 | -61.1385 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55c52578-3e54-3e8a-893b-a4a9e4ea14f4 | -9.1069 | -61.145599 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a25d5612-8708-3f90-9ccf-6de8ac104795 | -9.1084 | -61.152599 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdfac31-7a70-35ef-8937-be59d3a2e0db | -9.11 | -61.159698 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 828cc465-e5d5-3f70-93f8-806cc8d217c6 | -9.1115 | -61.166801 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b1cab5b-ff87-34c7-b75b-748b6f34c7c4 | -9.0955 | -61.140701 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee634804-4403-3008-a544-9720e36e2a25 | -9.0971 | -61.1478 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cedaa3ed-e9f5-3038-9356-198b746b8557 | -9.0986 | -61.1548 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5da38c3c-48ba-3bc4-b05c-89b654082112 | -9.1002 | -61.1619 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49c5730b-865e-340e-928f-1a2a57eb291a | -9.1017 | -61.168999 | 2024-10-14 01:23:25 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
