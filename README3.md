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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91e3fc23-dc5a-3bfb-a203-1a56c1da733a | -11.8879 | -50.3837 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a648d1b4-51ea-338b-96f5-23e71b7ac8c5 | -11.8066 | -47.1082 | 2026-07-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 117.1 |
| ea634639-0a7f-32db-929b-bd71f33f931b | -11.7548 | -50.3778 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 865b04ec-0f46-356d-ae4d-5f185050a202 | -11.7357 | -50.38 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e8156916-db02-3017-90ca-c964003be99c | -18.8004 | -51.2417 | 2026-07-23 00:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 63db7a16-1bf2-3fa1-acb8-aa3d0e515317 | -11.7929 | -50.3734 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| dd902e22-e4a2-3d6b-bc21-403aec8ad625 | -11.7879 | -47.0884 | 2026-07-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 241.9 |
| b66bd993-9bbd-31ef-b288-1e0b688f3295 | -11.6602 | -50.3459 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| c8550de7-54bf-3a48-a684-e899aa8d1100 | -11.6792 | -50.3437 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 4fae96cd-5f4c-3d98-8cf4-46001b4f97cf | -11.7687 | -47.0909 | 2026-07-23 00:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| a722ec81-050f-3f64-b800-8c88f4955063 | -18.7999 | -51.2638 | 2026-07-23 00:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 76.2 |
| eb946b10-bf9d-3aef-a1ae-19d87c404678 | -11.9072 | -50.36 | 2026-07-23 00:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| a0d5aff3-bcb1-3f5c-9a93-3eab24c92369 | -11.8066 | -47.1082 | 2026-07-23 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.5 |
| f008f00b-e345-390b-9c47-c442cf69b990 | -11.807 | -47.0858 | 2026-07-23 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c6253c0d-1bb7-3cb8-8526-ea48b85d08ce | -11.6983 | -50.3415 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2e35ffa4-ff30-37fd-8ec7-452dbf51e782 | -18.8004 | -51.2417 | 2026-07-23 00:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 1e526c86-c1a6-3e01-9bb5-dcea26c61e3e | -11.7929 | -50.3734 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| edca5dda-4e2f-3d07-8370-2fb95a04d944 | -11.7875 | -47.1108 | 2026-07-23 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 11c0283e-15b4-3ef6-b989-40744c57659f | -11.7879 | -47.0884 | 2026-07-23 00:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 28f3649b-66f5-33b0-baac-0d337c76aaf1 | -11.6602 | -50.3459 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 9951ad19-53a8-372d-a0f9-45c6a36332f0 | -11.7357 | -50.38 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 264457a5-3a15-3443-867d-e35768baf17f | -11.6792 | -50.3437 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| cc6b86c5-bfb1-3ae1-951c-2ee3d717ce8d | -11.698 | -50.3629 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 0252fd36-ecc7-32c8-9b60-4af59e8ddbcd | -11.6789 | -50.3651 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 45ff4682-0c4f-331c-8503-53ac9a91ea42 | -18.7804 | -51.2453 | 2026-07-23 00:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 36921538-72a8-3c25-9333-98171f511344 | -11.7738 | -50.3756 | 2026-07-23 00:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 54e495b2-b3a9-323e-9b0e-b7ef81d51703 | -11.76255 | -50.38263 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 0db2e17e-db46-3dd1-80cb-b3e2591771ee | -11.75984 | -50.36554 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| d24efd95-e78c-3716-9fdf-2200b878a257 | -11.79868 | -47.09084 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 5889d3a7-55f7-3f84-aded-4c7d526fcce6 | -11.62421 | -50.32425 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f67ccd24-49f3-350e-84b1-f1c3a5ec238c | -11.93362 | -50.37626 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| d7ded04a-5908-33c1-b6c0-2b45b4445830 | -11.7919 | -50.37191 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 667c1dff-17db-3f4b-8c35-7ef58c274d6b | -11.68945 | -50.34868 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.8 |
| d5408233-ca87-3d81-ba5c-df26335bf285 | -11.91904 | -50.36129 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b2461860-23d7-3357-91ba-637b2f634172 | -11.79264 | -47.12858 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 160.6 |
| 813490e8-28b6-3f1a-861f-259113be96a4 | -11.94546 | -50.37426 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 46711339-aa63-39bf-aba7-61d3f8505153 | -11.981 | -50.36824 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| 9f5937fb-4a36-3d47-b0d0-36f586b7274f | -11.96649 | -50.35326 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 90edb2f6-f300-30a8-8420-55156eff1c31 | -11.99865 | -50.35966 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 306588fb-0704-32e6-84ef-2394214d0b6a | -11.90717 | -50.36329 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 705c7955-0ae8-322b-b78f-187e9482c252 | -11.90992 | -50.38026 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 8e633f8b-bdb2-3fae-8599-db2bfd95cec2 | -12.03419 | -50.35363 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 00c5c763-90f1-3286-9fe4-aa571bb30a4d | -11.66285 | -50.33548 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| c07b37e0-e86f-3dfc-9355-18043cbb0534 | -12.02234 | -50.35564 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 8f1df048-f05b-3b51-a95c-52c9eadbc05b | -11.97836 | -50.35123 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 100658ea-9323-3850-9d56-fd2fbddbb296 | -11.94277 | -50.35728 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 35412fc1-4a39-3b9c-9492-5a116c674b4e | -11.6748 | -50.33346 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 81d4ab72-f41c-39b8-9a18-623391f6ff53 | -18.79683 | -51.2532 | 2026-07-23 00:35:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 1e45d784-e73f-3dfb-8f59-6ae4eab36704 | -11.69214 | -50.36587 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.4 |
| dae99430-aa01-3a65-92c3-f1e4a564cb5c | -12.01322 | -50.37458 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 954aaf68-9f8a-3176-9909-fb9310918e2b | -11.80403 | -47.1211 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 55e65638-425a-3f4c-93b6-1a2f6f915b38 | -17.57616 | -47.50613 | 2026-07-23 00:35:00 | TERRA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 0b023b70-80f5-3221-ac0f-cf482e813e6f | -12.02505 | -50.37257 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.9 |
| d2e5dcc1-50ab-3222-9cb6-17dd7ae8c4eb | -12.01049 | -50.35765 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| a793af4d-922f-3f7b-92cb-14fd88513cdc | -11.78631 | -50.3786 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| cc7f0e9f-02f1-36ed-934e-485261daa0b8 | -11.9868 | -50.36166 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 0f68ab6f-b389-3c53-b467-24a087ddf222 | -11.96916 | -50.37025 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 0fec82f6-898e-3b0d-9f5d-7173879c52c2 | -11.81313 | -47.34032 | 2026-07-23 00:35:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 0616530b-ca75-3113-9788-6d14b399a860 | -11.89223 | -50.38985 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 3ed4904c-ee6e-3430-834b-4a64ed256411 | -11.78748 | -47.09831 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 489.2 |
| 5105a91b-94da-3de1-b5ed-e6b3a0142c55 | -13.32399 | -54.31278 | 2026-07-23 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 67179428-d84a-36c7-9eab-675550020389 | -11.66559 | -50.35272 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c16f0e31-cc07-3c5e-9042-e21e87c0323c | -11.77215 | -47.10118 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| cb6de21a-8587-3698-85fe-0975e3cdb88f | -11.79819 | -50.37659 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| da263c06-8d0f-330f-bde5-f0f64b2dfba4 | -12.00139 | -50.37658 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 6191c01f-5baf-308f-b29e-861e9939dadc | -11.8028 | -47.09536 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 2c53ffc1-b573-374d-99b0-34be77e02fcf | -11.73604 | -50.36956 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.6 |
| f12d9a65-4a00-3eed-aa7a-2880087d268d | -11.90145 | -50.37085 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 33684594-b13f-3c03-8de7-a571c169bfd5 | -18.78696 | -51.25488 | 2026-07-23 00:35:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7c9bfed9-70c0-3ccf-98f0-541184c09c4c | -13.36914 | -54.3059 | 2026-07-23 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 77f679f7-7976-3a28-9657-bc0bf4e1e1e8 | -11.97217 | -50.34669 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| dbed5f15-efe1-3dd6-a835-d99773526869 | -18.79499 | -51.24149 | 2026-07-23 00:35:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 140.1 |
| b6bf8347-024e-385b-b20f-a1df0d50b2d5 | -18.54819 | -56.82484 | 2026-07-23 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 77259877-98a3-3305-90c0-5346b39193f4 | -11.61225 | -50.32626 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f2ccbc89-aaf0-35da-8731-7c20cd151d3b | -18.54951 | -56.83543 | 2026-07-23 00:35:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.0 |
| a3753f82-d4ab-31ec-b983-b3fb5713fbc3 | -11.77174 | -50.36353 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.1 |
| e7f0d1ee-5e39-343f-99a8-b8626395b6ee | -19.70621 | -48.08469 | 2026-07-23 00:35:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 23.4 |
| a9a22859-e99b-3877-9093-d15e3133916c | -11.99285 | -50.36621 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9ede1ff6-1fd7-3e53-8bba-8959538cc58b | -11.78874 | -47.12398 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 223.5 |
| f986c0cd-24e1-31a0-921c-986db87b6999 | -11.88622 | -50.38425 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 16df5adb-6e97-3d58-b643-a54043abc05b | -18.78511 | -51.24311 | 2026-07-23 00:35:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| d7c3295a-7ace-33fd-94a2-358d7d835bb6 | -11.67752 | -50.3507 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ed3f42be-ceeb-3c41-bcf9-009cb52d7d6a | -11.69755 | -50.35844 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.3 |
| d9e14510-47fe-349c-afa6-2409730addbc | -11.57633 | -48.40546 | 2026-07-23 00:35:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| d1ad8094-000c-39c8-af26-805c62c2689f | -11.77443 | -50.38061 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e075b171-9922-3f78-b660-1321405f4459 | -11.70405 | -50.36385 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 1a7e511a-eb24-3a05-8c8c-3946262108cd | -11.74794 | -50.36755 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 19e43c90-b978-3ca7-9008-143ef7975ac2 | -13.33301 | -54.31139 | 2026-07-23 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2cf11985-5658-3a09-a355-c3557ac3c98d | -11.9309 | -50.35929 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| ba22b15c-508c-386a-9516-b9ed49548f84 | -19.7095 | -48.07856 | 2026-07-23 00:35:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| ff4cf354-fdbb-3c02-b7f0-14d4167556cf | -11.70138 | -50.34665 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 0d746143-490f-300d-81c0-30f898ce2be2 | -11.78336 | -47.09377 | 2026-07-23 00:35:00 | TERRA_M-M | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 406.3 |
| c29da685-b1c8-3029-bf00-d764de8de48e | -13.37817 | -54.30452 | 2026-07-23 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 3ad414d4-4da2-3839-8e41-d8585203bdc4 | -13.31731 | -54.32942 | 2026-07-23 00:35:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ff14a388-31a7-366e-b342-46ec37f61f01 | -15.71404 | -53.7535 | 2026-07-23 00:35:00 | TERRA_M-M | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| de06411b-32f2-3644-9f76-5f71bb1192ac | -11.90408 | -50.38784 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 2e2e68a6-da55-3229-977a-da75aab3a416 | -21.04551 | -47.79042 | 2026-07-23 00:35:00 | TERRA_M-M | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 14d0b90a-5780-3404-b469-5adb2b696644 | -11.79469 | -50.38893 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| bb453434-94d4-3ab3-8b52-fc605661c477 | -11.92177 | -50.37826 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 6f3fd0b9-2cbb-320d-8f23-246e1e9e984d | -11.97495 | -50.36367 | 2026-07-23 00:35:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |


[Clique aqui para ver as próximas entradas](README4.md)
