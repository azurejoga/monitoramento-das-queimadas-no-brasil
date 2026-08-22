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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2dacc1d7-5d08-3054-b411-10cd699c5859 | -8.5218 | -54.8411 | 2026-08-22 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7312663f-c339-36cf-8e8e-5c474c69f2c6 | -8.9042 | -60.5385 | 2026-08-22 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 12a236af-cd18-3282-ba28-409f37f25fbe | -10.259 | -50.3265 | 2026-08-22 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 38bff864-8fb6-3b08-82e9-dfe2a0eb3881 | -9.1538 | -59.4446 | 2026-08-22 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| e23dcbfa-a715-3e6a-948b-be282e349ace | -9.1536 | -59.464 | 2026-08-22 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 58051174-07b6-36ec-a3b0-94c4d7ec3537 | -5.9997 | -57.8054 | 2026-08-22 02:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| f03def8c-c7d2-3de0-982c-cde67d29a03c | -9.191 | -59.4425 | 2026-08-22 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2347b5c7-6aac-35f6-9363-598de30b2cff | -8.5406 | -54.8197 | 2026-08-22 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 14eb3a59-5f00-3271-b9ad-9391dc166312 | -6.97 | -59.0465 | 2026-08-22 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| ed39bfcd-d207-325a-a550-be156ffc5f57 | -8.5404 | -54.8398 | 2026-08-22 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 867ebfbb-f21e-346d-b141-8a4fb5d2fb35 | -6.8569 | -59.4564 | 2026-08-22 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 2dda3e02-e60f-3493-bd09-6193a4e267a3 | -8.522 | -54.8209 | 2026-08-22 02:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 5a493bf7-8141-3604-a56b-b691acee0f00 | -6.8188 | -59.6696 | 2026-08-22 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| e55ffddc-4d9c-3686-9488-b457b6b1ba24 | -6.9699 | -59.0658 | 2026-08-22 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 354eba34-f1e6-3198-bca1-e6b2c38a7edd | -9.1722 | -59.4629 | 2026-08-22 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 193.1 |
| c62b3209-cf97-3659-bbd1-f73e95adb2e1 | -17.9613 | -42.728 | 2026-08-22 02:20:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.7 |
| 066c9563-55a9-3c29-8bc7-8f8bd515dec9 | -6.9699 | -59.0658 | 2026-08-22 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 52422e08-96d0-3f26-9016-afb166a5284f | -6.8188 | -59.6696 | 2026-08-22 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 39aa33c6-386f-3f1d-af47-3424a2d10707 | -8.5406 | -54.8197 | 2026-08-22 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 3fece0dd-34b1-3073-8555-81b97a0d6152 | -6.8569 | -59.4564 | 2026-08-22 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ceb530ab-e4b3-3ba1-b0be-44452b23f091 | -9.1722 | -59.4629 | 2026-08-22 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 219.8 |
| 3212f974-0066-310e-a489-c3722c3737fe | -17.9613 | -42.728 | 2026-08-22 02:30:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.7 |
| 6eee4279-efa5-3c2a-8efd-780fef33913f | -9.1724 | -59.4436 | 2026-08-22 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 38026e5d-2f6d-323a-b7ba-35af31d37251 | -9.1909 | -59.4619 | 2026-08-22 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 7089114f-f97a-3602-aba8-ce93e21c3f8c | -6.97 | -59.0465 | 2026-08-22 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 108.5 |
| fb57927d-41ea-386f-98c0-09ebe5ea07f5 | -9.1536 | -59.464 | 2026-08-22 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| b3250691-dc5c-30c2-a5ab-65ba9f1d96ee | -8.522 | -54.8209 | 2026-08-22 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 134.1 |
| f3030e44-9566-323a-876b-544ea682917e | -8.5404 | -54.8398 | 2026-08-22 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 38667a0e-5398-3e39-9416-53260194661f | -11.5864 | -46.5762 | 2026-08-22 02:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| de45202e-3b41-3436-a997-97b20d137cf8 | -9.1538 | -59.4446 | 2026-08-22 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 5646477f-1e99-334d-8e5a-267a466748bd | -8.5218 | -54.8411 | 2026-08-22 02:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 968d800e-9f24-3ed4-87ec-4c76eb57aaf8 | -9.191 | -59.4425 | 2026-08-22 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 6cae7d31-a440-3598-94c8-bd456eb3ede3 | -8.9042 | -60.5385 | 2026-08-22 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 25613ee7-1b41-3e4a-9b84-79621db28e6f | -8.522 | -54.8209 | 2026-08-22 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 26124117-b923-34aa-86ab-3b781885039e | -9.1724 | -59.4436 | 2026-08-22 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 21d94392-33df-327d-8ae2-99a060be8d62 | -9.1536 | -59.464 | 2026-08-22 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e5ca78ab-6cb4-3915-9237-7c066669885e | -9.191 | -59.4425 | 2026-08-22 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| ce9172f7-0b84-3ae3-975c-43d0099370a3 | -20.6358 | -47.4322 | 2026-08-22 02:40:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 8fbf9d82-82ef-3b29-a755-25bcd557b5cf | -8.5406 | -54.8197 | 2026-08-22 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.6 |
| f922b447-c574-372b-b38a-4a65fbad66a8 | -8.5404 | -54.8398 | 2026-08-22 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| a7c271dc-2dc6-36ca-b65e-bd8cee7ee0b1 | -9.1722 | -59.4629 | 2026-08-22 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 203.0 |
| 4bb0a2aa-2979-3a8a-8bcb-bf4e253fa60c | -6.8569 | -59.4564 | 2026-08-22 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| c71ebc63-f2cd-3168-b12c-110bf2c676ba | -17.9613 | -42.728 | 2026-08-22 02:40:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.9 |
| f980ff5d-a247-326c-a732-0c50dcbc1a5d | -8.5218 | -54.8411 | 2026-08-22 02:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 8f63d9b3-01e2-360e-9952-560e00a709dd | -6.8188 | -59.6696 | 2026-08-22 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| ad9558a4-ea9b-3e45-9ecf-6b643630814a | -6.97 | -59.0465 | 2026-08-22 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 1dcd597c-f28b-30f8-a68d-00e094d0e06d | -6.9699 | -59.0658 | 2026-08-22 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| b04c679f-6c89-3052-8fd2-2458929694bf | -9.1909 | -59.4619 | 2026-08-22 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 47c36502-e3da-38a0-ba27-37a65144e385 | -9.1538 | -59.4446 | 2026-08-22 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 887372b3-37de-3de5-bda0-8372682b055c | -8.5218 | -54.8411 | 2026-08-22 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 209eb487-4271-375f-beec-066ab53f3d6d | -6.97 | -59.0465 | 2026-08-22 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 94f7fbcc-b7de-3d8e-ac11-dd0f651e0ad1 | -5.9997 | -57.8054 | 2026-08-22 02:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bac6d7d7-52e6-323f-aebd-ee245689dccd | -9.1909 | -59.4619 | 2026-08-22 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 06f467c3-45e4-3281-8eff-959d8dce400d | -8.5404 | -54.8398 | 2026-08-22 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b0802573-c3ff-321c-a25d-1b9dccd9757d | -8.5406 | -54.8197 | 2026-08-22 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.1 |
| e0f45b2e-50b2-37ba-8d27-b1258d7abfc9 | -9.1722 | -59.4629 | 2026-08-22 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 190.9 |
| 29d69f3b-7fde-3d81-8c18-19876561674c | -6.8188 | -59.6696 | 2026-08-22 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 79377d1b-604f-3f7d-b966-6f35bcb7f6eb | -6.9699 | -59.0658 | 2026-08-22 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ecc6f8a2-5176-36c5-8b24-d300a5e76f5c | -9.191 | -59.4425 | 2026-08-22 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| c656e598-91e5-3abf-8d26-0176e6381829 | -9.1536 | -59.464 | 2026-08-22 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| cfda5a7c-5859-3a4e-87a2-4e77671bdbeb | -9.1724 | -59.4436 | 2026-08-22 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 5be4f00b-af73-31da-84cb-355d1051d1f4 | -8.522 | -54.8209 | 2026-08-22 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 411cb4d9-bdc3-3e95-9611-df2b5e9dcbae | -5.9997 | -57.8054 | 2026-08-22 03:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 24c1b8bb-3178-3751-9b04-0bb6bfa4f86d | -6.7693 | -58.6485 | 2026-08-22 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.4 |
| b348423e-c8ed-3b2a-8378-e929ff62acc1 | -6.7506 | -58.688 | 2026-08-22 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c90d7812-9478-35b3-a2e9-aaae6aca8070 | -6.7692 | -58.6679 | 2026-08-22 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 196.0 |
| ba2de709-3abe-3221-b7c2-2a61e6ceefd0 | -20.6358 | -47.4322 | 2026-08-22 03:00:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 11cbae49-da48-34f1-a995-08dd4f60c05c | -9.1722 | -59.4629 | 2026-08-22 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 176.6 |
| 24aa49a2-747e-3389-bdab-6d6b8b972fa4 | -9.1909 | -59.4619 | 2026-08-22 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6d6785ab-5fb7-3cb2-b212-8431ccf6805f | -6.7509 | -58.6493 | 2026-08-22 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 8ca4e791-7037-3d1f-9766-03fe6e03b3f4 | -8.5404 | -54.8398 | 2026-08-22 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 0a6f1814-37a0-32c2-be56-7c3230069353 | -9.1536 | -59.464 | 2026-08-22 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 9fbc3275-774f-33fc-9984-3906d7ae2a9d | -8.522 | -54.8209 | 2026-08-22 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| d75aab90-ce4b-3fc9-98b1-3f3d32bd4319 | -6.7507 | -58.6687 | 2026-08-22 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 198.6 |
| ba0ddb79-6302-3365-9bd8-7b7d2875f692 | -9.191 | -59.4425 | 2026-08-22 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 4114751b-5201-3f15-9675-3510de55e0cd | -20.6351 | -47.4558 | 2026-08-22 03:00:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 1f6b2a86-4956-32d6-a3a8-88bb4d4542ac | -6.7691 | -58.6873 | 2026-08-22 03:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 6e3c1ada-7d32-3d93-a78a-18d107cd95e2 | -6.97 | -59.0465 | 2026-08-22 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| de443b48-a6ac-3e34-ab1f-7bf16f6ff419 | -8.5218 | -54.8411 | 2026-08-22 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| add4646b-e773-3ffa-b4d3-6b510eada07c | -9.1724 | -59.4436 | 2026-08-22 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| f1eed129-0803-36ab-b695-e376b2bb3189 | -8.5406 | -54.8197 | 2026-08-22 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| adf33b27-64fb-3c88-a122-e8a5064c3ca9 | -6.8188 | -59.6696 | 2026-08-22 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 55cd4e90-997f-3408-894c-6a6364238ea3 | -6.97 | -59.0465 | 2026-08-22 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 4774343f-0bf2-309a-96a8-d9e66ae9cd22 | -9.1722 | -59.4629 | 2026-08-22 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 019144a6-3fa1-3947-b88e-fbd7e7ef1f84 | -8.5406 | -54.8197 | 2026-08-22 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| ae2d233b-afba-36b4-b6bf-63266ebff5d4 | -9.1909 | -59.4619 | 2026-08-22 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 8e9e411f-dea1-3ff9-8b7c-48f6c5fcd90a | -6.7691 | -58.6873 | 2026-08-22 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 3a06f3d7-9400-3ba2-9d0a-f09df790a6cb | -20.6351 | -47.4558 | 2026-08-22 03:10:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 01735135-0cd6-390a-81bf-2c708f57dbb3 | -9.1536 | -59.464 | 2026-08-22 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| cb021bf8-c079-3e92-a2d3-85c489fe1bb6 | -6.7507 | -58.6687 | 2026-08-22 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 176.8 |
| cf63770f-c1e1-3fca-8bee-c3bcf2a45cfb | -6.8188 | -59.6696 | 2026-08-22 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| a2666de6-956d-3279-9e8c-0081eddbdb92 | -6.7509 | -58.6493 | 2026-08-22 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ce240ffa-25ca-33bf-bcab-a306f5821597 | -8.5404 | -54.8398 | 2026-08-22 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8460f3fd-9fa4-3908-a00d-7257f27d227e | -6.7693 | -58.6485 | 2026-08-22 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 80f1e400-2c2a-3726-b4cf-c0fdd994e91e | -9.1724 | -59.4436 | 2026-08-22 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| b59b32be-b1e6-3917-8509-7dc5dc90b4a3 | -10.7512 | -50.254 | 2026-08-22 03:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 5ec4f38b-2c18-3ee4-9af8-af4cfd63f3f8 | -6.7692 | -58.6679 | 2026-08-22 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 183.0 |
| d9b3e766-b51e-31c8-8072-e84f5f8c5c7e | -6.9699 | -59.0658 | 2026-08-22 03:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 003a9ff8-5996-3e38-9f59-c4cf06d0a4a4 | -8.522 | -54.8209 | 2026-08-22 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| ebf43852-937e-34b8-b9b6-86a476f08f59 | -14.3937 | -51.8012 | 2026-08-22 03:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |


[Clique aqui para ver as próximas entradas](README11.md)
