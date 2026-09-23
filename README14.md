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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6a30bf6-cebe-3b7a-b79e-55ee2fc16ebc | -3.9548 | -59.3493 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a65a682-17aa-35a3-a395-4ea55e9fdbee | -4.0536 | -56.3092 | 2026-09-23 00:36:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c59821-c1af-340f-bbe2-876db5209d1a | -6.4431 | -54.9855 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52689e49-07b3-3a7b-8914-4bf855bf3cda | -4.5555 | -54.937401 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d173b6b1-4fc0-385f-8cbe-7dc88627ab62 | -12.8102 | -50.867802 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0731ff38-13ed-39e7-ab8a-74df04be80a7 | -6.0281 | -55.3353 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| feaf7dc3-3900-3bd7-8cd2-91d68c84b57c | -11.3032 | -51.349998 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| afefae25-39c0-37c4-8bef-0097e235dc3a | 1.7832 | -56.0163 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bab30e23-0a55-3e61-a3e4-de0174c172c4 | -13.9218 | -47.826599 | 2026-09-23 00:36:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f00066ff-c0a5-3f12-9163-8136a2684bb4 | -12.4731 | -47.0121 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c44e685-ba53-3753-a86b-8505570a0c4b | -5.6566 | -60.210098 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aaa698ff-a211-3570-bfbe-e28b229e0067 | -11.39 | -44.219398 | 2026-09-23 00:36:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b27ffdcf-34a4-3ed4-af80-05b82755c3ad | -3.7529 | -58.860401 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a835354f-2273-399f-929d-b7af4f01a8d1 | -1.919 | -58.2635 | 2026-09-23 00:36:00 | METOP-B | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9980091f-eaac-3d16-be2c-bd18b2ea9d2e | -3.4897 | -59.570301 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 98e9e047-bca2-30f4-a903-24f68746970f | -3.1487 | -60.622799 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5073793c-d8ee-3a4b-8083-f7c77aa6cf65 | -10.2549 | -49.9576 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 928421c3-9827-38e3-97bf-2cb4f922dc64 | -6.3921 | -60.005901 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd5829f8-421e-3858-9b4e-585751c6d113 | -5.454 | -60.129299 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69531181-f77a-32d2-b0c5-31ce19722834 | -7.4315 | -49.8405 | 2026-09-23 00:36:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18c9c974-234d-383d-ab63-25f3d8cb05d9 | -6.1487 | -59.925598 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9ac3a26a-ed8f-3183-b319-0067869e1f85 | -12.8492 | -50.858101 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c719150-ca81-3036-a29b-3b992bac1aca | 1.9084 | -60.567001 | 2026-09-23 00:36:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| aba2d41e-24df-3170-99a7-936ed4d15266 | 4.0996 | -60.995499 | 2026-09-23 00:36:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cc7703ed-0f86-3e4a-b3fa-eac057569d58 | -3.806 | -52.359798 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ff2921-6f95-3f24-95e6-64da1fd68d2a | -6.2798 | -59.914799 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b93dff13-230f-3bca-86bf-cb08a2c8030a | -10.2578 | -49.969299 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d941742-4bed-3234-a5d0-1e8271e314af | -6.1759 | -53.289001 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c764f548-c19b-371b-a91a-fef34286e817 | -6.0666 | -57.789799 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6863f2a7-9966-34b9-8c4c-3c28c4c5e8a8 | -8.1418 | -49.540501 | 2026-09-23 00:36:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7aafb1b-5d47-3239-a25c-3008433311bf | -10.5465 | -57.440601 | 2026-09-23 00:36:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 292be172-de15-386c-961c-cbace21f4be6 | -2.4133 | -58.262402 | 2026-09-23 00:36:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a9edc87f-986d-3e37-a2bc-852decd33464 | -3.8254 | -59.322601 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1930d79-7553-3b91-a2a3-77615cbaeeb7 | -6.2547 | -55.425301 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f60c1666-016c-313b-b139-39e425646c01 | -5.2402 | -48.181099 | 2026-09-23 00:36:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f2ae9846-c2f1-3f24-9d82-f8a007d723e8 | -12.793 | -50.882198 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c712d140-3068-3029-88e8-0a245a8471d7 | -3.6486 | -58.7626 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9606079e-7e97-3b88-8cac-0d6fc2e5b548 | -7.4185 | -49.8297 | 2026-09-23 00:36:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd7727b0-6ad4-3510-a303-7ed8a09585eb | -8.3167 | -54.881302 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e662f7ce-5e80-3f54-b593-5b7fd8024575 | -8.4868 | -57.612701 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34ab81df-fb86-341f-9f7e-8e2433617fd4 | -10.2577 | -50.223999 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66cb4232-1d18-3f13-9135-23cfe5135a26 | -3.4766 | -59.5574 | 2026-09-23 00:36:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6381aa42-1fb2-38f2-af2d-6d921d7e17b1 | -8.4502 | -55.014599 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb687b6f-34e4-32af-ad29-532ce1fb0f60 | -3.5936 | -59.4366 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ce66d7e7-8beb-35b8-a0e7-237ac3e3b73b | -3.3007 | -57.8564 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ffca47f-ae19-3d96-910c-90a7bbe06b9a | -5.9828 | -57.690701 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87eeb56f-655b-3bbe-b653-7659364049f0 | -6.6654 | -55.055698 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057ca624-547c-35b3-b5b2-53426ca28e8d | -5.7588 | -45.1437 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1c99189f-b939-33e8-8dca-eaa92687de29 | 2.9304 | -60.424999 | 2026-09-23 00:36:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c7c0af21-afcf-3993-aaa5-6ef6220de5fb | -6.6978 | -59.9487 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 792e6b87-f9cd-3c5f-84af-7fa19f3f2859 | -10.909 | -53.9482 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d5280f5c-8e61-3530-b25c-27ee79577681 | -10.8989 | -51.517502 | 2026-09-23 00:36:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 055049f1-9aac-3afc-a987-2258c2d41d91 | -6.4649 | -59.963402 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a6042d94-9c2b-3f5b-ae43-02fe363998a9 | -4.2526 | -59.993599 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| db3d15b2-6c82-3192-9927-95e142a898a6 | -2.5518 | -58.007999 | 2026-09-23 00:36:00 | METOP-B | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09f953ba-8ca7-38e3-99c6-1988c3d9fb68 | -6.1364 | -59.9636 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 736d0f6e-02ad-38ea-a293-aa6bd0d7c935 | -5.9988 | -57.7164 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f396cbc-21cb-3fd8-a055-f02b9ba8590a | -9.5131 | -59.738499 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0422e627-f972-321e-a4a7-fcb0256f2827 | -8.9185 | -61.470299 | 2026-09-23 00:36:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 94a07558-b617-3486-9da3-65ee5d0ac1d3 | -12.7976 | -50.901199 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a75859f3-65d0-3ba7-a279-2e009a3f93f9 | -9.9563 | -53.9776 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40e0cdfe-fb88-39df-9b85-0cac99977fee | -11.7032 | -50.9491 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5e17bc6-8361-325b-a023-31cac3b15bfa | -6.0907 | -57.666801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e39a4ef2-54bc-3c9e-9361-1d02b14555f2 | -7.5495 | -61.4716 | 2026-09-23 00:36:00 | METOP-B | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 071c2003-d877-3dd8-973e-9c76c474e25c | -3.6416 | -58.915298 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5b550454-fdae-3a51-a77f-effa87494699 | -8.196 | -54.7136 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ebd23e8f-f9ea-3a69-bce4-b48fd9703867 | -3.0656 | -58.0023 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e126001c-4434-3722-8795-a0242e5c2ab0 | -11.7464 | -50.999901 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a509943b-1214-3bee-80e7-5eaed882b541 | -6.1605 | -57.702702 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6439abf-9cb4-382d-8242-51a805b48669 | -3.8652 | -52.259899 | 2026-09-23 00:36:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd3d1d27-6cab-3f4c-a96f-0af0bbe7a9f8 | -5.9972 | -57.7094 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd2b9e46-d834-363b-b721-743a5c5c36d3 | -5.2693 | -47.249699 | 2026-09-23 00:36:00 | METOP-B | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0f6608-84d0-3b37-b930-f92dea6e4f1d | -2.6839 | -54.866402 | 2026-09-23 00:36:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d5f7c25-b1f6-3b3e-97bd-55df747bcf41 | -6.1193 | -59.931999 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 20e65579-332e-353c-8ed6-8cd74173ba21 | -9.5217 | -45.362099 | 2026-09-23 00:36:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 49742d1e-1d22-39a1-90c4-aa329426f371 | -4.298 | -49.125099 | 2026-09-23 00:36:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44ea0b4d-48b9-3b45-a0f3-791479d8cd37 | -7.4248 | -49.8559 | 2026-09-23 00:36:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcd752b3-1232-3b6f-9ce4-da8e4dd84a36 | -5.8037 | -49.1516 | 2026-09-23 00:36:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9d444c8-7c12-3d20-8127-19157261df04 | -8.9087 | -61.472401 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4243155c-6bf2-3190-99ad-e49642eb4eae | -10.3074 | -50.514702 | 2026-09-23 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7582537d-0681-3eae-891e-56eb65dbc4e0 | -5.2789 | -47.247299 | 2026-09-23 00:36:00 | METOP-B | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69b712c8-d5af-3a17-9682-980b58339910 | -6.6679 | -58.550098 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c810617e-d896-3f96-a37f-a7961b2b5c4f | -12.4634 | -47.014702 | 2026-09-23 00:36:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6b93a6a-ebd2-34e9-96ce-9db681a654d0 | -8.4406 | -48.698502 | 2026-09-23 00:36:00 | METOP-B | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 10622699-b627-37f0-ace0-294970941b62 | -12.7787 | -50.865601 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 44d56055-cfbe-3002-96a7-0cf142f3b077 | -2.9502 | -57.718601 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcb7ad9-f6da-3119-befe-def82fa69eeb | -3.2212 | -61.0406 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b239ec68-1e0e-392f-ab5d-3e6a16ea9a46 | -2.2297 | -48.740002 | 2026-09-23 00:36:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94e79573-89f8-35a4-afb3-b9b0369fd687 | -5.3433 | -45.154598 | 2026-09-23 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| feb680fa-350d-3898-beee-ef87b1491a1c | -3.7359 | -59.429001 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b7b5b48-bfdf-32c2-bdc3-5b2613a1fa0a | -5.7315 | -53.462502 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6af8e77-bfca-3190-aa7f-e3e1a5e3dc7d | -10.6166 | -53.9781 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3f8aad4e-2ad2-3b56-abb8-465611df4e8b | -4.9403 | -55.8106 | 2026-09-23 00:36:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d612bc36-1c04-3db9-82a8-9901586ebc95 | -3.8307 | -59.3923 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d95fd287-5270-3679-94ce-0c128e30d312 | -12.8125 | -50.8773 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2805c6e-f6e3-3b45-850b-122a12b001cb | -6.1876 | -57.777802 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 042d55c4-5d48-3095-8d7d-ee8f5b6f3d0c | -8.926 | -61.4571 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9cf9f906-fc1d-354e-9a2c-0282e5e81745 | -6.3021 | -57.737701 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c1254d9-04cb-3766-9dda-cffc0acfed76 | -6.1468 | -59.917198 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86aa038d-f533-3409-a781-3b226997b65a | -3.1468 | -60.614399 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README15.md)
