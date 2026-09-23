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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a91956a-d154-30b7-911d-1cdd2af73483 | -3.8371 | -59.375198 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 264e9ca8-3698-3555-a79a-1a7b00f1f7a4 | -4.0438 | -56.311401 | 2026-09-23 00:36:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7ca43ca-2274-3d35-ba6d-a246c5ad92b6 | -8.5896 | -54.630699 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e97def2e-406b-3e03-84d1-e1be2bfb6ac0 | -3.3977 | -61.048698 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cff7227-be9d-343a-802a-cb6f2225feed | -4.5637 | -54.927799 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1176565-ea3a-38f3-a9e0-c1e4c9acf3f6 | -7.5642 | -57.673901 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd6c84e8-b3b2-3298-a628-75664ea2a7f8 | -3.4961 | -59.1847 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca2dadce-63cd-36bf-82d1-f867eb8f0bec | -11.6981 | -50.970901 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3f0fced-6e66-3212-92bc-72009516663d | -3.963 | -59.3396 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd307230-fe69-325f-92f5-cefbde995aa6 | -8.7957 | -60.7924 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1ff9bc4-0c15-36ea-b818-c6bd1058b838 | -5.4083 | -60.201302 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 56fd5ba2-4285-3e0e-92b7-fc8c35243386 | -4.5539 | -54.93 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 965ab82f-b139-3daf-925b-92fb57491eb0 | -4.4501 | -55.0625 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9567ee31-128e-39de-8497-60d1d756d065 | -2.9517 | -57.725399 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03aa8207-17db-3283-aa23-f8c76aef71ba | -8.4486 | -55.007599 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e088c8-b21d-3ce2-b7e7-633ec56812c6 | -11.7671 | -50.059299 | 2026-09-23 00:36:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| afbe7807-4784-3f7a-b352-d9105d191cdc | -12.847 | -50.848598 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5be34faa-73cf-3141-a12d-c86f0138ea1b | -7.0401 | -62.916801 | 2026-09-23 00:36:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 55bade0e-6838-3fad-a4bf-1ad3653b82d6 | -12.8372 | -50.851002 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ff1e42b7-0005-31aa-9e0a-3f4a07fa4ce1 | -3.6697 | -57.071701 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4145f09-878d-31eb-a440-e65a9721aaba | 1.5656 | -55.839298 | 2026-09-23 00:36:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ccacbc-ee4d-3d2c-8701-9a86b8e54f3e | -6.0188 | -57.667999 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4465f60-1707-3d1c-91a2-73bc1f822680 | -6.1322 | -57.760502 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de751116-6a28-3285-9193-a4ade31045dd | -11.4596 | -47.370399 | 2026-09-23 00:36:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 329075db-0ed9-3c68-8589-c9cf15ed043f | -8.2534 | -55.237 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2e59da7-9a68-30c7-b134-d6f1fa36b40c | -6.0782 | -57.610901 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c57a4cb1-31fd-3cd3-88a4-617751eb0054 | -6.8532 | -62.997299 | 2026-09-23 00:36:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1214772-5363-3ae3-ba3a-a1454fdddd84 | -3.5756 | -50.015598 | 2026-09-23 00:36:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 622af764-e6e2-388a-9219-c2e59200f217 | -12.1018 | -50.032902 | 2026-09-23 00:36:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b4fa8701-4c8b-3b19-ae07-a63df18fb0b5 | -9.7083 | -58.120998 | 2026-09-23 00:36:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bd77565b-0325-3ff0-b53d-34629205821d | -5.8175 | -57.7346 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bfe90a6f-0494-3f0f-aeb8-fcbd7e076565 | -11.1378 | -51.047199 | 2026-09-23 00:36:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c0c29da3-e572-3255-802b-5bd31b71416b | -10.712 | -48.709202 | 2026-09-23 00:36:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2359b32c-fb0e-3060-a3a8-a13e4f3ab59f | -8.649 | -62.472198 | 2026-09-23 00:36:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 36ace5ff-a5ee-3353-a224-7c2908f5efee | -5.2831 | -60.193001 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35af773d-0243-394d-bbdf-0be63236a655 | -3.6749 | -57.049 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab6e9977-1714-3284-9505-78c1e02e2d05 | -10.3188 | -54.253899 | 2026-09-23 00:36:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 304dd547-ecb4-3a84-b3b7-77e9d6029170 | -3.7326 | -59.413898 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bbefe1c0-9d56-3668-9648-4a9cc4188462 | -5.9819 | -57.778999 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30168c23-a1ab-33a7-8ad4-79756cd57e8b | -14.3713 | -47.235901 | 2026-09-23 00:36:00 | METOP-B | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d3b592e1-f5e3-3fe3-9ada-370d317376f9 | -12.7614 | -50.880001 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6c016b96-c634-33ca-8425-a5f8c2f98864 | -6.3608 | -58.278702 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4de5f731-a39f-3d12-a858-2fbacde25b6e | -7.609 | -50.4063 | 2026-09-23 00:36:00 | METOP-B | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88020b9e-5ec6-38ca-8288-5273bc95f0ac | -6.6219 | -57.971901 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b89ae723-55bc-3eb3-8084-db3bf3546ac4 | -8.3021 | -54.772099 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdff706f-f1f6-39a0-a8aa-480801a528ce | -2.9119 | -57.777302 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b261337e-0d83-3f11-8401-5f56fcb24958 | -7.2808 | -56.451599 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad3c8eab-d66f-38dd-9f6b-c2cedec68cc7 | -6.6143 | -59.8955 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e09415ef-fb52-39ec-9f2d-7241e4882257 | -11.3099 | -51.377899 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e502e897-8070-377f-ac1b-6d96e224638d | -3.4549 | -60.244202 | 2026-09-23 00:36:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01f82478-831e-3935-b870-a7949180795b | -11.3828 | -44.192299 | 2026-09-23 00:36:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6eeb6955-d60c-3aed-b10b-6c0ff1272bba | -3.5953 | -59.444099 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0c078678-cb1c-3a24-9332-e364909338f2 | -3.2352 | -53.945202 | 2026-09-23 00:36:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4269ec9f-c9cc-3cc1-8533-cad2557dd29c | -6.6199 | -59.921001 | 2026-09-23 00:36:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 366914aa-b3c8-3566-97cb-4483c17c99b4 | -6.7341 | -55.085201 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18a51e7a-9260-3bd7-9f53-f4e9c0c211c4 | -6.3592 | -58.2714 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 112326d1-64ac-369b-b2b8-82f4ed83fad2 | -4.2694 | -56.260899 | 2026-09-23 00:36:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff079a01-3c6e-319c-a548-1b2984055c64 | -6.0985 | -57.701698 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 177b7dd9-ec53-3930-8f6c-4cc06b749cf1 | -9.528 | -45.386501 | 2026-09-23 00:36:00 | METOP-B | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 89b82a09-efc3-3ec8-b237-000caf5c0aaa | -4.3271 | -55.426899 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a573722b-cd9f-3757-8760-0451fabff923 | -10.2522 | -50.2015 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bbe93f7a-2d65-3262-9b1b-bd423613d548 | -2.9217 | -57.775101 | 2026-09-23 00:36:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9874f27b-2ab7-3a43-84c3-a2e8333f52b4 | -5.42 | -60.207699 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1259271-8f64-3e39-9206-e1dba5ffb19b | -6.4668 | -59.971901 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6dbadc28-bd11-30ac-b31f-3138d53b4cc4 | -6.6959 | -59.940201 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 09d9119d-14e3-3384-b63a-d63fff712745 | -6.4435 | -59.959202 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93b61169-8260-3125-9cef-348a81179cd3 | -12.7809 | -50.875099 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 84bde7bc-4e3d-3d5d-bbef-11d064f95ffb | -5.8149 | -52.052601 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08545001-e238-3ccd-980b-6f5e013165b8 | -6.0855 | -57.689899 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71c48b9f-44fe-389c-8021-e825a4495e9e | -9.5536 | -47.951599 | 2026-09-23 00:36:00 | METOP-B | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 345b729a-bbf8-39cb-883c-de33d258dbbd | -7.0373 | -62.903702 | 2026-09-23 00:36:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c6763dbe-6740-3acf-979f-3836fffc32ea | -10.9073 | -53.940899 | 2026-09-23 00:36:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c6ad42f9-28de-381b-9694-e005c6b16657 | -5.2447 | -48.199501 | 2026-09-23 00:36:00 | METOP-B | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6978ab57-7f07-3bb9-af6b-c4a9c20df3f8 | -3.5826 | -59.065601 | 2026-09-23 00:36:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e43cd415-47d3-3706-bc96-6350832a05e3 | -6.4562 | -54.9977 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f79241b-4a34-36d4-b26e-9cd46f2c3e12 | -3.0528 | -61.1614 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f72bab65-992c-3082-a234-d5b1934be5cf | -6.2923 | -57.739899 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb474f5e-2dae-3a8e-84d3-96889e401041 | -6.6801 | -55.075001 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3362320b-a735-324d-b826-d1140d2b6183 | -6.5227 | -55.379398 | 2026-09-23 00:36:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73992678-4036-3879-97f5-7095cf8eb8be | -3.1863 | -60.422901 | 2026-09-23 00:36:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| adcb87a7-4021-3966-8564-fb613af25905 | -7.412 | -49.8452 | 2026-09-23 00:36:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c733c2c-a96d-3917-8ed0-ba2f4a7ddd97 | -13.0198 | -48.640701 | 2026-09-23 00:36:00 | METOP-B | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46469808-0818-3032-b84d-238884aba5c4 | -5.8852 | -52.0886 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff5959a5-f9e8-3771-bd36-203004da3b3f | -10.2648 | -50.2104 | 2026-09-23 00:36:00 | METOP-B | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b608dcd2-62dc-3647-b112-e0815a2b732b | -3.8182 | -58.8764 | 2026-09-23 00:36:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a0533eb8-2090-344c-9bc0-4105502cb527 | -6.681 | -58.562801 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d534a367-3fef-302c-8e90-2825edcc2184 | -6.1652 | -57.723801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a0a146e0-dfa1-3a25-bd4e-090b91973fac | -9.7002 | -58.130798 | 2026-09-23 00:36:00 | METOP-B | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea09d179-de06-35da-a3bf-c41b48be913a | -6.7429 | -59.451 | 2026-09-23 00:36:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27a4a015-f47b-3ebf-a6a7-33efe5625f9d | -7.1015 | -52.746799 | 2026-09-23 00:36:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f79b89a4-ac2a-3e53-b82b-b51694e51cfd | -3.7097 | -60.095402 | 2026-09-23 00:36:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 40498f8a-182d-3655-b22e-faf8d98330b5 | -6.1346 | -59.955101 | 2026-09-23 00:36:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad83ce98-caa1-3b52-b52d-56d1772aa422 | 2.7199 | -60.6702 | 2026-09-23 00:36:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e9e1a31-48c9-389b-bc37-5fc9cb780bcc | -4.5603 | -54.912998 | 2026-09-23 00:36:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 662c48c4-36c3-3100-b1f0-2ef562724f97 | -12.8297 | -50.862999 | 2026-09-23 00:36:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aada4660-d350-3ad8-a3bc-00ad9a532169 | -4.4187 | -55.466801 | 2026-09-23 00:36:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4698715e-ddae-3fe9-8d60-d29a2c03c7a9 | -6.009 | -57.6702 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 789b39ca-82bc-3278-a8aa-2de4db7e3d77 | -8.9283 | -61.4683 | 2026-09-23 00:36:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 92f962f2-ea90-3be8-97fd-146029b7d4d6 | -3.1464 | -57.674999 | 2026-09-23 00:36:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0337ad9-1a3f-35f0-9c10-a4936f2d4937 | -6.3053 | -57.751801 | 2026-09-23 00:36:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
