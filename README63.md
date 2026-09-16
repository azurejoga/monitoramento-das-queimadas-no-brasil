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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffdd0eab-08f4-393f-b57c-3ca8128a85b6 | -6.36904 | -55.83108 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9ad4203-720f-342f-a65f-b81fa64c04f1 | -6.8064 | -59.17598 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f684f2d8-4378-3ee8-b472-e64a737f2975 | -3.11759 | -61.41824 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff7ab55e-ee38-3f93-bed0-2c89b3343796 | -5.24554 | -59.98338 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60635bb7-f1ed-34a2-855e-c021f789b0e3 | -4.43487 | -55.78994 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a8c5d64f-a645-3ae9-9f0e-93ff734c5526 | -5.75788 | -57.59291 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71c5f1f5-d232-3642-97d6-31d1b717f86a | -3.73798 | -55.94431 | 2026-09-16 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8ae3aee-9137-33b6-9a80-1d5824a10442 | -3.44378 | -58.00658 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98048fbd-2f5e-3d0e-aeca-6cdaab645731 | -3.76523 | -59.39215 | 2026-09-16 05:53:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 269b2e15-d5ba-3738-9d3b-03538db0212a | -3.58447 | -58.53228 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db7d2696-82c4-380f-9d29-42300072a334 | -6.75564 | -58.81393 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e88e8ca-3019-3d4c-8819-46a8ed354779 | -3.3731 | -61.33192 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a971c73-ddfe-3660-99b4-4ee94cabc947 | -3.81134 | -58.90076 | 2026-09-16 05:53:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 19eede41-17e0-336c-a472-8be73dd7bc15 | 2.61135 | -61.43187 | 2026-09-16 05:53:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dae2704a-c639-3935-9834-79e7111e7b90 | -5.64615 | -60.2204 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5df29293-13bb-3020-9d01-06c504af4c33 | -6.34518 | -62.70127 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 78106f65-6040-34b4-8e1f-b1a3aa14c659 | -6.33888 | -62.69043 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 365457aa-fc90-3998-a5c0-4f874a990dd5 | -3.73126 | -55.94228 | 2026-09-16 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41489c9d-eb1e-3c34-8621-5c29faacde1b | -6.34905 | -62.70185 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c75d350f-0ec3-3b69-9a56-5fedb70c2640 | -3.17796 | -61.10748 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5300a24a-6874-3e2a-83b6-811985831217 | -3.37225 | -61.30997 | 2026-09-16 05:53:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 360b3edc-382d-39de-8f34-ff804d1fc8c4 | -3.42159 | -58.22775 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54f231aa-6cca-3d50-a3e9-56cae9119425 | -3.12659 | -61.25422 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6cc36065-6095-32d0-991f-4bdfb4262285 | -3.5862 | -58.53463 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24217fd5-1ae9-3556-bc94-67084ba428dc | 0.09556 | -60.63787 | 2026-09-16 05:53:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7acd0b89-9ec3-3cd1-a8a5-36f784e8f919 | -3.17742 | -61.11113 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afb13ba1-38f8-34d2-9bdd-0d4b8d0f4575 | -3.75386 | -61.75887 | 2026-09-16 05:53:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdd0d89f-4707-3036-86ad-72f3590f1167 | -3.10795 | -61.10403 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f398a38-3716-32a7-9226-9141fc3ae183 | -5.46215 | -60.22493 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aadf534d-f9b3-3a45-9f6e-b6a2df6b39b4 | -6.32728 | -60.01451 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d1782dd-4517-3f6e-aebd-62f403433cc9 | -6.438 | -55.60639 | 2026-09-16 05:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03b1b7c3-3c94-3bd9-a7b6-fefb7b391ea8 | -4.40591 | -55.0845 | 2026-09-16 05:53:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08ba37ce-99fe-31e8-8e79-2cf04683d548 | -6.09213 | -57.69513 | 2026-09-16 05:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 800c0ac8-2aad-3fc1-afd8-66576d434204 | -5.45833 | -60.21974 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffd46ad6-14d3-3b42-a66c-a3ed047d065a | -3.73647 | -55.94771 | 2026-09-16 05:53:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bfd1878-19cd-30e0-a268-3124fb7757d9 | -3.58277 | -58.54326 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5abfe754-5778-33ec-9a84-28b59ca40030 | -3.18273 | -61.10809 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9de4efbc-63b2-336c-86c4-b70c12809cc9 | -3.58362 | -58.53777 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 563744e9-b52c-389c-a969-464f2c06ffcc | -3.70478 | -60.61502 | 2026-09-16 05:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae5c2ab6-7a13-37ed-9480-71fcc008161e | -6.44928 | -60.01424 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e21c71f-1383-378f-a04d-e3b426b3147f | -3.17397 | -61.11053 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4817d9c5-b7c0-3f66-ae4a-0c23a1f28b40 | -6.36967 | -55.82652 | 2026-09-16 05:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca781d6c-313e-3da8-a3c8-364ab86cc9c7 | -6.12584 | -59.88717 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4421ff95-34fa-3531-8f9d-37758e29589a | -6.33114 | -62.68928 | 2026-09-16 05:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f236d0f-abaf-37a9-8bc0-8601f930d022 | -3.4429 | -58.01255 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 63908010-c93e-3e3e-bcc3-b41c95ce9555 | -6.77165 | -58.8102 | 2026-09-16 05:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1078a6a1-5fe3-31f7-a3f6-46cc9e3a82b9 | -3.59111 | -58.53537 | 2026-09-16 05:53:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f88d82e8-96f7-3ccd-a06f-870ca76b3ac3 | -5.64164 | -60.21973 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4f99b122-03f3-3ef7-b7a5-3eec9e3f5ba8 | -3.12199 | -61.25717 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f137cd6-5e74-3a09-b00a-24f2649de52a | -3.18216 | -61.11174 | 2026-09-16 05:53:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 933114e9-cfd1-3691-a0bf-a37063edeee8 | -3.29449 | -59.46393 | 2026-09-16 05:53:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7586dd9-cc67-3597-9f0f-760ab7bb2a72 | -6.2983 | -59.98592 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c60cfb09-e361-3f92-9aa5-6dc05aa34f9d | -6.64806 | -59.96386 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d3ce910-9aa5-3403-b902-60137efe3f01 | -6.12118 | -59.8865 | 2026-09-16 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d2c61c2-66f7-3494-b472-a0e46601f3a3 | -3.69933 | -60.62238 | 2026-09-16 05:53:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1809453f-7405-3d05-be74-f1502be8ce4a | -6.75098 | -58.81027 | 2026-09-16 05:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1095427-a911-3407-87a6-928dec39be64 | -8.66036 | -66.50269 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c7e3b8e-c5cc-3589-86ab-e60bb1df9d5f | -7.64635 | -67.16891 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9a9bfbfe-bd2e-3ef0-a6ed-9235d4891c3e | -9.06382 | -65.92649 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7d4a042-d318-38cd-9e58-1f1bcff2c0a6 | -9.38853 | -60.31082 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4b1625d1-66a3-395f-85ed-d20dd8a60f9d | -3.11034 | -57.67878 | 2026-09-16 05:55:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9fc47d4-8ef9-3d4e-a510-db88dcafc02a | -12.11636 | -57.19756 | 2026-09-16 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9979d9be-44ba-342a-a057-4eaec46c51cc | -9.62611 | -61.82239 | 2026-09-16 05:55:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 33be1452-b568-351e-9c7d-549bd3d1637c | -1.85182 | -55.80896 | 2026-09-16 05:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eadeb4dd-b0bf-35fe-a0a0-da6880781caa | -9.13943 | -65.84315 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ef7d415d-be1f-3d99-b17f-a16c5a762a32 | -7.64966 | -67.16944 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e001f4e-c7de-38c6-aa50-e303770ae008 | -1.85293 | -55.80882 | 2026-09-16 05:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29a5542c-16c7-3799-b3cb-e0e2b808eaa2 | -7.63972 | -67.16787 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abef16fe-f45a-3bdf-a0c6-ce9cb2c35d2a | -9.22031 | -60.29523 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8231cc74-cb8d-3bbd-97f0-edfc80980c0e | -8.87861 | -62.51917 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab127656-a950-3cbd-9f73-1d7a5d1b619f | -9.89588 | -67.00534 | 2026-09-16 05:55:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d448aea-ebdd-3dd4-85b8-1f6b55b8ad23 | -9.38126 | -65.44811 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5947fe3-6cf4-3f07-8650-f775bdf76442 | -9.10603 | -65.56121 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ece8b7d-2e9a-35a9-a644-5f474ed8e2b1 | -7.64194 | -67.17532 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cecc6f58-7fc8-314b-b5d6-bee7ae0eea4c | -7.55279 | -62.32739 | 2026-09-16 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 394722af-02f9-32c7-9dc7-81a58e60b37a | -2.68181 | -57.60225 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 674d1a02-43cd-3877-a84b-118bad4ca030 | -7.61333 | -67.24901 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf616741-f9e6-39ce-a9a9-0e39cc972af9 | -8.63454 | -66.52094 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad8d7dfb-fae3-32dd-834f-a644529f167f | -7.64689 | -67.16544 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 084d0c7e-205f-373d-aea8-8f855d1f1514 | -9.39399 | -60.30629 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e5205527-602e-3d4f-875c-ace31a103ea2 | -12.05702 | -63.37518 | 2026-09-16 05:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27bc6c11-8f46-3ec9-b983-2169bd03bda2 | -2.68228 | -57.59916 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3c9d673d-b2b5-36c5-909e-a612faae3aa9 | -8.63544 | -66.57526 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a204d9a5-89cc-3243-8c50-fd880c883fb1 | -2.68698 | -57.60303 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50d13f78-669c-3fbe-9cf6-327c55595702 | -9.10414 | -65.93657 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f09c7ecf-4a9d-3cc5-90d9-27a2e0091921 | -9.5051 | -64.71831 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00e03f01-3532-3bda-94f1-d32a3c53fbf2 | -8.59919 | -64.10528 | 2026-09-16 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 99c6137d-2fe9-31f6-b89b-aa5795ad2497 | -9.06951 | -65.93494 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0da1004-ba98-3a17-a54a-22debfcd28bd | -7.85731 | -55.45465 | 2026-09-16 05:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a1c7538-2fbc-334c-9069-96b4424c905a | -9.06667 | -65.93071 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba3e04c2-f600-35b5-98d8-1af46e315ca0 | -7.63587 | -67.17081 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 78a96ecd-f44a-3504-8ac7-ced1cde7db26 | -6.92141 | -63.11208 | 2026-09-16 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79b56b10-e8d6-3b44-8512-0c4e9f6a77df | -8.36958 | -54.73433 | 2026-09-16 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4107fc0-c0c6-38f1-b872-6fdc1008ee3f | -9.05721 | -65.92217 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d533f893-fc9c-362a-a1e7-904058d035a1 | -7.61664 | -67.24953 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0863a68c-a0a8-37aa-a5aa-6a01fc95d738 | -9.06895 | -65.93864 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d052d192-d936-32bb-adf3-a0b958cb7448 | -8.64881 | -66.57735 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3793b826-1487-3841-a8fc-8138cd07ef2a | -9.25629 | -60.27936 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c86b5c29-5148-34d0-98c3-2e3cb1c2af08 | -9.71269 | -64.97427 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a5696c-f06b-3163-98c4-668567b5525f | -11.19178 | -55.03094 | 2026-09-16 05:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README64.md)
