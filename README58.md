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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a93891e-5130-3d6e-982d-f0a563ff472d | -10.06339 | -62.45264 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 603a6bad-e391-3a5b-8e41-3a56e5b7f29d | -14.20899 | -60.20235 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c0d3f75d-9968-30c2-a8d7-2d9642f5a656 | -14.47831 | -45.67485 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 6a044adb-9ebe-3757-a368-bff791dc11ce | -13.51112 | -46.25475 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29b44ee3-8640-38ee-aa55-ee8edcb10043 | -16.22847 | -49.70867 | 2026-08-17 05:18:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f708c106-d88a-3d52-b06c-a652425411f5 | -12.04112 | -46.47929 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dd8a6339-19da-3949-ac4f-515405867f02 | -11.47593 | -46.57462 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 394aa976-6be8-3a3d-887d-ae29ae94c9c2 | -13.78608 | -53.79882 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74f3d759-6e96-3e78-8d45-094b3189fe86 | -14.68689 | -57.19451 | 2026-08-17 05:18:00 | NOAA-20 | NOVA OLÍMPIA | MATO GROSSO | Brasil | 5106232 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| eee528be-08c4-3e68-984e-afb11d124053 | -11.70534 | -54.62189 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44337319-b2e5-3b7c-9b04-f377649c5e2b | -13.46745 | -51.80127 | 2026-08-17 05:18:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75b7ad24-e3ca-35aa-8af2-234308dee9c1 | -12.00289 | -46.47138 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 47b69b5f-5600-3789-85cf-bd8713f42479 | -11.72665 | -54.6034 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aea76974-c632-3bb3-8925-a8ac2128be87 | -13.5118 | -46.22236 | 2026-08-17 05:18:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdbcc042-43bd-3f79-91cf-a46f9ddf764c | -13.4273 | -57.0594 | 2026-08-17 05:18:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68080724-a678-3517-a09c-812316f2121f | -10.05961 | -62.45198 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3a5eb76-fa2c-35c4-98cb-b5839cf906c9 | -13.50291 | -46.24143 | 2026-08-17 05:18:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 49a63b07-b3fb-3cc2-bd22-a417810f05e5 | -14.49745 | -59.33205 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ca0c74f-fc40-3118-9bea-34309021bbca | -11.46914 | -46.58796 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 082451f3-9770-3fd9-b548-2784ec0407fa | -15.92654 | -56.48652 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0088509d-80ee-396d-8804-28a21441d892 | -14.29978 | -47.20326 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c9cc0e98-062a-3471-bdde-fd62ea1ced0e | -11.71813 | -54.6142 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2bfce18-b10a-3279-834e-2cc5086cee34 | -9.5954 | -60.50175 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a76b5c21-8f74-3392-b562-574abcf6c126 | -16.17758 | -55.95588 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 74433d06-f96e-3e0e-aada-5f2793895451 | -16.7464 | -49.37169 | 2026-08-17 05:18:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 65d4bae6-f116-349c-9be9-9e1eb86444f7 | -15.90602 | -56.47458 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ccd28c7a-7f5e-3615-98b1-3621d20a4431 | -15.90451 | -55.53943 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| a8409b14-e295-37f3-b14c-e8940be963e5 | -14.41631 | -53.06901 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a38e8940-b9dc-34e3-ad72-5376435a03e6 | -15.77343 | -56.03783 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 296c1211-f0b4-330c-97e1-33d07561860b | -15.90521 | -55.53446 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3fcda0f0-99e0-33bb-aaef-6f4f17961c80 | -14.48533 | -45.67557 | 2026-08-17 05:18:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 577b4406-ca18-394a-90a7-a621ae269616 | -11.80832 | -44.81382 | 2026-08-17 05:18:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 365c0a6a-c636-390a-99b1-281ecd915239 | -11.88095 | -50.22817 | 2026-08-17 05:18:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2e49aa4a-a65f-3527-ad79-c8ae3ec2f1a7 | -15.16659 | -48.65166 | 2026-08-17 05:18:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c8b7dd7-14ba-38e4-95b5-897385cf7a6a | -11.72532 | -54.61296 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8f3edc1-441c-3fe4-8154-d9a3e11b352e | -14.31612 | -53.04852 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dd15091-ed02-3f41-9aaf-fe58d587cb89 | -11.21022 | -54.81425 | 2026-08-17 05:18:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 896c92a3-1b01-3069-9d60-bf5c2353913e | -14.03124 | -53.62391 | 2026-08-17 05:18:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f0df180-43a6-337c-9466-00ef6cf6f775 | -15.8597 | -56.32694 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91b8101a-5f6a-3477-aa4a-15e1cea3ac99 | -12.71237 | -48.47415 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6478f303-372d-3df1-aa23-5a084e7bf789 | -13.63666 | -56.99214 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b61b9ef-96e4-36ef-8ae1-cf85412ea013 | -15.82984 | -54.20955 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a090880c-eaa2-3a30-8e2d-d856554a892f | -11.83809 | -51.7742 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02f08995-8f4a-31ad-9de3-4a0e34309cee | -14.30691 | -53.11027 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3374cb81-ac6d-3231-8def-773647bc4f46 | -16.29867 | -53.18169 | 2026-08-17 05:18:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58e4da19-b68c-36bf-abca-9105afd46a49 | -14.30105 | -53.08791 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e432c08e-1034-3d45-85c4-a92ed0f2e413 | -11.71952 | -54.6047 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0bf168c1-e8c7-34a5-a54a-bc0b1709149e | -16.22441 | -49.70867 | 2026-08-17 05:18:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bbb224b-62b8-3801-90c2-f6b86f2835cb | -12.73166 | -48.46082 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ae2ccd7-32c8-3831-978f-03993a4cdd6c | -11.21207 | -54.0202 | 2026-08-17 05:18:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0634992-ea6f-3e91-b7bc-76883a2b2833 | -12.04041 | -46.48952 | 2026-08-17 05:18:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d126d032-9375-3099-b2a4-8efb117b6b57 | -15.91218 | -55.54018 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d419ca6d-87f7-3efe-a01a-42d7c6fdd064 | -10.94364 | -57.14571 | 2026-08-17 05:18:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7df5595b-545e-30cc-8cc2-0cee87d381c0 | -13.63608 | -56.99599 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 449f973d-a902-3612-aa2f-8dd492a6ba5c | -11.14175 | -49.04079 | 2026-08-17 05:18:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4c1eb2e-5b40-341d-92e8-8c8b43006f83 | -15.82053 | -54.21634 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 38744f75-08ef-3fef-94af-30d1283d070f | -11.72021 | -54.59992 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a339eff-5827-3997-86e0-9f7817132f5f | -11.32146 | -47.01245 | 2026-08-17 05:18:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25a99dd4-e431-34ca-b802-3aba17bcafa2 | -14.86955 | -46.65327 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ca5e3683-03a5-3705-bd3d-558e057dc561 | -14.4465 | -51.83657 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 11f7422d-8f53-376c-9f99-c6b3f24e4ea4 | -14.50132 | -59.32904 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bbe8587c-9a32-3d8b-bc68-a2684a83a28a | -9.73697 | -60.74659 | 2026-08-17 05:18:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f93e64f-d545-361a-8081-70bf52cf8108 | -11.7164 | -54.59936 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a0e7d8-7e89-3150-93f2-9dcd5983e454 | -11.71051 | -54.61307 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9375bfb-a893-3ae2-bcf1-07a3e74877ee | -10.3179 | -59.14471 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91fa8ba4-ccfe-3708-af8c-29b089fd9b8c | -13.51986 | -46.23606 | 2026-08-17 05:18:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 734bfe3c-c3e5-37c6-9480-d42fb64215d1 | -12.67781 | -48.51739 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 781b5351-ee50-378d-a309-81b1b838f4a0 | -15.78351 | -55.57742 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4bdb4171-5a90-308f-9330-a8f6ededffd8 | -14.3199 | -53.04696 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 547e6cda-4c25-3854-9333-db0f516ca2e4 | -11.71882 | -54.60946 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14ee6bc5-dd7a-38d4-8dea-6b022870cfec | -14.8766 | -46.65014 | 2026-08-17 05:18:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5099f562-fece-3f17-986e-44c7864ce18b | -11.58004 | -54.68749 | 2026-08-17 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4e91f85-5d7c-34f0-a30b-ff4ea67b8d6c | -14.31175 | -53.04789 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dc005250-11c6-3013-b5a8-7458d7ece80f | -11.81969 | -51.7718 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44e12d3b-ebea-32cc-b6d4-c37573953d33 | -11.73133 | -54.57719 | 2026-08-17 05:18:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5acb5686-b557-3cd4-a4e6-37326a4599e1 | -15.85721 | -56.34443 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d3a045a-c737-37bd-a7bf-5a8f82d3fee3 | -11.80526 | -51.77743 | 2026-08-17 05:18:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec04201d-940e-3197-a6e0-e37567ba84f8 | -15.81892 | -54.19659 | 2026-08-17 05:18:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bb51ac2-f20d-3f98-a749-43cec17cb698 | -13.64012 | -56.99267 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ea7c6b5-0c84-3dc6-8b82-cdc0a594fc1c | -11.70877 | -54.59824 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f6b6f96-4b8b-3f78-b7ac-886b87929f3a | -11.90498 | -47.35338 | 2026-08-17 05:18:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 98452f61-45b4-30ff-a5f0-0c184e04be4b | -11.49193 | -46.61688 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfd5dc31-1b37-3e9f-8a60-74f549ff5791 | -12.65827 | -48.48286 | 2026-08-17 05:18:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 604d2312-8eea-3530-b961-a0db0b83d40a | -16.66789 | -49.45375 | 2026-08-17 05:18:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 32a79a49-18a8-332e-8c58-4c07da162600 | -11.50447 | -46.60844 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fab66bfe-49c6-368f-8a5d-0fc06266a99f | -11.71432 | -54.61365 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 306e4ed8-a2f7-3e1f-9366-e4544f23b159 | -14.3112 | -53.05225 | 2026-08-17 05:18:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93e10657-8ad4-3153-a987-b0cfe4419c96 | -15.91144 | -56.48869 | 2026-08-17 05:18:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 657b4aae-f3d5-30d8-b4c4-7d011e07f000 | -14.20508 | -60.20537 | 2026-08-17 05:18:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a5e8e704-cc55-3739-8b17-175f341d122d | -15.02373 | -52.72247 | 2026-08-17 05:18:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 49823954-94ff-3c60-9499-c0165e6a9e5f | -11.49528 | -46.58764 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 61a1f3a4-eb70-3595-acb8-95f1f11913b4 | -10.05506 | -62.45594 | 2026-08-17 05:18:00 | NOAA-20 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5211e72c-873e-35ef-badd-591f1a120f14 | -14.44243 | -51.8306 | 2026-08-17 05:18:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f355d92c-7359-37fe-999e-8907726d1215 | -11.32954 | -55.22434 | 2026-08-17 05:18:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4edc4df-12d5-3eb1-9777-6d34fcce3adb | -11.4945 | -46.58301 | 2026-08-17 05:18:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 78137c8b-c0a8-39a1-b35f-f130dad2f608 | -11.70427 | -54.60244 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ce50761-5d5c-36f5-9a57-c4b538485db4 | -9.59415 | -60.50941 | 2026-08-17 05:18:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e753ea9-919f-3523-8bb5-5b90bef1eb60 | -14.30795 | -47.18746 | 2026-08-17 05:18:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52048f76-fe6f-3329-8167-5756224c89fc | -11.69841 | -54.61603 | 2026-08-17 05:18:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6a65462-b216-3a19-9420-dd22cd36c516 | -15.90274 | -55.52429 | 2026-08-17 05:18:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |


[Clique aqui para ver as próximas entradas](README59.md)
