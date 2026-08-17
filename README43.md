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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d95abb0a-1836-3042-84fc-fe1e5ef19710 | -8.03168 | -55.14568 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6149604-358e-3679-8f0d-ffd3e652a75c | -6.60447 | -58.9746 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06f5ccea-2cc7-3bad-aff5-5ce97e92d125 | -8.04259 | -54.01802 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a3b77687-33f1-327b-846d-14b1fb40dd6f | -8.96658 | -60.53176 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cc57e16-ec87-3523-a9a5-e0a00e144dec | -6.77707 | -59.45314 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67d72b55-33a7-38e2-9cc2-24d6b99b3f60 | -9.1771 | -59.666 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81a56e12-f0c8-3b9f-9b61-8abe773dc4e7 | -8.65972 | -54.72147 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f366bf50-942d-3f64-9c5e-2a6c03c11dce | -6.69877 | -58.95645 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8b87891-0078-3174-bfaf-d26fd3b74afb | -6.62464 | -59.07366 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcc7b2ee-98e9-3d6c-874d-7ac2b06125cc | -7.07001 | -56.65649 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2cda850-6798-3b03-bbf2-e01cc75edb75 | -8.5086 | -54.90742 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 990d25ab-7b58-33ba-9c40-98d5e8bc14be | -6.61291 | -58.9649 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4f2e0aba-2f39-3622-a132-a677945494a7 | -8.90094 | -60.60473 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b789432-7625-3034-88b6-8574d58379cd | -6.86098 | -56.428 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80d4df96-a11a-31d6-8bd9-00d783b89bb2 | -8.59905 | -54.70334 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a47169a-4f3f-37a2-a963-7aac1f979c45 | -6.96592 | -59.3033 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d025981-2466-3bc6-b168-9d0df2798d5c | -6.62801 | -59.0742 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1431108e-8765-399d-a014-af02dea2c04b | -6.09383 | -57.72141 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9fb20ae-386d-330e-b909-47ab1b9ad19f | -6.10432 | -57.74078 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 33f29f6f-1948-38ae-a62e-cf068e978e49 | -7.43198 | -60.01776 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5669117f-c5b4-3288-bd7e-bee27f36100f | -8.63593 | -54.731 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2b8e6c2-7dcc-31a7-8dd1-8d3b33179033 | -8.97586 | -60.52782 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9bab1d5-d3e6-3fbd-a8c4-923f55bb657d | -6.70721 | -58.94682 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85508895-9c26-326d-9055-4d1701eded42 | -7.42262 | -60.01717 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dab9ece-dac4-3913-a71d-af9d8c30730d | -6.87272 | -56.41885 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 53c54f1b-2c5a-3c9e-9099-5f51c5f2f9f3 | -8.52193 | -54.89241 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66991181-7878-3661-96f5-21df02afa726 | -6.10266 | -57.72989 | 2026-08-17 05:16:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 111ab517-ffff-3d5c-a0c3-833a0bdadcd0 | -8.73386 | -62.89474 | 2026-08-17 05:16:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f5f6502b-0fc3-3741-a79c-c25de81fea1b | -6.84866 | -58.9696 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca48f262-0311-30cd-be58-56fada0697b2 | -7.61058 | -60.94987 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1fd62ff-5a27-36cb-a82b-fa8998acb579 | -7.78328 | -48.27749 | 2026-08-17 05:16:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d4a4c35-5432-3a50-9548-c2261264d8ed | -8.9593 | -60.51065 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d137fb4f-e1ff-308c-a697-c330b298f817 | -8.63721 | -54.72244 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bf18f26-e791-314a-94c6-b082a7346e12 | -6.86992 | -56.41476 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2c811da-dec6-3f76-8daf-138958355d6e | -6.77191 | -59.76616 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5c4b5870-43d2-3daa-884b-5c715557cb8a | -6.38384 | -51.74281 | 2026-08-17 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0c909b3-f06e-3244-b56c-b3aa2e459a93 | -8.4245 | -62.67838 | 2026-08-17 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d344288-97de-3b0a-9db0-ac5851cd3176 | -6.84144 | -56.44323 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26fb3210-f99d-3449-be31-76f6a9b8e112 | -7.61486 | -60.94635 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd9e28f3-9cd6-3784-b7bb-495adb702749 | -7.41855 | -60.02044 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9848b802-f0d7-326b-8f66-e5da37955ffb | -8.89535 | -60.55183 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7ff5749a-8d0e-34b6-a1bf-5ff785ae6be4 | -7.88751 | -61.79643 | 2026-08-17 05:16:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0df63907-20da-31cc-84ca-7200d1d559e2 | -7.55361 | -61.17805 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2d81ee35-3daa-3add-a311-691ef90ff613 | -6.82916 | -56.45592 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b580a556-cab5-3d73-b88a-007aa2e71773 | -7.54299 | -55.57497 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b0d55fb-9772-35ff-b21a-8bc6427b05ac | -8.96784 | -60.524 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07d87e21-d153-388a-9a7d-fdcf92b9c31b | -8.42058 | -62.6777 | 2026-08-17 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 457d5f84-6cab-335d-8e2a-24dbde262ae0 | -6.77867 | -59.46474 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52a6e3e4-240f-3d60-885d-337f6182ce4e | -6.63021 | -59.08197 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9514c425-802b-3464-a3d8-955b12586e85 | -7.79698 | -62.39371 | 2026-08-17 05:16:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b541caa-7324-3ce1-bcd8-4dcc900750a1 | -8.54721 | -54.60066 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 787fae7f-7fbf-37f9-856a-a5413ab8643b | -7.55577 | -61.16527 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a58c0a89-129a-3b33-9f7d-ce170c38bfe2 | -6.63027 | -58.97483 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b1bb0b4-d21f-3a75-b272-56df4338154e | -6.70106 | -58.94212 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ddfe246c-b703-30df-8cfb-e7cc4b96bf34 | -7.45176 | -60.00538 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe1e09c7-2863-3ce3-8ae4-9eef7aa94e00 | -6.69864 | -56.16413 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f4008ac-c96c-374b-8704-58efcd0c28eb | -6.70442 | -58.94269 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5c929d97-b055-3aa8-80fa-8ce37c4af5a8 | -8.97109 | -60.53501 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8fb94e5-8765-35b4-aa99-8f30b1cc726c | -6.59437 | -58.97298 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 104fe927-e744-34b8-9b26-4f476223095c | -6.8621 | -56.42086 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec454d2a-744c-3f12-8565-6d9c84ee60c0 | -6.84199 | -56.43967 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a001fbf-dfe6-31cf-b149-7d84091faa83 | -7.41978 | -60.01278 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7d60029-0f70-367c-bc26-4e5f660b3c43 | -9.18716 | -60.80323 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03a141b3-dd4e-3da4-92cf-0a60b47f85cb | -8.68439 | -54.75872 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f301f907-c663-3048-a60c-ac16e82c8c6b | -6.48417 | -55.90076 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c280241a-9eca-32cf-b9ed-4b3d8d7d2494 | -8.06189 | -48.53692 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9afc32b6-26fc-3c95-860b-661b1bf3a813 | -7.80937 | -47.84401 | 2026-08-17 05:16:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c35a662-2c5a-3d90-88f1-ae300780adf5 | -6.73446 | -58.58356 | 2026-08-17 05:16:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bbec67a-1614-3135-b9a8-eedcdce030a5 | -6.83166 | -59.09585 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27f8731e-5e7f-3752-bb60-d29f4a102747 | -8.61237 | -54.71413 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef23b6fc-c05d-3d06-90f9-c77b94a22693 | -6.71342 | -58.9295 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6de60a06-236f-32a9-9a93-9fa421b3a743 | -8.95013 | -60.545 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83b22247-4116-354c-a73c-5478ea4a14a8 | -6.96558 | -56.49853 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cf445623-2010-356c-86b7-e0a3863b3775 | -9.29907 | -56.81441 | 2026-08-17 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d467fa84-4e63-3640-9628-66e47ca7a52d | -7.3751 | -55.49855 | 2026-08-17 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9215282-c7d7-384a-86bb-3d6f2491cd1d | -8.62994 | -54.72124 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a7e123e0-a699-3c95-8c63-e60ebe7b2bcb | -9.19965 | -60.79318 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d688c009-ddb7-3399-a06c-d8fe2cae09a1 | -6.48473 | -55.8971 | 2026-08-17 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03e97bcd-eda3-3533-acd6-3037a5c44a8a | -7.42039 | -60.00898 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 113b6b3b-07b2-3794-af89-b72be495b931 | -6.65891 | -58.96846 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4497235d-cf86-3893-a1c1-8557f85a41fe | -8.526 | -54.91426 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eea6615-8782-3199-a987-0c07a159d65d | -7.3766 | -59.95116 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45058724-ed65-3bc1-b80b-676dd1874357 | -7.55391 | -61.17536 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dc32254-66c6-363c-96f9-b2da017bf3d6 | -8.5595 | -54.59367 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd2f1854-80e0-3d01-8211-b481b25f9ad5 | -8.0892 | -61.36129 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b20129c2-de22-31b2-bd78-03ff5d5a8ff7 | -10.46522 | -46.30741 | 2026-08-17 05:16:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8dceba70-9ba5-3f62-a0dc-60ae8dd2a76b | -8.63741 | -54.69617 | 2026-08-17 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d77fb148-1aec-3b66-9943-c2789350c18f | -8.95678 | -60.52614 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4dac808a-6e0b-3696-b902-de352cda86bf | -8.06239 | -48.53333 | 2026-08-17 05:16:00 | NOAA-20 | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5983befe-6d11-3d84-8f79-c6bbd214e8d9 | -8.95045 | -60.52111 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c83dc07b-d181-3d88-9b28-d2955dfebd06 | -8.98037 | -60.50075 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 018d1000-d581-38ac-9b12-1b2177c5c4f0 | -8.98256 | -60.50906 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| eafdec38-9d1b-3b0a-8bc1-72a352af4001 | -7.5553 | -61.16682 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c740e2f-3cd3-3cf2-85d9-454b12b359e4 | -9.47532 | -51.66348 | 2026-08-17 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3a56eb5-2c39-3d4f-b033-8506c92d7f19 | -7.61417 | -60.95046 | 2026-08-17 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cca7aae5-af3b-30bb-a329-b304e927d088 | -6.65554 | -58.96792 | 2026-08-17 05:16:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d468e15f-828d-32d3-afc2-39fde1be1fab | -8.9435 | -60.51996 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 630a5d64-67db-37b1-945b-412a3ce7811d | -9.05138 | -60.39425 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| adc40a1e-e08e-3c40-b86b-01f1131c5080 | -9.1787 | -59.67747 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df4111b4-9eff-39da-9a35-d0cc318313f0 | -8.97497 | -60.51177 | 2026-08-17 05:16:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
