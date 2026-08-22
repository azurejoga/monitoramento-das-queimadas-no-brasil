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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e6b11718-9afd-3388-9416-cd83c0ca33fe | -6.93706 | -59.31001 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8089b8fe-399f-3924-94e7-40933e7d68c9 | -8.52938 | -55.31839 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5c41a13-da42-39f3-bff3-e3b25a86af72 | -6.79455 | -58.64059 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69ea7fa3-76e3-3092-9503-9324dcd39829 | -6.38215 | -54.95075 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dd6681b4-5e70-3f80-a3d6-a30dabbf5bf6 | -11.16361 | -54.01609 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8ff8f2e-90d0-3e73-99f7-8d97844a4cb4 | -6.11657 | -59.9194 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8258efa-648d-35ea-a45b-e4ed2520b61e | -6.75499 | -58.65578 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f541b3f5-0473-32e5-a237-5af482a83fd4 | -6.11817 | -57.68976 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3084a4e-0382-3951-936d-5440f7220bc7 | -6.77382 | -58.68728 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| aa0a88fa-3593-3f61-9d2c-f3e73f06e08f | -7.0566 | -59.84046 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e096bbf-d2c0-3d3b-b5e8-6256dfc231d1 | -6.87752 | -56.63754 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6afafa6-2259-3379-80e6-f6d298fa7fa6 | -6.01054 | -57.79426 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5b33202-4073-3960-96e2-bc285a791374 | -6.8006 | -58.62369 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e76e9aa9-0d21-3cdf-927f-d1661f0323ff | -6.97494 | -59.58602 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b760654-8c58-323a-b3bd-5e66972b93a9 | -6.13933 | -59.90508 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18a285e5-3af2-3394-a780-6cb0b9d94641 | -12.79813 | -51.4799 | 2026-08-22 05:23:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0908512-874f-3920-add8-af9e2d2fd85e | -14.54368 | -53.00701 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14a7ea81-bc1f-325f-89ae-d089f0ebe26a | -8.09151 | -50.03679 | 2026-08-22 05:23:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f606434-c685-3e1f-b80a-b0041b2686fa | -6.81852 | -59.39398 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 248401b9-217c-33f3-b897-cec39e7e34f6 | -6.38757 | -54.95903 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe64dc69-7dcf-3735-81dc-d1e62e8d2a29 | -8.55222 | -54.85521 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c60cdf0-cd9e-37bf-8fc3-7eb14a54218e | -5.96248 | -51.95699 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c5d72cd-3e38-3bf7-b781-e04071e1680b | -6.92056 | -59.34995 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ed4731f-7930-3b92-b2de-67956acce7c9 | -6.13488 | -59.91155 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78a3770f-c8f6-3954-bfb1-753f64aeab90 | -6.81397 | -59.89127 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6186b1d9-9c83-392a-b82a-acab8228ce53 | -6.12269 | -59.90242 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea0ba499-b71c-353f-b017-c684de030016 | -6.13765 | -59.91558 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d4e22a6-bdac-3b0b-8943-409e002c1b3b | -6.85494 | -59.44234 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ad2e35-f15c-3a92-8bca-9b566b39b882 | -4.36697 | -55.7723 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d548e722-3097-356a-9921-048e90d987c6 | -7.55087 | -61.18873 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4090c5f-43fe-3f85-ab01-81886d0705ea | -6.8891 | -56.72753 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a953d96-9196-3c4a-8c11-c489612f627b | -6.84997 | -59.4309 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b08d9723-b9bc-3577-a6f4-57f207d237cf | -6.77279 | -59.44703 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 309b0b37-9bd4-3db1-88df-be158182c072 | -6.97439 | -59.58948 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd2d2ba6-9d3e-35d8-9b6e-93dcc9f82df0 | -6.12546 | -57.68723 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c59e646b-125c-3271-9922-d479e0575b99 | -6.81411 | -59.40037 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c6a1f25-9015-32b3-b538-f706a8aaa3b7 | -6.12325 | -59.89893 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f51dff2-7dce-3ff5-99b4-69dbf6cc593e | -13.95393 | -53.84907 | 2026-08-22 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1930c9d0-62da-3cd2-bb99-3504d7661c75 | -6.86163 | -59.03559 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc30e72f-5915-3827-8bc5-fb0fafafe76d | -6.7427 | -58.58247 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a305c83b-0aaf-338b-b014-f16daed46d3e | -7.68763 | -46.16632 | 2026-08-22 05:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b484485d-64e5-3a23-8065-d38e6d004770 | -6.95767 | -59.0508 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20abd6f2-b4f2-338b-97c6-5e16f540150e | -6.58424 | -59.00583 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e02d52f-92bc-3441-ab23-7a6f4e80a723 | -6.00385 | -57.81512 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4aeaabeb-78b1-36f7-928c-498253b06ae0 | -6.79564 | -58.63362 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 461b607f-ea50-32da-a280-d5b56cfb8bd3 | -14.54856 | -53.00775 | 2026-08-22 05:23:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec56ffae-783c-3a47-be5b-81cb3691bcdc | -11.16627 | -54.0293 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c855fa55-e07f-33d4-a278-a195868348e1 | -6.12879 | -59.90698 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb9cba32-0aec-3d9a-bab9-669e4b0f6628 | -6.25301 | -55.41862 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 963f281b-f1c3-3a79-a4af-f10eb0c37366 | -6.80365 | -59.42354 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| abdd0533-5215-35b1-88c8-d607795a039f | -11.16853 | -54.01247 | 2026-08-22 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6092b83e-f769-3f34-96bb-26e3fef33154 | -6.60398 | -58.38561 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c359743d-4fd6-3d82-8cd1-ef1ec7723262 | -6.80541 | -59.66883 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| beb437e4-8457-3f7f-a47b-c15df4ee6d24 | -6.76004 | -58.71004 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5fcf81c-060f-3dc0-a5b6-8ddb91ab49aa | -6.79292 | -58.65101 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 766c9248-9b9b-3e14-a00f-fc0e0cbed70f | -6.38062 | -54.95316 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f210f633-472e-3fb1-bbed-72849de85a1c | -7.0218 | -59.54735 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52cfeeff-acc6-34b3-ac17-cacebb3bee35 | -7.54656 | -55.56086 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0b98c9c-5ca3-332c-83fc-bc0c588bca7b | -14.40126 | -51.8017 | 2026-08-22 05:23:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7c62d4f-1fe5-3d74-a1a9-2c781102b3e8 | -6.80265 | -59.66484 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f1d96e83-e605-36b0-aa81-957d656884fe | -6.88866 | -59.44419 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d5d94f8-f11a-3cea-b697-7b26cc8ef1dc | -7.60781 | -60.94276 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7abd6143-b2f8-3c3c-b9f8-9f6738320759 | -6.75833 | -58.67772 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f954f081-ece3-35e6-87da-249c58a6f20f | -6.25369 | -55.41414 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 613030fd-ba5c-32a0-96b7-c1585243addd | -8.55618 | -54.85587 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdb8f4e8-41d8-3c50-94ce-fe56c9b80b72 | -8.52483 | -55.32261 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6caac0d-c970-302d-a8b6-51a570ec502e | -8.09365 | -51.66213 | 2026-08-22 05:23:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bcddd998-76e8-3f9e-845a-7cd2649623e2 | -6.89894 | -55.72031 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb404be0-8920-3400-8653-97147357c793 | -4.94069 | -55.7832 | 2026-08-22 05:23:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad282b10-89bf-336e-ac7b-aebacc645c05 | -6.79869 | -59.41211 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6fc0cc7d-33c6-363a-83fc-48b35176b897 | -12.09875 | -56.32137 | 2026-08-22 05:23:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 1a92b2d5-f47f-3af7-938b-b7bc99e1c111 | -6.3705 | -54.94209 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5558d3b3-ea25-38c0-b282-a9d86fbeb651 | -6.80641 | -59.42753 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 60028cb5-2ec6-35f6-8c53-20c6461df7e3 | -6.37717 | -56.10179 | 2026-08-22 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63371635-7d63-3476-925e-45ccbede7a69 | -6.69746 | -58.93477 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9db5e55-018d-317a-ba8a-341ba015f07d | -6.7738 | -58.66587 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb23c88b-aa7d-3211-ad93-15e7ce82e847 | -13.69213 | -51.84753 | 2026-08-22 05:23:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 393fe61d-03ff-3abd-9ab2-77a635a00e18 | -6.72095 | -48.11609 | 2026-08-22 05:23:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 52437f4f-ba19-39c9-82bd-81b4fc840687 | -8.59633 | -54.68831 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4df10c6e-a65b-3bbe-9ef4-8bd1e2d0a673 | -8.54099 | -54.82976 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 681a5acf-95fb-32e9-9ce4-27a29da19e76 | -7.01463 | -59.54976 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 011909a1-3219-3622-8c1f-06a9a0852069 | -8.53181 | -55.32864 | 2026-08-22 05:23:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 27c7c761-04f9-30c6-ad4d-eba28282d996 | -6.9343 | -59.30603 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e5cd3e5e-04c3-3f54-b31f-ce70692ef097 | -4.45741 | -55.55385 | 2026-08-22 05:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02568c52-560a-3c7b-9b38-cd15aedf8463 | -6.76549 | -58.65386 | 2026-08-22 05:23:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 30823824-f74a-37fc-9014-d4187e848a2a | -8.58634 | -54.78675 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 571f42b5-3423-30fe-b5b0-0b316db25bc7 | -6.79097 | -59.41798 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.7 |
| 86b6a16b-5b62-3b1b-8ff8-fad19c731c99 | -14.14291 | -48.06929 | 2026-08-22 05:23:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f822719-fb0d-3fb9-af9f-748b93e788dd | -2.44955 | -48.56146 | 2026-08-22 05:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4bb2b262-7fa8-3144-ab2b-b1c2b2e10433 | -6.80596 | -59.66537 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 502b7525-eaa1-37f3-93bc-5294b257b04b | -6.90183 | -58.9958 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8c8172b-b50f-3769-8903-58497aaf0429 | -6.09433 | -59.95181 | 2026-08-22 05:23:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4121ed67-dadc-3a8e-be01-81a66999f186 | -8.53931 | -54.81365 | 2026-08-22 05:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 209ce700-8d45-3c68-96af-6ad56a827db7 | -6.81037 | -59.65896 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75592e1f-1a15-3e32-9f78-42bf94a6da07 | -6.81976 | -59.66402 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a5b7c41e-ac2a-39da-9224-cb06822ba4a0 | -2.50309 | -48.13501 | 2026-08-22 05:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6cf94920-c0ae-3742-8ce6-a373c23a3dc0 | -6.42876 | -52.71611 | 2026-08-22 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2508d80e-6671-340b-8366-cd0eab17999c | -6.57152 | -58.979 | 2026-08-22 05:23:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0597e22-cf1a-3d01-8a7e-9951cfe42955 | -6.97698 | -58.32134 | 2026-08-22 05:23:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1e829e43-8d84-3ad9-bcfd-392e3de5c8d8 | -2.89805 | -48.80072 | 2026-08-22 05:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README63.md)
