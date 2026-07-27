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
| 5dbf3a99-bc31-34d9-ba23-17c5a3a45b93 | -10.9397 | -43.0593 | 2026-07-27 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 4463c560-b199-38ac-bfdb-8db4c8bff92e | -10.9205 | -43.0622 | 2026-07-27 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 03bd64cb-e4b1-30b0-9e4f-42241216d454 | -10.9588 | -43.0565 | 2026-07-27 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 73887f03-46ed-34ae-b24e-138f7eba637a | -10.9401 | -43.0355 | 2026-07-27 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0763e716-949d-3b2d-b526-d7bf8a689794 | -10.9397 | -43.0593 | 2026-07-27 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 221.9 |
| ba16d528-b320-32dd-b4a6-22b5ce891c8b | -10.9401 | -43.0355 | 2026-07-27 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| dd0f1cd4-5b00-3977-8193-bd28987c1550 | -10.94 | -43.05 | 2026-07-27 00:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4e58563-894e-34c5-b10f-0942a2d45308 | -10.9401 | -43.0355 | 2026-07-27 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 0b0a7249-478b-3c88-8509-9e43866620bb | -10.9397 | -43.0593 | 2026-07-27 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 256.1 |
| 5d5b226c-1b66-3435-bd87-dd11cf43573c | -10.9401 | -43.0355 | 2026-07-27 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 41e4cceb-ef58-3c00-99b3-f0004894b7d7 | -10.9397 | -43.0593 | 2026-07-27 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| ba4688a3-997e-3625-98eb-be1795334510 | -13.3559 | -54.277901 | 2026-07-27 00:31:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 994bc3db-3bec-383b-8004-9dffb84dbfc1 | -14.2406 | -54.557301 | 2026-07-27 00:31:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 488cda21-e90d-3888-afcf-98643e3e1b5d | -13.3657 | -54.2756 | 2026-07-27 00:31:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c15d6fcb-afd0-37c4-9e1d-f8d2861aaa99 | -14.5046 | -48.918301 | 2026-07-27 00:31:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5e82afb0-7fa8-3ee1-9bce-9a7f119a6c12 | -12.3088 | -50.357899 | 2026-07-27 00:31:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 613f6b35-c7c0-39cf-b9e6-d517e97a7406 | -13.6825 | -51.8965 | 2026-07-27 00:31:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbbfe6e3-87bc-3626-89e2-1c34cbf1cec7 | -10.9275 | -43.0354 | 2026-07-27 00:31:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c7edb5ea-75a6-331b-ad0e-9778f0ed0624 | -10.9132 | -56.357899 | 2026-07-27 00:31:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7991871-00be-3c20-a5d5-abebd71e7389 | -14.5071 | -48.9286 | 2026-07-27 00:31:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7248e1ef-8dfa-36c1-895f-ec8a54f1de04 | -7.1716 | -59.3046 | 2026-07-27 00:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35cb781c-5561-368f-a84b-ff3e9b951db8 | -7.1696 | -59.295601 | 2026-07-27 00:31:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e0add3a-2561-33f6-bbef-9643cf86299c | -10.9116 | -56.350601 | 2026-07-27 00:31:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b39b837e-8128-3d40-8c0e-b33a9ac055ea | -12.3066 | -50.348701 | 2026-07-27 00:31:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1ac667-4d03-3006-b47c-df885959d9d7 | -2.7997 | -48.665501 | 2026-07-27 00:31:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 647906f6-b6b8-377b-8dd1-8b012874d9db | -10.9103 | -43.0093 | 2026-07-27 00:31:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d101e26a-64c5-3189-9207-e65203ece4a3 | -14.2391 | -54.550201 | 2026-07-27 00:31:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| de57ee12-ea88-3293-841f-18a43fce09e7 | -10.918 | -43.037998 | 2026-07-27 00:31:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d3cac11a-a6ea-3a2a-8a70-3058d4bf474e | -14.4948 | -48.920799 | 2026-07-27 00:31:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e6abdf89-2678-30ea-86e7-dd82e7e4bbdf | -10.9352 | -43.063999 | 2026-07-27 00:31:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6ac3c432-8796-351d-b82c-8c01b7b60542 | -10.9084 | -43.040699 | 2026-07-27 00:31:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f428e86f-29ec-3d13-9510-5907fa102398 | -19.094999 | -44.323502 | 2026-07-27 00:31:00 | METOP-B | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4810c046-818b-3d21-98a4-c6018187ca18 | -10.9257 | -43.066601 | 2026-07-27 00:31:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e83abcee-b49e-3742-910b-f5783e469e84 | -13.6843 | -51.904099 | 2026-07-27 00:31:00 | METOP-B | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6616fda7-1ff1-321c-bd8a-d84de700ead3 | -10.9397 | -43.0593 | 2026-07-27 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 235.8 |
| 4ffa80dd-9b91-3c55-85d4-79ef693dbd28 | -10.9401 | -43.0355 | 2026-07-27 00:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.9 |
| e2a896f0-4c42-394f-830b-025d1c795af6 | -10.9401 | -43.0355 | 2026-07-27 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.7 |
| e93fd15d-5312-3fa6-8137-d917daf0563d | -10.9397 | -43.0593 | 2026-07-27 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 252.7 |
| ec7d39d3-3ea1-3f7b-8925-84cc02e79e37 | -10.9397 | -43.0593 | 2026-07-27 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 254.8 |
| 4689496c-b704-3894-86bf-119700866e19 | -10.9588 | -43.0565 | 2026-07-27 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| c8292b56-d89c-30a2-96bd-c8999c13aea5 | -10.9205 | -43.0622 | 2026-07-27 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 01eeb020-4c9a-3f3c-8a1f-826dfaa57ad5 | -10.9401 | -43.0355 | 2026-07-27 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 71a10e33-4a1d-3b35-80b8-94511ad8e484 | -14.2332 | -54.5716 | 2026-07-27 01:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 6afaa09d-7def-3689-a7c7-2f14b9705d53 | -10.9588 | -43.0565 | 2026-07-27 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| b69756b0-f34b-360a-9238-330cb1015fdc | -10.9401 | -43.0355 | 2026-07-27 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 6d6efea3-80dd-33a6-9831-243ef216d54b | -10.9397 | -43.0593 | 2026-07-27 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 276.4 |
| a3bca73e-5145-3bc5-9c7d-375499ce7f6c | -10.9205 | -43.0622 | 2026-07-27 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 3b5cfbe0-442f-3919-b801-a4599e40e077 | -10.94 | -43.05 | 2026-07-27 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83b46775-56c7-39dd-9c96-472bcf80d5a9 | -10.9401 | -43.0355 | 2026-07-27 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| ada976ce-0ca7-3301-8846-de8f4b4814a5 | -10.9588 | -43.0565 | 2026-07-27 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 81ba1346-254d-353a-a296-a35144601c25 | -10.9205 | -43.0622 | 2026-07-27 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| c1ea6a04-5805-3f43-b9a9-4e67ff1e737e | -10.9397 | -43.0593 | 2026-07-27 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 285.3 |
| ec2b94e7-ab23-3653-a151-c0f9f85bdd32 | -10.9205 | -43.0622 | 2026-07-27 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 6447476d-cf57-3acf-85a6-55619136c0f0 | -10.9401 | -43.0355 | 2026-07-27 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 1caec680-2615-3b0b-9aa5-c8b19bdab4df | -10.9397 | -43.0593 | 2026-07-27 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 246.9 |
| fa6eecec-8a42-32bd-93d2-6f4eefa0f915 | -10.9588 | -43.0565 | 2026-07-27 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 2a5f3203-f057-3833-97cb-568282b719bd | -8.86544 | -65.03636 | 2026-07-27 01:34:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.8 |
| beae85ff-0ff9-319b-9e06-3242c1c874bb | -10.9401 | -43.0355 | 2026-07-27 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 4e66fed9-2e05-39bb-b9de-d230cef066b0 | -10.9397 | -43.0593 | 2026-07-27 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 311.8 |
| 794e644c-2daa-3398-a777-c7d67134fd8f | -10.9401 | -43.0355 | 2026-07-27 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 2bf05bb2-7411-3bb7-9727-1265e8a2b9db | -10.9588 | -43.0565 | 2026-07-27 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| fba3c431-720a-3b26-aa52-46077a24dbf7 | -10.9397 | -43.0593 | 2026-07-27 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 287.0 |
| 7fdcddcc-7cb8-3007-8905-8b5e85305905 | -10.9588 | -43.0565 | 2026-07-27 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 211ad1ae-e0e8-3f8e-8bec-77fdcca78931 | -10.9205 | -43.0622 | 2026-07-27 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| bacf1cfb-ddce-3e22-85e3-0eb1606bbfa4 | -10.9401 | -43.0355 | 2026-07-27 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f6065ae8-b779-3c60-82a4-f9c3d1e6eb2f | -10.9397 | -43.0593 | 2026-07-27 02:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 190.5 |
| fcf8edef-30ed-3c1b-ab11-eb03feb9d414 | -10.9588 | -43.0565 | 2026-07-27 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 217fbb4f-5dd5-33e3-a949-30ff259c7506 | -10.9397 | -43.0593 | 2026-07-27 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.7 |
| bd3fdace-67bf-3782-a67e-fca07ae313de | -10.94 | -43.05 | 2026-07-27 02:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6d273fcc-6f04-34fb-b3fa-9a064c240ee2 | -10.9397 | -43.0593 | 2026-07-27 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 173.6 |
| 5668ce4c-3af3-3026-b5dc-46e94af25e9e | -10.9401 | -43.0355 | 2026-07-27 02:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 42bf430d-4ca3-300a-9591-bef7013d3672 | -11.475 | -47.5536 | 2026-07-27 02:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 2e7e3420-4f52-3bef-930d-f868cfb1ec49 | -10.9588 | -43.0565 | 2026-07-27 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 61138474-0ad0-3b96-b21d-63538da829b6 | -10.9397 | -43.0593 | 2026-07-27 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 5cfb6518-1417-3b12-8c7f-2fb7f34e6bf5 | -10.9397 | -43.0593 | 2026-07-27 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 02404c42-3785-3686-8269-481e48e67bfc | -10.9401 | -43.0355 | 2026-07-27 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.5 |
| bd747c7b-689a-3323-8d8b-3b7f33629fbb | -10.9397 | -43.0593 | 2026-07-27 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 149.6 |
| c6fbc1a7-aca2-3353-81f7-7cc20fe2c7bd | -10.9401 | -43.0355 | 2026-07-27 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e5245875-acb6-3895-a3d6-f2019773c037 | -10.9397 | -43.0593 | 2026-07-27 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| 2c8be844-3529-3c08-aa6f-a757c5562db7 | -10.9401 | -43.0355 | 2026-07-27 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 6d37f323-3acd-3a98-92bd-290062b043fa | -10.9397 | -43.0593 | 2026-07-27 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 199.0 |
| a0e65c1a-e434-35af-8c7e-409df8d4e20f | -21.5694 | -41.33454 | 2026-07-27 03:15:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c58625bf-24ee-3af6-a424-0a928061e815 | -21.57586 | -41.33645 | 2026-07-27 03:15:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b2b881d5-dad1-3e89-806b-ac7c9d21ed45 | -21.57347 | -41.33557 | 2026-07-27 03:15:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 813ce809-159d-310c-a0a4-b9d0de759643 | -10.9588 | -43.0565 | 2026-07-27 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 3640243c-7530-3e31-8090-09c0e21bd286 | -10.9401 | -43.0355 | 2026-07-27 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 806adc0a-620c-388b-bc0d-47acb036de9c | -10.9397 | -43.0593 | 2026-07-27 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.8 |
| 083f3f50-3cb6-3415-9f42-2f98caa6bb22 | -7.62133 | -38.79692 | 2026-07-27 03:28:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1d727b1e-1319-3b4e-95e5-8de968bd07c8 | -5.42067 | -43.42886 | 2026-07-27 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9e8bb132-ea2f-36ab-bcfa-886a4f72f756 | -5.42172 | -43.43124 | 2026-07-27 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2a281c70-a35b-361a-9955-18e2c51eded1 | -8.92772 | -40.13832 | 2026-07-27 03:28:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3755cb39-4913-3564-9e78-5bdc1156c0a0 | -5.35444 | -43.14017 | 2026-07-27 03:28:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3bcb969c-9489-3493-8cad-dfd453e3b573 | -5.35555 | -43.13414 | 2026-07-27 03:28:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe5b0599-df98-3870-9bcf-c53ff162d774 | -8.92832 | -40.13506 | 2026-07-27 03:28:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8329405e-ff7c-3674-9095-d0af373b6f90 | -4.90982 | -43.46855 | 2026-07-27 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 52b71425-b453-3c38-86d7-f0ba97e19485 | -4.90864 | -43.47509 | 2026-07-27 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e260ef0-1f8a-3b98-9ddb-3c82dbe81834 | -5.42285 | -43.4251 | 2026-07-27 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce6b6cba-5db1-3c3e-97fd-7f0e3c208bcb | -5.93624 | -43.64839 | 2026-07-27 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abef83be-0d1c-38d2-8d91-80b3f2ca3c56 | -5.35829 | -43.14045 | 2026-07-27 03:28:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 29d02160-8167-3110-8286-9e2f3b49a81b | -4.94565 | -37.9368 | 2026-07-27 03:28:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |


[Clique aqui para ver as próximas entradas](README2.md)
