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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 53dde1f8-6e15-31c4-a9db-e546749707bd | -8.44367 | -43.87162 | 2026-08-17 04:21:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e57c8755-3dfe-3618-a4c1-b685886c78ae | -14.87708 | -46.64844 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3dba9bd1-4941-3e67-863c-6bee32b69dbe | -8.52453 | -54.89002 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07628a11-2138-3919-8ad2-abf3ca45b3e7 | -8.63585 | -54.72068 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61962b89-2098-3f6e-8cf5-348ac02c56a5 | -11.71011 | -54.5924 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b280a49-4fbe-3c5e-b07c-5ad73e6fc6af | -11.71461 | -54.59629 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 371ae51f-4663-3213-bb0c-5c616e679341 | -8.63713 | -54.71373 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 668cdf76-fb32-3de0-8229-8023690ccb38 | -9.48553 | -51.67138 | 2026-08-17 04:21:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66b1356b-3c37-3971-af48-c380128a2eb1 | -12.65983 | -48.51913 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bd31ce09-6d81-32d2-85bf-04c7c8b1aea0 | -11.10261 | -47.27982 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3bcdc47-6384-3df8-bd28-06b8ce0c8b17 | -12.4657 | -46.65195 | 2026-08-17 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d563dc9e-99a3-320c-918d-36735f044731 | -12.68473 | -48.51931 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d3d11fa-e5fa-3483-943b-02023da29fe3 | -8.80318 | -45.78453 | 2026-08-17 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7aa7e562-73f7-39c9-8b48-37877ba2e9d0 | -14.87266 | -46.65501 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbec09b9-a3c2-3e4b-b629-a3bed667e839 | -11.69657 | -54.60852 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 685f275c-5cd6-3104-b9a1-786411e8e561 | -14.28848 | -53.06665 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adb26ab6-adb0-32db-807a-60dc51f41df8 | -11.82641 | -51.7746 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01d02805-dca2-3f50-9b00-5bd5abf1ee91 | -9.76081 | -47.23109 | 2026-08-17 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29ca3111-e76b-3448-b063-a420611a6504 | -10.51038 | -50.00472 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9988eddd-70a9-33b3-96b6-53c54bd3377c | -13.53152 | -46.27246 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec8494bb-78a1-309e-96ba-a76eac1f3b46 | -12.25969 | -45.90384 | 2026-08-17 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbaf6828-52f8-37ed-a3e3-ae0953f78d0a | -7.35981 | -55.48922 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4b319b94-bb58-32b0-9254-6f8e4baa1554 | -14.37756 | -51.86324 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3b1a0f8-db7f-3adb-ab7e-3aedffba9cf2 | -13.50393 | -46.2318 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00328cbe-4f27-3732-987c-168832324fd7 | -10.50716 | -50.02394 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 23d38c8e-637f-3be9-8352-45dff69ba706 | -7.37571 | -55.50039 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0e55a4ab-7bb9-3d83-b3b7-fe8ae5a132b9 | -14.90146 | -46.62319 | 2026-08-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 861fda15-0e2c-311f-97e3-6fb64c4854a4 | -14.44182 | -51.82992 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cbc20d7-c4b9-3935-80db-8eb4780e92a9 | -11.7163 | -54.61515 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92699bcb-21d6-3018-b87b-33f117dcd921 | -12.05085 | -46.45747 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dee363f2-3336-3647-83de-0056f3d4d6ba | -11.97674 | -46.4523 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9260dad2-4672-314d-a7f6-17cfc32defd2 | -15.07553 | -47.0099 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63448b82-f42d-3fba-aba9-be09a03c28d1 | -9.13004 | -46.02042 | 2026-08-17 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04d3bffc-b9fa-3fb1-9021-814916e01b02 | -10.38864 | -48.2667 | 2026-08-17 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d48b9a5-7f50-3ecd-890f-e20ee0a521e7 | -11.318 | -46.25126 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36fc9c4d-8a0e-3bc5-97ae-07a6a91526e3 | -6.11652 | -57.73424 | 2026-08-17 04:21:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 155dac0d-df7f-3a67-ae53-690348b91610 | -11.72865 | -54.60525 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a6bb455-0771-326b-8a5b-079e25adcc44 | -11.08701 | -45.15741 | 2026-08-17 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af96b043-946e-3bc6-a16d-2391b3dd3574 | -12.04033 | -46.48109 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ec22555-1b0a-34c6-8689-fb5f6364f7d3 | -8.07024 | -48.53861 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25252690-6808-38ae-9ae1-9ccc9045205e | -14.18877 | -53.06612 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1f3b36a2-d5a6-3434-a0f6-5c016a6173d1 | -7.39094 | -55.48466 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 799e5da4-b0ed-3456-8f8c-d75eb8cd2d42 | -14.28526 | -47.21152 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e5a3a2be-cce5-31c5-af68-a18130b82d7f | -6.82844 | -56.46457 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b7fc413-e5b7-34a1-8dcc-30149527e215 | -12.18262 | -45.14797 | 2026-08-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81ec1129-4b18-3571-be78-879cc8e08d81 | -14.3768 | -53.15368 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1ea75d9-e514-312a-8fed-c3d122c05032 | -7.37215 | -55.48697 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 006d5dec-85bb-39f6-80e1-867b73411920 | -11.49518 | -46.61621 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8beda986-32a0-3c0e-ae15-15187f7a2557 | -14.30915 | -47.18985 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 8abe262f-09b3-3eeb-b837-3a308368138a | -11.09293 | -47.29691 | 2026-08-17 04:21:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6881884d-a6c8-351e-85b3-8e48a1000d0b | -12.26852 | -45.91246 | 2026-08-17 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2854ea17-80f7-3c13-9b01-2ddd13e25886 | -8.37267 | -46.37923 | 2026-08-17 04:21:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b08be0fc-9ec0-3bab-ab8e-fda0d851d5fc | -14.29361 | -47.20191 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e98d1160-aa3c-3a11-a0b7-7419202cbc1e | -9.11246 | -45.93805 | 2026-08-17 04:21:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad7802fe-8bf9-3ec6-901c-f846f1c58646 | -12.65964 | -48.49893 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6769bd0-209e-36a8-a100-bad8fe64befb | -13.78191 | -53.81038 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 20302c45-1433-3c5f-b3d3-a13291b84210 | -7.06957 | -56.65931 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1288efc8-3382-39d8-9673-932c2362c2ce | -15.16166 | -50.08047 | 2026-08-17 04:21:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4eafbab-3714-3821-9b39-cf8c43e57fb9 | -14.38029 | -51.87126 | 2026-08-17 04:21:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6170ede7-a5ef-3f63-b4ac-bea5167b3003 | -11.72809 | -54.60823 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfe5a590-3ee3-33d6-b801-1db73fb0b353 | -11.7208 | -54.61914 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2718a98-bffe-3dd0-ae42-146f8ec0b6da | -8.06366 | -48.53319 | 2026-08-17 04:21:00 | NOAA-21 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2093d364-2fb6-360e-9cba-8ca8bc3b2e09 | -12.7615 | -48.43567 | 2026-08-17 04:21:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2921db62-1637-3b2d-9e2f-ec12832c6f2e | -14.2901 | -53.05788 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5c190bff-8242-3c3e-8202-43c17b12a7a7 | -11.23265 | -54.01712 | 2026-08-17 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 24145382-b084-3e60-9f9f-9d41a2662f2b | -11.13547 | -46.5249 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81afa3da-5da5-37ec-b020-c7b4b8598767 | -6.82312 | -56.45871 | 2026-08-17 04:21:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00ea20e5-c691-3d33-a634-00806d2b2648 | -11.14083 | -49.04356 | 2026-08-17 04:21:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 717706c1-7c42-30d6-9c3e-19dcc690e56f | -12.2542 | -45.91737 | 2026-08-17 04:21:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbe37038-93c1-3524-a499-822f6c47a6df | -11.82709 | -51.77075 | 2026-08-17 04:21:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25ffe798-e38e-362d-90a5-6fc22704d71f | -8.59789 | -54.70177 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08d463da-98d5-3fa5-aeb7-1680b226ecfc | -11.13107 | -46.5097 | 2026-08-17 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f6b5556b-1691-391a-83e8-2e12784981b1 | -14.49252 | -45.68184 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e64723e8-9668-3c88-9985-5bd90235b207 | -11.21221 | -54.81713 | 2026-08-17 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3732b77f-b203-3137-bc73-c65999789872 | -14.30583 | -47.1893 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5fada452-19c3-3400-8b9c-320d2fbe1036 | -11.46979 | -46.58306 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 858b4672-b003-3f2a-86ba-ab0abbd7404d | -10.49949 | -50.02261 | 2026-08-17 04:21:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49ba7cc9-c3e0-34d3-8b50-8d32823ff8d5 | -11.7298 | -54.57121 | 2026-08-17 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f31ad42-470d-346a-961b-5264d2469a95 | -12.02105 | -46.43104 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b69f0097-e593-37a0-82d4-dd76572c7a4e | -11.49359 | -46.58321 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 12a2fe6c-9e64-3482-9f2d-c1aa6bef48ca | -7.40182 | -55.48785 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 90629787-5c9f-34ff-811d-2f200797efe3 | -8.03426 | -55.1453 | 2026-08-17 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69fd8512-4ca3-3d40-a205-a3b7e1df6410 | -13.63761 | -56.99731 | 2026-08-17 04:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2e01f095-21a5-32d5-bb32-eee802b734e1 | -10.80039 | -42.74 | 2026-08-17 04:21:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5c682635-0829-3687-bd63-f783ec653ce1 | -7.39672 | -55.48566 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 89b74a00-6110-3814-b254-4aff8a0a35ed | -15.0882 | -47.01568 | 2026-08-17 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8af77fc4-c331-307e-bc7a-fa9e3dd47d4a | -11.50023 | -46.58426 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 363d332e-dd46-3830-b0da-6ee64014c12a | -9.5713 | -47.09845 | 2026-08-17 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e8d6118-7363-3440-9d6f-74f0e060b188 | -7.3714 | -55.49115 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 56c170fa-f92f-3534-bad0-1bfdc6b499d0 | -11.20241 | -54.81226 | 2026-08-17 04:21:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cdb69dfe-6735-3232-bd8f-882300c3efda | -12.02318 | -46.50369 | 2026-08-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f9b94873-9e9b-357a-b352-d5785ad62f50 | -14.47529 | -45.68277 | 2026-08-17 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a17bdbb8-90d4-32f4-9c11-19af37d7495b | -13.51991 | -46.23804 | 2026-08-17 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 49009dde-243d-37e4-a088-259d13c9fe65 | -11.70165 | -54.60939 | 2026-08-17 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| faba4fb8-e31f-3c6e-840c-ba01eb22a3c9 | -12.23816 | -47.03391 | 2026-08-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a21549ea-e436-3ed5-a873-6ceeb936877e | -14.27602 | -53.10958 | 2026-08-17 04:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3e68181b-d09b-33ab-afa8-0b9e7b244422 | -13.78746 | -53.80621 | 2026-08-17 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7a45c31-7567-348b-9c08-cbf164e5a5ed | -7.383 | -55.49304 | 2026-08-17 04:21:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 24b631d6-911c-3772-b757-2161bfdabe5d | -13.50888 | -46.22177 | 2026-08-17 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dae012fa-009e-369e-a365-022927808c47 | -11.5013 | -46.599 | 2026-08-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
