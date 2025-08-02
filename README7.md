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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 259cefd1-192a-388b-addb-1bc704172bb6 | -12.66669 | -44.54047 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6b66960c-4141-36ee-a52c-1089bf31f3f6 | -18.21063 | -44.71596 | 2025-08-02 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 84ad9f63-128f-3071-ba24-81e2d4b15219 | -12.6653 | -44.5079 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d5c38c2f-0290-3c11-bc73-82b3be547d52 | -12.67542 | -44.51945 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac7d5808-a095-32cd-ad29-9d74c5403178 | -12.66219 | -44.50195 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a487915e-728b-3831-83ac-d99808ac4905 | -18.21766 | -44.70964 | 2025-08-02 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dfde78d-681c-34f0-bd82-b665e3da1766 | -12.66293 | -44.48862 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e171368c-a7b9-3845-a6f3-dd5bfacf4f56 | -12.6581 | -44.49171 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2f3bd8e4-235c-3ceb-be12-4ca2e4a72138 | -12.66204 | -44.49311 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ae5ae709-af8d-3d3d-9b9a-699563651789 | -13.22149 | -42.25232 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eec522fe-c81c-3411-be44-daaf8aefd592 | -18.24348 | -45.16792 | 2025-08-02 03:34:00 | NPP-375D | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5ea12e3-5419-34a5-85e1-60c1f7aeefcd | -12.67181 | -44.48532 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cb7db296-2871-3f1b-9f3b-fe9eba3a6c6f | -19.57387 | -40.78903 | 2025-08-02 03:34:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e55bedde-0634-3b6a-8df7-c600fb19e62d | -16.2467 | -48.96203 | 2025-08-02 03:34:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d7bfdec6-cf91-3dea-8d8a-b64a1be57535 | -12.65699 | -44.48734 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 062c5d2b-f078-31e9-83ee-e2ba10e410f4 | -12.66035 | -44.51091 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a06805dc-9ef2-3f7c-9570-d5dfdaada0d0 | -13.17236 | -42.2317 | 2025-08-02 03:34:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4aa7842c-df20-3728-8142-f249efb59397 | -12.65343 | -44.50524 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| cbf5fd73-fab4-3d06-ac6f-de5e57842a9a | -12.66762 | -44.53595 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c7e24d2-ad70-3f15-8d48-8e5a5c1e3c1c | -19.69009 | -41.01861 | 2025-08-02 03:34:00 | NPP-375D | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| be7f5e61-4cbd-343c-87a5-0d8c10fe37fc | -15.37467 | -44.28125 | 2025-08-02 03:34:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2adba6bb-f3bb-3772-8200-110488de8111 | -12.65533 | -44.50511 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 969ed448-6fed-336b-a6c5-b445366a2524 | -12.54737 | -44.72109 | 2025-08-02 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a17bc9c4-1bd9-32c6-b6ee-0cd6800e8726 | -16.24539 | -48.96461 | 2025-08-02 03:34:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b0e25599-191f-3de1-9657-90e4e7e92298 | -12.66382 | -44.48415 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26d189cb-405c-3f83-b100-7368bcd3ef41 | -13.89728 | -42.12983 | 2025-08-02 03:34:00 | NPP-375D | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 214659a4-0d0a-320a-8ae0-66496a0b5ed4 | -18.21136 | -44.71251 | 2025-08-02 03:34:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7f2dbc7-9e98-3699-9713-5aeec28f1555 | -12.66721 | -44.50773 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e9e9370e-c1fd-3bcc-80ba-1ec80bcdbf7a | -12.65718 | -44.49617 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 29814e1d-8d52-36e1-97f8-78b935ce0a8f | -12.67124 | -44.5092 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 03adf2ba-6caa-31da-8a37-24fb9d553198 | -12.66976 | -44.48542 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 49a62e9c-50d6-31c0-8e33-d6d5d92cc480 | -11.9403 | -46.68005 | 2025-08-02 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ad9a711-d5da-3068-b078-356832f1cf19 | -11.95656 | -46.67065 | 2025-08-02 03:34:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c0ed0f4-74c5-355f-b51e-6d52e3237501 | -16.69076 | -41.01844 | 2025-08-02 03:34:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8b274077-a70a-3996-a717-19d0dc20d0fa | -12.54037 | -44.72449 | 2025-08-02 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7c0fd2b7-1feb-3a0b-957f-376fbf2e86d8 | -12.66441 | -44.51238 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| f64cd6d2-61a8-3974-80b9-1fab45ebc4cc | -12.65902 | -44.48726 | 2025-08-02 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5af83cee-f3b2-3b3e-a30b-f47ac5c10334 | -21.19974 | -44.99644 | 2025-08-02 03:36:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0b790b93-6386-34e3-98d4-984d513d8ef8 | -22.32204 | -48.71735 | 2025-08-02 03:36:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1f485871-3cce-3911-a07c-ac99325e2279 | -21.65917 | -46.93341 | 2025-08-02 03:36:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 96245ad7-4a06-341d-a891-cc93bf1ab0fc | -20.32066 | -46.63013 | 2025-08-02 03:36:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f44ed05a-1b68-3de5-b795-518f28b5dd41 | -21.54047 | -48.72462 | 2025-08-02 03:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8909c0a-38c7-3f01-9535-7eeabea6d8f0 | -22.32328 | -48.71489 | 2025-08-02 03:36:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b97f1722-4be1-3c2f-856a-7f06f61e3c0e | -20.07368 | -45.81963 | 2025-08-02 03:36:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56df2c26-1297-3a08-aa20-0216b5d85a32 | -23.70764 | -51.65389 | 2025-08-02 03:36:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 91c2b8d3-ce7b-35e2-b518-8cc9353a161f | -20.45515 | -46.41002 | 2025-08-02 03:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 528d9f3e-0a6d-39d1-802b-fcd61cb8f206 | -19.76114 | -46.03965 | 2025-08-02 03:36:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88322ad6-4795-3e28-bb2b-2ddcbd78ef2f | -20.32293 | -46.63041 | 2025-08-02 03:36:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ccd9953-9da6-315f-9f19-39741e94ffa0 | -22.32829 | -48.71935 | 2025-08-02 03:36:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 51242e4f-f92c-32b9-b72b-bf4a5a310543 | -22.40435 | -46.7871 | 2025-08-02 03:36:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d297ad8-3da2-3b85-b129-72b30516a3b8 | -21.54683 | -48.72659 | 2025-08-02 03:36:00 | NPP-375D | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40442c32-3e7d-3bbf-a9f3-924cac64a5aa | -20.31593 | -46.63416 | 2025-08-02 03:36:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae77072c-5d89-3d1e-b651-25c56fe2df30 | -22.74079 | -47.03156 | 2025-08-02 03:36:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8052020e-0dec-3f08-b4d8-0820c0977132 | -20.31972 | -46.63419 | 2025-08-02 03:36:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce2b9990-a1df-38b1-8bea-3db7a7aa7aa9 | -20.79531 | -41.12688 | 2025-08-02 03:36:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 70a8dae7-f967-3745-8ca5-2f3b5851780c | -21.66492 | -46.9351 | 2025-08-02 03:36:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b1e0685-fc49-3835-9a8c-fd10e1a22775 | -20.07018 | -45.81971 | 2025-08-02 03:36:00 | NPP-375D | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e04553b-5ab8-3269-9d11-453f03d43902 | -21.66258 | -46.93605 | 2025-08-02 03:36:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1129c643-2c7f-332a-8391-938b6ed98ddb | -20.45426 | -46.41388 | 2025-08-02 03:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f96d58b-7952-317b-8335-2b70ef873eb8 | -19.76035 | -46.04321 | 2025-08-02 03:36:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3286ff0d-884a-3195-a52e-af6212a83a4b | -21.03961 | -40.8502 | 2025-08-02 03:36:00 | NPP-375D | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| fa478bf6-34e3-31b0-b0f8-352366e7aaa2 | -20.45565 | -46.41277 | 2025-08-02 03:36:00 | NPP-375D | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f9859f5-52dd-37d8-81ae-c5e549623868 | -19.75479 | -46.04114 | 2025-08-02 03:36:00 | NPP-375D | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3124faa-06d8-3462-881b-f2b0a7cce559 | -21.13993 | -48.0186 | 2025-08-02 03:36:00 | NPP-375D | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d4f0482-129d-3937-ae20-68f62796bbb3 | -21.66355 | -46.93189 | 2025-08-02 03:36:00 | NPP-375D | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d4dbb5c-5888-3885-8a48-f219df3e1be1 | -22.32187 | -48.72062 | 2025-08-02 03:36:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e7d91d84-b9de-3cb7-bc88-8c5a67374855 | -21.19448 | -44.99544 | 2025-08-02 03:36:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f72ba02-ad57-3ad9-9c74-c20f94c1476b | -22.74181 | -47.0272 | 2025-08-02 03:36:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4dff51a-151a-3d16-98f9-79dd89260e2e | -20.32203 | -46.63446 | 2025-08-02 03:36:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6c27217-0ca2-308c-a174-580f6fc9e4e5 | -22.4019 | -43.43591 | 2025-08-02 03:36:00 | NPP-375D | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 72b4c0e0-7ea9-3b2b-8b72-a237faca1041 | -21.20048 | -44.99298 | 2025-08-02 03:36:00 | NPP-375D | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec6f3498-9ad6-3f91-b354-3c177c1bbdaf | -22.40337 | -46.79137 | 2025-08-02 03:36:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c63e1525-440e-35d1-b303-ca5796464b97 | -28.9138 | -50.1693 | 2025-08-02 03:38:00 | NPP-375D | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 94ebdfec-d481-3f60-9622-d4d8f08892fe | -9.1937 | -45.2886 | 2025-08-02 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9ebf4caf-71d5-39cd-93fd-7f156025fad9 | -12.6595 | -44.4882 | 2025-08-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 46ac4c75-4be6-36cd-87c6-a356ccebfd3d | -8.0513 | -43.1001 | 2025-08-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.9 |
| 364f50f6-6680-38c1-b5d8-a57e4f591e26 | -12.6591 | -44.5117 | 2025-08-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| f60bd83b-4533-3e7a-b6de-1a80d435ad9e | -8.0324 | -43.1022 | 2025-08-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 70.1 |
| ce475d0e-b2bf-3fe8-8706-74de7bc51322 | -8.0321 | -43.1257 | 2025-08-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 119.5 |
| a76f46b4-d3de-37ef-8f85-eb5338c39717 | -12.6784 | -44.5085 | 2025-08-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 14a94eab-2ed2-3543-97dc-f73c51240393 | -12.6789 | -44.4851 | 2025-08-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 2478941e-0d13-38ae-8f40-de1b759f7d8e | -8.0318 | -43.1493 | 2025-08-02 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.8 |
| 99377a81-b71f-367a-898a-eb85835d5fdb | -12.6595 | -44.4882 | 2025-08-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.3 |
| a08785e9-d095-3dc8-bd31-a1993e8d5f77 | -8.0513 | -43.1001 | 2025-08-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 8c525f1b-c7d9-37bc-ac7f-4c084e2a9721 | -8.0321 | -43.1257 | 2025-08-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| db9927dc-ac7b-3db6-89a5-d5a3e428b434 | -12.6784 | -44.5085 | 2025-08-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| a1c146b5-b74e-3b05-b24d-e492671e344e | -12.6591 | -44.5117 | 2025-08-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 43cb356f-188c-312b-8a16-6f03f291014e | -8.0324 | -43.1022 | 2025-08-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| d6c7ea9a-0759-38d7-b116-f45b7c783237 | -12.6789 | -44.4851 | 2025-08-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 7b945308-fd67-3b38-ac52-218edc94dd98 | -8.0318 | -43.1493 | 2025-08-02 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.9 |
| 1d5326d1-575e-3854-83fb-e16a936a8523 | -2.87973 | -40.30033 | 2025-08-02 03:51:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53c239a7-f833-3342-a40d-5e9ab1257ee3 | -2.83645 | -42.11446 | 2025-08-02 03:51:00 | NOAA-20 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aae2e13-80d0-38b2-aaa2-0560cd03d03d | -3.29942 | -40.01528 | 2025-08-02 03:51:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 368e5bb5-ea80-3ec7-8aa3-7e946c173e50 | -2.941 | -40.09461 | 2025-08-02 03:51:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 61266502-84b4-33c7-be66-1e022080b604 | -2.88324 | -40.30089 | 2025-08-02 03:51:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1f8f06a3-0097-344f-a1d4-4740c049c2b9 | -2.83513 | -42.11668 | 2025-08-02 03:51:00 | NOAA-20 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3166c69c-8839-3dda-b43e-0e4aaed2ca69 | -2.93691 | -40.09791 | 2025-08-02 03:51:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 411dd93c-feba-3620-95e8-759953e62043 | -2.94039 | -40.09846 | 2025-08-02 03:51:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| da4f9a78-2cf0-3d77-aff0-9e9bab9e2c3b | -6.52882 | -42.81072 | 2025-08-02 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e112a6af-2ad1-34dc-a139-30b6a3f6a20d | -3.59861 | -44.79356 | 2025-08-02 03:53:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README8.md)
