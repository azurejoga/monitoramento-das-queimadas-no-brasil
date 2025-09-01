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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97970fe7-28e9-312f-a2e7-7edc81ebed78 | -15.23223 | -53.79371 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bceb4d87-3c11-3a7d-bc31-df05e0c17574 | -10.77355 | -48.83689 | 2025-09-01 04:34:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea80ffd1-1605-352d-a903-935891ab155c | -18.07516 | -45.95007 | 2025-09-01 04:34:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 26ffeafc-5e01-3496-9f07-cb1dd5bd974e | -14.04248 | -44.59135 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff804138-3bc9-345b-84fb-4d4e35122343 | -12.78345 | -48.08608 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9b3bc7d-75da-3d58-84fe-c17cade4dab2 | -17.16145 | -46.07153 | 2025-09-01 04:34:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a35f1de-faf0-3e67-a9dc-5fba63e18e88 | -11.51742 | -54.47245 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 84c89a65-2d98-31d1-8c82-e5b5e93382e7 | -12.94484 | -48.09993 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f6aea23-5a34-3189-9184-33e8b58ba179 | -11.03794 | -47.04198 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1248353-61fb-3663-a204-bd7e7aff2459 | -13.50822 | -46.98177 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 899e3a41-b67c-3b54-a52a-b7772797350e | -13.53755 | -46.97746 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 601a48e1-6030-3f4d-8613-b52f14c1e281 | -15.54373 | -51.7212 | 2025-09-01 04:34:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a3facd3-abfa-35f4-ad75-d188e4750aee | -13.65043 | -48.1605 | 2025-09-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f72ed5b-07d9-34ee-9089-792396113bb6 | -13.68316 | -46.87236 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01b28995-bbfb-337d-9349-28135920caa1 | -11.20458 | -45.04293 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fae6430f-dda9-3fc8-a77c-0bbd70b297f6 | -13.32016 | -46.95801 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90811028-5100-3818-9863-36580726de58 | -12.90771 | -53.90028 | 2025-09-01 04:34:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7040fa70-35ba-37bf-9bfe-1b0eb5139260 | -11.59432 | -54.55558 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34e46bd9-3a3d-32cb-b2d6-010cbfa5678e | -15.58545 | -48.34318 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c3002b3d-20b8-32e9-9029-f2e8d2af577d | -11.79922 | -46.42746 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5d7db559-d40d-3901-8a79-244594ca1066 | -13.49255 | -46.99091 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 87138861-72c5-394e-8bcc-0cc16cc2afd7 | -12.63698 | -48.24424 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6e84137c-4555-3cc6-b64c-5dec252dc7c1 | -12.57457 | -48.21243 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f9815e4f-17c4-334d-bf92-ac2a8179e8a2 | -11.51808 | -54.46875 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89dc684d-5592-3dac-9b89-a9fb69d903e4 | -12.83722 | -48.07217 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10e48527-b719-3c6b-b4a5-7ebe180a36b2 | -15.69838 | -48.96288 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 08bd2566-ec5f-39f1-8ef9-a56b96aa01fe | -11.05654 | -52.03924 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48625759-ff7b-32d1-9117-a3a1e637c8cf | -12.61473 | -48.19669 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f051e0b-6b28-3731-842b-aff2f4630acb | -12.86963 | -44.75922 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f38152a-2522-3525-9dfa-5b2c8ac8e4ea | -12.14062 | -47.19744 | 2025-09-01 04:34:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80d6a0fd-c902-34de-915e-a2a7b0f6253d | -14.82404 | -46.7398 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82b0c782-99a0-3bc6-b9a3-f13f8afbd16f | -16.20554 | -55.95255 | 2025-09-01 04:34:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 0dcb65d8-cc0a-3502-8061-9c5994739f55 | -8.73433 | -62.41061 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8eea0384-f545-3bf7-a1c8-222e8cf27bc6 | -11.51873 | -54.46504 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c515d65d-2bfe-3666-87f2-77e40a135fda | -15.69292 | -52.74654 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6d74412-3c91-3a52-8de7-0db992003b38 | -11.8742 | -46.70527 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 95987376-b9ba-3e78-9bde-671dfdec8119 | -12.96052 | -48.10995 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d09bea6-4d83-3cb1-8787-e50d7dea84bd | -13.48847 | -46.99431 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fa085fd8-bfe5-3b2e-a206-beb2c4901590 | -14.31077 | -60.34689 | 2025-09-01 04:34:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 922d0a13-1d89-3aba-9397-c71788e757e9 | -13.49197 | -46.99483 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| bad180cd-d449-35dc-8793-3ef64a7a152b | -9.4358 | -60.57789 | 2025-09-01 04:34:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24e82339-a07d-30c8-afdf-a6a71766c4a3 | -16.29096 | -52.94184 | 2025-09-01 04:34:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8ea6dd7f-58a5-3a37-9403-2ca310cb9d8c | -13.36319 | -46.93961 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 875413d7-284b-33a1-8dd3-553e22f0967d | -11.05225 | -46.92469 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fbb2d37a-ae18-3fdd-bc97-cf914d8fc3f4 | -13.6975 | -46.92282 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f270e7c-376f-30b1-937c-c4a68546170e | -14.76097 | -46.75812 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dd3a204d-4fcd-3c87-9bac-46ae6223cdab | -12.8688 | -48.16967 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 627d58b0-3291-3a8c-adb4-19af351139fd | -12.91391 | -56.99336 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16559805-5f46-3e8f-923c-08946638cd9a | -11.91486 | -44.88567 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf67d35e-0d90-3fc4-a109-467c7c5b5d01 | -18.1184 | -48.54038 | 2025-09-01 04:34:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1738d471-8d1b-33c0-ae80-61958a7e5ae5 | -16.97114 | -49.31292 | 2025-09-01 04:34:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a3fffd8-3b1b-3ed3-9649-a4f40ae06e2a | -11.79568 | -46.42696 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c878c9b3-b9ed-34cc-8103-72e832732ea3 | -11.04593 | -46.98944 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1d6da688-b41a-311e-b704-2c94f4375b66 | -14.00393 | -44.50632 | 2025-09-01 04:34:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a5649e10-b74b-30a2-86a7-af42f101ecec | -11.04364 | -47.00448 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 019b9156-5e1b-3a09-857a-a5b0d4d61167 | -12.87022 | -48.06973 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3e5bc4cf-c6c1-31ac-9191-91115de5373e | -15.71957 | -49.00367 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a40066ae-1a67-3aba-adb1-90dc77ac7c40 | -14.02192 | -43.90676 | 2025-09-01 04:34:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b0ad8291-34c4-30fa-85c9-662ac4cccfe6 | -15.58828 | -48.34749 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9f0d5c74-ccc6-3da4-ab0d-ef78e4c71077 | -12.57177 | -48.20828 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ee9419f-694f-3663-8188-7fc51fbe5c4a | -14.74901 | -46.76477 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ae870cc9-e165-3311-b9cb-cda97f7f17e2 | -11.8046 | -46.41497 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0d20f75b-6455-3649-8848-f2a756a53e82 | -10.84328 | -55.75686 | 2025-09-01 04:34:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1297aa36-ae70-342e-828e-9c7444549091 | -15.70445 | -48.90049 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7d432723-c43f-3354-8b42-dc922352c040 | -14.78751 | -46.7388 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7729e675-730a-3e1a-b1eb-078061dd5542 | -11.88575 | -51.7016 | 2025-09-01 04:34:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8760550-26f9-32fa-840a-b31eaec77335 | -11.01039 | -46.85206 | 2025-09-01 04:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce7ea88c-8464-38d2-a3a9-90d552f751bf | -10.79063 | -47.26321 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8018da52-ed2a-3e17-b4e6-6f6379625408 | -13.35511 | -44.62259 | 2025-09-01 04:34:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a20f90e-7920-34b4-acbe-1b578db4f3dd | -14.02871 | -44.47635 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00446f31-1b91-36b4-8d32-eaa4c7a77ec7 | -14.46073 | -53.04918 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4366e0bd-516f-3388-b9fb-f5ca586981d1 | -14.04586 | -44.56628 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 387c0cb1-1f23-3a4f-9938-64e2b80cf00b | -13.70048 | -46.92709 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 306270c1-dd5c-37d4-b86e-38f3b229233f | -11.65111 | -44.86311 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46798bb3-e45c-3037-9461-cd8503227208 | -11.80042 | -46.41948 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fed03cf3-97f9-3f2f-9694-2365fe9d0a2b | -11.35617 | -43.52777 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15bb5fb4-5c71-37e0-8f87-84f6b5e51b24 | -15.6989 | -48.89184 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| bc45c479-6ace-3cc8-9116-46396405bc1b | -14.75316 | -46.76139 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1a93ec02-ec3c-3365-b5dc-ac9e241a5bbe | -11.46108 | -46.80864 | 2025-09-01 04:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51b2d6cc-20da-3f3a-a859-8c5535ba25c6 | -15.69221 | -48.93584 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e68abcb3-d101-3e12-8d92-89a6ce2e4c11 | -11.05398 | -46.91329 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc73e610-317d-39be-b390-5656572c6858 | -12.87997 | -48.16406 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 86f00148-48b8-3fe8-a1a8-322ecb90f566 | -8.7173 | -62.42212 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 30ea63e5-2896-38ee-980a-85e9688ba6e3 | -13.69692 | -46.87701 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 070d6e50-780f-3456-87fa-4cc1853bc2de | -11.96 | -45.80013 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 028c0977-3d80-35d0-8e8a-1bec4307a51d | -12.96297 | -48.10601 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82a3355b-2fe7-35b9-a241-1baf825cfdbc | -16.15489 | -49.63397 | 2025-09-01 04:34:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93af25de-d907-3294-8977-96cef35fe375 | -11.0328 | -47.05276 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae7e60e2-37cf-35f1-ad2b-abef378ca0b6 | -13.53401 | -46.97707 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 586a2532-1d1b-3f5f-b027-f9d51be676e9 | -11.89693 | -46.69637 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 129580bf-b6a2-3ebc-bf71-179736895b99 | -12.96107 | -48.10636 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1b94dd6-30e9-3a18-9b04-7fa99468171e | -11.87019 | -46.73265 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d5669e4-61a3-387c-922a-e131e89eaf29 | -14.82042 | -46.7395 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b20d4c83-1981-3c34-aa45-74179f536c1c | -11.01798 | -47.05815 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2825a99-6684-3f18-9d7f-f7344ebf78be | -15.70056 | -48.92602 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6d2ed4b-17d1-3a7f-8323-2db231679cd7 | -12.39178 | -46.4734 | 2025-09-01 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e432b7c-0237-343c-b906-62a2862b672a | -16.51133 | -55.03579 | 2025-09-01 04:34:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 73d4e3aa-3aa0-3cdc-a924-1d3b8fadaeee | -10.24001 | -51.10935 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a1a096c5-c336-3d2b-8651-229045bfe3cc | -12.82378 | -48.06997 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4a9a7c3-e9eb-3efa-85f6-8d175c0ef3d5 | -11.88594 | -46.74669 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README67.md)
