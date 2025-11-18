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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c78bcaa-60bd-3150-9fdd-a6645bcceb16 | -3.2516 | -50.685902 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea9abd22-e515-309f-9fad-88f2adf0f879 | -12.7245 | -45.386299 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cd87e39d-0685-35db-9012-e6406e8cd90c | -1.3242 | -49.318001 | 2025-11-18 00:11:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dee2a099-20b7-3f4b-b98b-b3ff6293235a | -4.1838 | -44.2402 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b84c35f-5f56-3d58-87ae-408c3adc1059 | -9.4091 | -48.441601 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 02752429-0ed3-3005-afdb-08bb986a0785 | -3.1947 | -45.697601 | 2025-11-18 00:11:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34b082ef-36be-3082-8b9c-71db9e770e41 | -11.5281 | -48.949299 | 2025-11-18 00:11:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c959799-c0e8-3b4d-afb3-e82601d73edb | -2.8214 | -45.4184 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 34823007-635e-35d2-8179-f1634fffd778 | -6.4313 | -43.813 | 2025-11-18 00:11:00 | METOP-B | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8917aea-8189-33dc-b614-4940d85e29da | -8.7843 | -44.385399 | 2025-11-18 00:11:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4b550163-319d-383f-939d-f3de206d8f59 | -10.6474 | -49.714199 | 2025-11-18 00:11:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fae2a440-187c-3e37-b564-ffaca604bb08 | -6.2104 | -46.884602 | 2025-11-18 00:11:00 | METOP-B | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e8fa50c0-6654-3829-8cbb-639d8eb2da1c | -5.8395 | -47.830399 | 2025-11-18 00:11:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 755787b4-18fa-3ac6-922e-441ec95529e6 | -7.6946 | -46.837002 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae22862e-a5c3-3df8-bcb6-a8ac7c92533f | -6.8263 | -46.291599 | 2025-11-18 00:11:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40bc9042-3f05-3928-a039-6bbee3fcd244 | -2.0174 | -46.936298 | 2025-11-18 00:11:00 | METOP-B | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efa53f45-16a8-3898-b519-7496b2b734d1 | -3.5194 | -50.274799 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3516e7e6-b836-3beb-902d-ebfd1d855c4a | -9.0397 | -48.539501 | 2025-11-18 00:11:00 | METOP-B | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 865c15a3-23ca-3b52-bfde-81f69cf4d3be | -11.661 | -44.721001 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8c130865-ecbb-3db4-97a9-3728042bd5d5 | -3.4727 | -55.399799 | 2025-11-18 00:11:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8adf72e0-8cee-38d4-b78c-557cc8372285 | -13.0915 | -42.959801 | 2025-11-18 00:11:00 | METOP-B | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 21d594b6-bf5a-3fd0-aba7-3a565f2d5d86 | -5.4257 | -43.047798 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9511373-4763-373f-8454-09c1b527f6eb | -5.3391 | -43.030102 | 2025-11-18 00:11:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 92ac4e16-684d-3b1e-96e1-ec857bebf05c | -0.889 | -51.987 | 2025-11-18 00:11:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 6f26be90-1502-3aa1-a7c6-2fc9f1b1325f | -2.5057 | -47.809601 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5094d45f-63e8-3c0c-9850-eae09ebed3cf | -4.1775 | -50.179501 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf8d63a1-b3ee-332a-a33e-b9f8808c7fc2 | -3.1741 | -46.590698 | 2025-11-18 00:11:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a430e437-d22a-3677-87cc-41d6202fd898 | -3.1927 | -45.688702 | 2025-11-18 00:11:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16ff52e0-3bde-3d0a-9cc0-1dab781b4e1e | -4.1693 | -50.188599 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 234a953b-65b6-34d7-9b15-c26184ab5fc1 | -9.3895 | -48.445999 | 2025-11-18 00:11:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f5bdff8-52bb-36a5-aa14-0da87d661b8e | -4.1741 | -44.2425 | 2025-11-18 00:11:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eb9965ea-d374-3d75-a535-78a2e56d1c18 | -6.4184 | -47.431499 | 2025-11-18 00:11:00 | METOP-B | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a8e1031-8ec4-3096-b188-65461609943d | -4.1841 | -45.6106 | 2025-11-18 00:11:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea320762-2d96-30f6-8ee3-a7181cf1daaf | -11.8547 | -49.2206 | 2025-11-18 00:11:00 | METOP-B | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3401a312-cb61-379c-a1a5-489ea292f983 | -2.8617 | -49.463299 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e968ca55-09da-3bd2-93a7-588887f452fe | -12.9842 | -44.1119 | 2025-11-18 00:11:00 | METOP-B | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6c0a4264-a2d9-3991-8537-ba3061303d5e | -5.42 | -43.023701 | 2025-11-18 00:11:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 09eb2eb0-3152-3af9-9c3f-db0fb967a69b | -8.865 | -47.310699 | 2025-11-18 00:11:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1840250f-10fc-3ac1-a472-7fc82acbb748 | -11.5265 | -48.942101 | 2025-11-18 00:11:00 | METOP-B | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fd378654-663b-3fd9-b588-7d4e8aff2806 | -6.7865 | -39.182201 | 2025-11-18 00:11:00 | METOP-B | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 60862dd4-16b3-3216-aff7-1d34d9a6381c | -3.1802 | -50.642899 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b93608f-9fd8-3d9a-97c0-a36b51cf8593 | -9.727 | -48.897499 | 2025-11-18 00:11:00 | METOP-B | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24a3b538-a60d-3124-af5d-b8bf9e877c9c | -10.7605 | -44.799702 | 2025-11-18 00:11:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d174d5c0-1051-3d41-b550-a10aea9d1a9f | -3.4233 | -43.4534 | 2025-11-18 00:11:00 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c68b4350-3dda-36e9-9be2-c6e444c1cba7 | -4.9653 | -44.6749 | 2025-11-18 00:11:00 | METOP-B | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8e403c3-4eb4-37ef-8bef-1ac934bb080b | -5.8297 | -47.8326 | 2025-11-18 00:11:00 | METOP-B | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| db80b372-6c25-33d9-9533-cc6cd95fef9c | -11.5183 | -48.9515 | 2025-11-18 00:11:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 481b937b-e9ac-3902-a480-a709414c0ec2 | -5.3266 | -43.759102 | 2025-11-18 00:11:00 | METOP-B | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b6e4770-3308-3639-925a-fce3714fcc8a | -3.2757 | -50.017399 | 2025-11-18 00:11:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34088a98-bf8a-3a3d-a3f1-6b60355836bf | -3.1067 | -45.717701 | 2025-11-18 00:11:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a9cbc645-56d5-3153-bca6-87084a2ae60d | -10.046 | -46.748199 | 2025-11-18 00:11:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9dbe162-e714-3fe6-ab76-c33908dbd9a3 | -12.736 | -45.391399 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b9bcc4d-75a9-3eb2-9684-2face634598f | -2.7184 | -45.1516 | 2025-11-18 00:11:00 | METOP-B | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed95122a-d926-3f98-a8b3-6541a8864869 | -12.854 | -41.480499 | 2025-11-18 00:11:00 | METOP-B | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 1d42e16e-01bd-363c-9ce0-43c8b930c9d8 | -12.2932 | -46.792301 | 2025-11-18 00:11:00 | METOP-B | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 662fad62-2016-33d0-a6bc-dfd94a9e9d8b | -7.1465 | -49.095798 | 2025-11-18 00:11:00 | METOP-B | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| a385ed70-1415-30e5-b784-5956735510bf | -1.765 | -47.1838 | 2025-11-18 00:11:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 25907465-0a58-3e02-a409-9f750d4f3700 | -3.1729 | -48.023602 | 2025-11-18 00:11:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5ccfa38-3811-358e-bce7-a75d65943698 | -5.5665 | -51.188301 | 2025-11-18 00:11:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9efc76f3-7fa5-32eb-aaa2-033fa2ea8fa8 | -2.5073 | -47.816898 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0c8b7af-4d93-31f0-bd47-a605639d0a76 | -2.9161 | -47.847198 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5abb2d4-322f-3a67-a169-2945749610a5 | -11.5167 | -48.944302 | 2025-11-18 00:11:00 | METOP-B | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4d222511-8716-341f-a487-625b8693b280 | -3.3416 | -44.379299 | 2025-11-18 00:11:00 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a8c89ef-8339-3e5e-b4da-a5ef79010e30 | -8.2054 | -45.038101 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| ee56220a-d751-376c-92be-654f31cbcda3 | -3.7599 | -50.931198 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d587601-e874-348d-93d9-8a06f3b75a97 | -4.1626 | -50.2047 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec51ae4b-0a68-33df-a906-059fa3ff6d1e | -10.85 | -44.873001 | 2025-11-18 00:11:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ecba2dc-c933-3436-b8d0-5d81201fb3ca | -3.6602 | -50.214298 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ade7dd60-6339-3e7e-a922-fa4237376b0f | -10.8482 | -44.077599 | 2025-11-18 00:11:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 471f0e70-cf20-35d7-85fa-f2aedbff50ec | -2.9907 | -45.4384 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5a8a3eb-5d1e-3c11-a699-e814d181bf8a | -2.9143 | -49.5592 | 2025-11-18 00:11:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6bffbcc6-30b5-38cd-b977-652723d066ac | -3.8914 | -49.096901 | 2025-11-18 00:11:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e389ff8-8823-3068-95ab-4e635946a0ba | -8.33 | -45.3503 | 2025-11-18 00:11:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 85b2a199-e10d-305f-81eb-c692db2f22ce | -3.9426 | -49.8689 | 2025-11-18 00:11:00 | METOP-B | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17f5da7c-5fa8-300d-b7ab-7eb97b24d056 | -12.7325 | -45.3764 | 2025-11-18 00:11:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b0db18b-8b32-329e-807c-c289721d6ea0 | -2.3408 | -55.787601 | 2025-11-18 00:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39c65180-4f40-3bc1-8566-549baad6795b | -15.4696 | -43.1744 | 2025-11-18 00:11:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| e80012b9-878f-36f3-ba4a-d69185bfacae | -8.7919 | -44.3741 | 2025-11-18 00:11:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bcaad9a1-497a-35d8-b97e-49fbe3b9a208 | -2.9243 | -47.8377 | 2025-11-18 00:11:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a89f1e46-27cb-3717-8d09-9018b2a6edca | -6.8605 | -47.066399 | 2025-11-18 00:11:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7aa82e5d-fe55-3aca-b440-f6d8a5c231d3 | -5.4479 | -40.957401 | 2025-11-18 00:11:00 | METOP-B | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb9f1a05-75df-3fa5-8bd0-39dae3eca651 | -11.5631 | -48.454399 | 2025-11-18 00:11:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fa2d01f9-8736-3ece-8d6e-dcc1c9159ae6 | -11.6903 | -44.713902 | 2025-11-18 00:11:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2fa09254-44d0-3826-aa4e-555eb853d6dd | -6.668 | -43.767899 | 2025-11-18 00:11:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e035b23b-c6bd-362c-854d-b889ff7c4929 | -6.1969 | -43.260201 | 2025-11-18 00:11:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 97600a20-032c-3eb7-816b-3c84cebc4d5c | -3.406 | -50.183701 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6581bff-ca99-3394-9da5-5fee29bedf46 | -13.7893 | -43.715698 | 2025-11-18 00:11:00 | METOP-B | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 158b56b2-27ad-3535-a962-178a33488df8 | -3.4813 | -51.569 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aca6debe-cd5a-3d00-ba23-11f219f5d338 | -4.636 | -45.515999 | 2025-11-18 00:11:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a27fd070-027c-3f06-bb31-de5fe6115451 | -12.8688 | -43.5825 | 2025-11-18 00:11:00 | METOP-B | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59e292f5-5160-3571-be4e-c6fc9a978f18 | -13.4588 | -44.021801 | 2025-11-18 00:11:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8dbee528-0523-3f6f-8625-ecb29bdc95f7 | -7.6979 | -42.175201 | 2025-11-18 00:11:00 | METOP-B | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ed79f64-9d06-3661-a064-a1e52381dd93 | -10.8402 | -44.875301 | 2025-11-18 00:11:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c6f13356-32a6-324b-bbeb-e1e2d2a6cbc8 | -4.136 | -46.337898 | 2025-11-18 00:11:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea8a66ef-9160-3ae2-b60b-07b7246684cb | -3.3321 | -51.500301 | 2025-11-18 00:11:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3324be-4671-3fbe-9eb6-6e6105f9bfa8 | -2.8192 | -45.409 | 2025-11-18 00:11:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 16010507-dff3-3ef7-8cf6-79dffbad1417 | -6.4289 | -43.802601 | 2025-11-18 00:11:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ac90d078-3069-3229-84de-defc7f5b8481 | -4.1822 | -50.200298 | 2025-11-18 00:11:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a209d8ff-042f-3674-a3a7-3f7c9d5d9bee | -9.9691 | -44.770599 | 2025-11-18 00:11:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 682527be-6e8a-3b78-9d26-40376f343754 | -3.5178 | -50.267799 | 2025-11-18 00:11:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
