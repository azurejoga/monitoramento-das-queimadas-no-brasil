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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d6d6e51-5dae-31f9-9517-d5a890640011 | -7.1048 | -41.7971 | 2026-09-14 14:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 150.8 |
| 54318818-d7ac-38d6-b181-4b10f1e922c7 | -15.5763 | -48.8144 | 2026-09-14 14:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 613cca48-bc2f-3384-95b1-b5ba6cc7a6f0 | -9.4423 | -47.8568 | 2026-09-14 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| e6986ebe-6b4d-33f5-b4c2-f1cef55fc087 | -10.7145 | -47.5374 | 2026-09-14 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| add4d1c0-7462-3950-98a4-4b463233498f | -11.2391 | -43.4413 | 2026-09-14 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| acba34a9-f10f-34b5-97ea-aa3965b85a30 | -10.5667 | -51.3349 | 2026-09-14 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| b90eb468-5cb7-3711-b9bc-3bdfda761e12 | -7.0859 | -41.799 | 2026-09-14 14:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| fd6fafc3-37cc-3aa9-a0ee-4a96070c9815 | -8.5812 | -44.4629 | 2026-09-14 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 6b435866-d627-3ae0-9f36-365faecff004 | -3.8095 | -58.9186 | 2026-09-14 14:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 496c673e-5aa3-3469-a4ce-b115dd37d426 | -9.5126 | -45.4796 | 2026-09-14 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bceee444-bf2a-3901-82f4-221aca34a36b | -3.8042 | -44.1072 | 2026-09-14 14:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 16849075-90c6-3db1-a7c0-a86bcecaac27 | -3.7181 | -58.863 | 2026-09-14 14:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 3dc4cd2c-44dd-3d0c-a2ac-de13a9cdbfab | -4.115 | -60.6886 | 2026-09-14 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e804b706-dc31-311a-ab4b-dc7a77b4340e | -3.3493 | -59.8288 | 2026-09-14 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 118.0 |
| 602a1ed1-f26e-3c3a-bde1-595696fbb6ef | -3.3494 | -59.8097 | 2026-09-14 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 7dba348b-d602-38a2-b9a8-09cc6ec3b93e | -6.5593 | -45.3173 | 2026-09-14 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 30e7850e-0577-3bac-b58e-376175cd97bb | -8.5809 | -44.486 | 2026-09-14 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 166.6 |
| d832dd86-156e-3273-9f0b-2aa37c111fdc | -3.1697 | -58.6437 | 2026-09-14 14:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 9af9e3bb-a457-38a0-b346-0cf2e0a630aa | -15.5572 | -48.7953 | 2026-09-14 14:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 97.1 |
| d0da63d9-be46-3818-922e-77175b5e58f5 | -3.8096 | -58.8994 | 2026-09-14 14:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 09551977-c757-341d-a3d5-be982642ca8b | -9.9956 | -50.2675 | 2026-09-14 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 6b45586d-ce32-32bd-85ca-a9441db59731 | -9.442 | -47.8788 | 2026-09-14 14:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| fe3ed47f-24cf-3a5c-9189-2080adf66d6c | -9.9768 | -50.2694 | 2026-09-14 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 6265ea25-39f3-3e7b-9e93-b7af7b4e8540 | -10.6832 | -54.127 | 2026-09-14 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| 9040fa4b-fe43-3d4a-bbfc-df4a76717eca | -3.6076 | -59.0769 | 2026-09-14 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| df5658fd-4e78-3773-896f-c1c66c8f7b6c | -6.5836 | -58.8691 | 2026-09-14 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 20ffadf8-5df7-311a-a038-0f89126352d1 | -7.1012 | -42.1088 | 2026-09-14 14:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 150.3 |
| 8852074d-d332-3dff-a9ae-e98c8d094a69 | -12.5329 | -47.1639 | 2026-09-14 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 7ac261b4-03e1-3a26-83ce-6aad0d10c4a7 | -4.1333 | -60.6882 | 2026-09-14 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 112.0 |
| 443bfc91-8d5c-3212-9742-f661dfdc78ad | -3.4089 | -58.1949 | 2026-09-14 14:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d982d998-2228-3d0b-994a-10a49fffbe9c | -6.1111 | -57.6645 | 2026-09-14 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| d73d8bf4-4397-3df0-8fa5-8c4e2cf91dd3 | -13.4453 | -43.8366 | 2026-09-14 14:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 68b85616-20cc-3981-b835-90450d3706ad | -8.7634 | -46.4194 | 2026-09-14 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 46573203-a2f5-35ef-8a42-589952bbaa09 | -10.433 | -48.6474 | 2026-09-14 14:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b8a165fc-c27f-3f79-af05-932396dcf593 | -3.7855 | -44.1081 | 2026-09-14 14:00:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| ff19d793-e611-3c58-86ed-8c78612f5a62 | -8.8081 | -45.8753 | 2026-09-14 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 175.0 |
| fa9dfde4-1e9a-3f45-b338-e3f176a02beb | -11.4771 | -47.4199 | 2026-09-14 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 878a9e9b-513b-3702-90db-80da534f600f | -3.3676 | -59.8285 | 2026-09-14 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| f7a28a0a-12e8-3aae-a128-5a698288f823 | -8.6001 | -44.4609 | 2026-09-14 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 122.4 |
| 8b033b5f-60bb-3403-b7ea-80df6907f703 | -3.6077 | -59.0577 | 2026-09-14 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| ca815662-8285-3723-9c7f-22675ec1dedd | -12.4341 | -47.3349 | 2026-09-14 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8eb4a6c6-058f-37e6-bcc0-efc3e6e544d7 | -3.7855 | -44.1081 | 2026-09-14 14:10:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| e9b1f3a2-8ebe-36f8-aab3-92e7cc98e59e | -12.1265 | -44.199 | 2026-09-14 14:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 110.1 |
| f046281d-9ad5-35d6-8df2-497048eb722e | -13.3059 | -51.3022 | 2026-09-14 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 9b3884ec-7adb-340f-95ab-05413096fe69 | -10.7145 | -47.5374 | 2026-09-14 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 710385ce-7284-32de-886c-3ab5cbc265a6 | -10.7726 | -46.2322 | 2026-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 187.6 |
| a3ed24a6-a028-3a6c-aca2-61437c6325d0 | -10.2922 | -45.339 | 2026-09-14 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 56.1 |
| ad0be73b-b691-34ae-bfe0-92da1d8b9afc | -1.7133 | -54.9521 | 2026-09-14 14:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8591d227-17ab-36b8-bd4c-fad717bfb392 | -10.312 | -45.2907 | 2026-09-14 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 250.1 |
| ae622424-2023-3ec8-a596-d2fe9a03fef8 | -14.1856 | -47.407 | 2026-09-14 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f56c6f66-2144-321b-95d2-e12d940ac586 | -14.205 | -47.4039 | 2026-09-14 14:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fe3d8dcf-cdc9-3e15-a63f-a094a85638e8 | -3.3871 | -59.4075 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 74ea0178-1a60-3b2e-a380-cf7cc4628705 | -2.9025 | -50.4004 | 2026-09-14 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.5 |
| 620b0709-223d-340a-90db-3c472abc02dc | -2.8839 | -50.4428 | 2026-09-14 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| cbb4e78e-2e19-3fce-b18d-a48961ec00e4 | -7.7636 | -46.6722 | 2026-09-14 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 077d9961-8c67-3a4f-8c2f-0d76abf9105a | -2.921 | -50.3999 | 2026-09-14 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 186c006c-cd14-3840-a460-5cf206ae1ceb | -4.1334 | -60.6692 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 65574f51-e47c-38a5-ac3c-84813edd9487 | -6.0925 | -57.6847 | 2026-09-14 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0f637c6e-3587-37cb-b5dd-706a74b05113 | -3.1697 | -58.6437 | 2026-09-14 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 41db001c-e0a0-3cd8-9498-157c80aab1fc | -3.4089 | -58.1949 | 2026-09-14 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5dc5ebe4-fc7d-3aa8-a1c8-7661c7d51954 | -15.5763 | -48.8144 | 2026-09-14 14:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 64.6 |
| c0ff26e0-8e8a-31e6-a191-bd01924a268c | -10.8096 | -46.2952 | 2026-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| af931357-ae7d-3707-bf8b-90264bce7092 | -8.8081 | -45.8753 | 2026-09-14 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 414.2 |
| 61289d2e-d6c0-3ef7-8595-bd913c1d351e | -2.9024 | -50.4423 | 2026-09-14 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 70906239-2f5f-336e-91c4-44f6988df444 | -8.6194 | -44.4357 | 2026-09-14 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 200.0 |
| c7d76818-1864-3b42-8d09-db9255fb1e35 | -8.5809 | -44.486 | 2026-09-14 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 160.8 |
| 547ea3f2-ca3b-3d28-a278-6eeacec0ada3 | -13.2867 | -51.3046 | 2026-09-14 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 09bea963-6800-39b9-83d7-be58ced6f8df | -7.0859 | -41.799 | 2026-09-14 14:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 137.3 |
| c81e5c0c-21a2-335f-8775-29c6825ca6ac | -10.5484 | -51.2945 | 2026-09-14 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 4a8c3a14-9a3f-30ed-9212-a8a82f169d6b | -10.8093 | -46.3179 | 2026-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 756.8 |
| 09519cb5-8c08-3dec-b0a2-d0a6b430ce65 | -15.5768 | -48.792 | 2026-09-14 14:10:00 | GOES-19 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 5281bfea-4444-338d-8d27-1d244823b2b3 | -3.3494 | -59.8097 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| ebfb9b59-6deb-3514-a9db-bef4c81da762 | -10.2929 | -45.2932 | 2026-09-14 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 128694a6-e3b6-320e-9674-8f4e4f4f31dd | -10.7715 | -46.3001 | 2026-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e9bbf854-89e1-3b01-817c-72d46c6b080d | -7.1051 | -41.7731 | 2026-09-14 14:10:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 147.5 |
| 2ebb74fc-f27e-3f47-8d00-a5c4f41ab207 | -8.5812 | -44.4629 | 2026-09-14 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 853a696c-9d9d-37ec-8fef-8b50b98e76c1 | -10.5667 | -51.3349 | 2026-09-14 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 128.7 |
| e5541ca1-c943-307f-bff3-e34fd8525a00 | -1.7316 | -54.9518 | 2026-09-14 14:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| ba0187fa-f1ba-3f3c-b3c2-888b8993bb38 | -10.7906 | -46.2977 | 2026-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 151.5 |
| f62bf7b5-f5d8-34dc-b789-4cdebe85b2c3 | -10.433 | -48.6474 | 2026-09-14 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| d12ac7a0-6103-3dee-98a6-3c1ae56d686d | -3.6076 | -59.0769 | 2026-09-14 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| d0a9f1c5-8df8-3e69-85bc-bb7126eedc68 | -13.4458 | -43.8128 | 2026-09-14 14:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 150.0 |
| d5ca0dec-2e64-3c21-af2b-a6cb2b8e4227 | -3.3505 | -59.3891 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ecbb4a34-4e1c-3942-afe8-cceb09a2332e | -6.8446 | -55.5611 | 2026-09-14 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 6b02e917-cdf1-372a-b4a2-e70e692c4e45 | -8.6001 | -44.4609 | 2026-09-14 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 0048ee4f-ff42-3613-9082-867551066209 | -3.3676 | -59.8285 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| a423023c-e312-3e3d-a371-390df0db82ec | -4.1333 | -60.6882 | 2026-09-14 14:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 48a03b2d-af24-3cde-9db0-f4659f68e373 | -10.6832 | -54.127 | 2026-09-14 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 545eaec9-c559-388c-a93f-671d67e580bb | -10.6827 | -54.1679 | 2026-09-14 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.5 |
| 96fc206f-1af8-3a92-a078-2f7e136bb50a | -10.6829 | -54.1475 | 2026-09-14 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 211.7 |
| e6db8784-f07a-3298-9de3-e3740e90c287 | -10.81 | -46.2726 | 2026-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| f7dd851f-4600-357a-b460-a280f1a91532 | -9.4936 | -45.4818 | 2026-09-14 14:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 287.4 |
| b6328de4-292c-38db-8cc6-90ebbd4c2d54 | -9.8989 | -47.6095 | 2026-09-14 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| a818fc87-eb42-3d7f-a12b-29c2163aaffb | -6.1109 | -57.684 | 2026-09-14 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 0433abe9-97f9-3e07-90ed-8e763ab3d6b2 | -10.6525 | -50.5631 | 2026-09-14 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 34574ead-6845-321c-a70e-e63fb48e9ca1 | -6.1111 | -57.6645 | 2026-09-14 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3ceefc94-c2d0-3995-8f72-e870e50299cf | -9.9768 | -50.2694 | 2026-09-14 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 067a80ad-8a14-382b-8a91-2976cdbb3fcc | -10.2926 | -45.3161 | 2026-09-14 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 01212eaf-c160-385b-b240-81bee251d2d0 | -10.3123 | -45.2678 | 2026-09-14 14:10:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 27525793-6705-39db-bd4b-6e6875f9df90 | -10.7722 | -46.2549 | 2026-09-14 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 164.2 |


[Clique aqui para ver as próximas entradas](README73.md)
