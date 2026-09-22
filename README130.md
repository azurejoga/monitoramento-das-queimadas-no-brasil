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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a957c12-1130-3859-bf95-5e8e8628b716 | -8.5982 | -54.6341 | 2026-09-22 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ea1b8108-8f52-34d6-a2e2-12b530fd5096 | -11.4113 | -46.7798 | 2026-09-22 13:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| f13f2525-9e13-3892-8f29-c8ac10159de5 | -12.6799 | -50.9526 | 2026-09-22 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 74191fb4-7e11-3f80-b29f-df4f6e08ecb1 | -3.405 | -59.522 | 2026-09-22 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 184.8 |
| b26b595a-2d0b-3ccb-a84e-2d5ec747e1b9 | -9.5353 | -47.9569 | 2026-09-22 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a5124889-800c-309a-aba0-d6ad3093bd18 | -12.0836 | -50.0378 | 2026-09-22 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 46be1e36-d137-38d3-bccb-bb64f3a8951a | -12.283 | -50.7011 | 2026-09-22 13:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 054f14fc-6db4-3fad-ba1d-e235a3ded7f4 | -12.3297 | -50.1586 | 2026-09-22 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 3ff210ec-f6a7-39f0-8050-b3f7bd0be2d9 | -3.4781 | -59.5396 | 2026-09-22 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 72.2 |
| c153ef5a-07bf-3196-9959-b9ca531443af | -9.8404 | -46.3911 | 2026-09-22 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| b961ce4a-b834-38aa-aeb7-4b1284ded5ca | -3.6946 | -60.5835 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 933bd12f-597a-35dc-b298-68c48e53a177 | -9.6111 | -43.9243 | 2026-09-22 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 152.7 |
| 790cbe99-3d13-37ce-a2ad-31948b6a8c74 | -10.7437 | -50.8089 | 2026-09-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 68f14002-aefd-346c-8504-b84520535a71 | -10.5908 | -53.9713 | 2026-09-22 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 8a314367-cba4-3f3a-b760-fc4b2088bc2a | -3.5654 | -43.4727 | 2026-09-22 13:40:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1fbb6e64-7fca-3c52-90bb-b174f203fe6b | -9.0475 | -44.9166 | 2026-09-22 13:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 154.8 |
| ad32ab5f-abb5-3800-bf60-63a99bb1e6be | -10.5748 | -46.7296 | 2026-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 381.9 |
| 9f992dea-0b65-346d-835a-38602ee671ff | -8.5984 | -54.6139 | 2026-09-22 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| da329fa6-c860-3d37-bb35-e82a6a1596d4 | -6.3436 | -55.8243 | 2026-09-22 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 1b9a32fd-fd7c-31bd-a42e-0053ff92ec5e | -10.9112 | -53.9635 | 2026-09-22 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a57e5d37-5aa3-36e6-8e89-cd73bd8e8c9b | -10.6878 | -50.751 | 2026-09-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 20fb1304-4b5e-3295-b8f6-c534c801d58e | -9.7883 | -46.0593 | 2026-09-22 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e2ed90b0-679c-352a-86ce-5e524be5954e | -7.0352 | -44.6396 | 2026-09-22 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 158.5 |
| ba656ad3-7a6b-326e-bae9-3c51b8b95d5b | -12.0839 | -50.0162 | 2026-09-22 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 8116346c-e52f-3d94-a3ac-0cee521b3bd6 | -8.7912 | -44.301 | 2026-09-22 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f71c4dc8-3d50-3196-957f-4e1e593c89b6 | -6.9228 | -42.8852 | 2026-09-22 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| 30b44982-afe4-3a2a-8dae-e37a4d9391c7 | -6.0925 | -57.6847 | 2026-09-22 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 054a4e31-2b16-339f-adb4-4d9855917445 | -13.2983 | -51.7713 | 2026-09-22 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 7d338daa-fc6e-3047-aff8-7a18bc515d9e | -11.1563 | -51.0839 | 2026-09-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 172.6 |
| 50fbf865-967e-3024-9663-39a827e48c11 | -11.44 | -47.3579 | 2026-09-22 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 0c679d65-30de-339d-a4b0-8c777213d052 | -11.175 | -51.1031 | 2026-09-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 5a23ebff-9336-3bc3-abeb-e4a640d4e524 | -11.1014 | -48.3293 | 2026-09-22 13:40:00 | GOES-19 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| b8e53386-a55e-3c86-85f9-314c0a0b66a6 | -3.4598 | -59.5591 | 2026-09-22 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 7ea01e84-5969-3319-84c6-f38130f4259e | -7.1273 | -48.4366 | 2026-09-22 13:40:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 81980f36-311c-382a-a260-92b4e96fa275 | -9.2762 | -46.1627 | 2026-09-22 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 4637b918-40f6-30d4-8413-9e2972f401fa | -3.6398 | -60.5846 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 96.3 |
| a7bbe4c9-c354-38de-b907-9167e2b489a3 | -9.0283 | -44.9417 | 2026-09-22 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 70.3 |
| e2ed52c4-8559-3a29-8c2f-3bab20fc0966 | -14.6688 | -45.6565 | 2026-09-22 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 2bf0cc57-4edf-32c5-97fe-a168b73e2fe3 | -11.156 | -51.1051 | 2026-09-22 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.7 |
| f437e348-8cd7-3ff0-8dee-dee5114223e0 | -9.5668 | -48.435 | 2026-09-22 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.3 |
| d6f621de-3ffe-336d-bf42-ea6edac870c0 | -12.6608 | -50.9549 | 2026-09-22 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| a2e556ab-e255-3dfc-adeb-ffb41a99f17f | -6.9416 | -42.8834 | 2026-09-22 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 290.1 |
| 35687969-b26d-349c-8b6e-a00be00f5381 | -7.0164 | -44.6413 | 2026-09-22 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 272e1363-2aa0-3612-bfba-7dd639ffcad0 | -9.9064 | -48.443 | 2026-09-22 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 06870559-e99d-3fce-b28c-5bbfe63d7b21 | -3.3867 | -59.5223 | 2026-09-22 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 99db197a-8c9c-36b4-ab45-02b6a5fb143a | -12.1027 | -50.0355 | 2026-09-22 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| d61baed4-5ccf-3e1e-91a3-fac59924756a | -12.4208 | -47.0002 | 2026-09-22 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 7352e655-793f-3775-ad50-17c39c8392dc | -6.2949 | -57.7545 | 2026-09-22 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 65cf1f8e-98f5-30a1-a664-00ab15d8efce | -8.6135 | -62.5171 | 2026-09-22 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 6d9a86a7-9373-32e2-920d-81cab07abf43 | -6.4486 | -59.9717 | 2026-09-22 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| afb38c79-df8d-32b1-a608-6dba1c28ce70 | -9.6108 | -43.9477 | 2026-09-22 13:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| bd171a42-1853-3c26-b0da-90de0606266a | -3.4599 | -59.54 | 2026-09-22 13:40:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 15323f3d-2868-311d-8dd6-c6b3209a01ed | -11.3606 | -51.3797 | 2026-09-22 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| e92e4dbc-6f13-3825-82c9-0e1d9a52d4ce | -6.2761 | -47.6287 | 2026-09-22 13:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 218daca4-3dd5-3310-a7e5-c124ac03d742 | -7.146 | -48.4352 | 2026-09-22 13:40:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 224.6 |
| 64fc1dc3-1638-3515-877d-7fbc51fb63e2 | -13.2979 | -51.7926 | 2026-09-22 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 3fae7fcd-d5b5-3afc-8258-484408354b90 | -3.6947 | -60.5645 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 120.8 |
| a531fb3f-6d07-3703-a55a-ef84b8897ea7 | -10.4539 | -51.3038 | 2026-09-22 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| ec96a66f-f71b-3a5c-a556-3dea0adbf83b | -13.9311 | -48.564 | 2026-09-22 13:40:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 068d254f-3d51-3e58-93ef-00e9b9fd5a5f | -11.3232 | -51.3414 | 2026-09-22 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 57c03390-525a-3846-94c2-5fd42fc4decc | -9.2383 | -46.1668 | 2026-09-22 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 5af2e4fe-1c02-30f5-b212-0f4e4a31d4ae | -3.7673 | -60.7339 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 112.4 |
| da1e6c48-27dd-361d-8d53-75e4fea3d0a9 | -7.1203 | -43.7323 | 2026-09-22 13:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 281.6 |
| 462c4b29-ab7e-3888-b0ba-7d56444f239f | -3.4057 | -59.273 | 2026-09-22 13:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e4dc1b16-7756-338e-bacf-1b0f92c1aeeb | -12.3484 | -50.1779 | 2026-09-22 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 185.3 |
| 2eca2d4e-d2a4-3680-8fa6-64a06c63c783 | -8.6171 | -54.6126 | 2026-09-22 13:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 295561cd-602b-3943-9f06-c0d2b63245a5 | -7.2994 | -59.5343 | 2026-09-22 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 1a2661ce-63f9-30b8-b6f6-5894b00f8699 | -12.6796 | -50.974 | 2026-09-22 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 114.5 |
| d369016f-1fd5-3025-bea1-d3269f91eec9 | -6.4302 | -59.9724 | 2026-09-22 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e302fa9a-b2ab-35a2-9ae1-01e3b384516c | -12.2726 | -50.1441 | 2026-09-22 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 1a6c304a-2c8f-390d-8c1a-96021567389b | -6.4485 | -59.9909 | 2026-09-22 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| be193166-25fd-3684-92eb-d76f7b17b1b2 | -14.6682 | -45.6798 | 2026-09-22 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 171.7 |
| fc9e5faf-b803-351f-b0a4-f98755bfd100 | -10.5752 | -46.7072 | 2026-09-22 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.9 |
| 09f92e42-41f4-3f83-8f5c-e295b4e4fba9 | -11.0054 | -53.9755 | 2026-09-22 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| cafc1aa5-2dd6-3e6f-ad6b-581b1f3b02be | -11.4209 | -47.3603 | 2026-09-22 13:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 96.0 |
| fee4bf8d-d34a-30a2-9f5f-28f1048b1cc7 | -10.6094 | -53.9902 | 2026-09-22 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| aa82b4a8-2369-384f-a7d7-5b77883da6cb | -10.5906 | -53.9918 | 2026-09-22 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 0393e788-abf3-3146-bc94-de000aae8e4c | -7.0349 | -44.6625 | 2026-09-22 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 646cf2d9-1496-3c5b-8625-af5f339e4614 | -6.3842 | -55.265 | 2026-09-22 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 7087c3e3-55c1-3a14-8dba-17b04f2f474e | -6.295 | -57.735 | 2026-09-22 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 82f7d8e5-99ef-3af9-8922-db1be3ad13cc | -9.788 | -46.0819 | 2026-09-22 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0988c0af-9dae-38d8-a021-9ed33e59cb22 | -6.384 | -55.285 | 2026-09-22 13:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 05adf821-57f9-3dba-ad0c-7291564b9cbe | -6.9225 | -42.9088 | 2026-09-22 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 517c1894-8dda-3b62-ac2c-e050a6477064 | -13.8952 | -45.4913 | 2026-09-22 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 2f5f3dae-7dc2-3064-a55b-0b61cfed0b45 | -7.5704 | -57.6766 | 2026-09-22 13:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 4b3bae0b-bb03-34d4-9f59-ee845800aec2 | -10.4536 | -51.325 | 2026-09-22 13:40:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 05bd6da1-be08-33ee-ae53-328736c4cb48 | -7.2673 | -44.043 | 2026-09-22 13:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 177.3 |
| e73cc7da-04c1-3e57-87d5-460a5744b250 | -12.9276 | -51.0076 | 2026-09-22 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| a0bb7d35-4bf6-3ec7-877f-07e430df6cf9 | -6.9414 | -42.907 | 2026-09-22 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 316.0 |
| a591cc6a-932d-3ada-95f9-50a661598111 | -9.0276 | -44.9875 | 2026-09-22 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 161.1 |
| 7a2fe6d4-6e7f-3265-acf0-2edc7e4e201f | -8.7916 | -44.2778 | 2026-09-22 13:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 149.5 |
| 27897079-4132-3d4c-bc03-a8b9af1be627 | -12.9273 | -51.0291 | 2026-09-22 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 48e5399c-5576-3181-912f-d06dd9da777b | -3.7856 | -60.7335 | 2026-09-22 13:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 258.3 |
| 7e51a115-7309-3303-8911-40e785684ce9 | -9.5542 | -47.9549 | 2026-09-22 13:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| af457282-edbd-3003-af28-ccb4f023ee7c | -9.8872 | -48.4669 | 2026-09-22 13:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c8a2d417-208f-388c-8e35-235539084e54 | -7.1273 | -48.4366 | 2026-09-22 13:50:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 57aa03e5-2489-3c48-9469-501d141e0b6c | -9.6108 | -43.9477 | 2026-09-22 13:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| d4afd926-029c-304a-958e-b93fd0a1c2cb | -9.152 | -50.0066 | 2026-09-22 13:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 67289c30-7ee5-35aa-accf-5a987022922a | -7.2996 | -59.5151 | 2026-09-22 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 02787543-b134-3d38-b1d4-817023c88b49 | -9.9058 | -48.4867 | 2026-09-22 13:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |


[Clique aqui para ver as próximas entradas](README131.md)
