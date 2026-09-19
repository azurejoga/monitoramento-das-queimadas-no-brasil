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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8c8453c-bd5c-3ba8-af8d-1bda56b5e98b | -2.9052 | -57.80851 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17a7a38f-8fb2-3300-b97f-a4e4d4913a8a | -2.89737 | -57.81379 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 062a43f6-019e-3259-8ea0-74ee4b72ace1 | -3.69317 | -60.6018 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4028cb24-b8e5-3d56-9f93-7b0429793f5e | -2.90116 | -57.78862 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ac662040-fb3b-3eb2-a461-a5725af9a762 | 1.31086 | -60.40373 | 2026-09-19 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9960f5ae-66c8-3b6b-a51d-61786a2de3c0 | -3.69105 | -60.60356 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1d4f1f92-47b0-333b-a873-5af6177e116d | -2.89832 | -57.80749 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 94bd6c8b-0648-3008-a5dd-b2992d2e4eba | -2.88739 | -57.78652 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12a71574-0ab1-3057-87c4-1ecdeb147b3d | -3.6951 | -60.61685 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 033f5cd0-6ca5-395f-921f-2699979d06a2 | -3.6963 | -60.60857 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cc59260-e756-330a-8004-d8156bc799a7 | -3.69254 | -60.60593 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f76c05ec-1a56-3c62-a686-7249e6e2e188 | -3.69165 | -60.59942 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fe76c12d-8a26-377c-b8ec-03c606d3bb75 | -3.33184 | -59.81384 | 2026-09-19 06:18:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3f7dc82-e9e6-336e-a926-56d44b63c17f | 0.78798 | -59.19912 | 2026-09-19 06:18:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf312cfe-d138-3a92-aa43-e67792083a3c | -2.89927 | -57.80119 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 66e3b52d-5e18-32b2-811a-8207ed90d277 | -2.89851 | -57.80768 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 9d4feec8-2265-38bb-880a-8ae770d04c9c | -2.90539 | -57.80873 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 4bf7a985-8534-39cc-abec-24089f80d766 | 1.31104 | -60.40409 | 2026-09-19 06:18:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 780ee702-7cf9-355f-a055-91422fa35366 | -3.69045 | -60.60771 | 2026-09-19 06:18:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a5337d3-005b-3940-8055-a6a8267d9fa3 | -2.9071 | -57.79593 | 2026-09-19 06:18:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7b134107-d421-3839-b642-0dd0ec35a9c6 | -10.7115 | -60.7312 | 2026-09-19 06:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| cd81eaaa-e3cd-3683-b67b-37db4049e1e6 | -18.0303 | -50.9385 | 2026-09-19 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 6c8d4f5f-3d01-3140-8dbc-3dffb2b31cc3 | -18.0274 | -51.0709 | 2026-09-19 06:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 7cfc01f2-6398-31a5-9079-fb4918f53bfb | -9.54089 | -63.78468 | 2026-09-19 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00a9d9a3-f332-392b-a11b-c7fc06150325 | -7.37149 | -68.01437 | 2026-09-19 06:20:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c74ffa6a-6e8a-32d3-8131-81c4ffe402fd | -10.71813 | -60.73056 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3621a518-aec9-3ff9-86dd-29cf570a9856 | -7.55942 | -61.32475 | 2026-09-19 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 792f09c7-63b3-3655-8ac7-91f78c53d2ee | -10.70471 | -60.73427 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| dd7738f9-4160-32fa-9c8c-62eb5d674612 | -9.06518 | -61.4255 | 2026-09-19 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd32fb03-18b4-38e2-a107-c78b8dd5a722 | -9.0646 | -61.42988 | 2026-09-19 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e3895a2-660b-3826-be2b-e5a600c765ba | -6.44589 | -59.98397 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6e38922-c064-372a-a00e-ab91656f8b42 | -6.71523 | -59.45759 | 2026-09-19 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb961af9-5c00-359d-a3ed-cbc774fe3113 | -5.76521 | -57.45303 | 2026-09-19 06:20:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 91d3bf72-690d-38ce-be60-ea1d93258e29 | -6.32022 | -59.93823 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea6e4dc-de4e-33d1-a7ed-5672acae0e6b | -10.69196 | -60.73252 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c034c5ae-b045-3e42-8f07-7dc3db3d69e5 | -7.37218 | -68.00982 | 2026-09-19 06:20:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20d9f388-c5fa-3c5d-a3be-26343bb54d86 | -6.70867 | -59.45673 | 2026-09-19 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b7b585b-6354-3a48-b86a-4274f198362e | -6.37095 | -58.28989 | 2026-09-19 06:20:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7a2337d4-c543-3e08-819c-6e20ec372a5a | -6.45289 | -59.97992 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7701fe71-29b9-3ee9-bad6-44eb90a8b5de | -7.55351 | -61.32395 | 2026-09-19 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b2cef85-551a-3a45-a2da-ce3dfe91664f | -10.6996 | -60.72303 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 12fa9760-a24a-3ed8-a5ab-eda3c3a64787 | -7.55827 | -61.33322 | 2026-09-19 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 708c23b3-42ff-3521-9c41-3b301b1b64db | -6.13383 | -59.9445 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1aff6fdf-ed86-3112-bcbc-3d34c5756905 | -9.54644 | -63.78235 | 2026-09-19 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c407285-7605-3069-b2cf-ba4f1c6934dd | -7.55294 | -61.32822 | 2026-09-19 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4885c852-8aba-3b6e-a2ef-0e2251dd99fa | -9.54169 | -63.77859 | 2026-09-19 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0a5090f-5b3a-37c3-920d-7d57fcc0f9a2 | -9.06683 | -61.42761 | 2026-09-19 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2cefcb1-7b56-3cd8-94bf-0b8eb4d1be26 | -10.70535 | -60.72904 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5f974562-e814-3a27-a077-6ed1fa2b3ed1 | -10.69897 | -60.72822 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 4936623d-a713-3896-b949-a2341af7f5e6 | -10.7111 | -60.73509 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 8bb04afd-aa94-304f-af98-7c4909ab9b48 | -5.76413 | -57.46103 | 2026-09-19 06:20:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ed9c6e22-a931-390a-877d-4011b4466a98 | -5.7579 | -57.45222 | 2026-09-19 06:20:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43f9adce-72c4-33d1-b8cd-23dd67a15946 | -7.55884 | -61.32902 | 2026-09-19 06:20:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30e49089-10f2-3dd0-96df-c2eaa47d2abb | -10.71238 | -60.72458 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 24f8217f-f331-3eb6-99f1-8711ea7f6f81 | -9.06083 | -61.42688 | 2026-09-19 06:20:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e6e57da-31f6-31a0-82ef-f3f88885b12d | -6.1345 | -59.93958 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54ce6b26-3327-39c1-acc0-f1976c19e8df | -7.37595 | -68.01041 | 2026-09-19 06:20:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15e579f9-6fcd-3806-9e24-4a2136074baf | -10.69134 | -60.7377 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0b7d40b-52e3-3ad5-ad65-8b8e27d977a5 | -6.71377 | -59.46083 | 2026-09-19 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e29e889-39af-366b-852c-25447bace0cc | -6.12749 | -59.94371 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eefe9f1f-ec22-3eb2-ba86-887d91904c83 | -6.44659 | -59.97885 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0c0e930-0495-38e6-95d7-d640b0705a78 | -5.75892 | -57.44473 | 2026-09-19 06:20:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea5433a2-78c5-3707-b663-7b082f487938 | -10.70408 | -60.73945 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e78c0e75-0813-3572-81b5-5f2fe44e8328 | -6.31953 | -59.94331 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efcbcd6c-ab77-3f6c-b22c-4bf7da98bfae | -6.70721 | -59.45996 | 2026-09-19 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a24bc40-0683-37ed-af44-39aa47bef7ec | -6.13315 | -59.94945 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3be9e47-1532-36ea-8f7e-4eae73da06eb | -10.69708 | -60.74375 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0de66ce0-870c-31be-bad9-88dbeaf08970 | -7.98653 | -71.34264 | 2026-09-19 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4161f213-d285-31c0-a895-0d44e39eb8c0 | -6.70789 | -59.46232 | 2026-09-19 06:20:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00f183ee-b4d6-3cc2-8621-ab41319a3800 | -6.44028 | -59.97781 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1157c3df-8e89-3535-b7f8-ca2b70e332e7 | -9.54129 | -63.78163 | 2026-09-19 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30ce3d0f-bd9c-3e4a-ba1f-b0f73f461e7c | -9.54685 | -63.77932 | 2026-09-19 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 670aa213-6e4a-3534-8ba4-06c8560dc371 | -10.70599 | -60.72379 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| cfe9d048-667b-3961-b441-2b7c300be704 | -7.98319 | -71.34212 | 2026-09-19 06:20:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e124051e-8c14-31bd-8226-66b0234e0a45 | -10.69834 | -60.73342 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7cfbd47b-c143-3c8b-bfe8-da6dac0de1d9 | -9.54725 | -63.77628 | 2026-09-19 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39884e01-5d43-3d50-a9b9-dea2ac19cb1a | -10.71174 | -60.72987 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 181c40f3-542d-3eb0-9a27-1b880b727bba | -10.69771 | -60.73861 | 2026-09-19 06:20:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 94e36b9a-afe8-3abf-ac7e-5f1ef58b63fe | -6.37008 | -58.29638 | 2026-09-19 06:20:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3802f89-59c3-348e-b9e3-b289bc300e65 | -9.5421 | -63.77553 | 2026-09-19 06:20:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 488e4e57-3980-3d65-882b-a8163dab2aa6 | -6.45219 | -59.98515 | 2026-09-19 06:20:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7fb519b0-dc5e-3f4c-a3c1-99ae70ed7edc | -12.34 | -50.7157 | 2026-09-19 06:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 7945e887-4b17-344e-b25b-e0f26f039060 | -18.0303 | -50.9385 | 2026-09-19 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 104a3cf3-4a17-31da-9936-8ea52df00009 | -10.7115 | -60.7312 | 2026-09-19 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 6c09d994-8ee2-3089-a450-7b35c5240b3f | -10.6928 | -60.7322 | 2026-09-19 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 674873e8-759d-3346-b043-bb05833b89ec | -18.0274 | -51.0709 | 2026-09-19 06:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 58e1772c-fc60-399f-8be4-abc568ff9490 | -18.0303 | -50.9385 | 2026-09-19 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 89100c3a-b4ca-3149-93a9-f464f6618cf0 | -18.0502 | -50.935 | 2026-09-19 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ed1052b5-69ed-3058-bd68-381cf5502dff | -10.7115 | -60.7312 | 2026-09-19 06:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| db8d5857-af11-3c03-b01d-1a62abd0ce03 | -12.34 | -50.7157 | 2026-09-19 06:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 5d622673-4820-3469-93f8-204261c90a58 | -18.0308 | -50.9164 | 2026-09-19 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 88e8d8b3-7081-3f8a-8743-227e11bfba3c | -18.0298 | -50.9606 | 2026-09-19 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 73ae07f9-2052-3f0d-a72a-a180dab329ee | -18.0274 | -51.0709 | 2026-09-19 06:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 58.3 |
| c32cb805-7acb-3535-be05-fe1f72053cf2 | -7.37177 | -68.02061 | 2026-09-19 06:40:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc5f3516-68e8-3f46-8635-662a6202d205 | -7.37233 | -68.01658 | 2026-09-19 06:40:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c09df035-8c19-376d-bd1b-9f438848b6c6 | -7.37217 | -68.02019 | 2026-09-19 06:40:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3732c214-6811-3a12-8f7b-4efe157ace5b | -7.37324 | -68.01211 | 2026-09-19 06:40:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afbfe1d3-cf83-3c8a-a0fe-217f62984d54 | -7.3727 | -68.01616 | 2026-09-19 06:40:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e703b0b5-f87a-3304-89db-a4f6efbe4aee | -7.37289 | -68.01254 | 2026-09-19 06:40:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 020b2cfe-c640-3141-a7dd-cf9631f037ef | -18.0274 | -51.0709 | 2026-09-19 06:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |


[Clique aqui para ver as próximas entradas](README100.md)
