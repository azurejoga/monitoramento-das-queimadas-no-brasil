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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ecdaa9d-9de6-3145-abc6-549baace8af2 | -14.45809 | -47.92987 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3208faf-c8c8-36fe-9787-ae050ec2ea63 | -13.54484 | -47.569 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 368d35d8-674d-3856-b5bf-5372255eaa5b | -11.81246 | -57.93967 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71b9aa67-fa8f-33b2-a4c3-2c50bec16502 | -13.65518 | -48.18305 | 2025-10-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69587b1d-13cf-3f86-bfee-a600294e0818 | -12.84057 | -48.64005 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a861b4e-830e-3947-b452-324873f900e5 | -12.24918 | -47.28941 | 2025-10-25 05:12:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d7a42c6-7319-30e1-9927-5998b7287b72 | -13.87539 | -48.38221 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63d47d31-1de1-31a1-9cff-9f4aa2e5c6d4 | -14.47604 | -47.89651 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c035b6f3-36e8-3862-915e-3ebb1169aa28 | -12.04304 | -54.24031 | 2025-10-25 05:12:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27379e8a-2264-3d53-97ca-6248f2a8fd71 | -13.33466 | -47.94722 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17856c46-0080-33e7-91d3-4334295afdf7 | -15.4739 | -50.46491 | 2025-10-25 05:12:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d1f9c13-5a9b-3a61-af68-e1312626544d | -11.5583 | -54.51641 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83a7591c-4379-351c-ba70-5a20a2aaeccb | -10.45442 | -58.09861 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a2fa74b3-55c3-3f7a-bd63-3029b5889b13 | -14.84442 | -52.44282 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d5d5793-6b79-3161-b6ba-f73911c4fb0b | -14.17626 | -47.31604 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| de316403-b54a-3dbc-90ee-00923fc66406 | -15.94716 | -56.11776 | 2025-10-25 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b8fbdda4-ad3f-3026-8c63-0f787f80d141 | -14.86574 | -48.10207 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 67bc3067-a5fb-3b03-b83a-0c84cb111a0a | -12.90105 | -48.59088 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3765783d-06f9-3ca1-b9c1-39f14984506a | -14.56273 | -54.17778 | 2025-10-25 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 57762297-28e8-365e-809f-0c187f594b54 | -13.04417 | -47.20861 | 2025-10-25 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 26c4d12d-6c04-3383-96ac-bc3f5be7efa0 | -14.8913 | -57.84845 | 2025-10-25 05:12:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 185cd93d-5e81-30d9-a561-72691ea0bdb8 | -12.47864 | -61.05598 | 2025-10-25 05:12:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64a5231c-bb87-3c6c-ba61-64329212dd75 | -14.9046 | -52.45684 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da8d30d0-8dd1-3fe6-884d-044afb11967f | -14.86795 | -48.08117 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cc528e4b-157f-32c8-a863-3cb61ff96724 | -15.84109 | -57.8636 | 2025-10-25 05:12:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| c2eb21da-f9e6-3364-8f51-e1dde253c783 | -14.87303 | -48.09047 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a270da77-9895-3478-911c-894af9e892a5 | -13.06208 | -50.29041 | 2025-10-25 05:12:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64e74f11-7e45-398b-8b9c-a8df09af820d | -14.93874 | -48.12935 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3e8e873e-357e-3d26-b746-b96c032d6a0f | -15.24357 | -47.93812 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1607db1-64eb-39ef-91aa-dda63c18ef96 | -14.87173 | -48.10269 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2338071c-14f2-3a31-be64-e77f75cd55e3 | -14.20459 | -47.30114 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5cdf3ea-18a1-3a8f-9056-edbc8a0c021d | -14.5632 | -54.17428 | 2025-10-25 05:12:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cf84ff7-f2eb-3229-ba28-91787e088f2d | -14.91025 | -52.44818 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d4a0c2-da1c-37ca-a5f7-5ffa08c6d977 | -14.45859 | -47.92542 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ff3f4635-32c2-3d90-9537-163c082f3f39 | -15.31168 | -53.02757 | 2025-10-25 05:12:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9319e95-02a9-34d5-97cc-86ba3bbbe39a | -13.04352 | -47.20612 | 2025-10-25 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 78c934f2-be51-381a-a876-678f7fcbd63a | -14.86373 | -48.09459 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 7467700a-ea5f-369d-b28c-ceec0289878b | -12.12934 | -46.71274 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b0133b9a-5d11-348b-821b-470ae085626b | -13.26242 | -50.36014 | 2025-10-25 05:12:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b7ccaf4-6ac2-3ee9-b561-2b2f651b1fc5 | -15.63082 | -55.84241 | 2025-10-25 05:12:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6d15ca6-e038-3767-af68-38811b445e9c | -11.81082 | -57.95023 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cecce14-7017-3f8c-94fe-c05cbddc5e4e | -16.21971 | -46.48984 | 2025-10-25 05:12:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b4075608-b305-3f74-8a8d-6b71cf1a2805 | -11.27316 | -54.2677 | 2025-10-25 05:12:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46acca98-89f5-3436-b421-a7d053f64188 | -13.44366 | -47.5282 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a39ce6c1-8e5d-32dc-91a3-022eed8b1fd9 | -12.87376 | -48.60197 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95326f3a-8b16-3c79-a806-818e75f6f059 | -10.62 | -67.93086 | 2025-10-25 05:12:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c801bbc-d939-3b48-9f24-9be3e00be855 | -14.91924 | -52.44926 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7721ff6-b5e0-3d57-a2e8-f08b179f737a | -14.48148 | -47.90281 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7531039e-dda7-3bdc-acb7-4a77fe4bcab1 | -13.33512 | -47.94315 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d5300fe-6a98-34f1-9214-fdfbb418dc94 | -12.12302 | -46.71205 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 953a9e2e-df3d-3db9-b7f7-3c434aeef6ae | -13.72803 | -48.37807 | 2025-10-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9f6bdb1-21d5-3944-8846-6afb2e31535d | -14.43927 | -48.07018 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10a9c7e3-40ec-31e1-b84c-87580c8a1752 | -13.92016 | -48.40293 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a2d3c17e-0ac6-3c41-98d8-aea3f45fe871 | -14.8726 | -48.09454 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 81aabd4e-ae38-31ae-bbea-796a274fb9db | -15.94414 | -56.11286 | 2025-10-25 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bf8ce344-caf7-308e-868e-378061aa4ed3 | -12.38662 | -49.94814 | 2025-10-25 05:12:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f83fb952-b902-3c87-a6c0-7828b4d1a5d2 | -13.88568 | -49.04887 | 2025-10-25 05:12:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c4981dc8-18db-3efd-b29f-11d999ae32a3 | -15.94353 | -56.11722 | 2025-10-25 05:12:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 11ac359f-f10a-35f9-a4e0-24ef8d2080ae | -14.44177 | -48.07361 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4af6893-bace-34e3-be88-1e6a4df25b88 | -13.62749 | -47.613 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 769492a5-d44c-33a6-98fc-4e5e7ca134a1 | -13.63386 | -47.61119 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca96d205-5029-368c-b4ce-c86e01aaecc8 | -13.03588 | -47.39051 | 2025-10-25 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c77618d9-c2ef-3c4f-8b15-1e28107c713d | -14.38469 | -51.52837 | 2025-10-25 05:12:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3b6cfa96-9f78-36c9-b744-a59cf25e47d7 | -13.90132 | -48.41364 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fe6aef2-9e11-3b48-87de-d3ce0fa016bb | -15.00035 | -49.98826 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6340ef0-9a79-32af-9501-70a078cc2290 | -14.20394 | -47.30701 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fbeecd9-38ef-3db4-960b-6b454cb99137 | -13.54659 | -47.56461 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50b4b077-6fe7-33b9-b1a4-00c34a6b4841 | -13.04969 | -47.20714 | 2025-10-25 05:12:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 248cd526-91eb-3f6e-a0ed-09c910230236 | -14.93356 | -48.51952 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5050675e-aa40-3c8b-8495-8d6b16b14bfd | -14.86841 | -48.07679 | 2025-10-25 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1bd1974-d2b6-320f-84a6-881b472f09e8 | -11.57138 | -51.47413 | 2025-10-25 05:12:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de882220-52b3-32a8-bd4b-b90857d1662a | -11.08814 | -55.92096 | 2025-10-25 05:12:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 715c4ecf-129f-3949-84d3-38dc6625a91b | -12.8798 | -48.59948 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e67d7c22-b984-3ab0-b22a-196ae87d6e99 | -15.237 | -47.94207 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d101440d-e817-339b-84a8-f7328b1864e9 | -13.87477 | -48.38354 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79269801-d5a0-3a0e-9cf0-3b0d4cb79e19 | -14.9355 | -48.12907 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b218825e-caf1-3f55-aa38-3588c82c8d07 | -10.55502 | -56.80817 | 2025-10-25 05:12:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a267602a-f777-3e8a-9597-4c67b561e8ea | -13.33696 | -47.92706 | 2025-10-25 05:12:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10500d7d-9b06-37cc-8b2e-3e0f2d1e6c78 | -15.23792 | -47.93338 | 2025-10-25 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a7d7cad2-c1f0-34a4-beb9-7011da458214 | -12.83982 | -48.64635 | 2025-10-25 05:12:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ebfbc169-695b-3246-838f-15be2ef3d976 | -12.12631 | -46.71433 | 2025-10-25 05:12:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c619935c-d00e-3c25-b3a2-2b61b294d063 | -11.98089 | -58.0606 | 2025-10-25 05:12:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 283aa931-0d95-3197-8d5e-9dde986dcfc8 | -13.90664 | -48.41856 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d516c04d-a240-33b4-9eab-aeb821dd0cfd | -11.37381 | -55.22519 | 2025-10-25 05:12:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d94534a-0200-31b7-82b0-13a00b4e13b7 | -14.56866 | -49.84393 | 2025-10-25 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eefc0b75-71c0-3c1c-85cc-15a3940c05c7 | -13.65011 | -48.1824 | 2025-10-25 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32a03a65-2076-33f1-b7b5-0dce84462117 | -11.36145 | -54.32583 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3614b88-c9c7-3dbd-99f5-dfd40e24b207 | -13.88496 | -48.40218 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 054f58f7-e429-359f-ba98-8ee3e83945d8 | -14.19637 | -47.30463 | 2025-10-25 05:12:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f32640ae-00f8-3e2c-8d82-c3c36a487334 | -14.86664 | -48.09354 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4e93ee80-df87-3e59-9a13-41616b99df7c | -13.88451 | -48.40617 | 2025-10-25 05:12:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 306b2178-afa4-3318-9a9c-4fae707214a0 | -14.86708 | -48.0894 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2d93a53-7dc7-3751-b5da-e2cdc8cd04b4 | -9.73817 | -64.66082 | 2025-10-25 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed4c0f2f-3dbe-3cdb-90a1-26c76a79474d | -14.91083 | -52.44352 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7119b44-0202-3f85-8412-4623e12d2e19 | -11.32614 | -53.93829 | 2025-10-25 05:12:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e19c73ab-6ab9-3a52-bbc3-65244fccd21e | -13.88465 | -49.05042 | 2025-10-25 05:12:00 | NOAA-21 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f7b76f08-35a5-3e15-bdb2-1766346f0d64 | -14.89227 | -52.44591 | 2025-10-25 05:12:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f2d64e1d-685a-3eeb-9dd5-c59508f41a38 | -14.87848 | -48.09632 | 2025-10-25 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f8e1112f-6913-3168-8d20-19469a50f747 | -10.63831 | -59.45139 | 2025-10-25 05:12:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 391b844c-14f8-3ab9-8fd9-0b77edaefcb7 | -10.61931 | -67.93457 | 2025-10-25 05:12:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README57.md)
