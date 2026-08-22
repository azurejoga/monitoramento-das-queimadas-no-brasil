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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8731ec9e-d60b-3574-bb16-785ece1e3aac | -6.39573 | -54.95422 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 127a3cbe-2542-3b18-93b5-9796f6a8bab6 | -11.73585 | -45.58554 | 2026-08-22 05:04:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3708dbcf-bd19-3dc8-a64d-4ef612cd24bb | -6.88867 | -59.42717 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 521061dd-8231-3108-af02-ed3f9045b0b3 | -6.379 | -54.94753 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b17b4b7-0e40-3879-851c-b984bc59c04f | -9.0686 | -60.43035 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8e5a4fa2-a0c4-31b0-ad68-af8c61c02550 | -6.55436 | -58.51613 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0165eb1-a254-3a47-b5fe-d630f63b9aa9 | -9.11558 | -61.60401 | 2026-08-22 05:04:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c2181970-9485-300b-99d1-0cd82a57e52b | -9.17926 | -59.465 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 16ac85a4-94ad-359c-9d07-eb2351ee7f86 | -10.90203 | -50.23555 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 252f9021-e80c-3a81-9690-c8b1b63416c1 | -6.38061 | -54.95956 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2abf4cfd-be8b-3144-8ebc-f6eac9fc20f5 | -12.01406 | -53.42964 | 2026-08-22 05:04:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ad15c0f-e1cd-3896-bd30-84bdbeb5acd6 | -7.69977 | -46.15422 | 2026-08-22 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88b3ba5d-d437-3f16-8a7b-b4ca32fe0efd | -6.76035 | -58.67968 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 799f1797-0210-33f0-a2b6-6520415a215d | -11.10289 | -49.88903 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f580dcd-c963-3baf-a4b2-ebc18091143f | -8.57446 | -54.79251 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 863d54f4-f86d-3db9-9ff7-4fbde3ac399e | -6.65506 | -56.33909 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82bac2fc-59e0-3cd9-9d77-ad6e236491ef | -6.23164 | -55.41231 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 339d441b-7904-36d9-8210-0e5951041189 | -10.29476 | -50.39123 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6839f03-04bd-353e-a68d-5853f4065a26 | -6.13373 | -57.75028 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c8adbd9-e7ce-361e-8c06-df87a17db272 | -6.80079 | -59.66289 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1bf3fc2f-953d-34e4-94dc-870de5743ebb | -12.84187 | -48.45617 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0631d63d-022e-3db5-8ca8-9ffd1194e5d1 | -6.97073 | -59.05906 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb83d576-61f9-3b9d-bff2-7955830ea085 | -8.5201 | -55.3225 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4f55a713-c419-37b4-8d85-4c3bcb27e8d7 | -9.1663 | -59.46272 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b93a300-0781-368d-90ef-ea3e23a9765e | -6.37484 | -62.90477 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c47e296e-ff98-3dd5-b840-f3b1d7265a67 | -6.42682 | -54.92735 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1f835e9-a0d3-3054-8054-aaf96d819234 | -11.49215 | -52.91923 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 28152699-da54-3aa5-8b1f-7bd0a7f2c4f9 | -6.81068 | -59.65987 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b406d13-dda2-3897-a696-8c3a3e42cfde | -6.82002 | -59.65894 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6da1f624-8ca7-30ff-80c4-838eb92c90ff | -6.00063 | -57.8009 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f0a7f90-f0cd-3ebf-97af-ad9494a17e38 | -6.89702 | -55.38229 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adcd47fb-5d22-3bd9-b4b0-08f3c559683b | -10.94896 | -49.59311 | 2026-08-22 05:04:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78c25a77-4342-3741-a09a-2c49779e4704 | -8.45826 | -51.55685 | 2026-08-22 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02d80171-fd67-3826-aa5d-48b88064a676 | -11.95083 | -45.48936 | 2026-08-22 05:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0d1f4aab-b664-3e5d-b021-dfe8089e32f8 | -6.77021 | -58.67321 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35ad282e-369a-3c99-990a-ddecdca672ae | -11.39345 | -47.20139 | 2026-08-22 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2e6d2d8-1455-3e05-8825-d8d09de59b46 | -9.06223 | -60.43917 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7de7a9d-2761-3cda-9de4-9561a3f882a4 | -8.10287 | -50.04404 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be8ec4bf-bf4c-3d83-bd8c-575a0bd97f89 | -6.00227 | -57.81606 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 42990eb0-2a45-300e-a5a5-245abd1f47e3 | -6.10661 | -57.73816 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64269101-b45c-3cc5-aaf7-7721d6e59ecf | -6.75834 | -58.69167 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef1c608b-1f79-3647-9844-a0f1f8dc8533 | -8.10585 | -50.04878 | 2026-08-22 05:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4fb0b30-f6e9-3b6a-a835-f74608f59629 | -10.1622 | -54.28872 | 2026-08-22 05:04:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c935dff-cf54-3335-81e6-366bc4925365 | -8.51665 | -55.32192 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6043d2b0-3075-3eef-aafe-b24787e793a2 | -9.165 | -57.0098 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8f401ad-0f91-3102-aff2-19bff978a213 | -6.22774 | -55.48167 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e01e60f2-604b-3e0b-93c2-ff6604bf2ada | -7.2544 | -49.91766 | 2026-08-22 05:04:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f9cd6f4e-2218-39d1-a27e-e34a67384d6c | -6.36845 | -62.90763 | 2026-08-22 05:04:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a18ef543-bbcd-3b5a-9185-40939b0b3310 | -6.84936 | -59.4318 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60c2b07a-465e-3725-861d-811e058408b1 | -13.44889 | -51.76301 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ebd05e94-bf61-376b-a009-0930610c8d9a | -9.18934 | -59.45829 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0fd6c823-4866-39d8-bff8-46684b99ca6e | -9.03199 | -45.88307 | 2026-08-22 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4335404f-4849-3028-a4f1-b2ee0190e2f9 | -8.1768 | -54.98134 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87ec2a2e-81f4-3df0-884b-8eddb254a943 | -6.5714 | -58.97356 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3b7f141-2f47-3755-90a3-ec6b6745243f | -8.69229 | -54.62865 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a2c9f1f-620a-3deb-9d46-dd6af3ac61b8 | -6.75451 | -58.66225 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 29ba785e-65c0-32a9-ba43-529cd0c60872 | -6.91515 | -59.35423 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70ecd39b-8917-31ff-8324-b26135444adb | -13.44115 | -51.84005 | 2026-08-22 05:04:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62532b91-24df-3769-a695-efb74e7facf6 | -8.53574 | -54.81621 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4a5dd580-3d58-3c04-b156-caea9ae551db | -6.80148 | -59.44181 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fe4d146-15e9-3ba6-8b3d-8d8e3b011d7f | -9.16702 | -59.45859 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a91607e1-2ab8-3de4-b086-6e869de6c57a | -6.79895 | -58.62341 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 604b58fb-22d7-3b7b-821d-6bb9ace5bd02 | -8.16526 | -54.98743 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 376a66ca-9ab7-379f-a64c-f416f5f63602 | -6.12766 | -57.68727 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bcdcc535-3e4f-32d7-94c0-f36d91a92397 | -6.78428 | -59.43441 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bd158356-90f6-3c27-b0e6-eda3514561cd | -6.77788 | -58.66904 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d4606e1-6a08-362a-b6a5-e4f06a0caba7 | -6.91303 | -60.07049 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 338c1a19-256b-354f-8553-f043f3c8a80d | -6.37553 | -54.94696 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 704b92d7-a69c-3b49-90ea-381edcdc1427 | -6.22419 | -55.48111 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 812bcd24-d856-367f-a590-f62fb6af6f7f | -8.16121 | -54.99068 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6a08f910-6c4c-3110-b4a5-c0d6546e1c8b | -12.82314 | -48.46735 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95a8c5ab-0441-35fb-b671-afe871babe45 | -9.21888 | -59.77539 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7794652-6a8a-3bf5-866e-a0844a08cf17 | -8.53735 | -54.82774 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 379fd7c4-0e2e-3d65-9ff6-2042ca239cc1 | -6.0953 | -59.95092 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49fccb18-2b88-3bd1-b6d6-596e19740ddc | -8.58775 | -54.75344 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8389b80b-37c0-3fc9-a10c-bed179b40223 | -8.52072 | -55.31872 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd96c22a-21b5-354a-855e-f7ed7dba6cdc | -6.78585 | -59.42539 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bb9e25c4-b99e-3a5c-a5a2-7d9efe7a01ef | -8.02752 | -51.79675 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1335a69-662e-3f7c-92bf-8106a29e4d10 | -12.83657 | -48.46362 | 2026-08-22 05:04:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 88d78cbf-cae8-3a1c-98f1-3ab5e8db378b | -10.8032 | -50.97429 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f75fe22e-5167-388a-86ea-1d5f49761d6f | -9.43541 | -51.62548 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe0fc48-58e5-3bb4-8a66-b9110128bea2 | -6.43445 | -56.18751 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f08624c9-efba-3bfd-aac4-239ac3d30c6f | -11.3326 | -45.02887 | 2026-08-22 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43693527-1922-3d98-9ea6-e871e6daeec1 | -8.63197 | -54.70064 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f61bb279-b305-3af4-833a-c461f2e28d10 | -6.15516 | -57.74659 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40b2fa52-9d17-3d35-ace8-36769e688e17 | -6.79827 | -58.98833 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 866486f6-41f1-3feb-ba28-e9fb35c1f7df | -8.58835 | -54.74978 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9938c7a-1f80-3cd3-b677-25434b2ad1e1 | -10.76995 | -51.0023 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b81cd3a9-5c3e-3132-b5a0-54c2c0bcc262 | -6.13576 | -59.91174 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb844169-86c9-3957-a148-08291ef82d2e | -6.89896 | -55.72196 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a045c36f-1dc9-3ced-bd85-8ad44c8b642e | -10.52 | -50.82256 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cf986cf-c55c-3410-8965-931ac9863b3b | -5.74984 | -53.58155 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8423a4a0-639c-39f8-ad4d-2e74aff0bce9 | -6.25495 | -55.41908 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd62a8e3-0b70-3e51-bbb6-787e5136c83b | -6.39226 | -54.95365 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3363d8a4-303f-374c-b2b4-bbdc14427643 | -6.82133 | -59.67803 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 9976aeb7-2e7c-34d3-91bf-851a0bbdb851 | -6.22353 | -55.48518 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02381ea2-f850-3532-bf9c-119a13b8a43c | -11.10601 | -49.8942 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 313caad1-5a4d-3c0e-b76c-b8d6de74a7a5 | -12.66524 | -47.80615 | 2026-08-22 05:04:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f84b3d54-239c-3605-8daa-f290f41d0edf | -6.77712 | -58.65809 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4441ebdd-06a0-3fe8-b1b3-44857b2820d2 | -11.16009 | -54.01785 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README51.md)
