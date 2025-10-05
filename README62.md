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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 626c54d3-cb5f-3004-a6ac-c020d03bd483 | -13.32122 | -47.17379 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e18a0685-3781-35d4-b522-11cad2b90379 | -15.23833 | -49.29153 | 2025-10-05 03:55:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4d06b6d-df2f-3523-8098-48a46255f07e | -10.7316 | -47.89759 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 707a1c6d-4f80-3f68-b09c-12fffd66ee16 | -13.28378 | -47.61147 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 044e37ea-50fe-3100-85e3-c893e4b9c7ff | -11.4889 | -44.9815 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c703d353-2f0d-3982-af20-fd846c1cfbb3 | -11.40611 | -43.48811 | 2025-10-05 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2983fc72-58d8-3d9c-86ef-97e160b90069 | -15.29902 | -46.31374 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dacd36c-7e11-3822-a3f5-bcd66fa2d938 | -12.90968 | -47.31378 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1e94d04-7626-395b-ad07-b85c914ef081 | -13.43896 | -47.28091 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c2e0f5e8-a9ff-318f-9aec-574b7a76fa13 | -15.35283 | -47.97417 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71240098-83f9-3410-bf1b-34dbc9f12ce4 | -15.72381 | -46.2556 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2df6c5b4-d411-3b05-bf89-132be837fdca | -17.95126 | -47.01958 | 2025-10-05 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a90efe60-b580-3939-a101-97ae63997589 | -13.73582 | -51.3073 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad431ced-2ca8-33fb-af8e-c7122700a206 | -16.3443 | -47.09783 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36ddb716-c20b-335d-af95-bd6057dc54b4 | -12.24547 | -47.83944 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8d75765f-7b62-304a-b98e-a28e3a982be0 | -11.83476 | -45.04826 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7c60e79-e182-37b5-9ac8-7bd86666a987 | -12.90072 | -47.31446 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cb51ecc6-35dc-356a-a982-d1676d9f4b64 | -13.25274 | -47.20445 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 565d4a53-e252-39d5-b8dd-f118a34056d2 | -12.59184 | -48.16594 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 55414067-3596-30e0-8c3a-25957499d0da | -15.20649 | -47.19923 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00699a83-893f-349e-86fb-fb5818532871 | -13.30151 | -48.12635 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e8cc074-43bc-3809-877b-53cb500579cc | -11.73768 | -46.82703 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37e5dc65-ae47-3a11-821b-1de59486e35d | -14.33371 | -45.85786 | 2025-10-05 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97f16457-53f0-3f1d-b5a4-699d0b40d81e | -16.00274 | -50.92534 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e68383a-2179-3f5e-89d4-e66e1264d6cd | -10.80294 | -48.82679 | 2025-10-05 03:55:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6f542de8-b3e0-32af-b4c0-886f5f6ec980 | -11.11307 | -47.1353 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4265a378-2025-30ab-8f56-0f92fdad24d9 | -11.62496 | -45.02938 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4120250a-05ae-3937-bbbb-b74483392fc3 | -14.94888 | -46.85273 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87c0c992-049b-3e6c-aa93-4757a6374062 | -16.00419 | -50.9348 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a6fba5b2-5ca9-3944-893b-075b79fb4825 | -11.83754 | -45.05666 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6720c97c-ae04-369a-bd53-087ef70cc02c | -17.01898 | -43.4525 | 2025-10-05 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e3e099b4-c285-3fa0-bde8-c21d4a2b3fe1 | -12.89929 | -47.31704 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1f319722-ccc7-3d3f-bf7a-7fbdff5152eb | -10.74189 | -47.89913 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4836689-5d7e-3b58-ba6a-0188a6bd99ef | -13.25117 | -48.49428 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08c8c5a8-0336-3434-9b83-b0847a33a9be | -16.00576 | -50.92709 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1476bb87-6918-37f5-9bef-6cd841d74ce3 | -11.23739 | -47.79272 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5a7f875-ad5e-3cab-a3c2-2a93b7c4318c | -10.49103 | -48.10711 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 908118c2-6deb-3f95-b171-07798651a28b | -14.95324 | -46.85392 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c304c19-f585-3aa8-9bde-068b3965c0d3 | -15.39618 | -47.95851 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a09fa558-774e-392e-86b4-537b9051d594 | -11.69238 | -47.4898 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5411e2f9-ff78-30b3-b471-7eb390ddd7ad | -11.50218 | -44.98755 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbe27760-c825-3032-b822-f86bc50192fd | -16.29055 | -45.24602 | 2025-10-05 03:55:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 85e2db9a-8efa-30f1-b969-7ace55966b93 | -12.10908 | -50.89796 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 54342216-4e77-3712-badb-0b7c8b959f72 | -13.08283 | -47.97227 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ec5a5dc8-b0ea-3b26-afb9-b91181ac1b94 | -10.99706 | -46.51398 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff1c70b4-7870-36ba-bd91-e4419d5808ea | -13.56212 | -44.09763 | 2025-10-05 03:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8876b434-b691-30bc-afd4-81f5a0745c00 | -14.6883 | -48.27667 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 694aec3f-c5cd-357f-93bd-642aa1436411 | -13.7436 | -47.97404 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f5bbc36-20d2-332c-960e-b61adec3732f | -12.46165 | -45.53084 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d65684c1-3e24-3518-ba4b-cfcf9fca13ed | -11.90815 | -46.2384 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35300cf3-6e83-3f1c-ab7f-d3ed9eaad8a3 | -13.64889 | -47.29372 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 305c2928-b6b5-3d5d-b626-6ef361671707 | -11.10292 | -47.76592 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64540662-cd6a-3f6e-9588-3b2bd16a15d6 | -11.11711 | -49.86562 | 2025-10-05 03:55:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b80ebf2c-756e-3fa4-965d-d4128df415d2 | -13.25974 | -47.60735 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8e428e5b-8826-347f-99a0-f32161d7ee1d | -13.83762 | -48.05024 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19178871-2522-3bb7-b43f-40e9f41f20ac | -14.9329 | -46.84011 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8370708d-b84d-3273-897c-baa3dfd33d4d | -12.45955 | -45.518 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3efaa9f5-2e51-3240-b1e0-357d39b65922 | -13.27231 | -47.61975 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dbe9f559-96ce-333c-960e-f9f68a701a0c | -14.66577 | -48.36865 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8470bee8-f3ef-3ee8-bc25-aa966ce99010 | -12.41538 | -45.15206 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aa61a96-d483-3714-875f-ef9fab287d96 | -16.36054 | -47.06032 | 2025-10-05 03:55:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 70656c01-7f1e-37c3-9d5a-e698ca9792fd | -14.59352 | -52.46552 | 2025-10-05 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d0eb063-58fd-3551-9db0-52b56703da81 | -11.51725 | -47.67552 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fa589dca-c9fd-318a-955a-6381a977d758 | -13.81135 | -48.05526 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfbaceda-8d9c-390c-b92e-6d8a569ac36d | -13.35229 | -47.20254 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8049c111-1162-3ae0-9cff-cc543914f08c | -12.45063 | -44.73742 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12de7f18-b9f1-3dbe-be32-4f20d61335ef | -11.14026 | -47.92993 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5058f278-3a5b-3822-bace-a2b1908d7d20 | -12.70001 | -45.84786 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de95d341-a6d2-31c9-8bbc-86ec656ffa53 | -11.83423 | -44.93237 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bef0d682-e864-3d0a-bc4e-abf627573691 | -11.53363 | -47.67375 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e1250103-e373-311a-b8d7-cac0ae1ca9cc | -13.29113 | -47.62541 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f5891d5-935f-396b-b9cc-6cd75925a40a | -11.09238 | -47.74329 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9aed8d78-661e-3e52-9038-b5eb7f800481 | -13.72521 | -48.08076 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ed929cbb-e1bd-349b-9e22-f2b260b631ff | -13.10406 | -47.8326 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 235f0792-f972-39aa-ac06-5da90099fa95 | -12.60461 | -48.12605 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb224568-51b6-329e-a431-daed4f2bef32 | -12.39687 | -51.10882 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e0a65a7e-9013-374d-97d1-f0b6e3ee42ba | -13.30357 | -48.09228 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 013c7cc4-01af-3be3-b29d-66b9413291b5 | -12.45814 | -45.52598 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b664bd81-df89-3454-abe9-ceb1680c0d73 | -15.366 | -47.9822 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4828fccc-7a55-3f2d-9da8-946c2b931da6 | -14.79992 | -44.89854 | 2025-10-05 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faf589c1-fa71-38ec-832b-f781b49ee069 | -11.09693 | -47.74263 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7727daf5-7431-3d6c-9a27-432f040f4a8d | -16.45135 | -42.68394 | 2025-10-05 03:55:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a100e6f-36cc-3f80-8ec7-e902df02ef93 | -13.34972 | -48.06542 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 37fa80f5-dbca-3b12-9916-742e885570c8 | -10.79754 | -48.82565 | 2025-10-05 03:55:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 62c7610b-231a-3615-a4e9-6b4ed5017cf9 | -14.02674 | -44.4614 | 2025-10-05 03:55:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df8bc227-54fe-3bdd-95ee-f834a8d98aac | -15.30156 | -47.32698 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2578baa-4924-3ee6-aeba-4a3ce301c616 | -13.26091 | -47.81565 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29ba3b6a-5185-300a-949a-964bea30e9eb | -13.11474 | -47.80267 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 100122b2-f657-3369-8840-31d0a24d7d8a | -14.32178 | -47.68149 | 2025-10-05 03:55:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 71e1781f-267d-3370-8fb6-d9045b02609d | -14.6768 | -48.25733 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4a454ba1-b1c1-304f-b9aa-f0d64e38479a | -15.37173 | -47.97786 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 73945de0-8cfa-3b5c-a162-e932190a66ef | -10.49625 | -48.10801 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c61ac5ab-78d9-3183-a1a3-60bfd095fcd4 | -11.88504 | -44.9813 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 244e656b-32eb-358d-a467-eef7492dab89 | -15.9865 | -50.91872 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e51ebfa7-d2e7-350a-8434-22deaf34c77b | -12.81516 | -50.53749 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0eab92a6-cb7e-3b7b-ae85-150e865809be | -11.57877 | -46.77329 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f067d9f-ede6-30e3-a840-9adf4408320e | -15.99131 | -50.92377 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34f4e690-e720-3eeb-b18b-c01d89d2f1d5 | -14.79304 | -44.89181 | 2025-10-05 03:55:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b481706d-14a2-3a4c-a2dd-78e85cbc501c | -13.62419 | -48.68642 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 86b17007-1ec1-31d8-a0ff-0f1c04ddedca | -15.30662 | -47.95965 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README63.md)
