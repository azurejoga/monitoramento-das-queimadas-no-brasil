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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd706f0b-83a3-33cf-ae96-221d113fda7e | -11.46009 | -45.10504 | 2025-07-16 05:06:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97865ca0-63f1-35de-9e15-aeeb892fc246 | -13.16722 | -50.77384 | 2025-07-16 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e48555a-17ae-3166-bff4-495eb98d5985 | -11.94223 | -63.84208 | 2025-07-16 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e7076b5-9c15-351d-846f-7cbb03537be7 | -10.56369 | -49.13808 | 2025-07-16 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ecc88d57-9fa1-371f-9453-918b8c85f31e | -12.48083 | -46.93552 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a04bf42-0b14-343a-ba0f-4327546b12bd | -13.01474 | -45.06759 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 1de06be2-fb65-3bf8-b69f-76eb57fc9fec | -10.89525 | -49.21489 | 2025-07-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 91caf3d1-5772-3c66-94c5-4c72cba61e29 | -10.38826 | -49.759 | 2025-07-16 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15ef0e16-6aae-38d9-b263-a8080d0a023c | -12.07274 | -43.48427 | 2025-07-16 05:06:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96321125-038a-349f-b082-49a3d67dffb1 | -13.02182 | -45.06282 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 02744098-ff27-3f1e-930b-f0c93defa185 | -10.53653 | -56.23687 | 2025-07-16 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e5412086-8330-3a69-aeaa-8e7d675d6458 | -11.47558 | -47.31635 | 2025-07-16 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b854804c-bb89-310e-8b8a-5e012b05149b | -10.05903 | -59.10853 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91cfd897-03e6-357f-9450-cc97c976431b | -11.47465 | -47.32383 | 2025-07-16 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31b3dabc-4977-33cb-b05c-d4d847b825f9 | -12.48278 | -46.91922 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f809224b-fea6-3866-b239-af2b643145d1 | -10.32413 | -49.92453 | 2025-07-16 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f31662d2-7e17-377b-b2f4-a1da1292e2a3 | -14.58793 | -48.11789 | 2025-07-16 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 959aeddb-9d51-3aeb-b9b0-a633557e2301 | -10.05359 | -59.3604 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62dbe4fc-c5fd-3550-8555-6d97c4cbdb20 | -13.02124 | -45.06841 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b1beabf2-cd58-389f-a7f9-46f23b65dda9 | -9.26938 | -56.29801 | 2025-07-16 05:06:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f38a6e2-d7b8-3aa1-a193-dd809b56fbe9 | -12.48325 | -46.92639 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e75066e8-b18a-31ec-9d16-04eda73837bb | -10.05683 | -59.10023 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1a2563c0-8e3b-3292-96bb-5268f7d2e63a | -12.47558 | -46.93065 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6359cdd4-98f8-383d-ab8f-538b5cff2eb5 | -11.87688 | -55.44849 | 2025-07-16 05:06:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 020793de-9f62-33d0-a625-e75cbd4641f1 | -11.1862 | -48.62765 | 2025-07-16 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33c95b17-b255-3929-849f-7943378bcb47 | -12.47655 | -46.92251 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80230b6a-55e5-33df-a803-4cfe5f97483b | -11.46 | -48.15926 | 2025-07-16 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2bf7b90-f6bb-33cc-87d7-710a66082767 | -13.023 | -45.05154 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 27854649-511b-38b8-9c92-85be53a2fabb | -12.48946 | -46.92309 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18e7565e-b9a3-33c9-9d8d-171d6c2f640f | -9.96535 | -64.95558 | 2025-07-16 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a69bb68b-4bef-304e-90de-e32452f5df9a | -13.15826 | -50.77258 | 2025-07-16 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ced3256-907b-3bf7-a20a-471ba7b7ba8a | -12.47509 | -46.93472 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 361ed5d9-e9a2-37cc-9acd-9fc00fbb5d7b | -12.2975 | -48.78691 | 2025-07-16 05:06:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1179efab-0c18-37da-a9b4-df39ab3bd6ac | -12.57096 | -48.88848 | 2025-07-16 05:06:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3033cbbd-ad53-33e8-ac77-a4a00aab2bf1 | -9.02534 | -59.54404 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e3dd2794-e02a-3c9c-a827-1080822c7f4d | -9.70869 | -56.18176 | 2025-07-16 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d04eb72d-5811-3d02-9592-684705ac8027 | -9.01515 | -61.22655 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ea3d5094-57c0-37b3-a8ee-783add9ccfd7 | -12.48181 | -46.92737 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8285d6db-85e4-383e-9b41-5bffb8fd6ddc | -13.01559 | -45.06002 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| e1325c49-7b62-34ed-bb56-d6675381c95a | -10.53599 | -56.24039 | 2025-07-16 05:06:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8cb1b6f5-12b3-39db-b6d1-2fbad79ab864 | -10.39287 | -49.75967 | 2025-07-16 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbf2837b-a4ad-38e0-ac98-0510e64c680b | -13.02147 | -45.06638 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 8c44db13-6d37-397a-97af-5f82306ef556 | -11.87726 | -58.71112 | 2025-07-16 05:06:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f449d98-9592-3a44-837b-cb95c5ce27d1 | -11.47144 | -47.30448 | 2025-07-16 05:06:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa09f379-2fca-3114-bb64-a86e508f1003 | -12.29242 | -48.78624 | 2025-07-16 05:06:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2a96fd93-da89-3447-b151-a81ff1f0355f | -9.66472 | -49.89024 | 2025-07-16 05:06:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ba93ae0-d063-35a5-8977-260ba2183463 | -10.27723 | -47.6151 | 2025-07-16 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18e47916-c0ef-33af-8ba1-782e22e2d7ac | -10.96393 | -49.24815 | 2025-07-16 05:06:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1cc56f9-ca23-327e-bf43-6d0ff93a2191 | -11.94141 | -63.84655 | 2025-07-16 05:06:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aaca11ae-daf0-3b2e-bb93-5b34003ec970 | -13.01532 | -45.06202 | 2025-07-16 05:06:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| de32a4ee-9b96-3629-aeda-b5979c9c8b99 | -12.47606 | -46.92658 | 2025-07-16 05:06:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa8bec10-7228-3662-afc7-5a125bc53486 | -11.2779 | -52.47204 | 2025-07-16 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c655eec4-dd57-3cf9-819b-b000dfd8c8b2 | -9.71351 | -61.29061 | 2025-07-16 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a9e7d4e-2653-3793-bb13-1bef2e7c3122 | -9.70484 | -56.18474 | 2025-07-16 05:06:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e2149cfa-430d-3bcd-abe8-70500af21e11 | -10.64561 | -44.48631 | 2025-07-16 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e96863b-b00a-31ef-8ae5-8ec2c82af40a | -9.9604 | -64.95467 | 2025-07-16 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a1f429f-6382-3180-a992-a6a09dfab389 | -13.16274 | -50.77321 | 2025-07-16 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5443bbea-5b29-3057-9258-5a478761b401 | -12.01993 | -47.77769 | 2025-07-16 05:06:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06136c2f-2aed-392c-bcd1-f6965d6ad50e | -10.65532 | -49.47724 | 2025-07-16 05:06:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19feb672-2e7a-3f13-91c0-c1366d5dd51a | -10.67563 | -56.54678 | 2025-07-16 05:06:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb015e5f-ec64-3206-9dca-ab9e5433f325 | -10.05966 | -59.10466 | 2025-07-16 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c15d588-2239-3e21-b96f-c2bf1e5c9930 | -11.94643 | -48.41843 | 2025-07-16 05:06:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ba7f19f5-7585-3f5e-a858-b862d79331e9 | -11.45958 | -48.16253 | 2025-07-16 05:06:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 119f3bfb-1a2e-34ca-9efc-33f620cb19f4 | -10.2835 | -47.62072 | 2025-07-16 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c67b14a0-1244-3730-bcd3-71def3324ee8 | -9.64934 | -63.4418 | 2025-07-16 05:06:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5822d12-8f32-3137-9150-0a4ed5433447 | -9.36204 | -58.83856 | 2025-07-16 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e41819ee-7fb1-3540-8710-83c4987a5936 | -10.32475 | -49.91982 | 2025-07-16 05:06:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 443022a9-37f8-32e2-8a8e-98e0ccb3d471 | -20.07457 | -47.64155 | 2025-07-16 05:08:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ace425c6-b42d-37d7-bd7a-c1e0111a5dba | -21.04177 | -55.99326 | 2025-07-16 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b3a2dad-dee6-3aa5-be6a-537147b3932b | -18.58364 | -52.39839 | 2025-07-16 05:08:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b2104937-111d-395b-ac8e-241771d8baf1 | -22.39978 | -49.79466 | 2025-07-16 05:08:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 68b548dc-53f1-3ace-8354-9c09863663d7 | -20.03482 | -47.38422 | 2025-07-16 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e8138ed-d82f-36f6-8468-4c02f83d9c8d | -16.08169 | -53.75027 | 2025-07-16 05:08:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e138600d-1a68-3c7c-b814-d08d4987e85e | -20.35708 | -46.55036 | 2025-07-16 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ad5f00a-90ed-37ee-abf9-aa388e1873a5 | -20.94189 | -56.59452 | 2025-07-16 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db4dfe03-89f5-35ab-9065-984508a2a1a4 | -21.96235 | -56.07482 | 2025-07-16 05:08:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cce5914d-3f6f-3aed-ae75-58cf151fd9b4 | -21.34807 | -48.62686 | 2025-07-16 05:08:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d544cb59-dd55-3c21-8eae-3bad93e52637 | -20.3522 | -46.54572 | 2025-07-16 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74e684ad-d026-3aa0-b8cf-52e46c44e41b | -21.04237 | -55.98877 | 2025-07-16 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8c1b15c-ab71-356f-905f-2c1671977c83 | -20.08053 | -47.64291 | 2025-07-16 05:08:00 | NOAA-21 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 1750d8d5-ee60-3515-9464-37c5a85c2fec | -14.42712 | -58.8964 | 2025-07-16 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff2be2be-0c32-3bb6-899c-fdc7ffc58185 | -14.48993 | -59.73484 | 2025-07-16 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2fc511e4-4f17-31a6-8893-7d3863549a0d | -20.02758 | -47.39609 | 2025-07-16 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0c48f4c5-c0d4-3e92-9c29-696208c3f6fb | -18.59616 | -52.40439 | 2025-07-16 05:08:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47fb91dc-a6ad-3edf-98d2-2049720747e0 | -15.32929 | -59.7177 | 2025-07-16 05:08:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cead12aa-a996-3e30-8801-2cb78b8e9c75 | -21.34703 | -48.62531 | 2025-07-16 05:08:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d5a28870-e49c-3133-81cb-d34cf19e1ce0 | -14.49007 | -59.73437 | 2025-07-16 05:08:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d7c7069a-55fb-3b15-b734-38f806810d3d | -20.03445 | -47.38825 | 2025-07-16 05:08:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2ffd1a2b-ae8b-34c5-a3b6-b6cd8f23fbf7 | -20.47705 | -53.67604 | 2025-07-16 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9167082-2eb8-3c32-9548-04604f7925ea | -18.65662 | -55.72349 | 2025-07-16 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 792576b8-d53a-3634-b612-74568b308519 | -15.34216 | -49.46716 | 2025-07-16 05:08:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f32ee21-79f8-373c-ac56-bd2f47d82bd5 | -17.85065 | -55.9082 | 2025-07-16 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f16ef65c-15a6-31a0-a6e3-b311ec33ca32 | -21.34661 | -48.62966 | 2025-07-16 05:08:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a507239e-3571-3e4e-8983-ec4140df1ea0 | -18.4231 | -54.55746 | 2025-07-16 05:08:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2e11b48-7b05-37c4-a359-b399f71f7015 | -18.58623 | -52.40112 | 2025-07-16 05:08:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fadcbc0-d4a2-3649-9143-158b3eab3196 | -20.93838 | -56.59395 | 2025-07-16 05:08:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c12c57c1-d85b-3f3a-afb8-8b605c7d291c | -19.47443 | -55.4515 | 2025-07-16 05:08:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d8cddb91-10d7-3760-9a03-8ca886e6802e | -20.35074 | -46.54851 | 2025-07-16 05:08:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2ef0e49-1964-301b-b3a9-e5b86ef07189 | -22.39942 | -49.79837 | 2025-07-16 05:08:00 | NOAA-21 | LUPÉRCIO | SÃO PAULO | Brasil | 3527801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f8f6661-8838-3c1b-acae-c0b9144dd8c6 | -18.59564 | -52.40878 | 2025-07-16 05:08:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
