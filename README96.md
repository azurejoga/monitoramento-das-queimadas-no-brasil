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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bc7b9f8e-ff47-3b7c-828a-b85347362328 | -11.8847 | -46.38688 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 211.8 |
| a8fa0c91-638f-3830-89bd-3a36de2a5dce | -11.00832 | -46.96373 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d0dbfb5b-0973-3925-b747-4889cab9602d | -13.3483 | -46.90933 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| cb8885cf-b8a4-34e9-bc05-538028a47085 | -9.70333 | -49.47281 | 2025-08-30 12:17:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 81d7041b-fd79-3f20-bf75-07451ab8d7b9 | -15.62197 | -40.1386 | 2025-08-30 12:17:00 | TERRA_M-T | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.5 |
| c93374d1-a9d7-375c-ad4f-c0a86dcd62a0 | -11.90242 | -46.38945 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 2e824a14-e543-3fe1-a827-5595d682a05b | -11.00207 | -46.94453 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 17f11078-731e-3ccb-875b-6bc2ffe169bf | -10.98597 | -50.79503 | 2025-08-30 12:17:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 567d92ef-cf57-3633-8418-bf7d2b618aef | -13.33687 | -46.92611 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 41.1 |
| a9c09fae-207e-3bc1-8784-d3833a882a32 | -11.01997 | -46.88314 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 27.8 |
| c2cca552-cfb1-3ee6-aea6-2a2afd5985de | -13.35798 | -46.98141 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 8efa32fd-5fe7-34e9-b467-fe3b28a7a282 | -12.93087 | -42.48634 | 2025-08-30 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 25.5 |
| cebec979-e47d-3422-b470-5ea415424703 | -11.94338 | -46.68579 | 2025-08-30 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b1c33516-f302-3259-a82a-6a913fe8904f | -15.84661 | -48.32325 | 2025-08-30 12:17:00 | TERRA_M-T | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 86f3ab5e-4589-3eaf-a1c6-452cce7abf60 | -11.82552 | -46.8642 | 2025-08-30 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4559ad4a-addd-360d-9192-b0671386b1a3 | -13.35944 | -46.90783 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 39.0 |
| 98e51e78-fbc6-386a-aa5e-06027e6299c6 | -15.31337 | -46.10019 | 2025-08-30 12:17:00 | TERRA_M-T | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 4bdaa490-d3c4-3796-a434-a5957f6280f4 | -13.34332 | -46.88094 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 31.8 |
| f83f9c1b-018b-39ce-854f-41d369c27f39 | -10.67289 | -48.74306 | 2025-08-30 12:17:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 35eef63d-5954-3271-85dc-8bea50cac18c | -12.66763 | -48.1706 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 697a0dc0-65b8-3759-8b94-5d16d7d054b8 | -13.52582 | -46.95705 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 36.4 |
| a4a96c21-c132-36ec-8046-2a6937f097b4 | -11.57486 | -46.35445 | 2025-08-30 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 5bf858a0-b0e9-3db0-9bfd-23ca023a4615 | -10.02869 | -48.04681 | 2025-08-30 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 52e62a34-39dc-380e-91b2-107083c42c70 | -13.51637 | -40.81881 | 2025-08-30 12:17:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 159abc90-5c14-3dbe-b8ae-021144c6fe1e | -9.70504 | -49.46157 | 2025-08-30 12:17:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7f6c9887-33fd-36fe-b283-d560f5db8ec8 | -10.02729 | -48.05633 | 2025-08-30 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 190c1f59-d04d-380a-88ea-61ca678c89c2 | -10.0322 | -48.08619 | 2025-08-30 12:17:00 | TERRA_M-T | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a9413926-3a8b-3b5d-9a21-3153e1091904 | -11.84467 | -46.79376 | 2025-08-30 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5eff8af6-f668-3437-9cce-b10f63e8c2ba | -13.32046 | -46.9145 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a71e06c2-2b19-3201-a02c-3fa92797674d | -12.94368 | -42.47324 | 2025-08-30 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 23.1 |
| 4bb87600-84be-3efe-b259-ff44562c912a | -11.94209 | -46.69476 | 2025-08-30 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 811bb1ce-cbf2-37a4-a6f2-c2318e387dfb | -11.89217 | -46.4615 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| cbf402b0-930f-3677-8fb5-ce72ee235ab2 | -13.55599 | -46.94888 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 218c2f98-c321-3dad-bf28-ebc1c0b01f98 | -11.89289 | -46.70918 | 2025-08-30 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aa6c0ce1-a0f0-3719-9656-18e4e377018c | -11.01242 | -46.87293 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 350c1fee-492f-3c8b-a928-b50cfd4fd563 | -9.69503 | -47.05257 | 2025-08-30 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 5535070b-9466-3121-8bda-92a1b1efd26b | -11.86305 | -46.47572 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 318f4d46-9840-3d69-bf31-cfcd515ceb4a | -13.5547 | -46.95791 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8e226da2-51e6-310d-a62a-2de3c2102f59 | -13.40736 | -46.95176 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 3f7e4b58-69d2-37d6-bd64-083721d3de9e | -15.44011 | -42.91002 | 2025-08-30 12:17:00 | TERRA_M-T | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2a26caf2-f06c-372c-ad2d-1961e1de7bcb | -11.72424 | -51.74207 | 2025-08-30 12:17:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 85eae06c-00f9-3370-bf27-b356ceafddf8 | -13.22342 | -44.96716 | 2025-08-30 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 500c5df7-aafa-3cc7-b388-481ac2d22494 | -11.76999 | -44.76096 | 2025-08-30 12:17:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 58f75e6c-0224-3632-9a9c-2f0063927250 | -14.04277 | -44.48993 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 84943fdf-1f22-33a7-bb48-615acef6c6b6 | -13.35217 | -46.88224 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 09243db9-4c3f-31db-9c7e-f700b335f76e | -13.51608 | -46.83546 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 28092069-f7e2-3930-b1e7-d2bdcaf36aea | -9.7128 | -47.05515 | 2025-08-30 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bc359c1d-6ccf-3fbf-b366-5386a317d602 | -13.58144 | -46.89711 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 13ca3428-517b-3096-b016-714214f56246 | -13.3541 | -47.0085 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 27.1 |
| e12318af-1621-3133-9cc7-fe77f85e29fc | -13.98358 | -41.37497 | 2025-08-30 12:17:00 | TERRA_M-T | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 4ec7d362-6318-326d-b0f9-3c2d067e74c7 | -13.34701 | -46.91837 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 2c625e25-fd47-3fb4-9bcc-f99b3c9506b6 | -12.92984 | -42.47997 | 2025-08-30 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 9a12ea2f-d480-337e-a05c-294d98ad27dc | -14.02275 | -44.56573 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 84f860c3-efc5-3941-80df-4040276a2a78 | -14.01306 | -44.56452 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 19581603-2191-35af-be13-2065595ab8fa | -10.70764 | -47.06636 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 477da44d-e873-3f02-abb2-ef3884ebb78f | -13.36921 | -47.02914 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 6100c44b-529f-32f7-9511-8d1af912e00e | -13.33189 | -46.89771 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 2f12bf6b-d0d9-3e93-ae8e-2a87280a7fbb | -9.67041 | -47.91089 | 2025-08-30 12:17:00 | TERRA_M-T | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 013546cf-6950-3ce4-b594-9fbb60d9d12a | -11.01868 | -46.89209 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| e7613682-07f3-3dc6-acc0-4ad1219ba7e5 | -10.09645 | -47.01637 | 2025-08-30 12:17:00 | TERRA_M-T | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 798b2265-735c-3355-9ad3-5082a8e75bdb | -13.36073 | -46.89878 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 23f57b1f-aba9-3bad-a30e-2d1ec3c6b591 | -11.84579 | -46.45761 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| c8705466-a0f9-35e0-b82a-d5723e1409d4 | -13.37676 | -47.03946 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 8565779b-8192-37c6-86db-a42b23fbab05 | -11.82936 | -46.44608 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 18b99c19-9e79-3deb-84b5-8bce47d24de8 | -11.58243 | -46.36472 | 2025-08-30 12:17:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 8e7a30ee-8fca-3303-a85f-fba8d8c65fcf | -11.88961 | -46.47949 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a544468b-2e9e-340c-9321-fe6ec1d28a22 | -9.71149 | -47.06414 | 2025-08-30 12:17:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5c1af09d-a37e-348c-9096-fe59e03c83ad | -10.66505 | -48.73157 | 2025-08-30 12:17:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 814721a5-b422-3b39-85ef-debe818c5454 | -10.94185 | -46.84755 | 2025-08-30 12:17:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 12b5555d-bd06-3f22-9660-b7e29c7ee46b | -13.40516 | -46.84058 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 96edc1d7-97eb-368d-b813-781a78febb66 | -17.85575 | -44.74165 | 2025-08-30 12:17:00 | TERRA_M-T | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3926d3be-d008-3df3-849e-3f236164aae2 | -12.65587 | -48.18798 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 6c768f51-eaa8-37ed-bb78-7f5f202f45fc | -12.94173 | -48.12645 | 2025-08-30 12:17:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 95987f8a-1e6c-3a4c-9e57-a97175355e9a | -16.41303 | -45.65026 | 2025-08-30 12:17:00 | TERRA_M-T | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 9e0f9710-15cc-3958-afd9-21098a207398 | -15.1129 | -48.17105 | 2025-08-30 12:17:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 419afaa8-fdfe-3f28-be3c-df49c0ea3603 | -11.89228 | -46.39715 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 496f7790-bb6f-3c76-8154-267702e0f9e0 | -13.35816 | -46.91686 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 0104f08b-10ba-3465-a9a9-74f35394821e | -11.06583 | -52.04019 | 2025-08-30 12:17:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 9b4007a2-76c4-3f0c-9776-7e34915b167b | -11.58372 | -46.35571 | 2025-08-30 12:17:00 | TERRA_M-T | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a90bfc0d-e2fe-3bef-9d75-4294c66b046f | -12.0582 | -50.62881 | 2025-08-30 12:17:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b55eaf1b-7bf4-33fa-8dd0-1a3528985e81 | -11.1096 | -43.12869 | 2025-08-30 12:17:00 | TERRA_M-T | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 972b8573-f51a-3e34-b947-99810720781b | -13.32931 | -46.91579 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 32.4 |
| c5dfe6f7-54d2-3289-a11d-752e638aa217 | -10.08178 | -48.86574 | 2025-08-30 12:17:00 | TERRA_M-T | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 09ab5ea3-21c9-3ab4-b939-d7acf1eead0e | -9.77268 | -49.89358 | 2025-08-30 12:17:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b0f38f65-ca78-3d2f-a054-5c60d25a62a9 | -13.33816 | -46.91708 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 83520dc5-8e98-3eb7-a1fd-4d18d48e7862 | -13.34571 | -46.9274 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 74b1a689-beed-30a3-8a7d-79e1bdaa1031 | -11.88332 | -46.46024 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 16af6b44-7bb0-357d-b1ef-c3786b855880 | -11.85419 | -46.47445 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 67e7abe5-405a-3dc5-a171-3f52fc3cd4ee | -14.01596 | -44.54269 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1a0a8484-9763-397e-a976-a8f3df6f9db5 | -13.44933 | -42.2662 | 2025-08-30 12:17:00 | TERRA_M-T | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| 4e88f738-81c6-364e-90a7-1f36522117db | -14.04128 | -44.50103 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 27.4 |
| e95238e2-25b1-3c8b-b371-ff0f132e6a12 | -13.36202 | -46.88975 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d82f955f-004c-346b-84b8-9ef9e77ecce6 | -9.77449 | -49.87551 | 2025-08-30 12:17:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 088544e5-e30c-3953-8c16-a3a0b492e7ed | -14.37463 | -47.85373 | 2025-08-30 12:17:00 | TERRA_M-T | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 3265374b-76d5-3d75-b427-61639bb1f58c | -11.82551 | -46.47306 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| c988cc08-28fd-3159-981b-1c6353e4e82f | -13.32802 | -46.92482 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1c291cba-a767-3d48-a8d4-a45575259743 | -14.02565 | -44.54397 | 2025-08-30 12:17:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 20273388-c0f7-3c7c-8690-993beeb859fe | -11.84718 | -46.38444 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 165c29e6-c239-3d45-b95b-986df281b9c7 | -11.85163 | -46.49243 | 2025-08-30 12:17:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 434bf6b7-6213-35ab-b7e3-3b948de512cc | -13.36331 | -46.88076 | 2025-08-30 12:17:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |


[Clique aqui para ver as próximas entradas](README97.md)
