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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f471de7e-11e6-3ea4-8dad-99407eea3a93 | -6.02442 | -57.68415 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 94df433f-7e32-3896-9ef6-1576a1fee5b1 | -6.65084 | -51.48556 | 2026-08-22 05:04:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd31210f-20d7-3917-bbaa-174894b33f2e | -6.76945 | -58.69217 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fbfcbe0f-f8cc-3d1a-968b-c998c4f4431d | -6.77115 | -58.69384 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ce5ffee-36d8-3e0a-9c9f-f902d34243f4 | -6.79738 | -59.60063 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32f673c9-75e8-30da-9394-6ce7f98189ca | -11.16173 | -54.02894 | 2026-08-22 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44771c42-fa40-3bc7-bee9-c326e38c2e0d | -6.37269 | -54.94255 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fab0395e-9f5b-31d2-bd9b-3b09c63785d1 | -6.37207 | -54.94638 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 102a2bc3-6754-3a47-ac55-8f1428f273b8 | -6.76733 | -58.70427 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e362a28-d20b-38ba-a4ea-ae53060fa1a6 | -6.15633 | -57.73951 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b70a632-7781-360a-a45c-c0c42f4efd36 | -8.62262 | -54.68824 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 198948af-3c3b-3121-88d3-d0ef0f059a92 | -6.85924 | -59.46329 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 3651b88c-fcd5-3809-8ec9-29fbaeb17229 | -8.53272 | -55.32394 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e001b1b-671a-3dd9-80e7-9eafa1d3d340 | -9.4239 | -60.41903 | 2026-08-22 05:04:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43e2399f-8872-3275-8470-386b9783fa56 | -12.28375 | -43.15561 | 2026-08-22 05:04:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c688056c-95cf-3515-996d-c24636595c07 | -11.94532 | -45.49186 | 2026-08-22 05:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76d2845d-9769-3d4c-b1fd-446a3f74b44d | -6.80008 | -59.42319 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 62d4f28c-cfc1-3fd5-be2d-c9488cbe92bb | -9.0635 | -60.44278 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8165056-5cdb-3b39-a687-37063eba7c31 | -6.79056 | -58.64652 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| eebbacd7-f5e6-375e-86b1-5cdafc997317 | -8.89354 | -60.54894 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 28d29cf5-6303-3ed4-a73d-0cc700dee54c | -9.21965 | -59.77108 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35df23d2-c2dd-39a9-8bdc-ff8e820ca352 | -7.34314 | -55.69959 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcf7a365-1e37-39bd-9d77-1649bac30d6b | -6.86657 | -59.41179 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eccad6d5-e3e6-3417-9887-eeda2f1dc32e | -9.44217 | -51.62265 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682c503d-ea48-3a19-99d1-18cb7babe20f | -8.40054 | -62.69045 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72b68688-52b0-31e2-9dc6-e2a4b86f601c | -6.76795 | -58.66055 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e63d9401-0e0e-385a-8ef1-47e5070da033 | -9.04697 | -50.87435 | 2026-08-22 05:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0bb09be2-fcbb-3c75-a689-9df42318c38a | -7.00126 | -59.58889 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40bc45e1-a88c-3efb-a68f-6a52f361e958 | -8.61897 | -54.73247 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5c5d1a17-1439-35da-8365-5fe34bec57ab | -6.82401 | -59.41816 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1d7c823e-3b28-396f-8557-cd495b51589e | -6.8098 | -59.42032 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d33f51ed-aad7-36be-a8d0-91a82f8802fb | -8.53634 | -54.81256 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c401abf9-f5a8-36af-9014-8096de6d5300 | -8.53335 | -54.83084 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ccb36bc6-a1f6-3b21-a65e-cf22c83c253f | -10.78527 | -51.02116 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bb858fb4-7c1a-39b9-a3ce-c84d6779beef | -13.43705 | -51.84351 | 2026-08-22 05:04:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2631f62c-0410-34c5-a290-749069291fb4 | -6.86288 | -59.03344 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e9a2efc5-5c49-34ca-bab1-e1be377d6543 | -9.17421 | -59.46838 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 398da699-34af-377e-bafd-dcd0f4dea224 | -10.68481 | -50.29625 | 2026-08-22 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 198d3f99-0adb-387e-81a1-0d46fb238a72 | -10.27419 | -50.37942 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f40be466-4664-31e9-a891-6fff5d677fe2 | -8.89442 | -60.54397 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 7d5a7eef-98a4-3b66-99f6-269702e42d1f | -6.01404 | -57.79586 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc045531-f392-3624-af62-74acbee53c50 | -6.21707 | -55.48001 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee095841-74c0-3454-b7c5-c9a9c42c36c9 | -5.90283 | -61.29356 | 2026-08-22 05:04:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0c0b3aa-4e19-30f1-99b9-df2b83d15dde | -8.54015 | -54.83196 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f851cd80-7803-3ee8-b69b-effb5662f10f | -7.37494 | -59.95164 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4db0d81b-8f4a-32f0-8094-1daec62d4cbf | -8.17275 | -54.98462 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0bc8906-d996-3427-91ef-eee0542f2617 | -10.30639 | -48.22422 | 2026-08-22 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 476ab3b8-dbd9-3f0a-9615-b90b4e59375c | -6.77223 | -58.67626 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 349bccc8-5dbd-3db2-b446-52b6c3fe192c | -9.17765 | -57.00264 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c4cedbe5-81c9-306c-b5a8-247238fce286 | -11.60065 | -46.55164 | 2026-08-22 05:04:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4f6e673f-dc62-3aa1-9aa0-56d1d665d873 | -9.16557 | -59.46684 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1cbf224e-f3d4-332e-8943-5430526d75da | -6.64696 | -56.34216 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b24a2ea6-8b81-39cd-9d4f-766722a816c0 | -6.81659 | -59.40772 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a3b864e7-33f1-3f63-b53a-4e1e608190e1 | -6.9779 | -59.58936 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d22d5d85-7e0d-3f03-b298-4a1da97b51f0 | -10.94532 | -51.41707 | 2026-08-22 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73f1c99f-bf88-3975-8d31-5390b1d97a17 | -10.30324 | -48.2166 | 2026-08-22 05:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 408e7b68-1a83-3054-8ba2-80c114a3fb9b | -9.16848 | -59.45033 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74c82e63-e3c9-3428-b310-a69c4e02e892 | -6.43078 | -56.1869 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf22c346-1fbc-37cf-ad4e-0c967081eb3e | -6.13927 | -59.89994 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62ccdb11-7d61-3117-b289-1e5bd53dc6f3 | -6.19239 | -52.37179 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5026009a-0bf9-33fc-960c-636a94aa482b | -6.88108 | -59.44417 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 42bb5b85-6476-39a7-8386-4cd56cfa13a4 | -8.22544 | -55.0281 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c50fe78e-19c3-354e-b9f3-ec56a4cf7802 | -6.42952 | -52.71513 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0447feae-6016-301a-a9ce-7c595fcb9914 | -10.2748 | -50.37516 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec1624a0-b529-3101-bcbd-0e8ae7b44fb4 | -6.6938 | -59.10234 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75e443bf-bdab-3620-b7c2-5e51ce677822 | -5.9632 | -51.95747 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11a37f01-f277-3614-bd40-6e5b1dcb18e9 | -6.09698 | -57.86956 | 2026-08-22 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e18323f-f159-3a74-a8b8-690e6fd1f37d | -6.76435 | -58.65586 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c9a7b2c1-de97-3bfb-865d-43c846b00a3f | -6.76662 | -58.70832 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2484e76-3a9b-395d-9408-3bdec1ab0b61 | -8.40598 | -62.69144 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97415d0d-5c0d-3035-bb2b-ad6851fc10b7 | -8.02588 | -54.01452 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fe907a8-d952-361d-8431-b769dfb20d7b | -10.96397 | -51.41196 | 2026-08-22 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b663a06-415c-3912-884f-0b579c580c36 | -8.61838 | -54.73612 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 65aef7bf-a2db-3c7a-890f-67ac6f266bcc | -9.04338 | -60.4487 | 2026-08-22 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3f17b16-8a14-31e3-ab69-ad95cffe862c | -6.78135 | -59.4247 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| bbcb627f-8a93-375e-85a0-34f022c6b814 | -6.82654 | -59.67702 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d228022e-4d79-319b-9814-16152215491a | -10.86298 | -51.05218 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4f9d83f3-60eb-30aa-b236-3ee6cd9f15b1 | -8.52835 | -54.81874 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 34602278-566b-3403-995f-97f672bcbdd9 | -8.54151 | -55.31373 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ad73fb9-323d-34ac-8726-53cbef5be783 | -6.97337 | -59.58865 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f574e1a3-7b08-341d-8be5-66d2a16094b3 | -8.6294 | -54.73757 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5f9b817-4512-35ea-b10d-06153eaed173 | -8.51604 | -55.3257 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b53847bc-94f4-3acb-a372-89e538a1598f | -11.38807 | -46.35564 | 2026-08-22 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e121f32-d28c-39ed-bd60-851d0194d002 | -6.79263 | -58.78712 | 2026-08-22 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46427e65-5251-3390-9095-f10e80a906b3 | -10.81619 | -50.98455 | 2026-08-22 05:04:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 22b28ab2-a526-3516-aa30-0e98c8af32e6 | -8.6316 | -54.69716 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20c25fb0-71a6-3437-9f4a-1f91bf6148c4 | -8.40726 | -62.68444 | 2026-08-22 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 08080ef0-3c57-3fe4-b519-84b5b859183c | -6.37677 | -56.10292 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2aef0baf-3e4a-326f-b7d2-d28149f41326 | -6.20737 | -55.63964 | 2026-08-22 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 717674e0-05cf-3355-801d-893bd0e71230 | -8.19114 | -54.97966 | 2026-08-22 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 555de031-44d8-394b-aeea-e9e0f65b27b1 | -8.02415 | -51.79623 | 2026-08-22 05:04:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee00f766-d9af-344e-8eb1-f1d858519bec | -6.85316 | -59.40939 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f2f3ed1-f6ca-3b76-b26c-2a15d9e6894f | -10.5232 | -50.77714 | 2026-08-22 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c9243670-74b1-3c74-87a3-60acd716435f | -6.76772 | -59.4498 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 408bf71d-c73f-3edb-b977-3ca6767e9a51 | -6.43234 | -52.76174 | 2026-08-22 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 096c58b3-63b5-3649-9f25-8738712367ce | -6.12174 | -59.91724 | 2026-08-22 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d124e06-ce41-3fc2-bf47-b9ece97d23fc | -7.47294 | -45.1464 | 2026-08-22 05:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a56d2e05-3535-3a7e-ab91-23545dce89a7 | -7.34422 | -55.67078 | 2026-08-22 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 77fcb0e2-e4f3-3119-8f21-7326471a8803 | -10.43558 | -50.47153 | 2026-08-22 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b97f6a1a-812a-3c94-b13c-e94c8535e99c | -6.95839 | -59.05258 | 2026-08-22 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |


[Clique aqui para ver as próximas entradas](README43.md)
