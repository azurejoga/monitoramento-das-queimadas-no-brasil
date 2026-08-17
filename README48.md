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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 298060b0-8905-3075-87f1-b88ba823c9a3 | -8.21019 | -55.0123 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd25075a-dc35-30d7-b53b-f739b926e37c | -6.11642 | -57.70728 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 85e52bbf-353b-36ef-8024-0bc61af22a76 | -6.86825 | -56.42546 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20856f92-5f1b-3e56-9d3d-b339822b4888 | -10.51568 | -50.78881 | 2026-08-17 05:16:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9ffab3b6-491d-3313-b792-c8029bdd0669 | -6.71507 | -58.94079 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 169cee9e-6e68-35f3-9e1c-d9062b690000 | -9.01609 | -60.47897 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccc84e33-8d24-3139-9e12-1d6abe404f9f | -9.4737 | -51.60852 | 2026-08-17 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa046fe6-9eb1-3719-a215-5a7c1b3f95ac | -8.8969 | -60.56409 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2af078fe-db50-316f-8b36-d06e9b20ea98 | -7.37972 | -55.51496 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79050abc-8758-3494-86ef-0b1aae35359f | -9.01042 | -60.47014 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b2d1fa05-4b97-34f1-9d36-31537fbbfe9d | -6.85931 | -58.96765 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 436e0aeb-15c1-3e08-92ee-5bc8b598101c | -8.90131 | -60.58081 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 373433cc-1c66-3569-b3fb-c8a6f7b239f3 | -8.89396 | -60.60357 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 2894978c-b0e1-3f54-b0b8-bee97b6584ad | -6.78148 | -59.46898 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7af49b13-c157-3bcb-a2b9-2fe42c702d04 | -7.38782 | -55.48486 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4ca9494f-b54b-31d4-b19b-3fd128b238d3 | -11.28043 | -45.81494 | 2026-08-17 05:16:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aae326ca-10b7-3fab-881c-4505bf2bcc54 | -10.38808 | -48.26565 | 2026-08-17 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8473eac-acf9-38b0-9195-5aaf791b5509 | -6.99204 | -59.03335 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d85323b2-178b-3ebf-adb7-e39a65016acf | -6.81632 | -56.45022 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7b113d5-c011-3e60-ba8e-251e194b3758 | -10.46587 | -46.30214 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a744ecca-9f5e-30ae-9cdc-03b6059bc521 | -8.06732 | -48.53766 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54280f2b-18fc-3065-a95e-07662b3e80a9 | -6.10487 | -57.73732 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f767b5f7-550b-3b5b-a3e5-43cab798aba9 | -6.62918 | -59.06699 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d33fe3e-51d6-3cfd-8e5f-7d199df57eb5 | -8.74002 | -62.90638 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4b851b4-063a-3458-9ee3-3f90ee8845ce | -7.37395 | -55.5062 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fca4be85-1d92-3c76-8f6c-00b0c2c64503 | -7.43481 | -60.02214 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 801e3be0-796c-3154-8c43-16131dd1508a | -8.96373 | -60.52729 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9e9f7f6-17a7-34ff-97c2-71878aca5e40 | -8.98153 | -60.53671 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a7dc51b-511a-3333-b56a-89ef507c239d | -3.56762 | -56.3141 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28e9093e-45ac-3ae9-9f26-ed80fd551e16 | -6.10927 | -57.73094 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3e049d89-912b-36cb-81f5-b15d5b96528a | -6.6494 | -58.96323 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c2013d98-6659-33e3-bfed-8d939d0c01c0 | -6.70778 | -58.94325 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76832065-e61a-3ea2-8b27-084510bb9fd6 | -6.69808 | -56.16773 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f4d1bad-2a19-3f89-9a5b-c0e177b5961b | -6.87007 | -58.94371 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 325b70e4-5b67-333c-939c-da22cf532108 | -6.6174 | -58.96908 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a2943952-0109-314c-859f-3a2fa891800a | -7.36678 | -55.49409 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d5d009d-345e-343d-a2a2-fe56a9404f5f | -7.55027 | -61.17475 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d102b85-f0c1-3263-b00c-34f6efd70480 | -8.95804 | -60.51839 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3227dc46-fd5c-351a-88ef-a6f1cc1b4e6f | -6.78548 | -59.46587 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aaf3c516-c2bb-3901-ba90-87b0432fce80 | -6.83406 | -58.97461 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be9ae208-47dd-33c0-b835-fdba907fb014 | -8.08991 | -61.35703 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| cf4c5173-5d7b-3e81-8a5a-0ba983347596 | -6.79044 | -58.78483 | 2026-08-17 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ffc98ec9-e384-3b41-96af-ff6c62505885 | -6.68485 | -59.06491 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24715add-c767-3184-a60d-37f01b6ccaa8 | -9.2003 | -60.78923 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee24d079-176b-3220-9596-d479de04178c | -7.52785 | -60.68504 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42b4801c-4d42-3bbd-8d9a-63fed81503e7 | -6.54523 | -58.49234 | 2026-08-17 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c28415f-a570-333d-98a2-fc627f3af904 | -7.37025 | -55.49463 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 25ee9020-b22a-3417-a6bb-063ecd7a1377 | -8.72815 | -62.9043 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 838d859c-695f-339e-989a-4eba74713996 | -3.89337 | -59.34867 | 2026-08-17 05:16:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9276c98e-3474-30f1-93b6-f7367b590ad1 | -7.14091 | -47.5298 | 2026-08-17 05:16:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7668707-8c09-3b2c-b109-998797b06826 | -7.33909 | -59.59988 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6ca323be-d563-3c5a-927e-7fa2fd34d3af | -8.26495 | -57.35143 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2d2be4d-c575-3dad-9c5c-a076b5a1338b | -8.98063 | -60.52064 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 395fbcc6-f129-385b-b97b-911a11534710 | -6.69992 | -58.94927 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2750701a-db40-3459-997a-eaa4a883daa7 | -6.68764 | -59.06905 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92e75df4-7221-312f-a380-f42369563717 | -6.63873 | -58.96519 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 432b9e16-b837-3773-8fa9-10162f48eeda | -7.53431 | -55.58535 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f57e5ba7-7e3f-37bd-afb8-8853662b3ba8 | -6.86601 | -56.41781 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61033619-87c6-34eb-8840-38b1fcf55a0e | -6.77807 | -59.46842 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31079bcb-fd79-361a-85a7-27354b459206 | -11.08883 | -47.30168 | 2026-08-17 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4528d522-c149-390f-ba75-2c8189a7a3ef | -7.38261 | -55.49582 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 11dd1955-53f9-301b-a8ba-5ed25034c2ab | -6.85072 | -59.10631 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e3b6e4c-d40c-391b-a644-890650382f4b | -6.71564 | -58.93721 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7946ccd-ed31-32ed-8388-b3de8adf29fd | -6.11534 | -57.73545 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a6fa015c-c7c4-387f-8e97-a3d169f59893 | -10.50262 | -50.01622 | 2026-08-17 05:16:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7a20c355-2490-35b1-be4c-9e920939387a | -8.63849 | -54.71391 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ae917a0-8338-3202-92dc-a1ba97fcafc8 | -6.85816 | -58.97481 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc8a923a-8f0a-36fa-8f17-4fe4c382380f | -9.06113 | -60.39979 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6896a7bd-ab92-386f-97b6-15d064cc21ba | -10.38187 | -48.26889 | 2026-08-17 05:16:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ae9d2f8-c263-3a97-98fc-3dd60b3de864 | -8.98346 | -60.5251 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00797254-ddda-304a-8aba-5bafaf12b261 | -3.49161 | -60.02558 | 2026-08-17 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 280930af-62c6-3bb3-a8fa-e1e37484b388 | -7.38493 | -55.48046 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c18eb38-4d36-3e5b-b2f3-9b202094155a | -8.90103 | -60.56078 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d2024cff-1219-3ad9-a173-8f8bfcf240db | -11.13335 | -46.51873 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 4d426d40-22d6-3bae-a292-7a22e5cae6ba | -7.38666 | -55.49252 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9591fbf0-197b-3fc6-b70e-79be37fad1ef | -6.69819 | -58.96005 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3268ea1c-3fed-3ca6-9800-fe2282cf1480 | -10.46664 | -46.30205 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a58a717c-e066-3116-a984-b0c84ef78b44 | -6.68986 | -59.07682 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0935bec0-cdc0-3660-9544-024dfa60f6ad | -9.17988 | -59.6702 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4a00f72-0906-382d-8942-cc94fb3c01c7 | -6.63874 | -56.34968 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c9ef36a-b2e2-3fa2-b95b-e270f9c44f0e | -8.96973 | -60.51239 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dab297c1-fdd9-32a3-b30e-074b59213994 | -8.96247 | -60.53506 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1355777b-70b5-3371-b12a-ae539f6d96f9 | -7.78348 | -48.27707 | 2026-08-17 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39b79510-545a-3093-8b34-8241c4348c69 | -6.48152 | -51.60325 | 2026-08-17 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 749fbd9d-51cd-320e-855b-135b1aa1a724 | -6.77647 | -59.45682 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27798ad9-0d4b-32eb-b4e1-93dfac1c6e1c | -7.9064 | -48.52983 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b89b835-d911-3349-8b44-152e7d800232 | -3.992 | -56.27372 | 2026-08-17 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3adf20df-0e8a-3740-8a72-3096d9ce3112 | -7.42444 | -60.02043 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c6ab7700-fefb-349c-8080-cdf70bae3a30 | -8.97383 | -60.50909 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 420b8730-4360-32ee-b02f-352f5fb135d5 | -8.9832 | -60.5052 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 134d70b5-2b93-33e1-93a5-5b025d690aac | -6.62639 | -59.06284 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b5c1eb27-cb59-3aad-beac-273fedea0b3e | -8.96943 | -60.53623 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7afe44f2-d733-3a13-b723-76beec3b7aaf | -6.70499 | -58.93912 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dc3b42dc-32b1-307d-806a-070a73f74b7d | -6.61902 | -58.98039 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dda9de4-ae59-33fb-8ad0-e670170a17f3 | -6.77346 | -59.47528 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb31b138-93a3-31bb-ac94-d6a02f6e82d6 | -6.11975 | -57.72906 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2b3fdaa7-422d-37a4-85ca-d39d5d501e3f | -8.21078 | -55.00829 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 306b66eb-ba37-3869-aa8a-91593ee5049d | -8.52362 | -54.9056 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1714bca-8c92-3688-b9d1-2886838d5eaf | -6.97071 | -59.03727 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b43ddde-bd9f-35f9-8862-b6bbaf508fe6 | -6.64268 | -58.96215 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README49.md)
