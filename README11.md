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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d8b519b-6cb5-3418-958a-26d89cd9be46 | -1.81825 | -54.16811 | 2026-01-06 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c42932b4-cfd2-3074-bbf1-6744cb0f287d | -2.74194 | -42.5866 | 2026-01-06 04:53:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dcf8a76d-cbfe-3563-ac56-e623ba5c7da7 | -4.1471 | -43.65123 | 2026-01-06 04:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 33accb77-5950-3db7-b9a0-d403ae140bdf | -3.21473 | -50.39996 | 2026-01-06 04:53:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47b65a51-7620-3f49-a856-1e9977a8e656 | -2.4463 | -53.81914 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98ae4b27-3b8f-3de9-85c7-8d4c755bdc0a | -2.09418 | -53.52026 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 20e9d301-3c14-3533-afc3-196a27f9226b | -2.52823 | -47.82603 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 851abacd-3669-3609-91db-83585b97a556 | -2.53583 | -47.82714 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 92b17210-d376-3b6f-9dc2-8c30f1024050 | -1.59742 | -53.35736 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48714738-45c9-3749-9be1-09c0dd88e9ac | -2.93053 | -48.22729 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bfc62b6f-8055-300f-9177-411e2a72be8b | -3.33154 | -52.70077 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1e1724b-39da-3b69-9588-96d9461cadd8 | -2.33997 | -47.86734 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 818ef8c9-3d24-39aa-8b61-adf57bd100eb | -3.70052 | -43.43935 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 932276ed-90ab-345d-a5fe-85220c5d5e34 | -2.2759 | -53.78901 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3e462ef3-0af8-3fef-ad23-033411535d7b | -2.6442 | -45.65095 | 2026-01-06 04:53:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4da3642f-aa48-37e5-9140-f60afb978d45 | -3.1839 | -51.09446 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4816540d-99eb-395c-91f3-4e56e7e3cb56 | -2.92308 | -48.22609 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d981780-61cc-34b9-9ec5-ccbf9478ccda | -1.36492 | -49.41651 | 2026-01-06 04:53:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b74618fe-1106-31f1-80d1-03167c9cffe6 | -2.17761 | -48.13831 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c09fc05-92be-3517-9d24-39d3d01dc71f | -5.53737 | -51.43779 | 2026-01-06 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6497eea8-ede9-3314-886d-752009fd876e | -2.64859 | -45.65162 | 2026-01-06 04:53:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b954223-f3eb-3509-877f-7dbc939d3931 | -2.09476 | -53.51661 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2475d19a-aa18-39d1-9828-53c4fd0da946 | -2.63601 | -48.48478 | 2026-01-06 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c433835-9371-3394-b851-88f68fc5affc | -1.25441 | -53.48845 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ba45f14-45d7-3266-b1bf-323b96893394 | -2.71668 | -54.54709 | 2026-01-06 04:53:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 13fc7a12-fb8d-3476-9da6-d2b307ca3663 | -1.55345 | -53.30564 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0aec37c-6f5f-32e7-be6e-462133a7941b | -1.59929 | -53.99023 | 2026-01-06 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ff4ac6a-66ea-36d0-8909-76b69fef2c75 | -3.10234 | -53.07215 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81c7841a-6769-3831-9e40-57f217b6365d | -2.52372 | -47.83007 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 74f219f7-2a52-30a6-b589-abfe0d6cb22f | -1.97609 | -53.36017 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b5c5e87-9652-3e18-8edc-142c88ed3ec1 | -2.16044 | -47.90236 | 2026-01-06 04:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47c6542e-ce06-3539-9ab5-3419e570fa05 | -2.85705 | -52.80075 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5cfa491b-8d94-3a87-afbd-54acd70042b2 | -2.52443 | -47.82545 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e8ee99bf-9f14-30f2-9231-23f4c191e087 | -1.59581 | -53.9897 | 2026-01-06 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036306ac-ec41-3f68-8750-f88f80cbbf69 | -2.74299 | -42.59019 | 2026-01-06 04:53:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 670e0095-0ecf-3053-8868-2a716528b9f2 | -2.52752 | -47.83065 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 36c8eabe-5731-34bd-b259-09c8e6430a85 | -1.48039 | -46.13939 | 2026-01-06 04:53:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 722f93b2-0710-3d85-ae8f-b062a61d1fc2 | -4.06348 | -42.53158 | 2026-01-06 04:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9b30ba13-f6cb-3416-a435-6145aa19160a | -2.47981 | -46.30194 | 2026-01-06 04:53:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73e069c0-906f-3df3-9f72-0113f626d854 | -1.46585 | -49.08107 | 2026-01-06 04:53:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1367c0d1-2a7d-350d-ab1b-4853ad109898 | -3.72178 | -47.20668 | 2026-01-06 04:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84804716-212d-3415-a5de-e10838938222 | -1.35454 | -49.41491 | 2026-01-06 04:53:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e15e269-087a-351a-91c6-70b1a782c4f0 | -3.69659 | -43.43623 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 32b438be-92ae-3d50-b352-0739b2759582 | -1.82192 | -53.91139 | 2026-01-06 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3526794-dcb2-3b0e-94d4-c124401dad06 | -2.80649 | -52.94693 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0609602-7ab1-3dea-bb1a-9b41e0286604 | -3.39372 | -53.68069 | 2026-01-06 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2c16e47-00d3-3576-b18a-27261f480a35 | -1.898 | -53.2557 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b2f4b56-143b-3e81-b4e0-df854df958ae | -2.7414 | -42.59006 | 2026-01-06 04:53:00 | NOAA-20 | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 33895897-ba09-3052-b680-b96ea54cd824 | -2.31203 | -48.42682 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d96ae219-0523-3b98-b7b3-e758ac18af8d | -2.27708 | -53.78157 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9ebf4eb5-f2da-32b8-be17-34070bbcab66 | -3.85556 | -54.10509 | 2026-01-06 04:53:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 581b8afb-80ed-33e5-ba2a-63e8d566f3ba | -2.66939 | -49.85373 | 2026-01-06 04:53:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 659db646-3fd6-3796-bfea-73bd2769f906 | -2.80983 | -52.94744 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c00976b-0172-3979-b945-eaa2f847498f | -2.46926 | -48.05958 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 634bfbdf-306a-3035-b5ee-15cc47c24258 | -1.358 | -49.41545 | 2026-01-06 04:53:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b0603c8-7fa6-3004-9a4a-fd929eb5fdaa | -4.06295 | -42.53526 | 2026-01-06 04:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24107935-c72f-3c25-9782-9f910a1eca66 | -2.44981 | -47.78262 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 34b2ea09-5633-39a5-8843-e82e7dae307a | -3.03201 | -46.92641 | 2026-01-06 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 215f8a96-f445-336d-8d21-b69f161de891 | -2.92681 | -48.2267 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f58e857b-94f7-322e-befc-2ee176ff90ed | -1.59403 | -53.35682 | 2026-01-06 04:53:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 955ab6ab-148f-3f50-87d6-d3f6d1b9f2b1 | -2.18132 | -48.13888 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8783a2f8-5873-32e8-831a-48c027f98c46 | -1.81759 | -54.16484 | 2026-01-06 04:53:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ac5acb-ebc5-3016-bdc6-ddcbce158e27 | -3.18166 | -51.08693 | 2026-01-06 04:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 019f0050-78da-3abd-b84e-205b22439600 | -3.70099 | -43.43623 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| b20a2b65-2043-3131-8d90-1ab0b9f5a365 | -2.44403 | -49.02518 | 2026-01-06 04:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b9e014d-a0d8-35d3-aafc-a7f114b6cbdf | -1.97271 | -53.35964 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3bc6943-d144-3c7f-966b-3273a707a39b | -2.53203 | -47.82659 | 2026-01-06 04:53:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e3aa109a-bc00-3cca-b167-e906b7885bb0 | -2.25006 | -48.17496 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24ccb533-32eb-3998-a78e-41c3f4dcfbc9 | -2.81373 | -52.94445 | 2026-01-06 04:53:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f17de48a-af47-3ab9-a320-d88d65edf5dc | -2.98306 | -48.58597 | 2026-01-06 04:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c2a220b-cdb2-3c48-b82d-d7d14ed48f1c | -0.7423 | -52.42582 | 2026-01-06 04:53:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83d66b20-9a4e-33fa-b78e-fa6650768600 | -4.06242 | -42.53894 | 2026-01-06 04:53:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 49b4cc4c-f382-3168-a240-0ef6e8ba8a98 | -1.14311 | -48.10214 | 2026-01-06 04:53:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1c9ef363-61c2-3e42-94b9-9addd1f3b861 | -3.56359 | -47.17508 | 2026-01-06 04:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8efed77c-25db-34c9-85c0-ce22f44cfa18 | -1.6538 | -52.05398 | 2026-01-06 04:53:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a99d5b83-ac2e-3744-974f-a468eba5903e | -4.1518 | -43.65508 | 2026-01-06 04:53:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 205785c0-c3f2-3828-b787-c60f722e859c | -2.16113 | -47.89782 | 2026-01-06 04:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c49cb395-3564-311e-b9a4-f7765051523b | -2.87681 | -52.5688 | 2026-01-06 04:53:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1feb3153-8c56-3997-b224-7eba347d2342 | -2.78622 | -54.08522 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92ea8ac2-f2a4-3310-a4f2-0af02f2cef37 | -7.5656 | -45.6314 | 2026-01-06 04:53:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6493923c-8733-31bd-b298-72b60b8e9f53 | -2.27365 | -53.78104 | 2026-01-06 04:53:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 549fb4ee-b25f-36f1-9834-36a497562dab | -3.69705 | -43.43301 | 2026-01-06 04:53:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| db4dafaa-d10f-38bd-9561-13d037328bc2 | -2.25376 | -48.17555 | 2026-01-06 04:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f89248b-345d-3fee-ae0d-b772662138b3 | -2.08174 | -48.36804 | 2026-01-06 04:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ad4d273-493b-3e86-9412-7a8aa06accbb | -15.62197 | -57.33683 | 2026-01-06 04:55:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17b5a293-c487-3f6a-bf3a-30c66b0583cc | -16.20013 | -59.32568 | 2026-01-06 04:55:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f81a4914-3e00-3be2-afd4-883a25418a24 | -16.35988 | -57.30892 | 2026-01-06 04:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f771a3f5-e280-3d0e-95a4-860d7bf8c44f | -17.94476 | -54.7789 | 2026-01-06 04:55:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78890d84-1927-3f6f-8929-52a0a26e6d37 | -20.51197 | -57.99162 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d03538d5-caf9-37a1-9713-313a599605b3 | -16.06004 | -60.07291 | 2026-01-06 04:55:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ab3186a2-cc84-30a0-9790-3b898cbbe0bf | -16.07269 | -56.58908 | 2026-01-06 04:55:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1119636c-7f0e-31e0-9170-f64e8aa3a808 | -18.54786 | -55.44024 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 79deb642-ae6b-3f32-93af-f3583959e184 | -16.59325 | -58.21169 | 2026-01-06 04:55:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c8aa5eb1-7364-3a7f-b8bf-f0439275db33 | -17.65207 | -56.44627 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c958ac11-2faa-3db4-a1c2-6e070595d4fa | -22.49233 | -46.94326 | 2026-01-06 04:55:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06616d9a-821a-3e9e-8157-68b743a32e01 | -20.5155 | -58.01252 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| fcad1a9d-5e6f-36d5-a0c9-0f72876fe546 | -22.49764 | -46.94386 | 2026-01-06 04:55:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9a271f2-ea3d-34b8-917d-a6cff151685b | -16.04464 | -59.21815 | 2026-01-06 04:55:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 358c3c12-80ee-3c07-9651-09f7c10db996 | -20.50383 | -57.99815 | 2026-01-06 04:55:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a06fb651-721b-34cf-96f3-651ff79e3bb6 | -16.00638 | -54.78421 | 2026-01-06 04:55:00 | NOAA-20 | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README12.md)
