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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29eef4db-973d-335d-ad98-a4033f37ecf2 | -6.25055 | -55.4337 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 04358e8a-372b-3b80-b342-01c45444a387 | -10.36107 | -50.01323 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| a3ef40cd-6653-346a-b1b3-874dac273dc9 | -7.31386 | -60.57646 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bedf35fb-0a2c-3cbe-a142-9af404336aee | -6.93328 | -55.63057 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67614aaf-b6e0-316c-8ce2-8d79261b1fdf | -9.02859 | -65.45338 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1457b0f7-1cca-3683-a7e0-a077f56a0b87 | -9.21904 | -65.79366 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f22f8a57-c0b1-3cd8-87c8-e989833c0d1e | -6.62376 | -58.38517 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa071315-a5d8-3080-982e-df965b5fe3d6 | -11.06076 | -51.52733 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 576d5d19-d157-31b8-b65e-06c93670509e | -5.85812 | -57.56077 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f019f7c7-d372-3e9e-81ad-bb1ff4f7c55b | -5.96125 | -57.67406 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c5ca45e8-a303-30bd-88d9-fec480660b4b | -7.76723 | -61.20462 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39218911-c0df-358c-b054-53f0c023537d | -8.94298 | -63.30078 | 2026-09-01 05:36:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ab96c3d-1fbb-3da1-815f-9c4c0c38409b | -7.04459 | -59.23097 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 330e46f9-d401-39aa-b60a-cb66f733c3d3 | -9.49612 | -67.67041 | 2026-09-01 05:36:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9343f4e8-6aba-33fd-96da-4c44509052ec | -9.92943 | -60.48683 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 641ea56f-ec41-39c6-bb1d-d288f5ee6d17 | -7.58162 | -60.47443 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d67108e5-46bf-3514-9cd1-7c1d503ab0aa | -7.58117 | -61.35976 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71d75474-c0f0-3bf4-bb03-f28c0c88c150 | -5.49225 | -57.14177 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8359c18c-5cfc-362a-a96a-10ea43341931 | -6.96043 | -56.43544 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4d7ea52-fd10-30f9-bc73-2efc0329eb3e | -8.36423 | -57.67454 | 2026-09-01 05:36:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3235a6fb-a812-371a-bcd2-5b11285b5721 | -7.35559 | -60.57898 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 6f074942-cb0e-335c-82f6-837a45b77277 | -7.05622 | -52.71638 | 2026-09-01 05:36:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b5066b8-7e91-3aa6-a984-6a0e9e6e6e78 | -6.24988 | -55.43841 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e4c7b21-972f-32e5-a455-9fa44f842cf7 | -7.57588 | -60.46581 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c2fcf21-a73b-36f3-a512-f772e0bb484c | -11.06797 | -60.69943 | 2026-09-01 05:36:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f919251-2949-3186-8e61-7c7930e2d911 | -9.14508 | -61.09924 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e7f3c45-2965-3ac4-a9a0-b5af3c3abc38 | -7.01697 | -59.59747 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a30d75d-632f-3d82-9351-c259801d1a4e | -9.839 | -64.97579 | 2026-09-01 05:36:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e536f0fd-a5ba-337e-94de-f7c3993d224d | -7.33844 | -60.57636 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 24098f5c-0cfe-3708-a202-70eafe861cc9 | -7.58967 | -60.46799 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 669f60fc-aa64-38f1-8ed7-caf97cf80b65 | -6.84975 | -59.46173 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5f71e4f-2f4a-3d35-981a-efcd3b988d74 | -5.87744 | -57.78252 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc9708d5-4a78-3756-9bfe-1a987242d926 | -9.17941 | -59.62058 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 893e4349-0ff9-3456-a0a1-3ca0e2d0595a | -7.28071 | -60.65519 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4267b33e-bc56-3c15-8829-6d0f8387d77a | -7.53591 | -61.38562 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c2901f9-f6b2-393d-839d-684888ca357e | -7.58334 | -60.48626 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07444b9d-6dd3-3087-91eb-37a696ebf898 | -11.24945 | -50.58391 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0faa5773-f782-347d-8950-acc349d6752c | -8.93152 | -62.36357 | 2026-09-01 05:36:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ef5c6c00-fb6e-34d0-a5b1-8a221c2d7c08 | -10.51004 | -57.43092 | 2026-09-01 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27881283-3b9b-3330-a303-1d89c67a5daf | -8.59303 | -54.72375 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25f8b687-5442-3cab-abb9-3acbb182dc27 | -10.32664 | -49.95081 | 2026-09-01 05:36:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0842be7c-4774-3552-8bea-e175804e1164 | -8.86333 | -66.77295 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83a6773e-2ed1-310d-9b14-9553bc37287a | -6.70285 | -55.41161 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7911948-7623-30c3-bffa-fe1535868956 | -6.24783 | -55.48534 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbb38355-3093-3fe4-be59-14ae963e9c4a | -7.28991 | -60.61856 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 263855c3-430b-3252-b03d-093880c851c5 | -11.26358 | -50.57952 | 2026-09-01 05:36:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 01896c75-8bb6-334b-8090-f344de5349b8 | -7.53311 | -61.38152 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16e5d43e-0518-33eb-a7c3-9dd9204afc48 | -11.24818 | -54.00693 | 2026-09-01 05:36:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39c8b449-55f7-3709-8f65-50ef73d4e492 | -6.11606 | -57.68453 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33d0d05d-64ed-3f0c-9768-b42e7d632774 | -7.6698 | -62.54815 | 2026-09-01 05:36:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 20310165-b83c-339b-b4d0-4a0701b3286a | -8.87419 | -66.89261 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 725ec681-6a4d-3f23-a795-149569d638d3 | -9.59345 | -60.51138 | 2026-09-01 05:36:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50b79e9d-3942-38ec-82f4-8fb6e4a8e8e7 | -7.86232 | -61.14896 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 352b98ea-5a7d-376b-8c98-fa206a0b43f0 | -11.06648 | -51.53324 | 2026-09-01 05:36:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e51ce42-ccdc-3f1b-9283-3b9795a6b30f | -7.55886 | -61.41474 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3588cac1-6bdc-3b43-a049-a20bfb93789f | -6.12104 | -57.67699 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c63feea8-e469-3a21-b28b-ac09fbf63823 | -6.78592 | -59.78902 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a25c141-a9fd-3e35-8fee-dca4cfd34f57 | -9.03869 | -65.39777 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea643912-a522-33f5-8d5a-4a161c357828 | -8.96918 | -71.25609 | 2026-09-01 05:36:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8e0e56e-3f11-32ce-bacf-1e2d250fd0f8 | -6.65592 | -59.43084 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f256f815-463a-3f54-83df-2fab9f6d3cde | -10.23613 | -54.34922 | 2026-09-01 05:36:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19fd4969-e42d-3ccd-a3cd-354f29c8dac9 | -9.94643 | -53.99627 | 2026-09-01 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8a2c1e0-bf89-3341-ae11-6403314d1b7b | -6.94869 | -55.62622 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 00b5e49b-6660-3653-80aa-780deca9d04a | -7.03797 | -59.2257 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb669e90-c67a-3978-aa93-6934317eee3f | -7.57243 | -60.46529 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e57b3f52-516e-3f5e-a04d-563c6620d91d | -9.0571 | -65.48143 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7109f473-432d-3bd7-9944-d1e4ed2a2dae | -9.98348 | -67.57775 | 2026-09-01 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1465a4af-ec40-3cbc-9c6e-76eb206e2345 | -9.21748 | -59.76527 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 94c0db1c-644a-3645-bd27-fcc00f1a0ae0 | -7.49308 | -55.31676 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| afd6b762-f425-33a9-b1b1-3d058ffc6e0d | -6.80652 | -59.77196 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67206ad3-0cd5-3710-b8c5-84ef6db3d81f | -5.93872 | -57.69103 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5417999-bed9-3961-88ef-85eb359408c1 | -5.48823 | -57.14114 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eacb920-3356-3862-9525-924118a08330 | -6.80708 | -59.09794 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a9252dda-b2cf-3405-9aff-f3574b19ea8c | -6.73842 | -56.34424 | 2026-09-01 05:36:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 031d24ba-fc1f-3b46-b506-a349f0ebce36 | -7.91109 | -61.33409 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 000e2a57-dfe2-3578-9700-977993d5f8de | -6.86159 | -59.48025 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1db7229f-b010-3296-8f7b-dc42ad5f8421 | -8.56764 | -63.18324 | 2026-09-01 05:36:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 860c106a-2a07-39be-9c6a-a61843ac4a44 | -9.24889 | -68.18928 | 2026-09-01 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b013715c-0b74-361f-b80d-033610e1fc17 | -9.13866 | -60.52664 | 2026-09-01 05:36:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f011ff8-593a-3bfb-944f-77d5ffa30a4c | -5.86975 | -57.77498 | 2026-09-01 05:36:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3467de9-2a2f-3ab6-86a4-008acaeca308 | -6.91225 | -59.48386 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5504d19-db0d-3443-a3a0-e31fa53b963c | -7.57071 | -60.47656 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 84fb3377-7f88-3eae-a2dc-95d03273e94c | -7.34072 | -60.58435 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a6986733-beca-329e-8de3-d0ea92e74bbc | -6.77888 | -59.78794 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e16085d1-2c49-356a-83de-ef8640cd8ca6 | -6.90931 | -59.47921 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 578e69e6-cb65-3cf8-8480-fa93475ab853 | -7.28599 | -49.82565 | 2026-09-01 05:36:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e2b39922-ddd0-3e1c-8a30-c0240d5ff56a | -5.57364 | -60.18984 | 2026-09-01 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d84455ae-9289-325c-9e9b-90c6d344cb99 | -10.82608 | -50.72124 | 2026-09-01 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3b86f65-ea39-3702-8663-f081aebc7db0 | -7.3076 | -60.59447 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc38ead1-2f2e-3b11-81c6-27f51f1a2503 | -7.35672 | -60.59445 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8582d994-b136-3968-8cef-9446aac274e5 | -8.11907 | -54.96679 | 2026-09-01 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| ced04e6e-9c9a-39e9-889d-3e8a0d7a6671 | -6.59216 | -58.59406 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 365e5f60-adf0-33c2-aac1-2542171ee25e | -9.05484 | -65.40852 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba2f7c75-f775-3582-b6f9-4d4bb74fcf94 | -6.96309 | -55.64898 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| b37bea16-1a2f-3fda-87ff-4d038cfeb124 | -8.5917 | -66.97849 | 2026-09-01 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fead532-8926-3014-a8e6-4c603209cdd1 | -6.80763 | -59.57635 | 2026-09-01 05:36:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ccc38d8-1b2b-3f5b-a854-3d5a0eaef004 | -7.63276 | -55.29227 | 2026-09-01 05:36:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3eb5ab7c-101c-3ce4-b377-1787b29384c7 | -6.60099 | -58.58624 | 2026-09-01 05:36:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5529ec1-01f0-3532-8820-299b617c6bb2 | -7.56552 | -61.37193 | 2026-09-01 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d81e580-8d75-347e-a4a5-c4e58b6d721f | -8.89306 | -68.90451 | 2026-09-01 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README80.md)
