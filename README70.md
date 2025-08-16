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
| 771febe1-be7d-3f92-ba0c-945b68a23d7d | -14.94377 | -54.69838 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| bb12be48-5a16-3745-8fea-00eac1157cc2 | -14.9514 | -54.73313 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 299c9708-4944-30fa-9672-1693196a0740 | -14.9666 | -54.72546 | 2025-08-16 05:53:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5a192376-0c65-3c3d-ac90-e00150227db0 | -14.94102 | -54.69227 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f0e6cc32-629c-3299-943c-01b6a317d208 | -14.93877 | -54.75203 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 56b741d7-c2e6-39ab-b193-b6c549732c06 | -13.11991 | -57.17145 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9c350b6-b8f4-3f75-aa32-87622ead2907 | -9.92231 | -63.18666 | 2025-08-16 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85558f6a-7a3e-356f-a664-0739f988f3f1 | -13.12756 | -57.16452 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2d2f8e41-8c67-30be-b6c7-b117df060956 | -13.00543 | -56.87209 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f6efaa3-fcb3-3f24-a75e-a72a289a3050 | -14.97373 | -54.72639 | 2025-08-16 05:53:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 223c4d43-81c2-3bf5-96ab-13ff6231c8d8 | -14.93675 | -54.69601 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 380a3794-0d26-3876-ae17-3880cfa99d81 | -13.12648 | -57.16773 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7875eb98-3b8e-3795-87db-1841996827bb | -14.97014 | -54.72522 | 2025-08-16 05:53:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| db43809a-f331-389f-a685-deef67a566b4 | -8.37556 | -70.14315 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 02904808-e129-3856-8c1d-2f2c0feb0349 | -8.86073 | -69.15333 | 2025-08-16 05:53:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e79633c4-07b6-35c9-8f1c-3e8fc8ae4698 | -14.86375 | -60.08652 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f3431d-fd17-3d49-94ef-5035ddab2ba9 | -14.96073 | -54.74836 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ed72e1db-8d54-328e-b33f-1db663d3cc54 | -8.40617 | -70.43771 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 842c7078-cee0-34c4-b6ba-2b407bd526e6 | -13.11447 | -57.17196 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aebec7e9-2954-3c92-a38c-ca762626f2f6 | -13.11386 | -57.1707 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc0a8078-bc91-3c44-a1fe-b26df0180896 | -9.04833 | -67.42199 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99f8c7ab-7d7f-3361-99f6-a465ba807dfd | -9.55822 | -68.57673 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c1599db0-1d2b-3614-80da-753f1c0a8868 | -10.67935 | -69.48507 | 2025-08-16 05:53:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e541c32b-6bf3-3be6-b995-61123e3e7833 | -12.03032 | -63.32824 | 2025-08-16 05:53:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 409dd3b6-5c5e-3701-924d-bfc22e52fa9f | -10.01019 | -59.22076 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34a5f87d-d685-3680-b7d0-9ce3ea7e38ed | -8.65863 | -70.04131 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6aeb702-521a-399a-ab46-8a5d1ad1a06a | -14.96196 | -54.73534 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| aac46042-b1d1-3a5b-85d5-d1c94413c8a7 | -10.05279 | -59.12077 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cd90195-3d57-3752-8d66-698d7ba8911f | -10.00915 | -59.2181 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd60f6a8-35e5-3d04-8d76-bfc81a4d44ce | -9.63244 | -63.0932 | 2025-08-16 05:53:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d81aa4d-3040-3738-91dc-e52e8711168e | -13.1326 | -57.17429 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a184e5b-242a-3602-8287-38f19910f835 | -14.87469 | -60.08193 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44d43077-70e0-37d2-b4fc-55e6e1d13a8a | -9.37112 | -66.57442 | 2025-08-16 05:53:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a4feda9-359d-35a5-a585-cba0135ee79b | -13.12701 | -57.16325 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a558a0f-d0f5-3c55-8342-abc2fe94a471 | -14.94322 | -54.70419 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8a15ff2e-c0d1-3954-aaf5-26db8ab165ef | -14.9625 | -54.72971 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ec2d7097-1c51-3e67-b95b-25f0117938fe | -10.00953 | -59.21514 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1b8f616-62e7-3020-9711-ee93e9f7aab3 | -13.12519 | -57.12651 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51a819a4-bb67-35f8-add9-a588ab745ba9 | -14.94361 | -54.73888 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ca668fdf-92e7-3415-abbf-baf1864ca3b3 | -14.96598 | -54.73167 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ac25d22f-538a-3782-b94a-ba7c82536860 | -13.44823 | -56.68024 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 252de0ca-3e9e-3dfa-a77d-1a15e4c5e0e9 | -14.93209 | -54.70944 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a7b1556b-9b72-33f4-ac73-c77af4e48b63 | -13.11752 | -57.13947 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e52a9d38-4797-39bf-afd2-f1e51ab2cd06 | -9.84785 | -62.22205 | 2025-08-16 05:53:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc09fc32-84c2-38cd-8e6c-a67aef23ae42 | -10.05318 | -59.11778 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00962b5f-eb83-33ff-893d-d2dcf5a3ae27 | -12.89072 | -62.09426 | 2025-08-16 05:53:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 592aebd0-7a4c-3452-93f6-1e479b274c1c | -9.28365 | -68.26167 | 2025-08-16 05:53:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d31514d1-a903-3c76-9edf-db73109106e1 | -13.44879 | -56.67525 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e14511c8-5f3e-32f3-9f3a-d093295e0df1 | -14.87431 | -60.08509 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9975545-d23c-3fba-9fd8-dfcdd757a443 | -9.02889 | -70.71365 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f949e5e-9e4d-3a1a-a01b-2edf0954f634 | -14.86923 | -60.08414 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1ffd77dd-3eee-3f5c-9b4c-4fb798822172 | -9.93565 | -67.84772 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cd83884-f716-3434-99b2-fd57fa50c045 | -8.40254 | -70.4371 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89f91786-2338-3c61-a53b-4063aedc4f87 | -9.04446 | -67.42495 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 07dcb723-3409-3be9-aaa9-693472ac8478 | -12.99874 | -56.87606 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9616c2e-bf26-3a02-9e63-90b1cef4d8ce | -13.13253 | -57.16848 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30d7f768-234e-394f-9d69-05ff71b331e0 | -14.94431 | -54.69253 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 19b06211-d4db-3682-b8ab-f51ffe3d8663 | -12.99926 | -56.87143 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f1b3dead-955a-33f6-ab5c-d760bc208568 | -13.12706 | -57.16901 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdcb2621-e1d7-31bc-81c0-44669391a64a | -14.93815 | -54.75872 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 59ee0721-8b07-323c-a6d6-f3a70875911e | -13.44198 | -56.67945 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 01df57a8-2099-3ac3-8c0e-1d65576a838f | -9.5358 | -66.14555 | 2025-08-16 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 412da34e-2a77-33ab-a98f-20f5a6c4affc | -14.94531 | -54.75917 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0a07b4b-22e2-3998-966b-ac2317a46893 | -10.67593 | -69.4845 | 2025-08-16 05:53:00 | NPP-375D | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2bddfa3-0aba-3210-8384-24506e304dd4 | -14.93275 | -54.7028 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e86acb70-a9ac-30b2-90ec-17c8e753f597 | -8.37198 | -70.14254 | 2025-08-16 05:53:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89507d26-74f3-3dc9-bfeb-7bcb193b0c3c | -14.86338 | -60.08961 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4255ac79-2361-3d55-bc87-a84c1c651e32 | -10.01384 | -59.22174 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c791abd7-3bf5-336e-b1d8-c620bb0b7f66 | -11.7298 | -64.89651 | 2025-08-16 05:53:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c7cd63b9-3bb7-3662-8df9-d8bce3f50a7d | -14.95842 | -54.73506 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d8d038b6-dcbf-32cb-a622-e0a7f32521b7 | -13.12656 | -57.17352 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40cb066e-cc42-338b-b72f-b54ffc33ddf2 | -13.44934 | -56.6703 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed34404c-bfc6-3efb-b005-9aa043c53529 | -14.86886 | -60.08724 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| aa6f4299-24c3-3ee9-b31c-aed1484229a7 | -14.87936 | -60.08632 | 2025-08-16 05:53:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4c5e662-2404-30e3-bbc5-cfe01944d433 | -9.03807 | -68.33526 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6343ec04-535f-3dc9-8f3e-e6e6dd2ee30d | -13.44989 | -56.66537 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0bd1195a-18c7-3bb1-b1be-c427d5936c9d | -10.0951 | -68.45508 | 2025-08-16 05:53:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4dd29c5-602d-3a6c-b298-c882e92f7953 | -14.93557 | -54.70875 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 418882da-ed3f-395b-8a00-d21dd9ad9304 | -13.0049 | -56.87671 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2ef85ef3-202b-3273-a6ec-669bb334a6f0 | -10.29689 | -68.41904 | 2025-08-16 05:53:00 | NPP-375D | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6da39b0-1b9d-3993-b23c-90eaa9f2c735 | -9.47258 | -65.6022 | 2025-08-16 05:53:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5a94041-5eab-39e9-abaa-e92315392cbe | -14.95901 | -54.72922 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 84a2ec35-67a6-3a14-a4cc-22a5b9e7b9f2 | -13.12595 | -57.17221 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5dee1c87-bf12-39dd-a087-d8f584709ecb | -12.89129 | -62.09005 | 2025-08-16 05:53:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccbbe8df-d2e6-3bae-8130-bf07c39dc5c4 | -9.81993 | -63.01218 | 2025-08-16 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f02f6cb-3f84-3764-acab-fcb2e53e6ba7 | -9.03671 | -67.43087 | 2025-08-16 05:53:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d87eba7-f51c-31e9-bf26-6d205f638c25 | -9.84837 | -62.2183 | 2025-08-16 05:53:00 | NPP-375D | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54f785a8-1c69-3583-9f8d-55da3cf4ee01 | -10.39721 | -64.50059 | 2025-08-16 05:53:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 476f60a2-66cb-3bec-aa52-f4e504f67264 | -10.04769 | -59.12004 | 2025-08-16 05:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb254e36-41d3-3ccb-97b2-3ac747f9d941 | -13.43518 | -56.68351 | 2025-08-16 05:53:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7f5366c-8d6e-3276-bfe2-9a20d9743ee0 | -10.47258 | -61.31779 | 2025-08-16 05:53:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a60b7ad-2385-3d86-9b6c-25ec0bd6a2b7 | -14.93337 | -54.69649 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 915b5bf8-558e-3336-b0d3-3bb242b8cd39 | -14.96806 | -54.711 | 2025-08-16 05:53:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27a74d3b-ca87-37f7-a721-9f44a4b5065d | -13.12411 | -57.13573 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a201ad24-957f-301f-b170-f8ac3cb0b627 | -14.95434 | -54.73968 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ea3a00d8-e5a8-3617-8b27-21305ab63297 | -13.00596 | -56.86739 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06b7b92b-138d-3562-a285-9b489fc367ab | -13.12465 | -57.13111 | 2025-08-16 05:53:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 177bad72-87d7-39af-a82f-ea96597101bd | -14.96949 | -54.73208 | 2025-08-16 05:53:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9ababf7c-9a8e-30bc-8073-eed84c2a3932 | -11.73341 | -64.89708 | 2025-08-16 05:53:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd88e01d-a739-3cef-aeab-732cc15396a3 | -9.81917 | -63.01371 | 2025-08-16 05:53:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README71.md)
