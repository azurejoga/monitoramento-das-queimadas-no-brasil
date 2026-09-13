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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f5398815-6d16-3180-80b0-e2be0997ea1f | -9.37864 | -50.11795 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0eb3540e-a4e1-3c93-b07f-3c7f8902b2d9 | -8.54212 | -54.71478 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 732386ed-6ba3-3973-8318-c30f31eb3909 | -6.72659 | -45.41588 | 2026-09-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00c51142-ac69-332f-9a43-77fad59dadca | -6.15466 | -59.94381 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bce9baf-65cb-34f9-9fb9-e9fbd21db776 | -6.132 | -57.69656 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 28e7a67d-9872-3c1b-b1ca-090f784e65d6 | -6.24027 | -51.69879 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 006c1bac-f7f8-399b-9a6d-b2229927e66d | -6.67243 | -58.87883 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d523d447-ade0-3455-9dca-0b24f4a4fca9 | -8.54666 | -54.70792 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3b4a86b-72ca-3c72-b646-c247e9cad82a | -4.8713 | -55.99664 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff421e04-5298-3a10-a225-00ee54ff3c88 | -3.04194 | -51.25763 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfba950f-26a2-3ce7-895f-ea7b01d1fe7a | -2.95363 | -50.41415 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6542b7c5-021d-36ae-a2b3-f1a907a132f7 | -6.28952 | -59.92676 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 773339ff-acc6-3ecb-95db-4573dd46f3ad | -3.35456 | -58.1879 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c5cd5136-9f1e-32e6-a129-e9f4e4f1a221 | -6.78263 | -59.85121 | 2026-09-13 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 974ff297-06ea-3639-a27c-1ac7d5b794cd | -5.61276 | -44.85256 | 2026-09-13 05:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dfb3c98-82a1-3f36-8a7d-6dcd90964db1 | -8.53361 | -54.70209 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f31280e-8c47-3028-a02b-2322244426c9 | -3.45465 | -47.46684 | 2026-09-13 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef463754-fecf-3295-ae29-4ce0a4b81db2 | -6.08407 | -57.86326 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f148ed2a-e0f0-326b-a304-a14db4a78deb | -6.1354 | -57.69714 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e830dfca-458e-3308-9b21-4a280d735f41 | -8.12017 | -54.79291 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c45ed524-96e7-35ee-ab2d-034df8bb6540 | -3.52262 | -54.47378 | 2026-09-13 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 49406eda-ef43-356f-acff-be6ec0992934 | -7.8667 | -54.69104 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aef48ba4-1446-3ac3-9b74-0f54a9f88446 | -2.66922 | -57.53558 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 166c6171-5726-3164-8572-073163a9b015 | -6.09516 | -57.68672 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc8a69ce-ab61-329d-875f-12fe3aca80e9 | -8.60894 | -55.23083 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d301541f-6cba-3ab5-98b9-1a2928947716 | -6.86079 | -47.42996 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a9b97fd-4ee3-34f7-aee7-f99ab3aba56d | -5.90407 | -52.10156 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f12de248-46d9-3c6e-a8a4-e31f3a0715b1 | -6.84956 | -47.43471 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 872f9c8d-21b9-3ed8-ac9e-dd4e60f10598 | -5.97919 | -57.77495 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae6a55d9-b7f1-37bb-9565-9bbe46e36036 | -6.13096 | -57.68133 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 402c56c7-a614-3cad-a226-e95d32c73f58 | -8.12242 | -54.80073 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb43f86c-dd6b-3bc7-920f-3465b7fd6392 | -7.8554 | -54.69677 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e68c3999-a017-379f-a905-d31b91134fe7 | -8.54326 | -54.70739 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00ff1d1e-c563-356e-8d87-1aa94f3de3f3 | -7.52299 | -47.33379 | 2026-09-13 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| faba8e2b-62c1-3603-be3f-7563b6bc0a43 | -7.86161 | -54.70158 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5a6ef33-a21c-34a4-8194-1cb4eb6a43e9 | -3.38555 | -50.75761 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8ca6876-790d-3a60-9d96-fbb971efc185 | -3.1651 | -58.6485 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6652052c-798c-3917-9589-a66020ad50dd | -6.79132 | -58.79436 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31fc5aed-a5bb-3269-88b1-c99b2df54660 | -6.5974 | -58.8507 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b9e9b6d0-d11c-38ee-8123-549578efe45a | -8.54156 | -54.71847 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a46a1357-6dfc-3b43-a9b3-2bd483d88e50 | -6.6368 | -58.5201 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5f7e8168-1740-3834-8bd8-ac4fbfd5fb70 | -2.46963 | -48.04293 | 2026-09-13 05:10:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8b7b199-860a-35ad-b8fc-944dbf70e88f | -7.86447 | -54.72813 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7a118e6-cb4b-3cae-a0fe-5799431975c9 | -2.96698 | -50.42374 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 205c0d2e-c242-38f7-a24d-26ac2f4a4ece | -7.87236 | -54.69942 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8dec14a9-4cb1-3b33-9544-9e42a35f13a8 | -6.76941 | -59.42739 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b2b91d6-c0a8-31d2-8a8b-d0c511a3f0da | -7.01287 | -44.62707 | 2026-09-13 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf36b849-47cf-3b9e-be8d-8dc310b2f45f | -6.28121 | -59.93011 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 16d1c98c-558d-312f-93f4-3b1a984bfb30 | -7.37366 | -45.3489 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 928e9d52-8d75-3bfd-be93-3ff7c0d2fbdf | -3.7136 | -58.86762 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 30ea4129-c6e0-3aa0-982d-1da650f5b3ae | -6.5089 | -47.60192 | 2026-09-13 05:10:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a9154dd-011d-3466-8218-65c9d11cd5e1 | -3.56778 | -53.0043 | 2026-09-13 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 045ac4ae-82fa-3117-b5c3-cced976996d5 | -6.01677 | -57.69411 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff9e50c5-219b-3b8e-8f25-76e36a2495a5 | -6.67664 | -58.87539 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0b40637-5087-324b-bf4f-4802851c8c7c | -7.34142 | -49.55783 | 2026-09-13 05:10:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e6a6e39-51db-3af9-91c0-6b0574320e01 | -3.96288 | -59.3573 | 2026-09-13 05:10:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b340f5f1-d34c-373b-89d9-fa947405fc77 | -7.86218 | -54.69787 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3cf33dc7-0f06-306b-8c58-a790590d693c | -2.96556 | -50.41594 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8e533e0-953c-399f-9658-ef3dfe445a21 | -8.11226 | -54.79916 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98d977b4-3334-3c88-9965-01e2c4ac27b8 | -1.2272 | -54.12229 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5224359-4338-35b2-ba13-ef62ba3400b6 | -8.12412 | -54.81216 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 585ec544-10bb-31fc-a67a-ddd976dc8162 | -2.66409 | -57.52295 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e953d1e2-3006-39fc-bde1-ba5284d9fd9d | -7.38502 | -45.35496 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8fcfec57-f26e-3691-a2cd-479cd91473b0 | -2.72167 | -53.97533 | 2026-09-13 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dc62586-bc9b-3fe6-8d40-91bb2753aef5 | -3.7907 | -59.36612 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 64473319-56f4-3e0e-a225-7cde636c19c1 | -3.91076 | -55.73492 | 2026-09-13 05:10:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b16b51bc-95af-3bb6-a286-f06611e74b1e | -2.96797 | -50.40062 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8d5263a-2988-3fd1-9ed0-786fffae79ef | -5.96589 | -47.21203 | 2026-09-13 05:10:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6d4a9bb-c9df-3076-aaff-6fe0f41330ae | -6.61448 | -58.85767 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46ab094b-4e25-308e-bc92-30bfb503ad45 | -7.86503 | -54.72448 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c1eb3031-a3d8-3f72-b8b2-cb91f3d07b4c | -4.10999 | -54.92556 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca4fd96c-c06a-3235-946f-cc8df276384d | -2.95207 | -50.39816 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 995e76df-c4d8-37ca-8380-c1fc06377640 | -1.73233 | -55.24549 | 2026-09-13 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6a70443-0b3a-3b7d-8f26-98147497af76 | -6.66821 | -58.88228 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fd43413-80bd-3237-a0ac-1307a4513fc4 | -2.94159 | -50.38698 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d056e43a-dff6-31af-b1be-43b375ed94ae | -7.85992 | -54.68997 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 265a0d64-e4e4-3514-aa59-c51b976fe0fb | -5.88707 | -52.06218 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f46e2e05-8854-3d3b-891f-513ab73f71df | -3.9812 | -51.08586 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc7e59ee-3db0-3b4b-9019-18d459209c9c | -3.04792 | -51.27065 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18602792-3832-333b-b044-018f3f9917fc | -3.74022 | -61.75337 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 049ad1db-70ae-3de0-82c1-2bd4c4cdba66 | -6.67309 | -58.87481 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 56fb2e71-1ead-328e-a813-175b71b1851f | -5.86296 | -46.22829 | 2026-09-13 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 21a6c801-f0dd-3125-9b32-460e22192c52 | -2.61479 | -54.75796 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2842772-3af3-31a8-8918-2efcafc406d5 | -5.18561 | -49.34871 | 2026-09-13 05:10:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a17bcbb-ff66-367b-b68b-8bc0ea1e32e1 | -7.86898 | -54.72137 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8631d145-169e-3805-8000-b3000b1fc8d6 | -2.71656 | -57.606 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b2348f2-77bd-3579-b481-36549f7221bc | -7.85597 | -54.6931 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 892ed42e-ca78-36fa-b49a-31e4c90f72b1 | -1.73089 | -57.15417 | 2026-09-13 05:10:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6bbd61f0-2666-3cb3-9263-6fefd7d2a647 | -3.6408 | -58.62657 | 2026-09-13 05:10:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| facc664f-06cb-3709-9532-71a113d626f3 | -6.28876 | -59.93131 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37abf440-ffd0-3c4f-90e3-38c0d2aa9f40 | -6.75639 | -58.96215 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58ee7fcf-38d9-335b-aab0-85da4fbbad9a | -2.63573 | -54.75423 | 2026-09-13 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcdeea04-f078-359c-8277-8359bf7d7345 | -5.48443 | -57.23617 | 2026-09-13 05:10:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a579999d-d630-36b1-8dd2-6dafb2940730 | -1.2261 | -54.12927 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7da47543-cd70-3444-948a-99308961ba9f | -9.37539 | -50.10842 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 64ef55e6-04e6-360e-ab76-1adbc755c61c | -2.94092 | -50.39126 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba3dc134-75d6-3f5e-8fe1-eb4aed1d89aa | -6.13599 | -57.69346 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4e61e270-6b02-3527-bcf4-5f999c1e411b | -6.08772 | -57.90591 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 10152d15-252c-3095-9724-c1cf5d31bf25 | -5.99897 | -57.71766 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0123d182-59cb-34e7-8d72-51def1207be8 | -6.07721 | -57.86219 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |


[Clique aqui para ver as próximas entradas](README44.md)
