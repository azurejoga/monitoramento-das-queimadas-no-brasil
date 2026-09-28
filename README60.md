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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f7ff20e-cbfc-3855-bc9a-8d2789ac0611 | -2.91671 | -58.30848 | 2026-09-28 05:27:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3c26139d-ae9b-3d49-9df5-c18a1ec15ccb | -4.79603 | -49.11469 | 2026-09-28 05:27:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2d8ab37-1a02-3e76-846a-201aacf22611 | -3.45694 | -56.81216 | 2026-09-28 05:27:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 271b2a14-d49a-38c6-a5f9-82928f8601a5 | -2.44542 | -49.22655 | 2026-09-28 05:27:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f469468-3f49-3423-8ccb-892997435f5d | -3.01029 | -54.21896 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76ec33bc-1876-3f2c-af85-351c60ba5557 | -2.79478 | -57.67128 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 706c4878-9d6e-3ee3-9b63-294411987f83 | -1.74436 | -57.18326 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8a460404-816a-317b-b78b-22d129c30906 | -1.0455 | -53.5642 | 2026-09-28 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07e6e6a1-85e2-38c6-99f4-ebc533e20b78 | -3.1775 | -57.0919 | 2026-09-28 05:27:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 725e0b37-4d48-3fee-87a2-8e112e89cd69 | -2.78839 | -57.68971 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a455068-0807-3a2b-acd2-83072c6d704b | -3.41469 | -48.33416 | 2026-09-28 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 773aca4a-ce06-3ee8-8006-d240a0ab290d | -2.79761 | -57.69891 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0b61f5c-96f6-3c5c-a354-7bb4f1aba735 | -2.89685 | -54.17094 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f35b53e9-d563-3811-8482-015fd7e4b7dc | -1.92596 | -52.13953 | 2026-09-28 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5753db35-e2eb-39f1-9750-42158685e6dc | -1.04378 | -53.56278 | 2026-09-28 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 51c22743-cd59-374d-ab8a-9d21449f7117 | -1.04745 | -53.56751 | 2026-09-28 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c0f67bd-6ddb-33ce-b5cd-f0296b63917b | 2.91802 | -60.085 | 2026-09-28 05:27:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b7a272d-7fe7-3298-9255-49cc4ee866c8 | -2.66172 | -51.73775 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e7251a2-8a93-3da1-9a78-464e6b0a6e92 | -2.53076 | -57.22593 | 2026-09-28 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c978f11f-3198-3e9b-9846-0dfaa19ca926 | -1.97082 | -54.25577 | 2026-09-28 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a0fb940e-698e-323b-87cc-10a8b15d4cc9 | -2.92203 | -54.20196 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f9b04c1-2a08-3fbe-985a-3eb2bb141747 | -2.05347 | -56.87204 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 51321cc7-42fa-3c0b-85e5-73ae440e846e | -3.42032 | -48.33976 | 2026-09-28 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 10730214-0b1a-3e39-9ba6-de464432d39a | -2.05766 | -56.86857 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ae5eebc-1179-3907-a2df-6effac1bcb07 | -2.26875 | -52.01691 | 2026-09-28 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0226156-e887-35b6-925b-a306232ab4d9 | -2.78376 | -57.69677 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f72306a-fa56-3a76-807f-a135e5684416 | -3.35995 | -50.46939 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| eb5ee2fa-23bc-35d2-acd0-15a8a2e3fa18 | -2.56452 | -57.37903 | 2026-09-28 05:27:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95438132-76b9-3bd9-bf69-fc1aa5c6218b | -2.77407 | -49.48315 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d97a32a7-d10e-3f29-9ddc-a0b85b0a1981 | -1.0498 | -53.56477 | 2026-09-28 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0bbbfdd-26f7-3490-8912-d128a747dab0 | 1.6544 | -55.92051 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0458904-8329-3f7d-8bf9-622b61eafd3f | -2.54778 | -56.28894 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ad19a27-2c75-3f4a-930c-4187f172e4b2 | -3.14767 | -54.08036 | 2026-09-28 05:27:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e507f97-b709-3d86-9d3a-b4c8ffe791ce | -1.76956 | -53.76354 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7b581c7f-c70d-3dd3-8118-0f2aad1f0321 | -2.91573 | -54.12858 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4227f95b-a15a-31cb-b67b-4e9760354ded | 1.6781 | -55.95423 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76b916a9-dcae-32f1-9c27-5983da3d1016 | -3.29124 | -50.32297 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd9c8c6f-5a0d-3a85-ac06-f7c7379c8694 | 1.26953 | -50.69053 | 2026-09-28 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7819c22b-8135-3ea8-8fa1-23ada5c1096f | -1.77003 | -53.76939 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b9784ace-6b7c-3d68-a805-7f2067d474ed | -2.27031 | -57.01452 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| b555a918-f229-3ce6-92fd-a70d47ec493e | -1.26191 | -54.68815 | 2026-09-28 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24de7e3b-26e0-32e0-a056-effca1eded69 | 0.47853 | -50.93884 | 2026-09-28 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31522192-725f-3fe2-997c-5d26f5721f0b | -2.9085 | -54.12447 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 46e65bfc-5933-3a5f-9ff9-1a86c8831def | -1.77384 | -53.76419 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 60fee655-d8e1-3870-859d-4384475783ff | -2.8593 | -54.13311 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2582c552-488a-3963-973e-fcdd421f856f | -4.31184 | -50.3964 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fd20817-022c-35ad-bb3e-43b3216f7ad3 | 1.67745 | -55.95017 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c35c5e-0a32-33ef-8f3e-4963d52887e4 | -3.20713 | -51.03799 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c9395322-c0f2-3bd3-b171-e0914b494d88 | -3.67956 | -47.4938 | 2026-09-28 05:27:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 144281c0-a852-387e-b123-94f2e07aeb65 | -2.90781 | -54.12336 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 504f1cdc-9021-3b70-8729-41fd97501a2e | -1.92992 | -52.14188 | 2026-09-28 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e16eda0c-9fb7-347a-8b43-6775b22381b8 | -2.78493 | -57.68918 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8fd8a615-dc07-3e83-a92d-0d98bbdd4ef6 | 1.15497 | -51.16344 | 2026-09-28 05:27:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0cdf0d4e-9b7e-3698-8041-032ad2627874 | -2.90912 | -54.12052 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be7f6c71-9674-3068-8319-c27d3c1491e9 | -2.87032 | -49.63501 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b04a0ac-7b6b-3636-adad-eaca6891ada8 | -1.73736 | -57.18217 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 99497352-5ef1-3d2b-97c1-828ae6a0793c | -1.90781 | -52.06709 | 2026-09-28 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b4b56fe-d7d1-3f98-865a-e14ae2dae347 | -1.22943 | -54.09729 | 2026-09-28 05:27:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6a55f605-15dc-3596-8f18-99f4877860aa | -2.97352 | -54.14909 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 32f78641-8627-335f-82c7-7e13673d1c40 | -2.67048 | -56.45913 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6ef30943-6321-3ae7-be62-9c8fb6a7ef66 | -0.49959 | -49.12857 | 2026-09-28 05:27:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6da8f30-4b3a-3a5e-a999-e552ac78b2b8 | -2.65629 | -51.73986 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce0a8d49-d701-3c22-a461-a9988813ea83 | -2.67349 | -56.46399 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 15c6a5ab-5440-3dad-9287-6d42de10b6bf | -1.04914 | -53.56887 | 2026-09-28 05:27:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 961d458c-ff66-36b1-825c-f02316f11048 | 0.28328 | -50.90877 | 2026-09-28 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b85463e5-53fc-3d46-a146-0bd058fb3e64 | -2.92875 | -56.57884 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1491c0f-cae5-3e8d-b7bb-9d57c5ceb38c | -2.55479 | -58.04449 | 2026-09-28 05:27:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6911e8e0-587c-3360-863c-c556e7f30451 | -2.90667 | -57.3652 | 2026-09-28 05:27:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c77e51da-bdc4-3db3-adfe-88165695db44 | -2.76765 | -49.48632 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d43c30a-1b8c-37d1-a4d8-1781e78195ae | -3.33594 | -58.11337 | 2026-09-28 05:27:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a40d9983-e950-3f31-863b-9d35427465c0 | 0.47796 | -50.93925 | 2026-09-28 05:27:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a8b9436-acf2-34c1-b2d3-c1ba790043a5 | -2.55421 | -58.04816 | 2026-09-28 05:27:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 79833f10-8905-3ff5-a9ad-be19e3de662c | -3.41397 | -48.33898 | 2026-09-28 05:27:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 31a724b0-62a0-3fad-ae1a-187b871de916 | -4.31542 | -50.39613 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 888e6d20-ac23-31cf-ae3e-825dcf39b78f | -3.03178 | -57.51141 | 2026-09-28 05:27:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 087a13a5-9c8b-38d8-88aa-2bb49799604f | 1.67874 | -55.95828 | 2026-09-28 05:27:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83765cf4-7de2-35cc-8928-21cc4d9073f5 | 2.38643 | -51.02116 | 2026-09-28 05:27:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 76cd206e-86b6-3cc6-b8e6-4e2474934ff5 | -2.78318 | -57.70055 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bba3f62-e8e8-3bb1-a930-19c5e4236021 | -1.26243 | -54.6848 | 2026-09-28 05:27:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a5494bd-08e4-3668-9772-6ec32dbe6623 | -4.31436 | -50.4036 | 2026-09-28 05:27:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| aae91ff7-36b3-34a5-87ec-715fca20a858 | -2.54426 | -56.42786 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93df908c-7f3a-3e1d-988a-0e4194de0fc4 | -1.82102 | -55.31896 | 2026-09-28 05:27:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bc144f52-a145-3220-a42b-0810f4165e95 | -2.97775 | -54.14986 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 432c15d4-4473-3448-b528-75856e3db382 | -1.92515 | -52.14466 | 2026-09-28 05:27:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44e80fdc-3c79-357e-9c07-64d378ae427c | -3.29178 | -50.31931 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02a7cfa1-f1d1-3fb1-bc7d-5ecf4b279d85 | -2.98435 | -51.05664 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 863db9c9-bc5f-33e6-9be8-843e10f93cc6 | -3.23667 | -50.57934 | 2026-09-28 05:27:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f84997da-da11-3329-9c7c-fd189b5d1fdc | -2.92942 | -56.57459 | 2026-09-28 05:27:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf4580e8-4381-323e-b4ac-8a821b4f0284 | -1.77323 | -53.76822 | 2026-09-28 05:27:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 8517ff9f-cdf7-396f-b311-f5ad3d1e1319 | -3.19607 | -51.03967 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ebd2a55-4f22-3443-b09f-a11b2a8c8a43 | -2.06772 | -56.87422 | 2026-09-28 05:27:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a33de6d3-b924-3b78-8ad0-9b8a24d1fbd7 | -4.7892 | -49.1186 | 2026-09-28 05:27:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea0f140e-de2f-37b6-a41b-3f87f1cbb9d5 | 2.39175 | -50.9929 | 2026-09-28 05:27:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64caa061-cd68-31f0-a19b-1958525b5470 | -2.9178 | -54.20132 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42c853c0-f2f8-3246-bc3d-aca5bd683ce4 | -2.76704 | -49.49044 | 2026-09-28 05:27:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e48a7e88-0ec3-364e-af8a-f40a6cc34686 | -3.20086 | -51.04377 | 2026-09-28 05:27:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ccdcf5f-7620-3df7-bca7-6012c069f674 | -0.50535 | -49.12947 | 2026-09-28 05:27:00 | NOAA-20 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8863d093-2e4d-3e81-984e-d3f4d057d37e | -3.12835 | -51.73384 | 2026-09-28 05:27:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1d536b6-0c3f-3830-9c34-360795652b92 | -2.91148 | -54.12795 | 2026-09-28 05:27:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbe61372-5593-3785-b324-c613b22ad9e9 | -2.7849 | -57.69823 | 2026-09-28 05:27:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README61.md)
