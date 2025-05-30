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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3393ce90-712f-30d1-b052-3a6bb406bbc3 | -8.16854 | -49.79932 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d4044c5-daec-3375-adfb-2b35013d9e85 | -11.89856 | -47.44244 | 2025-05-30 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a0a66a9-1de3-387f-b29f-564512d2bab5 | -9.79264 | -47.7507 | 2025-05-30 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c45d6f71-4b90-3e97-b2e3-ba5e951a03ed | -10.46041 | -47.94973 | 2025-05-30 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 11290437-6eb6-39fc-a780-ff1245258621 | -10.35407 | -48.73403 | 2025-05-30 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 97699e40-55fb-36d5-a8ca-2aa07f1c6c45 | -9.3982 | -48.41781 | 2025-05-30 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5810a10-a4b5-35d8-9ae3-f300f731e608 | -12.82597 | -47.39942 | 2025-05-30 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65be0f34-6ccc-3bc1-9339-9c35cb7586a5 | -9.25354 | -48.86118 | 2025-05-30 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f07a5ffd-d6bf-3e15-8ed3-243471c3b872 | -7.18877 | -43.10499 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e5a210d1-9e2f-3b15-ba49-0edbe4e79d82 | -7.19384 | -43.11054 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 90c5836c-e59a-325a-8b4b-9f5809fdcb64 | -12.0144 | -49.52222 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ab450484-0e41-3a1f-b91b-5e8ea605abcb | -7.61693 | -45.74331 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 06334c14-4262-3d04-ad94-d2ece3cbac97 | -13.6274 | -47.43294 | 2025-05-30 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4223c5a9-2e2e-3cd1-97f3-b89571458e6f | -10.41246 | -46.58194 | 2025-05-30 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13df0962-9a1b-3821-b347-6d6524a498ae | -7.69228 | -46.86605 | 2025-05-30 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7aa6774-496e-32f4-8b5f-d7d8fcbdb4c3 | -11.69299 | -46.21478 | 2025-05-30 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9484efc2-19c5-3a5a-a20f-15738424fa6c | -7.62056 | -45.7478 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d88359c-6d9e-31f9-91ba-dfc6b850c4e8 | -11.80291 | -47.38081 | 2025-05-30 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e28847d-82e3-317c-9e19-8a4399e4a978 | -6.6338 | -47.34896 | 2025-05-30 04:46:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ede1d1b-93f7-37e8-adce-0faaf4585aff | -13.09282 | -52.04692 | 2025-05-30 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 6b6390d5-8086-3aed-a843-00fb13068448 | -8.54641 | -46.42807 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0854050a-0b4e-313c-ab4d-d08a0ee2c495 | -7.84174 | -46.29718 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfd0ed6a-0e5c-36b7-b82c-ca427362945c | -12.01821 | -49.54623 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7bd2cc3-1859-3c1f-9527-c0c91c76f2a8 | -13.63653 | -47.42658 | 2025-05-30 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6acd86f-08ea-3a80-8c8f-5e235f204a47 | -11.98038 | -52.4617 | 2025-05-30 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfde7179-b902-3fef-bee1-a4f66fdf737b | -7.00704 | -44.61331 | 2025-05-30 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a169b03f-c593-3839-bec5-3f8b592b6cfd | -7.59095 | -45.95548 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d7af184-aeac-39a2-a2c6-5cb002fa15a9 | -12.30041 | -50.08969 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3eabf57e-d927-3f8f-92bc-7e0e1b127fba | -9.25883 | -48.87434 | 2025-05-30 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a15ad1b2-3deb-31e7-8e9f-296ab47ddd05 | -6.98629 | -46.31249 | 2025-05-30 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b95cee2-5c8e-3b46-81b1-f4e5dd5a62b1 | -7.66856 | -49.3764 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d2f1080-4282-3ce6-954d-b172347f8abd | -13.63247 | -47.4259 | 2025-05-30 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56703e00-2559-3938-b16a-e63ec7c62fb6 | -9.25294 | -48.86521 | 2025-05-30 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77bd91eb-03a2-3a49-934d-5171e81a74ec | -9.60927 | -49.02527 | 2025-05-30 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c06e01d6-1bf5-3f49-96c1-50fcef3f178c | -12.30388 | -50.09023 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6abfd08a-e3be-3566-b17e-6df18ebe41ed | -11.79673 | -44.28733 | 2025-05-30 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 38e59eef-1afe-3398-83ed-c0fb72095717 | -12.82193 | -47.39887 | 2025-05-30 04:46:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bf0be3e-c060-3436-a24b-00ca11c8bc52 | -8.79399 | -47.94305 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48958025-ac7c-3a29-bed6-63fc1e05ce14 | -7.2624 | -49.51286 | 2025-05-30 04:46:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eb65e889-6893-3e24-bea7-1f641bd4ab07 | -8.00442 | -45.69041 | 2025-05-30 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4787cb03-cb83-33c5-b85c-b98364be764e | -11.1308 | -54.21957 | 2025-05-30 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| feb693e5-6aa4-37a8-8407-32d0eeb33d88 | -7.58736 | -45.95113 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f40b3360-b02e-3370-a9ad-14fd6797c89a | -13.09944 | -52.04797 | 2025-05-30 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f1a921a4-5f2a-377c-8669-5a271bb3a78d | -9.3952 | -48.41296 | 2025-05-30 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7c648b3-bcef-327f-a7f8-ed8e8d982932 | -7.18918 | -43.10211 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0925bb5d-646e-353b-99a4-5dbb3a8d7b02 | -8.51807 | -50.01962 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 92bcbda6-1676-350d-9d92-7a9eea94499f | -7.95495 | -46.1733 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 793ae3e5-226a-33ba-9699-623a81a7b763 | -13.54093 | -43.67818 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e414f036-7d52-3d4f-ae6c-dfc53a9fa875 | -12.01051 | -49.52423 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| be12b9ec-09c2-3548-890b-6932284d7576 | -9.99276 | -48.16037 | 2025-05-30 04:46:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1167883a-b778-354c-807e-f6931128bb2b | -11.20916 | -47.82298 | 2025-05-30 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d25527f0-3c74-3d50-b550-156b373afe9e | -10.68712 | -57.65038 | 2025-05-30 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce0f7986-ae13-37de-96d7-40fa2572b9a6 | -11.03655 | -50.77948 | 2025-05-30 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 155d8f04-8b46-3f1b-b64a-6a17201c43c7 | -7.18379 | -43.10432 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b14885e3-20a6-33ae-957d-cedb5d04087b | -9.39758 | -48.42209 | 2025-05-30 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| adecf814-3836-3b6d-aa2a-3e082c59d810 | -11.03375 | -50.77534 | 2025-05-30 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 053679ce-3f25-3fd7-b838-4b0de46502fe | -7.61331 | -45.73875 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3c526a56-e81d-3d3d-81e7-c3f8efed9518 | -12.40029 | -50.00397 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6954a228-611e-3ad8-9bc6-c3a62948cb69 | -7.61277 | -45.74259 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 504ce4df-020c-311f-a3e2-caedff989619 | -8.84702 | -49.8409 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9b55a66-f72b-3584-b547-2ff4ada4a836 | -7.24595 | -43.10077 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| cddcaa30-858e-3fb4-b240-3b30d560f655 | -9.35967 | -57.55334 | 2025-05-30 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4129e68f-c598-3a81-911c-b600a7496c56 | -7.61639 | -45.74711 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c289f606-30b1-3ad6-8559-66a690c201f5 | -11.45327 | -49.10212 | 2025-05-30 04:46:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b36dbce3-fab8-34e2-9c52-436d209df63d | -7.96306 | -46.17488 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 00616fea-e060-3935-b7b3-3369cc6c8571 | -7.18338 | -43.10722 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c465c487-06c3-326d-9d49-b68fe64c28c4 | -13.54015 | -43.68212 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 7797937b-8eb0-3d68-88d8-7e6c0c712ae7 | -7.27639 | -44.22623 | 2025-05-30 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73763694-7344-3b18-8957-f0d9f3496d8c | -9.84816 | -48.14932 | 2025-05-30 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24ba6077-d216-3afb-adbe-815227d2c9d2 | -10.29738 | -57.14213 | 2025-05-30 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 58b75d2a-3f65-3925-81a7-221097f502fb | -8.79029 | -47.94252 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63ec948e-75aa-3a6e-9ecf-58bec50d7986 | -13.52968 | -43.68071 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 808ef118-e08f-3212-a107-be1c7dc246f8 | -10.17068 | -53.91991 | 2025-05-30 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ff836b5-69ff-3d70-b28c-193728ebfb9d | -9.36035 | -57.54943 | 2025-05-30 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bbf31ea2-9be2-35e0-a207-bc18e152fff5 | -10.68779 | -57.6465 | 2025-05-30 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98e7277c-cf2d-3152-9cc8-77d4f5f59791 | -9.26964 | -47.91473 | 2025-05-30 04:46:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dccecf22-8491-3969-b258-c3951c55754b | -12.01086 | -49.52169 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 80123ca9-fe77-352f-9a75-52b3e4f778a7 | -13.53569 | -43.67746 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cd04dea4-78bd-3ea3-8764-62ea8ed9e6da | -13.63602 | -47.43042 | 2025-05-30 04:46:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1233f90-5043-31d8-bf54-64f939a68ab9 | -11.57205 | -47.459 | 2025-05-30 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 540a1606-2035-3df9-a965-e8fbd788ab78 | -6.75507 | -44.93421 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c2dfa2e-dae8-3e37-a3c3-5283ea21f274 | -8.90555 | -44.77832 | 2025-05-30 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b8583700-e5b1-372c-bbab-f36b3a168d50 | -11.03991 | -50.78 | 2025-05-30 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aba6f80a-d5d3-3644-b3dd-012bf59ea054 | -8.9048 | -44.77665 | 2025-05-30 04:46:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3834d3de-bf52-31b0-8432-be65b5feee31 | -11.56021 | -47.45716 | 2025-05-30 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f5b326-5ab9-354b-a361-9ee24986aa01 | -10.05373 | -48.27998 | 2025-05-30 04:46:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 29b34389-3f3d-3384-8859-5f140be1f070 | -7.18426 | -43.10627 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| dcc78ca4-6762-3403-9bc2-11d25f9119a9 | -9.71946 | -48.31687 | 2025-05-30 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9e09337-29be-3235-b045-3662ea294c90 | -6.6369 | -55.00792 | 2025-05-30 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18ec89e9-eada-301f-aa49-f8093cb3d493 | -7.19293 | -43.11146 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c78a9238-042f-378d-90ad-3a75d69d5963 | -7.19345 | -43.11343 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f263e5bf-5d97-34dc-b752-3955e6113872 | -6.83142 | -44.65118 | 2025-05-30 04:46:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c4f25af-12b1-3532-9563-8b0c762aee2c | -9.36456 | -57.55016 | 2025-05-30 04:46:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d5d98d0-ddcf-3a70-8591-061224377043 | -11.56487 | -47.45255 | 2025-05-30 04:46:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de8cf98e-1124-3278-a6e4-c3a0a77e45fd | -7.53814 | -43.3206 | 2025-05-30 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aae4dbae-f832-3cb9-8fc2-db358fede1e8 | -7.90695 | -55.41526 | 2025-05-30 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdc35ab9-279e-352c-aa03-a1b8d853ca72 | -13.54055 | -43.68147 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 81bb5c5a-55c5-31b3-9a78-50dde3a7b5e6 | -8.52144 | -50.02015 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3ec9957-a9d6-3ca6-8ae4-a3d7519a6d2e | -7.71154 | -49.34837 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae7f2c05-8ae8-3cfb-b09f-3b2a3f20636e | -7.08683 | -46.04577 | 2025-05-30 04:46:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README10.md)
