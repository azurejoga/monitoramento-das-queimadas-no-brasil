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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b142bccc-98ac-3089-bb25-b3e467271073 | -14.82615 | -48.09638 | 2025-06-01 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c9afa95-cabc-3b7f-8667-e68a218c8f63 | -14.03207 | -55.13763 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12476887-9376-39dc-bdb1-03b6ac1f8c2d | -12.46198 | -54.91367 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5124d279-5209-3ff1-892a-667ff091efd5 | -12.08655 | -54.57717 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2851833d-fea1-32f2-8057-27298452d27a | -14.01694 | -55.12705 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d9cf5e22-8f00-37aa-90cf-93c2560cb4c1 | -11.79582 | -41.19559 | 2025-06-01 04:36:00 | NPP-375D | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e4e572c6-5e47-3aee-a2aa-62bfbd168012 | -11.91679 | -54.42453 | 2025-06-01 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01144db0-fd1b-308b-aaf6-0d566f9f2478 | -13.09785 | -45.26439 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d042a8e9-7a35-369b-af1b-e49457e54ce4 | -14.69635 | -45.10696 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6f76983-0fc6-3d9a-9433-b0ed9c85b515 | -11.03741 | -54.00245 | 2025-06-01 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbc6e126-a434-311b-b31b-c7f0fa6aa9b1 | -10.72566 | -49.54168 | 2025-06-01 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a938d4c3-56f9-3ad8-a658-0dd596cfe082 | -10.2919 | -57.14119 | 2025-06-01 04:36:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5e576c7-e424-3d02-b98a-40c6b8793910 | -15.9778 | -48.29114 | 2025-06-01 04:36:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8603638c-5d2a-3b3d-96f2-89db1f2bc922 | -11.89939 | -54.78581 | 2025-06-01 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad04b0a6-8ed9-37a2-abf8-ce6450b2e7fd | -15.07713 | -48.94265 | 2025-06-01 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75b44d08-036d-3a41-82dd-91395af0ffb0 | -12.52557 | -57.18288 | 2025-06-01 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd585b13-8ec2-3c0b-806f-a6631768a284 | -11.07862 | -54.77248 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 759245a4-31dd-33d9-ba8c-a3a7785dcbe2 | -14.6945 | -45.09088 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d093de26-00b1-3ed9-8f1b-ac5e1f03e840 | -12.12351 | -54.59871 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 535316f2-9bd2-3c6a-956e-6e3432001885 | -10.65623 | -49.42912 | 2025-06-01 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8c5710f-07e3-3a05-99e1-af06fd85c360 | -15.07786 | -48.94596 | 2025-06-01 04:36:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b2bbc42-03e8-39ec-986d-c9fd6bd3006a | -14.02929 | -55.12934 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d570ee5-0ce2-3349-81a0-af1b933b5871 | -13.10415 | -45.27505 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01786a0d-2038-389b-bd9f-7a6771623f49 | -13.101 | -45.26973 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c765b55-d85c-3b95-8c14-839100dd7909 | -11.08568 | -54.78176 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fadbac1-d943-3f54-b6da-ad20f5eb6529 | -11.83496 | -51.2731 | 2025-06-01 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc9adaff-a383-3ac9-837f-ca77d069d8f3 | -11.45354 | -55.00898 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 632ed1d5-0cdd-3de3-9502-e5e153859d96 | -10.82945 | -56.95697 | 2025-06-01 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 85c10ba1-dd8e-3fdb-9228-1663557dcead | -12.08377 | -54.5839 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3fa75f2f-2e41-3449-94d8-d56063c8acd0 | -14.67102 | -45.12278 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d9a96f1-f347-30b1-bab9-b9cc8c743d97 | -14.69495 | -45.11733 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 52dcdd27-a97b-3beb-b02a-cf499f67ed2e | -11.89871 | -54.78968 | 2025-06-01 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 210fb2b0-ed36-3d95-baff-33f76de01e57 | -12.08524 | -54.5847 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea74b454-f7ef-3273-9868-ebbfcae7212e | -14.69564 | -45.11224 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b514522-c6b4-384e-8593-9c521c53d47d | -13.09403 | -45.26382 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35761f1f-d821-30ee-b376-7c09a64a8404 | -11.08638 | -54.77786 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dee98f68-24c3-328c-b0b3-b60588aee9fc | -12.5294 | -57.18916 | 2025-06-01 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d068febb-11c6-3f89-b5e5-886726a8e3fc | -11.42143 | -55.09103 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| afa3af20-319a-3b91-8ac1-02467dfed726 | -14.68647 | -52.6919 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbf151b1-0fed-3835-9493-d2cd5aaa2e47 | -11.0751 | -54.76782 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 75219817-f8b2-33a1-9d13-e7cf5a91eb8c | -12.0907 | -49.4845 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eebbde18-2c87-38e5-af18-d98596acb101 | -11.43647 | -55.00591 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5301c334-1a79-3129-a62b-bb9091b6cfba | -11.07945 | -54.77423 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d55a489c-34a6-3b4e-9386-d8695577b4ea | -9.92709 | -59.90405 | 2025-06-01 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b07181a3-4705-34b7-9e99-797269cb07bb | -11.91798 | -55.43944 | 2025-06-01 04:36:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03653cda-b4bf-39a6-b984-cf7c99bd906f | -10.14396 | -52.14063 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31bb929f-891e-3ef7-bb61-6de82bf85da3 | -13.90284 | -54.66648 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 81a5a596-5e9f-37cf-a2a0-2d197102600d | -10.86653 | -47.46073 | 2025-06-01 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47a8fd78-6407-346f-9324-941bbc2be39b | -14.66989 | -45.12421 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 49c06c48-f3b2-3fa3-be43-9f9a63cc2555 | -14.67847 | -45.12017 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cc682f1-2ef3-3a6b-afc4-bb0fb8981916 | -11.44998 | -55.00419 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d66f5a54-098a-3e7b-8066-dcadbe0dfb62 | -14.68983 | -45.09561 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8583fdb5-faa1-3ff9-bf85-11c017eca420 | -13.95589 | -54.49029 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df303f1c-5c99-3a4c-9600-b301d6ba367d | -11.07721 | -54.78033 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 123d1cb9-9084-38fa-bec9-a0dfecb78136 | -13.10032 | -45.27451 | 2025-06-01 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4cd34ba-3890-350f-9846-55796486583b | -14.02862 | -55.13309 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f5de15e-acad-3a81-936e-7762d5d47db6 | -12.46089 | -54.91427 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62912d6d-b4a5-38a8-9b8a-2a59fb483344 | -12.08179 | -54.58017 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e4c367a-06bd-3203-91e7-82429d9dbe19 | -14.80927 | -48.37001 | 2025-06-01 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54862015-0dc0-33b0-a15d-d9820dc38f36 | -12.09364 | -54.67073 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6816ef8a-a482-3b88-bc16-ae144ccacd77 | -10.62785 | -49.43539 | 2025-06-01 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35a36b7f-f604-3bea-aca4-f80aeff8b7fa | -12.01757 | -49.51979 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40deea67-35e0-3666-b91e-80fefdd4cdd9 | -11.72526 | -56.43589 | 2025-06-01 04:36:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93f4b0d6-7718-32db-819d-0621ba99a95c | -12.12762 | -54.59947 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d43e84ec-7a27-3cfa-9399-dd36519137b8 | -11.0765 | -54.78427 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce27c94c-0e60-3b24-acbd-374dbf3c3835 | -11.92215 | -54.41804 | 2025-06-01 04:36:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 63de1f84-b01f-30e9-b7a2-01727b490a76 | -9.93388 | -59.90461 | 2025-06-01 04:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e7a58652-90f8-379c-a458-b46dd92f9768 | -10.73231 | -49.28545 | 2025-06-01 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4cf0ffe2-302c-3806-9361-9df9842683ce | -14.65116 | -45.40937 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0dc6d2bf-e83f-3285-a040-b5bf23ea7bb5 | -12.72355 | -54.97386 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e12e9c1a-2a77-3954-aff1-5cd04e80a543 | -12.72423 | -54.97002 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 07466570-21d4-31cf-9422-a423afbbffc1 | -10.14763 | -52.14124 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73f95030-1950-3f74-8393-9d5592bee750 | -12.02367 | -49.52441 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1ad0ea3-4ce9-3177-9e4d-af2623fba058 | -14.01904 | -55.13906 | 2025-06-01 04:36:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66aee854-eec2-32ef-afb8-25eddfef0f41 | -12.01644 | -49.52686 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 692d8f60-0781-3a12-bfa1-912d34df0f06 | -12.53041 | -57.18377 | 2025-06-01 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ef30ec3-e509-3be3-aba1-6f4fb0d9313f | -11.4207 | -55.09517 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8c691cb0-1405-346f-b306-5486745b538b | -12.12828 | -54.59575 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66c25f9b-a56e-3e03-ac95-03179ac8fdf8 | -15.06122 | -43.87069 | 2025-06-01 04:36:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ffefba1-c4dd-3dda-bc23-24d08088e0f4 | -14.83012 | -48.09322 | 2025-06-01 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 382e378d-5e01-38f0-b49d-a95ab57023a4 | -11.57609 | -47.44777 | 2025-06-01 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec4b5270-c072-354f-a6b3-f209facc9261 | -12.08513 | -54.5764 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70fb7e7e-909e-3819-a506-e38198b0da7d | -14.69379 | -45.09613 | 2025-06-01 04:36:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32327aca-d091-3b94-9c6f-20dc652ce5eb | -11.82803 | -51.27196 | 2025-06-01 04:36:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f43370e7-7b20-3e91-8df5-d08767064541 | -14.57944 | -58.75336 | 2025-06-01 04:36:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7997e2dd-1388-388d-9235-9763a5e23ab8 | -12.71938 | -54.97308 | 2025-06-01 04:36:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bbdeb7d8-2730-34ee-9800-35694dfbf613 | -11.0334 | -54.00171 | 2025-06-01 04:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d536c316-d863-324e-85e8-8b968279dd3c | -11.42573 | -55.09179 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dda956e-b41d-31fe-8052-b11c625736ec | -11.43291 | -55.00114 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 29c939d6-899f-32d7-865b-ebbc93f9e671 | -12.15616 | -48.68275 | 2025-06-01 04:36:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d7a884f-6cc4-3686-ac1c-42fbe8f42ba9 | -11.07877 | -54.77816 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d409d1f4-6ee3-315c-9016-3090de039609 | -14.68004 | -52.68652 | 2025-06-01 04:36:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5ba4b59-d978-372e-8c5d-71a32a1a1b0a | -15.89688 | -46.0123 | 2025-06-01 04:36:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a44e525-b21a-3d9e-9acd-5bf9b981e5dc | -12.0209 | -49.52033 | 2025-06-01 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc8282f5-d3ed-3bae-b57b-5d3f4dd7d264 | -11.08286 | -54.77321 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d28910be-9693-3ebc-b0cc-1634508aae5d | -11.57894 | -47.45202 | 2025-06-01 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7173dad4-6628-3eba-8148-1494ac501e30 | -11.07792 | -54.7764 | 2025-06-01 04:36:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9137bdc2-3573-3bd9-b94d-9d2ad133d9a1 | -10.07807 | -52.75468 | 2025-06-01 04:36:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5a2b0c4-3c47-3fb0-aa19-f9a827a7fb75 | -11.44572 | -55.00341 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4b0cee0-2cef-3677-aaee-d9a5826f5657 | -14.58006 | -58.75024 | 2025-06-01 04:36:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
