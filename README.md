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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24d4e773-4011-3e72-814a-60067d27b564 | -8.0952 | -44.0993 | 2026-05-20 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 40a8d0c3-5bd8-3d1c-b07f-09de3005ea7b | -11.6123 | -55.3283 | 2026-05-20 00:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 4974b7e7-76b0-3901-9460-f6ee087d73e3 | -12.6011 | -44.521 | 2026-05-20 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 8f5a324e-0984-3bf0-a1fa-224eca61ec6b | -8.095 | -44.1224 | 2026-05-20 00:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 57.1 |
| e42d8351-0b9d-3680-97e0-61db372166d8 | -11.6123 | -55.3283 | 2026-05-20 00:10:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| fe86f399-11d3-3cce-81e8-92e3e6a900d6 | -8.0952 | -44.0993 | 2026-05-20 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 60.4 |
| db5c09a2-2e53-3bed-9646-e115b6f8b891 | -8.095 | -44.1224 | 2026-05-20 00:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e765a59e-0de0-31d0-a91e-9f35fcc79939 | -12.6011 | -44.521 | 2026-05-20 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 1a450d6b-ff9a-3816-bbca-1a7df6483a52 | -12.6011 | -44.521 | 2026-05-20 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 8a707e31-fdca-3a8b-bc31-36f31e817e60 | -11.6123 | -55.3283 | 2026-05-20 00:20:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1592f251-85eb-3aa1-a3a7-6e425a1116d9 | -8.0952 | -44.0993 | 2026-05-20 00:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 6bb0b65d-03a2-33bb-9aeb-1ee4dabe80ad | -8.095 | -44.1224 | 2026-05-20 00:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.8 |
| 40cffd09-4a39-3380-84ac-5b769955d39e | -11.6123 | -55.3283 | 2026-05-20 00:30:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 14979b1c-6add-3459-9b33-f24b2df26b1a | -8.095 | -44.1224 | 2026-05-20 00:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 54.6 |
| cbbb6f0d-c3a2-34d3-b548-a7914c2b2ca3 | -12.6011 | -44.521 | 2026-05-20 00:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 3229855e-c551-33e3-8459-bbf088757609 | -11.7997 | -57.351898 | 2026-05-20 00:37:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee1829c0-db9d-3efb-9cfa-354042643e74 | -11.6065 | -54.186699 | 2026-05-20 00:37:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eec2c801-6f67-31d7-b67c-cc290aba5fba | -12.5969 | -44.526402 | 2026-05-20 00:37:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fe309699-4540-3cd5-a7bf-ae8cc35e35cc | -14.1576 | -52.886799 | 2026-05-20 00:37:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c878c916-ecf1-3c01-a9cb-816f2c429cbc | -9.9514 | -52.460999 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4397a84b-3a2d-36f7-9db5-f3009bc339ed | -7.6235 | -50.039902 | 2026-05-20 00:37:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc3f7da-edae-3e64-a628-728aa8867d85 | -14.1478 | -52.889198 | 2026-05-20 00:37:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4f6685a-6741-3bcd-9072-dc010ffaa691 | -14.1461 | -52.881802 | 2026-05-20 00:37:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae9581c-db0a-33ae-933e-a8c5457df1a3 | -11.6049 | -54.179699 | 2026-05-20 00:37:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 368eb397-55ee-35d1-846d-3365d7bf113e | -10.1139 | -52.405499 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f92abe38-9ae4-3822-8eaa-29169d71a1c3 | -8.7271 | -47.970901 | 2026-05-20 00:37:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 13e0fb72-981d-34f6-be19-d5ae5e1893bc | -12.457 | -54.439602 | 2026-05-20 00:37:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7091200b-5635-3204-9204-83ef25e4da2f | -8.0942 | -44.134899 | 2026-05-20 00:37:00 | METOP-B | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40dd227a-f71d-313d-a197-e60df9ded24a | -11.4531 | -55.109501 | 2026-05-20 00:37:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98931288-fe5a-3fb7-a01e-185b9f20f144 | -14.1722 | -52.860199 | 2026-05-20 00:37:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 64238c25-e686-3735-9eff-4cd2f6b00812 | -9.9695 | -52.4058 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e1e72d8f-1ef5-3d91-8c8a-233e4831b1b3 | -14.8468 | -48.527302 | 2026-05-20 00:37:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9a7561d4-70a7-30fc-b654-ff1fa25cf28f | -9.9597 | -52.408199 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c669a18b-c93e-3348-902e-a8955bba92f2 | -7.6207 | -50.028301 | 2026-05-20 00:37:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2872d765-b548-3e9a-b543-147c557c1b48 | -11.4629 | -55.1073 | 2026-05-20 00:37:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2926275e-8f2e-3149-a8d2-26f0c3ffd7d5 | -11.9131 | -43.857498 | 2026-05-20 00:37:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 78a39de5-64c0-335b-a6ca-8d74d0606a32 | -9.8949 | -52.440498 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8bf5e9-d494-347e-8df2-eaa5dd01e008 | -14.1624 | -52.862499 | 2026-05-20 00:37:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 455d1386-c2bc-3232-b3a2-1496b20c88ce | -11.4645 | -55.114201 | 2026-05-20 00:37:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1197414a-9154-3d26-b1bf-f0444c5b5681 | -11.6152 | -55.329102 | 2026-05-20 00:37:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 153a4004-8335-332a-9485-dad8c16bf694 | -9.8931 | -52.4324 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f5e9e531-661a-3fed-95a9-dd1ffa3d12b1 | -11.0391 | -49.527599 | 2026-05-20 00:37:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8f020e2f-cb27-3dac-bfbe-83d13b3249ae | -14.1559 | -52.879398 | 2026-05-20 00:37:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0210e04-ea9b-38bc-8f6d-c3ae4b545dbd | -14.1542 | -52.872101 | 2026-05-20 00:37:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 10aba69a-17df-39bd-8286-3fb14acabe42 | -12.4585 | -54.446602 | 2026-05-20 00:37:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fef7e0ac-c6eb-326d-8197-5e0cf770dbfe | -10.4825 | -49.362499 | 2026-05-20 00:37:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ddfff56-81db-3d1e-bee4-40394402f275 | -11.0057 | -53.991901 | 2026-05-20 00:37:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6aef961f-3578-3241-94f5-695e8c0ab7a1 | -8.0868 | -44.105999 | 2026-05-20 00:37:00 | METOP-B | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 153cab18-edfa-3b3b-8449-ce107d6f57fa | -11.6136 | -55.322102 | 2026-05-20 00:37:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e502b54-8266-346d-ace7-3ca6a3a26a91 | -9.8852 | -52.442799 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6fe06c-fea7-3a09-8925-0da1fb063c08 | -8.7309 | -47.986301 | 2026-05-20 00:37:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 21a56d96-cdf8-31f2-ab78-ad2a80e91afa | -12.5908 | -44.503601 | 2026-05-20 00:37:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a94dc379-b9e5-3d6c-9845-54380c82d2be | -9.8833 | -52.4347 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ad9a986-332e-3475-b093-de1ae3f9b291 | -11.798 | -57.344002 | 2026-05-20 00:37:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc08206-1d4b-336b-a7ff-3527607d0a98 | -11.6038 | -55.324299 | 2026-05-20 00:37:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ecfc138-2ddb-30ec-8846-9e3d27c42363 | -9.963 | -52.466702 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0ef88793-4549-39b5-8237-c42b2fc05f06 | -11.4794 | -52.9076 | 2026-05-20 00:37:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e63a1354-c74e-30b3-bebd-15a55cdaed53 | -11.4516 | -55.102501 | 2026-05-20 00:37:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e00aba2b-e15e-3f7f-9164-12246dc1e12e | -11.6121 | -55.315102 | 2026-05-20 00:37:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be40a184-d4de-3005-8e75-5a32c52e706f | -9.9611 | -52.458698 | 2026-05-20 00:37:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5b679a16-edd6-3d65-b670-5b0f7151f95a | -11.4696 | -52.909901 | 2026-05-20 00:37:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d8fc2107-6616-3dbb-9e1e-8529dee9472e | -12.6011 | -44.521 | 2026-05-20 00:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 86c1e1af-3bfc-3c1d-b402-d4ddbc60fad4 | -8.095 | -44.1224 | 2026-05-20 00:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d3dccd3e-d674-3594-ac68-625a398e5d5c | -11.6123 | -55.3283 | 2026-05-20 00:40:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 63992f1a-2d89-39c3-bef5-66405dd7f05a | -12.6011 | -44.521 | 2026-05-20 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| b2e7cb1e-2166-3398-9f81-4bb5245b8118 | -8.095 | -44.1224 | 2026-05-20 00:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b21db1a5-8bf1-37d2-b8da-fb5fe811294d | -11.6123 | -55.3283 | 2026-05-20 01:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c063d64d-a4b1-3b4c-9169-708d513b3d7a | -8.095 | -44.1224 | 2026-05-20 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 6829652a-5275-3cd2-9faf-928dda1147ac | -8.1138 | -44.1205 | 2026-05-20 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 3d6245ed-06fc-3fb1-b1e7-80e8ca478cdb | -8.095 | -44.1224 | 2026-05-20 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 76.0 |
| cd8f24ed-c3fe-3d7d-a530-4c404243260c | -8.095 | -44.1224 | 2026-05-20 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.1 |
| 164b893b-7945-3b22-83e6-d9d0e3784b95 | -9.6295 | -40.3392 | 2026-05-20 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 199.9 |
| e85c271e-168f-3b57-8af9-33ae0f654eb3 | -9.6104 | -40.342 | 2026-05-20 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 88.3 |
| bf48bdca-f83e-3d85-ae39-d37365692eb2 | -3.96188 | -43.12173 | 2026-05-20 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0201e96b-690a-3c3e-98b6-faadc36abdc0 | -2.87763 | -40.02113 | 2026-05-20 03:47:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e429a73a-3a4d-38f6-a6e9-e500c1a8b854 | -5.999 | -35.32837 | 2026-05-20 03:47:00 | NOAA-21 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f0d84d6d-817c-3543-935e-136ede779e51 | -3.9565 | -43.12576 | 2026-05-20 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c413eb2e-a380-3084-9b93-40e05ad26c1c | -3.9611 | -43.12652 | 2026-05-20 03:47:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 99e9897d-94bf-3d00-8e3f-76c7313a57d5 | -4.37045 | -37.8978 | 2026-05-20 03:47:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d75dfa4-e855-34ff-a315-8657dac02723 | -8.10455 | -44.126 | 2026-05-20 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7e6e283f-e547-3d47-92ba-0a16c60e8d63 | -12.22372 | -44.26081 | 2026-05-20 03:49:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04b23ccd-831b-34cb-b46f-70c22f98ac2a | -11.93164 | -46.92675 | 2026-05-20 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfc06350-829f-3ebb-a4b0-c908c989ac70 | -12.06343 | -45.28514 | 2026-05-20 03:49:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a614f9d0-a968-3163-836f-9ecca5fe198f | -12.60711 | -44.52607 | 2026-05-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e0bf6c49-71be-3944-ab7b-b2954bfd2756 | -8.70421 | -47.9146 | 2026-05-20 03:49:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 50d31a3a-2694-3f40-8a21-6e53b8319ed7 | -8.1016 | -44.11572 | 2026-05-20 03:49:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7920eb5f-056e-3b74-a851-a0083bc12acb | -13.29685 | -39.34887 | 2026-05-20 03:49:00 | NOAA-21 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 626b1727-a072-36be-801f-e35e0863a87f | -8.09865 | -44.10546 | 2026-05-20 03:49:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7d587be8-91e7-3b5c-ae71-6f5192c37424 | -5.95478 | -43.4879 | 2026-05-20 03:49:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3ecb284a-214c-3536-9c2a-b0cdb565bf32 | -11.01939 | -45.13247 | 2026-05-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa46e9bc-240e-3cab-b4bd-4802c6a2df85 | -10.48714 | -49.36814 | 2026-05-20 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f5ebd483-e90d-3960-8be6-a5f97b6b401b | -12.35288 | -45.68085 | 2026-05-20 03:49:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8aff5a3d-1b61-39d5-84d8-95cd7661ce60 | -10.49877 | -42.40906 | 2026-05-20 03:49:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3b7264d4-3f7b-386d-a193-57b226bb5d50 | -12.60352 | -44.52092 | 2026-05-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4344037b-00f8-3d94-ad37-90672ac7afe6 | -10.19198 | -36.9577 | 2026-05-20 03:49:00 | NOAA-21 | CANHOBA | SERGIPE | Brasil | 2801108 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cbb4a1d6-6cff-3157-a451-5be561978e6f | -7.40224 | -46.62238 | 2026-05-20 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e47acbd8-e4e5-3b31-885e-616d4f7cb993 | -12.44437 | -44.74935 | 2026-05-20 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 262949ac-2f8e-3dd0-a2a0-900637d49536 | -8.73341 | -47.98579 | 2026-05-20 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f24083b6-4c3b-398b-8a47-3aab22b1a774 | -12.25639 | -44.61048 | 2026-05-20 03:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3ef6b87-8d84-3062-9167-692a3fb91adc | -11.9321 | -43.86757 | 2026-05-20 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README2.md)
