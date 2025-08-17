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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f1124e1-5192-30ba-9aee-663ff22d441e | -4.73694 | -43.51661 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7f1874f-98b5-3295-a518-057a04e0b5ea | -6.07214 | -44.62741 | 2025-08-17 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bc369a3-4a44-30cc-96f4-dc39ae72e6f5 | -4.91114 | -43.2531 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 248688aa-4ad1-3626-a88e-9176ac108672 | -3.97231 | -42.52896 | 2025-08-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 99606afa-67b5-3e07-88c7-b0edf81136b9 | -3.98555 | -43.24133 | 2025-08-17 04:12:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c6714cf9-865a-3f98-b9a1-0a76fe3bdfe1 | -6.08911 | -44.60788 | 2025-08-17 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cb23569-1996-3076-8578-728b4486f15e | -4.91845 | -43.2502 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| eea921dc-7237-3645-94ad-4e11a961ba78 | -4.59984 | -43.31002 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 781910ea-968a-3268-b6bd-d633c288d392 | -3.97892 | -42.52999 | 2025-08-17 04:12:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 8a8f4e00-9417-3336-92ff-eba64fa0778e | -4.9179 | -43.25365 | 2025-08-17 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ac725906-bfb6-308a-9ad6-ec1dafb85029 | -5.9199 | -43.93976 | 2025-08-17 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 920f7a9f-ffa3-30fb-9bc6-c8eb47f60351 | -4.60482 | -43.32145 | 2025-08-17 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd0e44f9-14ac-3a64-9b31-e9da6614e3a0 | -10.30868 | -54.15757 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a16fd36c-fdca-30a6-834a-38fa294db7b8 | -7.5322 | -50.52759 | 2025-08-17 04:14:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 614b2599-d9ac-3eef-a945-fd4f1158eed8 | -10.86433 | -48.47357 | 2025-08-17 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 71d59e34-c38a-357c-851f-82f1ea006d12 | -10.84053 | -45.36111 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc8e4347-8094-3fba-8c49-12a8ba0f01dc | -8.50744 | -44.73687 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2953541a-2506-3a2f-aaa6-d0cb884e766b | -10.85461 | -45.33767 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3262ae5-fe9c-3d63-90a0-14c3087dfa87 | -10.85019 | -45.21592 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9eedc1ab-0544-307d-87e9-ec2baf637974 | -10.30793 | -54.16143 | 2025-08-17 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8ee1785b-d1c6-3c31-8497-894f722af693 | -7.02673 | -44.24581 | 2025-08-17 04:14:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba8fea60-df92-3423-b7b4-b4425ca28dcb | -10.30568 | -52.55785 | 2025-08-17 04:14:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 423166be-f6c5-309c-b4e5-52569153408f | -9.20784 | -39.49902 | 2025-08-17 04:14:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 98ad522e-c57f-37c6-82b7-bd3dc5c2d97e | -10.84388 | -45.36166 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16b9ad60-bd0d-307d-97f4-a3bd61fa2cdf | -6.61547 | -43.88235 | 2025-08-17 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 21412533-da91-35b1-8b88-44523c2c1a28 | -13.4316 | -45.89631 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 044ef774-6f9a-3d0d-b052-792ee51b0c5d | -11.89481 | -50.48994 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6688e95a-a230-3a31-b7df-2aa36c6ced43 | -6.916 | -43.85174 | 2025-08-17 04:14:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c86aef5b-9617-39c9-b52c-aeb1c91fba61 | -12.142 | -47.90831 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8480e539-1d6a-367f-96dc-5b06e07e2e35 | -12.86954 | -46.07153 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14ee310c-ff99-3980-9c38-90dce84fd5cf | -12.55804 | -46.94171 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b356fba-79b6-3323-854c-18d83fcda652 | -11.35474 | -55.39169 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 41c62a73-4460-3c07-b755-f1806d29b118 | -10.83165 | -45.35228 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c148da4-6d4b-3ddf-9b2c-7e2ccd731e68 | -6.61449 | -44.46358 | 2025-08-17 04:14:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f72198d7-601c-3e66-8be2-edd1e3693620 | -10.86712 | -48.50344 | 2025-08-17 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cc22df6-6f4c-32ab-810c-fc8b18a8973e | -6.54963 | -43.03049 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 60950eef-ca11-31fc-9ab4-748d219626e7 | -8.50076 | -44.73579 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 739fdcc6-6f4d-3e6b-8d97-62f9410b5a75 | -6.46471 | -55.8973 | 2025-08-17 04:14:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91a8922f-389d-3038-aa98-6cbe14318a85 | -13.56708 | -46.98994 | 2025-08-17 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b95505ea-a189-325a-b543-0ecbf42344b1 | -6.94198 | -41.73215 | 2025-08-17 04:14:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24e5eeeb-ea07-377e-94ad-e1fe4676d4c8 | -8.50801 | -44.73332 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4d4a3da3-c6e8-315b-ad8f-3d945b1e5779 | -7.16826 | -43.41568 | 2025-08-17 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 532c1f21-d887-3886-bdec-e187d4729cb6 | -9.27368 | -44.55646 | 2025-08-17 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12d2bb3e-1114-3787-83b9-9027629f59f1 | -13.44455 | -45.87996 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ecf1b366-3be5-3d8b-a31b-c3e079de42af | -10.83499 | -45.35283 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8c95e9c-6300-37d6-80b7-53613d55a2ad | -11.35386 | -55.39605 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3b256151-dc50-3645-8991-d40367ec7330 | -10.84734 | -45.34013 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 379b3410-0982-34cf-af5d-655c4df82a23 | -6.18819 | -45.43703 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d5e65f3a-fac8-3a82-8613-5a2a5b783870 | -8.81692 | -52.0481 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbf1da73-183b-358d-93af-2201aad63071 | -8.79445 | -52.0297 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77956dac-a706-3629-87f3-e9342dfe8a26 | -7.19502 | -46.2255 | 2025-08-17 04:14:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eba1444a-f22b-31c2-b660-6e8c85be153a | -9.34877 | -40.58364 | 2025-08-17 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c939a0e6-df1d-37f6-87ab-96193695a627 | -13.43435 | -45.90049 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c6e5264-ba37-3b39-bd3e-e1da41b6a6c2 | -10.83801 | -45.31282 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42dde3a0-c01b-3aad-8e70-164c60604c3d | -10.83995 | -45.36471 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b67d0a40-d533-36f6-82b7-b4af3c1be3ec | -12.61838 | -46.91105 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99c37f46-898c-38b5-8949-90b38ea2564f | -12.14125 | -47.91276 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b6f69089-bef1-3dc3-80c5-75bcfc21a29d | -7.14485 | -44.63207 | 2025-08-17 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5d099192-df9d-313d-a29c-4a54b5cddecd | -12.11935 | -47.90926 | 2025-08-17 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d024a719-3e9d-3590-bbec-998ca740adb6 | -6.61658 | -43.87539 | 2025-08-17 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5c471e02-27fe-3431-bb66-806d99aebd65 | -6.19181 | -45.44915 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f11faf7d-4fda-3830-ad5e-d01ca3db42e0 | -11.36204 | -55.40122 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 273bb109-6325-334c-ae7c-cd1938bc5637 | -8.36146 | -41.46938 | 2025-08-17 04:14:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eac0f254-c47d-31f8-8f56-5ba6c5bb61c2 | -6.77884 | -44.35118 | 2025-08-17 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ee40bea-f74a-305a-8574-e135db9ac4ee | -6.61935 | -43.87939 | 2025-08-17 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b54e999f-0a20-3490-88ce-91a17fc665ca | -13.65207 | -45.89942 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba2e1dfe-8800-3891-ad42-f12893280862 | -10.38433 | -47.80669 | 2025-08-17 04:14:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1ed47dd-4411-3b0b-badb-0c62a7e980a0 | -8.30453 | -55.10907 | 2025-08-17 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09d62c1f-e1f7-382d-93a5-18f6e75d7e38 | -7.07818 | -44.9392 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7844b026-8a12-3e3f-a3f8-374f2c43c20c | -13.42884 | -45.89214 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3c83e13-cf9e-3381-96bf-c0ae6cf69f97 | -12.45369 | -47.0012 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bc8221d-9772-3bba-88d1-d5fbd4e958e7 | -12.82193 | -45.99229 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aba55555-61ed-3bca-beec-d974b095c5b1 | -12.81916 | -45.9881 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f1a8212-d7be-3be5-b000-9df76bde2b35 | -7.62223 | -44.95933 | 2025-08-17 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf260e33-ab69-3078-bb8b-f17e1a12e07a | -10.84226 | -45.35034 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b37c91e-c025-36b1-9f31-992931c53565 | -7.15404 | -44.38199 | 2025-08-17 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9449679-e786-3807-8459-be3c32e47fdf | -6.19389 | -45.44591 | 2025-08-17 04:14:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2d10711-ce52-3f04-b0b9-016f4fce6c49 | -7.16772 | -43.41914 | 2025-08-17 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0fddb5a7-404f-36cf-8188-108b04b2a8ab | -13.0177 | -42.32488 | 2025-08-17 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 1f7fbc48-352b-38e3-b8f6-4e2ce63826b3 | -12.85907 | -46.05099 | 2025-08-17 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6001fd0f-ebef-3210-8f28-cded72eeba7e | -6.54741 | -43.02306 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d23e4448-9318-338f-a7ca-8c16dc6802bc | -10.85634 | -45.32691 | 2025-08-17 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a890ebb1-d788-3be0-ab79-97976eb2e2bf | -6.55072 | -43.02358 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 56ed4d9f-31d2-3592-8c27-c30189d1d43b | -10.87638 | -48.49534 | 2025-08-17 04:14:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 19e69838-78ed-3d47-a681-a94ed6e82093 | -13.43711 | -45.90467 | 2025-08-17 04:14:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1081e3da-3754-32c4-be96-752290ad1963 | -8.31155 | -47.61355 | 2025-08-17 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c6e75dc6-aa87-37dd-883a-88e9643ba3d8 | -12.19084 | -47.23214 | 2025-08-17 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b0a4a39-6380-3805-9dcb-3718bd16ed9d | -6.54247 | -43.03292 | 2025-08-17 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 08e3acdd-7e1d-385a-ae38-1e5f3d17e17b | -8.74814 | -44.03795 | 2025-08-17 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ce3b6c45-abd8-32a5-b249-0ae37784f0b4 | -11.09214 | -44.80818 | 2025-08-17 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4844d6be-7ff4-30d1-8073-e4a8785b0068 | -8.80095 | -52.07935 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52417fd0-d62a-371c-9b92-bc131b1e362c | -11.36034 | -55.40999 | 2025-08-17 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fbd21e7b-8a63-3049-9850-f3f3243f884c | -10.09977 | -46.91915 | 2025-08-17 04:14:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58ad9a56-b12f-3314-8bb8-eb752a974b04 | -9.76624 | -48.75331 | 2025-08-17 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4a3defda-ae50-318b-918d-dd1f6d404b6c | -12.35999 | -44.43794 | 2025-08-17 04:14:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ac74e92b-c4dd-3a6a-ad7f-ee4f992d1e41 | -10.6986 | -45.18363 | 2025-08-17 04:14:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a90d693-a552-3050-b743-a2037fb6f164 | -8.74483 | -44.03742 | 2025-08-17 04:14:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dffdfab1-0ae4-3989-a140-763ea2b353e8 | -8.50524 | -44.72922 | 2025-08-17 04:14:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b809e7f3-7779-3200-bfe5-e40bfad72de0 | -10.96365 | -49.56866 | 2025-08-17 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab58044a-5b8c-3aef-82a3-a1ec584d173d | -12.54411 | -46.93969 | 2025-08-17 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README17.md)
