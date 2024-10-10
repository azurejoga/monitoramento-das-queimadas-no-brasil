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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34945a86-1062-3672-8060-417fd6701854 | -5.23968 | -44.7966 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3ac096ff-40f5-3eba-a090-5799dce35c40 | -5.23913 | -44.80009 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c99c959f-f249-35c6-bf71-c7b132dfdc20 | -5.23635 | -44.79607 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2820f147-8912-32e4-8327-f8450298b42e | -5.2358 | -44.79956 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c492eb9a-0234-3f87-a1da-d9c037829785 | -5.23302 | -44.79556 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e8751d4-5e57-3eaa-8617-ba8aa9154e29 | -5.23247 | -44.79904 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ba8e9856-3931-36b5-b47c-2a7b60d1b6b7 | -5.22914 | -44.79852 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f2c71905-a795-31a5-aeda-9a498d3a1e33 | -5.03725 | -44.49787 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c247ce7b-4092-35fd-a909-a70c486abf69 | -6.37579 | -44.69784 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 936c6aaa-94d5-3ee2-996a-b093635eee21 | -6.36333 | -44.56087 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cd30ee4b-f5d3-3ab7-a5ad-5b01482cdf76 | -6.36001 | -44.56035 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90d999f7-ebb3-3edf-a92b-d7610d1e23c6 | -6.35668 | -44.55983 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b977800f-433f-3426-98be-9cbf31721095 | -6.30973 | -44.25766 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4bd249e8-169b-3c12-9b9b-2667a1a29766 | -6.28889 | -44.56355 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d301b3b-8fbe-30ac-a10d-268fe2f087f0 | -6.28557 | -44.56302 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97eee299-f35e-303f-8c52-76d0ac94ad61 | -6.26526 | -44.97255 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05851563-7f38-3306-a660-0302b936d0f6 | -6.26454 | -44.17954 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a56c1f52-eec0-39fd-9506-c0816fe136f4 | -6.26176 | -44.17556 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a524986d-f51c-313c-af52-b9c68c21448c | -6.25999 | -44.79002 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b72729e9-25b8-33de-97ae-cde0bce704e3 | -6.25922 | -44.66543 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a1c034f-0b16-371a-85b7-0077a809b0f0 | -6.25557 | -44.79644 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a6a48ec-e3ab-3cbf-9d90-c7d3af36e9d7 | -6.25338 | -44.81033 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d1fd93f-80e6-3175-a078-82ebd09d19a0 | -6.25279 | -44.79245 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d4e9915-9eb0-3aff-8966-2c394dd28ef9 | -6.25225 | -44.79592 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26ad48f3-0441-3a29-b27e-151648069051 | -6.25005 | -44.80981 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a55d3ed-a447-3c02-a8e9-f6b21d6adf33 | -6.22635 | -44.18425 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc7e9e6f-703b-3805-93d6-ceeb3c6a519f | -6.21837 | -44.10466 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9d059b9-60d7-3f77-9bc6-fcf53e3b978f | -6.21747 | -44.17574 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51c5a942-d309-3771-803e-b7f613e792c8 | -6.2159 | -44.20746 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfbcdbc1-6306-311c-8ecc-c36b3871f294 | -6.21505 | -44.10415 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49c524dd-0b73-300b-b852-027895a45274 | -6.2145 | -44.10762 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2bddc32-8434-33fe-9b76-039dc720c678 | -6.21414 | -44.17521 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db6f0afa-10e4-3930-9feb-2b4240008c5c | -6.20864 | -44.18858 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78b2f8ea-45d2-3762-b129-c3e0527e2eba | -6.20785 | -44.10658 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e062378-b9bb-3d7f-89d6-a5f133f0aadd | -6.20641 | -44.18111 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d83cb87-7b74-3066-ab5a-81f96d94da51 | -6.20478 | -44.19153 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 281dd8ff-d805-3574-9773-772b1015bd66 | -6.20453 | -44.10606 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e93461f6-9117-367e-a4cf-98271c278c46 | -6.20308 | -44.1806 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf30de6c-e081-38e5-990d-b2287280e255 | -6.19376 | -45.03623 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b35682ec-5032-3d65-8d96-22341f4a90d1 | -6.19201 | -44.38135 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa0cda9c-bd09-3f99-a5c1-1c5fbb07565f | -6.19099 | -45.03222 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2426cff-9098-3774-bb57-07de90461786 | -6.19043 | -45.03571 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7d5f35b-0c47-3cc2-b2bb-48cf17d2ce2c | -6.18868 | -44.38083 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06fb3579-5afd-3687-bade-5682362c67d5 | -6.18814 | -44.38429 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 36b90a5e-2ebd-3a36-9620-8eac833dc9c5 | -6.18536 | -44.38031 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59cc10a5-ecda-3be9-9c88-db59620801a8 | -6.1811 | -44.45069 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9842a310-9073-3219-94e7-8546a3944734 | -6.16593 | -44.01112 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 715b59c0-dd3c-31f0-9890-18b67bbfecab | -6.14428 | -43.82193 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 69b744bd-ddc4-36df-b20e-de3531fd57ee | -6.14374 | -43.82543 | 2024-10-10 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2e5eadce-abe8-3f6b-9678-3f16c01c404a | -6.07723 | -44.64056 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f38a13c-00fa-3e3a-b1fa-008c33033bf1 | -6.07668 | -44.64402 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 980e66c1-254a-3491-bbf1-94f9a9b1c4d1 | -6.0739 | -44.64003 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30940b82-f754-3a41-bd42-cc3122065f3f | -6.07336 | -44.6435 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 975a4584-3038-3b02-9479-5ccf22a766f7 | -6.07003 | -44.64298 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 193ebaf8-2287-318f-b17d-3e115b738c77 | -6.06949 | -44.64645 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4685d907-b659-3035-ab49-3ebcda534002 | -6.06684 | -44.70646 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbe12853-b975-3c92-96f0-aab29e8d30f5 | -6.06671 | -44.64245 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 060fbe72-2ddd-394c-bb6e-16273a85c5db | -6.06617 | -44.64592 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1aafec54-c55c-3107-b98d-682e8d169c68 | -6.06351 | -44.70593 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f8406145-0dda-3589-b90e-558b45a25ee1 | -6.03969 | -44.23282 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15f9f04c-b893-3215-afdf-72003ed0a1be | -6.03397 | -44.37753 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6d54758-4ef6-3b0a-be31-edcbb57e41f0 | -6.03274 | -44.85765 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a7d411f1-8f30-3281-88f7-d555f06225a1 | -5.95282 | -44.74129 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05635f76-bbcf-366f-875f-48f4f124106f | -5.95245 | -44.85161 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7c2a5b8-1fe8-3e36-801d-0b9d2467558d | -5.9503 | -44.58457 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3cc3db2-12be-3831-b737-3f12561200e3 | -5.94975 | -44.58804 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5008dc51-b136-3230-9abd-782dd713c02a | -6.5249 | -44.56913 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d430e28b-1b52-379b-969f-d1f0b9ba0ef5 | -5.94967 | -44.84761 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bcac2840-4a79-37e8-bef3-733d501cb3ab | -5.94949 | -44.74078 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 12006b09-8ac3-3f1b-817c-9682eb9693aa | -5.94912 | -44.85108 | 2024-10-10 04:17:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a7c94b6-792f-39d1-8ce5-7e6dfef86920 | -5.94617 | -44.74026 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af52904b-585a-3e03-946b-c0997dae779a | -5.93082 | -44.53533 | 2024-10-10 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 656c6ad8-418f-337f-b587-2cb0036c961e | -5.9122 | -44.63181 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d4b8632-920f-3447-89c3-8b045926a516 | -5.8131 | -44.12295 | 2024-10-10 04:17:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a4f6de17-a334-37b8-8526-bf7aabf6c871 | -5.71494 | -44.4874 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39a02b77-172c-3900-8a8e-98180b529c08 | -5.70442 | -44.79134 | 2024-10-10 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52f179b5-39db-3c55-86a6-2e5014bdfea6 | -5.4935 | -44.2857 | 2024-10-10 04:17:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f730a5f9-e39f-311e-8074-143d12061c71 | -5.49148 | -44.53055 | 2024-10-10 04:17:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd386e61-7359-3c7e-ada7-a3e1999f3669 | -6.81079 | -44.46798 | 2024-10-10 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 058cbbb9-bf9d-3a9e-8ef8-e94c1b5c7d76 | -6.62097 | -43.75956 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b673bbe8-416f-37b6-92d8-06a03c72bb34 | -6.61763 | -43.75903 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e986576b-4ac1-367c-9deb-2e2573f3a6b7 | -6.61033 | -43.73992 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08043808-8956-3b9d-a1f2-a0eb838618fe | -6.60978 | -43.74344 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b9b38bc-34fd-3f48-b58c-ac022a2318df | -6.60821 | -43.77558 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d507c56f-d4da-306a-b9bc-06f2187307f0 | -6.60808 | -43.73236 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| af3da97e-3d43-34d6-b556-72a9815b9269 | -6.60486 | -43.77506 | 2024-10-10 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b24f202c-6638-3c30-8f3d-44ff97f32335 | -6.73 | -44.16336 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2291363e-11c0-383c-ac36-46a8077ba48d | -6.72884 | -44.56195 | 2024-10-10 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f68e404-b85d-31f4-8b77-30429d3b8b82 | -6.72829 | -44.56542 | 2024-10-10 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b715acf-2870-3d58-98e0-a2622a32a9f8 | -6.64867 | -44.01132 | 2024-10-10 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc15698f-32be-319f-a9c8-d64c3e95c05b | -6.64533 | -44.01081 | 2024-10-10 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be67e428-75dd-3eba-a97c-7e12977fe758 | -6.52545 | -44.56566 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d422e10-a0aa-391f-bae5-b5ef8835176e | -6.52158 | -44.5686 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7b51d170-4520-3475-ab67-b4b04d699abf | -6.50996 | -44.33926 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12bd0470-d5fb-32c7-a07c-c87877802473 | -6.50941 | -44.34272 | 2024-10-10 04:17:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ed155591-7b99-39b6-9983-916019201a90 | -6.5091 | -44.69101 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b749dab-e304-31eb-a979-75a502bd077a | -6.50578 | -44.69048 | 2024-10-10 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d47e70b-b2ac-3950-8dcd-f62fed142984 | -3.49336 | -44.90559 | 2024-10-10 04:17:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 77396393-bb52-39da-92ac-a55c9c0a6f6b | -3.49279 | -44.90911 | 2024-10-10 04:17:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 87057289-3f3f-3b65-a90a-5ea7f09fa605 | -3.22078 | -45.45438 | 2024-10-10 04:17:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README60.md)
