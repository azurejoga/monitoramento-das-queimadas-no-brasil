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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd9cb362-959a-30c2-80a6-b51d37e8e132 | -9.93838 | -60.4856 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ec2a2a4-2848-3f84-a89f-035e5f40efa0 | -9.20161 | -59.64291 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7eb1769-ecfb-3eb8-87b6-468cf53eaefd | -8.10264 | -61.18515 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0426df84-5434-30db-8dd1-b53d958a1eb9 | -9.93903 | -60.48039 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3fe6c56-b425-37c1-8b03-0062f1c42557 | -6.92552 | -59.52903 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60e6203d-8235-3fc4-b232-aebe1ad6dbbd | -9.3456 | -62.58543 | 2025-08-15 06:10:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1bb0dd3e-1eb9-3a97-8e85-b2025cf5cc14 | -9.15484 | -59.6942 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b598664-82ee-3473-a67d-42a9507daab0 | -7.82075 | -61.32469 | 2025-08-15 06:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf9c7189-883f-3d69-bcdd-67cf19c2c175 | -9.49999 | -60.516 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 117a9f3e-044c-3f39-90dd-b48be4cb47c0 | -6.9241 | -59.53998 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0a3ddd4-9e1c-3f78-833e-40019a3e7742 | -7.07741 | -59.24013 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6514858-0d44-34d1-a84a-3d7f73ec4eaf | -6.89925 | -59.14986 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1835eb2-624a-3efd-9e5b-96d7416cd14c | -7.95227 | -61.7499 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 906eef0c-dedc-35b4-92a5-76bc451cd428 | -7.8838 | -61.81146 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f2d49f26-3bbe-36e3-a1ad-3c3fbd057fe7 | -7.09141 | -59.21314 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab87e900-4f36-32e6-9459-4d6a77459ae8 | -8.1134 | -61.19543 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 55a38341-56ac-31fc-aec9-b512b5549d8f | -11.40517 | -58.54696 | 2025-08-15 06:10:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c6a5a86-f81d-32a9-bf64-5fea18a96bf8 | -9.21118 | -59.65561 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1534fa0e-08f9-333c-aa89-456e0894c23d | -7.87927 | -61.81931 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 592dc881-3f9e-322a-beaf-e3b6005544a1 | -7.08405 | -59.21791 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c866b501-f52a-31a5-9e49-62a73d706174 | -7.58802 | -63.45198 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfb5349f-2689-364c-b044-7698e35f7109 | -7.62969 | -63.52379 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c43e351-40c1-312b-b80c-009153dece6b | -7.08402 | -59.24114 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adee4d0b-c225-371e-93ff-738bebec23af | -9.39756 | -60.54556 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03062dfa-3b5d-3bfa-b324-d07a2d5477a9 | -6.70448 | -58.84777 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6135c6a-fbe8-38bc-b8a2-048f8ea19c9b | -7.30428 | -60.625 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c90abc19-79f6-3324-8614-cdcf56603b89 | -6.7084 | -58.8176 | 2025-08-15 06:10:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a0a8518a-e6fb-355b-ba24-3dfe2e4cf510 | -9.2128 | -59.66107 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25f9e20e-fbf3-370f-b997-8b6c2bc419a4 | -7.07893 | -59.22902 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ca572c2-1a29-336b-b3b0-b6d424d3e5cf | -7.09067 | -59.21883 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a51c1a87-25d0-3295-88ed-45c08c9438d9 | -7.87189 | -61.81379 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01dbeb4a-aba2-389a-9438-7c26a3692239 | -6.89157 | -59.13132 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cb7ac3c-206e-37f9-8d3d-7d8f12a98955 | -9.50063 | -60.51089 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 62e91623-b1da-32d4-af00-2e9b92aef15d | -7.61959 | -63.52238 | 2025-08-15 06:10:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b0011de-71cf-37a0-9d66-d8b4164398a8 | -8.55721 | -63.91345 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b5b8c64-64d5-337f-8fc9-6bb4480c76bb | -7.32304 | -60.62391 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40455e3b-5ac5-33c6-bff7-e28ef0607699 | -6.90925 | -59.15123 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 938049d5-043d-3758-a142-07d1a897b36e | -7.53594 | -61.33865 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 60d5b6e0-5dad-3dc5-9d2c-d7240053ede6 | -10.42907 | -67.87335 | 2025-08-15 06:10:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d35ceeb-5002-3951-82c7-b9cd7332e73f | -8.0248 | -71.40582 | 2025-08-15 06:10:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd5d111a-a806-329c-8675-a4d882b04f5f | -7.53026 | -61.37747 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5633fd83-6886-3bbd-b6dd-ea51b2c536be | -7.0813 | -59.21159 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4c8ec587-3e39-3550-be8d-f95644cdbb10 | -7.5303 | -61.37939 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31d0e663-56e3-374b-8070-520039525539 | -7.42551 | -60.03592 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5eed144c-cd05-3e8e-8f62-806cc448dde5 | -8.67508 | -62.45097 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 571f0d30-a6c8-3215-b5c3-fac17b802010 | -10.3259 | -63.62231 | 2025-08-15 06:10:00 | NPP-375D | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3aebc74d-a6ee-3746-adcb-cdc8ad2d1ce5 | -6.87222 | -59.83895 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 507b7d61-7ad7-3a3d-9c5e-1db35f6a3897 | -6.95032 | -60.14472 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2254a658-c604-36bd-9f40-abff04a73036 | -7.52448 | -61.37857 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 81d15d29-bb4b-3bc2-b4fd-9d749278802f | -8.40149 | -70.43616 | 2025-08-15 06:10:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f2e6c32-d1f1-3849-b9d4-5ba74e9b0759 | -6.91662 | -59.14663 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a6274b1-962b-3be3-b883-0479b2bfb29c | -8.67555 | -62.44733 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 10806cf6-0c2d-3566-9bcb-877b26affecc | -7.8202 | -61.32878 | 2025-08-15 06:10:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cce61bae-1265-31f0-a438-5fa4051b1e3e | -8.56295 | -63.90847 | 2025-08-15 06:10:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dca73256-71b3-39ad-b803-cc67bd0a2272 | -6.89748 | -59.13784 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a94870d-453e-3c2e-91d7-dedacc03f858 | -9.17606 | -59.68566 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba1bd167-ab08-3e81-b41a-d7abc4cc7dec | -9.50441 | -60.53183 | 2025-08-15 06:10:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3cb90f09-bf3a-346c-a594-9978a3a9b8da | -9.83438 | -60.75838 | 2025-08-15 06:10:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9455b0f-bdb7-3f25-80d9-d78b28804f79 | -7.15447 | -59.64265 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24063f9e-8f58-319c-b177-00a6d2183919 | -6.92394 | -59.5395 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6842f3d-f721-3e47-b11e-90c3a98279ab | -9.15554 | -59.6885 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea200c2f-0099-30d5-a6d3-8c7e2b7afcd0 | -9.16803 | -59.69619 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b968e1ed-4200-3590-8d70-cc8e6b4709a2 | -7.52971 | -61.38166 | 2025-08-15 06:10:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1916245-91b7-3ec6-a77c-c86514e0bc52 | -7.31637 | -60.62742 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc12c132-9dae-3116-a417-e7afa03cc58a | -6.90006 | -59.14404 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 481169f1-8506-362f-96bf-03438c2abee1 | -6.47968 | -62.9403 | 2025-08-15 06:10:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7790719f-d55a-3b76-8b10-22441a16e462 | -7.15517 | -59.63728 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0ab7a76-db7e-3f61-b7af-866873a3a373 | -9.19 | -59.68172 | 2025-08-15 06:10:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f28e2afe-077c-3a3d-8fb7-171074fcb05e | -7.30368 | -60.62937 | 2025-08-15 06:10:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02451c3f-dd5d-3034-adb2-e11828ab297a | -15.38725 | -59.82044 | 2025-08-15 06:12:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 441549a6-3b21-39f8-ab78-344bd062f318 | -9.1706 | -59.6762 | 2025-08-15 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 45fe7281-7e35-37e7-a77c-9920a51ef800 | -13.4759 | -56.6537 | 2025-08-15 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| a57b5d3e-79bf-3b68-b01b-b1919dae61a9 | -9.1708 | -59.6568 | 2025-08-15 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.9 |
| c96078ab-fdb7-3336-a7c6-3df3aa300508 | -6.0807 | -59.9465 | 2025-08-15 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 26956a49-25f7-3f8a-bb55-d76680085861 | -9.1894 | -59.6558 | 2025-08-15 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 5cfb36bc-3409-36f9-9528-5d991e5f7516 | -9.4994 | -60.5278 | 2025-08-15 06:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| ddfb95c5-4c7f-3670-8802-1074c2c88aff | -5.455 | -60.1391 | 2025-08-15 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 27952577-0916-36a3-87c1-10b243581d95 | -13.4568 | -56.6555 | 2025-08-15 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 8b042852-ced4-3d01-8be7-3d0795a93f5f | -6.9303 | -59.5305 | 2025-08-15 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| f0663b96-b1cb-3d47-9e3a-d133122787fa | -13.4566 | -56.6757 | 2025-08-15 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| ef3e0825-851d-3b78-b71f-5eb37d218d22 | -13.4757 | -56.6739 | 2025-08-15 06:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 52c0b632-df01-353c-b413-1875f0860499 | -7.5919 | -63.4978 | 2025-08-15 06:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 76cac899-d1ba-38be-896b-1164cd87b297 | -7.5292 | -61.3254 | 2025-08-15 06:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 98b6d5e9-9eda-35a3-93c0-3fd4f8fee342 | -6.9302 | -59.5497 | 2025-08-15 06:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| dae0d4dd-a9b2-3e55-8535-e20ec9cdeeb7 | -5.455 | -60.1391 | 2025-08-15 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d411bafb-1c8a-37ea-8c03-690c7854bbd2 | -13.4757 | -56.6739 | 2025-08-15 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 175.9 |
| c0dd34bf-684c-3b7f-addd-025f301b87f2 | -7.5292 | -61.3254 | 2025-08-15 06:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 53d14b9d-64b1-38fd-be41-0827b0a9591f | -9.4994 | -60.5278 | 2025-08-15 06:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 6613dfe4-0e24-3e9a-9d7e-9a8d68ef5362 | -13.4566 | -56.6757 | 2025-08-15 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 242.6 |
| 36c64da1-036b-30eb-8eea-9b3ad01a3d3d | -6.0807 | -59.9465 | 2025-08-15 06:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 9eeedbda-a164-354c-bd53-50a24e85f091 | -9.1892 | -59.6752 | 2025-08-15 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 4cf3ef2e-9728-33d5-9be8-954167c01534 | -13.4759 | -56.6537 | 2025-08-15 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 3fbf70d3-d024-313f-91d0-62ef1bbe0ab9 | -6.9303 | -59.5305 | 2025-08-15 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| fc29a8b4-ba4a-35a1-a39f-7b9f6a465959 | -9.1708 | -59.6568 | 2025-08-15 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 5055e5ee-198b-30ab-a27e-7bfc7a321944 | -9.1894 | -59.6558 | 2025-08-15 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 540427be-7a57-3f26-9b08-b57a3afcaf84 | -19.4874 | -43.6179 | 2025-08-15 06:30:00 | GOES-19 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 51143ab5-a274-3b9b-a61b-02d039d4fc6e | -6.9302 | -59.5497 | 2025-08-15 06:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| a82618be-d37b-34ea-b052-473c91f56cd5 | -9.1706 | -59.6762 | 2025-08-15 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.0 |
| f8391196-9446-3205-94fd-e481ed66f6c0 | -13.4568 | -56.6555 | 2025-08-15 06:30:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 166.6 |
| dfab06de-79fa-3dbb-aed7-7814a1aef5df | -8.40256 | -70.43945 | 2025-08-15 06:31:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README71.md)
