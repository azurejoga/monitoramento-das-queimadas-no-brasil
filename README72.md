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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7f14f89-e4d5-344d-b081-1eeb806488ec | -1.63221 | -55.59641 | 2025-09-13 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef0e8d62-a8c3-3ae7-b789-d779f0cb1ddf | 0.67466 | -50.66418 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2f437bb-97eb-3136-aa9b-05c3c1ef943d | 0.69064 | -50.65405 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2a9e4a56-155c-313e-8e8e-b4e5f9442f11 | -2.28277 | -43.66513 | 2025-09-13 04:55:00 | NOAA-21 | HUMBERTO DE CAMPOS | MARANHÃO | Brasil | 2105005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1539ad1a-942f-3f0e-b5b6-c1dbeba1d01e | 1.57548 | -55.72599 | 2025-09-13 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1908dfee-de86-3534-8b88-1c51dda37179 | -1.97912 | -47.98378 | 2025-09-13 04:55:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 13abffa2-3337-37d8-9fe9-40b6f5ab862f | -2.65865 | -48.79764 | 2025-09-13 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2651ba17-fd9f-34dd-996d-959602acf5eb | 0.68946 | -50.64659 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c66dc19-e46e-3b1a-9c7d-e909e33c33da | 0.69633 | -50.64552 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9672d69-eb92-37cb-be17-28b7c35c9e88 | 0.69407 | -50.65352 | 2025-09-13 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2a43ff2f-cc5b-3ff4-9dfd-d24ae3776902 | -4.91751 | -56.00868 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d178918-3c76-3737-8f11-dc625a23ca8b | -8.09569 | -50.18708 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed38ff0d-4fb7-3437-83ce-bd01e1569026 | -7.52243 | -44.37904 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0fd8f03b-e3d8-3cb9-abe3-69186c7e5128 | -6.10748 | -45.94009 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98d04b1b-b2af-31b3-9192-2c1845d57ca9 | -6.19564 | -45.28571 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8e57c9d-ef92-3e73-9eb1-fc7fccc9a0c4 | -5.32951 | -45.72144 | 2025-09-13 04:57:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66ad3b76-e1d7-3c5e-b628-70c1df2f0e0f | -10.01488 | -50.38794 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e59c5759-6923-3240-a397-7964ffb054e9 | -9.26087 | -51.24171 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 65763dfe-c03c-3480-bf7b-7bdfef5d8dc7 | -9.91143 | -51.88331 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8700fb1b-3916-3368-9009-93d4ed7407d6 | -9.03063 | -47.03769 | 2025-09-13 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d6ff140-f4ba-310c-b58e-6816caa3ebeb | -6.15085 | -51.63622 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71b5767c-c6cf-38f1-bba9-c14afce224c2 | -10.33127 | -48.82556 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27f6048a-66bb-340d-a67e-747c0a5a17e9 | -9.5166 | -54.63328 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dfbc5ade-6719-3b8c-ad37-939aae150b5b | -10.01809 | -50.39363 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 046f092b-24cd-316a-a085-8dee746ffd78 | -6.29095 | -44.23936 | 2025-09-13 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e4471eb-f2e7-3d3c-9d3c-bbd6988291d3 | -4.55039 | -43.73019 | 2025-09-13 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbd6bb1b-5ee6-3581-8a2d-de62cdd4be0b | -9.49753 | -50.88537 | 2025-09-13 04:57:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eba519ed-151a-3c36-9f8b-645f7640006a | -3.90818 | -59.64993 | 2025-09-13 04:57:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4d13aef4-4943-3410-be5a-e3e5089f0205 | -10.23579 | -48.63868 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec01ec77-8cd2-380d-9a60-8b9e09c6414a | -9.79633 | -48.90057 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 007c0131-0841-33c2-a6ae-d322516944a5 | -8.09502 | -50.19184 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f17baa5-f414-3f53-912f-3bc721744e79 | -7.41261 | -44.35929 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5931fc8-7e28-3be0-b215-4d6570b4fbdf | -7.41317 | -44.3552 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8919a1a3-81f8-39db-acbf-d45449a8fc18 | -8.42665 | -55.63564 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 912b520c-6ba9-3a8d-913b-c14ebc544acb | -9.79463 | -48.90217 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1589d42-e73f-3742-9d8d-7ae67e8dbc9c | -7.94421 | -46.90672 | 2025-09-13 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 87c46aa0-08ea-3813-b638-e44e1e030897 | -3.217 | -47.13046 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b8b99edc-b07e-3c4a-85fb-135a68430d18 | -5.14541 | -56.27478 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34daeaff-3868-3e81-a597-bd736c7d289b | -9.70168 | -47.53439 | 2025-09-13 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7684b066-ddff-38bb-86b6-4e49c436a19f | -10.34067 | -48.82246 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26456c23-f103-302f-942e-f2c2a599ec2d | -6.25342 | -43.48062 | 2025-09-13 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52fe53d0-aa20-3c22-b985-60f1421f8542 | -5.71652 | -46.44503 | 2025-09-13 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6d18963-d205-3ffb-bb45-a93837e6ab57 | -5.93277 | -46.54095 | 2025-09-13 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae6fa7bd-66c6-3859-9fe2-b45f1583abc3 | -10.33753 | -48.81274 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eadb9cff-fe74-3fa3-8bcb-306de19ab056 | -9.0063 | -45.76968 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 4df811e0-06ec-39ea-a4a7-9b2bf8ce71db | -3.80115 | -48.91534 | 2025-09-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 79abaf16-a0c4-3e9e-aaea-c43cd4895cf8 | -9.80566 | -48.89701 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b725b3e1-38a6-37cd-8e50-c3910418074e | -9.80341 | -48.90273 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49ea7e0a-7c38-3f10-8bf4-eff9850d0211 | -8.09658 | -50.17587 | 2025-09-13 04:57:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e654e776-e2aa-31c5-9170-50d99a56fd9f | -7.56572 | -42.6531 | 2025-09-13 04:57:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| be1d72ae-a49e-30ba-a774-92e7d5043c36 | -4.93494 | -55.78781 | 2025-09-13 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cae0054-0912-38e6-99fb-25b42b60dafe | -7.45586 | -44.44135 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b117d49f-2e0a-3592-a9aa-12084dd7fe21 | -9.23453 | -51.2263 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 647ed132-ceb9-3615-811b-db5a3a4c154e | -3.48387 | -50.71545 | 2025-09-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2f769d0-ab1e-38e3-aa17-13500a872c2a | -9.97756 | -51.71716 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| efb1404b-7e25-379b-be48-32e58af600de | -9.02578 | -47.07373 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01cad4e2-9521-3679-8fe4-55faac23ae43 | -2.94961 | -48.59494 | 2025-09-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6f7d247a-bae3-37d4-ac28-c88c62b315c5 | -6.11116 | -45.94507 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9fbca19b-5302-39e7-af97-a7fed27b9835 | -9.2389 | -51.22242 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 178ef52f-3d49-36cc-b0b1-93967bba61fc | -10.22927 | -48.62 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e6dd15a-6e95-32b3-a1b3-f52774ca1380 | -4.41075 | -55.10039 | 2025-09-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61d6fa33-02de-3b72-9064-ad1cf2fd04d2 | -4.54412 | -43.73324 | 2025-09-13 04:57:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7a0ef83-7682-3d8a-aeb1-8806b98abcb9 | -10.01719 | -50.3949 | 2025-09-13 04:57:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22349da9-a98a-33ba-b94d-45c8ed76a45d | -6.10622 | -45.94886 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab552c65-406b-3b32-aded-00cc9378cdc1 | -3.81537 | -52.08779 | 2025-09-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c6d60693-4ce8-3aa9-b710-d43e7b928a56 | -7.32187 | -44.60211 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3825df4a-b529-3d81-9f3c-cc57811d5e89 | -9.91726 | -51.61706 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 061fd51c-f7b4-3a8e-bf6b-f23fe2f147e1 | -9.96419 | -51.70642 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3dace9f4-27b8-335e-81fc-b8a6e5e890c2 | -9.79295 | -48.89286 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f0e9a3f-82d7-3f60-b563-218a8d5f4642 | -6.21807 | -43.33933 | 2025-09-13 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e24f3d1-6f70-3b7a-a97e-34fb3937ec15 | -3.48528 | -48.4388 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c2afe60e-113d-35b9-8537-91b425c0cc24 | -8.92305 | -46.15672 | 2025-09-13 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8266d34c-90aa-393c-8a1e-7903d3f024b0 | -10.34511 | -48.82283 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d0d867f9-0990-3633-98eb-5a483ffdff04 | -3.23625 | -46.7865 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 1fc5c135-1dd6-3788-97a1-ca7da7b97d52 | -9.05276 | -45.81958 | 2025-09-13 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7c28585-b8c7-3fe9-9798-a2e1fdc08a18 | -7.14706 | -55.78232 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| cf2def3a-3a4d-3c33-af0f-6e0dfe8e334d | -9.52044 | -54.63032 | 2025-09-13 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 34.5 |
| 8288dba7-95ca-3e79-86c0-ce4f2a8e4eb4 | -9.7226 | -48.35172 | 2025-09-13 04:57:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3d0c3f6-30e5-3216-849a-679dbe4782ff | -10.38211 | -48.57701 | 2025-09-13 04:57:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05424979-3cc4-30eb-9a4e-ac6eb464cb06 | -7.94907 | -46.90736 | 2025-09-13 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6644b684-09ff-30a8-8e08-33b043492764 | -9.72557 | -46.92243 | 2025-09-13 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 05c894db-75bd-3f82-a008-d5a427b66622 | -7.66746 | -61.16768 | 2025-09-13 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 76af1feb-a9c0-3b40-ae17-0ee08254fd24 | -7.52532 | -44.3728 | 2025-09-13 04:57:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3e18be8-f2ee-3e4c-8cbf-31401da67e4d | -9.25153 | -51.25397 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3fe85b7-ae5f-3d4e-8c76-cf60e9344b3a | -6.53884 | -49.50168 | 2025-09-13 04:57:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5dad8ac-4641-3bef-818a-ae93d4280263 | -6.15175 | -51.63523 | 2025-09-13 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 486dd076-feb6-3134-b6b3-8c4b7480693e | -9.81058 | -48.89338 | 2025-09-13 04:57:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eec8ff80-8ab1-3afa-ada2-0e45aa8060db | -6.39315 | -45.64195 | 2025-09-13 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8dc3e96-4b5e-3fc9-93f7-88f8d962c019 | -9.4173 | -43.41175 | 2025-09-13 04:57:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5e9ca52e-40c8-34a1-bf5e-5ac47c49fe5b | -3.23033 | -47.13252 | 2025-09-13 04:57:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| efc33045-4a76-35bc-9c2d-ca5c9f8ec2d6 | -3.79764 | -47.58306 | 2025-09-13 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92626f3f-df72-3eeb-8110-b2ce366a8642 | -7.26924 | -57.57561 | 2025-09-13 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 786555c0-8a9e-3245-94e6-9b6d441b775a | -9.24395 | -51.21397 | 2025-09-13 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e78567f2-ccdf-38b5-9a7b-17a9b19a3445 | -9.90779 | -51.88293 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f505c896-25a5-300f-8f43-593741e12a73 | -4.60754 | -48.78942 | 2025-09-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c743367-be98-37df-b2d1-aa5dc0956616 | -10.3413 | -48.81797 | 2025-09-13 04:57:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ff55601b-4baf-39c1-9d48-29a2bbf153ea | -10.00124 | -51.73384 | 2025-09-13 04:57:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1e9fc83-8542-3279-aeb6-82855bc443b9 | -6.12614 | -42.95472 | 2025-09-13 04:57:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f48c4425-d7d0-3152-afcb-4cd8739e33bb | -6.99008 | -43.80267 | 2025-09-13 04:57:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52e7d3ed-9229-32d7-a85d-d042273acfa6 | -5.76942 | -46.15097 | 2025-09-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README73.md)
