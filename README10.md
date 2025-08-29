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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1c333969-01fc-309c-a243-6c016fc121f1 | -13.66822 | -46.88858 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 78d987ec-31df-3d2d-8c8b-514c581201cc | -7.73488 | -50.29658 | 2025-08-29 00:50:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7ba2bee3-4855-301f-931c-61ae98f36318 | -13.0264 | -56.92771 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| fbdfcfc2-122c-312a-825e-91dc9b12f151 | -6.69988 | -49.46133 | 2025-08-29 00:50:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 860de81f-5286-3c4f-ab1d-121cc7314802 | -6.94594 | -52.86333 | 2025-08-29 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 62dc2716-6096-3322-b84a-546dab486a6b | -13.62938 | -48.25053 | 2025-08-29 00:50:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 019dc7ee-2b8c-3e3b-a2f3-f8c1d0447b8a | -12.40102 | -46.44879 | 2025-08-29 00:50:00 | TERRA_M-M | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| fd36d6bd-167e-3eae-9569-4a556d65132f | -9.48799 | -45.37767 | 2025-08-29 00:50:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f112f0ef-3c47-3430-a8ce-10c3b123e4c1 | -10.02698 | -48.07689 | 2025-08-29 00:50:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| d738cef8-3dea-3496-8518-dd723fcc15c8 | -10.02858 | -51.11292 | 2025-08-29 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 56512e28-346e-349b-8379-7b97a68b4ee4 | -12.09108 | -44.73173 | 2025-08-29 00:50:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 189.9 |
| 2eb5ad0d-1622-3455-a70e-5e5c6e032e39 | -13.67082 | -46.88212 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 22.3 |
| a056fbca-d8be-3aae-93f0-a9395f7c7371 | -12.0875 | -44.70991 | 2025-08-29 00:50:00 | TERRA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 86dc38db-3d50-3665-9b21-e7d277070fe3 | -9.48146 | -45.4068 | 2025-08-29 00:50:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 18b7fbea-98bc-35c6-940f-a57736d02843 | -11.22915 | -55.0623 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 23767023-412c-3893-9eba-207fd3fbfccb | -5.69598 | -45.97985 | 2025-08-29 00:50:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 10252629-0155-3424-a073-38ddde1989c9 | -13.66434 | -46.91063 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 07cddda4-7c30-30a5-8336-b09caf5a96ca | -9.42995 | -47.63805 | 2025-08-29 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 232.7 |
| 40771006-1c73-3df4-bb17-b552c2b25d84 | -15.59864 | -48.04663 | 2025-08-29 00:50:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 53b31d4c-9bce-3ffc-8896-808ffcdc96d8 | -8.70513 | -50.36613 | 2025-08-29 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9d8a57d3-6550-3dde-b7f9-c72260f81b0c | -13.51615 | -46.86055 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 6dc01d07-5ebf-382c-aa06-5f93e8ca1f55 | -15.04373 | -48.12309 | 2025-08-29 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d34e8010-8fbb-3dc6-831c-c6b56b1fa6d1 | -5.63024 | -44.99936 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| d1f5918b-2b69-324d-bf6d-2f95d761c89c | -12.32483 | -47.05187 | 2025-08-29 00:50:00 | TERRA_M-M | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 2d2bd797-34b9-355a-a8ed-ef35bd3002dc | -13.81892 | -52.75962 | 2025-08-29 00:50:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 670f9e70-c81e-30e3-b378-85b1f98afe90 | -11.41815 | -55.18027 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 98cac8db-3dd0-34ae-9727-0de521f5c506 | -11.22892 | -55.05603 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| dea3a5b6-5b49-346f-b30e-abe032353707 | -10.84957 | -47.49969 | 2025-08-29 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b874bd7a-5ae8-362e-a9b1-0e43492be12e | -12.92941 | -56.98022 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 5db604b7-84cc-3b94-bcac-41365cdb3727 | -8.19168 | -61.36266 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| e44e2beb-3e20-383a-b3f2-76c3f62c44a2 | -9.45814 | -60.54785 | 2025-08-29 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 92c7be3c-b053-3d36-9c68-7e97a622c27a | -13.6323 | -48.2036 | 2025-08-29 00:50:00 | TERRA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 4f618160-bd53-3a14-9a9b-fb629c793a27 | -8.29342 | -61.4145 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.8 |
| af7b296d-d038-3c04-b196-fea3f0883cf3 | -5.61683 | -44.99606 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 353.8 |
| 3e708a84-2cdd-321e-b7cd-3856b52a88b2 | -13.43851 | -46.95266 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 50.4 |
| ee689b38-064c-38f5-9fec-1ecab8f76e7f | -14.33075 | -53.30156 | 2025-08-29 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 53ff32be-3e87-3c85-893b-a2c8e7b26444 | -6.70991 | -49.4598 | 2025-08-29 00:50:00 | TERRA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 7d6486cc-d627-34e0-922d-79458443ae4e | -13.44936 | -46.95132 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 2cc23857-cbf5-3bee-aeae-003c1eadd1b5 | -9.41646 | -60.58175 | 2025-08-29 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| fdd6f92e-147f-3331-baeb-b0336e2deeaf | -10.025 | -48.0638 | 2025-08-29 00:50:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 031d9d7b-e0cf-3532-85ec-ac9120c4383e | -13.18013 | -45.27336 | 2025-08-29 00:50:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 86c78d5a-8a25-325f-afab-3b91ca6df54d | -10.3822 | -57.82394 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 30.8 |
| b93b5773-abc8-3819-8b14-d01af54f9130 | -8.28786 | -61.40972 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| dac8501b-1fc4-3e7a-a825-b19802ad0b6b | -15.12477 | -48.11406 | 2025-08-29 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| eee3d362-b663-3859-aa19-76dce3702fb8 | -11.57961 | -46.28009 | 2025-08-29 00:50:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6d9b6a64-c849-3344-b8ab-c3a944bbb66e | -8.17605 | -61.36461 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| e81496b3-90b3-332e-a084-a7e091cf77aa | -12.62385 | -57.01889 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 200a76c9-b91f-3940-913c-0ec4727695fc | -10.36777 | -57.80745 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 29.8 |
| d65e3a46-4c84-31be-a7bc-3076ad62ef68 | -10.36998 | -57.82511 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 57b7ed0b-851b-3c18-ac65-d737c1730f64 | -13.55291 | -46.88243 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| acef7689-7f64-35b0-8e77-36561dbb5905 | -14.33206 | -53.31178 | 2025-08-29 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| cdf8a1b1-0088-35f3-851f-ea4346d29d62 | -11.31159 | -55.22422 | 2025-08-29 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a2907e97-b27c-3342-8211-e4b1aa9c916f | -14.35817 | -52.11095 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 47bff975-5b0b-3c1f-ac16-1d3eabbf17a1 | -8.56388 | -51.31458 | 2025-08-29 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 23bc2e47-0911-3f96-ade3-70c8d8bdfa26 | -11.33294 | -51.27908 | 2025-08-29 00:50:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d89db334-c3e1-3ed1-b191-f6ee2e39a912 | -8.18496 | -61.40178 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 91d0e298-68f6-3865-9cbc-e1e7264d2208 | -11.56801 | -46.28293 | 2025-08-29 00:50:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e998ef37-5771-3e93-9c87-e3f5d5480412 | -13.55075 | -46.86854 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 3e3c8a19-26a0-37cb-b5cd-2b0d856ef723 | -10.02729 | -51.1038 | 2025-08-29 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 29d3f98c-c781-3f23-abeb-e508613bdbe5 | -11.61343 | -47.31165 | 2025-08-29 00:50:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 7ccb3505-2907-3191-bb6d-5e7c8ea40188 | -12.06225 | -46.6313 | 2025-08-29 00:50:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| a16f6708-6cb5-3267-8ab2-6f8efd8e721a | -9.162 | -59.57664 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 097fbf14-1c5f-3e4e-9a84-82606c12c9e0 | -6.71163 | -49.47144 | 2025-08-29 00:50:00 | TERRA_M-M | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 761c55bc-d279-34e0-bd0f-3d0f49018ecd | -11.57086 | -49.51901 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 77d8b25f-9d9c-3300-b0ab-ae151889ec00 | -11.57578 | -49.51186 | 2025-08-29 00:50:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7433d2df-fcdd-31d3-ad06-944dcb90d587 | -8.55492 | -51.31585 | 2025-08-29 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 983b7db9-3359-3872-8ba4-2b623426bca7 | -7.63654 | -46.54161 | 2025-08-29 00:50:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 9369732a-e4d4-36ba-9383-4dac6740a982 | -15.12643 | -48.12507 | 2025-08-29 00:50:00 | TERRA_M-M | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| b89c597d-55bd-3ebb-b683-e8fa58c47bcd | -11.58368 | -46.38058 | 2025-08-29 00:50:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 06e8208f-7479-35d5-9574-29f598ea397b | -6.91826 | -52.85825 | 2025-08-29 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 44f23152-4cac-3747-95e6-77b1e15282a1 | -10.83875 | -47.5014 | 2025-08-29 00:50:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 64431141-afe4-393a-8052-f3de1f779c82 | -13.58776 | -46.87 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 9065425e-6b9c-3904-b22f-89ce125a0c8d | -12.90552 | -48.14387 | 2025-08-29 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 34bba91f-1475-3c0d-978f-e3e61bf81388 | -15.67593 | -52.75457 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4bcc22ec-b5ce-3348-8a7e-1d65b6454c76 | -12.03762 | -50.65403 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 32e4697f-6667-38b6-8f47-1e9de574caa7 | -7.05719 | -44.35749 | 2025-08-29 00:50:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 66acca33-5c8d-39b8-b166-c0eab754c052 | -14.29599 | -53.30239 | 2025-08-29 00:50:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 79489687-c9c3-3aeb-9bd6-4748c66826bc | -13.02131 | -56.92256 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| aac7adb2-60f6-3ba9-8dc0-f18a1da40b6c | -9.17552 | -59.45783 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 1a91d289-08a7-3f6b-b858-f26f88f28def | -9.4321 | -47.65231 | 2025-08-29 00:50:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 065fd141-5738-3f7d-b4d3-50554cf64c4c | -11.11567 | -45.11925 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 3d835c5f-db56-3a48-a1f7-0f2d73e7b9d2 | -14.90543 | -46.45489 | 2025-08-29 00:50:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 48c496ec-f5b3-3699-b572-b3864834cfe0 | -8.69869 | -50.38713 | 2025-08-29 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0044a0dc-3f24-3e30-b818-547c6f23a23f | -8.70634 | -47.87414 | 2025-08-29 00:50:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 046fa4fa-e29c-3597-b1c7-d5671650b141 | -5.61972 | -45.02798 | 2025-08-29 00:50:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 132.8 |
| 02a9ccff-bd53-3d05-b855-3d212bfd1055 | -9.15569 | -59.58311 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 370f7a49-28ec-3f73-a2b1-83011f8e5ab6 | -6.7082 | -49.44815 | 2025-08-29 00:50:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| c7506074-ee3a-3627-9662-5493492dd830 | -14.00093 | -46.35667 | 2025-08-29 00:50:00 | TERRA_M-M | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 85ae87a7-7c20-39ff-b704-ecd99c72a548 | -13.66646 | -46.92375 | 2025-08-29 00:50:00 | TERRA_M-M | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 14d5b6a3-994a-360f-b0b9-a2e6f05238fe | -9.1813 | -60.77365 | 2025-08-29 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 03061af5-204c-30c6-94d6-2e876ec0d534 | -12.70199 | -48.15317 | 2025-08-29 00:50:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a2b0d5a9-25f6-35f1-a932-e5efaaa54bdc | -6.48004 | -50.20898 | 2025-08-29 00:50:00 | TERRA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7af6e675-a8d6-3bd2-b7ae-503040a31ae2 | -8.19539 | -61.39408 | 2025-08-29 00:50:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| d07d1305-0e11-35f4-a097-c4ca5aec3b7c | -13.1955 | -45.28981 | 2025-08-29 00:50:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 538.6 |
| 0bbec46e-2239-3f23-8ed3-aa744857d019 | -10.01836 | -51.10513 | 2025-08-29 00:50:00 | TERRA_M-M | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7645e24e-5136-3003-b6e3-fa661f7894ce | -8.70655 | -50.37597 | 2025-08-29 00:50:00 | TERRA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 223e8309-b3e7-349e-92a2-7cf2dbf27981 | -6.54716 | -43.92727 | 2025-08-29 00:50:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 289.4 |
| 5f0fa81b-ff14-3a9c-a350-6d803a28ef11 | -10.45247 | -57.95462 | 2025-08-29 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1dba97af-d4fb-383c-97a0-649e9f49e98e | -8.55619 | -51.32486 | 2025-08-29 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d7ff8200-85b2-36b4-876b-ff8d87907a17 | -13.53997 | -46.87068 | 2025-08-29 00:50:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |


[Clique aqui para ver as próximas entradas](README11.md)
