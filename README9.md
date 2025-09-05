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
| 1129932d-d982-361c-bfc6-c8188eb57d31 | -9.076 | -57.115398 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ffbbcda4-ae01-3deb-8812-13bec9a38c5f | -22.409401 | -48.7178 | 2025-09-05 00:36:00 | METOP-B | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c47066e-0dcc-3ed1-b590-2233bc2d4dc5 | -2.1921 | -47.6101 | 2025-09-05 00:36:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c69248b-abdc-32b4-9e43-24ed47269186 | -7.2952 | -48.993401 | 2025-09-05 00:36:00 | METOP-B | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 1a5185f6-68f6-3148-91fa-52c9eadfc93d | -7.6116 | -48.807701 | 2025-09-05 00:36:00 | METOP-B | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 32f2fc68-bf7f-36e8-bbf6-f7f52beaab95 | -11.5073 | -54.544998 | 2025-09-05 00:36:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8f4d16a-fe6d-33dd-ac16-d9ebf0047a40 | -9.5569 | -49.008301 | 2025-09-05 00:36:00 | METOP-B | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5087ac03-dc1f-383d-8a1b-2e12fe0ffcb1 | -7.9145 | -52.3979 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9cb335-d8ac-35f8-bc49-10b2b410fec6 | -17.520201 | -52.311298 | 2025-09-05 00:36:00 | METOP-B | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ff962a00-742e-38b7-b296-9a0a48f423b8 | -6.6845 | -52.835201 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9f18c0b-a5c9-3f40-a36e-c38127050eeb | -6.1152 | -53.459301 | 2025-09-05 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04c544b3-38ee-3b93-97cb-6a106124b5eb | -6.5372 | -49.796398 | 2025-09-05 00:36:00 | METOP-B | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1c667df-b29a-387f-83c4-3335c5a529ff | -22.487301 | -46.768101 | 2025-09-05 00:36:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| db720e72-9b18-3c6e-9d7f-b970e244dd55 | -6.6648 | -52.839699 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03a4ec40-85e9-35b5-a865-1addf7baed7f | -11.5 | -52.249599 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3c221a-424e-38c9-b48c-722a16c66fd0 | -6.4263 | -51.130501 | 2025-09-05 00:36:00 | METOP-B | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee20f4d3-1ac3-3928-8240-46211a4f35a8 | -16.164101 | -52.9809 | 2025-09-05 00:36:00 | METOP-B | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 26c6b6bf-691c-3d58-8e33-d438b7c2dd3d | -22.127199 | -47.166199 | 2025-09-05 00:36:00 | METOP-B | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 83459ce6-e91b-38ad-9eb2-5d6898805ed3 | -10.3322 | -53.652901 | 2025-09-05 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3d74c961-2da9-336b-afae-9d2ceba05833 | -7.5808 | -50.334499 | 2025-09-05 00:36:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33551389-2291-3e1d-858f-74ddc52cc52d | -15.7128 | -52.3316 | 2025-09-05 00:36:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87847943-60d1-3853-a1dd-fb431e000a3d | -9.0904 | -57.0868 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f6f2efd0-de83-3179-a0a4-be9db1ce8323 | -9.9975 | -55.022301 | 2025-09-05 00:36:00 | METOP-B | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5717aa6a-b772-3872-9b05-50bbf902d179 | -12.3449 | -53.862099 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 632558fd-05f0-384f-88bc-48585b97147b | -5.4537 | -45.030201 | 2025-09-05 00:36:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 23de52b7-242c-3def-9f69-02519fbc401f | -9.8361 | -51.6492 | 2025-09-05 00:36:00 | METOP-B | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e4881e7-2339-30e2-9cac-33e72789e030 | -8.3854 | -51.352798 | 2025-09-05 00:36:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11d1cdb1-1f43-325f-a129-3044cf1c01ce | -10.0917 | -50.572201 | 2025-09-05 00:36:00 | METOP-B | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f063c009-8f71-3ebe-8e72-fb483bcc063a | -7.1977 | -46.287998 | 2025-09-05 00:36:00 | METOP-B | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5548b2a3-9140-34ed-bc01-10f2e81292a9 | -7.9331 | -45.356201 | 2025-09-05 00:36:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5f865036-1a97-3666-bcff-b6b23ff5514d | -9.1002 | -57.084702 | 2025-09-05 00:36:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8250720a-fd28-335d-8d28-2c1588a98c07 | -11.6801 | -51.458401 | 2025-09-05 00:36:00 | METOP-B | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e215784-1d02-3654-ac11-ee1ce7b95bd8 | -12.9594 | -57.123402 | 2025-09-05 00:36:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c631a917-537b-3308-8479-33fee369d1c7 | -9.2279 | -50.408901 | 2025-09-05 00:36:00 | METOP-B | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b23731cf-3cf4-3b81-ae3c-2f671c3887f9 | -5.4024 | -46.2071 | 2025-09-05 00:36:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e406d42b-a1e2-3d60-a6f7-34ceec678fda | -4.0586 | -50.470402 | 2025-09-05 00:36:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 964bbd5f-aae9-31b3-8079-3a21dbb9c09e | -23.225599 | -47.2075 | 2025-09-05 00:36:00 | METOP-B | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf2e9ef8-b3b5-323b-9b5d-fe70c1ef781b | -6.6943 | -52.833 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f08fe3-344e-3553-a517-c1fe9312e88a | -15.566 | -53.637001 | 2025-09-05 00:36:00 | METOP-B | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d6e15f5f-39d4-336d-8fb6-783ee9c22982 | -8.9164 | -47.044701 | 2025-09-05 00:36:00 | METOP-B | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d2cc3502-4b46-3ce3-969c-3c15044d51f9 | -5.3583 | -60.120201 | 2025-09-05 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b033273-e656-3011-80e3-95b6b6997921 | -11.4378 | -52.202999 | 2025-09-05 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa9ce425-3ef7-303a-82cf-ecf6ef1f953b | -5.3486 | -60.122299 | 2025-09-05 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e442fa1f-f226-3510-98e9-b07900b39d48 | -15.7026 | -51.777199 | 2025-09-05 00:36:00 | METOP-B | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a14bfe06-87d7-3405-b359-d7df2fd4be99 | -8.785 | -48.671101 | 2025-09-05 00:36:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bf501b9c-8cac-34f2-af80-89b87759d4a6 | -12.8271 | -48.0956 | 2025-09-05 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1c50008e-feb9-3d14-9f03-c0d9001962a1 | -12.8235 | -54.831001 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9f6205c5-dd63-34a6-bccf-902d0c15ecd2 | -12.2893 | -44.7892 | 2025-09-05 00:36:00 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9dc3b97d-d43c-3db9-bee2-8648bf9d7f72 | -12.3908 | -53.837101 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6281d0c3-e562-32b7-94bc-a247a0d09809 | -12.3743 | -53.855499 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| accca760-a571-3023-b747-8a90042465d1 | -12.8219 | -54.8237 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2e715bb1-0fc2-32b2-a267-5eead4e22c25 | -12.3661 | -53.8647 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c4fbb3d8-2eae-306b-9b7b-8ed92d68f161 | -12.1436 | -50.033798 | 2025-09-05 00:36:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a46232f5-297e-30e0-ae0c-17cfd9097463 | -12.856 | -54.839199 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 061f4547-fcfa-348a-b9cf-7e8a8fd4b3a0 | -12.5017 | -49.494801 | 2025-09-05 00:36:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d78b928c-ac76-392f-b03a-eb2db7dd8917 | -13.7278 | -48.015999 | 2025-09-05 00:36:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6e5a7fc5-86be-393e-934f-796ee5128f73 | -13.1286 | -51.883701 | 2025-09-05 00:36:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b0365ad-cee5-3e09-8be9-dc3d9a485583 | -13.9933 | -51.740799 | 2025-09-05 00:36:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b41f21d9-c0df-32d9-884f-0dbc5a4be7a7 | -12.2846 | -44.770901 | 2025-09-05 00:36:00 | METOP-B | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7b45fdb-653f-3fff-b069-5e158b9cc184 | -11.2476 | -43.634399 | 2025-09-05 00:36:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c78dfe1d-4c72-33e3-84ef-5e40218b0589 | -10.8699 | -45.087002 | 2025-09-05 00:36:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c053a2f5-aa67-3b89-9e41-d1592f03cd24 | -12.8254 | -54.7924 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9bca1b76-b01e-3371-bcce-d4adbc14f735 | -12.8317 | -54.821499 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8021b045-99ff-39f1-8883-3b301fd8f104 | -11.947 | -44.742699 | 2025-09-05 00:36:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9c54127-fc8d-36a6-9e76-ee2117c67a18 | -12.1153 | -50.176899 | 2025-09-05 00:36:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4ab169-3a6d-3d6e-98a4-1cd6fd87cefc | -12.8285 | -54.806999 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4c85bba1-e28d-3b50-ae6c-af2d2239e946 | -14.1436 | -51.903702 | 2025-09-05 00:36:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd2ece79-3df0-356f-bde3-d3f61564c350 | -12.3795 | -53.832199 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9629d943-0c28-3323-944c-dd298b49fd49 | -13.7252 | -48.005299 | 2025-09-05 00:36:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 22bd9b46-6a88-3ca1-b541-092ce50468f9 | -12.8349 | -54.836201 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 01b38ce5-1d6d-3fa7-a699-8ccac179b719 | -12.8364 | -54.843498 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e52a51ab-44e5-33a8-8ae9-8059cd929320 | -12.2941 | -48.113701 | 2025-09-05 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 879504ad-dda0-30fe-8f2e-37e3c4ec5283 | -12.3779 | -53.825199 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a5c8b17-d5c8-3681-afa4-59d86a94e4a6 | -13.7304 | -48.026699 | 2025-09-05 00:36:00 | METOP-B | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5fb27f82-3708-3fab-82ee-bc5402bf3b45 | -12.8592 | -54.853802 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ed704fe3-382c-333b-ab95-b673fe1200d8 | -12.8447 | -54.834099 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2af00baf-35e3-357f-afef-88370a427b08 | -12.827 | -54.799702 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a321214-6555-3f49-9940-38311f142ca3 | -11.9374 | -44.7453 | 2025-09-05 00:36:00 | METOP-B | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81170752-ed86-3bdf-be36-f7e906f3ba90 | -12.8545 | -54.831902 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| efb49a98-0122-3ff7-8fe1-6b91a3edf504 | -10.8288 | -46.026699 | 2025-09-05 00:36:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c751f9fb-d7c3-34ef-ba56-bbb6c83e0a66 | -12.8172 | -54.801899 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 684721da-85ae-38a0-b6ee-0a07638e0127 | -12.3759 | -53.862499 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b96b32c9-9fa6-33b8-8fb0-76076b9d05f8 | -12.8333 | -54.8288 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 08ad5db8-14ca-395e-a3ba-16935d3c30a8 | -12.8297 | -48.106499 | 2025-09-05 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98c7c963-6fc5-395c-868b-c03df27b417b | -12.8415 | -54.819401 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 313db7eb-441a-3721-a880-44e3467910be | -12.7306 | -48.038601 | 2025-09-05 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2602a16f-b38f-37cc-9a46-b68290efc110 | -12.8301 | -54.814301 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 266cbf03-99a3-38e2-aee4-d0aa41486880 | -12.8478 | -54.848701 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b9b94388-437f-34eb-876f-913d3713a862 | -12.8203 | -54.816502 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 51bb0179-f1ac-385f-9aa8-c60a9bc591b6 | -12.8383 | -54.804798 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4aa4ebe4-a1f9-335e-9d8a-4dd04f79987b | -12.1369 | -50.180698 | 2025-09-05 00:36:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da4c1885-7c6a-309d-8834-6ed09ff66d19 | -12.1477 | -50.051102 | 2025-09-05 00:36:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d34444bf-8e6a-3436-aa34-b6c2bfec60e9 | -11.1147 | -48.3615 | 2025-09-05 00:36:00 | METOP-B | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 04ea0475-a65b-36b1-901f-43c2abe6d154 | -12.372 | -48.094002 | 2025-09-05 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f633e15e-8edd-3325-b08a-417e86ac2cd9 | -12.8513 | -54.8172 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b40fc729-3787-35d2-9a4b-a366f1dcef04 | -12.3893 | -53.830002 | 2025-09-05 00:36:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90335dd6-84a6-3fe7-aad4-7bf99b165a89 | -12.7651 | -48.053299 | 2025-09-05 00:36:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2f9d3f1-e872-3c89-90d0-ea41118502cc | -12.1271 | -50.183102 | 2025-09-05 00:36:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8c369722-386b-3da3-a65a-e6569722743c | -12.8187 | -54.8092 | 2025-09-05 00:36:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4cac95e2-6586-3ed2-9a70-0b74538a3cdc | -12.1173 | -50.185398 | 2025-09-05 00:36:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README10.md)
