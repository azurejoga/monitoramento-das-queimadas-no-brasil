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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75783e75-b1fb-3039-9733-bd2aef941dd8 | -4.4773 | -48.18453 | 2026-09-08 06:59:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ec48fc22-5a22-3550-9779-3c7ba83fb609 | -4.36335 | -47.77673 | 2026-09-08 06:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 04b27cff-4187-38f1-acbe-ec5b4fc4ac7e | -3.24259 | -47.24831 | 2026-09-08 06:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ad42fb5a-1506-3626-a2a1-d7ed36d95431 | -3.54432 | -48.18068 | 2026-09-08 06:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 40413162-bb60-38d7-afa4-cfce1cf07831 | -4.10627 | -49.05795 | 2026-09-08 06:59:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 842756cc-bfa6-3b03-810a-8b0560383c86 | -3.24522 | -47.24413 | 2026-09-08 06:59:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 80786e2d-560a-3358-9b8e-03b85a119212 | -4.97867 | -50.63803 | 2026-09-08 06:59:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 43b01aaa-93c7-3ef0-9f33-31d07eeb0f3c | -11.48022 | -51.11215 | 2026-09-08 06:59:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 6748c932-18cb-3bff-88a7-b8980d73eb86 | -13.3009 | -45.2209 | 2026-09-08 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 112.3 |
| f2d48734-79b4-3106-85c5-5967667cc34e | -13.3004 | -45.2442 | 2026-09-08 07:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 72c96a75-3345-3d22-bdd5-6aca0759d39f | -13.30571 | -45.23985 | 2026-09-08 07:01:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 52e9218d-b635-3993-b3d9-038c05b98aee | -13.27925 | -61.768 | 2026-09-08 07:01:00 | AQUA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 4ddc544e-b595-3d4b-96b8-5d6659a23827 | -13.27131 | -61.77398 | 2026-09-08 07:01:00 | AQUA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a2483e4e-5ef7-36c6-a8ed-4a13bfbf0eb6 | -13.29223 | -45.23798 | 2026-09-08 07:01:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 57.1 |
| aafff72c-a16b-3de6-9d97-1a7341d358b2 | -13.29499 | -45.21523 | 2026-09-08 07:01:00 | AQUA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 46626557-30d3-35c4-9383-3f93586a8000 | -13.3009 | -45.2209 | 2026-09-08 07:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 545ab21e-caac-3779-968d-1369b781bd96 | -13.3009 | -45.2209 | 2026-09-08 07:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 21e0fa69-ae52-388f-84dd-56b9577fba74 | -13.3009 | -45.2209 | 2026-09-08 07:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 4c51a451-a4df-374a-8a13-14388336b4d0 | -13.3009 | -45.2209 | 2026-09-08 07:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 746c01ec-9f39-3994-aec5-f603506490d8 | -13.3009 | -45.2209 | 2026-09-08 07:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 90928cc0-126b-3e7a-a9bb-7b5d509b529a | -13.3009 | -45.2209 | 2026-09-08 08:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 61a48f72-e5f3-3061-b011-22cffa43d7fe | -13.3009 | -45.2209 | 2026-09-08 08:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 0be9e1bb-4cfa-36d0-b42d-59277cd3511f | -13.3009 | -45.2209 | 2026-09-08 08:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.0 |
| d612d6c5-a877-373f-9af1-d5a977dc3419 | -8.27119 | -42.11216 | 2026-09-08 10:49:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 21.6 |
| 54f3241d-ea0d-36eb-9b55-0ab4a833ea41 | -6.97013 | -37.99797 | 2026-09-08 10:49:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 6bc01da4-a1d4-3467-a387-36863dff7c3f | -13.04304 | -42.30295 | 2026-09-08 10:51:00 | TERRA_M-M | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 0e958a1c-4944-3d8c-9550-f0e5d97c9124 | -12.3872 | -43.44146 | 2026-09-08 10:51:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| b39f598c-ef0c-398b-bf2b-ed3c9fa466be | -12.37638 | -43.43356 | 2026-09-08 10:51:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| a29b0d9c-a550-3c23-8182-c0780c886bbe | -10.7208 | -45.8992 | 2026-09-08 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 1f553dec-1529-3df6-bdc6-882217b34ebd | -10.7017 | -45.9016 | 2026-09-08 11:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 127.7 |
| bf4e6b10-070f-3c49-8abb-814ecdb94a4d | -10.7013 | -45.9244 | 2026-09-08 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 6fa11d84-f59b-3021-b0dd-f5c6fab92bfe | -10.7208 | -45.8992 | 2026-09-08 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 274.2 |
| 587fc0d9-10cb-3dcd-b63d-0288671d8d30 | -10.7017 | -45.9016 | 2026-09-08 11:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| d570ce96-6a11-36a5-983b-055ece06e1ee | -10.7208 | -45.8992 | 2026-09-08 11:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 181.0 |
| 78d1da0a-1a2c-356d-a3a3-441eb6fa1389 | -10.7208 | -45.8992 | 2026-09-08 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 269.5 |
| 4029b6c5-6b9a-3845-bec1-99ceb836b4d5 | -9.7705 | -43.4354 | 2026-09-08 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 1ff2db85-d433-3ae3-a791-4e3a6a408a60 | -10.7013 | -45.9244 | 2026-09-08 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| d7bb1a03-a613-390b-a658-eb8b3df2ba36 | -10.7017 | -45.9016 | 2026-09-08 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 4872f04e-c0e0-34c8-af7a-161e043e8650 | -9.7511 | -43.4614 | 2026-09-08 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b45f16c8-8b33-34db-a506-d511a608055a | -9.7515 | -43.4378 | 2026-09-08 12:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 98.6 |
| cb9dcf09-2896-3fab-978c-fd1cc8e1f81b | -9.7702 | -43.4589 | 2026-09-08 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 174.5 |
| c03dfa8c-0a84-37a4-941b-865123bdb278 | -9.7705 | -43.4354 | 2026-09-08 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| b572c3fb-c1a2-38e9-85cc-7d312d2c851f | -9.7511 | -43.4614 | 2026-09-08 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| bee978ed-8367-31d4-a71d-e50bbf219fc0 | -10.7017 | -45.9016 | 2026-09-08 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.0 |
| d1f98199-2fb3-3c56-9778-c698472a9226 | -10.7208 | -45.8992 | 2026-09-08 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 184.6 |
| a2821777-d473-3fe7-80f8-3a5737ad4bc9 | -9.7508 | -43.485 | 2026-09-08 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 6f0cc756-ddf6-3992-a402-7d10fdcfa27c | -9.7515 | -43.4378 | 2026-09-08 12:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 42fea9c5-dc4d-3255-84a7-631dae20f946 | -10.7013 | -45.9244 | 2026-09-08 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 166.2 |
| 7d64d835-0246-3312-8522-156f7dfd97f7 | -9.7508 | -43.485 | 2026-09-08 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 6748cc91-6431-3bfc-8960-18548c77ce2b | -9.7702 | -43.4589 | 2026-09-08 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b3f6da7f-d07e-38f2-8c40-d9e44e03177e | -10.7208 | -45.8992 | 2026-09-08 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 2ac0680f-bf7d-3b70-994c-c2bce50f5ee7 | -9.7705 | -43.4354 | 2026-09-08 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 99.4 |
| bec7715c-9025-3bb8-aefb-85e109a604ff | -7.697 | -44.3016 | 2026-09-08 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c18a0d46-d510-30a7-82e3-01f3100fbbc8 | -2.7582 | -49.4771 | 2026-09-08 12:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| ffed0490-203b-34d6-a741-0e9b21893bd6 | -7.6968 | -44.3247 | 2026-09-08 12:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 148.6 |
| b0e8b57a-cb9f-3877-96f5-061d709d2548 | -8.691 | -44.727 | 2026-09-08 12:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 83301519-af45-3843-9c4b-b672cb4f67d3 | -9.7698 | -43.4825 | 2026-09-08 12:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| d71f0fab-3180-33fc-bf62-ae36e0cc5913 | 1.48229 | -50.86414 | 2026-09-08 12:25:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 23.5 |
| df4a24a7-9553-3d2b-84b1-b57800b3ebca | -3.82482 | -53.78178 | 2026-09-08 12:27:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 44e1aa53-bb12-3e46-a05d-c4039c1860b2 | -3.37969 | -59.42328 | 2026-09-08 12:27:00 | TERRA_M-T | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e64c824f-27a2-3ba1-a0e7-50926650e816 | -3.82644 | -53.76987 | 2026-09-08 12:27:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2f8623a5-2e81-30e2-bef3-567e33f0972c | 2.03945 | -55.84009 | 2026-09-08 12:27:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| da6bd1de-9e09-32eb-8e23-84b140b9c313 | -2.75605 | -49.49603 | 2026-09-08 12:27:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 41a032bd-c914-3db3-b0e8-f6186e1f2ed5 | -3.96203 | -58.95864 | 2026-09-08 12:27:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d9109d2f-933f-31b5-90c4-c531ddd27524 | -2.75953 | -49.47125 | 2026-09-08 12:27:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 126.2 |
| f626cf85-7e7c-3acf-b92d-87edbb049576 | -3.90177 | -52.27601 | 2026-09-08 12:27:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 74c1c781-11c5-33ca-a5b4-554c68a7d330 | -4.98563 | -50.63884 | 2026-09-08 12:27:00 | TERRA_M-T | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 870f4e79-b255-3e4d-a209-010ddc198c55 | -3.05857 | -59.26812 | 2026-09-08 12:27:00 | TERRA_M-T | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 93fdb7b0-a88b-3646-a18a-6ed1b8158f55 | -1.47836 | -54.8441 | 2026-09-08 12:27:00 | TERRA_M-T | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f7f1e4e5-87d8-3397-b3d0-b8081bdd04fd | -5.28911 | -60.11309 | 2026-09-08 12:27:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 2bf093d6-e388-394e-8443-1890c5531473 | -3.8188 | -53.76259 | 2026-09-08 12:27:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 78f60ecb-c5e2-3fa4-8f38-eab19fc2b010 | -3.95858 | -59.35696 | 2026-09-08 12:27:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 56cb6c45-05c2-34b4-b1e6-16d8eba89354 | -5.13974 | -56.27094 | 2026-09-08 12:27:00 | TERRA_M-T | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4c112b98-229a-36ed-9e63-8d7020a303e2 | -3.54551 | -48.1773 | 2026-09-08 12:27:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 1bdfdbea-c8e5-3bc9-b91f-2e78a41fd6c4 | -3.55456 | -48.18345 | 2026-09-08 12:27:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 0781f513-d97b-33ce-a210-d44e6c64bce0 | -3.19287 | -52.00488 | 2026-09-08 12:27:00 | TERRA_M-T | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b2d9f505-2bd7-3e04-aeed-cf06eaf70505 | -3.70621 | -58.94279 | 2026-09-08 12:27:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 583ad3ee-4da7-3f3f-8333-cb1c1087f596 | -1.70791 | -55.17811 | 2026-09-08 12:27:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7ca1a12e-a2eb-3c61-bb38-965fa29e59f1 | -3.64426 | -59.54719 | 2026-09-08 12:27:00 | TERRA_M-T | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ce7984c3-90b0-35f4-a2ea-e06e5d170102 | -2.82295 | -56.86419 | 2026-09-08 12:27:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 7ce27a31-7be9-3086-965b-712241b35069 | -2.8258 | -49.22794 | 2026-09-08 12:27:00 | TERRA_M-T | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 937a9a90-f9f6-387d-ab47-00ea765aae79 | -2.76307 | -49.47839 | 2026-09-08 12:27:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| a0fa5af2-083d-3801-b307-561c7c98a688 | -3.89482 | -55.81815 | 2026-09-08 12:27:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aebb4afe-450e-30b7-adc9-bad9b5ae3494 | -1.31923 | -53.13991 | 2026-09-08 12:27:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0e3176f8-ce6b-3cae-8467-b4736ff76e47 | -4.67575 | -55.63237 | 2026-09-08 12:27:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b52bda3b-cb0c-3871-a601-a909094265cf | -3.29921 | -54.82382 | 2026-09-08 12:27:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0e7e98a3-b11d-39e9-8751-71e7090cc86e | -4.03321 | -52.07438 | 2026-09-08 12:27:00 | TERRA_M-T | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 36d04798-9be2-3c81-95f6-7518fd3f79a7 | -1.70924 | -55.16861 | 2026-09-08 12:27:00 | TERRA_M-T | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f328c500-417e-3d23-9bcf-7bd3ce2da62a | -2.8217 | -56.87296 | 2026-09-08 12:27:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| d8ea5e72-f46c-3266-9d4d-c91deff47d49 | -2.81287 | -56.87175 | 2026-09-08 12:27:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 6cb63600-42c0-3d43-a17e-17598ea0a62a | -3.79452 | -55.87444 | 2026-09-08 12:27:00 | TERRA_M-T | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5f1ebd63-f7ee-3589-a69e-22978be7c277 | -5.2876 | -60.12347 | 2026-09-08 12:27:00 | TERRA_M-T | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 79061653-e6cf-3e18-864e-de34a53214bd | -3.9529 | -58.95736 | 2026-09-08 12:27:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| a435c88e-8169-391f-a60d-23fc50e53dd6 | -2.74888 | -49.47652 | 2026-09-08 12:27:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 6b5fb710-72fc-33a3-a634-890b32159d0b | -3.53866 | -48.18132 | 2026-09-08 12:27:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 269fefc6-302d-3cb5-aa5b-192c0b86121e | -4.66652 | -55.6312 | 2026-09-08 12:27:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| efda627c-c11f-32f4-b719-d16cb03e704d | -3.15234 | -60.6529 | 2026-09-08 12:27:00 | TERRA_M-T | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 21.1 |
| e8f3c9ae-3004-3eb9-947a-21808041049b | -2.81413 | -56.86298 | 2026-09-08 12:27:00 | TERRA_M-T | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 9b1daae7-a5ce-309b-9f19-fadd3add8237 | -3.77434 | -58.8526 | 2026-09-08 12:27:00 | TERRA_M-T | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e9f43f12-0e61-3a8c-8166-608e5e942754 | -7.0648 | -56.47457 | 2026-09-08 12:29:00 | TERRA_M-T | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |


[Clique aqui para ver as próximas entradas](README27.md)
